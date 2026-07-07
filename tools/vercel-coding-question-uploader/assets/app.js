const LANGUAGE_ALIASES = {
  py: "python",
  python3: "python",
  python: "python",
  js: "javascript",
  javascript: "javascript",
  node: "javascript",
  nodejs: "javascript",
  c: "c",
  "c++": "cpp",
  cpp: "cpp",
  java: "java",
  shell: "sh",
  bash: "sh",
  sh: "sh",
  sql: "sql",
  mysql: "sql",
  plsql: "plsql",
  mongodb: "mongodb",
  mongo: "mongodb",
  sqlite: "sqlite",
  postgresql: "postgresql",
  postgres: "postgresql",
  html: "html"
};

const SUBTYPE_LANGUAGES = {
  programming: ["c", "cpp", "java", "python", "javascript", "sh"],
  web: ["html"],
  db: ["sql", "plsql", "mongodb", "sqlite", "postgresql"]
};

const DEFAULT_PRELOADS = {
  c: "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
  cpp: "#include <iostream>\nusing namespace std;\n\nint main() {\n    return 0;\n}",
  java: "import java.util.*;\n\nclass Main {\n    public static void main(String[] args) {\n    }\n}",
  python: "",
  javascript: "const fs = require('fs');\nconst input = fs.readFileSync(0, 'utf-8');",
  sh: "#!/bin/sh",
  html: "<!doctype html>\n<html>\n<body>\n</body>\n</html>",
  sql: "SELECT * FROM users;",
  plsql: "BEGIN\n  NULL;\nEND;\n/",
  mongodb: "db.collection.find({});",
  sqlite: "SELECT 1;",
  postgresql: "SELECT 1;"
};

const REQUIRED_COLUMNS = [
  "title",
  "description",
  "score",
  "status",
  "difficulty",
  "bloomTaxonomy",
  "subjects",
  "topics",
  "subTopics",
  "codingType",
  "language"
];

const state = {
  fileName: "",
  rawRows: [],
  questions: [],
  validated: false,
  uploaded: false,
  lastUploadResult: null
};

const $ = (id) => document.getElementById(id);

function init() {
  initSuiteLinks();

  $("dropZone").addEventListener("click", () => $("fileInput").click());
  $("dropZone").addEventListener("keydown", (event) => {
    if (event.key === "Enter" || event.key === " ") {
      event.preventDefault();
      $("fileInput").click();
    }
  });
  $("fileInput").addEventListener("change", (event) => loadFile(event.target.files[0]));

  ["dragenter", "dragover"].forEach((name) => {
    $("dropZone").addEventListener(name, (event) => {
      event.preventDefault();
      $("dropZone").classList.add("is-over");
    });
  });
  ["dragleave", "drop"].forEach((name) => {
    $("dropZone").addEventListener(name, () => $("dropZone").classList.remove("is-over"));
  });
  $("dropZone").addEventListener("drop", (event) => {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    loadFile(file);
  });

  $("publicCount").addEventListener("change", rebuildFromRows);
  $("respectAllLanguages").addEventListener("change", rebuildFromRows);
  $("validateBtn").addEventListener("click", validateWithByteXL);
  $("uploadBtn").addEventListener("click", uploadToByteXL);
  $("downloadBtn").addEventListener("click", downloadJson);
  $("clearBtn").addEventListener("click", clearAll);

  render();
  renderIcons();
}

