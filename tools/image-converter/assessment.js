const MCQ_HEADERS = [
  "title",
  "description",
  "explanation",
  "score",
  "status",
  "difficulty",
  "bloomTaxonomy",
  "tags",
  "subjects",
  "topics",
  "subTopics",
  "companies",
  "option1",
  "option2",
  "option3",
  "option4",
  "answer"
];

const CODING_HEADERS = [
  "title",
  "description",
  "explanation",
  "score",
  "status",
  "difficulty",
  "bloomTaxonomy",
  "tags",
  "subjects",
  "topics",
  "subTopics",
  "companies",
  "codingType",
  "language",
  "supportAllLanguages",
  "enablePartialScore",
  "ignoreCase",
  "testcase1_input",
  "testcase1_output",
  "testcase2_input",
  "testcase2_output",
  "testcase3_input",
  "testcase3_output",
  "preloadCode_python",
  "solution_python",
  "hints"
];

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

const SAMPLE_ROWS = {
  mcq: {
    title: "Definition of programming",
    description: "Which statement best describes what programming means?",
    explanation: "Programming is writing precise instructions that a computer can execute.",
    score: 5,
    status: "published",
    difficulty: "easy",
    bloomTaxonomy: "remember",
    tags: "python - sample",
    subjects: "content-testing",
    topics: "python-programming",
    subTopics: "sample-subtopic",
    companies: "TCS,Infosys",
    option1: "Using applications such as a browser",
    option2: "Giving a computer ordered instructions to perform a task",
    option3: "Repairing hardware",
    option4: "Designing a circuit board",
    answer: 2
  },
  coding: {
    title: "Canteen Token Greeting",
    description: "Write a program that reads a student's name and prints a greeting.\n\n### Input Format\n- Line 1: Name\n\n### Output Format\n```\nHello <Name> your token number will be called shortly\n```",
    explanation: "",
    score: 5,
    status: "published",
    difficulty: "easy",
    bloomTaxonomy: "apply",
    tags: "python - sample",
    subjects: "content-testing",
    topics: "python-programming",
    subTopics: "sample-subtopic",
    companies: "",
    codingType: "Programming",
    language: "Python",
    supportAllLanguages: false,
    enablePartialScore: true,
    ignoreCase: true,
    testcase1_input: "Asha",
    testcase1_output: "Hello Asha your token number will be called shortly",
    testcase2_input: "Kabir",
    testcase2_output: "Hello Kabir your token number will be called shortly",
    testcase3_input: "Meera",
    testcase3_output: "Hello Meera your token number will be called shortly",
    preloadCode_python: "",
    solution_python: "name = input()\n\nprint(\"Hello\", name, \"your token number will be called shortly\")",
    hints: ""
  }
};

const REQUIRED_COLUMNS = {
  mcq: ["title", "description", "score", "status", "difficulty", "subjects", "topics", "subTopics", "option1", "option2", "option3", "option4", "answer"],
  coding: ["title", "description", "score", "status", "difficulty", "subjects", "topics", "subTopics", "codingType", "language"]
};

const state = {
  type: "mcq",
  fileName: "",
  rawRows: [],
  questions: [],
  validating: false,
  uploading: false,
  uploaded: 0,
  failed: 0
};

const $ = (id) => document.getElementById(id);

function init() {
  document.querySelectorAll(".segment-btn").forEach((button) => {
    button.addEventListener("click", () => setType(button.dataset.type));
  });

  $("downloadSampleBtn").addEventListener("click", downloadSample);
  $("pickFileBtn").addEventListener("click", () => $("fileInput").click());
  $("dropZone").addEventListener("click", () => $("fileInput").click());
  $("dropZone").addEventListener("keydown", (event) => {
    if (event.key === "Enter" || event.key === " ") {
      event.preventDefault();
      $("fileInput").click();
    }
  });
  $("fileInput").addEventListener("change", (event) => loadFile(event.target.files[0]));
  $("uploadToByteXLBtn").addEventListener("click", uploadToByteXL);
  $("resetBtn").addEventListener("click", resetAll);

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
    loadFile(event.dataTransfer.files[0]);
  });

  render();
}

