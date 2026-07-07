import io
import os
import posixpath
import re
import zipfile
from difflib import SequenceMatcher
from pathlib import Path, PurePosixPath
from typing import Any, Optional
from urllib.parse import unquote

import requests
from fastapi import Body, FastAPI, File, Form, HTTPException, Response, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse, StreamingResponse

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition", "X-Stats"],
)

BYTEXL_UPLOAD_URL = os.getenv("BYTEXL_UPLOAD_URL", "https://bytexl.app/api/upload/s3")
BYTEXL_API_BASE = os.getenv("BYTEXL_API_BASE", "https://bytexl.app").rstrip("/")
DEFAULT_READING_ID = os.getenv("BYTEXL_READING_ID", "44sqshkgw")
ONECOMPILER_WEB_BASE = os.getenv("ONECOMPILER_WEB_BASE", "https://onecompiler.com").rstrip("/")
SUPPORTED = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}
SKIP_ZIP_PARTS = {"__macosx", ".git", ".onecompiler_build", "node_modules", "sem2-image"}

MIME = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".webp": "image/webp",
    ".svg": "image/svg+xml",
}

ONECOMPILER_EDITOR_LANGUAGES = {
    "ada": "ada",
    "assembly": "assembly",
    "awk": "awk",
    "bash": "bash",
    "basic": "basic",
    "c": "c",
    "clojure": "clojure",
    "cobol": "cobol",
    "coffeescript": "coffeescript",
    "commonlisp": "commonlisp",
    "cpp": "cpp",
    "crystal": "crystal",
    "csharp": "csharp",
    "d": "d",
    "dart": "dart",
    "deno": "deno",
    "elixir": "elixir",
    "erlang": "erlang",
    "forth": "forth",
    "fortran": "fortran",
    "fsharp": "fsharp",
    "go": "golang",
    "groovy": "groovy",
    "haskell": "haskell",
    "haxe": "haxe",
    "html": "html",
    "java": "java",
    "javascript": "nodejs",
    "jshell": "jshell",
    "julia": "julia",
    "kotlin": "kotlin",
    "lua": "lua",
    "matplotlib": "matplotlib",
    "mongodb": "mongodb",
    "mysql": "mysql",
    "nim": "nim",
    "nodejs": "nodejs",
    "objectivec": "objectivec",
    "ocaml": "ocaml",
    "octave": "octave",
    "pascal": "pascal",
    "perl": "perl",
    "php": "php",
    "postgresql": "postgresql",
    "prolog": "prolog",
    "pygame": "pygame",
    "python": "python",
    "python2": "python",
    "r": "r",
    "racket": "racket",
    "ruby": "ruby",
    "rust": "rust",
    "scala": "scala",
    "scheme": "scheme",
    "seaborn": "seaborn",
    "sh": "sh",
    "sqlite": "sqlite",
    "swift": "swift",
    "tcl": "tcl",
    "tkinter": "tkinter",
    "typescript": "typescript",
    "v": "v",
    "vb": "vb",
    "zig": "zig",
}


def normalize_zip_path(path: str) -> str:
    normalized = posixpath.normpath(path.replace("\\", "/"))
    return "" if normalized == "." else normalized.lstrip("./")


def split_markdown_target(target: str) -> tuple[str, str]:
    target = target.strip()
    if target.startswith("<") and ">" in target:
        end = target.find(">")
        return target[1:end], target[end + 1 :].strip()

    match = re.match(r'^(.*?)(\s+(?:"[^"]*"|\'[^\']*\'|\([^)]*\)))$', target)
    if match:
        return match.group(1).strip(), match.group(2).strip()

    return target, ""


def has_url_scheme(path: str) -> bool:
    return bool(re.match(r"^[a-z][a-z0-9+.-]*:", path, re.IGNORECASE))


def resolve_markdown_image_path(markdown_path: str, image_path: str) -> str:
    decoded_path = unquote(image_path)
    markdown_dir = posixpath.dirname(markdown_path)
    return normalize_zip_path(posixpath.join(markdown_dir, decoded_path))


