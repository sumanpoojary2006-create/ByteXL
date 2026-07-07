#!/usr/bin/env python3
"""
ByteXL Image Uploader
Automatically upload images to a topic and get markdown links.

Commands:
    python3 upload_images.py list                                      # List all chapters/topics
    python3 upload_images.py push --topic "Variables" --md topic.md   # Upload images + output final markdown
    python3 upload_images.py upload --topic "Variables" --images ./images/  # Upload images only
"""

import argparse
import json
import re
import sys
import requests
from pathlib import Path

# ── Config ──────────────────────────────────────────────────────────────────
BASE_URL        = "https://bytexl.app"
READING_ID      = "44sqshkgw"   # Modern Python Programming
TOKEN           = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI0NHNqbjltZHYiLCJlbWFpbCI6InN1bWFuLnBvb2phcnlAYnl0ZXhsLmluIiwiaWF0IjoxNzgyODg4ODk0fQ.U0UHKY9USSwMNG8YPxrqOD7MNj6VV7YMP8H3BH-8rZ0"
CONFIG_FILE     = Path(__file__).parent / "bytexl_config.json"
SUPPORTED_EXT   = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}
# ────────────────────────────────────────────────────────────────────────────


def get_token() -> str:
    if CONFIG_FILE.exists():
        cfg = json.loads(CONFIG_FILE.read_text())
        if cfg.get("token"):
            return cfg["token"]
    return TOKEN


def auth_headers() -> dict:
    return {"Authorization": f"Bearer {get_token()}"}


def fetch_topics(reading_id: str):
    """Return flat list of {_id, title, chapter} for every page in the reading material."""
    url = f"{BASE_URL}/api/content/{reading_id}?includeDraft=true"
    resp = requests.get(url, headers=auth_headers())
    resp.raise_for_status()
    data = resp.json()["data"]
    topics = []
    for section in data.get("contentSections", []):
        chapter = section["title"]
        for page in section.get("contentPages", []):
            topics.append({"_id": page["_id"], "title": page["title"].strip(), "chapter": chapter})
    return topics


def find_topic(name: str, topics: list):
    name_lower = name.lower()
    # Exact match first
    for t in topics:
        if t["title"].lower() == name_lower:
            return t
    # Partial match
    for t in topics:
        if name_lower in t["title"].lower():
            return t
    return None


def upload_image(file_path: Path, topic_id: str):
    with open(file_path, "rb") as f:
        resp = requests.post(
            f"{BASE_URL}/api/upload/s3",
            data={"upload_file_type": "content", "upload_file_subtype": topic_id},
            files={"upload_file": (file_path.name, f, _mime(file_path))},
            headers=auth_headers(),
        )
    resp.raise_for_status()
    result = resp.json()
    if result.get("status") == "success" and result.get("url"):
        return result["url"]
    print(f"  API error: {result}", file=sys.stderr)
    return None


def _mime(path: Path) -> str:
    return {
        ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
        ".gif": "image/gif", ".webp": "image/webp", ".svg": "image/svg+xml",
    }.get(path.suffix.lower(), "application/octet-stream")


def collect_images(path_arg: str):
    p = Path(path_arg)
    if p.is_file():
        return [p]
    if p.is_dir():
        return sorted(f for f in p.iterdir() if f.is_file() and f.suffix.lower() in SUPPORTED_EXT)
    print(f"ERROR: '{path_arg}' not found.", file=sys.stderr)
    sys.exit(1)


# ── Commands ─────────────────────────────────────────────────────────────────

def cmd_list(args):
    print(f"\nFetching topics for reading: {READING_ID}...\n")
    topics = fetch_topics(READING_ID)
    current_chapter = None
    for t in topics:
        if t["chapter"] != current_chapter:
            current_chapter = t["chapter"]
            print(f"\n📚 {current_chapter}")
        print(f"   [{t['_id']}]  {t['title']}")
    print()


def cmd_upload(args):
    topics = fetch_topics(READING_ID)

    # Resolve topic ID
    if args.topic_id:
        topic_id = args.topic_id
        topic_title = args.topic_id
    elif args.topic:
        match = find_topic(args.topic, topics)
        if not match:
            print(f"ERROR: No topic found matching '{args.topic}'.")
            print("Run 'python3 upload_images.py list' to see all topics.")
            sys.exit(1)
        topic_id = match["_id"]
        topic_title = match["title"]
        print(f"Topic matched: [{topic_id}] {topic_title}")
    else:
        print("ERROR: Provide --topic 'Title' or --topic-id ID")
        sys.exit(1)

    images = collect_images(args.images)
    if not images:
        print("No supported images found.")
        sys.exit(1)

    print(f"\nUploading {len(images)} image(s)...\n")
    results = []
    for img in images:
        print(f"  {img.name} ... ", end="", flush=True)
        url = upload_image(img, topic_id)
        if url:
            md = f"![]({url})"
            print("✓")
            results.append((img.name, md))
        else:
            print("FAILED")

    print("\n" + "─" * 60)
    print("MARKDOWN LINKS — paste directly into the editor:\n")
    for name, md in results:
        print(f"# {name}")
        print(md)
        print()


