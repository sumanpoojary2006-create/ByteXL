## Introduction

Nadia's library system communicates with three external services: a catalog API that speaks JSON, a legacy report generator that only reads CSV, and a partner consortium that sends both. Every piece of data that enters or leaves her system passes through one of these two formats. She has been reading JSON with string splitting and `split(",")` for CSV -- both of which break silently on edge cases like embedded commas and nested objects.

This lesson covers `json` and `csv` properly: not just how to read and write them, but how to handle the edge cases that break naive implementations.

![Two file icons side by side: a JSON file with nested braces and an arrow showing json.loads/dumps converting it to and from a Python dict; a CSV file with a row grid and an arrow showing csv.reader/writer converting it to and from Python lists](images/08_json_csv.png)

## json: Reading and Writing JSON

The `json` module converts between Python objects and JSON strings (or files). There are four functions to know:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-08-json-and-csv-001-018911177d.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-08-json-and-csv-002-13d2f52514.html"
 width="100%"
></iframe>

## json.JSONDecodeError

Malformed JSON raises `json.JSONDecodeError`. Always handle it when parsing JSON from external sources:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-08-json-and-csv-003-0eae9915bd.html"
 width="100%"
></iframe>

## csv: Reading and Writing CSV

CSV looks simple but has tricky edge cases: fields that contain commas must be quoted, quoted fields can contain newlines, and different systems use different line endings. The `csv` module handles all of this correctly.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-08-json-and-csv-004-f34697c279.html"
 width="100%"
></iframe>

Always open CSV files with `newline=""`. If you do not, the `csv` module may miscount newlines inside quoted fields.

## DictReader and DictWriter

`csv.DictReader` treats the first row as column names and returns each subsequent row as a `dict`, making column access readable:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-08-json-and-csv-005-574b28908e.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-08-json-and-csv-006-cf1a9af0b2.html"
 width="100%"
></iframe>

## Conclusion

`json` and `csv` are Python's built-in formats for structured data exchange. `json` handles nested objects and preserves types. `csv` handles flat tabular data and integrates with spreadsheet tools. Both have edge cases that are handled correctly by the standard library and incorrectly by naive string manipulation. This concludes Unit 7. The next unit moves from using Python's standard library to ensuring its correct use: writing tests with `pytest`.
