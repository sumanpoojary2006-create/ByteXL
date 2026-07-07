#!/usr/bin/env python3
"""
Local UI for generating and uploading OneCompiler embeds.

Run from this folder:
    python3 onecompiler_ui.py
Then open:
    http://127.0.0.1:8765
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import threading
import time
import webbrowser
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent
# Content lives under <ByteXL>/content while scripts live under <ByteXL>/tools/scripts.
CONTENT_ROOT = ROOT.parent.parent / "content"
BUILD_DIR = ROOT / ".onecompiler_build"
PORT = 8765
LOCK = threading.Lock()
SIMPLE_UI_FILE = ROOT / "onecompiler_ui_simple.html"
EMBED_WRAPPER_FILE = ROOT / "onecompiler_embed_wrapper.html"


HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>ByteXL OneCompiler Builder</title>
  <style>
    :root {
      --bg: #f6f7f9;
      --panel: #ffffff;
      --ink: #18212f;
      --muted: #647084;
      --line: #d9dee8;
      --blue: #235c9f;
      --blue-dark: #184676;
      --green: #1d7a59;
      --red: #b4232a;
      --amber: #9a6400;
      --shadow: 0 1px 2px rgba(15, 23, 42, 0.08);
    }

    * { box-sizing: border-box; }

    body {
      margin: 0;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: var(--ink);
      background: var(--bg);
      letter-spacing: 0;
    }

    button, input, textarea {
      font: inherit;
    }

    .app {
      min-height: 100vh;
      display: grid;
      grid-template-columns: 360px minmax(0, 1fr);
    }

    aside {
      background: var(--panel);
      border-right: 1px solid var(--line);
      padding: 18px;
      overflow: auto;
    }

    main {
      padding: 18px;
      overflow: auto;
    }

    .brand {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      margin-bottom: 18px;
    }

    h1 {
      font-size: 18px;
      line-height: 1.2;
      margin: 0;
      font-weight: 700;
    }

    h2 {
      font-size: 13px;
      text-transform: uppercase;
      color: var(--muted);
      margin: 20px 0 10px;
      font-weight: 700;
    }

    .status-pill {
      border: 1px solid var(--line);
      border-radius: 999px;
      padding: 5px 9px;
      font-size: 12px;
      color: var(--muted);
      white-space: nowrap;
      background: #fbfcfd;
    }

    .source-list {
      display: grid;
      gap: 8px;
    }

    label.check {
      display: grid;
      grid-template-columns: 18px minmax(0, 1fr) auto;
      gap: 8px;
      align-items: center;
      padding: 8px;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: #fbfcfd;
    }

    label.check span {
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }

    .count {
      color: var(--muted);
      font-size: 12px;
    }

    .field {
      display: grid;
      gap: 6px;
      margin-bottom: 12px;
    }

    .field label {
      font-size: 13px;
      font-weight: 650;
    }

    input[type="text"],
    input[type="password"],
    textarea {
      width: 100%;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: #ffffff;
      color: var(--ink);
      padding: 9px 10px;
      outline: none;
    }

    textarea {
      min-height: 68px;
      resize: vertical;
    }

    input:focus,
    textarea:focus {
      border-color: var(--blue);
      box-shadow: 0 0 0 3px rgba(35, 92, 159, 0.13);
    }

    .row {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      align-items: center;
    }

    .button {
      border: 1px solid transparent;
      border-radius: 6px;
      min-height: 38px;
      padding: 8px 12px;
      cursor: pointer;
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--blue);
      color: #ffffff;
    }

    .button:hover { background: var(--blue-dark); }
    .button:disabled { opacity: 0.55; cursor: not-allowed; }

    .button.secondary {
      color: var(--ink);
      background: #ffffff;
      border-color: var(--line);
    }

    .button.secondary:hover {
      background: #eef2f7;
    }

    .button.danger {
      background: var(--red);
    }

    .button.danger:hover {
      background: #8f1d23;
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(4, minmax(150px, 1fr));
      gap: 12px;
      margin-bottom: 16px;
    }

    .metric {
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 13px;
      box-shadow: var(--shadow);
      min-height: 78px;
    }

    .metric strong {
      display: block;
      font-size: 26px;
      line-height: 1.1;
      margin-bottom: 5px;
    }

    .metric span {
      color: var(--muted);
      font-size: 13px;
    }

    .panel {
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      box-shadow: var(--shadow);
      margin-bottom: 16px;
    }

    .panel-head {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      border-bottom: 1px solid var(--line);
      padding: 12px 14px;
    }

    .panel-head h2 {
      margin: 0;
    }

    .panel-body {
      padding: 14px;
    }

    pre {
      margin: 0;
      white-space: pre-wrap;
      overflow-wrap: anywhere;
      font-size: 12px;
      line-height: 1.45;
      max-height: 420px;
      overflow: auto;
      background: #111827;
      color: #edf2f7;
      border-radius: 6px;
      padding: 12px;
    }

    .paths {
      display: grid;
      gap: 8px;
    }

    .path {
      display: flex;
      justify-content: space-between;
      gap: 12px;
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 9px 10px;
      background: #fbfcfd;
    }

    .path code {
      overflow-wrap: anywhere;
      color: #25364f;
    }

    .message {
      border-left: 4px solid var(--blue);
      background: #eef5ff;
      padding: 10px 12px;
      border-radius: 6px;
      color: #193557;
      margin-bottom: 12px;
    }

    .message.error {
      border-left-color: var(--red);
      background: #fff1f2;
      color: #7f1d1d;
    }

    .message.warn {
      border-left-color: var(--amber);
      background: #fff7e6;
      color: #6b4700;
    }

    .hidden {
      display: none;
    }

    @media (max-width: 900px) {
      .app {
        grid-template-columns: 1fr;
      }

      aside {
        border-right: 0;
        border-bottom: 1px solid var(--line);
      }

      .grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
      }
    }

    @media (max-width: 520px) {
      .grid {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
<body>
  <div class="app">
    <aside>
      <div class="brand">
        <h1>OneCompiler Builder</h1>
        <span id="serverState" class="status-pill">Ready</span>
      </div>

      <h2>Source Folders</h2>
      <div id="sources" class="source-list"></div>

      <h2>Generate</h2>
      <div class="field">
        <label for="customInputs">Extra paths</label>
        <textarea id="customInputs" placeholder="Optional file or folder paths, one per line"></textarea>
      </div>
      <div class="field">
        <label for="includeLanguages">Languages</label>
        <input id="includeLanguages" type="text" placeholder="Blank = all supported">
      </div>
      <div class="field">
        <label for="height">Editor height</label>
        <input id="height" type="text" value="350px">
      </div>
      <label class="check">
        <input id="convertUnlabeled" type="checkbox">
        <span>Convert unlabeled code as Python</span>
        <span></span>
      </label>
      <div style="height: 12px"></div>
      <button id="generateBtn" class="button">Generate build</button>

      <h2>Upload</h2>
      <div class="field">
        <label for="subtype">Upload folder</label>
        <input id="subtype" type="text" value="onecompiler-embeds">
      </div>
      <div class="field">
        <label for="token">ByteXL token</label>
        <input id="token" type="password" placeholder="Uses BYTEXL_TOKEN or bytexl_config.json if blank">
      </div>
      <div class="row">
        <button id="dryUploadBtn" class="button secondary">Dry run</button>
        <button id="uploadBtn" class="button danger">Upload</button>
      </div>
    </aside>

    <main>
      <div id="message" class="message hidden"></div>

      <div class="grid">
        <div class="metric"><strong id="filesScanned">0</strong><span>Files scanned</span></div>
        <div class="metric"><strong id="filesChanged">0</strong><span>Files changed</span></div>
        <div class="metric"><strong id="snippets">0</strong><span>Editors generated</span></div>
        <div class="metric"><strong id="skipped">0</strong><span>Blocks skipped</span></div>
      </div>

      <section class="panel">
        <div class="panel-head">
          <h2>Output</h2>
          <button id="refreshBtn" class="button secondary">Refresh</button>
        </div>
        <div class="panel-body">
          <div class="paths">
            <div class="path"><span>Report</span><code id="reportPath">-</code></div>
            <div class="path"><span>Converted Markdown</span><code id="readingPath">-</code></div>
            <div class="path"><span>Uploaded Markdown</span><code id="uploadedPath">-</code></div>
            <div class="path"><span>Wrapper HTML</span><code id="embedPath">-</code></div>
          </div>
        </div>
      </section>

      <section class="panel">
        <div class="panel-head">
          <h2>Last Command</h2>
          <span id="lastExit" class="status-pill">No run yet</span>
        </div>
        <div class="panel-body">
          <pre id="log">No command output yet.</pre>
        </div>
      </section>

      <section class="panel">
        <div class="panel-head">
          <h2>Report</h2>
          <span id="reportStatus" class="status-pill">Not loaded</span>
        </div>
        <div class="panel-body">
          <pre id="report">No report yet.</pre>
        </div>
      </section>
    </main>
  </div>

  <script>
    const $ = (id) => document.getElementById(id);

    function setBusy(isBusy, label = "Working") {
      $("serverState").textContent = isBusy ? label : "Ready";
      ["generateBtn", "dryUploadBtn", "uploadBtn", "refreshBtn"].forEach((id) => {
        $(id).disabled = isBusy;
      });
    }

    function showMessage(text, type = "info") {
      const box = $("message");
      box.textContent = text;
      box.className = `message ${type === "info" ? "" : type}`;
      box.classList.remove("hidden");
    }

    function hideMessage() {
      $("message").classList.add("hidden");
    }

    async function api(path, options = {}) {
      const response = await fetch(path, {
        headers: { "Content-Type": "application/json" },
        ...options
      });
      const payload = await response.json();
      if (!response.ok) {
        if (payload.stdout || payload.stderr || typeof payload.returncode !== "undefined") {
          renderCommand(payload);
          const details = (payload.stderr || payload.stdout || "").trim();
          throw new Error(details || `Command failed with exit ${payload.returncode}`);
        }
        throw new Error(payload.error || `Request failed: ${response.status}`);
      }
      return payload;
    }

    function checkedSources() {
      return Array.from(document.querySelectorAll("input[name='source']:checked")).map((item) => item.value);
    }

    function extraInputs() {
      return $("customInputs").value
        .split("\\n")
        .map((item) => item.trim())
        .filter(Boolean);
    }

    function renderOptions(options) {
      const container = $("sources");
      container.innerHTML = "";
      options.sources.forEach((source) => {
        const label = document.createElement("label");
        label.className = "check";
        label.innerHTML = `
          <input name="source" type="checkbox" value="${source.path}">
          <span title="${source.path}">${source.path}</span>
          <span class="count">${source.markdown_files}</span>
        `;
        const checkbox = label.querySelector("input");
        checkbox.checked = source.default;
        container.appendChild(label);
      });
    }

    function renderSummary(summaryPayload) {
      const summary = summaryPayload.summary || {};
      $("filesScanned").textContent = summary.files_scanned || 0;
      $("filesChanged").textContent = summary.files_changed || 0;
      $("snippets").textContent = summary.snippets_generated || 0;
      $("skipped").textContent = summary.blocks_skipped || 0;
      $("reportPath").textContent = summaryPayload.paths.report || "-";
      $("readingPath").textContent = summaryPayload.paths.reading_material || "-";
      $("uploadedPath").textContent = summaryPayload.paths.uploaded_reading_material || "-";
      $("embedPath").textContent = summaryPayload.paths.onecompiler_embeds || "-";
    }

    function renderCommand(result) {
      $("lastExit").textContent = `Exit ${result.returncode}`;
      $("lastExit").style.color = result.returncode === 0 ? "var(--green)" : "var(--red)";
      $("log").textContent = [result.stdout, result.stderr].filter(Boolean).join("\\n") || "Command finished with no output.";
    }

    async function refresh() {
      const summary = await api("/api/summary");
      renderSummary(summary);
      const report = await api("/api/report");
      $("report").textContent = report.report || "No report yet.";
      $("reportStatus").textContent = report.exists ? "Loaded" : "Missing";
    }

    async function load() {
      const options = await api("/api/options");
      renderOptions(options);
      await refresh();
    }

    $("generateBtn").addEventListener("click", async () => {
      hideMessage();
      setBusy(true, "Generating");
      try {
        const payload = {
          inputs: [...checkedSources(), ...extraInputs()],
          includeLanguages: $("includeLanguages").value.trim(),
          height: $("height").value.trim() || "350px",
          convertUnlabeled: $("convertUnlabeled").checked
        };
        const result = await api("/api/generate", {
          method: "POST",
          body: JSON.stringify(payload)
        });
        renderCommand(result);
        await refresh();
        showMessage("Build generated. Review the report before uploading.");
      } catch (error) {
        showMessage(error.message, "error");
      } finally {
        setBusy(false);
      }
    });

    $("dryUploadBtn").addEventListener("click", async () => {
      hideMessage();
      setBusy(true, "Checking");
      try {
        const result = await api("/api/upload", {
          method: "POST",
          body: JSON.stringify({ dryRun: true, subtype: $("subtype").value.trim() || "onecompiler-embeds" })
        });
        renderCommand(result);
        await refresh();
        showMessage("Dry run completed.");
      } catch (error) {
        showMessage(error.message, "error");
      } finally {
        setBusy(false);
      }
    });

    $("uploadBtn").addEventListener("click", async () => {
      hideMessage();
      const ok = window.confirm("Upload generated wrapper HTML files to ByteXL now?");
      if (!ok) return;
      setBusy(true, "Uploading");
      try {
        const result = await api("/api/upload", {
          method: "POST",
          body: JSON.stringify({
            dryRun: false,
            subtype: $("subtype").value.trim() || "onecompiler-embeds",
            token: $("token").value.trim()
          })
        });
        renderCommand(result);
        await refresh();
        showMessage("Upload finished. Use the uploaded Markdown folder.");
      } catch (error) {
        showMessage(error.message, "error");
      } finally {
        setBusy(false);
      }
    });

    $("refreshBtn").addEventListener("click", async () => {
      hideMessage();
      setBusy(true, "Refreshing");
      try {
        await refresh();
      } catch (error) {
        showMessage(error.message, "error");
      } finally {
        setBusy(false);
      }
    });

    load().catch((error) => showMessage(error.message, "error"));
  </script>
</body>
</html>
"""


