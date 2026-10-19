#!/usr/bin/env python3
"""QC a published ByteXL course against its local markdown, and repair dead code editors.

    python3 qc_course.py scan   <readingId> <local content dir> [--run] [--unit N ...]
    python3 qc_course.py repair <readingId> <local content dir> [--apply]

scan checks every lesson on the platform:
  * every OneCompiler embed resolves (GET /api/posts/<id> is 200; a missing post renders "Not Found")
  * the embedded code is the same code as the local lesson (catches stale or hand-edited editors)
  * code blocks are all accounted for: embeds + static python fences == local python fences
  * a snippet OneCompiler cannot keep (IPv4 literal, dotted-host URL) never sits behind an embed
  * every image URL answers, no relative image path is left, no page is empty, no IMAGE PROMPT leaks
  * with --run, every local python snippet is executed and compared with its "Expected output" block

repair replaces each dead embed with a static python code block taken from the local lesson
(dry run unless --apply). The snippet stays readable with its expected output; it just cannot run.

OneCompiler answers 200 and a fresh id when it refuses to store a snippet, so an upload that only
checks the HTTP status publishes an embed that shows "Not Found" (reproduced 19 Oct 2026).
"""
import concurrent.futures as cf
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import defaultdict

import requests

CONVERTER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "image-converter")
for line in open(os.path.join(CONVERTER, ".env"), encoding="utf-8"):
    if "=" in line and not line.startswith("#"):
        k, v = line.strip().split("=", 1)
        os.environ.setdefault(k, v.strip("\"'"))
sys.path.insert(0, CONVERTER)
import server as srv  # noqa: E402

EMBED_RE = re.compile(r'<iframe\s[^>]*?src="https://onecompiler\.com/embed/([a-z0-9]+)/([A-Za-z0-9]+)"[^>]*>\s*</iframe>', re.S)
FENCE_RE = re.compile(r"```python[^\n]*\n(.*?)```", re.S)
IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)")
IPV4 = re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}\b")
URL = re.compile(r"""https?://[^\s"'`)]*\.[^\s"'`)]*""", re.I)


def unit_number(title):
    m = re.match(r"\s*(\d+)\s*-", title)
    return int(m.group(1)) if m else None


def local_files(content_dir, section_title):
    n = unit_number(section_title)
    dirs = glob.glob(os.path.join(content_dir, f"{n} - *"))
    if len(dirs) != 1:
        return []
    return sorted(glob.glob(os.path.join(dirs[0], "[0-9][0-9]*.md")))


def load(reading_id, content_dir, units=None):
    content = srv.fetch_content(reading_id)
    pages = []
    for section in content["contentSections"]:
        n = unit_number(section["title"])
        if units and n not in units:
            continue
        files = local_files(content_dir, section["title"])
        refs = section["contentPages"]
        if len(files) != len(refs):
            print(f"!! unit {n}: {len(refs)} pages on the platform but {len(files)} local files")
            continue
        for ref, path in zip(refs, files):
            pages.append((section["title"], ref, path))

    def get(item):
        return item, srv.fetch_content_page(item[1]["_id"])

    with cf.ThreadPoolExecutor(8) as ex:
        return list(ex.map(get, pages))


def post_json(code_id):
    r = requests.get(f"https://onecompiler.com/api/posts/{code_id}", timeout=30)
    return r.status_code, (r.json() if r.status_code == 200 else None)


def norm(code):
    return "\n".join(line.rstrip() for line in code.strip().splitlines())


# The OneCompiler sandbox runs Python 3.12; use the newest local interpreter so syntax matches.
PYTHON = shutil.which("python3.12") or shutil.which("python3.11") or os.path.expanduser("~/.local/bin/python3.11") or sys.executable


def run_snippet(code):
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "main.py")
        open(path, "w", encoding="utf-8").write(code)
        try:
            p = subprocess.run([PYTHON, "-I", path], capture_output=True, text=True, timeout=20, cwd=d)
        except subprocess.TimeoutExpired:
            return None, "timed out"
        return p.stdout, p.stderr.strip().splitlines()[-1] if p.returncode else ""


def expected_after(markdown, fence_end):
    m = re.match(r"\s*Expected output:\s*\n+```[a-z]*\n(.*?)```", markdown[fence_end:], re.S)
    return m.group(1) if m else None


