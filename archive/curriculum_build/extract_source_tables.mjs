import fs from "node:fs/promises";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const sources = [
  {
    label: "advanced_java",
    file: "/Users/suman/Downloads/Course Blueprint for Advanced Java.xlsx",
    ranges: [
      ["Course Structure", "A1:B100"],
      ["Question Taxonomy", "A1:D246"],
    ],
  },
  {
    label: "java_foundations",
    file: "/Users/suman/Downloads/Course Blueprint for Java Foundations.xlsx",
    ranges: [
      ["Course Structure", "A1:B97"],
      ["Question Taxonomy", "A1:D261"],
      ["Overview", "A1:B3"],
    ],
  },
  {
    label: "eda_curriculum",
    file: "/Users/suman/Downloads/Exploratory Data Analysis Curriculum.xlsx",
    ranges: [
      ["TOC Revamp", "A1:F154"],
      ["MetaData v2", "A1:H140"],
      ["Sheet8", "A1:C39"],
    ],
  },
];

const out = {};
for (const source of sources) {
  const input = await FileBlob.load(source.file);
  const workbook = await SpreadsheetFile.importXlsx(input);
  out[source.label] = { file: source.file, tables: {} };
  for (const [sheetName, rangeAddress] of source.ranges) {
    const sheet = workbook.worksheets.getItem(sheetName);
    const values = sheet.getRange(rangeAddress).values;
    out[source.label].tables[`${sheetName}!${rangeAddress}`] = values;
  }
}

await fs.writeFile(
  "/Users/suman/Desktop/ByteXL/.curriculum_build/source_tables.json",
  JSON.stringify(out, null, 2),
);
console.log("Wrote .curriculum_build/source_tables.json");
