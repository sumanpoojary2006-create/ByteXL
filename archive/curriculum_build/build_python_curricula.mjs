import fs from "node:fs/promises";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const outputDir = "/Users/suman/Desktop/ByteXL/outputs/019edaf8-c419-7d52-abf0-2376236b860f";

const palette = {
  primary: "#17324D",
  secondary: "#1E6F68",
  accent: "#B7791F",
  softBlue: "#EAF2F8",
  softGreen: "#E8F5F1",
  softGold: "#FFF4D6",
  body: "#FFFFFF",
  grid: "#D7DEE8",
  text: "#17202A",
  muted: "#51606F",
};

const structurePalette = {
  unit: { dark: "#17324D", light: "#BFDDF2" },
  chapter: { dark: "#1E6F68", light: "#C4E9DA" },
  topic: { dark: "#2D5B87", light: "#F4F8FC" },
  exercise: { dark: "#B7791F", light: "#FFE8A3" },
  project: { dark: "#B7791F", light: "#FFE8A3" },
  question: { dark: "#6B46C1", light: "#E3D8FF" },
  challenge: { dark: "#C2410C", light: "#FFD6C7" },
  reading: { dark: "#2563EB", light: "#D6E8FF" },
  other: { dark: "#64748B", light: "#E5E7EB" },
  output: { dark: "#2F6F4E", light: "#D6F0DD" },
  sequence: { dark: "#4B5563", light: "#EDEFF3" },
};

function itemTypeColor(itemType) {
  const key = String(itemType ?? "").toLowerCase();
  if (key === "reading") return structurePalette.reading;
  if (key === "challenge") return structurePalette.challenge;
  if (key === "project") return structurePalette.project;
  if (key === "question") return structurePalette.question;
  return structurePalette.other;
}

function colName(index) {
  let n = index + 1;
  let name = "";
  while (n > 0) {
    const r = (n - 1) % 26;
    name = String.fromCharCode(65 + r) + name;
    n = Math.floor((n - 1) / 26);
  }
  return name;
}

function a1(row, col, rowCount, colCount) {
  const start = `${colName(col)}${row + 1}`;
  const end = `${colName(col + colCount - 1)}${row + rowCount}`;
  return `${start}:${end}`;
}

function padRows(rows, cols) {
  return rows.map((row) => {
    const next = [...row];
    while (next.length < cols) next.push("");
    return next.slice(0, cols);
  });
}

function slug(value) {
  return String(value)
    .replace(/[^A-Za-z0-9]+/g, "")
    .slice(0, 38);
}

function addSheet(workbook, name) {
  const sheet = workbook.worksheets.add(name);
  sheet.showGridLines = false;
  return sheet;
}

function setWidths(sheet, widths, rows = 260) {
  widths.forEach((width, col) => {
    sheet.getRangeByIndexes(0, col, rows, 1).format.columnWidthPx = width;
  });
}

function styleTitle(sheet, title, subtitle, cols) {
  const titleRange = sheet.getRange(a1(0, 0, 1, cols));
  titleRange.values = [[title, ...Array(cols - 1).fill("")]];
  titleRange.merge();
  titleRange.format.fill = { type: "solid", color: palette.primary };
  titleRange.format.font = { bold: true, color: palette.primary, size: 16 };
  titleRange.format.horizontalAlignment = "center";
  titleRange.format.verticalAlignment = "middle";
  titleRange.format.rowHeightPx = 34;

  const subtitleRange = sheet.getRange(a1(1, 0, 1, cols));
  subtitleRange.values = [[subtitle, ...Array(cols - 1).fill("")]];
  subtitleRange.merge();
  subtitleRange.format.fill = { type: "solid", color: palette.softBlue };
  subtitleRange.format.font = { italic: true, color: palette.muted, size: 11 };
  subtitleRange.format.horizontalAlignment = "center";
  subtitleRange.format.verticalAlignment = "middle";
  subtitleRange.format.rowHeightPx = 30;
}

function writeTableSheet(workbook, config) {
  const {
    name,
    title,
    subtitle,
    headers,
    rows,
    widths,
    rowHeight = 54,
    tableName,
    startRow = 4,
    headerFills,
    bodyFills,
    rowFillByValue,
    addTable = true,
  } = config;
  const sheet = addSheet(workbook, name);
  const cols = headers.length;
  styleTitle(sheet, title, subtitle, cols);
  setWidths(sheet, widths ?? Array(cols).fill(160), Math.max(rows.length + 12, 180));
  const matrix = [headers, ...padRows(rows, cols)];
  const range = sheet.getRangeByIndexes(startRow, 0, matrix.length, cols);
  range.values = matrix;

  const header = sheet.getRangeByIndexes(startRow, 0, 1, cols);
  header.format.fill = { type: "solid", color: palette.secondary };
  header.format.font = { bold: true, color: "#FFFFFF" };
  header.format.horizontalAlignment = "center";
  header.format.verticalAlignment = "middle";
  header.format.wrapText = true;
  header.format.rowHeightPx = 30;

  const body = sheet.getRangeByIndexes(startRow + 1, 0, rows.length, cols);
  body.format.fill = { type: "solid", color: palette.body };
  body.format.font = { color: palette.text, size: 10 };
  body.format.wrapText = true;
  body.format.verticalAlignment = "top";
  body.format.borders = { preset: "all", style: "thin", color: palette.grid };
  body.format.rowHeightPx = rowHeight;

  if (addTable) {
    const table = sheet.tables.add(a1(startRow, 0, matrix.length, cols), true, tableName ?? slug(name));
    table.style = "TableStyleMedium2";
    table.showFilterButton = true;
  }

  if (headerFills) {
    headerFills.forEach((color, col) => {
      if (!color) return;
      const cell = sheet.getRangeByIndexes(startRow, col, 1, 1);
      cell.format.fill = { type: "solid", color };
      cell.format.font = { bold: true, color: "#FFFFFF" };
    });
  }

  if (bodyFills) {
    bodyFills.forEach((color, col) => {
      if (!color) return;
      sheet.getRangeByIndexes(startRow + 1, col, rows.length, 1).format.fill = { type: "solid", color };
    });
  }

  if (rowFillByValue) {
    const { columnIndex, paletteForValue } = rowFillByValue;
    rows.forEach((row, rowIndex) => {
      const color = paletteForValue(row[columnIndex], row);
      if (!color) return;
      sheet.getRangeByIndexes(startRow + 1 + rowIndex, 0, 1, cols).format.fill = { type: "solid", color };
      const typeCell = sheet.getRangeByIndexes(startRow + 1 + rowIndex, columnIndex, 1, 1);
      const typeColors = itemTypeColor(row[columnIndex]);
      typeCell.format.fill = { type: "solid", color: typeColors.dark };
      typeCell.format.font = { bold: true, color: "#FFFFFF" };
      typeCell.format.horizontalAlignment = "center";
    });
  }

  sheet.freezePanes.freezeRows(startRow + 1);
  return sheet;
}

function writeMergedCurriculumSheet(workbook, course, rows, topicCount) {
  const sheet = addSheet(workbook, "Curriculum Table");
  const headers = ["Unit", "Chapter", "Topic", "Exercise"];
  const startRow = 4;
  const cols = headers.length;
  styleTitle(
    sheet,
    "Unit-wise Curriculum Table",
    "Required EDA-style format: Unit | Chapter | Topic | Exercise | merged Unit and Chapter blocks for ByteXL readability",
    cols,
  );
  setWidths(sheet, [280, 300, 460, 720], Math.max(rows.length + 12, 180));

  const matrix = [headers, ...rows];
  sheet.getRangeByIndexes(startRow, 0, matrix.length, cols).values = matrix;

  const header = sheet.getRangeByIndexes(startRow, 0, 1, cols);
  header.format.font = { bold: true, color: "#FFFFFF" };
  header.format.horizontalAlignment = "center";
  header.format.verticalAlignment = "middle";
  header.format.wrapText = true;
  header.format.rowHeightPx = 34;
  [
    structurePalette.unit.dark,
    structurePalette.chapter.dark,
    structurePalette.topic.dark,
    structurePalette.exercise.dark,
  ].forEach((color, col) => {
    sheet.getRangeByIndexes(startRow, col, 1, 1).format.fill = { type: "solid", color };
  });

  const body = sheet.getRangeByIndexes(startRow + 1, 0, rows.length, cols);
  body.format.font = { color: palette.text, size: 10 };
  body.format.wrapText = true;
  body.format.verticalAlignment = "top";
  body.format.borders = { preset: "all", style: "thin", color: palette.grid };
  body.format.rowHeightPx = 54;

  let blockStart = 0;
  let blockIndex = 0;
  while (blockStart < rows.length) {
    const unit = rows[blockStart][0];
    const chapter = rows[blockStart][1];
    let blockEnd = blockStart + 1;
    while (blockEnd < rows.length && rows[blockEnd][0] === unit && rows[blockEnd][1] === chapter) {
      blockEnd += 1;
    }
    const span = blockEnd - blockStart;
    const excelStart = startRow + 1 + blockStart;
    const topicFill = blockIndex % 2 === 0 ? "#FFFFFF" : structurePalette.topic.light;
    const exerciseFill = blockIndex % 2 === 0 ? structurePalette.exercise.light : "#FFF9E8";

    const blockRange = sheet.getRangeByIndexes(excelStart, 0, span, cols);
    blockRange.format.borders = {
      insideHorizontal: { style: "thin", color: palette.grid },
      insideVertical: { style: "thin", color: palette.grid },
      top: { style: "medium", color: palette.primary },
      bottom: { style: "medium", color: palette.primary },
      left: { style: "thin", color: palette.grid },
      right: { style: "thin", color: palette.grid },
    };

    if (span > 1) {
      sheet.getRangeByIndexes(excelStart, 0, span, 1).merge();
      sheet.getRangeByIndexes(excelStart, 1, span, 1).merge();
    }

    sheet.getRangeByIndexes(excelStart, 0, span, 1).format.fill = { type: "solid", color: structurePalette.unit.light };
    sheet.getRangeByIndexes(excelStart, 1, span, 1).format.fill = { type: "solid", color: structurePalette.chapter.light };
    sheet.getRangeByIndexes(excelStart, 2, span, 1).format.fill = { type: "solid", color: topicFill };
    sheet.getRangeByIndexes(excelStart, 3, span, 1).format.fill = { type: "solid", color: exerciseFill };

    const mergedLabels = sheet.getRangeByIndexes(excelStart, 0, span, 2);
    mergedLabels.format.font = { bold: true, color: palette.primary, size: 10 };
    mergedLabels.format.horizontalAlignment = "center";
    mergedLabels.format.verticalAlignment = "middle";
    mergedLabels.format.wrapText = true;

    blockStart = blockEnd;
    blockIndex += 1;
  }

  sheet.freezePanes.freezeRows(startRow + 1);
  return sheet;
}

function writeStructureLegendSheet(workbook, course) {
  const rows = [
    ["Unit", "Blue", "Top-level ByteXL unit. Use this as the unit name in the product.", course.productUnitTitle ?? "Unit"],
    ["Chapter", "Green", "Chapter grouping under the unit. Each chapter contains readings, projects, questions, and challenges.", "Chapter 1, Chapter 2, ..."],
    ["Topic", "Light neutral blue", "The concept or skill students learn in that chapter.", "Variables, loops, OOP, APIs, testing"],
    ["Exercise", "Gold", "Hands-on task students complete for the topic.", "Code lab, worksheet, mini feature, debugging task"],
    ["Reading", "Blue tag", "Concept explanation or guided lab item to add in ByteXL.", "Use for most topics"],
    ["Challenge", "Coral tag", "Optional or stretch task for fast learners.", "Use after chapter checkpoint or as enrichment"],
    ["Project", "Gold tag", "Mini build, milestone, or capstone artifact.", "Use where topic title includes mini project/product/capstone"],
    ["Question", "Purple tag", "Quiz, checkpoint, output prediction, or debugging question set.", "Use at each chapter end"],
    ["Other", "Gray tag", "Orientation, setup, notes, or teacher framing item.", "Use at chapter start"],
  ];
  const sheet = writeTableSheet(workbook, {
    name: "Structure Legend",
    title: "Visual Structure Legend",
    subtitle: "Color system used across the workbook to distinguish hierarchy, product item types, and learner outputs",
    headers: ["Structure", "Visual color", "Meaning", "Where to use it"],
    rows,
    widths: [180, 180, 620, 420],
    rowHeight: 58,
    tableName: `${course.shortName}Legend`,
    addTable: false,
    headerFills: [
      structurePalette.unit.dark,
      structurePalette.chapter.dark,
      structurePalette.topic.dark,
      structurePalette.exercise.dark,
    ],
    bodyFills: [
      "#FFFFFF",
      "#FFFFFF",
      "#FFFFFF",
      "#FFFFFF",
    ],
  });

  rows.forEach((row, index) => {
    const key = row[0].toLowerCase();
    let colors = structurePalette.other;
    if (key === "unit") colors = structurePalette.unit;
    if (key === "chapter") colors = structurePalette.chapter;
    if (key === "topic") colors = structurePalette.topic;
    if (key === "exercise") colors = structurePalette.exercise;
    if (key === "reading") colors = structurePalette.reading;
    if (key === "challenge") colors = structurePalette.challenge;
    if (key === "project") colors = structurePalette.project;
    if (key === "question") colors = structurePalette.question;
    if (key === "other") colors = structurePalette.other;
    const rowNumber = 5 + 1 + index;
    sheet.getRangeByIndexes(rowNumber - 1, 0, 1, 4).format.fill = { type: "solid", color: colors.light };
    const swatch = sheet.getRangeByIndexes(rowNumber - 1, 1, 1, 1);
    swatch.format.fill = { type: "solid", color: colors.dark };
    swatch.format.font = { bold: true, color: "#FFFFFF" };
    swatch.format.horizontalAlignment = "center";
  });

  return sheet;
}

