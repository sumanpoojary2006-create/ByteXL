## Introduction

Nadia's library system communicates with three external services: a catalog API that speaks JSON, a legacy report generator that only reads CSV, and a partner consortium that sends both. Every piece of data that enters or leaves her system passes through one of these two formats. She has been reading JSON with string splitting and `split(",")` for CSV -- both of which break silently on edge cases like embedded commas and nested objects.

This lesson covers `json` and `csv` properly: not just how to read and write them, but how to handle the edge cases that break naive implementations.

![Two file icons side by side: a JSON file with nested braces and an arrow showing json.loads/dumps converting it to and from a Python dict; a CSV file with a row grid and an arrow showing csv.reader/writer converting it to and from Python lists](images/08_json_csv.png)

## json: Reading and Writing JSON

The `json` module converts between Python objects and JSON strings (or files). There are four functions to know:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2pzb25fYW5kX2NzdiBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoiaW1wb3J0IGpzb25cblxuIyBQeXRob24gZGljdCAtPiBKU09OIHN0cmluZ1xuZGF0YSA9IHtcImlzYm5cIjogXCI5NzgtMDAxXCIsIFwidGl0bGVcIjogXCJEdW5lXCIsIFwiY29waWVzXCI6IDMsIFwiYXZhaWxhYmxlXCI6IFRydWV9XG5qc29uX3N0cmluZyA9IGpzb24uZHVtcHMoZGF0YSlcbnByaW50KGpzb25fc3RyaW5nKVxuIyAne1wiaXNiblwiOiBcIjk3OC0wMDFcIiwgXCJ0aXRsZVwiOiBcIkR1bmVcIiwgXCJjb3BpZXNcIjogMywgXCJhdmFpbGFibGVcIjogdHJ1ZX0nXG5cbiMgSlNPTiBzdHJpbmcgLT4gUHl0aG9uIGRpY3RcbnBhcnNlZCA9IGpzb24ubG9hZHMoanNvbl9zdHJpbmcpXG5wcmludChwYXJzZWRbXCJ0aXRsZVwiXSkgICAjICdEdW5lJ1xucHJpbnQodHlwZShwYXJzZWQpKSAgICAgICMgPGNsYXNzICdkaWN0Jz5cblxuIyBXcml0ZSB0byBhIGZpbGVcbndpdGggb3BlbihcImNhdGFsb2cuanNvblwiLCBcIndcIikgYXMgZjpcbiAgICBqc29uLmR1bXAoZGF0YSwgZiwgaW5kZW50PTIpXG5cbiMgUmVhZCBmcm9tIGEgZmlsZVxud2l0aCBvcGVuKFwiY2F0YWxvZy5qc29uXCIsIFwiclwiKSBhcyBmOlxuICAgIGxvYWRlZCA9IGpzb24ubG9hZChmKVxucHJpbnQobG9hZGVkKSJ9"
 width="100%"
></iframe>

`dumps`/`loads` work with strings. `dump`/`load` work with file objects. The `indent=2` argument to `dump`/`dumps` produces readable pretty-printed JSON.

## JSON Type Mapping

Python and JSON types map to each other, but not always one-to-one:

| Python | JSON |
|---|---|
| `dict` | object (`{}`) |
| `list`, `tuple` | array (`[]`) |
| `str` | string |
| `int`, `float` | number |
| `True` / `False` | `true` / `false` |
| `None` | `null` |
| `datetime` | no native equivalent |

Dates have no JSON type. The standard practice is to store them as ISO 8601 strings:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2pzb25fYW5kX2NzdiBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoiZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZVxuaW1wb3J0IGpzb25cblxucmVjb3JkID0ge1xuICAgIFwiaXNiblwiOiBcIjk3OC0wMDFcIixcbiAgICBcImJvcnJvd19kYXRlXCI6IGRhdGUoMjAyNiwgNywgMSkuaXNvZm9ybWF0KCkgICMgJzIwMjYtMDctMDEnXG59XG5qc29uX3N0ciA9IGpzb24uZHVtcHMocmVjb3JkKVxucGFyc2VkID0ganNvbi5sb2Fkcyhqc29uX3N0cilcbmJvcnJvd19kYXRlID0gZGF0ZS5mcm9taXNvZm9ybWF0KHBhcnNlZFtcImJvcnJvd19kYXRlXCJdKSJ9"
 width="100%"
></iframe>

## json.JSONDecodeError

Malformed JSON raises `json.JSONDecodeError`. Always handle it when parsing JSON from external sources:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2pzb25fYW5kX2NzdiBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoiaW1wb3J0IGpzb25cblxuZGVmIHBhcnNlX2NhdGFsb2cocmF3OiBzdHIpIC0-IGRpY3QgfCBOb25lOlxuICAgIHRyeTpcbiAgICAgICAgcmV0dXJuIGpzb24ubG9hZHMocmF3KVxuICAgIGV4Y2VwdCBqc29uLkpTT05EZWNvZGVFcnJvciBhcyBleGM6XG4gICAgICAgIHByaW50KGZcIkludmFsaWQgSlNPTjoge2V4Y31cIilcbiAgICAgICAgcmV0dXJuIE5vbmUifQ"
 width="100%"
