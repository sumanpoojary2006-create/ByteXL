#!/usr/bin/env python3
"""
Generate OneCompiler editor embeds for ByteXL reading material.

Default behavior is safe: source markdown files are not edited. Converted
markdown copies, wrapper HTML files, a JSON manifest, and a report are written
under .onecompiler_build/.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import html
import json
import os
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parent
# Content lives under <ByteXL>/content while scripts live under <ByteXL>/tools/scripts.
CONTENT_ROOT = ROOT.parent.parent / "content"
DEFAULT_OUTPUT = ROOT / ".onecompiler_build"
EMBED_DIR_NAME = "onecompiler-embeds"
READING_DIR_NAME = "reading-material"
DEFAULT_LOCAL_WRAPPER_URL = "http://127.0.0.1:8765/embed.html"

LANGUAGE_ALIASES = {
    "py": "python",
    "python3": "python",
    "python2": "python2",
    "js": "javascript",
    "node": "nodejs",
    "node.js": "nodejs",
    "ts": "typescript",
    "java": "java",
    "c": "c",
    "c++": "cpp",
    "cpp": "cpp",
    "cc": "cpp",
    "cxx": "cpp",
    "c#": "csharp",
    "cs": "csharp",
    "csharp": "csharp",
    "html": "html",
    "html5": "html",
    "php": "php",
    "rb": "ruby",
    "ruby": "ruby",
    "go": "go",
    "golang": "go",
    "rs": "rust",
    "rust": "rust",
    "kt": "kotlin",
    "kotlin": "kotlin",
    "scala": "scala",
    "swift": "swift",
    "r": "r",
    "perl": "perl",
    "pl": "perl",
    "bash": "bash",
    "shell": "bash",
    "sh": "sh",
    "sql": "mysql",
    "mysql": "mysql",
    "postgres": "postgresql",
    "postgresql": "postgresql",
    "sqlite": "sqlite",
    "mongodb": "mongodb",
    "mongo": "mongodb",
    "lua": "lua",
    "dart": "dart",
    "julia": "julia",
    "groovy": "groovy",
    "haskell": "haskell",
    "hs": "haskell",
    "clojure": "clojure",
    "ex": "elixir",
    "elixir": "elixir",
    "erl": "erlang",
    "erlang": "erlang",
    "fsharp": "fsharp",
    "fs": "fsharp",
    "vb": "vb",
    "v": "v",
    "zig": "zig",
    "nim": "nim",
    "pascal": "pascal",
    "fortran": "fortran",
    "cobol": "cobol",
    "racket": "racket",
    "scheme": "scheme",
    "tcl": "tcl",
    "awk": "awk",
    "matplotlib": "matplotlib",
    "seaborn": "seaborn",
    "tkinter": "tkinter",
    "pygame": "pygame",
}

ONECOMPILER_LANGUAGES = {
    "ada",
    "assembly",
    "awk",
    "bash",
    "basic",
    "c",
    "clojure",
    "cobol",
    "coffeescript",
    "commonlisp",
    "cpp",
    "crystal",
    "csharp",
    "d",
    "dart",
    "deno",
    "elixir",
    "erlang",
    "forth",
    "fortran",
    "fsharp",
    "go",
    "groovy",
    "haskell",
    "haxe",
    "html",
    "java",
    "javascript",
    "jshell",
    "julia",
    "kotlin",
    "lua",
    "matplotlib",
    "mongodb",
    "mysql",
    "nim",
    "nodejs",
    "objectivec",
    "ocaml",
    "octave",
    "pascal",
    "perl",
    "php",
    "postgresql",
    "prolog",
    "pygame",
    "python",
    "python2",
    "r",
    "racket",
    "ruby",
    "rust",
    "scala",
    "scheme",
    "seaborn",
    "sh",
    "sqlite",
    "swift",
    "tcl",
    "tkinter",
    "typescript",
    "v",
    "vb",
    "zig",
}

DEFAULT_SKIP_LANGUAGES = {
    "csv",
    "diff",
    "ini",
    "json",
    "markdown",
    "md",
    "mermaid",
    "output",
    "plain",
    "plaintext",
    "console",
    "text",
    "toml",
    "traceback",
    "xml",
    "yaml",
    "yml",
}

FILE_EXTENSIONS = {
    "bash": "sh",
    "c": "c",
    "cpp": "cpp",
    "csharp": "cs",
    "go": "go",
    "html": "html",
    "java": "java",
    "javascript": "js",
    "kotlin": "kt",
    "mysql": "sql",
    "nodejs": "js",
    "php": "php",
    "postgresql": "sql",
    "python": "py",
    "python2": "py",
    "r": "r",
    "ruby": "rb",
    "rust": "rs",
    "scala": "scala",
    "sh": "sh",
    "sqlite": "sql",
    "swift": "swift",
    "typescript": "ts",
}


@dataclass(frozen=True)
class FencedBlock:
    start: int
    end: int
    start_line: int
    end_line: int
    info: str
    code: str


def slugify(value: str, max_len: int = 90) -> str:
    value = value.replace(os.sep, "/")
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    return value[:max_len].strip("-") or "snippet"


def normalize_language(info: str) -> str | None:
    token = (info or "").strip().split(maxsplit=1)[0] if info.strip() else ""
    token = token.strip("{}").strip(".").lower()
    token = token.removeprefix("language-")
    if not token:
        return None
    return LANGUAGE_ALIASES.get(token, token)


def filename_for(language: str, index: int) -> str:
    extension = FILE_EXTENSIONS.get(language, language)
    if language == "java":
        return "Main.java"
    return f"main_{index:03d}.{extension}"


def find_markdown_files(inputs: Iterable[str]) -> list[Path]:
    ignored_dirs = {
        ".git",
        ".onecompiler_build",
        "__pycache__",
        "node_modules",
    }
    files: list[Path] = []
    paths = [Path(item).expanduser() for item in inputs]
    if not paths:
        paths = [CONTENT_ROOT]

    for path in paths:
        path = path if path.is_absolute() else CONTENT_ROOT / path
        if path.is_file() and path.suffix.lower() == ".md":
            files.append(path.resolve())
        elif path.is_dir():
            for candidate in path.rglob("*.md"):
                if ignored_dirs.intersection(candidate.relative_to(path).parts):
                    continue
                files.append(candidate.resolve())

    return sorted(set(files))


def iter_fenced_blocks(markdown: str) -> list[FencedBlock]:
    lines = markdown.splitlines(keepends=True)
    offsets: list[int] = []
    pos = 0
    for line in lines:
        offsets.append(pos)
        pos += len(line)

    blocks: list[FencedBlock] = []
    i = 0
    while i < len(lines):
        start_match = re.match(r"^[ \t]{0,3}(`{3,}|~{3,})([^\r\n]*)", lines[i])
        if not start_match:
            i += 1
            continue

        fence = start_match.group(1)
        fence_char = fence[0]
        fence_len = len(fence)
        info = start_match.group(2).strip()
        close_re = re.compile(rf"^[ \t]{{0,3}}{re.escape(fence_char)}{{{fence_len},}}[ \t]*\r?\n?$")

        j = i + 1
        while j < len(lines) and not close_re.match(lines[j]):
            j += 1
        if j >= len(lines):
            i += 1
            continue

        code_start = offsets[i] + len(lines[i])
        code_end = offsets[j]
        block_end = offsets[j] + len(lines[j])
        blocks.append(
            FencedBlock(
                start=offsets[i],
                end=block_end,
                start_line=i + 1,
                end_line=j + 1,
                info=info,
                code=markdown[code_start:code_end],
            )
        )
        i = j + 1

    return blocks


def iframe_html(src: str, height: str) -> str:
    safe_src = html.escape(src, quote=True)
    safe_height = html.escape(height, quote=True)
    return (
        "<iframe\n"
        ' frameBorder="0"\n'
        f' height="{safe_height}"\n'
        f' src="{safe_src}"\n'
        ' width="100%"\n'
        "></iframe>\n"
    )


def wrapper_html(snippet: dict) -> str:
    data = json.dumps(snippet, ensure_ascii=False).replace("<", "\\u003c")
    language = html.escape(snippet["language"], quote=True)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(snippet["title"])}</title>
  <style>
    html, body {{
      width: 100%;
      height: 100%;
      margin: 0;
      overflow: hidden;
      background: #ffffff;
    }}
    iframe {{
      display: block;
      width: 100%;
      height: 100vh;
      border: 0;
    }}
  </style>
</head>
<body>
  <iframe id="oc-editor" title="OneCompiler {language} editor" allow="clipboard-read; clipboard-write"></iframe>
  <script id="snippet-data" type="application/json">{data}</script>
  <script>
    const snippet = JSON.parse(document.getElementById("snippet-data").textContent);
    const editor = document.getElementById("oc-editor");
    const params = new URLSearchParams({{
      hideNew: "true",
      hideTitle: "true",
      hideLanguageSelection: "true",
      listenToEvents: "true"
    }});

    editor.src = `https://onecompiler.com/embed/${{encodeURIComponent(snippet.language)}}?${{params.toString()}}`;

    function populateCode() {{
      if (!editor.contentWindow) return;
      editor.contentWindow.postMessage({{
        eventType: "populateCode",
        language: snippet.language,
        files: [{{
          name: snippet.filename,
          content: snippet.code
        }}]
      }}, "https://onecompiler.com");
    }}

    editor.addEventListener("load", () => {{
      populateCode();
      setTimeout(populateCode, 600);
      setTimeout(populateCode, 1500);
    }});
  </script>
</body>
</html>
"""


