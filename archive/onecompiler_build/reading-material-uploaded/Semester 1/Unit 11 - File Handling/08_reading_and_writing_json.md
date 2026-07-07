## Introduction

Tara's combined fest report, from the sets and dictionaries unit, was a nested dictionary: stall names mapping to their own dictionaries of items and prices. CSV cannot represent that shape at all; it only knows flat rows and columns, with no natural way to say "this value is itself a whole group of other values." She needs a file format that preserves real structure, nesting included, exactly as Python's own dictionaries and lists already do.

That format is **JSON**, short for JavaScript Object Notation, and despite the name, it has become the standard way nearly every modern programming language saves and exchanges structured data, with Python's built-in `json` module translating directly between it and Python's own dictionaries and lists.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-11-file-handling/08_nested_dict_to_json_file.png)

## What JSON Looks Like

JSON text looks remarkably close to a Python dictionary or list, with curly braces for objects, square brackets for arrays, and quoted text for strings.

```json
{
    "Merch": {"T-shirt": 350, "Mug": 150},
    "Food": {"Samosa": 30, "Cold Drink": 40}
}
```

This is exactly the nested dictionary shape from the sets and dictionaries unit, written out as plain text in a way any program, in any language, can read back correctly.

## Writing a Dictionary to a JSON File: json.dump

`json.dump` takes a Python object and writes it directly into an open file, as JSON text.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-11-file-handling-08-reading-and-writing-json-001-9e53948491.html"
 width="100%"
></iframe>

`indent=4` is optional, but it formats the saved file with readable line breaks and indentation, rather than squeezing everything onto a single dense line, which matters enormously the moment a human ever needs to open the file directly.

## Reading a JSON File Back: json.load

`json.load` reads an open file's JSON text and reconstructs the original Python structure, nesting and all.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-11-file-handling-08-reading-and-writing-json-002-60d8311177.html"
 width="100%"
></iframe>

`loaded_stalls` comes back as a genuine Python dictionary, with the exact same nested shape it was saved with, so the double-key lookup from the nested dictionaries unit works immediately, with no extra parsing of any kind required.

## Converting To and From a String Directly: dumps and loads

Sometimes you want the JSON text itself, as a string, rather than writing straight to a file, for example to print it, or to send it somewhere other than a file. `json.dumps` (with an "s" for string) and `json.loads` do exactly that.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-11-file-handling-08-reading-and-writing-json-003-053b1dee00.html"
 width="100%"
></iframe>

The pattern to remember: the function ending in a plain "p," `dump` and `load`, works directly with an open file, while the function ending in "s," `dumps` and `loads`, works with a plain string.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-11-file-handling/08_json_file_vs_string.png)


## What JSON Can and Cannot Hold

JSON supports the data shapes you already know well: dictionaries (as JSON "objects"), lists (as JSON "arrays"), strings, numbers, booleans, and a `null` value, which becomes Python's `None`. It cannot directly hold a Python tuple, which gets silently converted into a JSON array, indistinguishable from a list once saved; if that distinction matters to your program, JSON alone cannot preserve it.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-11-file-handling-08-reading-and-writing-json-004-d69152f593.html"
 width="100%"
></iframe>

Notice the tuple became `[15.2993, 74.124]`, square brackets, exactly like a list, in the saved JSON.

## CSV vs JSON at a Glance

| | CSV | JSON |
|---|---|---|
| Best shape | Flat rows and columns | Nested structures, dictionaries within dictionaries |
| Types preserved | No, everything is text | Mostly yes: numbers, booleans, `None`, nesting |
| Human readable | Yes, as a simple table | Yes, especially with `indent` |
| Tuples preserved as tuples | N/A | No, saved as JSON arrays, indistinguishable from lists |

## Your Turn: Save and Reload the Fest Report

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-11-file-handling-08-reading-and-writing-json-005-b51ae34bd5.html"
 width="100%"
></iframe>

This is the exact nested-loop reporting pattern from the sets and dictionaries unit, now reading from a file that genuinely outlives the program that wrote it.

## Conclusion

JSON preserves nested, structured data, dictionaries within dictionaries and lists within them, far more faithfully than CSV's flat rows ever could, with `json.dump`/`json.load` working directly with open files and `json.dumps`/`json.loads` working with plain strings; only tuples lose their identity, silently saved as ordinary JSON arrays. Choosing between CSV and JSON comes down to the shape of your data: flat and tabular favours CSV, nested and structured favours JSON. With reliable reading and writing in place for text, CSV, and JSON alike, the final lesson of this unit covers the pitfalls that catch even careful programmers: encoding mismatches and missing files.
