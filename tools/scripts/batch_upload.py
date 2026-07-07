#!/usr/bin/env python3
"""
ByteXL Batch Image Uploader
Scans every markdown file, uploads local images, rewrites files in-place.
Run from the ByteXL folder: python3 batch_upload.py
"""

import re
import sys
import requests
from pathlib import Path

BASE_URL = "https://bytexl.app"
TOKEN    = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI0NHNqbjltZHYiLCJlbWFpbCI6InN1bWFuLnBvb2phcnlAYnl0ZXhsLmluIiwiaWF0IjoxNzgyODg4ODk0fQ.U0UHKY9USSwMNG8YPxrqOD7MNj6VV7YMP8H3BH-8rZ0"

# ── Known topic ID mapping (filename prefix → ByteXL topic _id) ──────────────
# Semester 1, Unit 1 - Introduction to Programming  [reading: 44sqshkgw]
TOPIC_MAP = {
    "Semester 1/Unit 1 - Introduction to Programming/01": "44t2h5tak",
    "Semester 1/Unit 1 - Introduction to Programming/02": "44t2he3ww",
    "Semester 1/Unit 1 - Introduction to Programming/03": "44t2hg268",
    "Semester 1/Unit 1 - Introduction to Programming/04": "44t2hgunm",
    "Semester 1/Unit 1 - Introduction to Programming/05": "44t2hhpwk",
    "Semester 1/Unit 1 - Introduction to Programming/06": "44t2hjg29",
    "Semester 1/Unit 1 - Introduction to Programming/07": "44t2hkagj",
    "Semester 1/Unit 1 - Introduction to Programming/08": "44t2hkxxy",
    "Semester 1/Unit 1 - Introduction to Programming/09": "44t2hky6v",
    # Unit 2 - Data Types and Operators
    "Semester 1/Unit 2 - Data Types and Operators/01": "44t7vzund",
    "Semester 1/Unit 2 - Data Types and Operators/02": "44t82usgz",
    "Semester 1/Unit 2 - Data Types and Operators/03": "44t82w7y6",
    "Semester 1/Unit 2 - Data Types and Operators/04": "44t82xext",
    "Semester 1/Unit 2 - Data Types and Operators/05": "44t82yggj",
    "Semester 1/Unit 2 - Data Types and Operators/06": "44t82zdka",
    "Semester 1/Unit 2 - Data Types and Operators/07": "44t8334sg",
    "Semester 1/Unit 2 - Data Types and Operators/08": "44t8348fj",
    "Semester 1/Unit 2 - Data Types and Operators/09": "44t8356mw",
    "Semester 1/Unit 2 - Data Types and Operators/10": "44t836kc7",
    # Unit 3 - Control Flow
    "Semester 1/Unit 3 - Control Flow/01": "44t8h2g6c",
    "Semester 1/Unit 3 - Control Flow/02": "44t8hdc6u",
    "Semester 1/Unit 3 - Control Flow/03": "44t8he64e",
    "Semester 1/Unit 3 - Control Flow/04": "44t8hgejq",
    "Semester 1/Unit 3 - Control Flow/05": "44t8hhawj",
    "Semester 1/Unit 3 - Control Flow/06": "44t8hm2bs",
    "Semester 1/Unit 3 - Control Flow/07": "44t8hn4ng",
    "Semester 1/Unit 3 - Control Flow/08": "44t8hnwp7",
    "Semester 1/Unit 3 - Control Flow/09": "44t8hpwft",
    # Unit 4 - Looping
    "Semester 1/Unit 4 - Looping/01": "44tb5j2kk",
    "Semester 1/Unit 4 - Looping/02": "44tb5k4ef",
    "Semester 1/Unit 4 - Looping/03": "44tb5kfd6",
    "Semester 1/Unit 4 - Looping/04": "44tb5m6t8",
    "Semester 1/Unit 4 - Looping/05": "44tb5mm6y",
    "Semester 1/Unit 4 - Looping/06": "44tb5n423",
    "Semester 1/Unit 4 - Looping/07": "44tb5ngqj",
    "Semester 1/Unit 4 - Looping/08": "44tb5nv3h",
}