def markdown_count(path: Path) -> int:
    ignored = {".git", ".onecompiler_build", "__pycache__", "node_modules"}
    total = 0
    for candidate in path.rglob("*.md"):
        rel_parts = candidate.relative_to(path).parts
        if ignored.intersection(rel_parts):
            continue
        total += 1
    return total


def safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def json_response(handler: BaseHTTPRequestHandler, payload: dict, status: int = 200) -> None:
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


def text_response(handler: BaseHTTPRequestHandler, body: str, content_type: str = "text/html; charset=utf-8") -> None:
    data = body.encode("utf-8")
    handler.send_response(HTTPStatus.OK)
    handler.send_header("Content-Type", content_type)
    handler.send_header("Content-Length", str(len(data)))
    handler.end_headers()
    handler.wfile.write(data)


def ui_html() -> str:
    if SIMPLE_UI_FILE.exists():
        return SIMPLE_UI_FILE.read_text(encoding="utf-8")
    return HTML


def default_wrapper_url() -> str:
    port = int(os.environ.get("ONECOMPILER_UI_PORT", PORT))
    return f"http://127.0.0.1:{port}/embed.html"


def read_body(handler: BaseHTTPRequestHandler) -> dict:
    length = int(handler.headers.get("Content-Length", "0"))
    if length == 0:
        return {}
    raw = handler.rfile.read(length)
    return json.loads(raw.decode("utf-8"))


