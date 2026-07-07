## Introduction

Tara's fest files are starting to spread across folders: a `logs` folder, a `reports` folder, a `data` folder for anything structured. She tries building a path to one of them by gluing strings together, `"data" + "/" + "fest_log.txt"`, and it works fine on her own laptop, until a teammate on a different operating system runs the exact same script and it quietly fails, because Windows paths are built with backslashes, not the forward slash Tara assumed everywhere.

Python's `pathlib` module represents file paths as proper objects instead of fragile strings, building them correctly for whatever operating system the script actually runs on, with no manual slash-guessing required at all.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-11-file-handling/05_pathlib_cross_platform_paths.png)

## Creating a Path

`Path`, from the `pathlib` module, wraps a file or folder location as an object you can work with directly.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X3dvcmtpbmdfd2l0aF9maWxlX3BhdGhzX3VzaW5nX3BhdGhsaWIgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6ImZyb20gcGF0aGxpYiBpbXBvcnQgUGF0aFxuXG5sb2dfZmlsZSA9IFBhdGgoXCJsb2dzL2Zlc3RfbG9nLnR4dFwiKVxucHJpbnQobG9nX2ZpbGUpICAgICMgbG9ncy9mZXN0X2xvZy50eHQifQ"
 width="100%"
></iframe>

## Building Paths With the / Operator

`pathlib` overloads the division operator, `/`, to join path pieces together correctly for whichever operating system the code is actually running on.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X3dvcmtpbmdfd2l0aF9maWxlX3BhdGhzX3VzaW5nX3BhdGhsaWIgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6ImZyb20gcGF0aGxpYiBpbXBvcnQgUGF0aFxuXG5mb2xkZXIgPSBQYXRoKFwibG9nc1wiKVxubG9nX2ZpbGUgPSBmb2xkZXIgLyBcImZlc3RfbG9nLnR4dFwiXG5wcmludChsb2dfZmlsZSkgICAgIyBsb2dzL2Zlc3RfbG9nLnR4dCJ9"
 width="100%"
></iframe>

This looks unusual the first time you see it, dividing a path by a string, but it is exactly the tool this lesson opened with: no manually typed slashes, no guessing which character a different operating system expects, because `Path` handles that detail correctly on its own.

## Checking Whether a Path Exists

`.exists()` checks whether a file or folder is actually present, without needing to try opening it first.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X3dvcmtpbmdfd2l0aF9maWxlX3BhdGhzX3VzaW5nX3BhdGhsaWIgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6ImZyb20gcGF0aGxpYiBpbXBvcnQgUGF0aFxuXG5sb2dfZmlsZSA9IFBhdGgoXCJmZXN0X2xvZy50eHRcIilcbnByaW50KGxvZ19maWxlLmV4aXN0cygpKSAgICAjIFRydWUgb3IgRmFsc2UsIGRlcGVuZGluZyBvbiB3aGV0aGVyIGl0IGlzIHJlYWxseSB0aGVyZSJ9"
 width="100%"
></iframe>

This is a clean, safe way to check before reading, sidestepping a `FileNotFoundError` entirely, a pattern the final lesson of this unit returns to properly.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-11-file-handling/05_pathlib_path_build_check.png)


## Reading and Writing Directly Through a Path

A `Path` object can read and write a file's contents directly, without a separate `open()` call at all, for the common case of working with an entire file's text in one go.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X3dvcmtpbmdfd2l0aF9maWxlX3BhdGhzX3VzaW5nX3BhdGhsaWIgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6ImZyb20gcGF0aGxpYiBpbXBvcnQgUGF0aFxuXG5sb2dfZmlsZSA9IFBhdGgoXCJmZXN0X2xvZy50eHRcIilcbmxvZ19maWxlLndyaXRlX3RleHQoXCJHYXRlIG9wZW5lZCBhdCA5IEFNXFxuXCIpXG5cbmNvbnRlbnRzID0gbG9nX2ZpbGUucmVhZF90ZXh0KClcbnByaW50KGNvbnRlbnRzKSAgICAjIEdhdGUgb3BlbmVkIGF0IDkgQU0ifQ"
 width="100%"
></iframe>

For anything more involved, line-by-line reading, append mode, or working with `with` directly, `Path` objects can still be passed straight into `open()`, exactly where a plain filename string would have gone.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X3dvcmtpbmdfd2l0aF9maWxlX3BhdGhzX3VzaW5nX3BhdGhsaWIgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6IndpdGggb3Blbihsb2dfZmlsZSwgXCJhXCIpIGFzIGZpbGU6XG4gICAgZmlsZS53cml0ZShcIkZpcnN0IHdyaXN0YmFuZCBzY2FubmVkIGF0IDk6MDIgQU1cXG5cIikifQ"
 width="100%"
