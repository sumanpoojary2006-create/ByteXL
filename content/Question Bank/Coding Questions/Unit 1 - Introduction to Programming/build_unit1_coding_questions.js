// Generates "Unit 1 - Introduction to Programming - Coding Questions.docx"
// Template follows: coding question pattern fpr sample.docx
// Scope lock: Unit 1 only teaches variables, input(), and print() -- no operators,
// casting, conditionals, or loops. Every solution below uses only those three things.

const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  ShadingType, BorderStyle,
} = require("docx");

const CODE_FONT = "Courier New";
const CODE_SHADE = "F2F2F2";

function codeBlock(lines) {
  const children = [];
  lines.forEach((line, i) => {
    if (i > 0) children.push(new TextRun({ break: 1, text: line, font: CODE_FONT, size: 20 }));
    else children.push(new TextRun({ text: line, font: CODE_FONT, size: 20 }));
  });
  return new Paragraph({
    shading: { fill: CODE_SHADE, type: ShadingType.CLEAR },
    spacing: { before: 60, after: 120 },
    children,
  });
}

function label(text) {
  return new Paragraph({
    spacing: { before: 160, after: 60 },
    children: [new TextRun({ text, bold: true })],
  });
}

function bulletPara(text) {
  return new Paragraph({
    spacing: { after: 40 },
    children: [new TextRun({ text: "•  " + text })],
  });
}

function bodyPara(text) {
  return new Paragraph({ spacing: { after: 80 }, children: [new TextRun({ text })] });
}

// ---- helpers for the two recurring output shapes -------------------------

// Sentence shape (Easy): tokens are static words or {{var}} placeholders.
// join with single spaces, exactly like print(a, b, c, ...) does.
function sentenceLine(tokens) {
  return tokens.join(" ");
}

// Label-line shape (Medium / Hard): "Label: value" per field, optional header/footer.
function labelLines(fields, values, header, footer) {
  const lines = [];
  if (header) lines.push(header);
  fields.forEach((f, i) => lines.push(`${f}: ${values[i]}`));
  if (footer) lines.push(footer);
  return lines;
}

function pySentence(parts) {
  // parts: array of either {var: 'name'} or {lit: 'some words'}
  const args = parts.map((p) => (p.lit !== undefined ? `"${p.lit}"` : p.var));
  return `print(${args.join(", ")})`;
}

function pyLabelLines(fields, varNames, header, footer) {
  const lines = [];
  varNames.forEach((v) => lines.push(`${v} = input()`));
  lines.push("");
  if (header) lines.push(`print("${header}")`);
  fields.forEach((f, i) => lines.push(`print("${f}:", ${varNames[i]})`));
  if (footer) lines.push(`print("${footer}")`);
  return lines;
}

// ---- question data ---------------------------------------------------------

function easyQ(n, title, fields, varNames, parts, examples) {
  // parts uses {{0}}, {{1}}... referring to varNames index, for the placeholder template
  const placeholderParts = parts.map((p) =>
    p.var !== undefined ? `<${fields[p.var]}>` : p.lit
  );
  const outputTemplate = sentenceLine(placeholderParts);

  const inputLines = fields.map((f, i) => `- Line ${i + 1}: ${f}`);
  const solution = [
    ...varNames.map((v) => `${v} = input()`),
    "",
    pySentence(parts.map((p) => (p.var !== undefined ? { var: varNames[p.var] } : p))),
  ];

  const testCases = examples.map((vals) => {
    const tokens = parts.map((p) => (p.var !== undefined ? vals[p.var] : p.lit));
    return { input: vals, output: [sentenceLine(tokens)] };
  });

  return {
    n, difficulty: "Easy", title,
    scenario: null, // filled per-question below via override
    fields, inputLines, outputTemplate, footerNote: null,
    constraints: [
      "Every input value is a non-empty single line of text.",
      "No input value exceeds 40 characters.",
      "Input values may contain letters, digits, and spaces only.",
    ],
    testCases, solution,
  };
}

