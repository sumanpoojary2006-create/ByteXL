#!/usr/bin/env python3
"""
Audit Markdown reading material for durable OneCompiler iframe links.

The script is read-only. It flags iframe src values that point at ByteXL wrapper
apps/S3 HTML files instead of saved OneCompiler editor or Studio URLs.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import asdict, dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent.parent.parent
CONTENT_ROOT = ROOT / "content"


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    src: str
    status: str
    reason: str


class IframeParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.iframes: list[tuple[int, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "iframe":
            return
        values = {name.lower(): value for name, value in attrs if value is not None}
        src = values.get("src")
        if src:
            self.iframes.append((self.getpos()[0], src))


def markdown_files(paths: list[str]) -> list[Path]:
    selected = [Path(item).expanduser() for item in paths] if paths else [CONTENT_ROOT]
    files: list[Path] = []
    for path in selected:
        path = path if path.is_absolute() else ROOT / path
        if path.is_file() and path.suffix.lower() == ".md":
            files.append(path)
        elif path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
    return sorted(set(file.resolve() for file in files))


def classify_src(src: str) -> tuple[str, str]:
    parsed = urlparse(src)
    host = parsed.netloc.lower()
    path = parsed.path.strip("/")
    parts = path.split("/") if path else []

    if host.endswith("onecompiler.com"):
        if len(parts) >= 3 and parts[0] == "embed" and parts[1] == "studio":
            return "ok", "saved OneCompiler Studio workspace embed"
        if len(parts) >= 3 and parts[0] == "embed":
            return "ok", "saved OneCompiler code embed"
        if len(parts) >= 2 and parts[0] == "embed":
            return "warning", "generic OneCompiler embed without saved code ID"
        return "warning", "OneCompiler URL, but not a recognized saved embed"

    wrapper_hosts = {
        "image-converter-pi-rouge.vercel.app",
        "vercel-onecompiler-builder.vercel.app",
        "127.0.0.1:8765",
        "localhost:8765",
    }
    if host in wrapper_hosts or src.startswith("http://127.0.0.1:8765/embed.html"):
        return "needs_migration", "ByteXL wrapper app URL, not a saved OneCompiler link"

    if host == "s3.ap-south-1.amazonaws.com" and re.search(r"/onecompiler-embeds[^/]*/", parsed.path):
        return "needs_migration", "uploaded wrapper HTML, not a saved OneCompiler link"

    if "embed.html#" in src:
        return "needs_migration", "encoded wrapper URL, not a saved OneCompiler link"

    return "other", "iframe source is not recognized as a OneCompiler editor"


def scan_file(path: Path) -> list[Finding]:
    text = path.read_text(encoding="utf-8", errors="replace")
    parser = IframeParser()
    parser.feed(text)
    findings: list[Finding] = []
    try:
        display = str(path.relative_to(ROOT))
    except ValueError:
        display = str(path)

    for line, src in parser.iframes:
        status, reason = classify_src(src)
        findings.append(Finding(display, line, src, status, reason))
    return findings


def summarize(findings: list[Finding]) -> dict[str, int]:
    summary: dict[str, int] = {}
    for item in findings:
        summary[item.status] = summary.get(item.status, 0) + 1
    return dict(sorted(summary.items()))


def write_csv(path: Path, findings: list[Finding]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["file", "line", "src", "status", "reason"])
        writer.writeheader()
        for item in findings:
            writer.writerow(asdict(item))


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit reading-material iframe links.")
    parser.add_argument("paths", nargs="*", help="Markdown files or folders to scan. Defaults to content/.")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of a text summary.")
    parser.add_argument("--csv", default="", help="Write full findings to a CSV file.")
    parser.add_argument(
        "--fail-on-risk",
        action="store_true",
        help="Exit non-zero when needs_migration or warning findings are present.",
    )
    args = parser.parse_args()

    files = markdown_files(args.paths)
    findings: list[Finding] = []
    for path in files:
        findings.extend(scan_file(path))

    summary = summarize(findings)

    if args.csv:
        write_csv((Path(args.csv).expanduser() if args.csv else Path(args.csv)), findings)

    if args.json:
        print(json.dumps({"summary": summary, "findings": [asdict(item) for item in findings]}, indent=2))
    else:
        print("OneCompiler iframe audit")
        print(f"Markdown files scanned: {len(files)}")
        print(f"Iframes found: {len(findings)}")
        for status, count in summary.items():
            print(f"{status}: {count}")
        risky = [item for item in findings if item.status in {"needs_migration", "warning"}]
        if risky:
            print()
            print("First risky links:")
            for item in risky[:20]:
                print(f"- {item.file}:{item.line} [{item.status}] {item.reason}")

    if args.fail_on_risk and any(item.status in {"needs_migration", "warning"} for item in findings):
        return 1
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        sys.exit(0)
