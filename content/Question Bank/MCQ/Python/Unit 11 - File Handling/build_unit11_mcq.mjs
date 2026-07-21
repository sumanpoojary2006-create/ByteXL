import fs from "node:fs/promises";
import path from "node:path";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const ROOT = process.cwd();
const UNIT = 11;
const TITLE = "File Handling";
const TOPIC = "file-handling";
const SHEET_NAME = "Python - MCQ - 11";
const UNIT_DIR = path.join(
  ROOT,
  "content/Question Bank/MCQ/Python/Unit 11 - File Handling",
);
const DATA_FILE = path.join(UNIT_DIR, "unit11_questions.json");
const TEMPLATE_FILE = path.join(
  ROOT,
  "content/Question Bank/Template/questions-mcq-template.xlsx",
);
const CONTENT_FILE = path.join(UNIT_DIR, "Unit 11 - File Handling - MCQ.xlsx");
const DELIVERY_DIR = path.join(ROOT, "outputs/units-6-13-qc-upgrade");
const DELIVERY_FILE = path.join(DELIVERY_DIR, "Unit 11 - File Handling - MCQ.xlsx");
const PREVIEW_FILE = path.join(DELIVERY_DIR, "Unit 11 - File Handling - MCQ.png");

const HEADERS = [
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
  "answer",
];
const LETTERS = "ABCD";
const SCORE = { easy: 5, medium: 8, hard: 10 };
const REQUIRED_KEYS = [
  "set",
  "difficulty",
  "bloom",
  "subtopic",
  "description",
  "explanation",
  "options",
  "answer",
].sort();

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

function tally(values) {
  return Object.fromEntries(
    [...values.reduce((counts, value) => {
      counts.set(value, (counts.get(value) ?? 0) + 1);
      return counts;
    }, new Map()).entries()].sort(),
  );
}

