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

const UPDATE_ID_HEADER = "questionId";

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
  "testcase4_input",
  "testcase4_output",
  "testcase5_input",
  "testcase5_output",
  "testcase6_input",
  "testcase6_output",
  "testcase7_input",
  "testcase7_output",
  "preloadCode_python",
  "setupFile1_filename",
  "setupFile1_content",
  "solution_python",
  "hints"
];

// Show the first two coding test cases and keep the remaining fixtures hidden.
const PUBLIC_CODING_TEST_CASE_COUNT = 2;

function externalApiBase() {
  const configured = location.protocol === "file:"
    ? "http://127.0.0.1:8000"
    : String(window.IMAGE_CONVERTER_CONFIG?.apiBase || "").trim();
  if (!configured) throw new Error("The update API is not configured.");

  const api = new URL(configured, location.href);
  const isVercel = api.hostname === "vercel.app" || api.hostname.endsWith(".vercel.app");
  if (api.origin === location.origin || isVercel) {
    throw new Error("Assessment updates cannot use Vercel. Configure an external API host.");
  }
  return api.origin;
}

const API_BASE = externalApiBase();

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
    testcase4_input: "Ravi",
    testcase4_output: "Hello Ravi your token number will be called shortly",
    testcase5_input: "Nila",
    testcase5_output: "Hello Nila your token number will be called shortly",
    testcase6_input: "Dev",
    testcase6_output: "Hello Dev your token number will be called shortly",
    testcase7_input: "Ira",
    testcase7_output: "Hello Ira your token number will be called shortly",
    preloadCode_python: "",
    setupFile1_filename: "students.csv",
    setupFile1_content: "name,score\nAsha,88\nKabir,92",
    solution_python: "name = input()\n\nprint(\"Hello\", name, \"your token number will be called shortly\")",
    hints: ""
  }
};

const REQUIRED_COLUMNS = {
  mcq: ["title", "description", "score", "status", "difficulty", "subjects", "topics", "subTopics", "option1", "option2", "option3", "option4", "answer"],
  coding: ["title", "description", "score", "status", "difficulty", "subjects", "topics", "subTopics", "codingType", "language"]
};

const state = {
  mode: "create",
  type: "mcq",
  fileName: "",
  rawRows: [],
  questions: [],
  validating: false,
  uploading: false,
  uploaded: 0,
  created: 0,
  updated: 0,
  failed: 0,
  unchanged: 0,
  preflightComplete: false
};

const $ = (id) => document.getElementById(id);

function init() {
  document.querySelectorAll(".type-btn").forEach((button) => {
    button.addEventListener("click", () => setType(button.dataset.type));
  });
  document.querySelectorAll(".mode-btn").forEach((button) => {
    button.addEventListener("click", () => setMode(button.dataset.mode));
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
  $("uploadToByteXLBtn").addEventListener("click", handlePrimaryAction);
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
  state.created = 0;
  state.updated = 0;
  state.failed = 0;
  state.unchanged = 0;
  state.preflightComplete = false;
  $("fileInput").value = "";
  hideMessage();
  hideProgress();
  log(`Selected ${labelForType(type)} ${state.mode === "update" ? "update" : "upload"}.`);
  render();
}

function setMode(mode) {
  if (!["create", "update"].includes(mode) || state.uploading) return;
  state.mode = mode;
  state.fileName = "";
  state.rawRows = [];
  state.questions = [];
  state.uploaded = 0;
  state.created = 0;
  state.updated = 0;
  state.failed = 0;
  state.unchanged = 0;
  state.preflightComplete = false;
  $("fileInput").value = "";
  hideMessage();
  hideProgress();
  log(mode === "update"
    ? "Update mode selected. Every row must include an existing ByteXL questionId. This mode cannot create questions."
    : "Create mode selected. New questions are added and exact duplicates may be updated.");
  render();
}

function downloadSample() {
  if (!window.XLSX) {
    showMessage("Spreadsheet library did not load. Refresh and try again.", "error");
    return;
  }
  const headers = headersForType(state.type);
  const sample = SAMPLE_ROWS[state.type];
  const rows = [headers, headers.map((header) => header === UPDATE_ID_HEADER ? "existing-question-id" : sample[header] ?? "")];
  const worksheet = XLSX.utils.aoa_to_sheet(rows);
  const workbook = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(workbook, worksheet, labelForType(state.type));
  XLSX.writeFile(workbook, `bytexl-${state.type}-${state.mode === "update" ? "update" : "create"}-sample.xlsx`);
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
    state.created = 0;
    state.updated = 0;
    state.failed = 0;
    state.unchanged = 0;
    state.preflightComplete = false;
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
  const requiredColumns = state.mode === "update"
    ? [UPDATE_ID_HEADER, ...REQUIRED_COLUMNS[state.type]]
    : REQUIRED_COLUMNS[state.type];
  const missingColumns = requiredColumns.filter((column) => !headers.includes(column));
  const seenTitles = new Map();
  const seenIds = new Map();

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
      if (state.mode === "update" && question.questionId) {
        if (seenIds.has(question.questionId)) {
          question.errors.push(`Duplicate questionId also appears on row ${seenIds.get(question.questionId)}.`);
        } else {
          seenIds.set(question.questionId, index + 2);
        }
      }
      return question;
    });
}