def get_upload_token() -> str:
    return os.getenv("BYTEXL_UPLOAD_TOKEN", "")


def get_content_token() -> str:
    return os.getenv("BYTEXL_CONTENT_TOKEN") or get_upload_token()


def auth_headers() -> dict[str, str]:
    token = get_content_token()
    if not token:
        raise HTTPException(500, "ByteXL token is not configured on the server")
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


def onecompiler_editor_language_for(language: str) -> str:
    editor_language = ONECOMPILER_EDITOR_LANGUAGES.get(str(language or "").lower())
    if not editor_language:
        raise HTTPException(400, f"No OneCompiler editor is configured for language: {language}")
    return editor_language


def onecompiler_save(payload: dict[str, Any]) -> Any:
    try:
        resp = requests.post(
            f"{ONECOMPILER_WEB_BASE}/api/editorx/save",
            json=payload,
            headers={"Content-Type": "application/json", "User-Agent": "ByteXL Content Converter"},
            timeout=90,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as exc:
        raise HTTPException(502, f"OneCompiler API request failed: {exc}") from exc
    except ValueError as exc:
        raise HTTPException(502, "OneCompiler returned an invalid response") from exc


def bytexl_get(path: str) -> Any:
    try:
        resp = requests.get(f"{BYTEXL_API_BASE}{path}", headers=auth_headers(), timeout=60)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as exc:
        raise HTTPException(502, f"ByteXL read failed: {exc}") from exc
    except ValueError as exc:
        raise HTTPException(502, "ByteXL returned an invalid response") from exc


def bytexl_post(path: str, payload: dict[str, Any]) -> Any:
    try:
        resp = requests.post(f"{BYTEXL_API_BASE}{path}", json=payload, headers=auth_headers(), timeout=90)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as exc:
        raise HTTPException(502, f"ByteXL update failed: {exc}") from exc
    except ValueError as exc:
        raise HTTPException(502, "ByteXL returned an invalid response") from exc


def get_bytexl_id() -> str:
    try:
        resp = requests.get(f"{BYTEXL_API_BASE}/api/getId", timeout=30)
        resp.raise_for_status()
        value = resp.json().get("id")
    except (requests.RequestException, ValueError) as exc:
        raise HTTPException(502, "Could not create a ByteXL id") from exc
    if not value:
        raise HTTPException(502, "ByteXL did not return an id")
    return value


def upload_to_s3(filename: str, data: bytes, subtype: str) -> Optional[str]:
    token = get_upload_token()
    if not token:
        raise RuntimeError("BYTEXL_UPLOAD_TOKEN is not configured")

    ext = Path(filename).suffix.lower()
    try:
        resp = requests.post(
            BYTEXL_UPLOAD_URL,
            data={"upload_file_type": "content", "upload_file_subtype": subtype},
            files={"upload_file": (filename, io.BytesIO(data), MIME.get(ext, "application/octet-stream"))},
            headers={"Authorization": f"Bearer {token}"},
            timeout=60,
        )
        resp.raise_for_status()
        result = resp.json()
    except (requests.RequestException, ValueError):
        return None

    return result.get("url") if result.get("status") == "success" else None


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:40] or "content"


def normalize_match_text(text: str) -> str:
    text = unquote(str(text or "")).lower()
    text = re.sub(r"\.(md|markdown)$", "", text)
    text = re.sub(r"^[\s_-]*(unit|chapter)?\s*\d+\s*[-_:.)]*\s*", "", text)
    text = text.replace("&", " and ")
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def similarity(left: str, right: str) -> float:
    left_norm = normalize_match_text(left)
    right_norm = normalize_match_text(right)
    if not left_norm or not right_norm:
        return 0
    if left_norm == right_norm:
        return 1
    if left_norm in right_norm or right_norm in left_norm:
        return 0.92
    return SequenceMatcher(None, left_norm, right_norm).ratio()