def current_summary() -> dict:
    manifest_path = BUILD_DIR / "snippets.json"
    summary = {
        "files_scanned": 0,
        "files_changed": 0,
        "snippets_generated": 0,
        "blocks_skipped": 0,
        "languages": {},
    }
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            summary.update(manifest.get("summary", {}))
        except json.JSONDecodeError:
            pass

    return {
        "summary": summary,
        "paths": {
            "report": str(BUILD_DIR / "report.md") if (BUILD_DIR / "report.md").exists() else "",
            "reading_material": str(BUILD_DIR / "reading-material") if (BUILD_DIR / "reading-material").exists() else "",
            "uploaded_reading_material": str(BUILD_DIR / "reading-material-uploaded")
            if (BUILD_DIR / "reading-material-uploaded").exists()
            else "",
            "onecompiler_embeds": str(BUILD_DIR / "onecompiler-embeds")
            if (BUILD_DIR / "onecompiler-embeds").exists()
            else "",
        },
    }


def run_command(command: list[str], timeout: int = 900) -> dict:
    start = time.time()
    completed = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        capture_output=True,
        timeout=timeout,
    )
    return {
        "command": command,
        "returncode": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "elapsedSeconds": round(time.time() - start, 2),
    }


def validate_inputs(items: list[str]) -> list[str]:
    clean: list[str] = []
    for item in items:
        value = str(item).strip()
        if not value:
            continue
        path = Path(value).expanduser()
        if not path.is_absolute():
            path = CONTENT_ROOT / path
        try:
            path.resolve().relative_to(CONTENT_ROOT)
        except ValueError:
            raise ValueError(f"Path is outside the workspace: {value}")
        if not path.exists():
            raise ValueError(f"Path does not exist: {value}")
        clean.append(str(path.relative_to(CONTENT_ROOT)))
    return clean


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt: str, *args) -> None:
        timestamp = time.strftime("%H:%M:%S")
        print(f"[{timestamp}] {fmt % args}")

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        try:
            if parsed.path == "/":
                text_response(self, ui_html())
            elif parsed.path == "/embed.html":
                if not EMBED_WRAPPER_FILE.exists():
                    raise FileNotFoundError(f"Missing wrapper page: {EMBED_WRAPPER_FILE}")
                text_response(self, EMBED_WRAPPER_FILE.read_text(encoding="utf-8"))
            elif parsed.path == "/api/options":
                sources = []
                for child in sorted(CONTENT_ROOT.iterdir()):
                    if not child.is_dir() or child.name.startswith("."):
                        continue
                    count = markdown_count(child)
                    if count == 0:
                        continue
                    sources.append(
                        {
                            "path": child.name,
                            "markdown_files": count,
                            "default": child.name in {"Semester 1", "Semester 2"},
                        }
                    )
                json_response(self, {"sources": sources})
            elif parsed.path == "/api/summary":
                json_response(self, current_summary())
            elif parsed.path == "/api/report":
                report_path = BUILD_DIR / "report.md"
                if report_path.exists():
                    json_response(self, {"exists": True, "report": report_path.read_text(encoding="utf-8")})
                else:
                    json_response(self, {"exists": False, "report": ""})
            else:
                json_response(self, {"error": "Not found"}, HTTPStatus.NOT_FOUND)
        except Exception as exc:
            json_response(self, {"error": str(exc)}, HTTPStatus.INTERNAL_SERVER_ERROR)

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        try:
            payload = read_body(self)
            if parsed.path == "/api/generate":
                with LOCK:
                    inputs = validate_inputs(payload.get("inputs", []))
                    if not inputs:
                        raise ValueError("Select at least one source folder or path.")

                    command = [sys.executable, "generate_onecompiler_embeds.py", *inputs]
                    include_languages = str(payload.get("includeLanguages", "")).strip()
                    height = str(payload.get("height", "350px")).strip() or "350px"
                    wrapper_url = str(payload.get("wrapperUrl", "")).strip() or default_wrapper_url()
                    if not re.match(r"^https?://", wrapper_url):
                        raise ValueError("Wrapper URL must start with http:// or https://")
                    command.extend(["--height", height])
                    command.extend(["--embed-strategy", "encoded-url", "--wrapper-url", wrapper_url])
                    if include_languages:
                        if not re.fullmatch(r"[a-zA-Z0-9_,+.# -]+", include_languages):
                            raise ValueError("Language filter contains unsupported characters.")
                        command.extend(["--include-languages", include_languages])
                    if payload.get("convertUnlabeled"):
                        command.append("--convert-unlabeled")

                    result = run_command(command)
                    json_response(self, result)
            elif parsed.path == "/api/upload":
                with LOCK:
                    command = [sys.executable, "upload_onecompiler_embeds.py"]
                    subtype = str(payload.get("subtype", "onecompiler-embeds")).strip() or "onecompiler-embeds"
                    command.extend(["--subtype", subtype])
                    if payload.get("dryRun"):
                        command.append("--dry-run")
                    token = str(payload.get("token", "")).strip()
                    if token and not payload.get("dryRun"):
                        command.extend(["--token", token])

                    result = run_command(command, timeout=1800)
                    json_response(self, result)
            else:
                json_response(self, {"error": "Not found"}, HTTPStatus.NOT_FOUND)
        except Exception as exc:
            json_response(self, {"error": str(exc)}, HTTPStatus.BAD_REQUEST)


def main() -> None:
    port = int(os.environ.get("ONECOMPILER_UI_PORT", PORT))
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    url = f"http://127.0.0.1:{port}"
    print(f"OneCompiler Builder UI running at {url}")
    print("Press Ctrl+C to stop.")
    if "--no-open" not in sys.argv:
        threading.Timer(0.5, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
