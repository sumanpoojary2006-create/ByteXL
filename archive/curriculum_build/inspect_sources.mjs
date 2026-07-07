import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const files = [
  "/Users/suman/Downloads/Course Blueprint for Advanced Java.xlsx",
  "/Users/suman/Downloads/Course Blueprint for Java Foundations.xlsx",
  "/Users/suman/Downloads/Exploratory Data Analysis Curriculum.xlsx",
];

for (const file of files) {
  console.log(`\n===== ${file} =====`);
  const input = await FileBlob.load(file);
  const workbook = await SpreadsheetFile.importXlsx(input);
  const overview = await workbook.inspect({
    kind: "workbook,sheet,table",
    maxChars: 12000,
    tableMaxRows: 12,
    tableMaxCols: 14,
    tableMaxCellChars: 160,
  });
  console.log(overview.ndjson);

  const sheets = await workbook.inspect({
    kind: "sheet",
    include: "id,name",
    maxChars: 6000,
  });
  console.log("SHEETS");
  console.log(sheets.ndjson);

  for (const line of sheets.ndjson.split("\n").filter(Boolean)) {
    let record;
    try {
      record = JSON.parse(line);
    } catch {
      continue;
    }
    const name = record.name ?? record.id;
    if (!name) continue;
    const region = await workbook.inspect({
      kind: "region",
      sheetId: name,
      range: "A1:N80",
      maxChars: 20000,
      tableMaxRows: 24,
      tableMaxCols: 14,
      tableMaxCellChars: 180,
    });
    console.log(`REGION ${name}`);
    console.log(region.ndjson);
  }
}