function topic(topic, exercise, opts = {}) {
  return { topic, exercise, ...opts };
}

const sourceNotes = [
  ["Uploaded workbook", "/Users/suman/Downloads/Course Blueprint for Java Foundations.xlsx", "Used for foundational sequencing, course structure conventions, and taxonomy depth. Improved by adding learner purpose, exercises, projects, mistakes, use cases, and assessment design."],
  ["Uploaded workbook", "/Users/suman/Downloads/Course Blueprint for Advanced Java.xlsx", "Used for advanced software engineering scope: collections, file I/O, JSON, concurrency, database programming, design principles, build tools, and testing. Adapted into Pythonic equivalents."],
  ["Uploaded workbook", "/Users/suman/Downloads/Exploratory Data Analysis Curriculum.xlsx", "Used as the structural model for Unit, Chapter, Topic, Exercise, plus challenge and assessment rhythm. Extended with trainer-ready learning design."],
  ["Harvard CS50P", "https://cs50.harvard.edu/python/syllabus/", "Inspired the progression through functions, variables, conditionals, loops, exceptions, unit tests, libraries, file I/O, regex, and classes."],
  ["MIT 6.100L", "https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/pages/syllabus/", "Inspired confidence-building for learners with little to no programming experience, finger exercises, problem sets, and computation as practical problem solving."],
  ["Stanford CS106A", "https://web.stanford.edu/class/archive/cs/cs106a/cs106a.1202/handouts/syllabus-cs106a.html", "Inspired guided programming, lab-style lectures, decomposition, style, text processing, debugging, performance, and whole-program structure."],
  ["UC Berkeley CS61A", "https://cs61a.org/articles/about-61a/", "Inspired labs, discussion groups, pair programming, larger projects, abstraction, and careful AI-use guidance."],
  ["Oxford CS Practicals", "https://www.cs.ox.ac.uk/teaching/courses/2025-2026/practicals/", "Inspired practical sign-off, report-based evidence, demonstrator discussions, and evaluating implemented programs."],
  ["MIT Missing Semester", "https://missing.csail.mit.edu/", "Inspired command-line fluency, development tools, debugging/profiling, Git, packaging, code quality, and responsible AI tool awareness."],
  ["Google Python Class", "https://developers.google.com/edu/python", "Inspired sequential exercises that move from strings and lists to full programs using files and HTTP connections."],
  ["Practical Python Programming", "https://dabeaz-course.github.io/practical-python/", "Inspired an exercise-heavy professional training style centered on script writing, data manipulation, and program organization."],
];