function initSuiteLinks() {
  const link = $("readingUploaderLink");
  if (!link) return;

  const params = new URLSearchParams(window.location.search);
  const requestedUrl = params.get("readingUploaderUrl");
  const storageKey = "bytexlReadingUploaderUrlV2";

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

async function loadFile(file) {
  if (!file) return;

  try {
    setBusy(true, "Reading");
    state.fileName = file.name;
    state.validated = false;
    state.uploaded = false;
    state.lastUploadResult = null;

    const buffer = await file.arrayBuffer();
    const workbook = XLSX.read(buffer, { type: "array", cellDates: false });
    const sheetName = workbook.SheetNames[0];
    const sheet = workbook.Sheets[sheetName];
    state.rawRows = XLSX.utils.sheet_to_json(sheet, { defval: "", raw: false });
    rebuildFromRows();
    log(`Loaded ${state.rawRows.length} row(s) from ${file.name}.`);
    showMessage(`Loaded ${state.rawRows.length} question row(s).`, "success");
  } catch (error) {
    showMessage(error.message || "Could not read file.", "error");
    log(`ERROR: ${error.message || error}`);
  } finally {
    setBusy(false);
  }
}

function rebuildFromRows() {
  if (!state.rawRows.length) {
    render();
    return;
  }

  const seenTitles = new Map();
  const headers = Object.keys(state.rawRows[0] || {});
  const missingColumns = REQUIRED_COLUMNS.filter((column) => !headers.includes(column));

  state.questions = state.rawRows
    .filter((row) => Object.values(row).some((value) => clean(value) !== ""))
    .map((row, index) => {
      const built = buildQuestion(row, index + 2);
      built.errors.push(...missingColumns.map((column) => `Missing column: ${column}`));

      const titleKey = built.payload.title.toLowerCase();
      if (titleKey) {
        if (seenTitles.has(titleKey)) {
          built.warnings.push(`Duplicate title also appears on row ${seenTitles.get(titleKey)}.`);
        } else {
          seenTitles.set(titleKey, index + 2);
        }
      }

      return built;
    });

  state.validated = false;
  state.uploaded = false;
  render();
}

function buildQuestion(row, rowNumber) {
  const errors = [];
  const warnings = [];
  const codingType = normalizeCodingType(row.codingType);
  const language = normalizeLanguage(row.language) || inferLanguageFromColumns(row) || "python";
  const allSupported = $("respectAllLanguages").checked && toBool(row.supportAllLanguages, false);
  const supportedLanguages = allSupported ? SUBTYPE_LANGUAGES[codingType] : [language];
  const testCases = extractTestCases(row, rowNumber);
  const preloads = buildLanguageMap(row, "preloadCode", supportedLanguages, true);
  const codeSolutions = buildLanguageMap(row, "solution", supportedLanguages, false);
  const hints = splitHints(row.hints);

  if (!clean(row.title)) errors.push("Title is required.");
  if (!clean(row.description)) errors.push("Description is required.");
  if (toNumber(row.score, 0) <= 0) errors.push("Score must be greater than 0.");
  if (!clean(row.status)) errors.push("Status is required.");
  if (!clean(row.difficulty)) errors.push("Difficulty is required.");
  if (!clean(row.bloomTaxonomy)) warnings.push("Bloom taxonomy is blank; using apply.");
  if (!splitList(row.subjects).length) errors.push("At least one subject is required.");
  if (!splitList(row.topics).length) errors.push("At least one topic is required.");
  if (!splitList(row.subTopics).length) errors.push("At least one subTopic is required.");
  if (!SUBTYPE_LANGUAGES[codingType].includes(language) && !allSupported) {
    errors.push(`Language ${language} is not valid for ${codingType}.`);
  }
  if (!testCases.length) errors.push("At least one testcase is required.");
  if (testCases.some((testCase) => clean(testCase.output) === "")) {
    errors.push("Every testcase must have an output.");
  }
  if (!Object.values(codeSolutions).some((value) => clean(value) !== "")) {
    warnings.push("No solution code found.");
  }
  if (allSupported && Object.keys(codeSolutions).length < supportedLanguages.length) {
    warnings.push("supportAllLanguages is true, but not every language has a solution column.");
  }

  const payload = {
    title: clean(row.title),
    description: clean(row.description),
    explanation: clean(row.explanation),
    score: toNumber(row.score, 5),
    type: "coding",
    subType: codingType,
    difficulty: normalizeToken(row.difficulty, "easy"),
    bloomTaxonomy: normalizeToken(row.bloomTaxonomy, "apply"),
    tags: splitList(row.tags),
    subjects: splitList(row.subjects),
    topics: splitList(row.topics),
    subTopics: splitList(row.subTopics),
    companies: splitList(row.companies),
    status: normalizeStatus(row.status),
    submit: null,
    partialScore: toBool(row.enablePartialScore, true),
    codeOptions: {
      supportedLanguages,
      testCases,
      preloads,
      codeSolutions,
      hints,
      ignoreCase: toBool(row.ignoreCase, true),
      privileged: false,
      setupFiles: []
    },
    multipleChoiceOptions: {
      selectionType: "single",
      options: ["", "", "", ""],
      answer: []
    },
    fillInTheBlankOptions: {
      answer: ""
    },
    descriptiveOptions: {
      answerTags: []
    }
  };

  return {
    rowNumber,
    source: row,
    payload,
    errors,
    warnings,
    bytexlErrors: [],
    uploadedId: ""
  };
}

function extractTestCases(row, rowNumber) {
  const numbers = new Set();
  Object.keys(row).forEach((key) => {
    const match = key.match(/^testcase(\d+)_(input|output|explanation|timeLimit|memoryLimit)$/i);
    if (match) numbers.add(Number(match[1]));
  });

  return [...numbers]
    .sort((a, b) => a - b)
    .map((number, index) => {
      const input = clean(row[`testcase${number}_input`]);
      const output = clean(row[`testcase${number}_output`]);
      const explanation = clean(row[`testcase${number}_explanation`]);
      const timeLimit = toOptionalNumber(row[`testcase${number}_timeLimit`]);
      const memoryLimit = toOptionalNumber(row[`testcase${number}_memoryLimit`]);

      if (!input && !output && !explanation && !timeLimit && !memoryLimit) {
        return null;
      }

      const testCase = {
        id: makeLocalId(rowNumber, number),
        input,
        output,
        difficulty: normalizeToken(row.difficulty, "easy"),
        visibility: index < (Number($("publicCount").value) || 0) ? "public" : "private"
      };

      if (explanation) testCase.explanation = explanation;
      if (timeLimit !== null) testCase.timeLimit = timeLimit;
      if (memoryLimit !== null) testCase.memoryLimit = memoryLimit;

      return testCase;
    })
    .filter(Boolean);
}

function buildLanguageMap(row, prefix, supportedLanguages, includeDefaults) {
  const map = {};
  const prefixLower = `${prefix.toLowerCase()}_`;
  const columnByLanguage = {};

  Object.keys(row).forEach((key) => {
    const lower = key.toLowerCase();
    if (!lower.startsWith(prefixLower)) return;
    const suffix = key.slice(prefix.length + 1);
    const language = normalizeLanguage(suffix);
    if (language) columnByLanguage[language] = key;
  });

  supportedLanguages.forEach((language) => {
    const key = columnByLanguage[language];
    if (key) {
      map[language] = clean(row[key]);
    } else if (includeDefaults) {
      map[language] = DEFAULT_PRELOADS[language] || "";
    }
  });

  if (!includeDefaults) {
    Object.keys(map).forEach((language) => {
      if (!map[language]) delete map[language];
    });
  }

  return map;
}

function inferLanguageFromColumns(row) {
  for (const key of Object.keys(row)) {
    const match = key.match(/^(solution|preloadCode)_(.+)$/i);
    if (match && clean(row[key])) {
      return normalizeLanguage(match[2]);
    }
  }
  return "";
}

function normalizeLanguage(value) {
  const key = clean(value).toLowerCase().replace(/\s+/g, "");
  return LANGUAGE_ALIASES[key] || "";
}

function normalizeCodingType(value) {
  const token = clean(value).toLowerCase();
  if (token.includes("web")) return "web";
  if (token.includes("database") || token === "db" || token.includes("sql")) return "db";
  return "programming";
}

function normalizeStatus(value) {
  const token = clean(value).toLowerCase();
  if (token === "published" || token === "publish") return "published";
  return "draft";
}

function normalizeToken(value, fallback) {
  return clean(value).toLowerCase().replace(/\s+/g, "") || fallback;
}

function splitList(value) {
  return clean(value)
    .split(",")
    .map((item) => item.trim())
    .filter(Boolean);
}

function splitHints(value) {
  const text = clean(value);
  if (!text) return [];
  return text
    .split(/\n|\|\|/g)
    .map((hint) => hint.trim())
    .filter(Boolean);
}

function toBool(value, fallback) {
  if (typeof value === "boolean") return value;
  const token = clean(value).toLowerCase();
  if (!token) return fallback;
  if (["true", "yes", "y", "1", "enabled"].includes(token)) return true;
  if (["false", "no", "n", "0", "disabled"].includes(token)) return false;
  return fallback;
}

function toNumber(value, fallback) {
  const number = Number(clean(value));
  return Number.isFinite(number) ? number : fallback;
}

function toOptionalNumber(value) {
  const text = clean(value);
  if (!text) return null;
  const number = Number(text);
  return Number.isFinite(number) ? number : null;
}

function clean(value) {
  if (value === null || value === undefined) return "";
  return String(value).replace(/\r\n/g, "\n").trim();
}

function makeLocalId(rowNumber, testNumber) {
  return `cq-${rowNumber}-${testNumber}-${Math.random().toString(36).slice(2, 9)}`;
}

async function validateWithByteXL() {
  if (!state.questions.length) return;
  const token = requireToken();
  if (!token) return;

  const localErrors = state.questions.reduce((sum, question) => sum + question.errors.length, 0);
  if (localErrors > 0) {
    showMessage("Fix local errors before ByteXL validation.", "error");
    return;
  }

  try {
    setBusy(true, "Validating");
    const payload = state.questions.map((question) => question.payload);
    const result = await bytexlRequest("/api/questions/batch-validate", "POST", payload, token);

    if (!Array.isArray(result)) {
      throw new Error("Unexpected validation response from ByteXL.");
    }

    state.questions.forEach((question, index) => {
      const item = result[index] || {};
      question.bytexlErrors = Array.isArray(item.errors) ? item.errors.map(formatIssue) : [];
    });
    state.validated = true;
    state.uploaded = false;

    const errorCount = countErrors();
    if (errorCount > 0) {
      showMessage(`${errorCount} ByteXL validation issue(s) found.`, "error");
      log(`ByteXL validation completed with ${errorCount} issue(s).`);
    } else {
      showMessage("ByteXL validation passed.", "success");
      log(`ByteXL validation passed for ${state.questions.length} question(s).`);
    }
  } catch (error) {
    showMessage(error.message || "Validation failed.", "error");
    log(`ERROR: ${error.message || error}`);
  } finally {
    setBusy(false);
    render();
  }
}

async function uploadToByteXL() {
  if (!state.questions.length) return;
  const token = requireToken();
  if (!token) return;
  if (!state.validated || countErrors() > 0) {
    showMessage("Validate successfully before uploading.", "error");
    return;
  }

  try {
    setBusy(true, "Uploading");
    const payload = state.questions.map((question) => question.payload);
    const result = await bytexlRequest("/api/questions/batch", "POST", payload, token);
    state.lastUploadResult = result;

    if (!Array.isArray(result)) {
      throw new Error("Unexpected upload response from ByteXL.");
    }

    let uploaded = 0;
    state.questions.forEach((question, index) => {
      const item = result[index] || {};
      question.uploadedId = item._id || "";
      if (question.uploadedId) uploaded += 1;
      if (!question.uploadedId && item.message) {
        question.bytexlErrors = [String(item.message)];
      }
    });

    state.uploaded = uploaded === state.questions.length;
    if (state.uploaded) {
      showMessage(`Uploaded ${uploaded} coding question(s).`, "success");
      log(`Upload completed. ${uploaded}/${state.questions.length} question(s) created.`);
    } else {
      showMessage(`Uploaded ${uploaded}/${state.questions.length}. Check rows with errors.`, "error");
      log(`Partial upload. ${uploaded}/${state.questions.length} question(s) created.`);
    }
  } catch (error) {
    showMessage(error.message || "Upload failed.", "error");
    log(`ERROR: ${error.message || error}`);
  } finally {
    setBusy(false);
    render();
  }
}

async function bytexlRequest(path, method, body, token) {
  const response = await fetch("/api/bytexl", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-ByteXL-Token": token
    },
    body: JSON.stringify({ path, method, body })
  });

  const text = await response.text();
  let data = text;
  try {
    data = text ? JSON.parse(text) : null;
  } catch {
    data = text;
  }

  if (!response.ok) {
    const message = typeof data === "string" ? data : data?.message || data?.error || "ByteXL request failed";
    throw new Error(message);
  }

  return data;
}