function setType(type) {
  if (!["mcq", "coding"].includes(type) || state.uploading) return;
  state.type = type;
  state.fileName = "";
  state.rawRows = [];
  state.questions = [];
  state.uploaded = 0;
  state.failed = 0;
  $("fileInput").value = "";
  hideMessage();
  hideProgress();
  log(`Selected ${labelForType(type)} upload.`);
  render();
}

function downloadSample() {
  if (!window.XLSX) {
    showMessage("Spreadsheet library did not load. Refresh and try again.", "error");
    return;
  }
  const headers = headersForType(state.type);
  const sample = SAMPLE_ROWS[state.type];
  const rows = [headers, headers.map((header) => sample[header] ?? "")];
  const worksheet = XLSX.utils.aoa_to_sheet(rows);
  const workbook = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(workbook, worksheet, labelForType(state.type));
  XLSX.writeFile(workbook, `bytexl-${state.type}-sample.xlsx`);
}

async function loadFile(file) {
  if (!file) return;
  if (!/\.(xlsx|xls|csv)$/i.test(file.name)) {
    showMessage("Please upload an XLSX, XLS, or CSV file.", "error");
    return;
  }
  if (!window.XLSX) {
    showMessage("Spreadsheet library did not load. Refresh and try again.", "error");
    return;
  }

  try {
    setBusy(true, "Reading");
    state.fileName = file.name;
    state.uploaded = 0;
    state.failed = 0;
    hideProgress();

    const buffer = await file.arrayBuffer();
    const workbook = XLSX.read(buffer, { type: "array", cellDates: false });
    const sheet = workbook.Sheets[workbook.SheetNames[0]];
    state.rawRows = XLSX.utils.sheet_to_json(sheet, { defval: "", raw: false });
    rebuildQuestions();
    showMessage(`Preview loaded for ${state.questions.length} ${labelForType(state.type).toLowerCase()} question(s).`, "success");
    log(`Loaded ${state.rawRows.length} row(s) from ${file.name}.`);
  } catch (error) {
    showMessage(error.message || "Could not read file.", "error");
    log(`ERROR: ${error.message || error}`);
  } finally {
    setBusy(false);
    render();
  }
}

function rebuildQuestions() {
  const headers = Object.keys(state.rawRows[0] || {});
  const missingColumns = REQUIRED_COLUMNS[state.type].filter((column) => !headers.includes(column));
  const seenTitles = new Map();

  state.questions = state.rawRows
    .filter((row) => Object.values(row).some((value) => clean(value) !== ""))
    .map((row, index) => {
      const question = state.type === "mcq" ? buildMcqQuestion(row, index + 2) : buildCodingQuestion(row, index + 2);
      question.errors.push(...missingColumns.map((column) => `Missing column: ${column}`));

      const titleKey = question.payload.title.toLowerCase();
      if (titleKey) {
        if (seenTitles.has(titleKey)) {
          question.warnings.push(`Duplicate title also appears on row ${seenTitles.get(titleKey)}.`);
        } else {
          seenTitles.set(titleKey, index + 2);
        }
      }
      return question;
    });
}

