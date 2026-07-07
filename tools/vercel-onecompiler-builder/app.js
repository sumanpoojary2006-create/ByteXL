const LANGUAGE_ALIASES = {
  py: "python",
  python3: "python",
  python2: "python2",
  js: "javascript",
  node: "nodejs",
  "node.js": "nodejs",
  ts: "typescript",
  java: "java",
  c: "c",
  "c++": "cpp",
  cpp: "cpp",
  cc: "cpp",
  cxx: "cpp",
  "c#": "csharp",
  cs: "csharp",
  csharp: "csharp",
  html: "html",
  html5: "html",
  php: "php",
  rb: "ruby",
  ruby: "ruby",
  go: "go",
  golang: "go",
  rs: "rust",
  rust: "rust",
  kt: "kotlin",
  kotlin: "kotlin",
  scala: "scala",
  swift: "swift",
  r: "r",
  perl: "perl",
  pl: "perl",
  bash: "bash",
  shell: "bash",
  sh: "sh",
  sql: "mysql",
  mysql: "mysql",
  postgres: "postgresql",
  postgresql: "postgresql",
  sqlite: "sqlite",
  mongodb: "mongodb",
  mongo: "mongodb",
  lua: "lua",
  dart: "dart",
  julia: "julia",
  groovy: "groovy",
  haskell: "haskell",
  hs: "haskell",
  clojure: "clojure",
  ex: "elixir",
  elixir: "elixir",
  erl: "erlang",
  erlang: "erlang",
  fsharp: "fsharp",
  fs: "fsharp",
  vb: "vb",
  v: "v",
  zig: "zig",
  nim: "nim",
  pascal: "pascal",
  fortran: "fortran",
  cobol: "cobol",
  racket: "racket",
  scheme: "scheme",
  tcl: "tcl",
  awk: "awk",
  matplotlib: "matplotlib",
  seaborn: "seaborn",
  tkinter: "tkinter",
  pygame: "pygame"
};

const ONECOMPILER_LANGUAGES = new Set([
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
  "zig"
]);

const DEFAULT_SKIP_LANGUAGES = new Set([
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
  "yml"
]);

const FILE_EXTENSIONS = {
  bash: "sh",
  c: "c",
  cpp: "cpp",
  csharp: "cs",
  go: "go",
  html: "html",
  java: "java",
  javascript: "js",
  kotlin: "kt",
  mysql: "sql",
  nodejs: "js",
  php: "php",
  postgresql: "sql",
  python: "py",
  python2: "py",
  r: "r",
  ruby: "rb",
  rust: "rs",
  scala: "scala",
  sh: "sh",
  sqlite: "sql",
  swift: "swift",
  typescript: "ts"
};

const state = {
  entries: [],
  outputBlob: null,
  outputUrl: "",
  lastReport: ""
};

const $ = (id) => document.getElementById(id);

function init() {
  $("wrapperUrl").value = new URL("./embed.html", window.location.href).href;
  initSuiteLinks();

  $("folderBtn").addEventListener("click", () => $("folderInput").click());
  $("filesBtn").addEventListener("click", () => $("filesInput").click());
  $("clearBtn").addEventListener("click", clearAll);
  $("generateBtn").addEventListener("click", generateZip);
  $("downloadBtn").addEventListener("click", downloadOutput);
  $("folderInput").addEventListener("change", (event) => loadFileList(event.target.files, "folder"));
  $("filesInput").addEventListener("change", (event) => loadFileList(event.target.files, "files"));

  const dropZone = $("dropZone");
  dropZone.addEventListener("click", () => $("filesInput").click());
  dropZone.addEventListener("keydown", (event) => {
    if (event.key === "Enter" || event.key === " ") {
      event.preventDefault();
      $("filesInput").click();
    }
  });
  ["dragenter", "dragover"].forEach((name) => {
    dropZone.addEventListener(name, (event) => {
      event.preventDefault();
      dropZone.classList.add("is-over");
    });
  });
  ["dragleave", "drop"].forEach((name) => {
    dropZone.addEventListener(name, () => dropZone.classList.remove("is-over"));
  });
  dropZone.addEventListener("drop", (event) => {
    event.preventDefault();
    loadFileList(event.dataTransfer.files, "drop");
  });

  renderIcons();
  renderLoadedSummary();
}