def extract_unit(path: str) -> dict[str, Any]:
    parts = [part for part in normalize_zip_path(path).split("/") if part]
    for part in parts[:-1]:
        match = re.match(r"^\s*Unit\s+(\d+)\s*[-:]\s*(.+?)\s*$", part, re.IGNORECASE)
        if match:
            return {"number": int(match.group(1)), "title": match.group(2).strip(), "folder": part}
    folder = parts[-2] if len(parts) > 1 else ""
    return {"number": None, "title": folder.strip(), "folder": folder}


def extract_topic_number(path: str) -> Optional[int]:
    stem = PurePosixPath(path).stem
    match = re.match(r"^\s*(\d{1,3})(?:[\s_.-]+|$)", stem)
    if match:
        return int(match.group(1))

    match = re.match(r"^\s*(?:topic|lesson|page|module)\s*(\d{1,3})(?:[\s_.:-]+|$)", stem, re.IGNORECASE)
    return int(match.group(1)) if match else None


def natural_sort_key(text: str) -> tuple[tuple[int, Any], ...]:
    parts = re.split(r"(\d+)", normalize_zip_path(text).lower())
    return tuple((0, int(part)) if part.isdigit() else (1, part) for part in parts)


def fallback_topic_title(path: str) -> str:
    stem = re.sub(r"^\s*\d{1,3}(?:[\s_.-]+|$)", "", PurePosixPath(path).stem)
    stem = re.sub(r"^\s*(?:topic|lesson|page|module)\s*\d{1,3}(?:[\s_.:-]+|$)", "", stem, flags=re.IGNORECASE)
    words = re.sub(r"[_-]+", " ", stem).strip()
    return words[:1].upper() + words[1:] if words else PurePosixPath(path).stem


def parse_readme_topics(files: list[dict[str, str]]) -> dict[str, str]:
    topic_titles: dict[str, str] = {}
    for item in files:
        path = normalize_zip_path(item.get("path", ""))
        if PurePosixPath(path).name.lower() != "readme.md":
            continue
        folder = PurePosixPath(path).parent.as_posix()
        for line in item.get("markdown", "").splitlines():
            if "|" not in line or ".md" not in line:
                continue
            cols = [col.strip() for col in line.strip().strip("|").split("|")]
            if len(cols) < 3 or not re.match(r"^\d+$", cols[0]):
                continue
            link_match = re.search(r"\(([^)]+\.md)\)", cols[1], re.IGNORECASE)
            if not link_match:
                continue
            linked = normalize_zip_path(posixpath.join(folder, link_match.group(1)))
            title = re.sub(r"`", "", cols[2]).strip()
            if title:
                topic_titles[linked] = title
    return topic_titles


def markdown_records(files: list[dict[str, str]]) -> list[dict[str, Any]]:
    titles = parse_readme_topics(files)
    records = []
    for index, item in enumerate(files):
        path = normalize_zip_path(item.get("path", ""))
        if any(part.lower() in SKIP_ZIP_PARTS for part in path.split("/")):
            continue
        name = PurePosixPath(path).name.lower()
        if not path.lower().endswith((".md", ".markdown")):
            continue
        if name == "readme.md" or name.startswith("onecompiler-"):
            continue
        unit = extract_unit(path)
        records.append(
            {
                "path": path,
                "markdown": item.get("markdown", ""),
                "unitNumber": unit["number"],
                "unitTitle": unit["title"] or "Imported Content",
                "topicNumber": extract_topic_number(path),
                "topicTitle": titles.get(path) or fallback_topic_title(path),
                "zipIndex": index,
            }
        )
    # Sort numerically when filenames expose an order, and otherwise preserve
    # the uploaded ZIP order instead of falling back to lexicographic order
    # where Topic 10 would appear before Topic 2.
    records.sort(
        key=lambda r: (
            r["unitNumber"] if r["unitNumber"] is not None else 9999,
            r["topicNumber"] if r["topicNumber"] is not None else r["zipIndex"],
            natural_sort_key(r["path"]),
        )
    )
    return records


def find_section(content: dict[str, Any], record: dict[str, Any]) -> tuple[Optional[dict[str, Any]], float]:
    best = (None, 0.0)
    for section in content.get("contentSections", []) or []:
        score = similarity(record["unitTitle"], section.get("title", ""))
        if score > best[1]:
            best = (section, score)
    return best


