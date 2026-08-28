import io
import hashlib
import json
import os
import posixpath
import re
import sys
import time
import zipfile
from difflib import SequenceMatcher
from pathlib import Path, PurePosixPath
from typing import Any, Optional
from urllib.parse import unquote

import requests
from fastapi import Body, FastAPI, File, Form, HTTPException, Request, Response, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse, StreamingResponse

app = FastAPI()
frontend_origins = [
    origin.strip()
    for origin in os.getenv(
        "FRONTEND_ORIGINS",
        "https://image-converter-pi-rouge.vercel.app,http://127.0.0.1:8000,http://localhost:8000",
    ).split(",")
    if origin.strip()
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=frontend_origins,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition", "X-Stats"],
)

def canonical_bytexl_url(url: str) -> str:
    """Move legacy bytexl.app URLs to the current API host.

    The legacy host returns HTTP 301 for API calls. HTTP clients commonly turn a
    redirected POST into a GET, which drops image multipart bodies and JSON payloads.
    Normalize even explicitly configured legacy URLs so existing deployments recover
    without requiring an environment-variable change first.
    """
    return re.sub(
        r"^https://(?:www\.)?bytexl\.app(?=/|$)",
        "https://app.bytexl.ai",
        str(url or "").strip(),
        flags=re.IGNORECASE,
    )


BYTEXL_UPLOAD_URL = canonical_bytexl_url(
    os.getenv("BYTEXL_UPLOAD_URL", "https://app.bytexl.ai/api/upload/s3")
)
BYTEXL_API_BASE = canonical_bytexl_url(
    os.getenv("BYTEXL_API_BASE", "https://app.bytexl.ai")
).rstrip("/")
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

SQL_LANGUAGES = {"mysql", "postgresql", "sqlite"}
POSTGRESQL_QUERY_MARKER = re.compile(r"(?im)^--\s*Query\s*$")


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


PYTHON_EDITOR_LANGUAGES = {"python", "python2"}
# Pure-stdlib stand-ins shipped beside a snippet so lesson code that imports these can
# still run in the sandbox. Injected only when the snippet actually imports them.
SANDBOX_SHIM_DIR = Path(__file__).parent / "sandbox"
SANDBOX_SHIMS = {"fastapi": "fastapi.py", "pydantic": "pydantic.py"}


def sandbox_shim_files(code: str) -> list[dict[str, str]]:
    """The shim modules a snippet needs, including any the shims need themselves."""
    roots = set(python_import_roots(code))
    if not roots & set(SANDBOX_SHIMS):
        return []
    needed = ["pydantic", "fastapi"] if "fastapi" in roots else ["pydantic"]
    files = []
    for module in needed:
        source = SANDBOX_SHIM_DIR / SANDBOX_SHIMS[module]
        if source.is_file():
            files.append({"name": SANDBOX_SHIMS[module], "content": source.read_text()})
    return files
# Verified against the live OneCompiler sandbox (Python 3.12.3): these are the only
# non-stdlib imports available. It has no outbound network and pip refuses to install
# under PEP 668, so anything else fails on the import line.
PYTHON_SANDBOX_EXTRA_PACKAGES = {"requests", "numpy", "pandas"}
PYTHON_IMPORT_RE = re.compile(
    r"^(?:from\s+([A-Za-z_][\w.]*)\s+import\s|import\s+(.+))", re.MULTILINE
)


def python_import_roots(code: str) -> list[str]:
    roots: list[str] = []
    for line in str(code or "").splitlines():
        if line[:1] in (" ", "\t"):
            continue
        match = PYTHON_IMPORT_RE.match(line.split("#", 1)[0].strip())
        if not match:
            continue
        if match.group(1):
            roots.append(match.group(1).split(".")[0])
            continue
        for part in (match.group(2) or "").split(","):
            name = part.strip().split(" as ")[0].strip()
            if re.fullmatch(r"[A-Za-z_][\w.]*", name or ""):
                roots.append(name.split(".")[0])
    return list(dict.fromkeys(roots))


def local_module_names(fixture_names: Any) -> set[str]:
    """Modules a lesson ships beside the snippet are present in the workspace."""
    modules: set[str] = set()
    for name in fixture_names or []:
        clean = str(name or "").lstrip("./")
        if clean:
            modules.add(clean.split("/")[0].removesuffix(".py"))
    return modules


def missing_sandbox_packages(language: str, code: str, local_modules: Any = None) -> list[str]:
    if str(language or "").lower() not in PYTHON_EDITOR_LANGUAGES:
        return []
    available = (
        set(sys.stdlib_module_names)
        | PYTHON_SANDBOX_EXTRA_PACKAGES
        | set(SANDBOX_SHIMS)
        | local_module_names(local_modules)
    )
    return [root for root in python_import_roots(code) if root not in available]


SHELL_EDITOR_LANGUAGES = {"bash", "sh"}
# Verified against the live sandbox: bash 5.2 with coreutils, but no uv, git, docker,
# wget or zip. The second set is installed yet still unusable, because the sandbox has
# no network and runs no services, so curl, pip and npm fail whatever the block says.
SHELL_SANDBOX_COMMANDS = {
    "bash", "sh", "echo", "printf", "ls", "tac", "cat", "head", "tail", "wc", "sort", "uniq",
    "grep", "sed", "awk", "cut", "tr", "paste", "join", "comm", "find", "xargs", "mkdir", "rmdir",
    "cp", "mv", "rm", "touch", "ln", "chmod", "pwd", "basename", "dirname", "date", "sleep", "seq",
    "env", "tee", "diff", "cmp", "md5sum", "sha256sum", "tar", "gzip", "gunzip", "unzip", "python3",
    "node", "sqlite3", "make", "nl", "rev", "shuf", "split", "stat", "du", "df", "ps", "expr",
    "test", "true", "false", "yes",
}
SHELL_KEYWORDS = {
    "if", "then", "else", "elif", "fi", "for", "while", "until", "do", "done", "case", "esac", "in",
    "function", "select", "time", "cd", "read", "export", "local", "return", "exit", "source", ".",
    ":", "set", "unset", "shift", "declare", "typeset", "readonly", "eval", "exec", "trap", "wait",
    "break", "continue", "let", "alias", "[", "[[",
}
SHELL_UNAVAILABLE_COMMANDS = {
    "curl", "wget", "pip", "pip3", "npm", "npx", "ssh", "scp", "rsync", "git", "apt", "apt-get",
    "yum", "dnf", "brew", "docker", "docker-compose", "kubectl", "uv", "uvx", "poetry", "pipenv",
    "conda", "uvicorn", "fastapi", "gunicorn", "alembic", "psql", "mysql", "mongo", "mongosh",
    "redis-cli", "celery", "pytest", "ruff", "mypy", "systemctl", "nc", "ping",
}
SHELL_ASSIGNMENT_RE = re.compile(r"^[A-Za-z_]\w*=")