def encoded_wrapper_src(snippet: dict, wrapper_url: str) -> str:
    payload = {
        "title": snippet["title"],
        "language": snippet["language"],
        "filename": snippet["filename"],
        "code": snippet["code"],
    }
    raw = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    token = base64.urlsafe_b64encode(raw).decode("ascii").rstrip("=")
    return f"{wrapper_url.split('#', 1)[0]}#{token}"


def public_src_for(embed_file: Path, converted_md: Path, public_base_url: str | None) -> str:
    if public_base_url:
        return f"{public_base_url.rstrip('/')}/{embed_file.name}"
    return os.path.relpath(embed_file, converted_md.parent).replace(os.sep, "/")


def clean_output_dirs(output_dir: Path) -> None:
    for child in [output_dir / EMBED_DIR_NAME, output_dir / READING_DIR_NAME]:
        if child.exists():
            shutil.rmtree(child)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / EMBED_DIR_NAME).mkdir(parents=True, exist_ok=True)
    (output_dir / READING_DIR_NAME).mkdir(parents=True, exist_ok=True)


def should_convert(
    language: str | None,
    code: str,
    *,
    convert_unlabeled: bool,
    default_language: str,
    include_languages: set[str] | None,
    skip_languages: set[str],
) -> tuple[bool, str | None, str]:
    if not code.strip():
        return False, language, "empty"

    if language is None:
        if not convert_unlabeled:
            return False, language, "unlabeled"
        language = default_language

    if language in skip_languages:
        return False, language, "skipped-language"

    if include_languages is not None and language not in include_languages:
        return False, language, "not-in-include-list"

    if language not in ONECOMPILER_LANGUAGES:
        return False, language, "unsupported-language"

    return True, language, "converted"