def find_page(section: dict[str, Any], record: dict[str, Any]) -> tuple[Optional[dict[str, Any]], float, str]:
    pages = section.get("contentPages", []) or []
    best = (None, 0.0, "title")
    for page in pages:
        score = similarity(record["topicTitle"], page.get("title", ""))
        if score > best[1]:
            best = (page, score, "title")
    topic_number = record.get("topicNumber")
    if topic_number and 1 <= topic_number <= len(pages):
        by_position = pages[topic_number - 1]
        position_score = similarity(record["topicTitle"], by_position.get("title", ""))
        if position_score >= 0.5 and position_score >= best[1] - 0.1:
            return by_position, max(position_score, 0.75), "position"
    return best


def build_upload_plan(
    content: dict[str, Any],
    records: list[dict[str, Any]],
    create_missing: bool,
) -> dict[str, Any]:
    plan = []
    unmatched = []
    updates = creates = 0
    seen_targets: set[str] = set()

    for record in records:
        section, section_score = find_section(content, record)
        section_action = "update"
        if not section or section_score < 0.72:
            if not create_missing:
                unmatched.append({**record, "reason": "No matching unit/chapter"})
                continue
            section = None
            section_action = "create"

        page = None
        page_score = 0.0
        page_match = "new"
        page_action = "create"
        if section:
            page, page_score, page_match = find_page(section, record)
            if page and page_score >= 0.62:
                page_action = "update"
            elif not create_missing:
                unmatched.append({**record, "reason": "No matching topic"})
                continue
            else:
                page = None

        target_key = page.get("_id") if page else f"new:{record['unitTitle']}:{record['topicNumber']}:{record['topicTitle']}"
        if target_key in seen_targets:
            unmatched.append({**record, "reason": "Duplicate target topic"})
            continue
        seen_targets.add(target_key)

        if page_action == "update":
            updates += 1
        else:
            creates += 1

        plan.append(
            {
                "path": record["path"],
                "unitTitle": record["unitTitle"],
                "topicTitle": record["topicTitle"],
                "topicNumber": record.get("topicNumber"),
                "sectionAction": section_action,
                "sectionId": section.get("_id") if section else None,
                "matchedSectionTitle": section.get("title") if section else None,
                "sectionScore": round(section_score, 3) if section else 0,
                "pageAction": page_action,
                "pageId": page.get("_id") if page else None,
                "matchedPageTitle": page.get("title") if page else None,
                "pageScore": round(page_score, 3) if page else 0,
                "pageMatch": page_match,
            }
        )

    return {
        "readingId": content.get("_id"),
        "readingTitle": content.get("title"),
        "records": len(records),
        "matched": len(plan),
        "updates": updates,
        "creates": creates,
        "unmatched": unmatched,
        "items": plan,
        "canUpload": len(plan) > 0 and len(unmatched) == 0,
    }


def fetch_content(reading_id: str) -> dict[str, Any]:
    result = bytexl_get(f"/api/content/{reading_id}")
    if result.get("status") == "failed" or not result.get("data"):
        raise HTTPException(404, result.get("message") or "Reading material not found")
    return result["data"]


def fetch_content_page(page_id: str) -> dict[str, Any]:
    result = bytexl_get(f"/api/content-page/{page_id}")
    if result.get("status") == "failed" or not result.get("data"):
        raise HTTPException(404, result.get("message") or f"Topic not found: {page_id}")
    return result["data"]


def save_content_page(page: dict[str, Any]) -> dict[str, Any]:
    result = bytexl_post("/api/content-page", page)
    if result.get("status") == "failed" or not result.get("data"):
        raise HTTPException(502, result.get("message") or "ByteXL topic save failed")
    return result["data"]


def save_content(content: dict[str, Any]) -> dict[str, Any]:
    result = bytexl_post("/api/content", content)
    if result.get("status") == "failed":
        raise HTTPException(502, result.get("message") or "ByteXL content save failed")
    return result.get("data") or content