const fundamentalsUnits = [
  {
    unit: "Unit 1: Programmer Mindset and Python Setup",
    chapters: [
      {
        chapter: "Chapter 1: Why Programming Matters",
        purpose: "Students see programming as a way to automate decisions, organize information, and build useful tools.",
        analogy: "A program is like a recipe that can make decisions while it runs.",
        topics: [
          topic("What is programming? Inputs, processing, outputs", "Map three everyday tasks - fee payment, food ordering, attendance - into input, processing, and output steps.", { interview: "Explain the difference between data, instructions, and output using a real app." }),
          topic("Why Python? Readability, ecosystem, and real-world uses", "Compare how Python is used in automation, web APIs, data analysis, AI, testing, and scripting; write one use case you care about.", { activity: "Students vote on a problem they want Python to solve by the end of the course." }),
          topic("Computational thinking: decomposition, pattern recognition, abstraction", "Break an ATM withdrawal process into smaller functions on paper before writing any code.", { bug: "A vague problem statement leads to code that mixes input, logic, and output." }),
          topic("Pseudocode and flowcharts before code", "Create pseudocode and a simple flowchart for a scholarship eligibility checker.", { challenge: "Convert the flowchart into nested conditions once conditionals are taught." }),
        ],
      },
      {
        chapter: "Chapter 2: Working Environment",
        purpose: "Students learn how code moves from editor to interpreter to output.",
        analogy: "The editor is the notebook, the interpreter is the teacher checking each instruction, and the terminal is the conversation window.",
        topics: [
          topic("Python interpreter, scripts, notebooks, and terminals", "Run the same profile-printing program in a REPL, a .py file, and a notebook cell; note what changes.", { lab: "Build `hello_profile.py` that prints name, branch, goal, and one Python use case." }),
          topic("Installing Python, VS Code/PyCharm, and Jupyter options", "Set up a local or browser-based environment and submit a screenshot plus `python --version` output.", { bug: "Fix a path or interpreter mismatch where the terminal runs a different Python version." }),
          topic("Running, stopping, and rerunning programs safely", "Create a script with an intentional infinite loop, stop it safely, then repair it with a counter.", { why: "Students need confidence controlling programs before loops become complex." }),
          topic("Folder structure, README files, and naming conventions", "Create a course workspace with `labs`, `projects`, and `notes` folders plus a README describing your learning goal.", { challenge: "Initialize a Git repository and make a first commit if Git is available." }),
        ],
      },
    ],
  },
  {
    unit: "Unit 2: Data, Variables, and Expressions",
    chapters: [
      {
        chapter: "Chapter 3: Variables and Core Data Types",
        purpose: "Students learn how programs remember information and represent real-world values.",
        analogy: "Variables are labelled containers; data types are the shape of what can go inside.",
        topics: [
          topic("Variables, assignment, identifiers, and naming style", "Build a student profile card using variables for name, age, city, course, and weekly learning target.", { bug: "Fix invalid names, accidental spaces, and variables used before assignment." }),
          topic("Numbers: int, float, rounding, and precision awareness", "Create a bill splitter that handles tax, discount, tip, and number of people.", { interview: "Why might money calculations need careful rounding?" }),
          topic("Strings, quotes, escape characters, and f-strings", "Generate a clean receipt message using f-strings and aligned output.", { challenge: "Add currency formatting and plural handling." }),
          topic("Booleans and None as signals", "Model login state, payment state, and optional coupon code with booleans and `None`.", { bug: "Debug code that checks `None` using equality in inconsistent ways." }),
          topic("Type conversion and input from users", "Build a BMI and category calculator that converts text input into numeric values.", { ai: "Ask an AI tutor to explain why `input()` returns text; verify by printing `type()`." }),
        ],
      },
      {
        chapter: "Chapter 4: Operators and Expressions",
        purpose: "Students turn stored data into computed decisions and results.",
        analogy: "Operators are the buttons on a calculator, but code lets you chain them into business rules.",
        topics: [
          topic("Arithmetic operators and precedence", "Predict and then run 12 expressions involving parentheses, powers, floor division, and modulo.", { lab: "Create a time converter from total minutes to hours and minutes." }),
          topic("Comparison operators and truth tables", "Write eligibility checks for age, score, attendance, and fee status.", { interview: "Explain why `=` and `==` mean different things." }),
          topic("Logical operators: and, or, not", "Build a movie-ticket discount rule with age, day, student status, and coupon validity.", { bug: "Fix a condition that is always true because `or` is used incorrectly." }),
          topic("Readable comments and clean expression formatting", "Refactor a messy discount calculator into readable lines with meaningful names.", { challenge: "Add type hints and explain one variable name change." }),
          topic("Mini project: Personal finance calculator", "Create a console app that calculates monthly savings, wants/needs split, and emergency-fund progress.", { milestone: "Capstone habit: define inputs, outputs, and validation before coding." }),
        ],
      },
    ],
  },
  {
    unit: "Unit 3: Decisions and Repetition",
    chapters: [
      {
        chapter: "Chapter 5: Conditional Logic",
        purpose: "Students learn to make programs respond differently to different situations.",
        analogy: "Conditionals are like checkpoints at an airport: different passengers take different paths.",
        topics: [
          topic("if, elif, else for branching", "Create a scholarship classifier using marks, income band, and attendance.", { bug: "Fix a missing `else` that leaves the result variable undefined." }),
          topic("Nested conditions and guard clauses", "Build a delivery-fee calculator that checks service area before distance and cart value.", { challenge: "Refactor nested logic into clearer early exits after functions are taught." }),
          topic("match-case for readable multi-way choices", "Create a campus helpdesk menu using `match-case` for category routing.", { interview: "When is `match-case` clearer than many `elif` branches?" }),
          topic("Input validation and defensive decisions", "Reject invalid marks, negative prices, and empty names with friendly messages.", { ai: "Ask AI for five invalid inputs for your program, then test them yourself." }),
        ],
      },
      {
        chapter: "Chapter 6: Loops and Repetition Patterns",
        purpose: "Students automate repeated work without copy-pasting code.",
        analogy: "A loop is a playlist: it keeps playing items until the list ends or you press stop.",
        topics: [
          topic("while loops, counters, and sentinels", "Build an ATM-style menu that repeats until the user chooses Exit.", { bug: "Debug an infinite loop caused by not updating the loop variable." }),
          topic("for loops and range", "Generate multiplication tables, weekly study reminders, and numbered invoices.", { challenge: "Add start, stop, and step inputs with validation." }),
          topic("break, continue, and loop else", "Search for a product in inventory and stop once found; skip discontinued products.", { interview: "Explain the difference between skipping one item and stopping the loop." }),
          topic("Nested loops for grids and combinations", "Print a seating chart and mark reserved seats based on row and column.", { lab: "Create a mini pattern printer with rows, columns, and alignment." }),
          topic("Loop patterns: count, sum, min, max, search", "Analyze a list of scores to find average, highest, lowest, pass count, and first failing student.", { bug: "Fix a max/min algorithm initialized with the wrong value." }),
          topic("Mini project: Number guessing game with analytics", "Build a game that gives hints, counts attempts, stores best score, and handles invalid guesses.", { milestone: "Capstone habit: track state across a repeated workflow." }),
        ],
      },
    ],
  },
  {
    unit: "Unit 4: Text and Collections",
    chapters: [
      {
        chapter: "Chapter 7: Strings as Real-World Text Data",
        purpose: "Students learn that text is structured data, not just words.",
        analogy: "A string is like a row of lockers: each character has a position.",
        topics: [
          topic("Indexing, slicing, and immutability", "Create a username generator from full name, batch year, and department code.", { bug: "Fix off-by-one slicing errors in initials and roll-number extraction." }),
          topic("String methods for cleaning and standardizing text", "Clean messy survey responses by trimming spaces, normalizing case, and replacing symbols.", { lab: "Create a text-cleaning function list to reuse later." }),
          topic("Searching, splitting, joining, and parsing", "Extract hashtags, mentions, and keywords from a social post string.", { challenge: "Add a simple profanity or banned-word filter using a list." }),
          topic("Mini lab: Text message analyzer", "Count words, characters, vowels, suspicious links, and repeated punctuation in messages.", { interview: "How can string processing support spam detection or customer support?" }),
        ],
      },
      {
        chapter: "Chapter 8: Lists and Tuples",
        purpose: "Students model ordered collections and learn mutation carefully.",
        analogy: "A list is a flexible playlist; a tuple is a locked coordinate or record.",
        topics: [
          topic("List creation, indexing, and traversal", "Build a playlist viewer that prints numbered songs and selected song details.", { bug: "Fix an IndexError caused by confusing item number and index." }),
          topic("List methods, mutation, append, insert, remove, sort", "Create a shopping cart that adds, removes, sorts, and totals items.", { interview: "Why can mutability be useful and risky?" }),
          topic("List slicing and copying", "Split a task list into today, upcoming, and backlog without damaging the original list.", { bug: "Debug aliasing when two variables point to the same list." }),
          topic("Nested lists for tables and grids", "Build a gradebook matrix and compute each student's average.", { challenge: "Print the gradebook as aligned columns." }),
          topic("Tuples and unpacking", "Represent coordinates, RGB values, and database-like rows using tuples and unpacking.", { lab: "Swap two variables without a temporary variable." }),
        ],
      },
      {
        chapter: "Chapter 9: Dictionaries and Sets",
        purpose: "Students learn fast lookup, structured records, and uniqueness.",
        analogy: "A dictionary is a contact book; a set is a guest list that refuses duplicates.",
        topics: [
          topic("Dictionary keys, values, and lookup", "Create a contact book that searches phone numbers by name.", { bug: "Fix KeyError by using `get()` or membership checks." }),
          topic("Updating and iterating dictionaries", "Track inventory quantity and price, then compute stock value by item.", { interview: "When is a dictionary better than a list?" }),
          topic("Nested dictionaries for records", "Model students with name, marks, attendance, and placement interest.", { challenge: "Convert the nested dictionary into a printed report card." }),
          topic("Sets for uniqueness and membership", "Remove duplicate registrations and find common interests between two clubs.", { lab: "Compute union, intersection, and difference for event attendee lists." }),
          topic("Mini product build: Campus event planner", "Build a menu-driven planner using lists, dictionaries, and sets to manage events, registrations, and duplicate checks.", { milestone: "Capstone habit: choose data structures based on the questions the app must answer." }),
        ],
      },
    ],
  },
  {
    unit: "Unit 5: Functions and Reusable Program Design",
    chapters: [
      {
        chapter: "Chapter 10: Functions",
        purpose: "Students move from scripts to reusable, testable building blocks.",
        analogy: "A function is a vending machine: inputs go in, predictable output comes out.",
        topics: [
          topic("Defining and calling functions", "Create reusable functions for area, perimeter, temperature conversion, and grade category.", { bug: "Fix a function that prints a result but returns `None` unexpectedly." }),
          topic("Parameters, arguments, and return values", "Build payroll functions for gross pay, deductions, net pay, and payslip text.", { interview: "Explain why returning values improves reuse and testing." }),
          topic("Scope, local variables, and global pitfalls", "Debug a score tracker that accidentally changes or reads the wrong variable.", { ai: "Ask AI to explain a scope error, then draw the local/global variable boxes." }),
          topic("Default arguments and keyword arguments", "Create a ticket-pricing function with optional discount, tax, and currency.", { challenge: "Avoid mutable default arguments in a list-building function." }),
          topic("Docstrings, type hints, and readable APIs", "Document three utility functions and add simple type hints for parameters and returns.", { lab: "Peer review function names and docstrings for clarity." }),
        ],
      },
      {
        chapter: "Chapter 11: Decomposition and Small-Program Architecture",
        purpose: "Students learn how to break a program into understandable parts.",
        analogy: "A well-built program is a campus map: each building has a clear job and path.",
        topics: [
          topic("Decomposing a monolithic script", "Refactor a 60-line marks analyzer into input, validation, processing, and output functions.", { bug: "Fix duplicated logic that calculates grade category in two places differently." }),
          topic("Designing function contracts", "Write preconditions and expected outputs for functions before coding them.", { interview: "What should a function promise to its caller?" }),
          topic("Manual tests and table-driven examples", "Create a table of inputs and expected outputs for a discount function, then verify it.", { challenge: "Turn the table into assert statements." }),
          topic("Intro to recursion through trace diagrams", "Trace factorial and countdown recursively, then compare to a loop version.", { why: "Recursion builds mental models for later algorithms without overloading beginners." }),
          topic("Mini project: CLI quiz engine", "Build a quiz app with functions for loading questions, asking, scoring, and showing feedback.", { milestone: "Capstone habit: separate data, logic, and presentation." }),
        ],
      },
    ],
  },
  {
    unit: "Unit 6: Files, Errors, and Persistence",
    chapters: [
      {
        chapter: "Chapter 12: File Handling",
        purpose: "Students make programs remember work beyond one run.",
        analogy: "Files are the program's long-term memory.",
        topics: [
          topic("Paths, folders, and safe file organization", "Create a notes folder and write a script that checks whether required files exist.", { bug: "Fix code that works only on one laptop because of a hard-coded absolute path." }),
          topic("Reading and writing text files", "Build a daily journal analyzer that counts entries, words, and most frequent mood tag.", { lab: "Add append mode so new entries do not overwrite previous ones." }),
          topic("CSV files for tabular data", "Read an attendance CSV and calculate attendance percentage by student.", { interview: "Why is CSV still common in business tools?" }),
          topic("JSON files for structured data", "Save and load settings for a habit tracker using JSON.", { challenge: "Pretty-print JSON and handle a missing settings file." }),
        ],
      },
      {
        chapter: "Chapter 13: Error Handling and Debugging",
        purpose: "Students learn to make programs fail kindly and recover.",
        analogy: "Exception handling is a safety net under a trapeze act: the goal is still to perform well, but mistakes are handled.",
        topics: [
          topic("Reading tracebacks like clues", "Diagnose five broken snippets and identify file, line number, error type, and likely cause.", { bug: "Fix TypeError, ValueError, IndexError, KeyError, and FileNotFoundError examples." }),
          topic("try, except, else, finally", "Build robust numeric input and file-reading flows with friendly retry messages.", { interview: "When should you catch an exception and when should you let it fail?" }),
          topic("Raising exceptions for invalid states", "Create validators for age, mark, email-like text, and quantity.", { challenge: "Design helpful error messages that tell the user how to fix the issue." }),
          topic("Debugging with print, breakpoints, and trace tables", "Use the debugger to step through a faulty expense calculation and repair it.", { ai: "Ask AI for possible causes of a traceback, then verify each cause manually." }),
          topic("Mini project: Expense tracker with CSV and JSON", "Build an expense tracker that saves transactions to CSV and settings to JSON, with validation and helpful errors.", { milestone: "Capstone habit: combine persistence, validation, and user experience." }),
        ],
      },
    ],
  },
  {
    unit: "Unit 7: Problem Solving, Testing, and Code Quality",
    chapters: [
      {
        chapter: "Chapter 14: Core Problem-Solving Patterns",
        purpose: "Students practice reusable patterns that appear in interviews and real apps.",
        analogy: "Problem-solving patterns are like common moves in a sport: once learned, they appear everywhere.",
        topics: [
          topic("Linear search and membership checks", "Find the first absent student, first overdue invoice, and first invalid mark in a list.", { interview: "Explain when a loop search is enough and when a dictionary would be better." }),
          topic("Counting and frequency maps", "Count word frequency in feedback comments and print the top repeated words.", { bug: "Fix a dictionary counter that forgets to initialize a missing key." }),
          topic("Sorting with sorted, reverse, and key", "Sort products by price, rating, and stock priority.", { challenge: "Sort student records by marks descending and name ascending." }),
          topic("Complexity intuition without heavy math", "Compare a single loop and nested loop by counting operations for different input sizes.", { lab: "Time two duplicate-detection approaches using small lists." }),
        ],
      },
      {
        chapter: "Chapter 15: Testing and Review Foundations",
        purpose: "Students learn that correctness is designed, not hoped for.",
        analogy: "Tests are like seatbelts: they do not drive the car, but they protect every trip.",
        topics: [
          topic("Assertions for quick checks", "Write assert checks for grade, discount, and username functions.", { bug: "Fix an assertion that checks the wrong expected value." }),
          topic("Beginner unit testing with simple test files", "Create a `test_utils.py` file with tests for three utility functions.", { challenge: "Run the tests from the terminal and capture pass/fail output." }),
          topic("Code review checklist: clarity, duplication, naming, edge cases", "Review a peer's mini project using a structured checklist and give two actionable suggestions.", { interview: "What makes code maintainable for a teammate?" }),
          topic("Mini project: Command-line study planner", "Build a study planner that stores tasks, marks progress, handles missed deadlines, and includes basic tests.", { milestone: "Capstone habit: demonstrate correctness with tests and a README." }),
        ],
      },
    ],
  },
  {
    unit: "Unit 8: Beginner Product Studio",
    chapters: [
      {
        chapter: "Chapter 16: Building and Presenting Complete Beginner Projects",
        purpose: "Students integrate fundamentals into small products they can demo.",
        analogy: "A project is a small shop: it needs a front counter, back room, rules, and records.",
        topics: [
          topic("CLI app structure: menu, actions, validation, storage", "Scaffold a menu-driven app with Add, View, Search, Update, Delete, Save, and Exit.", { lab: "Use functions for each menu action." }),
          topic("Documentation, README, and demo storytelling", "Write a README with problem, users, features, setup, sample run, and limitations.", { activity: "Students do a two-minute demo: problem, feature, bug fixed, next step." }),
          topic("Capstone milestone 1: Problem and user story", "Choose a capstone problem and write three user stories plus success criteria.", { ai: "Ask AI to critique whether the user stories are specific; revise without copying code." }),
          topic("Capstone milestone 2: Data model and flow", "Design the list/dictionary/file structure and draw the program flow before coding.", { challenge: "Identify one edge case per user story." }),
          topic("Capstone milestone 3: Build, test, debug, present", "Deliver a working beginner Python product with persistent data, validation, tests, and demo script.", { interview: "Be ready to explain one bug you fixed and one design trade-off." }),
        ],
      },
    ],
  },
];