></iframe>

## Useful Path Properties

A `Path` object can answer several questions about itself directly, as attributes rather than method calls.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X3dvcmtpbmdfd2l0aF9maWxlX3BhdGhzX3VzaW5nX3BhdGhsaWIgY29kZSA2IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA2LnB5IiwiY29kZSI6ImZyb20gcGF0aGxpYiBpbXBvcnQgUGF0aFxuXG5yZXBvcnQgPSBQYXRoKFwicmVwb3J0cy9kYXkxX3NhbGVzLmNzdlwiKVxucHJpbnQocmVwb3J0Lm5hbWUpICAgICAgIyBkYXkxX3NhbGVzLmNzdlxucHJpbnQocmVwb3J0LnN0ZW0pICAgICAgIyBkYXkxX3NhbGVzXG5wcmludChyZXBvcnQuc3VmZml4KSAgICAjIC5jc3ZcbnByaW50KHJlcG9ydC5wYXJlbnQpICAgICMgcmVwb3J0cyJ9"
 width="100%"
></iframe>

`.name` is the full filename, `.stem` is the filename without its extension, `.suffix` is just the extension, and `.parent` is the containing folder, all read directly without any string-splitting of your own.

## Creating a Folder

`.mkdir()` creates a new folder, and its `exist_ok=True` option quietly does nothing if the folder is already there, instead of raising an error.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X3dvcmtpbmdfd2l0aF9maWxlX3BhdGhzX3VzaW5nX3BhdGhsaWIgY29kZSA3IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA3LnB5IiwiY29kZSI6ImZyb20gcGF0aGxpYiBpbXBvcnQgUGF0aFxuXG5QYXRoKFwicmVwb3J0c1wiKS5ta2RpcihleGlzdF9vaz1UcnVlKSJ9"
 width="100%"
></iframe>

## pathlib at a Glance

| Tool | What It Does |
|---|---|
| `Path("folder/file.txt")` | Wraps a location as a path object |
| `folder / "file.txt"` | Joins path pieces, correctly, for any operating system |
| `.exists()` | Checks whether the path is actually there |
| `.read_text()` / `.write_text()` | Reads or writes an entire file's text directly |
| `.name`, `.stem`, `.suffix`, `.parent` | Read parts of the path without manual string splitting |
| `.mkdir(exist_ok=True)` | Creates a folder, safely, even if it already exists |

## Your Turn: Build a Reports Folder Safely

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X3dvcmtpbmdfd2l0aF9maWxlX3BhdGhzX3VzaW5nX3BhdGhsaWIgY29kZSA4IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA4LnB5IiwiY29kZSI6ImZyb20gcGF0aGxpYiBpbXBvcnQgUGF0aFxuXG5yZXBvcnRzX2ZvbGRlciA9IFBhdGgoXCJyZXBvcnRzXCIpXG5yZXBvcnRzX2ZvbGRlci5ta2RpcihleGlzdF9vaz1UcnVlKVxuXG5yZXBvcnRfZmlsZSA9IHJlcG9ydHNfZm9sZGVyIC8gXCJkYXkxX3NhbGVzLnR4dFwiXG5yZXBvcnRfZmlsZS53cml0ZV90ZXh0KFwiVG90YWwgc2FsZXM6IDQ1MDBcXG5cIilcblxucHJpbnQocmVwb3J0X2ZpbGUuZXhpc3RzKCkpICAgICAjIFRydWVcbnByaW50KHJlcG9ydF9maWxlLnJlYWRfdGV4dCgpKSAgIyBUb3RhbCBzYWxlczogNDUwMCJ9"
 width="100%"
></iframe>

Notice the folder and the file inside it were both built using the same `/` joining style, with no manually typed slash anywhere in the whole script.

## Conclusion

`pathlib`'s `Path` represents a file location as a proper object rather than a fragile string, joined correctly across operating systems with the `/` operator, and capable of checking existence, reading and writing text directly, inspecting its own name and extension, and creating folders safely. Prefer `Path` over manual string concatenation for any path your code builds itself. With reliable paths in hand, the next lesson covers finding files that match a pattern, such as every sales file for the fest, without knowing their exact names in advance.