def scan(reading_id, content_dir, run=False, units=None):
    findings = []
    stats = defaultdict(int)
    pages = load(reading_id, content_dir, units)
    embeds = []
    for (section, ref, path), page in pages:
        md = page.get("markdown") or ""
        label = f"{os.path.basename(os.path.dirname(path))} / {os.path.basename(path)}"
        stats["pages"] += 1
        if len(md.strip()) < 500:
            findings.append((label, "empty-or-tiny page", len(md)))
        if "IMAGE PROMPT" in md:
            findings.append((label, "IMAGE PROMPT comment published", ""))
        for img in IMG_RE.findall(md):
            if not img.startswith("http"):
                findings.append((label, "relative image path left in page", img))
        local = open(path, encoding="utf-8").read()
        local_blocks = FENCE_RE.findall(local)
        platform_embeds = EMBED_RE.findall(md)
        static_blocks = FENCE_RE.findall(md)
        if len(platform_embeds) + len(static_blocks) != len(local_blocks):
            findings.append((label, "code blocks do not add up",
                             f"{len(platform_embeds)} editors + {len(static_blocks)} static != {len(local_blocks)} local"))
        for lang, code_id in platform_embeds:
            embeds.append((label, ref["_id"], lang, code_id))
        if run:
            for m in FENCE_RE.finditer(local):
                out, err = run_snippet(m.group(1))
                want = expected_after(local, m.end())
                stats["snippets run"] += 1
                if err:
                    findings.append((label, "snippet fails when run", err))
                elif want is not None and out.strip() != want.strip():
                    findings.append((label, "output differs from Expected output", out.strip()[:80]))
    stats["editors"] = len(embeds)

    def check(e):
        label, pid, lang, code_id = e
        status, data = post_json(code_id)
        return e, status, data

    with cf.ThreadPoolExecutor(8) as ex:
        results = list(ex.map(check, embeds))
    by_page = defaultdict(list)
    for e, status, data in results:
        by_page[e[1]].append((e, status, data))
        if status != 200:
            findings.append((e[0], "editor shows Not Found", f"{e[2]}/{e[3]} -> HTTP {status}"))
    # compare embedded code with the local snippet of the same position
    for (section, ref, path), page in pages:
        local_blocks = FENCE_RE.findall(open(path, encoding="utf-8").read())
        md = page.get("markdown") or ""
        seq = [("embed", m.group(2)) if m.group(2) else ("static", None)
               for m in re.finditer(EMBED_RE.pattern + r"|```python[^\n]*\n.*?```", md, re.S)]
        if len(seq) != len(local_blocks):
            continue
        posts = {e[3]: (s, d) for e, s, d in by_page.get(ref["_id"], [])}
        label = f"{os.path.basename(os.path.dirname(path))} / {os.path.basename(path)}"
        for (kind, code_id), code in zip(seq, local_blocks):
            if kind != "embed":
                continue
            if IPV4.search(code) or URL.search(code):
                findings.append((label, "editor wraps a snippet OneCompiler cannot keep", code_id))
            status, data = posts.get(code_id, (None, None))
            if status == 200:
                files = (data.get("properties") or {}).get("files") or []
                main = files[0]["content"] if files else ""
                stats["editors compared"] += 1
                if norm(main) != norm(code):
                    findings.append((label, "editor code differs from the lesson", code_id))
    # images
    imgs = set()
    for (_, _, _), page in pages:
        imgs.update(i for i in IMG_RE.findall(page.get("markdown") or "") if i.startswith("http"))
    stats["images"] = len(imgs)

    def head(u):
        try:
            r = requests.get(u, timeout=30, stream=True)
            return u, r.status_code
        except requests.RequestException as exc:
            return u, str(exc)[:40]

    with cf.ThreadPoolExecutor(12) as ex:
        for u, s in ex.map(head, sorted(imgs)):
            if s != 200:
                findings.append(("(image)", "image does not load", f"{u} -> {s}"))
    print(dict(stats))
    print(f"{len(findings)} finding(s)")
    for f in findings:
        print("  -", " | ".join(str(x) for x in f))
    return findings


def repair(reading_id, content_dir, apply=False):
    pages = load(reading_id, content_dir)
    fixed = 0
    for (section, ref, path), page in pages:
        md = page.get("markdown") or ""
        local_blocks = FENCE_RE.findall(open(path, encoding="utf-8").read())
        matches = list(re.finditer(EMBED_RE.pattern + r"|```python[^\n]*\n.*?```", md, re.S))
        if len(matches) != len(local_blocks):
            continue
        dead = []
        for m, code in zip(matches, local_blocks):
            if m.group(2) and post_json(m.group(2))[0] != 200:
                dead.append((m, code))
        if not dead:
            continue
        new, pos = [], 0
        for m, code in dead:
            new.append(md[pos:m.start()])
            new.append("```python\n" + code.rstrip("\n") + "\n```")
            pos = m.end()
        new.append(md[pos:])
        label = f"{os.path.basename(os.path.dirname(path))} / {os.path.basename(path)}"
        print(f"{'FIX ' if apply else 'would fix '}{label}: {len(dead)} dead editor(s) -> static code")
        fixed += len(dead)
        if apply:
            page["markdown"] = "".join(new)
            srv.save_content_page(page)
    print(f"{fixed} editor(s) {'replaced' if apply else 'would be replaced'}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 3 or args[0] not in ("scan", "repair"):
        sys.exit(__doc__)
    cmd, rid, cdir = args[:3]
    flags = args[3:]
    units = None
    if "--unit" in flags:
        units = {int(x) for x in flags[flags.index("--unit") + 1:] if x.isdigit()}
    if cmd == "scan":
        sys.exit(1 if scan(rid, cdir, run="--run" in flags, units=units) else 0)
    repair(rid, cdir, apply="--apply" in flags)