const advancedUnits = [
  {
    unit: "Unit 1: Professional Python Workspace and Project Structure",
    chapters: [
      {
        chapter: "Chapter 1: Environment, Tooling, and Workflow",
        purpose: "Students move from single scripts to repeatable professional workspaces.",
        analogy: "A virtual environment is a separate toolbox for each project.",
        topics: [
          topic("Python versions, virtual environments, pip, and dependency isolation", "Create a venv, install `requests` and `pytest`, freeze dependencies, and explain why isolation matters.", { bug: "Fix a project that works globally but fails inside a fresh venv." }),
          topic("Command line fluency for Python developers", "Use terminal commands to create folders, run scripts, pass arguments, and inspect files.", { source: "MIT Missing Semester inspired tool fluency." }),
          topic("Project layout: scripts, packages, tests, data, docs", "Refactor a flat folder into `src`, `tests`, `data`, and `docs` with a clear README.", { interview: "Why does project layout matter after the first week of development?" }),
          topic("Git basics for curriculum projects", "Create feature branches, commit meaningful milestones, and write a short changelog.", { challenge: "Resolve a simple merge conflict in a README." }),
        ],
      },
      {
        chapter: "Chapter 2: Modules, Packages, and Imports",
        purpose: "Students learn how Python code is organized and reused across files.",
        analogy: "Modules are rooms, packages are buildings, and imports are doors between them.",
        topics: [
          topic("Modules, import styles, and namespace clarity", "Split a utility script into modules and import only what each file needs.", { bug: "Fix shadowing caused by naming a file `random.py`." }),
          topic("__name__, runnable modules, and script entry points", "Create a module that can be imported without running its CLI demo.", { interview: "Explain why `if __name__ == '__main__'` exists." }),
          topic("Package structure and __init__.py", "Build a small `texttools` package with cleaning, counting, and formatting modules.", { challenge: "Expose a clean public API from `__init__.py`." }),
          topic("argparse and command-line interfaces", "Create a CLI that accepts input file, output file, and mode flags.", { lab: "Add helpful `--help` text and invalid argument handling." }),
          topic("Mini product build: Reusable text utility package", "Package a text-cleaning tool that can be imported or run from the command line.", { milestone: "Capstone habit: every project must be runnable, importable, and documented." }),
        ],
      },
    ],
  },
  {
    unit: "Unit 2: Object-Oriented Python and Data Modeling",
    chapters: [
      {
        chapter: "Chapter 3: Classes, Objects, and Encapsulation",
        purpose: "Students model real-world entities with behavior and state.",
        analogy: "A class is a blueprint; an object is a specific building made from it.",
        topics: [
          topic("Classes, instances, attributes, and methods", "Model a bank account with deposit, withdraw, balance, and transaction history.", { bug: "Fix code that stores shared state as a class variable by accident." }),
          topic("Constructors, invariants, and validation", "Create a `CourseEnrollment` class that rejects invalid marks, duplicate student IDs, and negative fees.", { interview: "What should always be true after an object is created?" }),
          topic("Encapsulation, properties, and controlled mutation", "Add validated properties to an inventory item so stock cannot become negative.", { challenge: "Log every stock change through a method." }),
          topic("dataclasses for simple data carriers", "Refactor plain dictionaries into `dataclass` records for products or tickets.", { lab: "Compare printed output and equality behavior before and after dataclasses." }),
        ],
      },
      {
        chapter: "Chapter 4: Relationships and Python Protocols",
        purpose: "Students learn composition, polymorphism, and Pythonic object behavior.",
        analogy: "Composition is building with parts; inheritance is specializing a base idea.",
        topics: [
          topic("Composition vs inheritance", "Design a course platform using `Student`, `Course`, `Lesson`, and `ProgressTracker` objects.", { bug: "Refactor an inheritance tree that should have used composition." }),
          topic("Inheritance, overriding, and polymorphism", "Create notification classes for email, SMS, and in-app messages with a shared interface.", { interview: "When is polymorphism more flexible than if/else type checks?" }),
          topic("Magic methods: __str__, __repr__, __len__, __eq__", "Build a `Playlist` or `Cart` class that behaves naturally with print, len, and equality.", { challenge: "Add ordering for leaderboard entries." }),
          topic("Protocols and duck typing", "Write a function that accepts any object with a `send()` method and test it with multiple classes.", { ai: "Ask AI for two examples of duck typing; identify which one is unsafe and why." }),
          topic("Mini product build: Training center management model", "Model students, courses, batches, attendance, and reports using OOP and composition.", { milestone: "Capstone habit: create a domain model before writing storage or UI code." }),
        ],
      },
    ],
  },
  {
    unit: "Unit 3: Pythonic Abstractions and Functional Techniques",
    chapters: [
      {
        chapter: "Chapter 5: Functions as First-Class Objects",
        purpose: "Students use functions as values to reduce repetition and build flexible behavior.",
        analogy: "Passing a function is like handing someone a strategy card they can apply later.",
        topics: [
          topic("First-class functions and callbacks", "Build a report generator that accepts different scoring functions.", { bug: "Fix a callback that is called too early instead of being passed." }),
          topic("Lambda, key functions, and sorted transformations", "Sort complex student and product records by multiple business rules.", { interview: "When is a named function clearer than a lambda?" }),
          topic("map, filter, any, all, zip, enumerate", "Transform and validate batches of form submissions using built-ins.", { challenge: "Rewrite one built-in solution as an explicit loop and compare readability." }),
          topic("Comprehensions for lists, dicts, and sets", "Build transformed records, reverse lookup dictionaries, and unique tag sets.", { bug: "Fix a comprehension that hides too much logic in one line." }),
        ],
      },
      {
        chapter: "Chapter 6: Decorators, Iterators, Generators, Context Managers",
        purpose: "Students master Python abstractions that appear in frameworks and libraries.",
        analogy: "A decorator is a wrapper on a gift: the original function remains, but behavior is added around it.",
        topics: [
          topic("Decorators without arguments", "Write a timing decorator and apply it to report-generation functions.", { interview: "Explain how a decorator changes a function call." }),
          topic("Decorators with arguments and functools.wraps", "Create a retry decorator for flaky network-like functions.", { bug: "Fix lost function metadata by adding `functools.wraps`." }),
          topic("Iterators and the iterator protocol", "Build a custom `BatchReader` that yields chunks of records.", { challenge: "Make the iterator resettable or document why it is one-pass." }),
          topic("Generators and yield for streaming data", "Process a large log file line by line and yield only error records.", { lab: "Compare memory use between list loading and generator streaming." }),
          topic("Context managers with with and contextlib", "Create a timer context manager and a safe temporary-file writer.", { bug: "Fix resource leaks caused by missing file close calls." }),
          topic("Mini product build: Streaming log analyzer", "Build a tool that streams logs, filters patterns, times processing, and writes a summary report.", { milestone: "Capstone habit: choose lazy processing when data may grow." }),
        ],
      },
    ],
  },
  {
    unit: "Unit 4: Advanced Data Handling, Text Automation, and APIs",
    chapters: [
      {
        chapter: "Chapter 7: Files, Serialization, and Configuration",
        purpose: "Students handle real project files safely and flexibly.",
        analogy: "Configuration is the control panel; data files are the project memory.",
        topics: [
          topic("pathlib, shutil, glob, and file organization", "Build a downloads organizer that groups files by extension and date.", { bug: "Fix path code that breaks on Windows or macOS." }),
          topic("CSV, JSON, and nested data transformation", "Convert messy JSON API-like data into a normalized CSV report.", { interview: "When is JSON better than CSV?" }),
          topic("Configuration files and environment variables", "Read app settings from `.env` or config files without hard-coding secrets.", { challenge: "Add environment-specific config for dev and test." }),
          topic("Robust file pipelines and backup strategy", "Write an import pipeline that validates input, writes output atomically, and keeps backups.", { lab: "Simulate a failure halfway through and confirm the original file survives." }),
        ],
      },
      {
        chapter: "Chapter 8: Regular Expressions and APIs",
        purpose: "Students extract meaning from text and communicate with web services.",
        analogy: "Regex is a stencil for finding patterns; an API is a service counter for software.",
        topics: [
          topic("Regular expression basics: literals, classes, groups, anchors", "Extract invoice IDs, dates, phone numbers, and course codes from messy text.", { source: "Google Python Class and CS50P inspired regex placement." }),
          topic("Regex substitution and validation", "Clean log lines and validate simple email-like and roll-number formats.", { bug: "Fix a greedy regex that captures too much text." }),
          topic("HTTP fundamentals, requests, status codes, JSON responses", "Call a public API, inspect status code, parse JSON, and handle failure cases.", { interview: "What does a 404 or 429 response mean for your program?" }),
          topic("API authentication, pagination, rate limits, and retries", "Design a resilient API client skeleton with retry/backoff and clear error messages.", { challenge: "Mock the API response before calling the real service." }),
          topic("Mini product build: API-powered dashboard data collector", "Collect public API data, clean it, save it to CSV/JSON, and produce a summary report.", { milestone: "Capstone habit: separate API, parsing, storage, and reporting layers." }),
        ],
      },
    ],
  },
  {
    unit: "Unit 5: Reliability - Testing, Debugging, Logging, and Quality",
    chapters: [
      {
        chapter: "Chapter 9: Testing with pytest",
        purpose: "Students learn to protect behavior as programs evolve.",
        analogy: "Tests are a contract with your future self.",
        topics: [
          topic("pytest basics, assertions, and test discovery", "Write pytest tests for validators, formatters, and calculators.", { bug: "Fix tests that pass accidentally because they do not assert anything." }),
          topic("Parametrized tests and edge-case design", "Test discount rules with normal, boundary, and invalid values using parametrization.", { interview: "What is an edge case and why do teams track them?" }),
          topic("Fixtures and temporary files", "Test a file importer without touching real project data.", { challenge: "Use a temporary directory fixture for output files." }),
          topic("Mocking APIs and external services", "Test an API client using fake responses for success, timeout, and bad status.", { ai: "Ask AI for possible edge cases, then convert only the useful ones into tests." }),
          topic("TDD and regression testing", "Reproduce a reported bug with a failing test, fix the code, and keep the test.", { milestone: "Capstone habit: every fixed bug leaves a test behind." }),
        ],
      },
      {
        chapter: "Chapter 10: Debugging, Logging, Profiling, and Static Quality",
        purpose: "Students diagnose issues systematically and keep code production-friendly.",
        analogy: "Logs are a flight recorder; profiling is a stopwatch for code.",
        topics: [
          topic("pdb, breakpoints, and structured debugging", "Step through a failing order-processing workflow and inspect variables at each stage.", { bug: "Fix a bug caused by mutation across function calls." }),
          topic("logging levels, handlers, and useful messages", "Add debug, info, warning, and error logs to a CLI app.", { interview: "What should go in logs and what should never be logged?" }),
          topic("Profiling with timeit and cProfile", "Find the slowest function in a data-cleaning script and optimize one bottleneck.", { challenge: "Compare readability before and after optimization." }),
          topic("Type hints, mypy mindset, linting, and formatting", "Add type hints and run a formatter/linter on a small package.", { lab: "Fix three style issues without changing behavior." }),
          topic("Mini product build: Tested CLI toolkit", "Ship a CLI utility with tests, logging, type hints, and documented commands.", { milestone: "Capstone habit: quality gates are part of the product, not an afterthought." }),
        ],
      },
    ],
  },
  {
    unit: "Unit 6: Databases and Persistent Applications",
    chapters: [
      {
        chapter: "Chapter 11: SQL and SQLite from Python",
        purpose: "Students store, query, and protect structured application data.",
        analogy: "A database is a library with indexes, rules, and a librarian that answers questions.",
        topics: [
          topic("Relational thinking: tables, rows, columns, keys", "Design tables for students, courses, enrollments, and attendance.", { interview: "Why is duplicate data dangerous in a database?" }),
          topic("SQLite setup and basic SQL", "Create tables and run SELECT, INSERT, UPDATE, DELETE queries from a SQLite shell or notebook.", { bug: "Fix a query that returns too many rows because of a missing WHERE clause." }),
          topic("Python DB-API and parameterized queries", "Build safe CRUD functions using sqlite3 and parameterized values.", { challenge: "Show how string-formatted SQL can become unsafe." }),
          topic("Transactions, commits, rollbacks, and constraints", "Simulate a failed fee payment update and roll it back cleanly.", { lab: "Add NOT NULL, UNIQUE, and foreign key constraints." }),
          topic("Intro to ORM thinking", "Map a simple Python object to a database row and discuss ORM trade-offs.", { ai: "Ask AI to compare raw SQL and ORM, then add your own project-specific conclusion." }),
          topic("Mini product build: Personal CRM with SQLite", "Build a contact and follow-up tracker with CRUD operations, search, tests, and seed data.", { milestone: "Capstone habit: database schema is a design artifact." }),
        ],
      },
    ],
  },
  {
    unit: "Unit 7: Performance, Concurrency, and Production Readiness",
    chapters: [
      {
        chapter: "Chapter 12: Performance and Scaling Mindset",
        purpose: "Students learn when and how to optimize without guessing.",
        analogy: "Optimization is medicine: diagnose first, treat only what is sick.",
        topics: [
          topic("Big-O intuition for Python developers", "Compare list membership, set membership, nested loops, and dictionary lookup using timing experiments.", { interview: "Why can a set lookup be faster than scanning a list?" }),
          topic("Memory-aware programming and generators", "Process a simulated large CSV using generator pipelines instead of loading all rows.", { bug: "Fix memory blow-up caused by converting a generator to a list too early." }),
          topic("Caching with functools.lru_cache", "Speed up repeated expensive calculations or API-like lookups with caching.", { challenge: "Invalidate cache intentionally and explain stale data risk." }),
          topic("Vectorization awareness and library boundaries", "Identify when a loop should stay Python and when a library like pandas would be appropriate.", { lab: "Rewrite a slow pure-Python aggregate using a more suitable structure." }),
        ],
      },
      {
        chapter: "Chapter 13: Concurrency and Shipping Code",
        purpose: "Students understand responsible concurrency and basic packaging.",
        analogy: "Concurrency is a kitchen with several cooks; coordination matters more than speed alone.",
        topics: [
          topic("Threading and concurrent.futures for I/O-bound work", "Download or simulate multiple API calls concurrently and compare total time.", { bug: "Fix shared-state mutation in threaded code." }),
          topic("asyncio basics and async HTTP mindset", "Trace an async workflow with await, tasks, and event loop concepts.", { challenge: "Rewrite a sequential fake API caller using async tasks." }),
          topic("Packaging basics: pyproject, build, console scripts", "Package a small CLI tool and install it into a fresh virtual environment.", { source: "MIT Missing Semester inspired packaging and shipping code." }),
          topic("Secrets, environment variables, and safe configuration", "Move API keys and credentials out of code into environment configuration.", { interview: "Why should secrets not be committed to Git?" }),
          topic("Mini product build: Concurrent API monitor", "Build a monitor that checks several endpoints, logs status, caches results, and writes a report.", { milestone: "Capstone habit: production readiness includes performance, logs, config, and failure modes." }),
        ],
      },
    ],
  },
  {
    unit: "Unit 8: Clean Code, Design Patterns, and Architecture",
    chapters: [
      {
        chapter: "Chapter 14: Clean Code and Refactoring",
        purpose: "Students make code easier to change without breaking it.",
        analogy: "Refactoring is cleaning a room without throwing away the furniture.",
        topics: [
          topic("Clean code principles: names, small functions, single responsibility", "Refactor a long report script into named functions and service modules.", { bug: "Fix a function that does validation, database work, and printing all at once." }),
          topic("Error design and domain exceptions", "Create custom exceptions for validation, missing records, and external service failures.", { interview: "How do domain errors differ from system errors?" }),
          topic("Layered architecture: UI, service, repository, domain", "Restructure a CLI app so menu code does not directly run SQL queries.", { challenge: "Draw a dependency diagram and identify one forbidden dependency." }),
          topic("Documentation: README, docstrings, examples, decision records", "Write docs that explain setup, commands, design choices, and known limitations.", { ai: "Ask AI to review your README for missing user steps; verify every suggestion manually." }),
        ],
      },
      {
        chapter: "Chapter 15: Practical Design Patterns",
        purpose: "Students recognize reusable design ideas without over-engineering.",
        analogy: "Patterns are proven building layouts, not decorations to force onto every problem.",
        topics: [
          topic("Factory pattern for object creation", "Create different notification sender objects from config values.", { bug: "Fix scattered object-creation if/else blocks." }),
          topic("Strategy pattern for interchangeable business rules", "Implement multiple grading or pricing strategies behind a shared interface.", { interview: "When does Strategy remove complex conditionals?" }),
          topic("Adapter pattern for external APIs", "Wrap two different API response formats behind a common method.", { challenge: "Add tests that prove the service layer does not care which adapter is used." }),
          topic("Observer/event pattern for notifications", "Notify logging, email, and dashboard components when a task status changes.", { lab: "Keep the subject independent from concrete observers." }),
          topic("Singleton caution and dependency injection", "Refactor a hidden global config into explicit dependencies.", { ai: "Ask AI for a Singleton example, then critique why it might hurt testing." }),
          topic("Mini product build: Plugin-based automation app", "Build an app where new processors or notification channels can be added without editing the core loop.", { milestone: "Capstone habit: extension points should be intentional and tested." }),
        ],
      },
    ],
  },
  {
    unit: "Unit 9: Advanced Python Product Studio",
    chapters: [
      {
        chapter: "Chapter 16: Capstone Engineering Sprint",
        purpose: "Students ship a robust Python application that demonstrates advanced concepts end to end.",
        analogy: "The capstone is a small software company in one project: design, build, test, observe, and explain.",
        topics: [
          topic("Capstone milestone 1: Product brief and technical design", "Write a one-page product brief, architecture sketch, data model, risk list, and test strategy.", { activity: "Run a design review with peers before coding." }),
          topic("Capstone milestone 2: Vertical slice", "Build one end-to-end feature through CLI/API layer, domain logic, storage, logs, and tests.", { bug: "Fix integration bugs before adding more features." }),
          topic("Capstone milestone 3: Reliability and performance gate", "Add automated tests, logging, error handling, profiling notes, and config separation.", { challenge: "Include one measured optimization with before/after evidence." }),
          topic("Capstone milestone 4: Packaging, documentation, and demo", "Package or install the app, write docs, and deliver a 5-minute demo with Q&A.", { interview: "Explain architecture, trade-offs, testing strategy, and one failure mode." }),
          topic("Responsible AI-assisted engineering review", "Use AI only for explanation, edge-case brainstorming, test idea generation, and code review prompts; cite usage and verify manually.", { source: "Inspired by Berkeley's explicit AI policy and MIT Missing Semester AI/tooling awareness." }),
        ],
      },
    ],
  },
];

