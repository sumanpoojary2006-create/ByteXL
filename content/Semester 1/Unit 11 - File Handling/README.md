# Unit 11: File Handling

**Semester 1: Python Fundamentals**

Make data persist beyond a single run by reading and writing files.

## Topics (teach in order)

| # | Topic | File |
|---|-------|------|
| 1 | Why Files: Persisting Data Beyond Runtime | [01_why_files_persisting_data_beyond_runtime.md](01_why_files_persisting_data_beyond_runtime.md) |
| 2 | Reading Text Files (open, read, readlines) | [02_reading_text_files.md](02_reading_text_files.md) |
| 3 | Writing and Appending to Files | [03_writing_and_appending_to_files.md](03_writing_and_appending_to_files.md) |
| 4 | The with Statement (Context-Managed Files) | [04_the_with_statement.md](04_the_with_statement.md) |
| 5 | Working with File Paths using pathlib | [05_working_with_file_paths_using_pathlib.md](05_working_with_file_paths_using_pathlib.md) |
| 6 | Finding Files with glob (Pattern Matching) | [06_finding_files_with_glob.md](06_finding_files_with_glob.md) |
| 7 | Reading and Writing CSV Files | [07_reading_and_writing_csv_files.md](07_reading_and_writing_csv_files.md) |
| 8 | Reading and Writing JSON | [08_reading_and_writing_json.md](08_reading_and_writing_json.md) |
| 9 | Common File Pitfalls: Encoding and Missing Files | [09_common_file_pitfalls_encoding_and_missing_files.md](09_common_file_pitfalls_encoding_and_missing_files.md) |

## How each lesson is written

Each lesson follows the house style: a standardized **Introduction** heading (no page-title H1), a story-led flow with real-world examples and situation-based questions under natural headings, a concept-scoped illustration, and a closing **Conclusion**. Plain-English explanations are preferred; Python code is kept simple and interactive. No emojis, no em dashes.

Lessons continue Tara's thread from Unit 7: her in-memory fest data vanishing on exit, reading and writing a wristband log, append-safe daily logging, crash-safe `with` blocks, pathlib-built report paths, glob-matched daily sales files, CSV sales records, the nested stall report saved as JSON, and closing pitfalls around missing files and encoding. Note: exception handling (try/except) is intentionally not used anywhere in this unit, since it is taught in the next one; missing-file handling here uses `Path.exists()` guard checks instead, with an explicit forward-reference to Unit 12.

_Status: lesson content authored for all 9 topics, all code blocks verified to run correctly and match documented output in isolated test directories._