function buildBaseQuestion(row, rowNumber, type) {
  const errors = [];
  const warnings = [];

  if (!clean(row.title)) errors.push("Title is required.");
  if (!clean(row.description)) errors.push("Description is required.");
  if (toNumber(row.score, 0) <= 0) errors.push("Score must be greater than 0.");
  if (!clean(row.status)) errors.push("Status is required.");
  if (!clean(row.difficulty)) errors.push("Difficulty is required.");
  if (!clean(row.bloomTaxonomy)) warnings.push("Bloom taxonomy is blank; using apply.");
  if (!splitList(row.subjects).length) errors.push("At least one subject is required.");
  if (!splitList(row.topics).length) errors.push("At least one topic is required.");
  if (!splitList(row.subTopics).length) errors.push("At least one subTopic is required.");

  const payload = {
    title: clean(row.title),
    description: clean(row.description),
    explanation: clean(row.explanation),
    score: toNumber(row.score, 5),
    type,
    difficulty: normalizeToken(row.difficulty, "easy"),
    bloomTaxonomy: normalizeToken(row.bloomTaxonomy, "apply"),
    tags: splitList(row.tags),
    subjects: splitList(row.subjects),
    topics: splitList(row.topics),
    subTopics: splitList(row.subTopics),
    companies: splitList(row.companies),
    status: normalizeStatus(row.status),
    submit: null,
    partialScore: false,
    codeOptions: {
      supportedLanguages: [],
      testCases: [],
      preloads: {},
      codeSolutions: {},
      hints: [],
      ignoreCase: true,
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

  return { rowNumber, source: row, payload, errors, warnings, bytexlErrors: [], uploadedId: "" };
}

function buildMcqQuestion(row, rowNumber) {
  const question = buildBaseQuestion(row, rowNumber, "multipleChoice");
  question.payload.subType = "single";

  const options = [row.option1, row.option2, row.option3, row.option4].map(clean);
  const answer = parseAnswer(row.answer, options);
  if (options.some((option) => !option)) question.errors.push("All four options are required.");
  if (answer === null) question.errors.push("Answer must be 1, 2, 3, 4, or the exact correct option text.");

  question.payload.multipleChoiceOptions = {
    selectionType: "single",
    options,
    answer: answer === null ? [] : [answer]
  };
  return question;
}

function buildCodingQuestion(row, rowNumber) {
  const question = buildBaseQuestion(row, rowNumber, "coding");
  const codingType = normalizeCodingType(row.codingType);
  const language = normalizeLanguage(row.language) || inferLanguageFromColumns(row) || "python";
  const allSupported = toBool(row.supportAllLanguages, false);
  const supportedLanguages = allSupported ? SUBTYPE_LANGUAGES[codingType] : [language];
  const testCases = extractTestCases(row, rowNumber);
  const preloads = buildLanguageMap(row, "preloadCode", supportedLanguages, true);
  const codeSolutions = buildLanguageMap(row, "solution", supportedLanguages, false);

  if (!SUBTYPE_LANGUAGES[codingType].includes(language) && !allSupported) {
    question.errors.push(`Language ${language} is not valid for ${codingType}.`);
  }
  if (!testCases.length) question.errors.push("At least one testcase is required.");
  if (testCases.some((testCase) => clean(testCase.output) === "")) {
    question.errors.push("Every testcase must have an output.");
  }
  if (!Object.values(codeSolutions).some((value) => clean(value) !== "")) {
    question.warnings.push("No solution code found.");
  }
  if (allSupported && Object.keys(codeSolutions).length < supportedLanguages.length) {
    question.warnings.push("supportAllLanguages is true, but not every language has a solution column.");
  }

  question.payload.subType = codingType;
  question.payload.partialScore = toBool(row.enablePartialScore, true);
  question.payload.codeOptions = {
    supportedLanguages,
    testCases,
    preloads,
    codeSolutions,
    hints: splitHints(row.hints),
    ignoreCase: toBool(row.ignoreCase, true),
    privileged: false,
    setupFiles: []
  };
  return question;
}

function parseAnswer(value, options) {
  const text = clean(value);
  if (!text) return null;
  const number = Number(text);
  if (Number.isInteger(number) && number >= 1 && number <= options.length) {
    return number - 1;
  }
  const match = options.findIndex((option) => option.toLowerCase() === text.toLowerCase());
  return match >= 0 ? match : null;
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

      if (!input && !output && !explanation && !timeLimit && !memoryLimit) return null;

      const testCase = {
        id: `assessment-${rowNumber}-${number}`,
        input,
        output,
        difficulty: normalizeToken(row.difficulty, "easy"),
        visibility: index === 0 ? "public" : "private"
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
    if (match && clean(row[key])) return normalizeLanguage(match[2]);
  }
  return "";
}

async function uploadToByteXL() {
  if (!state.questions.length || state.uploading) return;
  if (countLocalErrors() > 0) {
    showMessage("Fix sheet errors before uploading.", "error");
    return;
  }

  try {
    setBusy(true, "Validating");
    showMessage("Validating with ByteXL before upload...", "");
    const validation = await postJson("/assessment/validate", {
      type: state.type,
      questions: state.questions.map((question) => question.payload)
    });
    applyValidation(validation.result);
    render();

    if (countErrors() > 0) {
      showMessage("ByteXL found issues. Fix the highlighted rows before uploading.", "error");
      log(`Validation failed with ${countErrors()} issue(s).`);
      return;
    }

    state.uploading = true;
    state.uploaded = 0;
    state.failed = 0;
    showProgress(0, state.questions.length);
    showMessage("Uploading questions to ByteXL...", "");
    log(`Uploading ${state.questions.length} question(s)...`);

    for (let index = 0; index < state.questions.length; index += 1) {
      const question = state.questions[index];
      setBusy(true, `Uploading ${index + 1}/${state.questions.length}`);
      const payload = await postJson("/assessment/upload-one", { type: state.type, question: question.payload });
      const item = Array.isArray(payload.result) ? payload.result[0] || {} : {};
      question.uploadedId = item._id || "";
      if (question.uploadedId) {
        state.uploaded += 1;
      } else {
        state.failed += 1;
        if (item.message) question.bytexlErrors = [String(item.message)];
      }
      showProgress(state.uploaded, state.questions.length - state.uploaded);
      renderRows();
    }

    if (state.failed > 0) {
      showMessage(`Uploaded ${state.uploaded}/${state.questions.length}. Check failed rows.`, "error");
      log(`Partial upload: ${state.uploaded} added, ${state.questions.length - state.uploaded} left.`);
    } else {
      showMessage(`Uploaded ${state.uploaded} question(s) successfully.`, "success");
      log(`Upload complete: ${state.uploaded} added, 0 left.`);
    }
  } catch (error) {
    showMessage(error.message || "Upload failed.", "error");
    log(`ERROR: ${error.message || error}`);
  } finally {
    state.uploading = false;
    setBusy(false);
    render();
  }
}

function applyValidation(result) {
  if (!Array.isArray(result)) throw new Error("Unexpected validation response from ByteXL.");
  state.questions.forEach((question, index) => {
    const item = result[index] || {};
    question.bytexlErrors = Array.isArray(item.errors) ? item.errors.map(formatIssue) : [];
  });
}

async function postJson(url, body) {
  const response = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body)
  });
  const text = await response.text();
  let data = text;
  try {
    data = text ? JSON.parse(text) : null;
  } catch {
    data = text;
  }
  if (!response.ok) {
    const message = typeof data === "string" ? data : data?.detail || data?.message || "Request failed";
    throw new Error(message);
  }
  return data;
}