function flattenCurriculum(units) {
  const rows = [];
  const experience = [];
  let count = 1;
  for (const unit of units) {
    for (const chapter of unit.chapters) {
      for (const item of chapter.topics) {
        rows.push([unit.unit, chapter.chapter, item.topic, item.exercise]);
        experience.push([
          unit.unit,
          chapter.chapter,
          item.topic,
          item.why ?? chapter.purpose,
          item.analogy ?? chapter.analogy,
          item.activity ?? `Pair-trace the idea behind "${item.topic}" before writing code; one student predicts, one student verifies by running it.`,
          item.lab ?? item.exercise,
          item.interview ?? `Explain where "${item.topic}" appears in real projects and describe one edge case.`,
          item.bug ?? `Debug a short broken snippet related to "${item.topic}" and write the root cause in one sentence.`,
          item.ai ?? `Ask an AI tutor for a conceptual explanation of "${item.topic}", then verify by writing and running your own example. No copied solutions.`,
          item.challenge ?? "Extend the exercise with validation, tests, file input/output, or a second user scenario.",
        ]);
        count += 1;
      }
    }
  }
  return { rows, experience, topicCount: count - 1 };
}

function chapterBlueprint(units, subject) {
  const rows = [];
  let quiz = 1;
  let assessment = 1;
  for (const unit of units) {
    for (const chapter of unit.chapters) {
      const topicCount = chapter.topics.length;
      const challengeQuestions = Math.max(6, topicCount * 2);
      const assessmentQuestions = Math.max(10, topicCount * 3);
      rows.push([
        subject,
        unit.unit,
        chapter.chapter,
        `Quiz ${quiz}`,
        challengeQuestions,
        assessmentQuestions,
        challengeQuestions + assessmentQuestions,
        `Standardized Assessment ${assessment}`,
        chapter.topics.some((t) => t.topic.toLowerCase().includes("mini") || t.topic.toLowerCase().includes("capstone")) ? "Project gate" : "Concept gate",
      ]);
      quiz += 1;
      if (quiz % 4 === 1) assessment += 1;
    }
  }
  return rows;
}

function buildMetadataRows(course) {
  return [
    ["Strong curriculum title", course.title],
    ["ByteXL product hierarchy", course.productUnitTitle ? `Create exactly one unit named "${course.productUnitTitle}". Add all listed chapters under that single unit.` : "Use the unit and chapter hierarchy shown in the curriculum table."],
    ["Target learner profile", course.target],
    ["Prerequisites", course.prerequisites],
    ["Learning outcomes", course.outcomes.join("\n")],
    ["Estimated duration", course.duration],
    ["Recommended pacing", course.pacing],
    ["Primary pedagogy", course.pedagogy],
    ["Learner promise", course.promise],
    ["Trainer note", course.trainerNote],
  ];
}

function buildTeachingRows(course) {
  return [
    ["Tools/platforms required", "Python 3.12 or newer; VS Code or PyCharm; Jupyter Notebook where useful; terminal; Git/GitHub optional for Fundamentals and recommended for Advanced; pytest and requests for Advanced; SQLite for Advanced database units."],
    ["Classroom mode", "Use 10-12 minute concept bursts followed by immediate code labs. Every lesson should end with a visible artifact: script, function, test, file, report, or mini feature."],
    ["Online mode", "Give starter notebooks or repos, short explainer videos, auto-check quizzes, weekly live debugging clinics, and peer demo rooms."],
    ["Bootcamp mode", "Teach in daily build cycles: concept, guided lab, independent sprint, code review, bug fix, reflection, and product demo."],
    ["Student engagement idea: Bug of the day", "Start each session with one realistic bug. Students predict the error, reproduce it, fix it, and write the lesson learned."],
    ["Student engagement idea: Driver-navigator pairs", "One student types, one explains the next step. Switch roles every 12 minutes to keep both accountable."],
    ["Student engagement idea: Interview minute", "End selected topics with a one-minute oral explanation connected to common junior developer interviews."],
    ["Student engagement idea: Mini product demos", "Every unit ends with a small product demo, not only a quiz. Students show input, behavior, edge case, and one bug fixed."],
    ["Student engagement idea: AI critique lab", "Students may use AI for conceptual explanations, edge-case brainstorming, and code review prompts, but they must run, verify, and cite what they used."],
    ["Trainer rhythm", course.trainerRhythm],
  ];
}

function buildAssessmentRows(course) {
  return course.assessment.map((item) => [
    item.component,
    item.weight,
    item.evidence,
    item.frequency,
    item.rubric,
  ]);
}

function buildProjectRows(projects) {
  return projects.map((p) => [
    p.stage,
    p.type,
    p.project,
    p.outcome,
    p.concepts,
    p.deliverables,
    p.milestone,
    p.assessment,
  ]);
}

function buildMistakeRows(mistakes) {
  return mistakes.map((m) => [m.topic, m.mistake, m.symptom, m.fix, m.debug]);
}

function buildUseCaseRows(useCases) {
  return useCases.map((u) => [u.topic, u.industry, u.useCase, u.task, u.interview]);
}

function buildChallengeRows(challenges) {
  return challenges.map((c) => [c.level, c.theme, c.challenge, c.success, c.support]);
}

function productCompatibleUnits(course) {
  if (!course.productUnitTitle) return course.units;
  return [
    {
      unit: course.productUnitTitle,
      chapters: course.units.flatMap((unit) =>
        unit.chapters.map((chapter) => ({
          ...chapter,
          originalUnit: unit.unit,
        })),
      ),
    },
  ];
}

function productItemType(topicText) {
  const lower = topicText.toLowerCase();
  if (lower.includes("capstone") || lower.includes("mini project") || lower.includes("mini product build")) {
    return "Project";
  }
  if (lower.includes("challenge")) return "Challenge";
  if (lower.includes("assessment") || lower.includes("quiz")) return "Question";
  return "Reading";
}

function byteXlBuildMapRows(course, units) {
  const rows = [];
  let sequence = 1;
  for (const unit of units) {
    for (const chapter of unit.chapters) {
      rows.push([
        unit.unit,
        chapter.chapter,
        "Other",
        "Chapter orientation",
        `Original learning phase: ${chapter.originalUnit ?? unit.unit}. Start with why this chapter matters and the real-world analogy.`,
        "Students can explain the chapter goal before writing code.",
        sequence++,
      ]);
      for (const item of chapter.topics) {
        const type = productItemType(item.topic);
        rows.push([
          unit.unit,
          chapter.chapter,
          type,
          item.topic,
          item.exercise,
          type === "Project"
            ? "Working mini build, milestone artifact, or capstone evidence."
            : "Completed code lab, reflection, debug note, or checked answer.",
          sequence++,
        ]);
      }
      rows.push([
        unit.unit,
        chapter.chapter,
        "Question",
        `${chapter.chapter.replace(/^Chapter\s+\d+:\s*/, "")} checkpoint`,
        "Add 5-8 concept, output-prediction, debugging, and application questions for this chapter.",
        "Students demonstrate understanding before moving to the next chapter.",
        sequence++,
      ]);
      rows.push([
        unit.unit,
        chapter.chapter,
        "Challenge",
        `${chapter.chapter.replace(/^Chapter\s+\d+:\s*/, "")} stretch challenge`,
        "Use the optional challenge from the Topic Experience Map or ask learners to extend the chapter mini build with validation, tests, persistence, or a second user scenario.",
        "Advanced learners produce an extension without slowing the core class.",
        sequence++,
      ]);
    }
  }
  return rows;
}