function structuredQ(n, difficulty, title, fields, varNames, header, footer, examples) {
  const placeholderValues = fields.map((f) => `<${f.toLowerCase().replace(/ /g, "_")}>`);
  const outputLines = labelLines(fields, placeholderValues, header, footer);
  const inputLines = fields.map((f, i) => `- Line ${i + 1}: ${f}`);
  const solution = pyLabelLines(fields, varNames, header, footer);

  const testCases = examples.map((vals) => ({
    input: vals,
    output: labelLines(fields, vals, header, footer),
  }));

  return {
    n, difficulty, title, fields, inputLines, outputLines, header, footer,
    constraints: [
      "Every input value is a non-empty single line of text.",
      "No input value exceeds 40 characters.",
      "ID-like fields (roll numbers, token numbers, dates, etc.) are read and printed as plain text, never as numbers.",
    ],
    testCases, solution,
  };
}

const Q = [];

// ---------------------------- EASY (sentence style) -------------------------

Q.push({ ...easyQ(0, "Canteen Token Greeting", ["Name"], ["name"],
  [{ lit: "Hello" }, { var: 0 }, { lit: "your token number will be called shortly" }],
  [["Asha"], ["Kabir"], ["Meera"]]),
  scenarioText: "The college canteen app greets every student by name the moment they place an order. Write a program that reads a student's name and prints a short greeting confirming that their token number will be called shortly." });

Q.push({ ...easyQ(0, "Birthday Wish", ["Name"], ["name"],
  [{ lit: "Happy Birthday" }, { var: 0 }, { lit: "have a great day" }],
  [["Rohan"], ["Priya"], ["Sneha"]]),
  scenarioText: "A college group chat has a small bot that wishes a student on their birthday. Write a program that reads a student's name and prints a short birthday wish." });

Q.push({ ...easyQ(0, "Library Borrow Confirmation", ["Name", "Book Title"], ["name", "book"],
  [{ var: 0 }, { lit: "has borrowed" }, { var: 1 }, { lit: "from the library" }],
  [["Arjun", "Clean Code"], ["Divya", "Python Crash Course"], ["Vikram", "Atomic Habits"]]),
  scenarioText: "The college library logs every book that gets borrowed. Write a program that reads a student's name and the title of the book they borrowed, then prints a confirmation line." });

Q.push({ ...easyQ(0, "Club Membership Confirmation", ["Name", "Club Name"], ["name", "club"],
  [{ var: 0 }, { lit: "is now a member of the" }, { var: 1 }, { lit: "club" }],
  [["Asha", "Photography"], ["Kabir", "Coding"], ["Meera", "Dance"]]),
  scenarioText: "Students sign up for college clubs at the start of every semester. Write a program that reads a student's name and the club they joined, then prints a confirmation line." });

// ---------------------------- MEDIUM (label-line, no header/footer) ---------

Q.push({ ...structuredQ(0, "Medium", "Mini Student ID Card",
  ["Name", "Roll No", "Department"], ["name", "roll_no", "department"], null, null,
  [["Asha Verma", "21CS104", "Computer Science"],
   ["Kabir Khan", "21EC078", "Electronics"],
   ["Meera Iyer", "21ME032", "Mechanical"]]),
  scenarioText: "The college admin office wants a quick preview of a student's ID card before printing it. Write a program that reads a student's name, roll number, and department, then prints them as three clearly labelled lines." });

Q.push({ ...structuredQ(0, "Medium", "Canteen Receipt Header",
  ["Item", "Token No", "Counter"], ["item", "token_no", "counter"], null, null,
  [["Veg Sandwich", "T-104", "2"], ["Cold Coffee", "T-087", "1"], ["Masala Dosa", "T-156", "3"]]),
  scenarioText: "The canteen's billing screen shows a short header before the full receipt prints. Write a program that reads the item name, token number, and counter number, then prints them as three labelled lines." });

