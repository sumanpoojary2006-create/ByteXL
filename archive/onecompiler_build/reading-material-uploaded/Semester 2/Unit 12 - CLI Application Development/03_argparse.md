## Introduction

Priya's `import_books.py` script needs three things `sys.argv` makes difficult: optional arguments with defaults, a `--help` flag that explains how to use the tool, and automatic type conversion (the `--limit` option should be an integer, not a string). `argparse` provides all of these in about ten lines.

![An argparse-powered command shown with --help output: usage line, positional arguments, optional arguments with types and defaults, all automatically generated from the parser definition](images/03_argparse.png)

## Basic argparse Structure

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-03-argparse-001-bd546c2af2.html"
 width="100%"
></iframe>

Running:
<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-03-argparse-002-dc44d6cb20.html"
 width="100%"
></iframe>

## Argument Types

`argparse` converts arguments to the specified type, raising a clean error if conversion fails:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-03-argparse-003-39b47b954c.html"
 width="100%"
></iframe>

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-03-argparse-004-9f373062aa.html"
 width="100%"
></iframe>

Argparse shows the error message and exits with code 2 automatically.

## Subcommands

Many CLIs have subcommands (`git commit`, `git push`). `argparse` supports this with subparsers:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-03-argparse-005-d7c6975f41.html"
 width="100%"
></iframe>

Running:
<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-03-argparse-006-43517bd7ba.html"
 width="100%"
></iframe>

## Mutually Exclusive Arguments

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-03-argparse-007-bef5941fbf.html"
 width="100%"
></iframe>

## argparse at a Glance

| Feature | How to use |
|---|---|
| Positional arg | `add_argument("name")` |
| Optional arg | `add_argument("--name")` |
| Type conversion | `add_argument("--n", type=int)` |
| Default value | `add_argument("--n", default=10)` |
| Flag (boolean) | `add_argument("--flag", action="store_true")` |
| Restricted choices | `add_argument("--fmt", choices=["csv","json"])` |
| Subcommands | `subparsers = parser.add_subparsers(...)` |

## Your Turn

Build a `report.py` CLI with two subcommands: `daily` (requires `--date`) and `monthly` (requires `--month`, `--year`). Each prints a summary of what it would generate:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-03-argparse-008-4b03507027.html"
 width="100%"
></iframe>

Test: `python report.py daily --date 2026-07-01` and `python report.py monthly --month 7 --year 2026`.

## Conclusion

`argparse` provides structured argument parsing: types, defaults, help text, choices, and subcommands, all with automatic `--help` and error messages. It is the standard library choice for most CLI tools. The next lesson introduces `typer`, a third-party library that achieves the same thing with even less code by using Python type annotations.