function createWorkbook(course, fileName) {
  const workbook = Workbook.create();
  const units = productCompatibleUnits(course);
  const { rows, experience, topicCount } = flattenCurriculum(units);

  writeTableSheet(workbook, {
    name: "Overview",
    title: course.title,
    subtitle: `${course.subtitle} | ${topicCount} topic rows | Premium trainer-ready workbook`,
    headers: ["Section", "Details"],
    rows: buildMetadataRows(course),
    widths: [230, 980],
    rowHeight: 76,
    tableName: `${course.shortName}Overview`,
    addTable: false,
    headerFills: [palette.primary, palette.secondary],
    bodyFills: [structurePalette.unit.light, "#FFFFFF"],
  });

  writeStructureLegendSheet(workbook, course);

  writeMergedCurriculumSheet(workbook, course, rows, topicCount);

  writeTableSheet(workbook, {
    name: "ByteXL Build Map",
    title: "ByteXL Course Builder Map",
    subtitle: "Create one unit in the product, then add these chapters and chapter items under that unit",
    headers: ["Product Unit Title", "Chapter", "Item Type", "Item Title", "What to add in ByteXL", "Student output", "Suggested Sequence"],
    rows: byteXlBuildMapRows(course, units),
    widths: [270, 290, 120, 330, 620, 360, 120],
    rowHeight: 72,
    tableName: `${course.shortName}ByteXLMap`,
    addTable: false,
    headerFills: [
      structurePalette.unit.dark,
      structurePalette.chapter.dark,
      structurePalette.other.dark,
      structurePalette.topic.dark,
      structurePalette.reading.dark,
      structurePalette.output.dark,
      structurePalette.sequence.dark,
    ],
    rowFillByValue: {
      columnIndex: 2,
      paletteForValue: (value) => itemTypeColor(value).light,
    },
  });

  writeTableSheet(workbook, {
    name: "Topic Experience Map",
    title: "Chapter-wise Topic Breakdown and Learning Experience",
    subtitle: "Purpose, analogy, activity, code lab, interview connection, bug to debug, AI activity, and challenge for every topic",
    headers: [
      "Unit",
      "Chapter",
      "Topic",
      "Why this topic matters",
      "Real-world analogy",
      "Student activity",
      "Code lab",
      "Interview connection",
      "Common bug to debug",
      "AI-assisted learning activity",
      "Optional challenge",
    ],
    rows: experience,
    widths: [210, 230, 310, 390, 300, 360, 390, 340, 360, 390, 360],
    rowHeight: 96,
    tableName: `${course.shortName}Experience`,
    addTable: false,
    headerFills: [
      structurePalette.unit.dark,
      structurePalette.chapter.dark,
      structurePalette.topic.dark,
      palette.secondary,
      palette.secondary,
      structurePalette.reading.dark,
      structurePalette.exercise.dark,
      structurePalette.question.dark,
      structurePalette.challenge.dark,
      structurePalette.question.dark,
      structurePalette.challenge.dark,
    ],
    bodyFills: [
      structurePalette.unit.light,
      structurePalette.chapter.light,
      structurePalette.topic.light,
      structurePalette.chapter.light,
      "#F0F7F5",
      structurePalette.reading.light,
      structurePalette.exercise.light,
      structurePalette.question.light,
      structurePalette.challenge.light,
      "#F4EFFF",
      "#FFF7ED",
    ],
  });

  writeTableSheet(workbook, {
    name: "Projects Capstone",
    title: "Mini Projects and Capstone Ideas",
    subtitle: "Project ladder from guided builds to independent product demos",
    headers: ["Stage", "Type", "Project", "Product outcome", "Required concepts", "Deliverables", "Capstone milestone", "Assessment evidence"],
    rows: buildProjectRows(course.projects),
    widths: [150, 160, 280, 420, 390, 420, 360, 360],
    rowHeight: 88,
    tableName: `${course.shortName}Projects`,
    addTable: false,
    headerFills: [
      structurePalette.unit.dark,
      structurePalette.project.dark,
      structurePalette.project.dark,
      structurePalette.output.dark,
      structurePalette.topic.dark,
      structurePalette.reading.dark,
      structurePalette.exercise.dark,
      structurePalette.question.dark,
    ],
    bodyFills: [
      structurePalette.unit.light,
      structurePalette.project.light,
      structurePalette.project.light,
      structurePalette.output.light,
      structurePalette.topic.light,
      structurePalette.reading.light,
      structurePalette.exercise.light,
      structurePalette.question.light,
    ],
  });

  writeTableSheet(workbook, {
    name: "Assessment Strategy",
    title: "Assessment Strategy",
    subtitle: "Balanced concept checks, code labs, debugging, projects, review, and capstone performance",
    headers: ["Component", "Weight", "Evidence", "Frequency", "Rubric focus"],
    rows: buildAssessmentRows(course),
    widths: [250, 120, 520, 260, 520],
    rowHeight: 78,
    tableName: `${course.shortName}Assess`,
    addTable: false,
    headerFills: [
      structurePalette.question.dark,
      structurePalette.sequence.dark,
      structurePalette.output.dark,
      structurePalette.chapter.dark,
      structurePalette.topic.dark,
    ],
    bodyFills: [
      structurePalette.question.light,
      structurePalette.sequence.light,
      structurePalette.output.light,
      structurePalette.chapter.light,
      structurePalette.topic.light,
    ],
  });

  writeTableSheet(workbook, {
    name: "Teaching Approach",
    title: "Tools, Teaching Approach, and Student Engagement",
    subtitle: "Designed for classroom, online, and bootcamp-style delivery",
    headers: ["Area", "Recommendation"],
    rows: buildTeachingRows(course),
    widths: [300, 1000],
    rowHeight: 74,
    tableName: `${course.shortName}Teaching`,
    addTable: false,
    headerFills: [structurePalette.chapter.dark, structurePalette.reading.dark],
    bodyFills: [structurePalette.chapter.light, "#FFFFFF"],
  });

  writeTableSheet(workbook, {
    name: "Mistakes Debug Bank",
    title: "Common Mistakes Students Make",
    subtitle: "Use as a trainer debugging bank and student self-check guide",
    headers: ["Topic area", "Common mistake", "How it shows up", "Trainer intervention", "Debug prompt"],
    rows: buildMistakeRows(course.mistakes),
    widths: [240, 360, 360, 430, 430],
    rowHeight: 82,
    tableName: `${course.shortName}Mistakes`,
    addTable: false,
    headerFills: [
      structurePalette.topic.dark,
      structurePalette.challenge.dark,
      structurePalette.challenge.dark,
      structurePalette.output.dark,
      structurePalette.question.dark,
    ],
    bodyFills: [
      structurePalette.topic.light,
      structurePalette.challenge.light,
      "#FFF1EA",
      structurePalette.output.light,
      structurePalette.question.light,
    ],
  });

  writeTableSheet(workbook, {
    name: "Use Cases Interviews",
    title: "Real-world Use Cases and Interview Connections",
    subtitle: "Connect every major skill to a business, product, or engineering use case",
    headers: ["Topic area", "Industry/domain", "Real-world use case", "Hands-on task", "Interview connection"],
    rows: buildUseCaseRows(course.useCases),
    widths: [240, 230, 420, 440, 390],
    rowHeight: 78,
    tableName: `${course.shortName}UseCases`,
    addTable: false,
    headerFills: [
      structurePalette.topic.dark,
      structurePalette.unit.dark,
      structurePalette.output.dark,
      structurePalette.exercise.dark,
      structurePalette.question.dark,
    ],
    bodyFills: [
      structurePalette.topic.light,
      structurePalette.unit.light,
      structurePalette.output.light,
      structurePalette.exercise.light,
      structurePalette.question.light,
    ],
  });

  writeTableSheet(workbook, {
    name: "Challenge Track",
    title: "Optional Challenge Sections for Advanced Learners",
    subtitle: "Stretch paths that keep fast learners engaged without overwhelming beginners",
    headers: ["Level", "Theme", "Challenge", "Success criteria", "Support needed"],
    rows: buildChallengeRows(course.challenges),
    widths: [150, 260, 520, 430, 360],
    rowHeight: 82,
    tableName: `${course.shortName}Challenges`,
    addTable: false,
    headerFills: [
      structurePalette.challenge.dark,
      structurePalette.topic.dark,
      structurePalette.challenge.dark,
      structurePalette.output.dark,
      structurePalette.other.dark,
    ],
    bodyFills: [
      structurePalette.challenge.light,
      structurePalette.topic.light,
      "#FFF1EA",
      structurePalette.output.light,
      structurePalette.other.light,
    ],
  });

  writeTableSheet(workbook, {
    name: "Question Blueprint",
    title: "Question Taxonomy and Assessment Blueprint",
    subtitle: "Mirrors the reference workbook metadata style while adding project gates",
    headers: ["Subject", "Unit", "Chapter", "Quiz", "# Challenge Questions", "# Assessment Questions", "Net Questions / Chapter", "Standardized Assessment", "Gate"],
    rows: chapterBlueprint(units, course.subject),
    widths: [180, 270, 310, 120, 160, 170, 160, 210, 160],
    rowHeight: 54,
    tableName: `${course.shortName}Blueprint`,
    addTable: false,
    headerFills: [
      structurePalette.unit.dark,
      structurePalette.unit.dark,
      structurePalette.chapter.dark,
      structurePalette.question.dark,
      structurePalette.challenge.dark,
      structurePalette.question.dark,
      structurePalette.sequence.dark,
      structurePalette.question.dark,
      structurePalette.project.dark,
    ],
    bodyFills: [
      structurePalette.unit.light,
      structurePalette.unit.light,
      structurePalette.chapter.light,
      structurePalette.question.light,
      structurePalette.challenge.light,
      structurePalette.question.light,
      structurePalette.sequence.light,
      "#F4EFFF",
      structurePalette.project.light,
    ],
  });

  writeTableSheet(workbook, {
    name: "Source Notes",
    title: "Primary References and Research Inspiration",
    subtitle: "Uploaded curriculum files are the primary reference; public sources are used for inspiration and benchmarking",
    headers: ["Source", "Path or URL", "How it informed this curriculum"],
    rows: sourceNotes,
    widths: [240, 580, 760],
    rowHeight: 82,
    tableName: `${course.shortName}Sources`,
    addTable: false,
    headerFills: [structurePalette.other.dark, structurePalette.reading.dark, structurePalette.output.dark],
    bodyFills: [structurePalette.other.light, structurePalette.reading.light, structurePalette.output.light],
  });

  return { workbook, fileName };
}

