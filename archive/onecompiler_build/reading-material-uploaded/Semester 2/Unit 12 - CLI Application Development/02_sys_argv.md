## Introduction

Priya's simplest CLI tool needs to accept one argument: a file path. Before using `argparse`, she wants to understand how Python receives command-line arguments at the lowest level: `sys.argv`. This foundation makes everything in the higher-level tools more intuitive.

![sys.argv shown as a list with index 0 being the script name and indices 1+ being the command-line arguments in order](images/02_sys_argv.png)

## What sys.argv Contains

When Python runs a script, `sys.argv` is a list of strings. The first element (`sys.argv[0]`) is the script name. Every subsequent element is a command-line argument.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-02-sys-argv-001-30589f6a5d.html"
 width="100%"
></iframe>

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-02-sys-argv-002-9186b15f64.html"
 width="100%"
></iframe>

Every argument is a string, even numbers. Converting types is the developer's responsibility.

## Reading Arguments Directly

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-02-sys-argv-003-262e04f136.html"
 width="100%"
></iframe>

Running:
<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-02-sys-argv-004-550ae6c3e1.html"
 width="100%"
></iframe>

## Parsing Multiple Arguments Manually

For more arguments, manual parsing becomes fragile but illustrates what argparse does under the hood:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-02-sys-argv-005-e8c8635c6b.html"
 width="100%"
></iframe>

This is essentially what `argparse` does, but with all the edge cases handled automatically.

## When sys.argv Is Enough

`sys.argv` is appropriate for:
- One-off scripts with at most one or two arguments
- Scripts where the arguments are always positional and never optional
- Simple utility functions used only internally

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-02-sys-argv-006-77f78208ea.html"
 width="100%"
></iframe>

For anything more complex -- optional flags, types other than strings, help text, default values -- use `argparse` or `typer`.

## sys.argv at a Glance

| Item | Value |
|---|---|
| `sys.argv[0]` | The script name |
| `sys.argv[1]` | First argument |
| `sys.argv[1:]` | All arguments (excludes script name) |
| `len(sys.argv)` | Total items including script name |
| All values | Strings (even if they look like numbers) |

## Your Turn

Write a `word_count.py` script that accepts a filename as `sys.argv[1]` and prints the number of lines, words, and characters in the file, matching the behavior of the Unix `wc` command:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-02-sys-argv-007-229128921b.html"
 width="100%"
></iframe>

Run it on a text file, then run the real `wc` command on the same file and compare the output.

## Conclusion

`sys.argv` is a list of strings containing the script name and all command-line arguments. It provides direct, unmediated access to what the user typed. For anything beyond one or two positional arguments, the manual parsing it requires becomes error-prone. The next lesson introduces `argparse`, the standard library's structured argument parser.