Q.push({ ...structuredQ(0, "Medium", "Hostel Mess Card",
  ["Name", "Room No", "Mess Plan"], ["name", "room_no", "mess_plan"], null, null,
  [["Rohan Patil", "B-204", "Veg"], ["Priya Nair", "G-112", "Non-Veg"], ["Sneha Rao", "C-318", "Veg"]]),
  scenarioText: "The hostel mess counter scans a student's mess card before serving food. Write a program that reads a student's name, room number, and mess plan, then prints them as three labelled lines." });

Q.push({ ...structuredQ(0, "Medium", "Event Registration Confirmation",
  ["Name", "Event", "Day"], ["name", "event", "day"], null, null,
  [["Arjun Mehta", "Hackathon", "Day 1"], ["Divya Shah", "Quiz Night", "Day 2"], ["Vikram Joshi", "Robotics Demo", "Day 1"]]),
  scenarioText: "The fest registration desk prints a small confirmation slip for every student who signs up for an event. Write a program that reads a student's name, the event, and the day, then prints them as three labelled lines." });

// ---------------------------- HARD (label-line, header + footer) -----------

Q.push({ ...structuredQ(0, "Hard", "Exam Hall Ticket",
  ["Name", "Roll No", "Course", "Semester", "Exam Center", "Exam Date"],
  ["name", "roll_no", "course", "semester", "exam_center", "exam_date"],
  "EXAM HALL TICKET", "Carry a valid ID proof to the exam center",
  [["Asha Verma", "21CS104", "B.Tech CSE", "Semester 3", "Block A, Room 12", "12 Dec 2026"],
   ["Kabir Khan", "21EC078", "B.Tech ECE", "Semester 3", "Block B, Room 4", "12 Dec 2026"],
   ["Meera Iyer", "21ME032", "B.Tech Mech", "Semester 3", "Block A, Room 9", "13 Dec 2026"]]),
  scenarioText: "The examination cell generates a hall ticket for every student before the semester exams. Write a program that reads a student's name, roll number, course, semester, exam center, and exam date, then prints the complete hall ticket." });

Q.push({ ...structuredQ(0, "Hard", "Hostel Room Allotment Letter",
  ["Name", "Room No", "Block", "Warden", "Move-in Date"],
  ["name", "room_no", "block", "warden", "move_in_date"],
  "HOSTEL ALLOTMENT LETTER", "Report to the warden on the move-in date",
  [["Rohan Patil", "G-112", "Ganga Block", "Mr. Suresh Iyer", "1 Jul 2026"],
   ["Priya Nair", "C-318", "Cauvery Block", "Mrs. Anita Rao", "2 Jul 2026"],
   ["Sneha Rao", "B-204", "Brahmaputra Block", "Mr. Suresh Iyer", "1 Jul 2026"]]),
  scenarioText: "The hostel office sends every new student an allotment letter before the semester begins. Write a program that reads a student's name, room number, block, warden's name, and move-in date, then prints the complete letter." });

// extra set continues...
Q.push({ ...easyQ(0, "Movie Ticket Greeting", ["Name", "Movie"], ["name", "movie"],
  [{ lit: "Enjoy the movie" }, { var: 0 }, { lit: "your ticket for" }, { var: 1 }, { lit: "is confirmed" }],
  [["Asha", "Interstellar"], ["Kabir", "3 Idiots"], ["Meera", "RRR"]]),
  scenarioText: "The campus movie-night app confirms every ticket booking with a short message. Write a program that reads a student's name and the movie they booked, then prints a confirmation line." });

Q.push({ ...easyQ(0, "Gym Check-in", ["Name"], ["name"],
  [{ lit: "Welcome to the gym" }, { var: 0 }, { lit: "check-in time recorded" }],
  [["Rohan"], ["Priya"], ["Vikram"]]),
  scenarioText: "The campus gym logs every student who checks in at the entrance. Write a program that reads a student's name and prints a short check-in confirmation." });