def shell_command_names(code: str) -> list[str]:
    names: list[str] = []
    # Quoted spans are collapsed first so separators inside a JSON argument are not
    # mistaken for the start of another command.
    cleaned = re.sub(r"\\\r?\n", " ", str(code or ""))
    cleaned = re.sub(r"'[^']*'", "''", cleaned)
    cleaned = re.sub(r'"[^"]*"', '""', cleaned)
    for raw_line in cleaned.splitlines():
        line = raw_line.split("#", 1)[0].strip()
        if not line:
            continue
        for statement in re.split(r"\|\||&&|[|;&]", line):
            tokens = statement.split()
            for token in tokens:
                stripped = token.lstrip("(\"'`$")
                if not stripped:
                    continue
                if SHELL_ASSIGNMENT_RE.match(stripped):
                    continue
                if stripped in {"sudo", "command", "env"}:
                    continue
                name = stripped.rsplit("/", 1)[-1]
                # Redirections (2>&1, >out.txt) and argument fragments are not commands.
                if not re.fullmatch(r"[A-Za-z_][\w.+-]*", name):
                    break
                if name not in SHELL_KEYWORDS:
                    names.append(name)
                break
    return list(dict.fromkeys(names))


def undefined_top_level_names(language: str, code: str) -> list[str]:
    """Names a snippet reaches into at statement level but never defines.

    An illustrative fragment such as a bare `@app.get(...)` is valid Python that cannot
    run, so it must not become an editor that raises NameError in the published lesson.
    """
    if str(language or "").lower() not in PYTHON_EDITOR_LANGUAGES:
        return []
    defined = {"self", "cls"}
    needed: list[str] = []
    for raw_line in str(code or "").splitlines():
        bare = raw_line.split("#", 1)[0]
        trimmed = bare.strip()
        if not trimmed:
            continue
        for pattern in (
            r"^([A-Za-z_]\w*)\s*(?::[^=]+)?=[^=]",
            r"^(?:async\s+)?def\s+([A-Za-z_]\w*)",
            r"^class\s+([A-Za-z_]\w*)",
        ):
            match = re.match(pattern, trimmed)
            if match:
                defined.add(match.group(1))
        match = re.match(r"^for\s+([A-Za-z_][\w, ]*)\s+in\s", trimmed)
        if match:
            defined.update(name.strip() for name in match.group(1).split(","))
        match = re.search(r"\bas\s+([A-Za-z_]\w*)", trimmed)
        if match:
            defined.add(match.group(1))
        match = re.match(r"^import\s+(.+)$", trimmed)
        if match:
            for part in match.group(1).split(","):
                defined.add(part.strip().split(" as ")[-1].split(".")[0].strip())
        match = re.match(r"^from\s+[\w.]+\s+import\s+(.+)$", trimmed)
        if match:
            for part in match.group(1).split(","):
                defined.add(part.strip().split(" as ")[-1].replace("(", "").replace(")", "").strip())
        for pattern in (r"^@([A-Za-z_]\w*)", r"^([A-Za-z_]\w*)\.[A-Za-z_]"):
            match = re.match(pattern, bare)
            if match and match.group(1) not in needed:
                needed.append(match.group(1))
    return [name for name in needed if name not in defined]


def unavailable_shell_commands(language: str, code: str) -> list[str]:
    if str(language or "").lower() not in SHELL_EDITOR_LANGUAGES:
        return []
    return [
        name
        for name in shell_command_names(code)
        if name in SHELL_UNAVAILABLE_COMMANDS or name not in SHELL_SANDBOX_COMMANDS
    ]


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


def split_postgresql_code(code: str) -> tuple[str, str]:
    match = POSTGRESQL_QUERY_MARKER.search(code)
    if not match:
        return "", code.rstrip()

    setup = code[: match.start()].rstrip()
    commands = code[match.end() :].lstrip().rstrip()
    return setup, commands or code.rstrip()


def postgresql_files(code: str, extra_files: Any) -> list[dict[str, str]]:
    setup_parts: list[str] = []
    if isinstance(extra_files, list):
        for extra in extra_files:
            if not isinstance(extra, dict):
                continue
            content = str(extra.get("content") or "").rstrip()
            if content:
                setup_parts.append(content)

    setup, commands = split_postgresql_code(code)
    setup_parts.append(setup)
    files = [{"name": "commands.sql", "content": commands}]
    init_sql = "\n\n".join(part for part in setup_parts if part).strip()
    if init_sql:
        files.append({"name": "init.sql", "content": init_sql})
    return files


def bytexl_get(path: str) -> Any:
    try:
        resp = requests.get(f"{BYTEXL_API_BASE}{path}", headers=auth_headers(), timeout=60)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as exc:
        raise HTTPException(502, f"ByteXL read failed: {exc}") from exc
    except ValueError as exc:
        raise HTTPException(502, "ByteXL returned an invalid response") from exc


def bytexl_post(path: str, payload: Any) -> Any:
    try:
        resp = requests.post(f"{BYTEXL_API_BASE}{path}", json=payload, headers=auth_headers(), timeout=90)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as exc:
        raise HTTPException(502, f"ByteXL update failed: {exc}") from exc
    except ValueError as exc:
        raise HTTPException(502, "ByteXL returned an invalid response") from exc


def validate_questions_with_bytexl(questions: list[dict[str, Any]]) -> tuple[Any, Optional[str]]:
    """Validate questions upstream, falling back only when the validator is unavailable.

    ByteXL's batch validator is an advisory preflight check. Question creation uses a
    separate endpoint, so a server-side failure in the validator must not make the
    uploader unusable after the sheet has passed its local checks.
    """
    try:
        resp = requests.post(
            f"{BYTEXL_API_BASE}/api/questions/batch-validate",
            json=questions,
            headers=auth_headers(),
            timeout=90,
        )
        resp.raise_for_status()
        return resp.json(), None
    except requests.RequestException as exc:
        upstream_response = getattr(exc, "response", None)
        upstream_status = getattr(upstream_response, "status_code", None)
        if upstream_status is not None and upstream_status < 500:
            raise HTTPException(502, f"ByteXL validation failed: {exc}") from exc

        warning = (
            "ByteXL validation is temporarily unavailable; "
            "the sheet passed local validation and upload can continue."
        )
        return [{"errors": []} for _ in questions], warning
    except ValueError:
        warning = (
            "ByteXL validation returned an invalid response; "
            "the sheet passed local validation and upload can continue."
        )
        return [{"errors": []} for _ in questions], warning