function resetAll() {
  state.fileName = "";
  state.rawRows = [];
  state.questions = [];
  state.uploaded = 0;
  state.failed = 0;
  $("fileInput").value = "";
  hideMessage();
  hideProgress();
  log("Waiting for assessment sheet.");
  render();
}

function render() {
  document.querySelectorAll(".segment-btn").forEach((button) => {
    button.classList.toggle("active", button.dataset.type === state.type);
  });
  $("fileName").textContent = state.fileName || "No file selected";
  $("questionCount").textContent = state.questions.length;
  $("readyCount").textContent = countReady();
  $("warningCount").textContent = countWarnings();
  $("errorCount").textContent = countErrors();
  $("uploadToByteXLBtn").disabled = state.questions.length === 0 || countErrors() > 0 || state.uploading;
  $("previewState").textContent = state.questions.length ? (countErrors() ? "Needs fixes" : "Ready") : "Waiting";
  renderRows();
}

function renderRows() {
  if (!state.questions.length) {
    $("questionRows").innerHTML = `<tr><td class="empty" colspan="7">Choose a type and upload an XLSX sheet to preview questions.</td></tr>`;
    return;
  }

  $("questionRows").innerHTML = state.questions.map((question) => {
    const errors = [...question.errors, ...question.bytexlErrors];
    const status = question.uploadedId
      ? `<span class="badge ok">Uploaded</span>`
      : errors.length
        ? `<span class="badge err">Error</span>`
        : question.warnings.length
          ? `<span class="badge warn">Warning</span>`
          : `<span class="badge ok">Ready</span>`;
    const notes = [...errors.map((item) => ["error-text", item]), ...question.warnings.map((item) => ["warn-text", item])];
    return `
      <tr>
        <td>${question.rowNumber}</td>
        <td>${escapeHtml(labelForType(state.type))}</td>
        <td>${escapeHtml(question.payload.title || "(Untitled)")}</td>
        <td>${escapeHtml(question.payload.difficulty || "-")}</td>
        <td>${escapeHtml(question.payload.score)}</td>
        <td>${status}</td>
        <td><div class="notes">${notes.length ? notes.map(([className, text]) => `<span class="${className}">${escapeHtml(text)}</span>`).join("") : "<span>No issues</span>"}</div></td>
      </tr>`;
  }).join("");
}