Q.push({ ...easyQ(0, "WhatsApp Status Update", ["Name", "Status"], ["name", "status"],
  [{ var: 0 }, { lit: "updated their status to" }, { var: 1 }],
  [["Asha", "Exam week, send help"], ["Kabir", "Fest mode on"], ["Meera", "Coffee and code"]]),
  scenarioText: "A group chat bot announces every status update a student posts. Write a program that reads a student's name and their new status text, then prints an announcement line." });

Q.push({ ...easyQ(0, "Roommate Introduction", ["Name 1", "Name 2"], ["name1", "name2"],
  [{ var: 0 }, { lit: "and" }, { var: 1 }, { lit: "are now roommates" }],
  [["Arjun", "Vikram"], ["Divya", "Sneha"], ["Asha", "Meera"]]),
  scenarioText: "The hostel allotment system announces every new roommate pairing. Write a program that reads two students' names and prints a line announcing that they are now roommates." });

Q.push({ ...easyQ(0, "Class Rep Announcement", ["Name", "Message"], ["name", "message"],
  [{ lit: "Class Rep" }, { var: 0 }, { lit: "says" }, { var: 1 }],
  [["Kabir", "Submit assignments by Friday"], ["Meera", "Class moved to Room 204"], ["Asha", "Guest lecture at 2 PM"]]),
  scenarioText: "The class representative posts short announcements to the class group. Write a program that reads the class rep's name and the announcement message, then prints them as a single announcement line." });

Q.push({ ...easyQ(0, "Login Welcome Message", ["Name"], ["name"],
  [{ lit: "Welcome back" }, { var: 0 }, { lit: "you have successfully logged in" }],
  [["Rohan"], ["Divya"], ["Vikram"]]),
  scenarioText: "The student portal greets every student right after they log in. Write a program that reads a student's name and prints a short welcome-back message." });

Q.push({ ...structuredQ(0, "Medium", "Library Card",
  ["Name", "Book", "Due Date"], ["name", "book", "due_date"], null, null,
  [["Asha Verma", "Clean Code", "20 Jul 2026"], ["Kabir Khan", "Atomic Habits", "22 Jul 2026"], ["Meera Iyer", "Deep Work", "25 Jul 2026"]]),
  scenarioText: "The library counter prints a small slip every time a book is issued. Write a program that reads a student's name, the book title, and the due date, then prints them as three labelled lines." });

Q.push({ ...structuredQ(0, "Medium", "Cab Booking Confirmation",
  ["Passenger", "Pickup", "Drop"], ["passenger", "pickup", "drop"], null, null,
  [["Rohan Patil", "Hostel Gate", "Railway Station"], ["Priya Nair", "Main Block", "City Mall"], ["Sneha Rao", "Library", "Airport"]]),
  scenarioText: "The campus cab-sharing app confirms every booking with a short slip. Write a program that reads the passenger's name, the pickup point, and the drop point, then prints them as three labelled lines." });

Q.push({ ...structuredQ(0, "Medium", "Online Order Confirmation",
  ["Item", "Quantity", "Deliver To"], ["item", "quantity", "deliver_to"], null, null,
  [["Notebook Set", "2", "Hostel Block B, Room 204"], ["Phone Charger", "1", "Hostel Block C, Room 118"], ["Sticky Notes", "3", "Hostel Block A, Room 305"]]),
  scenarioText: "A campus stationery app confirms every order placed by a student. Write a program that reads the item name, quantity, and delivery address, then prints them as three labelled lines. Quantity is read and printed as plain text." });

Q.push({ ...structuredQ(0, "Medium", "Class Timetable Slot",
  ["Subject", "Time", "Room"], ["subject", "time", "room"], null, null,
  [["Data Structures", "10:00 AM", "204"], ["Operating Systems", "12:00 PM", "118"], ["Python Lab", "2:00 PM", "Lab 3"]]),
  scenarioText: "The timetable app shows the next class on a student's dashboard. Write a program that reads the subject name, time, and room, then prints them as three labelled lines." });