def duplicate_question_id(result: Any) -> Optional[str]:
    if not isinstance(result, dict):
        return None
    message = str(result.get("message") or "")
    match = re.search(r"Duplicate:\s*question:\s*id:\s*([A-Za-z0-9_-]+)", message, re.IGNORECASE)
    return match.group(1) if match else None


def validation_results_for_upsert(result: Any) -> Any:
    if not isinstance(result, list):
        return result

    cleaned = []
    for item in result:
        if not isinstance(item, dict):
            cleaned.append(item)
            continue

        duplicate_id = None
        remaining_errors = []
        for error in item.get("errors") or []:
            if not isinstance(error, dict):
                remaining_errors.append(error)
                continue
            is_duplicate = str(error.get("code") or "").lower() == "duplicate"
            is_question = str(error.get("field") or "").lower() == "question"
            match = re.search(r"\bid:\s*([A-Za-z0-9_-]+)", str(error.get("message") or ""), re.IGNORECASE)
            if is_duplicate and is_question and match:
                duplicate_id = match.group(1)
            else:
                remaining_errors.append(error)

        cleaned.append(
            {
                **item,
                "errors": remaining_errors,
                **({"duplicateQuestionId": duplicate_id, "uploadAction": "update"} if duplicate_id else {}),
            }
        )
    return cleaned


def has_non_duplicate_error(result: Any) -> bool:
    if not isinstance(result, dict):
        return True
    message = str(result.get("message") or "")
    remaining = re.sub(
        r"Duplicate:\s*question:\s*id:\s*[A-Za-z0-9_-]+\s*,?",
        "",
        message,
        flags=re.IGNORECASE,
    ).strip(" ,")
    return bool(remaining)


def update_duplicate_question(question_id: str, question: dict[str, Any]) -> dict[str, Any]:
    response = bytexl_get(f"/api/questions/_edit/{question_id}")
    existing = response.get("data") if isinstance(response, dict) else None
    if not isinstance(existing, dict) or not existing:
        raise HTTPException(502, f"ByteXL duplicate question {question_id} could not be loaded")

    if existing.get("status") == "archived":
        bytexl_post(f"/api/questions-vault/restore/{question_id}", {})

    merged = {**existing, **question, "_id": question_id}
    updated = bytexl_post("/api/questions", merged)
    item = updated.get("data") if isinstance(updated, dict) and isinstance(updated.get("data"), dict) else updated
    if not isinstance(item, dict):
        item = {}
    return {**item, "_id": item.get("_id") or question_id, "uploadAction": "updated"}


UPDATE_CONTROL_FIELDS = {"questionId", "expectedRevision"}


def assessment_update_question_id(question: Any) -> str:
    if not isinstance(question, dict):
        return ""
    return str(question.get("questionId") or "").strip()


def assessment_update_payload(question: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in question.items() if key not in UPDATE_CONTROL_FIELDS and key != "_id"}


def assessment_question_revision(question: dict[str, Any]) -> str:
    canonical = json.dumps(question, sort_keys=True, separators=(",", ":"), default=str, ensure_ascii=False)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def assessment_changed_fields(existing: dict[str, Any], incoming: dict[str, Any]) -> list[str]:
    return sorted(key for key, value in incoming.items() if existing.get(key) != value)


def load_assessment_question(question_id: str) -> dict[str, Any]:
    response = bytexl_get(f"/api/questions/_edit/{question_id}")
    existing = response.get("data") if isinstance(response, dict) else None
    if not isinstance(existing, dict) or not existing:
        raise HTTPException(404, f"ByteXL question {question_id} was not found")
    return existing


def assessment_update_identity_errors(
    question_id: str,
    existing: dict[str, Any],
    incoming: dict[str, Any],
) -> list[str]:
    errors: list[str] = []
    incoming_title = str(incoming.get("title") or "").strip()
    existing_title = str(existing.get("title") or "").strip()
    if incoming_title != existing_title:
        errors.append(
            f'Title mismatch for {question_id}: ByteXL has "{existing_title}" but the sheet has "{incoming_title}".'
        )
    incoming_type = str(incoming.get("type") or "").strip()
    existing_type = str(existing.get("type") or "").strip()
    if incoming_type and existing_type and incoming_type != existing_type:
        errors.append(
            f"Type mismatch for {question_id}: ByteXL has {existing_type} but the sheet has {incoming_type}."
        )
    if str(existing.get("status") or "").lower() == "archived":
        errors.append(f"Question {question_id} is archived. Restore it in ByteXL before updating it.")
    return errors