function buildBaseQuestion(row, rowNumber, type) {
  const errors = [];
  const warnings = [];
  const questionId = clean(row.questionId);

  if (state.mode === "update" && !questionId) errors.push("questionId is required in update mode.");
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
      setupFiles: {}
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
    questionId,
    payload,
    errors,
    warnings,
    bytexlErrors: [],
    uploadedId: "",
    changedFields: [],
    expectedRevision: "",
    resultAction: ""
  };
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
  const setupFiles = extractSetupFiles(row, question.errors);

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
    setupFiles
  };
  return question;
}

function parseAnswer(value, options) {
  const text = clean(value);
  if (!text) return null;
  const number = Number(text);
  if (Number.isInteger(number) && number >= 1 && number <= options.length) {
    return number;
  }
  const match = options.findIndex((option) => option.toLowerCase() === text.toLowerCase());
  return match >= 0 ? match + 1 : null;
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
      const input = cleanTestCaseText(row[`testcase${number}_input`], { trim: true });
      const output = cleanTestCaseText(row[`testcase${number}_output`], { trim: false });
      const explanation = clean(row[`testcase${number}_explanation`]);
      const timeLimit = toOptionalNumber(row[`testcase${number}_timeLimit`]);
      const memoryLimit = toOptionalNumber(row[`testcase${number}_memoryLimit`]);

      if (!input && !output && !explanation && !timeLimit && !memoryLimit) return null;

      const testCase = {
        id: `assessment-${rowNumber}-${number}`,
        input,
        output,
        difficulty: normalizeToken(row.difficulty, "easy"),
        visibility: index < PUBLIC_CODING_TEST_CASE_COUNT ? "public" : "private"
      };
      if (explanation) testCase.explanation = explanation;
      if (timeLimit !== null) testCase.timeLimit = timeLimit;
      if (memoryLimit !== null) testCase.memoryLimit = memoryLimit;
      return testCase;
    })
    .filter(Boolean);
}