function validateQuestions(questions) {
  const allowedSubtopics = new Set([
    "context-managed-files", "csv-processing", "file-errors",
    "file-operations", "file-paths", "glob-pattern-matching",
    "json-processing",
  ]);
  assert(questions.length === 40, `Expected 40 questions, got ${questions.length}`);
  for (const [index, question] of questions.entries()) {
    const number = index + 1;
    assert(
      JSON.stringify(Object.keys(question).sort()) === JSON.stringify(REQUIRED_KEYS),
      `Question ${number} has incorrect keys`,
    );
    assert(question.set === (index < 10 ? 1 : 2), `Question ${number} is in the wrong set`);
    assert(Object.hasOwn(SCORE, question.difficulty), `Question ${number} has invalid difficulty`);
    assert(["understand", "apply", "analyze"].includes(question.bloom), `Question ${number} has invalid Bloom taxonomy`);
    assert(Array.isArray(question.options) && question.options.length === 4, `Question ${number} must have four options`);
    assert(new Set(question.options).size === 4, `Question ${number} has duplicate options`);
    assert(LETTERS.includes(question.answer), `Question ${number} has invalid answer letter`);
    assert(allowedSubtopics.has(question.subtopic), `Question ${number} has invalid subtopic taxonomy`);
    assert(question.description.trim() && question.explanation.trim(), `Question ${number} has blank text`);
    assert(!question.description.startsWith("What is the output"), `Question ${number} lacks a scenario`);
    assert(!JSON.stringify(question).includes("—"), `Question ${number} contains an em dash`);
    const fenceCount = (question.description.match(/```/g) ?? []).length;
    assert(fenceCount % 2 === 0, `Question ${number} has an unmatched code fence`);
  }

  const answerCounts = tally(questions.map((question) => question.answer));
  assert(JSON.stringify(answerCounts) === JSON.stringify({ A: 10, B: 10, C: 10, D: 10 }), `Unbalanced answers: ${JSON.stringify(answerCounts)}`);
  const set1Counts = tally(questions.slice(0, 10).map((question) => question.answer));
  assert(JSON.stringify(Object.values(set1Counts).sort()) === JSON.stringify([2, 2, 3, 3]), `Set 1 answer balance failed: ${JSON.stringify(set1Counts)}`);
  assert(new Set(questions.slice(0, 10).map((question) => question.subtopic)).size === 7, "Set 1 must cover all seven Unit 11 taxonomy subtopics");
  assert(new Set(questions.map((question) => question.description)).size === 40, "Duplicate descriptions found");

  let maximumRun = 1;
  let currentRun = 1;
  for (let index = 1; index < questions.length; index += 1) {
    currentRun = questions[index].answer === questions[index - 1].answer ? currentRun + 1 : 1;
    maximumRun = Math.max(maximumRun, currentRun);
  }
  assert(maximumRun <= 2, `Answer letter repeats ${maximumRun} times consecutively`);

  let correctIsLongest = 0;
  let correctIsShortest = 0;
  for (const question of questions) {
    const lengths = question.options.map((option) => option.length);
    const correctLength = lengths[LETTERS.indexOf(question.answer)];
    if (correctLength === Math.max(...lengths)) correctIsLongest += 1;
    if (correctLength === Math.min(...lengths)) correctIsShortest += 1;
  }
  assert(correctIsLongest <= 14, `Correct option is longest too often: ${correctIsLongest}/40`);
  assert(correctIsShortest >= 8, `Correct option is rarely shortest: ${correctIsShortest}/40`);

  return { answerCounts, set1Counts, maximumRun, correctIsLongest, correctIsShortest };
}

function buildRows(questions) {
  const counters = { 1: 0, 2: 0 };
  return questions.map((question) => {
    counters[question.set] += 1;
    const answer = LETTERS.indexOf(question.answer) + 1;
    return [
      `Python - MCQ - ${UNIT}.${question.set}.${counters[question.set]}`,
      question.description,
      question.explanation,
      SCORE[question.difficulty],
      "published",
      question.difficulty,
      question.bloom,
      `python - Set ${question.set}`,
      "python",
      TOPIC,
      question.subtopic,
      null,
      ...question.options,
      answer,
    ];
  });
}

const questions = JSON.parse(await fs.readFile(DATA_FILE, "utf8"));
const quality = validateQuestions(questions);
const rows = buildRows(questions);

const workbook = await SpreadsheetFile.importXlsx(await FileBlob.load(TEMPLATE_FILE));
const sheet = workbook.worksheets.getItemAt(0);
sheet.name = SHEET_NAME;
sheet.getRange("A2:Q3").clear({ applyTo: "contents" });
sheet.getRange("A2:Q41").values = rows;

const headerValues = sheet.getRange("A1:Q1").values[0];
assert(JSON.stringify(headerValues) === JSON.stringify(HEADERS), "Template headers do not match the canonical schema");

await fs.mkdir(DELIVERY_DIR, { recursive: true });
const preview = await workbook.render({
  sheetName: SHEET_NAME,
  range: "A1:Q41",
  scale: 0.7,
  format: "png",
});
await fs.writeFile(PREVIEW_FILE, new Uint8Array(await preview.arrayBuffer()));

const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save(DELIVERY_FILE);
await fs.copyFile(DELIVERY_FILE, CONTENT_FILE);

const saved = await SpreadsheetFile.importXlsx(await FileBlob.load(CONTENT_FILE));
const savedSheet = saved.worksheets.getItemAt(0);
assert(savedSheet.name === SHEET_NAME, `Unexpected sheet name: ${savedSheet.name}`);
const savedValues = savedSheet.getRange("A1:Q41").values;
assert(savedValues.length === 41, `Saved workbook has ${savedValues.length - 1} questions`);
assert(JSON.stringify(savedValues[0]) === JSON.stringify(HEADERS), "Saved headers changed");
assert(JSON.stringify(savedValues.slice(1)) === JSON.stringify(rows), "Saved workbook rows do not match the source data");
assert(
  JSON.stringify(tally(savedValues.slice(1).map((row) => LETTERS[row[16] - 1]))) ===
    JSON.stringify({ A: 10, B: 10, C: 10, D: 10 }),
  "Saved answer distribution changed",
);

const inspection = await saved.inspect({
  kind: "workbook,sheet,table",
  include: "id,name,values,formulas",
  maxChars: 5000,
  tableMaxRows: 4,
  tableMaxCols: 17,
  tableMaxCellChars: 100,
});
const errors = await saved.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 100 },
  summary: "final formula error scan",
});

console.log(inspection.ndjson);
console.log(errors.ndjson);
console.log(JSON.stringify({
  unit: `${UNIT} - ${TITLE}`,
  questions: questions.length,
  setCounts: tally(questions.map((question) => question.set)),
  difficulty: tally(questions.map((question) => question.difficulty)),
  subtopics: tally(questions.map((question) => question.subtopic)),
  ...quality,
  contentFile: CONTENT_FILE,
  deliveryFile: DELIVERY_FILE,
  previewFile: PREVIEW_FILE,
}, null, 2));