def cmd_push(args):
    """Upload all images referenced in a markdown file and output the rewritten markdown."""
    md_path = Path(args.md)
    if not md_path.exists():
        print(f"ERROR: '{args.md}' not found.")
        sys.exit(1)

    topics = fetch_topics(READING_ID)

    # Resolve topic ID
    if args.topic_id:
        topic_id = args.topic_id
        topic_title = args.topic_id
    elif args.topic:
        match = find_topic(args.topic, topics)
        if not match:
            print(f"ERROR: No topic found matching '{args.topic}'.")
            print("Run 'python3 upload_images.py list' to see all topics.")
            sys.exit(1)
        topic_id = match["_id"]
        topic_title = match["title"]
        print(f"Topic: [{topic_id}] {topic_title}\n", file=sys.stderr)
    else:
        print("ERROR: Provide --topic 'Title' or --topic-id ID")
        sys.exit(1)

    content = md_path.read_text(encoding="utf-8")

    # Find all local image references: ![alt](path)  — skip http/https URLs
    image_refs = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', content)
    local_refs = [(alt, path) for alt, path in image_refs if not path.startswith("http")]

    if not local_refs:
        print("No local image references found in the markdown. Nothing to upload.", file=sys.stderr)
        print(content)
        return

    print(f"Found {len(local_refs)} local image(s) to upload...\n", file=sys.stderr)

    # Upload each unique local image path
    url_map = {}  # local_path → s3_url
    md_dir = md_path.parent

    for alt, local_path in local_refs:
        if local_path in url_map:
            continue  # already uploaded

        img_file = (md_dir / local_path).resolve()
        if not img_file.exists():
            print(f"  WARNING: '{local_path}' not found, skipping.", file=sys.stderr)
            url_map[local_path] = None
            continue

        print(f"  Uploading: {img_file.name} ...", end="", flush=True, file=sys.stderr)
        url = upload_image(img_file, topic_id)
        if url:
            url_map[local_path] = url
            print(" ✓", file=sys.stderr)
        else:
            url_map[local_path] = None
            print(" FAILED", file=sys.stderr)

    # Rewrite markdown — replace local paths with S3 URLs
    def replace_image(m):
        alt = m.group(1)
        path = m.group(2)
        if path.startswith("http"):
            return m.group(0)
        s3_url = url_map.get(path)
        if s3_url:
            return f"![]({s3_url})"
        return m.group(0)  # leave unchanged if upload failed

    rewritten = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', replace_image, content)

    # Write to output file or print
    if args.output:
        out_path = Path(args.output)
        out_path.write_text(rewritten, encoding="utf-8")
        print(f"\nSaved to: {out_path}", file=sys.stderr)
    else:
        print("\n" + "─" * 60, file=sys.stderr)
        print("FINAL MARKDOWN (copy and paste into ByteXL editor):\n", file=sys.stderr)
        print(rewritten)


def cmd_set_token(args):
    cfg = {}
    if CONFIG_FILE.exists():
        cfg = json.loads(CONFIG_FILE.read_text())
    cfg["token"] = args.token.strip()
    CONFIG_FILE.write_text(json.dumps(cfg, indent=2))
    print(f"Token saved to {CONFIG_FILE}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="ByteXL Image Uploader")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("list", help="List all chapters and topics with their IDs")

    ps = sub.add_parser("push", help="Upload images in a markdown file and output rewritten markdown")
    ps.add_argument("--md", required=True, help="Path to your markdown file")
    ps.add_argument("--topic", help="Topic title (fuzzy match)")
    ps.add_argument("--topic-id", help="Topic ID directly (e.g. 44t7vzund)")
    ps.add_argument("--output", "-o", help="Save rewritten markdown to this file instead of printing")

    up = sub.add_parser("upload", help="Upload images to a topic")
    up.add_argument("--topic", help="Topic title (fuzzy match)")
    up.add_argument("--topic-id", help="Topic ID directly (e.g. 44t7vzund)")
    up.add_argument("--images", required=True, help="Image file or folder of images")

    st = sub.add_parser("set-token", help="Save a new auth token")
    st.add_argument("token", help="New Bearer token value")

    args = parser.parse_args()

    if args.command == "push":
        cmd_push(args)
    elif args.command == "list":
        cmd_list(args)
    elif args.command == "upload":
        cmd_upload(args)
    elif args.command == "set-token":
        cmd_set_token(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