def validate_existing_assessment_updates(questions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for question in questions:
        question_id = assessment_update_question_id(question)
        errors: list[str] = []
        if not question_id:
            errors.append("questionId is required in update mode.")
        elif not re.fullmatch(r"[A-Za-z0-9_-]+", question_id):
            errors.append("questionId contains unsupported characters.")
        elif question_id in seen_ids:
            errors.append(f"Duplicate questionId in this sheet: {question_id}.")
        if question_id:
            seen_ids.add(question_id)

        if errors:
            results.append({"questionId": question_id, "errors": errors, "changedFields": []})
            continue

        try:
            existing = load_assessment_question(question_id)
        except HTTPException as exc:
            results.append(
                {"questionId": question_id, "errors": [str(exc.detail)], "changedFields": []}
            )
            continue

        incoming = assessment_update_payload(question)
        errors.extend(assessment_update_identity_errors(question_id, existing, incoming))
        changed_fields = assessment_changed_fields(existing, incoming)
        results.append(
            {
                "questionId": question_id,
                "currentTitle": existing.get("title") or "",
                "changedFields": changed_fields,
                "expectedRevision": assessment_question_revision(existing),
                "uploadAction": "update" if changed_fields else "unchanged",
                "errors": errors,
            }
        )
    return results


def update_existing_assessment_questions(questions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for question in questions:
        question_id = assessment_update_question_id(question)
        if not question_id:
            results.append({"status": "failed", "message": "questionId is required in update mode."})
            continue
        if question_id in seen_ids:
            results.append(
                {"status": "failed", "questionId": question_id, "message": f"Duplicate questionId: {question_id}."}
            )
            continue
        seen_ids.add(question_id)

        try:
            existing = load_assessment_question(question_id)
            incoming = assessment_update_payload(question)
            identity_errors = assessment_update_identity_errors(question_id, existing, incoming)
            if identity_errors:
                results.append(
                    {"status": "failed", "questionId": question_id, "message": " ".join(identity_errors)}
                )
                continue

            expected_revision = str(question.get("expectedRevision") or "").strip()
            current_revision = assessment_question_revision(existing)
            if not expected_revision or expected_revision != current_revision:
                results.append(
                    {
                        "status": "conflict",
                        "questionId": question_id,
                        "message": "Question changed after validation. Validate the sheet again before updating.",
                    }
                )
                continue

            changed_fields = assessment_changed_fields(existing, incoming)
            if not changed_fields:
                results.append(
                    {
                        "_id": question_id,
                        "uploadAction": "unchanged",
                        "changedFields": [],
                    }
                )
                continue

            merged = {**existing, **incoming, "_id": question_id}
            updated = bytexl_post("/api/questions", merged)
            item = updated.get("data") if isinstance(updated, dict) and isinstance(updated.get("data"), dict) else updated
            if not isinstance(item, dict):
                item = {}
            updated_id = item.get("_id") or question_id
            if updated_id != question_id:
                results.append(
                    {
                        "status": "failed",
                        "questionId": question_id,
                        "message": "ByteXL returned a different question ID; update was not accepted.",
                    }
                )
                continue
            results.append(
                {
                    **item,
                    "_id": question_id,
                    "uploadAction": "updated",
                    "changedFields": changed_fields,
                }
            )
        except HTTPException as exc:
            results.append(
                {"status": "failed", "questionId": question_id, "message": str(exc.detail)}
            )
    return results


def upsert_assessment_questions(questions: list[dict[str, Any]]) -> list[Any]:
    results = bytexl_post("/api/questions/batch", questions)
    if not isinstance(results, list):
        raise HTTPException(502, "ByteXL returned an unexpected batch upload response")

    upserted: list[Any] = []
    for index, result in enumerate(results):
        if isinstance(result, dict) and result.get("_id"):
            upserted.append({**result, "uploadAction": "created"})
            continue

        duplicate_id = duplicate_question_id(result)
        if duplicate_id and not has_non_duplicate_error(result) and index < len(questions):
            try:
                upserted.append(update_duplicate_question(duplicate_id, questions[index]))
            except HTTPException as exc:
                upserted.append({"status": "failed", "message": str(exc.detail)})
            continue

        upserted.append(result)
    return upserted


SET_TWO_TAG_RE = re.compile(r"(?:^|[^a-z0-9])set\s*[-_]?\s*2(?:$|[^a-z0-9])", re.IGNORECASE)


def is_set_two_question(question: Any) -> bool:
    if not isinstance(question, dict):
        return False
    tags = question.get("tags")
    values = tags if isinstance(tags, list) else [tags]
    return any(SET_TWO_TAG_RE.search(str(value or "")) for value in values)


def normalize_assessment_question_title(value: Any) -> str:
    return " ".join(str(value or "").split()).casefold()


def published_question_items() -> list[dict[str, Any]]:
    response = bytexl_get("/api/questions?status=published&summaryScreen=true")
    if isinstance(response, list):
        items = response
    elif isinstance(response, dict):
        items = response.get("items") or response.get("data") or []
    else:
        items = []
    if not isinstance(items, list):
        raise HTTPException(502, "ByteXL returned an unexpected question list")
    return [item for item in items if isinstance(item, dict)]


def published_test_items() -> list[dict[str, Any]]:
    response = bytexl_get("/api/tests?builderListView=true")
    if isinstance(response, list):
        items = response
    elif isinstance(response, dict):
        items = response.get("items") or response.get("data") or []
    else:
        items = []
    if not isinstance(items, list):
        raise HTTPException(502, "ByteXL returned an unexpected test list")
    return [item for item in items if isinstance(item, dict)]


SET_TWO_STRUCTURED_TITLE_RE = re.compile(
    r"^(?P<course>.+?)\s+-\s+(?P<kind>MCQ|Coding(?:\s+Question)?s?)\s*(?:-\s*)?"
    r"(?P<unit>\d+)\.2\.(?P<order>\d+)\s*$",
    re.IGNORECASE,
)


def parse_set_two_question_title(question: dict[str, Any]) -> Optional[dict[str, Any]]:
    if not is_set_two_question(question):
        return None
    title = " ".join(str(question.get("title") or "").split())
    match = SET_TWO_STRUCTURED_TITLE_RE.fullmatch(title)
    if not match:
        return None
    return {
        "course": match.group("course").strip(),
        "unit": int(match.group("unit")),
        "order": int(match.group("order")),
        "kind": "coding" if match.group("kind").lower().startswith("coding") else "mcq",
    }


def assessment_title_for_set_two_group(course: str, unit: int) -> str:
    display_course = re.sub(
        r"^Introduction to Artificial Intelligence$",
        "Intro to Artificial Intelligence",
        course,
        flags=re.IGNORECASE,
    )
    return f"{display_course} - Assessment {unit}"


def normalize_assessment_test_title(value: Any) -> str:
    title = " ".join(str(value or "").split()).casefold()
    title = title.replace("introduction to artificial intelligence", "intro to artificial intelligence")
    title = re.sub(r"\(\s*v\d+\s*\)", " ", title, flags=re.IGNORECASE)
    return re.sub(r"[^a-z0-9]+", " ", title).strip()


def set_two_group_key(course: str, unit: int) -> str:
    canonical = f"{course.casefold()}|{unit}"
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:16]


def fetch_test_question_ids(test_id: str) -> frozenset[str]:
    detail = bytexl_get(f"/api/tests/{test_id}")
    data = detail.get("data") if isinstance(detail, dict) else None
    data = data if isinstance(data, dict) else (detail if isinstance(detail, dict) else {})
    questions = data.get("questions") if isinstance(data, dict) else None
    if not isinstance(questions, list):
        return frozenset()
    return frozenset(str(question["_id"]) for question in questions if isinstance(question, dict) and question.get("_id"))


def find_existing_test_by_question_ids(
    question_ids: list[str],
    tests: list[dict[str, Any]],
    detail_cache: dict[str, frozenset[str]],
) -> Optional[dict[str, Any]]:
    """Fall back to matching by exact question-set when titles disagree.

    ByteXL's existing Set 2 assessments use inconsistent naming per course
    ("Introduction to AI" vs "Introduction to Artificial Intelligence",
    "(v1)" suffixes, hyphen spacing) so exact-title matching alone misses
    real duplicates. Standardized-assessment tests are rare platform-wide
    (dozens, not thousands), so checking their actual question ids is cheap
    and unambiguous: a hash-id collision across an entire question set is
    not something that happens by chance.
    """
    wanted = frozenset(question_ids)
    for test in tests:
        if test.get("testIntent") != "standardizedAssessment":
            continue
        if test.get("questionsCount") != len(wanted):
            continue
        test_id = str(test.get("_id") or "")
        if not test_id:
            continue
        if test_id not in detail_cache:
            try:
                detail_cache[test_id] = fetch_test_question_ids(test_id)
            except HTTPException:
                detail_cache[test_id] = frozenset()
        if detail_cache[test_id] and detail_cache[test_id] == wanted:
            return test
    return None


def set_two_assessment_candidates(
    questions: list[dict[str, Any]],
    tests: list[dict[str, Any]],
) -> dict[str, Any]:
    groups: dict[tuple[str, int], list[dict[str, Any]]] = {}
    structured_count = 0
    set_two_count = 0
    for question in questions:
        if not is_set_two_question(question):
            continue
        set_two_count += 1
        parsed = parse_set_two_question_title(question)
        if not parsed or not question.get("_id"):
            continue
        structured_count += 1
        key = (parsed["course"], parsed["unit"])
        groups.setdefault(key, []).append({**question, "_setTwo": parsed})

    existing_by_title: dict[str, dict[str, Any]] = {}
    for test in tests:
        key = normalize_assessment_test_title(test.get("title"))
        if key and test.get("_id"):
            existing_by_title.setdefault(key, test)

    detail_cache: dict[str, frozenset[str]] = {}
    candidates: list[dict[str, Any]] = []
    for (course, unit), items in groups.items():
        items.sort(key=lambda question: (question["_setTwo"]["order"], str(question.get("_id"))))
        orders = [question["_setTwo"]["order"] for question in items]
        duplicate_orders = sorted({order for order in orders if orders.count(order) > 1})
        title = assessment_title_for_set_two_group(course, unit)
        question_ids = [str(question["_id"]) for question in items]
        existing = existing_by_title.get(normalize_assessment_test_title(title))
        if not existing:
            existing = find_existing_test_by_question_ids(question_ids, tests, detail_cache)
        kinds = sorted({question["_setTwo"]["kind"] for question in items})
        duration = 60 if "coding" in kinds else 30
        candidates.append(
            {
                "groupKey": set_two_group_key(course, unit),
                "course": course,
                "unit": unit,
                "title": title,
                "duration": duration,
                "questionCount": len(items),
                "questionTypes": kinds,
                "firstQuestion": items[0].get("title") or "",
                "lastQuestion": items[-1].get("title") or "",
                "questionIds": question_ids,
                "ready": not duplicate_orders,
                "issues": ([f"Duplicate question numbers: {', '.join(map(str, duplicate_orders))}"] if duplicate_orders else []),
                "existingTest": (
                    {
                        "_id": existing.get("_id"),
                        "title": existing.get("title"),
                        "status": existing.get("status"),
                        "editUrl": f'{BYTEXL_API_BASE}/tests/_edit/{existing.get("_id")}/{assessment_url_slug(existing.get("title") or title)}',
                    }
                    if existing
                    else None
                ),
            }
        )

    candidates.sort(key=lambda candidate: (candidate["course"].casefold(), candidate["unit"]))
    return {
        "candidates": candidates,
        "setTwoQuestionCount": set_two_count,
        "structuredQuestionCount": structured_count,
        "unstructuredQuestionCount": set_two_count - structured_count,
        "candidateCount": len(candidates),
        "readyCount": sum(candidate["ready"] and not candidate["existingTest"] for candidate in candidates),
        "existingCount": sum(bool(candidate["existingTest"]) for candidate in candidates),
    }


def assessment_url_slug(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", str(title or "").lower()).strip("-")
    return slug or "assessment"


def subject_set_two_pool(subject: str, questions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    subject_key = subject.strip().casefold()
    return [
        question
        for question in questions
        if is_set_two_question(question)
        and subject_key in [str(item).casefold() for item in (question.get("subjects") or [])]
    ]


def blueprint_order_key(question: dict[str, Any]) -> tuple[int, str]:
    title = str(question.get("title") or "")
    match = re.search(r"(\d+)\.2\.(\d+)", title)
    return (int(match.group(2)) if match else 10**6, title)


def blueprint_pool_by_topic(
    pool: list[dict[str, Any]], topics: list[str], question_type: str
) -> dict[str, list[dict[str, Any]]]:
    pools: dict[str, list[dict[str, Any]]] = {}
    for topic in topics:
        matched = [
            question
            for question in pool
            if question.get("type") == question_type and topic in (question.get("topics") or [])
        ]
        matched.sort(key=blueprint_order_key)
        pools[topic] = matched
    return pools


def blueprint_round_robin(
    pools: dict[str, list[dict[str, Any]]], topics: list[str], count: int
) -> list[dict[str, Any]]:
    """Spread the pick evenly across topics instead of draining the first one.

    A blueprint row can merge several curriculum topics into one assessment
    (e.g. OOP + modules + standard library). Taking the requested count
    straight off the first topic's pool would make the test lopsided, so
    this takes one question per topic per pass until the count is met or
    every pool is exhausted.
    """
    taken: list[dict[str, Any]] = []
    cursors = {topic: 0 for topic in topics}
    while len(taken) < count:
        progressed = False
        for topic in topics:
            if len(taken) >= count:
                break
            pool = pools[topic]
            idx = cursors[topic]
            if idx < len(pool):
                taken.append(pool[idx])
                cursors[topic] += 1
                progressed = True
        if not progressed:
            break
    return taken


def resolve_blueprint_row(
    pool: list[dict[str, Any]], row: dict[str, Any], tests: list[dict[str, Any]]
) -> dict[str, Any]:
    title = " ".join(str(row.get("title") or "").split())
    topics = [str(topic).strip() for topic in (row.get("topics") or []) if str(topic).strip()]
    mcq_count = int(row.get("mcqCount") or 0)
    coding_count = int(row.get("codingCount") or 0)
    duration = int(row.get("duration") or 30)

    mcq_pools = blueprint_pool_by_topic(pool, topics, "multipleChoice")
    coding_pools = blueprint_pool_by_topic(pool, topics, "coding")
    mcq_selected = blueprint_round_robin(mcq_pools, topics, mcq_count)
    coding_selected = blueprint_round_robin(coding_pools, topics, coding_count)

    mcq_available = sum(len(items) for items in mcq_pools.values())
    coding_available = sum(len(items) for items in coding_pools.values())

    question_ids = [str(question["_id"]) for question in mcq_selected + coding_selected]
    existing = find_existing_test_by_question_ids(question_ids, tests, {}) if question_ids else None

    issues: list[str] = []
    if len(mcq_selected) < mcq_count:
        issues.append(f"Needs {mcq_count} MCQs, only {mcq_available} available")
    if len(coding_selected) < coding_count:
        issues.append(f"Needs {coding_count} coding problems, only {coding_available} available")

    return {
        "title": title,
        "topics": topics,
        "duration": duration,
        "mcqRequested": mcq_count,
        "codingRequested": coding_count,
        "mcqAvailable": mcq_available,
        "codingAvailable": coding_available,
        "mcqSelectedCount": len(mcq_selected),
        "codingSelectedCount": len(coding_selected),
        "questionIds": question_ids,
        "ready": not issues and not existing,
        "issues": issues,
        "existingTest": (
            {
                "_id": existing.get("_id"),
                "title": existing.get("title"),
                "editUrl": f'{BYTEXL_API_BASE}/tests/_edit/{existing.get("_id")}/{assessment_url_slug(existing.get("title") or title)}',
            }
            if existing
            else None
        ),
    }


def build_standardized_assessment_payload(
    title: str,
    duration: int,
    status: str,
    shuffle_questions: bool,
    question_ids: list[str],
) -> dict[str, Any]:
    return {
        "title": title,
        "name": "",
        "description": "",
        "tags": [],
        "status": status,
        "testIntent": "standardizedAssessment",
        "labMode": False,
        "timeLimit": duration,
        "showInstructionsOnStart": False,
        "shuffleQuestions": shuffle_questions,
        "captureUserImages": False,
        "recordSession": False,
        "forceFullScreen": False,
        "captureTabSwitches": False,
        "closeAfterNumberOfTabSwitches": 0,
        "showReportAfterTest": False,
        "sendReportViaEmail": False,
        "showReportAfter": "",
        "questions": question_ids,
        "enableSections": False,
        "sections": [],
    }


def get_bytexl_id() -> str:
    """Fetch a section ID without making a brief upstream outage fatal.

    Product uploads only call this endpoint when they need to create a missing
    section.  The endpoint is small but external, and a cold connection or a
    transient 5xx previously aborted the entire upload on the first attempt.
    """
    token = get_content_token()
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    last_error = ""

    for attempt in range(3):
        try:
            resp = requests.get(
                f"{BYTEXL_API_BASE}/api/getId",
                headers=headers,
                timeout=30,
            )
            resp.raise_for_status()
            result = resp.json()
            value = result.get("id") if isinstance(result, dict) else None
            if value:
                return str(value)
            last_error = "ByteXL returned a response without an id"
        except requests.RequestException as exc:
            upstream_response = getattr(exc, "response", None)
            if upstream_response is not None:
                last_error = f"ByteXL returned HTTP {upstream_response.status_code}"
            else:
                last_error = str(exc)
        except ValueError:
            last_error = "ByteXL returned an invalid response"

        if attempt < 2:
            time.sleep(0.25 * (attempt + 1))

    detail = last_error or "ByteXL did not return an id"
    raise HTTPException(502, f"Could not create a ByteXL id after 3 attempts: {detail}")


def upload_to_s3(filename: str, data: bytes, subtype: str) -> str:
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
    except requests.RequestException as exc:
        upstream_response = getattr(exc, "response", None)
        detail = ""
        if upstream_response is not None:
            detail = str(getattr(upstream_response, "text", "") or "").strip()[:300]
            if detail.lower().startswith(("<!doctype html", "<html")):
                detail = f"upstream returned HTTP {upstream_response.status_code}"
        suffix = f": {detail}" if detail else f": {exc}"
        raise HTTPException(502, f"ByteXL image upload failed{suffix}") from exc
    except ValueError as exc:
        raise HTTPException(502, "ByteXL image upload returned an invalid response") from exc

    if not isinstance(result, dict):
        raise HTTPException(502, "ByteXL image upload returned an invalid response")
    url = result.get("url")
    if result.get("status") != "success" or not url:
        message = result.get("message") or result.get("error") or "no image URL was returned"
        raise HTTPException(502, f"ByteXL image upload failed: {message}")
    return url


def content_addressed_image_name(filename: str, data: bytes) -> str:
    """Return a stable S3 name that cannot collide with a different image.

    Course ZIPs commonly repeat names such as ``01_intro.png`` in every unit.
    ByteXL stores uploads by subtype and filename, so sending only that basename
    allows a later unit to overwrite an earlier unit's image.  Key the stored
    name by the actual uploaded bytes while retaining a readable stem.
    """
    path = Path(filename or "image")
    ext = path.suffix.lower()
    stem = re.sub(r"[^A-Za-z0-9._-]+", "-", path.stem).strip("-._")[:80] or "image"
    digest = hashlib.sha256(data).hexdigest()[:16]
    return f"{stem}-{digest}{ext}"


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
    """Return explicit topic titles declared by README tables.

    A README title is authoritative. Filenames are deliberately kept short for
    portability and therefore cannot preserve punctuation, acronyms, symbols,
    or the end of long titles.
    """
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
            linked = normalize_zip_path(posixpath.join(folder, unquote(link_match.group(1))))
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


def read_assessment_builder() -> str:
    return (Path(__file__).parent / "assessment-builder.html").read_text(encoding="utf-8")


def read_assessment_builder_js() -> str:
    return (Path(__file__).parent / "assessment-builder.js").read_text(encoding="utf-8")


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


@app.get("/config.js")
async def config_js(request: Request):
    origin = f"{request.url.scheme}://{request.headers.get('host', 'localhost:8000')}"
    return Response(
        f'window.IMAGE_CONVERTER_CONFIG = Object.freeze({{ apiBase: "{origin}" }});',
        media_type="application/javascript",
    )


@app.get("/assessment", response_class=HTMLResponse)
async def assessment_page():
    return read_assessment()


@app.get("/assessment.js")
async def assessment_js():
    return Response(read_assessment_js(), media_type="application/javascript; charset=utf-8")


@app.get("/assessment-builder", response_class=HTMLResponse)
async def assessment_builder_page():
    return read_assessment_builder()


@app.get("/assessment-builder.js")
async def assessment_builder_js():
    return Response(read_assessment_builder_js(), media_type="application/javascript; charset=utf-8")


@app.get("/xlsx.full.min.js")
async def xlsx_vendor():
    return FileResponse(Path(__file__).parent / "xlsx.full.min.js", media_type="application/javascript")


@app.get("/embed.html", response_class=HTMLResponse)
async def embed_page():
    return read_embed()


@app.head("/")
@app.head("/convert")
@app.head("/assessment")
@app.head("/assessment-builder")
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
    extra_files = payload.get("extraFiles") or []

    if not language:
        raise HTTPException(400, "Language is required")
    if not filename or filename.endswith("/"):
        raise HTTPException(400, "A valid filename is required")
    if not code.strip():
        raise HTTPException(400, "Code is required")

    editor_language = onecompiler_editor_language_for(language)

    # Refuse an editor that is certain to fail on its import line. The browser
    # already screens these out; this is the backstop for direct API callers.
    fixture_names = [
        str(extra.get("name") or "")
        for extra in (extra_files if isinstance(extra_files, list) else [])
        if isinstance(extra, dict)
    ]
    missing = missing_sandbox_packages(language, code, fixture_names)
    if missing:
        raise HTTPException(
            400,
            "The OneCompiler Python sandbox cannot import "
            f"{', '.join(missing)}. It has no network access and pip is blocked, so this "
            "block must stay a static code block.",
        )

    undefined = undefined_top_level_names(language, code)
    if undefined:
        raise HTTPException(
            400,
            f"This snippet uses {', '.join(undefined)} without defining it, so an editor "
            "would raise NameError. It must stay a static code block.",
        )

    unavailable = unavailable_shell_commands(language, code)
    if unavailable:
        raise HTTPException(
            400,
            "The OneCompiler shell sandbox cannot run "
            f"{', '.join(unavailable)}. It has no network access and no services running, so this "
            "block must stay a static code block.",
        )

    tags = ["bytexl", "reading-material"]
    if snippet_id:
        tags.append(snippet_id[:40])

    if language == "postgresql":
        files = postgresql_files(code, extra_files)
        extra_files = []
    elif language in SQL_LANGUAGES:
        setup_parts: list[str] = []
        if isinstance(extra_files, list):
            for extra in extra_files:
                if not isinstance(extra, dict):
                    continue
                content = str(extra.get("content") or "").rstrip()
                if content:
                    setup_parts.append(content)
        if setup_parts:
            query = code.rstrip()
            code = "\n\n".join([*setup_parts, "-- Query\n" + query]).strip()
        filename = "main_001.sql"
        extra_files = []
        files = [{"name": filename, "content": code}]
    else:
        # The main runnable file is always file 0 (the active tab). Non-SQL
        # fixtures declared with `with=` are added beside it so file-reading
        # examples still have their inputs available.
        files = [{"name": filename, "content": code}]
        seen_names = {filename}
        # Stand-in modules go in before the lesson's own fixtures, so `import fastapi`
        # resolves inside the workspace instead of failing.
        for shim in sandbox_shim_files(code):
            if shim["name"] not in seen_names:
                files.append(shim)
                seen_names.add(shim["name"])
        if isinstance(extra_files, list):
            for extra in extra_files:
                if not isinstance(extra, dict):
                    continue
                extra_name = normalize_zip_path(str(extra.get("name") or "")).lstrip("/")
                if not extra_name or extra_name.endswith("/") or extra_name in seen_names:
                    continue
                files.append({"name": extra_name, "content": str(extra.get("content") or "")})
                seen_names.add(extra_name)

    properties: dict[str, Any] = {
        "language": editor_language,
        "files": files,
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
            page["title"] = item["topicTitle"]
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

    result, warning = validate_questions_with_bytexl(questions)
    return {
        "status": "success",
        "result": validation_results_for_upsert(result),
        "validationMode": "local-fallback" if warning else "bytexl",
        "warning": warning,
    }


@app.post("/assessment/upload")
async def assessment_upload(payload: dict[str, Any] = Body(...)):
    questions = payload.get("questions") or []
    if not isinstance(questions, list) or not questions:
        raise HTTPException(400, "No assessment questions were provided")

    result = upsert_assessment_questions(questions)
    return {"status": "success", "result": result}


@app.post("/assessment/update/validate")
async def assessment_update_validate(payload: dict[str, Any] = Body(...)):
    questions = payload.get("questions") or []
    if not isinstance(questions, list) or not questions:
        raise HTTPException(400, "No assessment questions were provided")
    if not all(isinstance(question, dict) for question in questions):
        raise HTTPException(400, "Every assessment question must be an object")

    result = validate_existing_assessment_updates(questions)
    return {"status": "success", "result": result, "created": 0}


@app.post("/assessment/update")
async def assessment_update(payload: dict[str, Any] = Body(...)):
    if payload.get("confirm") is not True:
        raise HTTPException(400, "Validate first, then confirm the update")
    questions = payload.get("questions") or []
    if not isinstance(questions, list) or not questions:
        raise HTTPException(400, "No assessment questions were provided")
    if not all(isinstance(question, dict) for question in questions):
        raise HTTPException(400, "Every assessment question must be an object")

    result = update_existing_assessment_questions(questions)
    return {"status": "success", "result": result, "created": 0}


@app.post("/assessment/upload-one")
async def assessment_upload_one(payload: dict[str, Any] = Body(...)):
    question = payload.get("question")
    if not isinstance(question, dict) or not question:
        raise HTTPException(400, "No assessment question was provided")

    result = upsert_assessment_questions([question])
    return {"status": "success", "result": result}


@app.get("/test-assessment/candidates")
async def test_assessment_candidates():
    result = set_two_assessment_candidates(published_question_items(), published_test_items())
    return {"status": "success", **result}


@app.post("/test-assessment/create")
async def test_assessment_create(payload: dict[str, Any] = Body(...)):
    if payload.get("confirm") is not True:
        raise HTTPException(400, "Review the detected Set 2 groups, then confirm assessment creation")

    requested_keys = payload.get("groupKeys") or []
    if not isinstance(requested_keys, list) or not requested_keys:
        raise HTTPException(400, "Choose at least one detected Set 2 group")
    requested_keys = [str(key or "").strip() for key in requested_keys]
    if len(requested_keys) > 100:
        raise HTTPException(400, "A maximum of 100 assessments can be created at once")
    if len(set(requested_keys)) != len(requested_keys):
        raise HTTPException(400, "The same Set 2 group was selected more than once")

    overrides_payload = payload.get("overrides") or {}
    if not isinstance(overrides_payload, dict):
        raise HTTPException(400, "overrides must be an object keyed by group key")

    discovery = set_two_assessment_candidates(published_question_items(), published_test_items())
    by_key = {candidate["groupKey"]: candidate for candidate in discovery["candidates"]}
    missing_keys = [key for key in requested_keys if key not in by_key]
    if missing_keys:
        raise HTTPException(409, "Set 2 groups changed after discovery. Refresh the list and try again.")

    selected = [by_key[key] for key in requested_keys]
    blocked = [candidate for candidate in selected if not candidate["ready"] or candidate["existingTest"]]
    if blocked:
        titles = ", ".join(candidate["title"] for candidate in blocked[:5])
        raise HTTPException(409, f"These assessments are not eligible for creation: {titles}")

    prepared: list[dict[str, Any]] = []
    for candidate in selected:
        override = overrides_payload.get(candidate["groupKey"])
        override = override if isinstance(override, dict) else {}

        title = candidate["title"]
        if "title" in override:
            title = " ".join(str(override.get("title") or "").split())
            if not title:
                raise HTTPException(400, f'Title is required for "{candidate["title"]}"')
            if len(title) > 180:
                raise HTTPException(400, f'Title must be 180 characters or fewer for "{candidate["title"]}"')

        duration = candidate["duration"]
        if "duration" in override:
            duration = override.get("duration")
            if isinstance(duration, bool) or not isinstance(duration, int) or not 0 <= duration <= 1440:
                raise HTTPException(400, f'Duration must be a whole number from 0 to 1440 minutes for "{candidate["title"]}"')

        prepared.append({**candidate, "title": title, "duration": duration})

    results: list[dict[str, Any]] = []
    for candidate in prepared:
        test_payload = build_standardized_assessment_payload(
            title=candidate["title"],
            duration=candidate["duration"],
            status="published",
            shuffle_questions=False,
            question_ids=candidate["questionIds"],
        )
        try:
            response = bytexl_post("/api/tests", test_payload)
            created = response.get("data") if isinstance(response, dict) and isinstance(response.get("data"), dict) else response
            if not isinstance(created, dict) or not created.get("_id"):
                results.append({"status": "failed", "title": candidate["title"], "message": "ByteXL did not return the created assessment"})
                continue
            test_id = str(created["_id"])
            created_title = str(created.get("title") or candidate["title"])
            slug = assessment_url_slug(created_title)
            results.append(
                {
                    "status": "created",
                    "testId": test_id,
                    "title": created_title,
                    "questionCount": candidate["questionCount"],
                    "editUrl": f"{BYTEXL_API_BASE}/tests/_edit/{test_id}/{slug}",
                    "previewUrl": f"{BYTEXL_API_BASE}/test/{test_id}/{slug}",
                }
            )
        except HTTPException as exc:
            results.append({"status": "failed", "title": candidate["title"], "message": str(exc.detail)})

    return {
        "status": "success",
        "createdCount": sum(result["status"] == "created" for result in results),
        "failedCount": sum(result["status"] == "failed" for result in results),
        "results": results,
    }


def parse_blueprint_rows(payload: dict[str, Any]) -> tuple[str, list[dict[str, Any]]]:
    subject = str(payload.get("subject") or "").strip()
    if not subject:
        raise HTTPException(400, "subject is required")
    rows = payload.get("rows")
    if not isinstance(rows, list) or not rows:
        raise HTTPException(400, "At least one blueprint row is required")
    if len(rows) > 50:
        raise HTTPException(400, "A maximum of 50 blueprint rows can be used at once")
    if not all(isinstance(row, dict) for row in rows):
        raise HTTPException(400, "Every blueprint row must be an object")
    return subject, rows


@app.post("/test-assessment/blueprint/preview")
async def test_assessment_blueprint_preview(payload: dict[str, Any] = Body(...)):
    subject, rows = parse_blueprint_rows(payload)
    pool = subject_set_two_pool(subject, published_question_items())
    tests = published_test_items()
    resolved = [resolve_blueprint_row(pool, row, tests) for row in rows]
    return {
        "status": "success",
        "subject": subject,
        "poolSize": len(pool),
        "rows": resolved,
        "readyCount": sum(row["ready"] for row in resolved),
    }


@app.post("/test-assessment/blueprint/create")
async def test_assessment_blueprint_create(payload: dict[str, Any] = Body(...)):
    if payload.get("confirm") is not True:
        raise HTTPException(400, "Preview the blueprint, then confirm assessment creation")
    subject, rows = parse_blueprint_rows(payload)

    pool = subject_set_two_pool(subject, published_question_items())
    tests = published_test_items()
    resolved = [resolve_blueprint_row(pool, row, tests) for row in rows]
    blocked = [row for row in resolved if not row["ready"]]
    if blocked:
        titles = ", ".join(row["title"] for row in blocked[:5])
        raise HTTPException(409, f"These blueprint rows are not eligible for creation: {titles}")

    results: list[dict[str, Any]] = []
    for row in resolved:
        test_payload = build_standardized_assessment_payload(
            title=row["title"],
            duration=row["duration"],
            status="published",
            shuffle_questions=False,
            question_ids=row["questionIds"],
        )
        try:
            response = bytexl_post("/api/tests", test_payload)
            created = response.get("data") if isinstance(response, dict) and isinstance(response.get("data"), dict) else response
            if not isinstance(created, dict) or not created.get("_id"):
                results.append({"status": "failed", "title": row["title"], "message": "ByteXL did not return the created assessment"})
                continue
            test_id = str(created["_id"])
            created_title = str(created.get("title") or row["title"])
            slug = assessment_url_slug(created_title)
            results.append(
                {
                    "status": "created",
                    "testId": test_id,
                    "title": created_title,
                    "questionCount": len(row["questionIds"]),
                    "editUrl": f"{BYTEXL_API_BASE}/tests/_edit/{test_id}/{slug}",
                    "previewUrl": f"{BYTEXL_API_BASE}/test/{test_id}/{slug}",
                }
            )
        except HTTPException as exc:
            results.append({"status": "failed", "title": row["title"], "message": str(exc.detail)})

    return {
        "status": "success",
        "createdCount": sum(result["status"] == "created" for result in results),
        "failedCount": sum(result["status"] == "failed" for result in results),
        "results": results,
    }


@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...), subtype: str = Form("content")):
    ext = Path(file.filename or "").suffix.lower()
    if ext not in SUPPORTED:
        raise HTTPException(400, "Unsupported image type")

    if not get_upload_token():
        raise HTTPException(500, "BYTEXL_UPLOAD_TOKEN is not configured on the server")

    data = await file.read()
    upload_name = content_addressed_image_name(Path(file.filename).name, data)
    url = upload_to_s3(upload_name, data, slugify(subtype))
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