function initSuiteLinks() {
  const link = $("codingUploaderLink");
  if (!link) return;

  const params = new URLSearchParams(window.location.search);
  const requestedUrl = params.get("codingUploaderUrl");
  const storageKey = "bytexlCodingUploaderUrl";

  try {
    if (requestedUrl) {
      localStorage.setItem(storageKey, requestedUrl);
    }
    link.href = localStorage.getItem(storageKey) || link.dataset.defaultHref || link.href;
  } catch {
    link.href = requestedUrl || link.dataset.defaultHref || link.href;
  }
}

function renderIcons() {
  if (window.lucide) {
    window.lucide.createIcons();
  }
}

async function loadFileList(fileList, sourceType) {
  try {
    if (!window.JSZip) {
      throw new Error("ZIP library did not load. Refresh the page and try again.");
    }

    const files = Array.from(fileList || []);
    if (!files.length) return;

    resetOutput();
    setStatus("Loading files...", "warn");

    const entries = [];
    for (const file of files) {
      if (looksLikeZip(file)) {
        const zipEntries = await loadZipFile(file, files.length > 1 ? stripExtension(file.name) : "");
        entries.push(...zipEntries);
      } else {
        const path = normalizePath(sourceType === "folder" ? file.webkitRelativePath || file.name : file.name);
        if (!shouldIgnorePath(path)) {
          entries.push({ path, type: "file", source: file, size: file.size });
        }
      }
    }

    state.entries = dedupeEntries(entries);
    if (!state.entries.length) {
      throw new Error("No usable files found.");
    }

    renderLoadedSummary();
    setStatus(`Loaded ${state.entries.length} file(s).`, "ok");
    $("dropZone").classList.add("has-files");
    $("generateBtn").disabled = markdownEntries().length === 0;
  } catch (error) {
    setStatus(error.message, "error");
  } finally {
    $("folderInput").value = "";
    $("filesInput").value = "";
  }
}

async function loadZipFile(file, prefix) {
  const zip = await window.JSZip.loadAsync(file);
  const entries = [];
  zip.forEach((relativePath, zipEntry) => {
    const path = normalizePath(prefix ? `${prefix}/${relativePath}` : relativePath);
    if (!zipEntry.dir && !shouldIgnorePath(path)) {
      entries.push({ path, type: "zip", source: zipEntry, size: 0 });
    }
  });
  return entries;
}

function dedupeEntries(entries) {
  const seen = new Map();
  for (const entry of entries) {
    let path = entry.path;
    if (seen.has(path)) {
      const dot = path.lastIndexOf(".");
      const base = dot > -1 ? path.slice(0, dot) : path;
      const ext = dot > -1 ? path.slice(dot) : "";
      let index = 2;
      while (seen.has(`${base}-${index}${ext}`)) index += 1;
      path = `${base}-${index}${ext}`;
    }
    seen.set(path, { ...entry, path });
  }
  return Array.from(seen.values()).sort((a, b) => a.path.localeCompare(b.path, undefined, { numeric: true, sensitivity: "base" }));
}

