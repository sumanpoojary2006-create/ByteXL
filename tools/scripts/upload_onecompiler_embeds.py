#!/usr/bin/env python3
"""
Bulk-upload generated OneCompiler wrapper pages to ByteXL S3 and rewrite the
converted markdown to use the returned public URLs.

Run this after generate_onecompiler_embeds.py. It is intentionally separate so
you can inspect the generated files before uploading them.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CONFIG_FILE = ROOT / "bytexl_config.json"
DEFAULT_BASE_URL = "https://bytexl.app"


def get_token(explicit: str | None) -> str:
    if explicit:
        return explicit.strip()

    env_token = os.environ.get("BYTEXL_TOKEN")
    if env_token:
        return env_token.strip()

    if CONFIG_FILE.exists():
        config = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
        if config.get("token"):
            return str(config["token"]).strip()

    legacy_token = legacy_script_token()
    if legacy_token:
        return legacy_token

    print(
        "ERROR: ByteXL token not found. Set BYTEXL_TOKEN or save bytexl_config.json with a token.",
        file=sys.stderr,
    )
    sys.exit(1)


def legacy_script_token() -> str | None:
    """Reuse the token already present in older local ByteXL helper scripts."""
    for script_name in ["upload_images.py", "batch_upload.py"]:
        script_path = ROOT / script_name
        if not script_path.exists():
            continue
        match = re.search(
            r'^\s*TOKEN\s*=\s*["\']([^"\']+)["\']',
            script_path.read_text(encoding="utf-8"),
            flags=re.MULTILINE,
        )
        if match and match.group(1).strip():
            return match.group(1).strip()
    return None


def upload_html(base_url: str, token: str, file_path: Path, subtype: str) -> str:
    import requests

    with file_path.open("rb") as handle:
        response = requests.post(
            f"{base_url.rstrip('/')}/api/upload/s3",
            data={"upload_file_type": "content", "upload_file_subtype": subtype},
            files={"upload_file": (file_path.name, handle, "text/html")},
            headers={"Authorization": f"Bearer {token}"},
            timeout=60,
        )
    response.raise_for_status()
    payload = response.json()
    if payload.get("status") == "success" and payload.get("url"):
        return payload["url"]
    raise RuntimeError(f"Upload failed for {file_path.name}: {payload}")


def rewrite_markdown(reading_dir: Path, output_dir: Path, url_map: dict[str, str]) -> int:
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    rewritten_files = 0
    for md_file in sorted(reading_dir.rglob("*.md")):
        rel = md_file.relative_to(reading_dir)
        target = output_dir / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        content = md_file.read_text(encoding="utf-8")
        original = content

        for snippet_id, public_url in url_map.items():
            content = re.sub(
                rf'src="[^"]*{re.escape(snippet_id)}\.html"',
                f'src="{public_url}"',
                content,
            )

        target.write_text(content, encoding="utf-8")
        if content != original:
            rewritten_files += 1

    return rewritten_files


def main() -> None:
    parser = argparse.ArgumentParser(description="Upload generated OneCompiler wrapper HTML files to ByteXL S3.")
    parser.add_argument("--build-dir", default=str(ROOT / ".onecompiler_build"), help="Build folder from generate_onecompiler_embeds.py.")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL, help="ByteXL base URL.")
    parser.add_argument("--token", default="", help="ByteXL JWT token. Prefer BYTEXL_TOKEN or bytexl_config.json.")
    parser.add_argument("--subtype", default="onecompiler-embeds", help="S3 upload subtype/folder.")
    parser.add_argument("--dry-run", action="store_true", help="Show what would upload without calling the API.")
    args = parser.parse_args()

    build_dir = Path(args.build_dir).expanduser().resolve()
    manifest_path = build_dir / "snippets.json"
    if not manifest_path.exists():
        print(f"ERROR: Missing manifest: {manifest_path}", file=sys.stderr)
        print("Run generate_onecompiler_embeds.py first.", file=sys.stderr)
        sys.exit(1)

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    snippets = manifest.get("snippets", [])
    embed_dir = build_dir / manifest.get("embed_dir", "onecompiler-embeds")
    reading_dir = build_dir / manifest.get("reading_dir", "reading-material")
    uploaded_reading_dir = build_dir / "reading-material-uploaded"
    upload_map_path = build_dir / "upload-map.json"

    if not snippets:
        print("No generated snippets found. Nothing to upload.")
        return

    if args.dry_run:
        print(f"DRY RUN: would upload {len(snippets)} HTML wrapper file(s) from {embed_dir}.")
        return

    token = get_token(args.token or None)
    url_map: dict[str, str] = {}

    for index, snippet in enumerate(snippets, 1):
        snippet_id = snippet["id"]
        html_file = embed_dir / f"{snippet_id}.html"
        if not html_file.exists():
            raise FileNotFoundError(f"Missing wrapper HTML: {html_file}")

        print(f"[{index}/{len(snippets)}] Uploading {html_file.name} ... ", end="", flush=True)
        url = upload_html(args.base_url, token, html_file, args.subtype)
        url_map[snippet_id] = url
        print("done")

    rewritten_files = rewrite_markdown(reading_dir, uploaded_reading_dir, url_map)

    upload_map = {
        "base_url": args.base_url,
        "subtype": args.subtype,
        "uploaded_count": len(url_map),
        "rewritten_markdown_files": rewritten_files,
        "urls": url_map,
    }
    upload_map_path.write_text(json.dumps(upload_map, indent=2), encoding="utf-8")

    print()
    print(f"Uploaded {len(url_map)} wrapper file(s).")
    print(f"Rewritten markdown folder: {uploaded_reading_dir}")
    print(f"Upload map: {upload_map_path}")


if __name__ == "__main__":
    main()