function extractSetupFiles(row, errors) {
  const setupFiles = {};
  const slots = new Map();

  Object.keys(row).forEach((key) => {
    const match = key.match(/^setupFile(\d*)_(filename|content)$/i);
    if (!match) return;
    const number = Number(match[1] || 1);
    const slot = slots.get(number) || {};
    slot[match[2].toLowerCase()] = key;
    slots.set(number, slot);
  });

  [...slots.entries()]
    .sort(([a], [b]) => a - b)
    .forEach(([number, slot]) => {
      const filename = clean(slot.filename ? row[slot.filename] : "");
      const content = normalizeFileContent(slot.content ? row[slot.content] : "");
      if (!filename) {
        if (content.trim()) errors.push(`Setup file ${number} has content but no filename.`);
        return;
      }
      if (Object.prototype.hasOwnProperty.call(setupFiles, filename)) {
        errors.push(`Duplicate setup filename: ${filename}`);
        return;
      }
      setupFiles[filename] = content;
    });

  const jsonKey = Object.keys(row).find((key) => key.toLowerCase() === "setupfiles");
  const jsonText = jsonKey ? clean(row[jsonKey]) : "";
  if (jsonText) {
    try {
      const parsed = JSON.parse(jsonText);
      if (!parsed || Array.isArray(parsed) || typeof parsed !== "object") {
        errors.push("setupFiles must be a JSON object mapping filenames to file content.");
      } else {
        Object.entries(parsed).forEach(([filenameValue, contentValue]) => {
          const filename = clean(filenameValue);
          if (!filename) return;
          if (Object.prototype.hasOwnProperty.call(setupFiles, filename)) {
            errors.push(`Duplicate setup filename: ${filename}`);
            return;
          }
          setupFiles[filename] = normalizeFileContent(contentValue);
        });
      }
    } catch {
      errors.push("setupFiles contains invalid JSON.");
    }
  }

  return setupFiles;
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

function handlePrimaryAction() {
  if (state.mode === "create") return uploadToByteXL();
  if (state.preflightComplete) return applyExistingUpdates();
  return validateExistingUpdates();
}

function questionForUpdate(question, includeRevision = false) {
  return {
    ...question.payload,
    questionId: question.questionId,
    ...(includeRevision ? { expectedRevision: question.expectedRevision } : {})
  };
}

// Each question update performs a ByteXL read and write. Isolating updates
// prevents one slow question from timing out a complete serverless batch.
const UPDATE_BATCH_SIZE = 1;

function chunksOf(items, size) {
  const chunks = [];
  for (let index = 0; index < items.length; index += size) {
    chunks.push(items.slice(index, index + size));
  }
  return chunks;
}

async function validateExistingUpdates() {
  if (!state.questions.length || state.uploading) return;
  if (countLocalErrors() > 0) {
    showMessage("Fix sheet errors before validating updates.", "error");
    return;
  }

  try {
    setBusy(true, "Validating");
    state.updated = 0;
    state.failed = 0;
    state.created = 0;
    state.unchanged = 0;
    hideProgress();
    state.questions.forEach((question) => {
      question.bytexlErrors = [];
      question.changedFields = [];
      question.expectedRevision = "";
      question.resultAction = "";
      question.uploadedId = "";
    });
    state.preflightComplete = false;
    showMessage("Validating question data and resolving existing ByteXL IDs...", "");

    const schemaValidation = await postJson("/assessment/validate", {
      type: state.type,
      questions: state.questions.map((question) => question.payload)
    });
    applyValidation(schemaValidation.result);
    if (countErrors() > 0) {
      showMessage("ByteXL found question-data issues. Fix the highlighted rows before updating.", "error");
      log(`Update validation stopped with ${countErrors()} question-data issue(s).`);
      return;
    }

    const validation = await postJson("/assessment/update/validate", {
      type: state.type,
      questions: state.questions.map((question) => questionForUpdate(question))
    });
    applyUpdateValidation(validation.result);
    state.preflightComplete = countErrors() === 0;
    state.unchanged = state.questions.filter((question) => question.resultAction === "unchanged").length;
    const pending = countPendingUpdates();

    if (!state.preflightComplete) {
      showMessage("Some existing questions could not be validated. No questions were changed.", "error");
      log(`Update preflight failed with ${countErrors()} issue(s). Created: 0.`);
    } else {
      showMessage(
        `${pending} existing question(s) ready to update; ${state.unchanged} unchanged; 0 will be created. Review the preview, then apply updates.`,
        pending ? "success" : "warning"
      );
      log(`Preflight complete: ${pending} updates, ${state.unchanged} unchanged, 0 creates.`);
    }
  } catch (error) {
    showMessage(error.message || "Could not validate existing questions.", "error");
    log(`ERROR: ${error.message || error}`);
  } finally {
    setBusy(false);
    render();
  }
}

function applyUpdateValidation(result) {
  if (!Array.isArray(result)) throw new Error("Unexpected update validation response from ByteXL.");
  state.questions.forEach((question, index) => {
    const item = result[index] || {};
    question.bytexlErrors = Array.isArray(item.errors) ? item.errors.map(formatIssue) : [];
    question.changedFields = Array.isArray(item.changedFields) ? item.changedFields : [];
    question.expectedRevision = clean(item.expectedRevision);
    question.resultAction = clean(item.uploadAction);
  });
}

async function applyExistingUpdates() {
  if (!state.preflightComplete || countErrors() > 0 || state.uploading) return;
  const pending = countPendingUpdates();
  if (!pending) {
    showMessage("Every row is unchanged. Nothing was sent to ByteXL.", "warning");
    return;
  }
  if (!window.confirm(`Update ${pending} existing ByteXL question(s)? This operation will create 0 questions.`)) return;

  const pendingQuestions = state.questions.filter(
    (question) => !question.errors.length && !question.bytexlErrors.length && question.changedFields.length > 0
  );

  try {
    state.uploading = true;
    state.updated = 0;
    state.unchanged = state.questions.filter((question) => question.resultAction === "unchanged").length;
    state.failed = 0;
    state.created = 0;
    setBusy(true, "Updating");
    showUpdateProgress(0, pendingQuestions.length, 0);
    showMessage(`Updating 0 of ${pendingQuestions.length} changed questions by ByteXL ID...`, "");
    log(`Applying ${pending} ID-based update(s) in batches of ${UPDATE_BATCH_SIZE}. Create fallback is disabled.`);

    let processed = 0;
    for (const batch of chunksOf(pendingQuestions, UPDATE_BATCH_SIZE)) {
      try {
        const update = await postJson("/assessment/update", {
          type: state.type,
          confirm: true,
          questions: batch.map((question) => questionForUpdate(question, true))
        });
        if (!Array.isArray(update.result) || update.result.length !== batch.length) {
          throw new Error("Unexpected update response from ByteXL.");
        }

        batch.forEach((question, index) => {
          const rawItem = update.result[index] || {};
          const item = rawItem.data && typeof rawItem.data === "object" ? rawItem.data : rawItem;
          question.resultAction = clean(item.uploadAction || item.status);
          question.changedFields = Array.isArray(item.changedFields) ? item.changedFields : question.changedFields;
          if (item._id && ["updated", "unchanged"].includes(question.resultAction)) {
            question.uploadedId = item._id;
            question.bytexlErrors = [];
            if (question.resultAction === "updated") state.updated += 1;
            else state.unchanged += 1;
          } else {
            state.failed += 1;
            question.bytexlErrors = [String(item.message || "ByteXL did not update this question.")];
          }
        });
      } catch (error) {
        batch.forEach((question) => {
          state.failed += 1;
          question.resultAction = "failed";
          question.bytexlErrors = [String(error.message || error || "Update request failed.")];
        });
      }

      processed += batch.length;
      showUpdateProgress(processed, pendingQuestions.length, state.failed);
      showMessage(`Updating ${processed} of ${pendingQuestions.length} changed questions by ByteXL ID...`, "");
      log(`Update progress: ${processed}/${pendingQuestions.length} processed, ${state.updated} updated, ${state.failed} failed, 0 created.`);
    }
    state.preflightComplete = false;

    if (state.failed) {
      showMessage(`Updated ${state.updated}; unchanged ${state.unchanged}; failed ${state.failed}; created 0.`, "error");
      log(`Partial update: ${state.updated} updated, ${state.unchanged} unchanged, ${state.failed} failed, 0 created.`);
    } else {
      showMessage(`Updated ${state.updated} existing question(s); ${state.unchanged} unchanged; 0 created.`, "success");
      log(`Update complete: ${state.updated} updated, ${state.unchanged} unchanged, 0 created.`);
    }
  } catch (error) {
    showMessage(error.message || "Update failed.", "error");
    log(`ERROR: ${error.message || error}`);
  } finally {
    state.uploading = false;
    setBusy(false);
    render();
  }
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
    state.created = 0;
    state.updated = 0;
    state.failed = 0;
    showProgress(0, state.questions.length);
    showMessage(
      validation.warning || "Uploading questions to ByteXL...",
      validation.warning ? "warning" : ""
    );
    log(`${validation.warning ? `WARNING: ${validation.warning} ` : ""}Uploading ${state.questions.length} question(s)...`);

    const upload = await postJson("/assessment/upload", {
      type: state.type,
      questions: state.questions.map((question) => question.payload)
    });
    if (!Array.isArray(upload.result)) {
      throw new Error("Unexpected upload response from ByteXL.");
    }

    state.questions.forEach((question, index) => {
      const rawItem = upload.result[index] || {};
      const item = rawItem.data && typeof rawItem.data === "object" ? rawItem.data : rawItem;
      question.uploadedId = item._id || "";
      if (question.uploadedId) {
        question.bytexlErrors = [];
        state.uploaded += 1;
        if (item.uploadAction === "updated") state.updated += 1;
        else state.created += 1;
      } else {
        state.failed += 1;
        question.bytexlErrors = [String(item.message || "ByteXL did not create this question.")];
      }
    });
    showProgress(state.uploaded, state.questions.length - state.uploaded);
    renderRows();

    if (state.failed > 0) {
      showMessage(`Uploaded ${state.uploaded}/${state.questions.length}. Check failed rows.`, "error");
      log(`Partial upload: ${state.uploaded} added, ${state.questions.length - state.uploaded} left.`);
    } else {
      showMessage(
        `Processed ${state.uploaded} question(s): ${state.created} created, ${state.updated} updated.`,
        "success"
      );
      log(`Upload complete: ${state.created} created, ${state.updated} updated, 0 left.`);
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
  let response;
  try {
    response = await fetch(API_BASE + url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body)
    });
  } catch {
    const operation = url === "/assessment/update" ? "update" : "request";
    throw new Error(`The ${operation} connection closed before the server returned a result. No create fallback was used; validate again to reconcile the existing question IDs.`);
  }
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
  state.created = 0;
  state.updated = 0;
  state.failed = 0;
  state.unchanged = 0;
  state.preflightComplete = false;
  $("fileInput").value = "";
  hideMessage();
  hideProgress();
  log(state.mode === "update" ? "Waiting for an update sheet with questionId values." : "Waiting for assessment sheet.");
  render();
}