def content_page_ref(page: dict[str, Any], fallback_title: str) -> dict[str, Any]:
    return {
        "_id": page.get("_id"),
        "title": page.get("title") or fallback_title,
        "publishStatus": page.get("publishStatus") or "published",
    }


def reorder_section_pages(
    section: dict[str, Any],
    ordered_page_ids: list[str],
    saved_page_refs: dict[str, dict[str, Any]],
    replace_all: bool,
) -> None:
    pages = section.get("contentPages", []) or []
    pages_by_id = {page.get("_id"): page for page in pages if page.get("_id")}
    ordered_pages = []
    seen_page_ids: set[str] = set()

    for page_id in ordered_page_ids:
        if not page_id or page_id in seen_page_ids:
            continue
        page_ref = pages_by_id.get(page_id) or saved_page_refs.get(page_id)
        if not page_ref:
            continue
        if page_id in saved_page_refs:
            page_ref = {**page_ref, **saved_page_refs[page_id]}
        ordered_pages.append(page_ref)
        seen_page_ids.add(page_id)

    if replace_all:
        section["contentPages"] = ordered_pages
    else:
        section["contentPages"] = ordered_pages + [
            page for page in pages if page.get("_id") not in seen_page_ids
        ]


def read_index() -> str:
    return (Path(__file__).parent / "index.html").read_text(encoding="utf-8")


def read_embed() -> str:
    return (Path(__file__).parent / "embed.html").read_text(encoding="utf-8")


def read_assessment() -> str:
    return (Path(__file__).parent / "assessment.html").read_text(encoding="utf-8")


def read_assessment_js() -> str:
    return (Path(__file__).parent / "assessment.js").read_text(encoding="utf-8")


@app.get("/save-token", response_class=HTMLResponse)
async def save_token_page(t: str = ""):
    if t:
        env_path = Path(__file__).parent / ".env"
        existing = env_path.read_text() if env_path.exists() else ""
        lines = [l for l in existing.splitlines() if not l.startswith("BYTEXL_UPLOAD_TOKEN=")]
        lines.append(f"BYTEXL_UPLOAD_TOKEN={t}")
        env_path.write_text("\n".join(lines) + "\n")
        return HTMLResponse("<html><body style='font-family:sans-serif;padding:40px'><h2>✅ Token saved!</h2><p>You can close this tab and return to ByteXL.</p><script>window.name=''</script></body></html>")
    return HTMLResponse("<html><body style='font-family:sans-serif;padding:40px'><h2>⚠️ No token provided.</h2></body></html>")


@app.get("/", response_class=HTMLResponse)
async def index():
    return read_index()


@app.get("/convert", response_class=HTMLResponse)
async def convert_page():
    return read_index()


@app.get("/assessment", response_class=HTMLResponse)
async def assessment_page():
    return read_assessment()


@app.get("/assessment.js")
async def assessment_js():
    return Response(read_assessment_js(), media_type="application/javascript; charset=utf-8")


@app.get("/xlsx.full.min.js")
async def xlsx_vendor():
    return FileResponse(Path(__file__).parent / "xlsx.full.min.js", media_type="application/javascript")


@app.get("/embed.html", response_class=HTMLResponse)
async def embed_page():
    return read_embed()


@app.head("/")
@app.head("/convert")
@app.head("/assessment")
@app.head("/embed.html")
async def page_head():
    return Response(status_code=200)


@app.get("/healthz")
async def healthz():
    return {"status": "ok"}


@app.get("/reading-materials")
async def reading_materials():
    result = bytexl_get("/api/content/v2/list?pageSize=10000")
    items = result.get("items") or result.get("data") or []
    return {
        "status": "success",
        "defaultReadingId": DEFAULT_READING_ID,
        "items": [
            {
                "_id": item.get("_id"),
                "title": item.get("title"),
                "chapterCount": item.get("chapterCount"),
                "topicCount": item.get("topicCount"),
            }
            for item in items
            if item.get("_id") and item.get("title")
        ],
    }