Q.push({ ...structuredQ(0, "Medium", "Hostel Visitor Pass",
  ["Visitor Name", "Student Name", "Room No", "Valid Until"],
  ["visitor_name", "student_name", "room_no", "valid_until"], null, null,
  [["Mr. Verma", "Asha Verma", "G-112", "6:00 PM"], ["Mrs. Khan", "Kabir Khan", "B-204", "7:00 PM"], ["Mr. Iyer", "Meera Iyer", "C-318", "6:30 PM"]]),
  scenarioText: "The hostel gate issues a short visitor pass for anyone visiting a student. Write a program that reads the visitor's name, the student's name, the room number, and the valid-until time, then prints them as four labelled lines." });

Q.push({ ...structuredQ(0, "Medium", "Internship Confirmation (Mini)",
  ["Name", "Company", "Role", "Start Date"], ["name", "company", "role", "start_date"], null, null,
  [["Asha Verma", "BrightTech", "Data Analyst Intern", "1 Aug 2026"], ["Kabir Khan", "NimbusSoft", "Backend Intern", "5 Aug 2026"], ["Meera Iyer", "Craftly", "Marketing Intern", "10 Aug 2026"]]),
  scenarioText: "The placement cell sends a quick confirmation note whenever a student is placed for an internship. Write a program that reads a student's name, the company, the role, and the start date, then prints them as four labelled lines." });

Q.push({ ...structuredQ(0, "Hard", "Certificate of Participation",
  ["Name", "Event", "Position", "College", "Date"],
  ["name", "event", "position", "college", "date"],
  "CERTIFICATE OF PARTICIPATION", "Issued by the Student Activities Committee",
  [["Arjun Mehta", "Hackathon 2026", "Winner", "ABC Institute of Technology", "15 Mar 2026"],
   ["Divya Shah", "Quiz Night", "Runner-up", "ABC Institute of Technology", "16 Mar 2026"],
   ["Vikram Joshi", "Robotics Demo", "Participant", "ABC Institute of Technology", "17 Mar 2026"]]),
  scenarioText: "The Student Activities Committee prints a certificate for every fest participant. Write a program that reads a student's name, the event, their position, the college name, and the date, then prints the complete certificate." });

Q.push({ ...structuredQ(0, "Hard", "College ID Card",
  ["Name", "Roll No", "Department", "Year", "Blood Group"],
  ["name", "roll_no", "department", "year", "blood_group"],
  "COLLEGE ID CARD", "This card is non-transferable",
  [["Rohan Patil", "21CS104", "Computer Science", "2nd Year", "B+"],
   ["Priya Nair", "21EC078", "Electronics", "2nd Year", "O+"],
   ["Sneha Rao", "21ME032", "Mechanical", "3rd Year", "A+"]]),
  scenarioText: "The admin office issues a college ID card to every student at the start of the year. Write a program that reads a student's name, roll number, department, year, and blood group, then prints the complete ID card." });

Q.push({ ...structuredQ(0, "Hard", "Canteen Bill Slip",
  ["Name", "Item", "Token No", "Counter", "Time"],
  ["name", "item", "token_no", "counter", "time"],
  "CANTEEN BILL", "Thank you, visit again",
  [["Asha Verma", "Veg Thali", "T-204", "2", "1:15 PM"],
   ["Kabir Khan", "Cold Coffee", "T-087", "1", "11:30 AM"],
   ["Meera Iyer", "Masala Dosa", "T-156", "3", "9:45 AM"]]),
  scenarioText: "The canteen billing counter prints a slip for every order. Write a program that reads the customer's name, the item, the token number, the counter number, and the time, then prints the complete bill slip." });