def parse_csv_set(value: str) -> set[str]:
    return {item.strip().lower() for item in value.split(",") if item.strip()}


def build_report(summary: dict, files: list[dict], skipped: list[dict]) -> str:
    lines = [
        "# OneCompiler Embed Conversion Report",
        "",
        "## Summary",
        "",
        f"- Embed strategy: {summary['embed_strategy']}",
        f"- Wrapper URL: {summary['wrapper_url'] or '(not set)'}",
        f"- Markdown files scanned: {summary['files_scanned']}",
        f"- Markdown files changed: {summary['files_changed']}",
        f"- Code editors generated: {summary['snippets_generated']}",
        f"- Blocks skipped: {summary['blocks_skipped']}",
        "",
        "## Languages Converted",
        "",
    ]

    if summary["languages"]:
        for language, count in sorted(summary["languages"].items()):
            lines.append(f"- {language}: {count}")
    else:
        lines.append("- None")

    lines.extend(["", "## Changed Files", ""])
    if files:
        lines.append("| File | Editors |")
        lines.append("|---|---:|")
        for item in files:
            lines.append(f"| `{item['source_file']}` | {item['converted_blocks']} |")
    else:
        lines.append("No files were changed.")

    lines.extend(["", "## Skipped Blocks", ""])
    if skipped:
        lines.append("| File | Lines | Language | Reason |")
        lines.append("|---|---:|---|---|")
        for item in skipped[:500]:
            language = item.get("language") or "(none)"
            lines.append(
                f"| `{item['source_file']}` | {item['start_line']}-{item['end_line']} | "
                f"`{language}` | {item['reason']} |"
            )
        if len(skipped) > 500:
            lines.append(f"| ... | ... | ... | {len(skipped) - 500} more skipped blocks omitted |")
    else:
        lines.append("No skipped blocks.")

    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate OneCompiler embeds from Markdown code fences.")
    parser.add_argument("inputs", nargs="*", help="Markdown files or folders to scan. Defaults to this workspace.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Build output folder.")
    parser.add_argument("--public-base-url", default="", help="Public URL where generated wrapper HTML files will be hosted.")
    parser.add_argument(
        "--embed-strategy",
        choices=["wrapper-files", "encoded-url"],
        default="wrapper-files",
        help="wrapper-files creates one HTML file per snippet. encoded-url uses one hosted wrapper URL with code in the URL hash.",
    )
    parser.add_argument(
        "--wrapper-url",
        default="",
        help="Public URL of onecompiler_embed_wrapper.html. Required for --embed-strategy encoded-url.",
    )
    parser.add_argument("--height", default="350px", help="Outer iframe height.")
    parser.add_argument("--default-language", default="python", help="Language to use with --convert-unlabeled.")
    parser.add_argument("--convert-unlabeled", action="store_true", help="Convert unlabeled code fences using --default-language.")
    parser.add_argument(
        "--include-languages",
        default="",
        help="Comma-separated OneCompiler languages to convert. Empty means all supported languages.",
    )
    parser.add_argument(
        "--skip-languages",
        default=",".join(sorted(DEFAULT_SKIP_LANGUAGES)),
        help="Comma-separated languages to skip.",
    )
    parser.add_argument("--in-place", action="store_true", help="Rewrite source markdown files in place.")
    parser.add_argument("--no-backup", action="store_true", help="Do not create .bak.onecompiler backups with --in-place.")
    parser.add_argument("--write-all", action="store_true", help="Write unchanged markdown copies to the output folder too.")
    args = parser.parse_args()

    output_dir = (Path(args.output).expanduser() if args.output else DEFAULT_OUTPUT).resolve()
    public_base_url = args.public_base_url.strip() or None
    wrapper_url = args.wrapper_url.strip()
    if args.embed_strategy == "encoded-url" and not wrapper_url:
        wrapper_url = DEFAULT_LOCAL_WRAPPER_URL
    include_languages = parse_csv_set(args.include_languages) if args.include_languages.strip() else None
    skip_languages = parse_csv_set(args.skip_languages)
    default_language = normalize_language(args.default_language) or args.default_language

    markdown_files = find_markdown_files(args.inputs)
    clean_output_dirs(output_dir)

    snippets: list[dict] = []
    changed_files: list[dict] = []
    skipped_blocks: list[dict] = []
    language_counts: dict[str, int] = {}

    embed_dir = output_dir / EMBED_DIR_NAME
    reading_dir = output_dir / READING_DIR_NAME

    for md_path in markdown_files:
        rel_path = md_path.relative_to(CONTENT_ROOT)
        original = md_path.read_text(encoding="utf-8")
        blocks = iter_fenced_blocks(original)
        replacements: list[tuple[int, int, str]] = []
        converted_count = 0
        file_block_index = 0

        converted_md_path = reading_dir / rel_path
        converted_md_path.parent.mkdir(parents=True, exist_ok=True)

        for block in blocks:
            raw_language = normalize_language(block.info)
            convert, language, reason = should_convert(
                raw_language,
                block.code,
                convert_unlabeled=args.convert_unlabeled,
                default_language=default_language,
                include_languages=include_languages,
                skip_languages=skip_languages,
            )
            if not convert:
                skipped_blocks.append(
                    {
                        "source_file": str(rel_path),
                        "start_line": block.start_line,
                        "end_line": block.end_line,
                        "language": language,
                        "reason": reason,
                    }
                )
                continue

            assert language is not None
            file_block_index += 1
            converted_count += 1
            digest = hashlib.sha1(
                f"{rel_path.as_posix()}:{block.start_line}:{block.code}".encode("utf-8")
            ).hexdigest()[:10]
            snippet_id = f"{slugify(rel_path.with_suffix('').as_posix(), 78)}-{file_block_index:03d}-{digest}"
            embed_file = embed_dir / f"{snippet_id}.html"
            title = f"{rel_path.stem} code {file_block_index}"

            snippet = {
                "id": snippet_id,
                "title": title,
                "language": language,
                "filename": filename_for(language, file_block_index),
                "code": block.code.rstrip("\n"),
                "source_file": str(rel_path),
                "start_line": block.start_line,
                "end_line": block.end_line,
                "embed_file": str(embed_file.relative_to(output_dir)),
            }

            if args.embed_strategy == "encoded-url":
                src = encoded_wrapper_src(snippet, wrapper_url)
            else:
                embed_file.write_text(wrapper_html(snippet), encoding="utf-8")
                src = public_src_for(embed_file, converted_md_path, public_base_url)
            replacements.append((block.start, block.end, iframe_html(src, args.height)))
            snippet_meta = {key: value for key, value in snippet.items() if key != "code"} | {
                "sha1": digest,
                "src_length": len(src),
            }
            snippets.append(snippet_meta)
            language_counts[language] = language_counts.get(language, 0) + 1

        converted = original
        for start, end, replacement in reversed(replacements):
            converted = converted[:start] + replacement + converted[end:]

        if converted_count or args.write_all:
            if args.in_place:
                if converted != original:
                    if not args.no_backup:
                        backup = md_path.with_suffix(md_path.suffix + ".bak.onecompiler")
                        backup.write_text(original, encoding="utf-8")
                    md_path.write_text(converted, encoding="utf-8")
            else:
                converted_md_path.write_text(converted, encoding="utf-8")

        if converted_count:
            changed_files.append(
                {
                    "source_file": str(rel_path),
                    "converted_file": str(converted_md_path.relative_to(output_dir)),
                    "converted_blocks": converted_count,
                }
            )

    summary = {
        "embed_strategy": args.embed_strategy,
        "wrapper_url": wrapper_url if args.embed_strategy == "encoded-url" else public_base_url,
        "files_scanned": len(markdown_files),
        "files_changed": len(changed_files),
        "snippets_generated": len(snippets),
        "blocks_skipped": len(skipped_blocks),
        "languages": language_counts,
    }

    manifest = {
        "summary": summary,
        "output_dir": str(output_dir),
        "embed_dir": EMBED_DIR_NAME,
        "reading_dir": READING_DIR_NAME,
        "public_base_url": public_base_url,
        "snippets": snippets,
        "changed_files": changed_files,
        "skipped_blocks": skipped_blocks,
    }
    (output_dir / "snippets.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    (output_dir / "report.md").write_text(build_report(summary, changed_files, skipped_blocks), encoding="utf-8")

    print(f"Scanned {summary['files_scanned']} markdown files.")
    print(f"Generated {summary['snippets_generated']} OneCompiler editor wrapper(s).")
    print(f"Changed markdown copies: {summary['files_changed']}.")
    print(f"Report: {output_dir / 'report.md'}")
    if args.embed_strategy == "encoded-url":
        print(f"Final markdown uses wrapper URL: {wrapper_url}")
        if wrapper_url == DEFAULT_LOCAL_WRAPPER_URL:
            print("Note: replace the local wrapper URL with a public hosted /embed.html URL before students use it.")
    elif not public_base_url:
        print("Next: host or upload the generated onecompiler-embeds HTML files, then update iframe src values.")


if __name__ == "__main__":
    main()