const fundamentalsCourse = {
  shortName: "PyFund",
  subject: "python-fundamentals",
  title: "Python Fundamentals: Build Real Programs From Day One",
  subtitle: "Beginner-friendly, problem-centered Python curriculum with hands-on practice in every topic",
  productUnitTitle: "Unit 1: Python Fundamentals",
  target: "Absolute beginners, first-year engineering students, non-CS learners, early bootcamp learners, and professionals who want a practical first programming language.",
  prerequisites: "Basic computer literacy, ability to use files/folders, willingness to practice daily, and basic arithmetic. No prior programming experience required.",
  duration: "72-90 instructional hours, plus 25-35 hours of guided practice and capstone work.",
  pacing: "1 ByteXL product unit containing 16 chapters; recommended 2-3 sessions per chapter with one mini project or checkpoint every 1-2 weeks.",
  pedagogy: "Concept first, code immediately, debug intentionally, reflect briefly, and build a product incrementally.",
  promise: "By the end, students can design, code, debug, test, and present small Python applications that use core data structures, functions, files, and error handling.",
  trainerNote: "Do not rush syntax. Every concept should start from a relatable problem, move to a tiny runnable example, then become part of a mini product.",
  outcomes: [
    "Write Python programs using variables, data types, operators, conditionals, loops, strings, collections, and functions.",
    "Choose appropriate data structures for common beginner problems.",
    "Read and write text, CSV, and JSON files safely.",
    "Use exceptions, tracebacks, print debugging, breakpoints, and simple tests to improve reliability.",
    "Decompose small applications into readable functions with docstrings and type hints.",
    "Build and demo beginner-friendly CLI products with validation and persistent data.",
    "Use AI tools responsibly for explanation and edge-case brainstorming without outsourcing problem solving.",
  ],
  trainerRhythm: "Every chapter follows: why it matters, analogy, prediction activity, live code lab, independent exercise, common bug, reflection, and optional challenge.",
  units: fundamentalsUnits,
  assessment: [
    { component: "Concept quizzes", weight: "15%", evidence: "Short quizzes on syntax, tracebacks, output prediction, and vocabulary.", frequency: "Every chapter", rubric: "Accuracy, reasoning, and ability to explain why an answer is correct." },
    { component: "Code labs", weight: "25%", evidence: "Completed exercises for every topic, checked through output, code review, or notebook submission.", frequency: "Every session", rubric: "Correctness, readability, input handling, and small commits or submissions." },
    { component: "Debugging challenges", weight: "10%", evidence: "Bug reports with root cause, fix, and one prevention note.", frequency: "At least once per unit", rubric: "Traceback reading, hypothesis testing, and clarity of explanation." },
    { component: "Mini projects", weight: "20%", evidence: "Unit projects such as finance calculator, event planner, quiz engine, and expense tracker.", frequency: "Every 1-2 units", rubric: "Working features, data structure choice, validation, and demo quality." },
    { component: "Capstone product", weight: "20%", evidence: "Complete beginner Python product with persistent data, validation, tests, README, and demo.", frequency: "Final 2-3 weeks", rubric: "Problem fit, working software, code organization, edge cases, and presentation." },
    { component: "Reflection and peer review", weight: "10%", evidence: "Code review notes, AI-use citations where applicable, learning journal, and peer feedback.", frequency: "Weekly", rubric: "Specificity, honesty, improvement over time, and constructive feedback." },
  ],
  projects: [
    { stage: "Unit 2", type: "Mini project", project: "Personal finance calculator", outcome: "A tool that calculates monthly savings, needs/wants split, tax, and goals.", concepts: "Variables, numbers, strings, operators, input conversion.", deliverables: "Runnable script, sample inputs/outputs, short README.", milestone: "Define inputs and outputs before coding.", assessment: "Correct calculations, readable names, helpful messages." },
    { stage: "Unit 3", type: "Mini project", project: "Number guessing game with analytics", outcome: "A replayable game with attempts, hints, best score, and invalid input handling.", concepts: "Conditionals, loops, random numbers, state tracking.", deliverables: "Game script, edge-case test notes, demo.", milestone: "Track state across repeated interactions.", assessment: "Loop control, validations, user experience." },
    { stage: "Unit 4", type: "Mini product build", project: "Campus event planner", outcome: "Manage events, registrations, duplicates, and attendee lists.", concepts: "Strings, lists, dictionaries, sets, nested records.", deliverables: "Menu-driven script and sample dataset.", milestone: "Choose structures based on lookup and uniqueness needs.", assessment: "Data structure fit, duplicate handling, search feature." },
    { stage: "Unit 5", type: "Mini project", project: "CLI quiz engine", outcome: "Reusable quiz app with question loading, scoring, and feedback.", concepts: "Functions, decomposition, manual tests.", deliverables: "Functions file, quiz data, sample run.", milestone: "Separate data, logic, and output.", assessment: "Modularity, naming, return values, correctness." },
    { stage: "Unit 6", type: "Mini project", project: "Expense tracker with CSV and JSON", outcome: "Track expenses, categories, settings, and monthly summaries.", concepts: "Files, CSV, JSON, exceptions, validation.", deliverables: "Script, sample CSV/JSON, bug log.", milestone: "Combine persistence and validation.", assessment: "File safety, error messages, summary accuracy." },
    { stage: "Unit 7", type: "Mini project", project: "Command-line study planner", outcome: "Store study tasks, priorities, deadlines, progress, and reminders.", concepts: "Problem-solving patterns, sorting, tests, review.", deliverables: "CLI app, tests, README.", milestone: "Demonstrate correctness through tests.", assessment: "Search/sort logic, tests, maintainable functions." },
    { stage: "Final", type: "Capstone idea", project: "Student success tracker", outcome: "Track attendance, marks, goals, interventions, and export a summary.", concepts: "Full fundamentals stack.", deliverables: "Working app, data files, README, demo script.", milestone: "Capstone milestones 1-3.", assessment: "End-to-end functionality, data persistence, edge cases, presentation." },
    { stage: "Final", type: "Capstone idea", project: "Micro inventory manager", outcome: "Manage products, stock, low-stock alerts, transactions, and reports.", concepts: "Collections, functions, files, exceptions, tests.", deliverables: "Working CLI product and sample inventory.", milestone: "Explain data model and one bug fixed.", assessment: "Data integrity, user flow, code organization." },
    { stage: "Final", type: "Capstone idea", project: "Personal habit and budget coach", outcome: "Combine habits, expenses, reminders, and weekly progress feedback.", concepts: "Strings, collections, files, validation, reports.", deliverables: "App, persistent files, tests, README.", milestone: "Use AI only for edge-case brainstorming and cite it.", assessment: "Student relevance, reliable persistence, polished demo." },
  ],
  mistakes: [
    { topic: "Variables", mistake: "Using unclear names or reusing one variable for unrelated meanings.", symptom: "Code works briefly but becomes difficult to debug.", fix: "Rename variables based on role and lifetime.", debug: "Ask: what real-world value does this variable represent right now?" },
    { topic: "Input conversion", mistake: "Forgetting that `input()` returns text.", symptom: "TypeError during arithmetic or string concatenation surprises.", fix: "Convert at the boundary and validate immediately.", debug: "Print `type(value)` before using it in calculations." },
    { topic: "Conditionals", mistake: "Writing conditions that are always true.", symptom: "Wrong branch runs for many inputs.", fix: "Use explicit comparisons on both sides of `or` and `and`.", debug: "Make a truth table with three sample inputs." },
    { topic: "Loops", mistake: "Not updating the loop variable.", symptom: "Infinite loop or repeated output.", fix: "Identify the value that must change each iteration.", debug: "Print the loop variable at top and bottom of the loop." },
    { topic: "Lists", mistake: "Confusing human position 1 with Python index 0.", symptom: "IndexError or wrong item selected.", fix: "Convert menu choices to index by subtracting 1 after validation.", debug: "Write list indexes above the values on paper." },
    { topic: "Dictionaries", mistake: "Assuming a key exists.", symptom: "KeyError on new or misspelled data.", fix: "Use membership checks, `.get()`, or initialize keys intentionally.", debug: "Print the dictionary keys before lookup." },
    { topic: "Functions", mistake: "Printing inside a function instead of returning a value.", symptom: "Later code receives `None` and fails.", fix: "Return data from logic functions; print only in presentation layer.", debug: "Assign the function result to a variable and print it." },
    { topic: "Files", mistake: "Hard-coding paths that only work on one machine.", symptom: "FileNotFoundError on another computer.", fix: "Use relative paths and project folders.", debug: "Print current working directory and expected path." },
    { topic: "Exceptions", mistake: "Catching every exception with a bare except.", symptom: "Real bugs disappear behind generic messages.", fix: "Catch specific exceptions and log or re-raise unexpected ones.", debug: "Temporarily remove the broad except to see the real traceback." },
    { topic: "Testing", mistake: "Testing only happy paths.", symptom: "Program fails on empty, invalid, or boundary input.", fix: "Include normal, boundary, invalid, and missing-data cases.", debug: "Ask: what is the smallest, largest, empty, and weird input?" },
  ],
  useCases: [
    { topic: "Variables and expressions", industry: "Finance", useCase: "EMI, savings, tax, discount, and payroll calculations.", task: "Build a calculator with clear inputs and formatted outputs.", interview: "Explain type conversion and rounding choices." },
    { topic: "Conditionals", industry: "EdTech", useCase: "Eligibility, grading, scholarship, and progression rules.", task: "Write a rule engine for pass, warning, and intervention categories.", interview: "Explain how you handle overlapping conditions." },
    { topic: "Loops", industry: "Operations", useCase: "Process repeated orders, attendance rows, or ticket queues.", task: "Summarize a batch of transactions and stop on invalid records.", interview: "Explain sentinel loops and loop termination." },
    { topic: "Strings", industry: "Customer support", useCase: "Clean survey responses, extract tags, detect repeated complaint words.", task: "Write a text cleaner and keyword counter.", interview: "Explain slicing, methods, and immutability." },
    { topic: "Lists and dictionaries", industry: "Retail", useCase: "Inventory, carts, contacts, menus, and records.", task: "Build inventory lookup and low-stock reporting.", interview: "Choose between list, dictionary, tuple, and set." },
    { topic: "Functions", industry: "Any software team", useCase: "Reusable validation, formatting, calculation, and reporting utilities.", task: "Refactor a script into testable functions.", interview: "Explain parameters, returns, and scope." },
    { topic: "Files", industry: "Admin automation", useCase: "Read CSV exports, write reports, save user settings.", task: "Create a CSV/JSON-backed tracker.", interview: "Explain safe file handling and missing file recovery." },
    { topic: "Debugging and tests", industry: "Quality engineering", useCase: "Find root causes and protect fixes.", task: "Turn a bug into a failing test and then pass it.", interview: "Describe a bug you fixed and how you prevented it." },
  ],
  challenges: [
    { level: "Stretch 1", theme: "CLI polish", challenge: "Add menus, input retry loops, and friendly help text to every mini project.", success: "A new user can run the app without trainer help.", support: "Provide starter menu template." },
    { level: "Stretch 2", theme: "Testing", challenge: "Convert manual test tables into assert-based test files.", success: "At least 10 meaningful tests pass from the terminal.", support: "Give examples of normal, boundary, and invalid cases." },
    { level: "Stretch 3", theme: "Data persistence", challenge: "Add CSV or JSON persistence to an earlier project.", success: "Data survives closing and reopening the app.", support: "Provide file schema examples." },
    { level: "Stretch 4", theme: "Code review", challenge: "Refactor a peer's script for naming, duplication, and function boundaries.", success: "Behavior stays the same and readability improves.", support: "Use the review checklist." },
    { level: "Stretch 5", theme: "Portfolio", challenge: "Publish a cleaned capstone repository with README, sample data, and demo transcript.", success: "A reviewer can install/run or understand the project.", support: "Provide README template and demo checklist." },
  ],
};