async function generateZip() {
  try {
    if (!state.entries.length) {
      throw new Error("Upload files first.");
    }

    const mdEntries = markdownEntries();
    if (!mdEntries.length) {
      throw new Error("No Markdown files found.");
    }

    resetOutput();
    setControlsBusy(true);
    setStatus("Converting Markdown...", "warn");

    const settings = readSettings();
    const outputZip = new window.JSZip();
    const changedFiles = [];
    const skippedBlocks = [];
    const languageCounts = {};
    const longUrls = [];
    const fileWarnings = [];
    let editorsGenerated = 0;

    for (let index = 0; index < state.entries.length; index += 1) {
      const entry = state.entries[index];
      if (isMarkdownPath(entry.path)) {
        const original = await readEntryAsText(entry);
        const result = convertMarkdown(original, entry.path, settings);
        outputZip.file(entry.path, result.markdown);
        if (result.convertedBlocks > 0) {
          changedFiles.push({ path: entry.path, editors: result.convertedBlocks });
        }
        for (const item of result.skippedBlocks) skippedBlocks.push(item);
        for (const item of result.longUrls) longUrls.push(item);
        for (const item of result.fileWarnings) fileWarnings.push(item);
        editorsGenerated += result.convertedBlocks;
        for (const [language, count] of Object.entries(result.languageCounts)) {
          languageCounts[language] = (languageCounts[language] || 0) + count;
        }
      } else {
        outputZip.file(entry.path, await readEntryAsArrayBuffer(entry));
      }
      setStatus(`Processed ${index + 1} of ${state.entries.length} file(s)...`, "warn");
    }

    const summary = {
      filesLoaded: state.entries.length,
      markdownFiles: mdEntries.length,
      filesChanged: changedFiles.length,
      editorsGenerated,
      skippedBlocks: skippedBlocks.length,
      fileWarnings: fileWarnings.length,
      wrapperUrl: settings.wrapperUrl,
      languages: languageCounts,
      longUrls
    };

    const report = buildReport(summary, changedFiles, skippedBlocks, fileWarnings);
    state.lastReport = report;
    outputZip.file("onecompiler-report.md", report);
    outputZip.file(
      "onecompiler-manifest.json",
      JSON.stringify({ summary, changedFiles, skippedBlocks, fileWarnings }, null, 2)
    );

    setStatus("Creating ZIP...", "warn");
    state.outputBlob = await outputZip.generateAsync({ type: "blob" }, (metadata) => {
      setStatus(`Creating ZIP ${Math.round(metadata.percent)}%...`, "warn");
    });
    state.outputUrl = URL.createObjectURL(state.outputBlob);

    $("editorCount").textContent = String(editorsGenerated);
    $("skippedCount").textContent = String(skippedBlocks.length);
    $("downloadBtn").disabled = false;
    $("report").textContent = report;
    $("reportState").textContent = "Ready";
    $("reportState").className = "status-ok";
    setStatus(`Ready: ${editorsGenerated} editor(s) generated.`, "ok");
  } catch (error) {
    setStatus(error.message, "error");
    $("reportState").textContent = "Error";
    $("reportState").className = "status-error";
  } finally {
    setControlsBusy(false);
  }
}

function convertMarkdown(markdown, filePath, settings) {
  const blocks = iterFencedBlocks(markdown);
  const replacements = [];
  const skippedBlocks = [];
  const longUrls = [];
  const fileWarnings = [];
  const languageCounts = {};
  let convertedBlocks = 0;
  let fileBlockIndex = 0;

  // Pass 1: collect every `file=<name>` block into a per-document registry.
  // These blocks are never converted into their own iframe, regardless of
  // language, so a `python file=billing.py` block is not mistaken for a
  // runnable snippet.
  const fileRegistry = new Map();
  for (const block of blocks) {
    const { attrs } = parseBlockInfo(block.info);
    if (attrs.file) {
      fileRegistry.set(attrs.file, block.code.replace(/\n+$/, ""));
    }
  }

  // Pass 2: convert runnable blocks, resolving `with=` references against
  // the registry built above.
  for (const block of blocks) {
    const { language: rawLanguage, attrs } = parseBlockInfo(block.info);
    if (attrs.file) {
      continue;
    }

    const decision = shouldConvert(rawLanguage, block.code, settings);
    if (!decision.convert) {
      skippedBlocks.push({
        file: filePath,
        lines: `${block.startLine}-${block.endLine}`,
        language: decision.language || "(none)",
        reason: decision.reason
      });
      continue;
    }

    const extraFiles = [];
    if (attrs.with) {
      for (const name of attrs.with.split(",").map((item) => item.trim()).filter(Boolean)) {
        if (fileRegistry.has(name)) {
          extraFiles.push({ name, content: fileRegistry.get(name) });
        } else {
          fileWarnings.push({
            file: filePath,
            lines: `${block.startLine}-${block.endLine}`,
            name
          });
        }
      }
    }

    fileBlockIndex += 1;
    convertedBlocks += 1;
    const language = decision.language;
    const snippet = {
      title: `${baseNameWithoutExtension(filePath)} code ${fileBlockIndex}`,
      language,
      filename: filenameFor(language, fileBlockIndex),
      code: block.code.replace(/\n+$/, ""),
      extraFiles
    };
    const src = encodedWrapperSrc(snippet, settings.wrapperUrl);
    if (src.length > 8000) {
      longUrls.push({ file: filePath, lines: `${block.startLine}-${block.endLine}`, length: src.length });
    }
    replacements.push([block.start, block.end, iframeHtml(src, settings.height)]);
    languageCounts[language] = (languageCounts[language] || 0) + 1;
  }

  let converted = markdown;
  for (const [start, end, replacement] of replacements.reverse()) {
    converted = converted.slice(0, start) + replacement + converted.slice(end);
  }

  return {
    markdown: converted,
    convertedBlocks,
    skippedBlocks,
    languageCounts,
    longUrls,
    fileWarnings
  };
}