@app.get("/content-tree")
async def content_tree(reading_id: str = DEFAULT_READING_ID):
    content = fetch_content(reading_id)
    return {
        "status": "success",
        "reading": {
            "_id": content.get("_id"),
            "title": content.get("title"),
            "sections": [
                {
                    "_id": section.get("_id"),
                    "title": section.get("title"),
                    "topics": [
                        {
                            "_id": page.get("_id"),
                            "title": page.get("title"),
                            "publishStatus": page.get("publishStatus"),
                        }
                        for page in section.get("contentPages", []) or []
                    ],
                }
                for section in content.get("contentSections", []) or []
            ],
        },
    }


@app.post("/onecompiler/workspace")
async def create_onecompiler_workspace(payload: dict[str, Any] = Body(...)):
    language = str(payload.get("language") or "").strip().lower()
    title = str(payload.get("title") or "ByteXL code editor").strip()[:120]
    filename = normalize_zip_path(str(payload.get("filename") or "main.py")).lstrip("/")
    code = str(payload.get("code") or "")
    source_file = normalize_zip_path(str(payload.get("sourceFile") or ""))
    snippet_id = str(payload.get("snippetId") or "").strip()

    if not language:
        raise HTTPException(400, "Language is required")
    if not filename or filename.endswith("/"):
        raise HTTPException(400, "A valid filename is required")
    if not code.strip():
        raise HTTPException(400, "Code is required")

    editor_language = onecompiler_editor_language_for(language)
    tags = ["bytexl", "reading-material"]
    if snippet_id:
        tags.append(snippet_id[:40])
    properties: dict[str, Any] = {
        "language": editor_language,
        "files": [{"name": filename, "content": code}],
        "stdin": "",
        "source": "bytexl-reading-material",
    }
    if source_file:
        properties["sourceFile"] = source_file
    if snippet_id:
        properties["snippetId"] = snippet_id

    save_payload: dict[str, Any] = {
        "title": title,
        "description": f"Generated from ByteXL reading material: {source_file}" if source_file else "Generated from ByteXL reading material",
        "tags": tags,
        "visibility": "public",
        "properties": properties,
    }

    saved = onecompiler_save(save_payload)
    code_id = saved.get("_id") or saved.get("codeId") or saved.get("id")
    if not code_id:
        raise HTTPException(502, "OneCompiler did not return a code id")

    code_url = f"{ONECOMPILER_WEB_BASE}/{editor_language}/{code_id}"
    embed_url = f"{ONECOMPILER_WEB_BASE}/embed/{editor_language}/{code_id}"

    return {
        "status": "success",
        "codeId": code_id,
        "workspaceId": code_id,
        "language": editor_language,
        "templateId": editor_language,
        "url": code_url,
        "embedUrl": embed_url,
    }


@app.post("/preview-product-upload")
async def preview_product_upload(payload: dict[str, Any] = Body(...)):
    reading_id = payload.get("readingId") or DEFAULT_READING_ID
    files = payload.get("files") or []
    if not isinstance(files, list) or not files:
        raise HTTPException(400, "No markdown files were provided")

    content = fetch_content(reading_id)
    records = markdown_records(files)
    if not records:
        raise HTTPException(400, "No lesson markdown files found for upload")

    plan = build_upload_plan(content, records, bool(payload.get("createMissing", True)))
    return {"status": "success", "plan": plan}