function render() {
  document.querySelectorAll(".type-btn").forEach((button) => {
    button.classList.toggle("active", button.dataset.type === state.type);
  });
  document.querySelectorAll(".mode-btn").forEach((button) => {
    button.classList.toggle("active", button.dataset.mode === state.mode);
  });
  const isUpdate = state.mode === "update";
  $("workflowTitle").textContent = isUpdate ? "Update Existing Questions" : "Create or Import Questions";
  $("workflowSub").textContent = isUpdate
    ? "Update questions by their existing ByteXL ID. This workflow cannot create questions."
    : "Use the sample format, preview every row, then add questions to ByteXL.";
  $("downloadSampleBtn").textContent = isUpdate ? "Download update template" : "Download create template";
  $("uploadToByteXLBtn").textContent = isUpdate
    ? (state.preflightComplete ? `Apply ${countPendingUpdates()} update(s)` : "Validate existing questions")
    : "Upload to ByteXL";
  $("primaryStepLabel").textContent = isUpdate ? "Validate IDs" : "Preview";
  $("finalStepLabel").textContent = isUpdate ? "Apply updates" : "Upload";
  $("previewDescription").textContent = isUpdate
    ? "Review resolved IDs and changed fields. Update mode always creates 0 questions."
    : "All questions are shown here before upload.";
  $("fileName").textContent = state.fileName || "No file selected";
  $("questionCount").textContent = state.questions.length;
  $("readyCount").textContent = countReady();
  $("warningCount").textContent = countWarnings();
  $("errorCount").textContent = countErrors();
  $("uploadToByteXLBtn").disabled = state.questions.length === 0 || countErrors() > 0 || state.uploading || (isUpdate && state.preflightComplete && countPendingUpdates() === 0);
  $("previewState").textContent = state.questions.length
    ? (countErrors() ? "Needs fixes" : isUpdate && state.preflightComplete ? "Validated" : "Ready")
    : "Waiting";
  renderRows();
}