></iframe>

## csv: Reading and Writing CSV

CSV looks simple but has tricky edge cases: fields that contain commas must be quoted, quoted fields can contain newlines, and different systems use different line endings. The `csv` module handles all of this correctly.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2pzb25fYW5kX2NzdiBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoiaW1wb3J0IGNzdlxuXG4jIFdyaXRpbmcgQ1NWXG5yb3dzID0gW1xuICAgIFtcImlzYm5cIiwgXCJ0aXRsZVwiLCBcImdlbnJlXCIsIFwiY29waWVzXCJdLFxuICAgIFtcIjk3OC0wMDFcIiwgXCJEdW5lXCIsIFwiU2NpZW5jZSBGaWN0aW9uXCIsIFwiM1wiXSxcbiAgICBbXCI5NzgtMDAyXCIsIFwiVGhlLCBHcmVhdCBHYXRzYnlcIiwgXCJGaWN0aW9uXCIsIFwiNVwiXSwgICMgY29tbWEgaW5zaWRlIGEgZmllbGRcbl1cblxud2l0aCBvcGVuKFwiY2F0YWxvZy5jc3ZcIiwgXCJ3XCIsIG5ld2xpbmU9XCJcIikgYXMgZjpcbiAgICB3cml0ZXIgPSBjc3Yud3JpdGVyKGYpXG4gICAgd3JpdGVyLndyaXRlcm93cyhyb3dzKVxuIyBUaGUgY29tbWEgaW5zaWRlIFwiVGhlLCBHcmVhdCBHYXRzYnlcIiBpcyBjb3JyZWN0bHkgcXVvdGVkIGluIHRoZSBmaWxlXG5cbiMgUmVhZGluZyBDU1ZcbndpdGggb3BlbihcImNhdGFsb2cuY3N2XCIsIFwiclwiLCBuZXdsaW5lPVwiXCIpIGFzIGY6XG4gICAgcmVhZGVyID0gY3N2LnJlYWRlcihmKVxuICAgIGZvciByb3cgaW4gcmVhZGVyOlxuICAgICAgICBwcmludChyb3cpXG4jIFsnaXNibicsICd0aXRsZScsICdnZW5yZScsICdjb3BpZXMnXVxuIyBbJzk3OC0wMDEnLCAnRHVuZScsICdTY2llbmNlIEZpY3Rpb24nLCAnMyddXG4jIFsnOTc4LTAwMicsICdUaGUsIEdyZWF0IEdhdHNieScsICdGaWN0aW9uJywgJzUnXSJ9"
 width="100%"
></iframe>

Always open CSV files with `newline=""`. If you do not, the `csv` module may miscount newlines inside quoted fields.

## DictReader and DictWriter

`csv.DictReader` treats the first row as column names and returns each subsequent row as a `dict`, making column access readable:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2pzb25fYW5kX2NzdiBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoiaW1wb3J0IGNzdlxuXG4jIERpY3RXcml0ZXI6IHdyaXRlIHdpdGggY29sdW1uIG5hbWVzXG5maWVsZG5hbWVzID0gW1wiaXNiblwiLCBcInRpdGxlXCIsIFwiY29waWVzXCJdXG53aXRoIG9wZW4oXCJjYXRhbG9nLmNzdlwiLCBcIndcIiwgbmV3bGluZT1cIlwiKSBhcyBmOlxuICAgIHdyaXRlciA9IGNzdi5EaWN0V3JpdGVyKGYsIGZpZWxkbmFtZXM9ZmllbGRuYW1lcylcbiAgICB3cml0ZXIud3JpdGVoZWFkZXIoKVxuICAgIHdyaXRlci53cml0ZXJvdyh7XCJpc2JuXCI6IFwiOTc4LTAwMVwiLCBcInRpdGxlXCI6IFwiRHVuZVwiLCBcImNvcGllc1wiOiAzfSlcbiAgICB3cml0ZXIud3JpdGVyb3coe1wiaXNiblwiOiBcIjk3OC0wMDJcIiwgXCJ0aXRsZVwiOiBcIkZvdW5kYXRpb25cIiwgXCJjb3BpZXNcIjogMn0pXG5cbiMgRGljdFJlYWRlcjogcmVhZCBhcyBkaWN0c1xud2l0aCBvcGVuKFwiY2F0YWxvZy5jc3ZcIiwgXCJyXCIsIG5ld2xpbmU9XCJcIikgYXMgZjpcbiAgICByZWFkZXIgPSBjc3YuRGljdFJlYWRlcihmKVxuICAgIGZvciByb3cgaW4gcmVhZGVyOlxuICAgICAgICBwcmludChmXCJ7cm93Wydpc2JuJ119OiB7cm93Wyd0aXRsZSddfSAoe3Jvd1snY29waWVzJ119IGNvcGllcylcIikifQ"
 width="100%"