@app.post("/upload-to-product")
async def upload_to_product(payload: dict[str, Any] = Body(...)):
    if payload.get("confirm") is not True:
        raise HTTPException(400, "Preview first, then confirm the upload")

    reading_id = payload.get("readingId") or DEFAULT_READING_ID
    files = payload.get("files") or []
    create_missing = bool(payload.get("createMissing", True))
    replace_all = bool(payload.get("replaceAll", False))
    content = fetch_content(reading_id)
    records = markdown_records(files)
    record_by_path = {record["path"]: record for record in records}
    plan = build_upload_plan(content, records, create_missing)

    if not plan["canUpload"]:
        raise HTTPException(400, "Upload blocked because one or more files could not be mapped")

    sections_by_id = {section.get("_id"): section for section in content.get("contentSections", []) or []}
    created_sections: dict[str, dict[str, Any]] = {}
    saved_page_refs: dict[str, dict[str, Any]] = {}
    updated_topics = 0
    created_topics = 0

    for item in plan["items"]:
        record = record_by_path[item["path"]]

        if item["sectionAction"] == "create":
            section_key = normalize_match_text(item["unitTitle"])
            section = created_sections.get(section_key)
            if not section:
                section = {"_id": get_bytexl_id(), "title": item["unitTitle"], "contentPages": []}
                created_sections[section_key] = section
                # Insert in numeric unit order rather than always appending
                plan_unit_num = record.get("unitNumber") or 9999
                sections = content.setdefault("contentSections", [])
                insert_at = len(sections)
                for idx, sec in enumerate(sections):
                    # Find the position just after all sections with a lower unit number
                    # We tag newly-created sections with their unit number for comparison
                    sec_unit = sec.get("_unitNumber", 9999)
                    if sec_unit > plan_unit_num:
                        insert_at = idx
                        break
                section["_unitNumber"] = plan_unit_num
                sections.insert(insert_at, section)
            item["sectionId"] = section["_id"]
        else:
            section = sections_by_id.get(item["sectionId"])
            if not section:
                raise HTTPException(400, f"Mapped section was not found for {item['path']}")

        if item["pageAction"] == "update":
            page = fetch_content_page(item["pageId"])
            page["markdown"] = record["markdown"]
            page["publishStatus"] = page.get("publishStatus") or "published"
            page = save_content_page(page)
            page_ref = content_page_ref(page, item["topicTitle"])
            if page_ref["_id"]:
                saved_page_refs[page_ref["_id"]] = page_ref
            updated_topics += 1
        else:
            page = save_content_page(
                {
                    "title": item["topicTitle"],
                    "markdown": record["markdown"],
                    "publishStatus": "published",
                }
            )
            page_ref = content_page_ref(page, item["topicTitle"])
            if page_ref["_id"]:
                item["pageId"] = page_ref["_id"]
                saved_page_refs[page_ref["_id"]] = page_ref
            section.setdefault("contentPages", []).append(page_ref)
            created_topics += 1

    # Build a lookup of every section we know about.
    all_sections_by_id = {s["_id"]: s for s in content.get("contentSections", [])}
    all_sections_by_id.update({s["_id"]: s for s in created_sections.values()})

    ordered_page_ids_by_section: dict[str, list[str]] = {}
    for item in plan["items"]:
        section_id = item.get("sectionId")
        page_id = item.get("pageId")
        if section_id and page_id:
            ordered_page_ids_by_section.setdefault(section_id, []).append(page_id)

    for section_id, page_ids in ordered_page_ids_by_section.items():
        section = all_sections_by_id.get(section_id)
        if section:
            reorder_section_pages(section, page_ids, saved_page_refs, replace_all)

    # Collect the plan sections in ZIP order (already sorted by unit number).
    seen_ids: set[str] = set()
    plan_ordered: list[dict[str, Any]] = []
    for item in plan["items"]:
        sid = item.get("sectionId")
        if sid and sid not in seen_ids:
            seen_ids.add(sid)
            if sid in all_sections_by_id:
                plan_ordered.append(all_sections_by_id[sid])

    if replace_all:
        # Replace mode: only keep what is in the ZIP. Ghost sections and content
        # from other semesters are removed. Order follows the ZIP exactly.
        content["contentSections"] = plan_ordered
    else:
        # Merge mode: preserve existing sections that are NOT in this upload
        # (e.g. other semester units), then append new sections in ZIP order.
        existing_not_in_plan = [
            s for s in content.get("contentSections", [])
            if s.get("_id") not in seen_ids
        ]
        content["contentSections"] = existing_not_in_plan + plan_ordered

    for section in content.get("contentSections", []) or []:
        section.pop("_unitNumber", None)

    save_content(content)

    return {
        "status": "success",
        "readingId": reading_id,
        "readingTitle": content.get("title"),
        "updatedTopics": updated_topics,
        "createdTopics": created_topics,
        "createdUnits": len(created_sections),
    }