function renderRows() {
  if (!state.questions.length) {
    $("questionRows").innerHTML = `<tr><td class="empty" colspan="9">Choose a workflow and type, then upload an XLSX sheet to preview questions.</td></tr>`;
    return;
  }

  $("questionRows").innerHTML = state.questions.map((question) => {
    const errors = [...question.errors, ...question.bytexlErrors];
    const completedLabel = question.resultAction === "updated" ? "Updated" : question.resultAction === "unchanged" ? "Unchanged" : "Uploaded";
    const status = question.uploadedId
      ? `<span class="badge ok">${completedLabel}</span>`
      : errors.length
        ? `<span class="badge err">Error</span>`
        : state.mode === "update" && state.preflightComplete
          ? `<span class="badge ok">${question.resultAction === "unchanged" ? "Unchanged" : "Ready to update"}</span>`
        : question.warnings.length
          ? `<span class="badge warn">Warning</span>`
          : `<span class="badge ok">Ready</span>`;
    const notes = [...errors.map((item) => ["error-text", item]), ...question.warnings.map((item) => ["warn-text", item])];
    return `
      <tr>
        <td>${question.rowNumber}</td>
        <td>${escapeHtml(labelForType(state.type))}</td>
        <td>${escapeHtml(question.questionId || "—")}</td>
        <td>${escapeHtml(question.payload.title || "(Untitled)")}</td>
        <td>${escapeHtml(question.payload.difficulty || "-")}</td>
        <td>${escapeHtml(question.payload.score)}</td>
        <td>${escapeHtml(question.changedFields.length ? question.changedFields.join(", ") : "—")}</td>
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

function countPendingUpdates() {
  return state.questions.filter((question) => !question.errors.length && !question.bytexlErrors.length && question.changedFields.length > 0).length;
}

function headersForType(type) {
  const headers = type === "mcq" ? MCQ_HEADERS : CODING_HEADERS;
  return state.mode === "update" ? [UPDATE_ID_HEADER, ...headers] : headers;
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

function cleanTestCaseText(value, { trim = false } = {}) {
  if (value === null || value === undefined) return "";
  const text = String(value).replace(/\r\n/g, "\n");
  return trim ? text.trim() : text;
}

function normalizeFileContent(value) {
  if (value === null || value === undefined) return "";
  return String(value).replace(/\r\n/g, "\n");
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

function showUpdateProgress(processed, total, failed) {
  const percent = total ? Math.round((processed / total) * 100) : 100;
  $("progressPanel").classList.add("show");
  $("progressFill").style.width = `${percent}%`;
  $("progressText").textContent = `${processed} of ${total} processed, ${failed} failed`;
}

function hideProgress() {
  $("progressPanel").classList.remove("show");
  $("progressFill").style.width = "0%";
  $("progressText").textContent = state.mode === "update" ? "0 processed, 0 failed" : "0 added, 0 left";
}

function setBusy(isBusy, label = "Working") {
  $("statusPill").textContent = isBusy ? label : "Ready";
  ["downloadSampleBtn", "pickFileBtn", "uploadToByteXLBtn", "resetBtn"].forEach((id) => {
    const button = $(id);
    if (id === "uploadToByteXLBtn") {
      button.disabled = isBusy || state.questions.length === 0 || countErrors() > 0 || (state.mode === "update" && state.preflightComplete && countPendingUpdates() === 0);
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