Q.push({ ...structuredQ(0, "Hard", "Food Delivery Slip",
  ["Name", "Item", "Restaurant", "Address", "Delivery Time"],
  ["name", "item", "restaurant", "address", "delivery_time"],
  "FOOD DELIVERY SLIP", "Your order is on the way",
  [["Rohan Patil", "Paneer Wrap", "Campus Bites", "Hostel Block B, Room 204", "8:30 PM"],
   ["Priya Nair", "Veg Biryani", "Spice Route", "Hostel Block C, Room 118", "9:00 PM"],
   ["Sneha Rao", "Masala Maggi", "Campus Bites", "Hostel Block A, Room 305", "11:00 PM"]]),
  scenarioText: "A campus food delivery app prints a slip for every order placed. Write a program that reads the customer's name, the item, the restaurant, the delivery address, and the delivery time, then prints the complete slip." });

Q.push({ ...structuredQ(0, "Hard", "Cab Trip Receipt",
  ["Name", "Pickup", "Drop", "Driver", "Fare"],
  ["name", "pickup", "drop", "driver", "fare"],
  "CAB TRIP RECEIPT", "Thank you for riding with us",
  [["Arjun Mehta", "Hostel Gate", "Railway Station", "Suresh", "180"],
   ["Divya Shah", "Main Block", "City Mall", "Ramesh", "120"],
   ["Vikram Joshi", "Library", "Airport", "Suresh", "450"]]),
  scenarioText: "A campus cab-sharing app prints a receipt at the end of every trip. Write a program that reads the passenger's name, the pickup point, the drop point, the driver's name, and the fare, then prints the complete receipt. Fare is read and printed as plain text." });

Q.push({ ...structuredQ(0, "Hard", "Internship Offer Snippet",
  ["Name", "Company", "Role", "Start Date", "Stipend"],
  ["name", "company", "role", "start_date", "stipend"],
  "INTERNSHIP OFFER", "Please confirm your acceptance by email",
  [["Asha Verma", "BrightTech", "Data Analyst Intern", "1 Aug 2026", "15000"],
   ["Kabir Khan", "NimbusSoft", "Backend Intern", "5 Aug 2026", "12000"],
   ["Meera Iyer", "Craftly", "Marketing Intern", "10 Aug 2026", "10000"]]),
  scenarioText: "The placement cell prints a short offer snippet for every student placed in an internship. Write a program that reads a student's name, the company, the role, the start date, and the stipend, then prints the complete offer snippet. Stipend is read and printed as plain text." });

Q.push({ ...structuredQ(0, "Hard", "Library Membership Card",
  ["Name", "Member ID", "Book", "Issue Date", "Due Date"],
  ["name", "member_id", "book", "issue_date", "due_date"],
  "LIBRARY MEMBERSHIP CARD", "Return books on or before the due date",
  [["Rohan Patil", "LIB-2041", "Clean Code", "20 Jul 2026", "3 Aug 2026"],
   ["Priya Nair", "LIB-2042", "Atomic Habits", "21 Jul 2026", "4 Aug 2026"],
   ["Sneha Rao", "LIB-2043", "Deep Work", "22 Jul 2026", "5 Aug 2026"]]),
  scenarioText: "The library issues a membership card to every student who registers. Write a program that reads a student's name, member ID, current book, issue date, and due date, then prints the complete card." });

Q.push({ ...structuredQ(0, "Hard", "Class Representative Announcement",
  ["Name", "Class", "Message", "Date", "Time"],
  ["name", "class_name", "message", "date", "time"],
  "ANNOUNCEMENT", "- Class Representative",
  [["Kabir Khan", "B.Tech CSE - Sem 3", "Assignment deadline extended to Friday", "12 Mar 2026", "5:00 PM"],
   ["Meera Iyer", "B.Tech ECE - Sem 3", "Class moved to Room 204", "13 Mar 2026", "9:00 AM"],
   ["Asha Verma", "B.Tech ME - Sem 3", "Guest lecture in the auditorium", "14 Mar 2026", "2:00 PM"]]),
  scenarioText: "The class representative posts a formal announcement to the class group on important days. Write a program that reads the class rep's name, the class, the message, the date, and the time, then prints the complete announcement." });

