import fs from "node:fs/promises";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const workbook = Workbook.create();
const sheet = workbook.worksheets.add("Fill Test");
sheet.getRange("A1:D4").values = [
  ["Syntax", "Expected", "Notes", "Visible?"],
  ["format.fill = { color }", "red", "", ""],
  ["format.fill = { type: solid, color }", "green", "", ""],
  ["format.fill = string", "blue", "", ""],
];

sheet.getRange("A1:D1").format.fill = { color: "#17324D" };
sheet.getRange("A1:D1").format.font = { bold: true, color: "#FFFFFF" };
sheet.getRange("A2:D2").format.fill = { color: "#FF0000" };
sheet.getRange("A3:D3").format.fill = { type: "solid", color: "#00AA00" };
sheet.getRange("A4:D4").format.fill = "#0000FF";
sheet.getRange("A1:D4").format.borders = { preset: "all", style: "thin", color: "#999999" };

await fs.mkdir("/Users/suman/Desktop/ByteXL/.curriculum_build/fill_test", { recursive: true });
const preview = await workbook.render({ sheetName: "Fill Test", autoCrop: "all", scale: 2, format: "png" });
await fs.writeFile(
  "/Users/suman/Desktop/ByteXL/.curriculum_build/fill_test/fill_test.png",
  new Uint8Array(await preview.arrayBuffer()),
);
const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save("/Users/suman/Desktop/ByteXL/.curriculum_build/fill_test/fill_test.xlsx");
console.log("wrote fill test");