const advancedCourse = {
  shortName: "AdvPy",
  subject: "advanced-python-concepts",
  title: "Advanced Python Concepts: Engineering Python for Production",
  subtitle: "A rigorous Python software engineering curriculum for robust, testable, maintainable applications",
  productUnitTitle: "Unit 2: Advanced Python Concepts",
  target: "Learners who can already write Python scripts with functions, collections, files, and basic debugging, and now need professional engineering depth.",
  prerequisites: "Python fundamentals, functions, collections, file handling, basic CLI comfort, and willingness to use terminal, Git, and tests.",
  duration: "84-110 instructional hours, plus 40-55 hours of labs, project sprints, and capstone engineering work.",
  pacing: "1 ByteXL product unit containing 16 chapters; recommended two labs per chapter and one engineering project sprint every two chapters.",
  pedagogy: "Architecture through practice: design small, test early, observe behavior, refactor intentionally, and ship usable tools.",
  promise: "By the end, students can build production-minded Python applications using OOP, packages, decorators, iterators, generators, context managers, APIs, testing, logging, databases, performance profiling, clean code, and design patterns.",
  trainerNote: "Advanced does not mean obscure. Every feature must answer: how does this make code more reusable, reliable, scalable, testable, or maintainable?",
  outcomes: [
    "Structure Python projects into packages with clean imports, CLI entry points, configuration, and documentation.",
    "Design object models using encapsulation, composition, polymorphism, dataclasses, magic methods, and protocols.",
    "Use decorators, iterators, generators, and context managers to create Pythonic abstractions.",
    "Build file pipelines, regex extractors, and resilient API clients.",
    "Write meaningful tests with pytest, fixtures, parametrization, mocking, and regression workflows.",
    "Add logging, debugging, profiling, type hints, linting, and quality gates.",
    "Connect to SQLite databases safely with schemas, parameterized queries, transactions, and constraints.",
    "Optimize only after measuring, use concurrency for appropriate I/O workloads, and package code for reuse.",
    "Apply clean code, layered architecture, and design patterns without over-engineering.",
  ],
  trainerRhythm: "Every chapter follows: professional scenario, design sketch, guided implementation, test gate, logging/debugging gate, refactor review, and product demo.",
  units: advancedUnits,
  assessment: [
    { component: "Advanced concept checks", weight: "10%", evidence: "Short quizzes on OOP, imports, decorators, generators, APIs, SQL, testing, and architecture.", frequency: "Every chapter", rubric: "Precise vocabulary, trade-off reasoning, and ability to read unfamiliar code." },
    { component: "Code labs", weight: "20%", evidence: "Hands-on labs for each advanced topic with runnable code and edge cases.", frequency: "Every session", rubric: "Correctness, idiomatic Python, tests, and clean commits." },
    { component: "Testing and reliability gates", weight: "15%", evidence: "pytest suites, mocks, logging output, error handling, and regression tests.", frequency: "Every project sprint", rubric: "Coverage of behavior, edge cases, failure modes, and maintainable test design." },
    { component: "Engineering mini products", weight: "25%", evidence: "Reusable package, OOP model, streaming analyzer, API collector, tested CLI, CRM, API monitor, plugin app.", frequency: "Every 1-2 units", rubric: "Architecture, separation of concerns, maintainability, documentation, and demo quality." },
    { component: "Code review and design review", weight: "10%", evidence: "Design docs, review comments, refactoring notes, and trade-off explanations.", frequency: "Biweekly", rubric: "Specific reasoning, simplicity, correctness, and ability to improve without breaking behavior." },
    { component: "Advanced capstone", weight: "20%", evidence: "Production-minded Python application with package structure, tests, logs, database/API/file layer, performance notes, and demo.", frequency: "Final 3-4 weeks", rubric: "End-to-end reliability, architecture, test strategy, failure handling, and professional presentation." },
  ],
  projects: [
    { stage: "Unit 1", type: "Mini product build", project: "Reusable text utility package", outcome: "Importable and runnable package with CLI flags and README.", concepts: "venv, modules, packages, imports, argparse, Git.", deliverables: "Package folder, CLI script, README, sample files.", milestone: "Runnable, importable, documented.", assessment: "Clean imports, CLI behavior, project layout." },
    { stage: "Unit 2", type: "Mini product build", project: "Training center management model", outcome: "OOP domain model for students, batches, attendance, and reports.", concepts: "Classes, dataclasses, properties, composition, polymorphism.", deliverables: "Domain classes, demo script, tests for invariants.", milestone: "Domain model before UI/storage.", assessment: "Encapsulation, invariants, object relationships." },
    { stage: "Unit 3", type: "Mini product build", project: "Streaming log analyzer", outcome: "Generator-powered analyzer with timing decorator and context manager.", concepts: "Decorators, iterators, generators, context managers.", deliverables: "Analyzer package, sample logs, report output.", milestone: "Lazy processing for growing data.", assessment: "Memory-aware design, clean abstractions." },
    { stage: "Unit 4", type: "Mini product build", project: "API-powered dashboard data collector", outcome: "API client that fetches, validates, stores, and summarizes data.", concepts: "Regex, requests, JSON, config, retries, file pipelines.", deliverables: "API module, parser, CSV/JSON outputs, tests with mock data.", milestone: "Separate API, parsing, storage, reporting.", assessment: "Failure handling, clean boundaries, data quality." },
    { stage: "Unit 5", type: "Mini product build", project: "Tested CLI toolkit", outcome: "CLI utility with pytest suite, logging, type hints, and docs.", concepts: "pytest, fixtures, mocking, logging, profiling, linting.", deliverables: "CLI app, tests, log samples, profiling note.", milestone: "Quality gates are part of product.", assessment: "Reliability, tests, logs, maintainable code." },
    { stage: "Unit 6", type: "Mini product build", project: "Personal CRM with SQLite", outcome: "CRUD app for contacts, follow-ups, tags, and search.", concepts: "SQLite, DB-API, transactions, constraints, safe queries.", deliverables: "Database schema, seed data, app, tests.", milestone: "Schema is a design artifact.", assessment: "Data integrity, SQL safety, transaction behavior." },
    { stage: "Unit 7", type: "Mini product build", project: "Concurrent API monitor", outcome: "Monitor endpoints concurrently, cache results, log failures, and write status reports.", concepts: "concurrent.futures, asyncio mindset, caching, packaging, secrets.", deliverables: "Monitor app, config sample, logs, package install steps.", milestone: "Production readiness includes failure modes.", assessment: "Concurrency fit, config safety, observability." },
    { stage: "Unit 8", type: "Mini product build", project: "Plugin-based automation app", outcome: "Extensible app with processors or notification channels as plugins.", concepts: "Clean code, layered architecture, Factory, Strategy, Adapter, Observer.", deliverables: "Core app, two plugins, tests, design note.", milestone: "Extension points intentional and tested.", assessment: "Pattern fit, simplicity, testability." },
    { stage: "Final", type: "Capstone idea", project: "Customer support triage system", outcome: "Ingest tickets, classify with rules, store in database, expose CLI reports, log decisions.", concepts: "OOP, regex, files/API, SQLite, tests, logging, patterns.", deliverables: "Packaged app, schema, tests, docs, demo.", milestone: "Vertical slice before full feature set.", assessment: "Architecture, reliability, explainability." },
    { stage: "Final", type: "Capstone idea", project: "Learning analytics backend toolkit", outcome: "Import course data, compute progress, detect risks, export reports, and support plugins.", concepts: "Packages, DB, generators, testing, design patterns.", deliverables: "Toolkit package, CLI, sample data, tests.", milestone: "Performance and reliability gate.", assessment: "Data design, clean APIs, tests, maintainability." },
    { stage: "Final", type: "Capstone idea", project: "API data quality monitor", outcome: "Poll APIs, validate records, cache results, persist incidents, and produce operational reports.", concepts: "APIs, concurrency, caching, SQLite, logging, packaging.", deliverables: "App, config template, logs, docs, demo.", milestone: "Production-ready demo and failure-mode explanation.", assessment: "Resilience, observability, safe config, packaging." },
  ],
  mistakes: [
    { topic: "Virtual environments", mistake: "Installing dependencies globally and assuming every machine has them.", symptom: "Project fails on a fresh setup.", fix: "Create venv, document dependencies, and test clean installation.", debug: "Recreate environment from scratch and run tests." },
    { topic: "Imports", mistake: "Circular imports or shadowing standard library modules.", symptom: "ImportError or surprising module attributes.", fix: "Move shared logic to lower-level modules and rename conflicting files.", debug: "Print module `__file__` and draw import direction." },
    { topic: "OOP", mistake: "Using inheritance for every relationship.", symptom: "Rigid classes and duplicated override logic.", fix: "Prefer composition when objects have parts or collaborators.", debug: "Ask: is this an is-a relationship or has-a relationship?" },
    { topic: "Dataclasses", mistake: "Skipping validation for fields that must obey rules.", symptom: "Invalid objects exist and fail later.", fix: "Use `__post_init__`, properties, or factory functions.", debug: "Write tests for invalid construction." },
    { topic: "Decorators", mistake: "Not preserving metadata with `functools.wraps`.", symptom: "Names, docs, and test reports become confusing.", fix: "Wrap inner function with `@wraps(func)`.", debug: "Print `__name__` before and after decorating." },
    { topic: "Generators", mistake: "Expecting a generator to restart after being consumed.", symptom: "Second loop produces no output.", fix: "Create a new generator or design a re-iterable object.", debug: "Convert a tiny generator to a list once to observe consumption." },
    { topic: "Context managers", mistake: "Opening resources without guaranteed cleanup.", symptom: "Locked files, leaked handles, partial writes.", fix: "Use `with` or contextlib.", debug: "Force an exception and verify cleanup still happens." },
    { topic: "APIs", mistake: "Assuming every HTTP response is successful JSON.", symptom: "JSONDecodeError, KeyError, silent wrong results.", fix: "Check status codes, content type, timeouts, and expected keys.", debug: "Mock 200, 404, 429, timeout, and malformed JSON." },
    { topic: "Testing", mistake: "Testing implementation details instead of behavior.", symptom: "Tests break during refactor even when behavior is correct.", fix: "Write tests around public inputs/outputs and observable effects.", debug: "Refactor code and see which tests should not have failed." },
    { topic: "Logging", mistake: "Logging secrets or too much noisy detail.", symptom: "Security risk and unreadable logs.", fix: "Log events, IDs, and states; never credentials or raw sensitive data.", debug: "Review logs as if they were shared with support staff." },
    { topic: "SQL", mistake: "Building SQL with string formatting.", symptom: "SQL injection risk and broken quotes.", fix: "Use parameterized queries.", debug: "Try an input containing quotes and confirm the query stays safe." },
    { topic: "Performance", mistake: "Optimizing before measuring.", symptom: "Complex code with no proven benefit.", fix: "Profile first, change one bottleneck, measure again.", debug: "Record before/after timings in a short note." },
    { topic: "Patterns", mistake: "Forcing design patterns into simple problems.", symptom: "Too many classes and hard-to-follow flow.", fix: "Use patterns only when they remove real duplication or coupling.", debug: "Delete the pattern mentally and compare complexity." },
  ],
  useCases: [
    { topic: "Packages and CLI", industry: "Internal tools", useCase: "Reusable scripts distributed across a team.", task: "Build an importable CLI utility with documented commands.", interview: "Explain project layout and dependency isolation." },
    { topic: "OOP and dataclasses", industry: "EdTech/SaaS", useCase: "Domain models for users, subscriptions, progress, and rules.", task: "Model entities with invariants and tested behavior.", interview: "Explain composition vs inheritance with examples." },
    { topic: "Decorators", industry: "Web frameworks", useCase: "Authentication, timing, caching, retry, route registration.", task: "Write and test timing and retry decorators.", interview: "Explain closures and wrapper behavior." },
    { topic: "Generators", industry: "Data engineering", useCase: "Streaming logs, CSV rows, events, and large exports.", task: "Build a memory-aware record pipeline.", interview: "Explain lazy evaluation and one-pass iteration." },
    { topic: "Context managers", industry: "Infrastructure", useCase: "Safe file handling, locks, database sessions, temporary resources.", task: "Create safe writer and timer context managers.", interview: "Explain cleanup guarantees." },
    { topic: "Regex and APIs", industry: "Automation", useCase: "Extract identifiers and connect systems over HTTP.", task: "Build resilient API collector with validation.", interview: "Explain status codes, retries, and regex greediness." },
    { topic: "Testing and logging", industry: "Software engineering", useCase: "Prevent regressions and diagnose production issues.", task: "Add pytest, mocks, and structured logs to a CLI app.", interview: "Describe test pyramid basics and logging levels." },
    { topic: "Databases", industry: "Business systems", useCase: "CRUD tools, reporting, audit trails, and search.", task: "Build SQLite-backed CRM with safe queries.", interview: "Explain transactions and SQL injection prevention." },
    { topic: "Performance and concurrency", industry: "Operations monitoring", useCase: "Process large files or call many endpoints efficiently.", task: "Measure bottlenecks and add appropriate concurrency.", interview: "Explain I/O-bound vs CPU-bound work." },
    { topic: "Design patterns", industry: "Platform engineering", useCase: "Extensible plugin systems and interchangeable strategies.", task: "Build plugin-based automation with tests.", interview: "Explain Strategy, Factory, and Adapter trade-offs." },
  ],
  challenges: [
    { level: "Stretch 1", theme: "Typing", challenge: "Add type hints to a package and run a static type checker mindset review.", success: "Public functions have meaningful annotations and no obvious type confusion.", support: "Provide before/after examples." },
    { level: "Stretch 2", theme: "CI thinking", challenge: "Create a local quality script that runs tests, linting, and formatting checks.", success: "One command verifies quality gates.", support: "Provide command checklist; CI platform optional." },
    { level: "Stretch 3", theme: "Async", challenge: "Rewrite a sequential API polling lab with asyncio and compare complexity.", success: "Students explain whether async improved the design.", support: "Provide fake API delays to avoid service dependency." },
    { level: "Stretch 4", theme: "Architecture", challenge: "Add a second storage backend to a project without changing the service layer.", success: "Tests pass against both backends.", support: "Use repository interface examples." },
    { level: "Stretch 5", theme: "Packaging", challenge: "Build and install a wheel in a fresh environment.", success: "CLI entry point works after installation.", support: "Provide pyproject template." },
    { level: "Stretch 6", theme: "Observability", challenge: "Add structured logs and a failure dashboard CSV to the capstone.", success: "A reviewer can understand failures without reading source code.", support: "Provide log field checklist." },
  ],
};

async function exportWorkbook(course, fileName) {
  const { workbook } = createWorkbook(course, fileName);

  const checks = await workbook.inspect({
    kind: "match",
    searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
    options: { useRegex: true, maxResults: 50 },
    summary: "formula error scan",
  });
  console.log(`${fileName} formula scan`);
  console.log(checks.ndjson || "No formula errors found.");

  const overview = await workbook.inspect({
    kind: "table",
    range: "Curriculum Table!A5:D14",
    include: "values",
    tableMaxRows: 10,
    tableMaxCols: 4,
    maxChars: 6000,
  });
  console.log(`${fileName} curriculum preview`);
  console.log(overview.ndjson);

  const previewDir = `${outputDir}/previews`;
  await fs.mkdir(previewDir, { recursive: true });
  for (const sheetName of [
    "Overview",
    "Structure Legend",
    "Curriculum Table",
    "ByteXL Build Map",
    "Topic Experience Map",
    "Projects Capstone",
    "Assessment Strategy",
    "Teaching Approach",
    "Mistakes Debug Bank",
    "Use Cases Interviews",
    "Challenge Track",
    "Question Blueprint",
    "Source Notes",
  ]) {
    const preview = await workbook.render({ sheetName, autoCrop: "all", scale: 1, format: "png" });
    const bytes = new Uint8Array(await preview.arrayBuffer());
    await fs.writeFile(`${previewDir}/${course.shortName}_${slug(sheetName)}.png`, bytes);
    console.log(`${course.shortName} rendered ${sheetName}: ${bytes.length} bytes`);
  }

  await fs.mkdir(outputDir, { recursive: true });
  const output = await SpreadsheetFile.exportXlsx(workbook);
  const outPath = `${outputDir}/${fileName}`;
  await output.save(outPath);
  console.log(`Saved ${outPath}`);
}

await exportWorkbook(fundamentalsCourse, "Python Fundamentals Curriculum - ByteXL Unit 1.xlsx");
await exportWorkbook(advancedCourse, "Advanced Python Concepts Curriculum - ByteXL Unit 2.xlsx");