function parseBlockInfo(info) {
  const tokens = (info || "").trim().split(/\s+/).filter(Boolean);
  const languageToken = tokens[0] || "";
  const cleaned = languageToken.replace(/^[{.]+|[}.]+$/g, "").toLowerCase().replace(/^language-/, "");
  const language = cleaned ? (LANGUAGE_ALIASES[cleaned] || cleaned) : null;

  const attrs = {};
  for (const token of tokens.slice(1)) {
    const match = token.match(/^([a-zA-Z][\w-]*)=(.+)$/);
    if (match) {
      attrs[match[1]] = match[2];
    }
  }

  return { language, attrs };
}

function iterFencedBlocks(markdown) {
  const lines = markdown.match(/[^\n]*\n|[^\n]+$/g) || [];
  const offsets = [];
  let position = 0;
  for (const line of lines) {
    offsets.push(position);
    position += line.length;
  }

  const blocks = [];
  let index = 0;
  while (index < lines.length) {
    const startMatch = lines[index].match(/^[ \t]{0,3}(`{3,}|~{3,})([^\r\n]*)/);
    if (!startMatch) {
      index += 1;
      continue;
    }

    const fence = startMatch[1];
    const fenceChar = fence[0];
    const fenceLength = fence.length;
    const info = (startMatch[2] || "").trim();
    const closeRe = new RegExp(`^[ \\t]{0,3}${escapeRegExp(fenceChar)}{${fenceLength},}[ \\t]*\\r?\\n?$`);

    let closeIndex = index + 1;
    while (closeIndex < lines.length && !closeRe.test(lines[closeIndex])) {
      closeIndex += 1;
    }
    if (closeIndex >= lines.length) {
      index += 1;
      continue;
    }

    const codeStart = offsets[index] + lines[index].length;
    const codeEnd = offsets[closeIndex];
    const blockEnd = offsets[closeIndex] + lines[closeIndex].length;
    blocks.push({
      start: offsets[index],
      end: blockEnd,
      startLine: index + 1,
      endLine: closeIndex + 1,
      info,
      code: markdown.slice(codeStart, codeEnd)
    });
    index = closeIndex + 1;
  }

  return blocks;
}

function shouldConvert(language, code, settings) {
  if (!code.trim()) {
    return { convert: false, language, reason: "empty" };
  }

  let selectedLanguage = language;
  if (!selectedLanguage) {
    if (!settings.convertUnlabeled) {
      return { convert: false, language, reason: "unlabeled" };
    }
    selectedLanguage = "python";
  }

  if (DEFAULT_SKIP_LANGUAGES.has(selectedLanguage)) {
    return { convert: false, language: selectedLanguage, reason: "skipped-language" };
  }

  if (settings.includeLanguages && !settings.includeLanguages.has(selectedLanguage)) {
    return { convert: false, language: selectedLanguage, reason: "not-in-include-list" };
  }

  if (!ONECOMPILER_LANGUAGES.has(selectedLanguage)) {
    return { convert: false, language: selectedLanguage, reason: "unsupported-language" };
  }

  return { convert: true, language: selectedLanguage, reason: "converted" };
}

function readSettings() {
  const wrapperUrl = $("wrapperUrl").value.trim() || new URL("./embed.html", window.location.href).href;
  if (!/^https?:\/\//i.test(wrapperUrl)) {
    throw new Error("Wrapper URL must start with http:// or https://.");
  }

  const height = $("height").value.trim() || "350px";
  const languages = $("languages").value.trim();
  return {
    wrapperUrl,
    height,
    includeLanguages: languages ? parseLanguageSet(languages) : null,
    convertUnlabeled: $("convertUnlabeled").checked
  };
}

function parseLanguageSet(value) {
  const result = new Set();
  for (const item of value.split(",")) {
    const language = normalizeLanguage(item);
    if (language) result.add(language);
  }
  return result;
}

function normalizeLanguage(info) {
  const token = (info || "").trim().split(/\s+/, 1)[0];
  if (!token) return null;
  const cleaned = token.replace(/^[{.]+|[}.]+$/g, "").toLowerCase().replace(/^language-/, "");
  return LANGUAGE_ALIASES[cleaned] || cleaned;
}

function encodedWrapperSrc(snippet, wrapperUrl) {
  const raw = JSON.stringify(snippet);
  const token = base64UrlEncode(raw);
  return `${wrapperUrl.split("#", 1)[0]}#${token}`;
}

function base64UrlEncode(value) {
  const bytes = new TextEncoder().encode(value);
  let binary = "";
  const chunkSize = 0x8000;
  for (let index = 0; index < bytes.length; index += chunkSize) {
    const chunk = bytes.subarray(index, index + chunkSize);
    binary += String.fromCharCode(...chunk);
  }
  return btoa(binary).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}

function iframeHtml(src, height) {
  return `<iframe
 frameBorder="0"
 height="${escapeAttribute(height)}"
 src="${escapeAttribute(src)}"
 width="100%"
></iframe>
`;
}

function filenameFor(language, index) {
  if (language === "java") return "Main.java";
  const extension = FILE_EXTENSIONS[language] || language;
  return `main_${String(index).padStart(3, "0")}.${extension}`;
}

function buildReport(summary, changedFiles, skippedBlocks, fileWarnings) {
  const lines = [
    "# OneCompiler Browser Conversion Report",
    "",
    "## Summary",
    "",
    `- Wrapper URL: ${summary.wrapperUrl}`,
    `- Files loaded: ${summary.filesLoaded}`,
    `- Markdown files: ${summary.markdownFiles}`,
    `- Markdown files changed: ${summary.filesChanged}`,
    `- Code editors generated: ${summary.editorsGenerated}`,
    `- Blocks skipped: ${summary.skippedBlocks}`,
    `- File reference warnings: ${summary.fileWarnings}`,
    "",
    "## Languages Converted",
    ""
  ];

  const languageEntries = Object.entries(summary.languages).sort((a, b) => a[0].localeCompare(b[0]));
  if (languageEntries.length) {
    for (const [language, count] of languageEntries) {
      lines.push(`- ${language}: ${count}`);
    }
  } else {
    lines.push("- None");
  }

  if (summary.longUrls.length) {
    lines.push("", "## URL Length Warnings", "");
    for (const item of summary.longUrls.slice(0, 100)) {
      lines.push(`- ${item.file}, lines ${item.lines}: ${item.length} characters`);
    }
  }

  lines.push("", "## Changed Files", "");
  if (changedFiles.length) {
    lines.push("| File | Editors |");
    lines.push("|---|---:|");
    for (const item of changedFiles.slice(0, 500)) {
      lines.push(`| \`${item.path}\` | ${item.editors} |`);
    }
    if (changedFiles.length > 500) {
      lines.push(`| ... | ${changedFiles.length - 500} more omitted |`);
    }
  } else {
    lines.push("No files were changed.");
  }

  lines.push("", "## Skipped Blocks", "");
  if (skippedBlocks.length) {
    lines.push("| File | Lines | Language | Reason |");
    lines.push("|---|---:|---|---|");
    for (const item of skippedBlocks.slice(0, 500)) {
      lines.push(`| \`${item.file}\` | ${item.lines} | \`${item.language}\` | ${item.reason} |`);
    }
    if (skippedBlocks.length > 500) {
      lines.push(`| ... | ... | ... | ${skippedBlocks.length - 500} more omitted |`);
    }
  } else {
    lines.push("No skipped blocks.");
  }

  lines.push("", "## File Reference Warnings", "");
  if (fileWarnings && fileWarnings.length) {
    lines.push("A `with=` block referenced a filename with no matching `file=` definition anywhere in that document. Check for typos or missing fixture blocks.");
    lines.push("");
    lines.push("| File | Lines | Missing name |");
    lines.push("|---|---:|---|");
    for (const item of fileWarnings.slice(0, 500)) {
      lines.push(`| \`${item.file}\` | ${item.lines} | \`${item.name}\` |`);
    }
    if (fileWarnings.length > 500) {
      lines.push(`| ... | ... | ${fileWarnings.length - 500} more omitted |`);
    }
  } else {
    lines.push("No file reference warnings.");
  }

  lines.push("");
  return lines.join("\n");
}

function markdownEntries() {
  return state.entries.filter((entry) => isMarkdownPath(entry.path));
}

function renderLoadedSummary() {
  const mdCount = markdownEntries().length;
  $("fileCount").textContent = String(state.entries.length);
  $("markdownCount").textContent = String(mdCount);
  $("editorCount").textContent = "0";
  $("skippedCount").textContent = "0";
  $("generateBtn").disabled = mdCount === 0;
}

function setControlsBusy(isBusy) {
  $("folderBtn").disabled = isBusy;
  $("filesBtn").disabled = isBusy;
  $("generateBtn").disabled = isBusy || markdownEntries().length === 0;
  $("clearBtn").disabled = isBusy;
}

function setStatus(text, type) {
  $("statusText").textContent = text;
  $("statusText").className = type === "error" ? "status-error" : type === "ok" ? "status-ok" : "status-warn";
}

function resetOutput() {
  if (state.outputUrl) URL.revokeObjectURL(state.outputUrl);
  state.outputBlob = null;
  state.outputUrl = "";
  state.lastReport = "";
  $("downloadBtn").disabled = true;
  $("report").textContent = state.entries.length ? "Ready to generate." : "Upload reading material to begin.";
  $("reportState").textContent = state.entries.length ? "Ready" : "Waiting";
  $("reportState").className = "";
  $("editorCount").textContent = "0";
  $("skippedCount").textContent = "0";
}

function clearAll() {
  state.entries = [];
  resetOutput();
  renderLoadedSummary();
  $("dropZone").classList.remove("has-files");
  setStatus("No files loaded yet.", "warn");
}

function downloadOutput() {
  if (!state.outputUrl) return;
  const link = document.createElement("a");
  link.href = state.outputUrl;
  link.download = "onecompiler-reading-material.zip";
  document.body.appendChild(link);
  link.click();
  link.remove();
}

async function readEntryAsText(entry) {
  if (entry.type === "zip") {
    return entry.source.async("text");
  }
  return entry.source.text();
}

async function readEntryAsArrayBuffer(entry) {
  if (entry.type === "zip") {
    return entry.source.async("arraybuffer");
  }
  return entry.source.arrayBuffer();
}

function isMarkdownPath(path) {
  return /\.(md|markdown)$/i.test(path);
}

function looksLikeZip(file) {
  return /\.zip$/i.test(file.name || "") || file.type === "application/zip";
}

function normalizePath(path) {
  return String(path || "")
    .replace(/\\/g, "/")
    .replace(/^\/+/, "")
    .replace(/^\.\//, "")
    .split("/")
    .filter(Boolean)
    .join("/");
}

function shouldIgnorePath(path) {
  const parts = normalizePath(path).split("/");
  if (!parts.length) return true;
  if (parts.includes("__MACOSX")) return true;
  if (parts.includes(".git")) return true;
  if (parts.includes(".onecompiler_build")) return true;
  if (parts.includes("node_modules")) return true;
  return parts[parts.length - 1] === ".DS_Store";
}

function stripExtension(path) {
  const name = normalizePath(path).split("/").pop() || "archive";
  return name.replace(/\.[^.]+$/, "");
}

function baseNameWithoutExtension(path) {
  return stripExtension(path).replace(/[_-]+/g, " ").trim() || "code";
}

function escapeRegExp(value) {
  return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function escapeAttribute(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/"/g, "&quot;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

document.addEventListener("DOMContentLoaded", init);