function requireToken() {
  const token = $("tokenInput").value.trim();
  if (!token) {
    showMessage("Paste a ByteXL token first.", "error");
    $("tokenInput").focus();
    return "";
  }
  return token;
}

function downloadJson() {
  const payload = {
    sourceFile: state.fileName,
    generatedAt: new Date().toISOString(),
    questions: state.questions.map((question) => question.payload),
    localIssues: state.questions.map((question) => ({
      row: question.rowNumber,
      title: question.payload.title,
      errors: question.errors,
      warnings: question.warnings,
      bytexlErrors: question.bytexlErrors
    }))
  };
  const blob = new Blob([JSON.stringify(payload, null, 2)], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement("a");
  anchor.href = url;
  anchor.download = `${state.fileName || "coding-questions"}.json`;
  anchor.click();
  URL.revokeObjectURL(url);
}

function clearAll() {
  state.fileName = "";
  state.rawRows = [];
  state.questions = [];
  state.validated = false;
  state.uploaded = false;
  state.lastUploadResult = null;
  $("fileInput").value = "";
  $("tokenInput").value = "";
  hideMessage();
  log("Waiting for file.");
  render();
}

function render() {
  $("fileName").textContent = state.fileName || "No file selected";
  $("questionCount").textContent = state.questions.length;
  $("readyCount").textContent = countReady();
  $("warningCount").textContent = countWarnings();
  $("errorCount").textContent = countErrors();
  $("validateBtn").disabled = state.questions.length === 0;
  $("downloadBtn").disabled = state.questions.length === 0;
  $("uploadBtn").disabled = !state.validated || countErrors() > 0 || state.uploaded;

  if (state.uploaded) {
    $("validationState").textContent = "Uploaded";
  } else if (state.validated && countErrors() === 0) {
    $("validationState").textContent = "Validated";
  } else if (state.validated) {
    $("validationState").textContent = "Needs fixes";
  } else {
    $("validationState").textContent = "Not validated";
  }

  renderRows();
  renderIcons();
}

function renderRows() {
  if (!state.questions.length) {
    $("questionRows").innerHTML = `<tr><td colspan="6" class="empty">Upload a coding-question workbook to begin.</td></tr>`;
    return;
  }

  $("questionRows").innerHTML = state.questions
    .map((question) => {
      const errors = [...question.errors, ...question.bytexlErrors];
      const warnings = question.warnings;
      const badge = question.uploadedId
        ? `<span class="badge ok">Uploaded</span>`
        : errors.length
          ? `<span class="badge err">Error</span>`
          : warnings.length
            ? `<span class="badge warn">Warning</span>`
            : `<span class="badge ok">Ready</span>`;
      const notes = [
        ...errors.map((item) => `<span class="error-text">${escapeHtml(item)}</span>`),
        ...warnings.map((item) => `<span class="warn-text">${escapeHtml(item)}</span>`),
        question.uploadedId ? `<span>ByteXL ID: ${escapeHtml(question.uploadedId)}</span>` : ""
      ]
        .filter(Boolean)
        .join("");

      return `
        <tr>
          <td>${question.rowNumber}</td>
          <td><strong>${escapeHtml(question.payload.title || "Untitled")}</strong><br><span>${escapeHtml(question.payload.difficulty)} / ${escapeHtml(question.payload.status)}</span></td>
          <td>${escapeHtml(question.payload.codeOptions.supportedLanguages.join(", "))}</td>
          <td>${question.payload.codeOptions.testCases.length}</td>
          <td>${badge}</td>
          <td><div class="notes">${notes || "<span>No issues</span>"}</div></td>
        </tr>
      `;
    })
    .join("");
}

function countReady() {
  return state.questions.filter((question) => {
    return !question.errors.length && !question.bytexlErrors.length;
  }).length;
}

function countWarnings() {
  return state.questions.reduce((sum, question) => sum + question.warnings.length, 0);
}

function countErrors() {
  return state.questions.reduce((sum, question) => {
    return sum + question.errors.length + question.bytexlErrors.length;
  }, 0);
}

function formatIssue(issue) {
  if (typeof issue === "string") return issue;
  if (issue?.code === "Duplicate" && issue?.data?.title) {
    return `Duplicate question: ${issue.data.title}${issue.data._id ? ` (${issue.data._id})` : ""}`;
  }
  if (issue?.message) return issue.message;
  if (issue?.field && issue?.error) return `${issue.field}: ${issue.error}`;
  return JSON.stringify(issue);
}

function showMessage(text, type = "") {
  $("message").hidden = false;
  $("message").className = `message ${type}`.trim();
  $("message").textContent = text;
}

function hideMessage() {
  $("message").hidden = true;
  $("message").textContent = "";
}

function log(text) {
  $("logOutput").textContent = text;
}

function setBusy(isBusy, label = "Working") {
  $("statusPill").textContent = isBusy ? label : "Ready";
  document.body.style.cursor = isBusy ? "progress" : "";
  ["validateBtn", "uploadBtn", "downloadBtn", "clearBtn"].forEach((id) => {
    $(id).disabled = isBusy || (
      id === "validateBtn" && state.questions.length === 0
    ) || (
      id === "uploadBtn" && (!state.validated || countErrors() > 0 || state.uploaded)
    ) || (
      id === "downloadBtn" && state.questions.length === 0
    );
  });
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

document.addEventListener("DOMContentLoaded", init);