function countReady() {
  return state.questions.filter((question) => !question.errors.length && !question.bytexlErrors.length).length;
}

function countWarnings() {
  return state.questions.reduce((sum, question) => sum + question.warnings.length, 0);
}

function countLocalErrors() {
  return state.questions.reduce((sum, question) => sum + question.errors.length, 0);
}

function countErrors() {
  return state.questions.reduce((sum, question) => sum + question.errors.length + question.bytexlErrors.length, 0);
}

function headersForType(type) {
  return type === "mcq" ? MCQ_HEADERS : CODING_HEADERS;
}

function labelForType(type) {
  return type === "mcq" ? "MCQ" : "Coding";
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
  return clean(value).split(",").map((item) => item.trim()).filter(Boolean);
}

function splitHints(value) {
  const text = clean(value);
  if (!text) return [];
  return text.split(/\n|\|\|/g).map((hint) => hint.trim()).filter(Boolean);
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

function formatIssue(issue) {
  if (typeof issue === "string") return issue;
  if (issue?.message) return issue.message;
  if (issue?.field) return `${issue.field}: ${issue.reason || "invalid"}`;
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

function showProgress(added, left) {
  const total = added + left;
  const percent = total ? Math.round((added / total) * 100) : 0;
  $("progressPanel").classList.add("show");
  $("progressFill").style.width = `${percent}%`;
  $("progressText").textContent = `${added} added, ${left} left`;
}

function hideProgress() {
  $("progressPanel").classList.remove("show");
  $("progressFill").style.width = "0%";
  $("progressText").textContent = "0 added, 0 left";
}

function setBusy(isBusy, label = "Working") {
  $("statusPill").textContent = isBusy ? label : "Ready";
  ["downloadSampleBtn", "pickFileBtn", "uploadToByteXLBtn", "resetBtn"].forEach((id) => {
    const button = $(id);
    if (id === "uploadToByteXLBtn") {
      button.disabled = isBusy || state.questions.length === 0 || countErrors() > 0;
    } else {
      button.disabled = isBusy;
    }
  });
  document.querySelectorAll(".segment-btn").forEach((button) => {
    button.disabled = isBusy;
  });
}

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

document.addEventListener("DOMContentLoaded", init);