// ---- assign final question numbers, set 10 as the Course Set --------------
Q.forEach((q, i) => { q.n = i + 1; });
const COURSE_SET = Q.slice(0, 10);
const EXTRA_SET = Q.slice(10);

// ---- render one question into an array of Paragraphs ----------------------

function renderQuestion(q) {
  const out = [];
  out.push(new Paragraph({
    heading: HeadingLevel.HEADING_3,
    spacing: { before: 320, after: 60 },
    children: [new TextRun({ text: `Q${q.n}. ${q.title}` })],
  }));
  out.push(new Paragraph({
    spacing: { after: 160 },
    children: [new TextRun({ text: `Difficulty: ${q.difficulty}`, bold: true, italics: true })],
  }));

  out.push(label("Problem Statement"));
  out.push(bodyPara(q.scenarioText));
  out.push(bodyPara("The program must:"));
  q.fields.forEach((f) => out.push(bulletPara(`Read ${f}.`)));
  out.push(bulletPara("Print the result in exactly the format shown below."));

  out.push(label("Input Format"));
  q.inputLines.forEach((l) => out.push(bulletPara(l.replace(/^- /, ""))));

  out.push(label("Output Format"));
  if (q.outputTemplate) {
    out.push(codeBlock([q.outputTemplate]));
  } else {
    out.push(codeBlock(q.outputLines));
  }
  out.push(bodyPara("Every value must be printed exactly as entered, with no extra text added or removed."));

  out.push(label("Constraints"));
  q.constraints.forEach((c) => out.push(bulletPara(c)));

  q.testCases.forEach((tc, i) => {
    out.push(label(`Test Case ${i + 1}`));
    out.push(bodyPara("Input:"));
    out.push(codeBlock(tc.input));
    out.push(bodyPara("Output:"));
    out.push(codeBlock(tc.output));
  });

  out.push(label("Python Solution"));
  out.push(codeBlock(q.solution));

  return out;
}

// ---- assemble document -----------------------------------------------------

const children = [];

children.push(new Paragraph({
  heading: HeadingLevel.TITLE,
  alignment: AlignmentType.CENTER,
  spacing: { after: 120 },
  children: [new TextRun({ text: "Unit 1 — Introduction to Programming" })],
}));
children.push(new Paragraph({
  heading: HeadingLevel.HEADING_2,
  alignment: AlignmentType.CENTER,
  spacing: { after: 320 },
  children: [new TextRun({ text: "Coding Question Bank" })],
}));
children.push(bodyPara(
  "Scope note: Unit 1 only teaches variables, input(), and print(). Every question below " +
  "is solvable using exactly those three things, with no operators, type casting, conditionals, " +
  "or loops, since those are taught in later units."
));

children.push(new Paragraph({
  heading: HeadingLevel.HEADING_1,
  spacing: { before: 400, after: 160 },
  children: [new TextRun({ text: "Course Set (10 Questions)" })],
}));
COURSE_SET.forEach((q) => children.push(...renderQuestion(q)));

children.push(new Paragraph({
  heading: HeadingLevel.HEADING_1,
  spacing: { before: 500, after: 160 },
  children: [new TextRun({ text: "Extra / Assessment Set (20 Questions)" })],
}));
EXTRA_SET.forEach((q) => children.push(...renderQuestion(q)));

const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
      },
    },
    children,
  }],
});

Packer.toBuffer(doc).then((buffer) => {
  const fs = require("fs");
  const outPath = __dirname + "/Unit 1 - Introduction to Programming - Coding Questions.docx";
  fs.writeFileSync(outPath, buffer);
  console.log("Written:", outPath);
  console.log("Course set:", COURSE_SET.length, "Extra set:", EXTRA_SET.length);
  console.log("By difficulty (course):", COURSE_SET.map((q) => q.difficulty).join(","));
  console.log("By difficulty (extra):", EXTRA_SET.map((q) => q.difficulty).join(","));
});