SUPPORTED_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}
ROOT = Path(__file__).parent
# Content lives under <ByteXL>/content while scripts live under <ByteXL>/tools/scripts.
CONTENT_ROOT = ROOT.parent.parent / "content"


def auth_headers():
    return {"Authorization": f"Bearer {TOKEN}"}


def topic_id_for(md_path: Path) -> str:
    """Return the ByteXL topic ID or a slug derived from the file path."""
    rel = md_path.relative_to(CONTENT_ROOT)
    # Try prefix match (folder/NN)
    parts = rel.parts
    prefix_key = "/".join(parts[:-1]) + "/" + parts[-1][:2]
    for k, v in TOPIC_MAP.items():
        if prefix_key.startswith(k):
            return v
    # Fallback: slugify the unit folder name for unmapped units
    unit_folder = parts[1] if len(parts) > 2 else parts[0]
    slug = re.sub(r"[^a-z0-9]+", "-", unit_folder.lower()).strip("-")
    return slug[:40]


def mime(path: Path) -> str:
    return {
        ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
        ".gif": "image/gif", ".webp": "image/webp", ".svg": "image/svg+xml",
    }.get(path.suffix.lower(), "application/octet-stream")


def upload(file_path: Path, subtype: str):
    with open(file_path, "rb") as f:
        r = requests.post(
            f"{BASE_URL}/api/upload/s3",
            data={"upload_file_type": "content", "upload_file_subtype": subtype},
            files={"upload_file": (file_path.name, f, mime(file_path))},
            headers=auth_headers(),
        )
    r.raise_for_status()
    result = r.json()
    if result.get("status") == "success":
        return result["url"]
    return None


def process_file(md_path: Path, dry_run=False):
    content = md_path.read_text(encoding="utf-8")
    local_refs = [
        (alt, p) for alt, p in re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', content)
        if not p.startswith("http")
    ]
    if not local_refs:
        return 0

    subtype = topic_id_for(md_path)
    url_cache = {}
    changed = False

    for alt, local_path in local_refs:
        if local_path in url_cache:
            continue
        img_file = (md_path.parent / local_path).resolve()
        if not img_file.exists():
            print(f"    ⚠ missing: {local_path}")
            url_cache[local_path] = None
            continue

        if dry_run:
            print(f"    would upload: {img_file.name} → [{subtype}]")
            url_cache[local_path] = f"https://s3.example.com/{img_file.name}"
            continue

        print(f"    ↑ {img_file.name} ... ", end="", flush=True)
        url = upload(img_file, subtype)
        if url:
            url_cache[local_path] = url
            print("✓")
            changed = True
        else:
            url_cache[local_path] = None
            print("FAILED")

    if not any(url_cache.values()):
        return 0

    def replace_img(m):
        path = m.group(2)
        if path.startswith("http"):
            return m.group(0)
        url = url_cache.get(path)
        return f"![]({url})" if url else m.group(0)

    new_content = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', replace_img, content)

    if not dry_run and new_content != content:
        md_path.write_text(new_content, encoding="utf-8")

    return sum(1 for u in url_cache.values() if u)


def main():
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("DRY RUN — no files will be changed\n")

    md_files = sorted(CONTENT_ROOT.rglob("*.md"))
    total_uploaded = 0
    total_files = 0

    for md in md_files:
        # Skip script/readme files at root level
        if md.parent == CONTENT_ROOT:
            continue

        content = md.read_text(encoding="utf-8")
        local_imgs = [p for _, p in re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', content)
                      if not p.startswith("http")]
        if not local_imgs:
            continue

        rel = md.relative_to(ROOT)
        subtype = topic_id_for(md)
        mapped = subtype in TOPIC_MAP.values()
        label = "✓ mapped" if mapped else "~ slug"
        print(f"\n[{label}: {subtype}] {rel}")

        n = process_file(md, dry_run=dry_run)
        total_uploaded += n
        if n:
            total_files += 1

    print(f"\n{'─'*60}")
    print(f"Done. {total_uploaded} images uploaded across {total_files} files.")
    if dry_run:
        print("(dry run — re-run without --dry-run to apply)")


if __name__ == "__main__":
    main()