@app.post("/assessment/validate")
async def assessment_validate(payload: dict[str, Any] = Body(...)):
    questions = payload.get("questions") or []
    if not isinstance(questions, list) or not questions:
        raise HTTPException(400, "No assessment questions were provided")

    result = bytexl_post("/api/questions/batch-validate", questions)
    return {"status": "success", "result": result}


@app.post("/assessment/upload-one")
async def assessment_upload_one(payload: dict[str, Any] = Body(...)):
    question = payload.get("question")
    if not isinstance(question, dict) or not question:
        raise HTTPException(400, "No assessment question was provided")

    result = bytexl_post("/api/questions/batch", [question])
    return {"status": "success", "result": result}


@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...), subtype: str = Form("content")):
    ext = Path(file.filename or "").suffix.lower()
    if ext not in SUPPORTED:
        raise HTTPException(400, "Unsupported image type")

    if not get_upload_token():
        raise HTTPException(500, "BYTEXL_UPLOAD_TOKEN is not configured on the server")

    data = await file.read()
    url = upload_to_s3(Path(file.filename).name, data, slugify(subtype))
    if not url:
        raise HTTPException(502, "ByteXL image upload failed")

    return {"status": "success", "url": url}


@app.post("/convert")
async def convert(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".zip"):
        raise HTTPException(400, "Please upload a .zip file")

    raw = await file.read()

    try:
        src = zipfile.ZipFile(io.BytesIO(raw))
    except zipfile.BadZipFile:
        raise HTTPException(400, "Invalid ZIP file")

    names = src.namelist()
    md_files = [n for n in names if n.lower().endswith(".md")]
    img_files = [n for n in names if not n.endswith("/") and PurePosixPath(n).suffix.lower() in SUPPORTED]

    if not md_files:
        raise HTTPException(400, "No markdown files found in the ZIP")

    if img_files and not get_upload_token():
        raise HTTPException(500, "BYTEXL_UPLOAD_TOKEN is not configured on the server")

    url_map: dict[str, str] = {}
    stats = {"uploaded": 0, "failed": 0, "missing": 0}

    for img_path in img_files:
        img_data = src.read(img_path)
        parts = PurePosixPath(img_path).parts
        subtype = slugify(parts[-2]) if len(parts) >= 2 else "content"
        url = upload_to_s3(PurePosixPath(img_path).name, img_data, subtype)
        if url:
            url_map[normalize_zip_path(img_path)] = url
            stats["uploaded"] += 1
        else:
            stats["failed"] += 1

    filename_map: dict[str, Optional[str]] = {}
    for img_path, url in url_map.items():
        filename = PurePosixPath(img_path).name
        filename_map[filename] = None if filename in filename_map else url

    out_buf = io.BytesIO()
    with zipfile.ZipFile(out_buf, "w", zipfile.ZIP_DEFLATED) as dst:
        for name in names:
            data = src.read(name)

            if name.lower().endswith(".md"):
                text = data.decode("utf-8", errors="replace")

                def replace_img(m):
                    alt, target = m.group(1), m.group(2)
                    local_path, title = split_markdown_target(target)
                    if has_url_scheme(local_path):
                        return m.group(0)

                    resolved = resolve_markdown_image_path(name, local_path)
                    filename = PurePosixPath(unquote(local_path)).name
                    s3 = url_map.get(resolved) or filename_map.get(filename)
                    if s3:
                        title_suffix = f" {title}" if title else ""
                        return f"![{alt}]({s3}{title_suffix})"

                    stats["missing"] += 1
                    return m.group(0)

                text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", replace_img, text)
                data = text.encode("utf-8")

            dst.writestr(name, data)

    src.close()
    out_buf.seek(0)

    out_name = Path(file.filename).stem + "_converted.zip"
    return StreamingResponse(
        out_buf,
        media_type="application/zip",
        headers={
            "Content-Disposition": f'attachment; filename="{out_name}"',
            "X-Stats": f"uploaded={stats['uploaded']},failed={stats['failed']},missing={stats['missing']}",
        },
    )
