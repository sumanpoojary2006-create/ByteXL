const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  PageBreak, BorderStyle,
} = require("docx");

const units = [
  { num: 1, title: "Unit 1 - Introduction to Programming", file: "Unit 1 - Introduction to Programming - MCQ.xlsx" },
  { num: 2, title: "Unit 2 - Data Types and Operators", file: "Unit 2 - Data Types and Operators - MCQ.xlsx" },
  { num: 3, title: "Unit 3 - Control Flow", file: "Unit 3 - Control Flow - MCQ.xlsx" },
];

const data = JSON.parse(fs.readFileSync("mcq_review_data.json", "utf8"));

const optionLetters = ["A", "B", "C", "D"];

function buildUnitChildren(unit, questions) {
  const children = [];
  children.push(new Paragraph({
    heading: HeadingLevel.HEADING_1,
    children: [new TextRun(unit.title)],
  }));

  questions.forEach((q, idx) => {
    const n = idx + 1;
    children.push(new Paragraph({
      heading: HeadingLevel.HEADING_2,
      children: [new TextRun(`Q${n}. ${q.title}`)],
    }));
    children.push(new Paragraph({
      children: [new TextRun({ text: q.description, italics: false })],
      spacing: { after: 120 },
    }));

    const options = [q.option1, q.option2, q.option3, q.option4];
    options.forEach((opt, i) => {
      if (opt === null || opt === undefined || opt === "None") return;
      const isCorrect = (i + 1) === Number(q.answer);
      children.push(new Paragraph({
        children: [
          new TextRun({ text: `${optionLetters[i]}. `, bold: isCorrect }),
          new TextRun({ text: String(opt), bold: isCorrect }),
          new TextRun({ text: isCorrect ? "  (Correct)" : "", bold: true, color: "2E7D32" }),
        ],
        indent: { left: 360 },
      }));
    });

    if (q.explanation && q.explanation !== "None") {
      children.push(new Paragraph({
        children: [
          new TextRun({ text: "Explanation: ", bold: true }),
          new TextRun(String(q.explanation)),
        ],
        spacing: { before: 80, after: 60 },
      }));
    }

    children.push(new Paragraph({
      children: [
        new TextRun({ text: `Difficulty: ${q.difficulty}   |   Bloom: ${q.bloomTaxonomy}   |   Score: ${q.score}   |   Tags: ${q.tags}`, size: 18, color: "777777" }),
      ],
      spacing: { after: 200 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: "CCCCCC", space: 4 } },
    }));
  });

  return children;
}

const sections = [];
units.forEach((unit, i) => {
  const questions = data[unit.file];
  const children = buildUnitChildren(unit, questions);
  if (i > 0) {
    children[0] = new Paragraph({
      heading: HeadingLevel.HEADING_1,
      pageBreakBefore: true,
      children: [new TextRun(unit.title)],
    });
  }
  sections.push({
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
      },
    },
    children,
  });
});

const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 32, bold: true, font: "Arial" },
        paragraph: { spacing: { before: 240, after: 240 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 26, bold: true, font: "Arial" },
        paragraph: { spacing: { before: 200, after: 100 }, outlineLevel: 1 } },
    ],
  },
  sections,
});

Packer.toBuffer(doc).then((buffer) => {
  fs.writeFileSync("MCQ Review - Unit 1, 2 and Unit 3.docx", buffer);
  console.log("done");
});