></iframe>

`DictReader` is almost always preferable to `reader` because it makes the column being accessed explicit in the code.

## Choosing json vs csv

| Consideration | JSON | CSV |
|---|---|---|
| Nested data | Supported natively | Not supported |
| Data types | Preserved (int, bool, null) | Everything is a string |
| Readability | Good for nested structures | Good for tabular data |
| Interop with spreadsheets | Poor | Excellent |
| Streaming large files | Requires `ijson` or manual chunks | Line-by-line with `csv.reader` |

## The json / csv Modules at a Glance

| Function | What it does |
|---|---|
| `json.dumps(obj)` | Python object to JSON string |
| `json.loads(string)` | JSON string to Python object |
| `json.dump(obj, file)` | Python object to JSON file |
| `json.load(file)` | JSON file to Python object |
| `csv.reader(file)` | Read rows as lists |
| `csv.writer(file)` | Write rows as lists |
| `csv.DictReader(file)` | Read rows as dicts (first row = headers) |
| `csv.DictWriter(file, fieldnames)` | Write rows as dicts |

## Your Turn

Write two functions: `export_catalog_json` and `export_catalog_csv`, both accepting a list of book dicts and a file path. Then write `load_catalog(path)` that detects the file extension and calls the correct reader.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2pzb25fYW5kX2NzdiBjb2RlIDYiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDYucHkiLCJjb2RlIjoiaW1wb3J0IGpzb24sIGNzdlxuZnJvbSBwYXRobGliIGltcG9ydCBQYXRoXG5cbmRlZiBleHBvcnRfY2F0YWxvZ19qc29uKGJvb2tzLCBwYXRoKTpcbiAgICBQYXRoKHBhdGgpLndyaXRlX3RleHQoanNvbi5kdW1wcyhib29rcywgaW5kZW50PTIpKVxuXG5kZWYgZXhwb3J0X2NhdGFsb2dfY3N2KGJvb2tzLCBwYXRoKTpcbiAgICBpZiBub3QgYm9va3M6XG4gICAgICAgIHJldHVyblxuICAgIHdpdGggb3BlbihwYXRoLCBcIndcIiwgbmV3bGluZT1cIlwiKSBhcyBmOlxuICAgICAgICB3cml0ZXIgPSBjc3YuRGljdFdyaXRlcihmLCBmaWVsZG5hbWVzPWJvb2tzWzBdLmtleXMoKSlcbiAgICAgICAgd3JpdGVyLndyaXRlaGVhZGVyKClcbiAgICAgICAgd3JpdGVyLndyaXRlcm93cyhib29rcylcblxuZGVmIGxvYWRfY2F0YWxvZyhwYXRoKTpcbiAgICBwID0gUGF0aChwYXRoKVxuICAgIGlmIHAuc3VmZml4ID09IFwiLmpzb25cIjpcbiAgICAgICAgcmV0dXJuIGpzb24ubG9hZHMocC5yZWFkX3RleHQoKSlcbiAgICBlbGlmIHAuc3VmZml4ID09IFwiLmNzdlwiOlxuICAgICAgICB3aXRoIG9wZW4ocCwgbmV3bGluZT1cIlwiKSBhcyBmOlxuICAgICAgICAgICAgcmV0dXJuIGxpc3QoY3N2LkRpY3RSZWFkZXIoZikpXG4gICAgcmFpc2UgVmFsdWVFcnJvcihmXCJVbnN1cHBvcnRlZCBmb3JtYXQ6IHtwLnN1ZmZpeH1cIilcblxuYm9va3MgPSBbe1wiaXNiblwiOiBcIjk3OC0wMDFcIiwgXCJ0aXRsZVwiOiBcIkR1bmVcIn0sIHtcImlzYm5cIjogXCI5NzgtMDAyXCIsIFwidGl0bGVcIjogXCJGb3VuZGF0aW9uXCJ9XVxuZXhwb3J0X2NhdGFsb2dfanNvbihib29rcywgXCJjYXRhbG9nLmpzb25cIilcbmV4cG9ydF9jYXRhbG9nX2Nzdihib29rcywgXCJjYXRhbG9nLmNzdlwiKVxucHJpbnQobG9hZF9jYXRhbG9nKFwiY2F0YWxvZy5qc29uXCIpKVxucHJpbnQobG9hZF9jYXRhbG9nKFwiY2F0YWxvZy5jc3ZcIikpIn0"
 width="100%"
></iframe>

## Conclusion

`json` and `csv` are Python's built-in formats for structured data exchange. `json` handles nested objects and preserves types. `csv` handles flat tabular data and integrates with spreadsheet tools. Both have edge cases that are handled correctly by the standard library and incorrectly by naive string manipulation. This concludes Unit 7. The next unit moves from using Python's standard library to ensuring its correct use: writing tests with `pytest`.
