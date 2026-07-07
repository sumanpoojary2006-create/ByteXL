## Introduction

Nadia's catalog export script runs fine on her MacBook but fails on the Windows server in the consortium's office. The path separator is wrong: `"data/catalogs/branch_1.csv"` uses a forward slash that Windows does not accept in certain contexts. Her script also hard-codes `"/home/nadia/data"` as the working directory, which does not exist on the server.

The fix is to stop constructing file paths as strings and start using Python's path objects, which handle separators, relative vs absolute paths, and home-directory expansion automatically.

![Two paths shown side by side: a fragile string path built with + and "/" operators, and a safe pathlib.Path built with / operator, annotated with methods: .exists(), .mkdir(), .glob()](images/07_os_sys_pathlib.png)

## pathlib.Path: The Modern Way

`pathlib.Path` represents a file system path as an object. The `/` operator joins path segments, automatically using the correct separator for the platform.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X29zX3N5c19wYXRobGliIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGhcblxuIyBCdWlsZCBhIHBhdGggd2l0aG91dCBjYXJpbmcgYWJvdXQgT1Mgc2VwYXJhdG9yc1xuZGF0YV9kaXIgPSBQYXRoKFwiZGF0YVwiKSAvIFwiY2F0YWxvZ3NcIiAvIFwiMjAyNlwiXG5wcmludChkYXRhX2RpcikgICAgICAgICAjIGRhdGEvY2F0YWxvZ3MvMjAyNiAgKExpbnV4L01hYylcbiAgICAgICAgICAgICAgICAgICAgICAgICMgZGF0YVxcY2F0YWxvZ3NcXDIwMjYgICAoV2luZG93cylcblxuIyBJbnNwZWN0IGEgcGF0aFxucGF0aCA9IFBhdGgoXCIvVXNlcnMvbmFkaWEvZGF0YS9jYXRhbG9nLmNzdlwiKVxucHJpbnQocGF0aC5uYW1lKSAgICAgICAgIyAnY2F0YWxvZy5jc3YnXG5wcmludChwYXRoLnN0ZW0pICAgICAgICAjICdjYXRhbG9nJ1xucHJpbnQocGF0aC5zdWZmaXgpICAgICAgIyAnLmNzdidcbnByaW50KHBhdGgucGFyZW50KSAgICAgICMgL1VzZXJzL25hZGlhL2RhdGFcblxuIyBDaGVjayBleGlzdGVuY2VcbnByaW50KHBhdGguZXhpc3RzKCkpICAgICMgVHJ1ZSBvciBGYWxzZVxucHJpbnQocGF0aC5pc19maWxlKCkpICAgIyBUcnVlIGlmIGl0IGlzIGEgZmlsZVxucHJpbnQocGF0aC5pc19kaXIoKSkgICAgIyBUcnVlIGlmIGl0IGlzIGEgZGlyZWN0b3J5In0"
 width="100%"
></iframe>

## Creating and Walking Directories

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X29zX3N5c19wYXRobGliIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGhcblxub3V0cHV0X2RpciA9IFBhdGgoXCJleHBvcnRzXCIpIC8gXCIyMDI2XCIgLyBcImp1bHlcIlxub3V0cHV0X2Rpci5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpXG4jIGNyZWF0ZXMgYWxsIGludGVybWVkaWF0ZSBkaXJlY3Rvcmllczsgbm8gZXJyb3IgaWYgYWxyZWFkeSBleGlzdHNcblxuIyBXcml0ZSBhIGZpbGUgaW50byB0aGUgZGlyZWN0b3J5OlxuY2F0YWxvZ19maWxlID0gb3V0cHV0X2RpciAvIFwiYnJhbmNoXzEuY3N2XCJcbmNhdGFsb2dfZmlsZS53cml0ZV90ZXh0KFwiaXNibix0aXRsZVxcbjk3OC0wMDEsRHVuZVxcblwiKVxuXG4jIFJlYWQgaXQgYmFjazpcbnByaW50KGNhdGFsb2dfZmlsZS5yZWFkX3RleHQoKSkifQ"
 width="100%"
></iframe>

`mkdir(parents=True, exist_ok=True)` is the safe combination: `parents=True` creates all missing parent directories, `exist_ok=True` avoids an error if the directory already exists.

## Globbing: Find Files by Pattern

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X29zX3N5c19wYXRobGliIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGhcblxuZGF0YV9kaXIgPSBQYXRoKFwiZXhwb3J0c1wiKVxuXG4jIEZpbmQgYWxsIENTViBmaWxlcyByZWN1cnNpdmVseTpcbmNzdl9maWxlcyA9IGxpc3QoZGF0YV9kaXIucmdsb2IoXCIqLmNzdlwiKSlcbmZvciBmIGluIGNzdl9maWxlczpcbiAgICBwcmludChmKVxuXG4jIEZpbmQgYWxsIGZpbGVzIGluIHRoZSBpbW1lZGlhdGUgZGlyZWN0b3J5IG9ubHk6XG5qc29uX2ZpbGVzID0gbGlzdChkYXRhX2Rpci5nbG9iKFwiKi5qc29uXCIpKSJ9"
 width="100%"
></iframe>

`rglob` is "recursive glob" -- it searches the directory and all subdirectories.

## os and os.path

`os` provides lower-level system operations. `pathlib` replaces most of `os.path`, but some `os` operations have no pathlib equivalent:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X29zX3N5c19wYXRobGliIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJpbXBvcnQgb3NcblxuIyBFbnZpcm9ubWVudCB2YXJpYWJsZXNcbmhvbWUgPSBvcy5lbnZpcm9uLmdldChcIkhPTUVcIiwgXCIvdG1wXCIpICAgIyBzYWZlOiByZXR1cm5zIGRlZmF1bHQgaWYgbWlzc2luZ1xuYXBpX2tleSA9IG9zLmVudmlyb25bXCJMSUJSQVJZX0FQSV9LRVlcIl0gICMgcmFpc2VzIEtleUVycm9yIGlmIG1pc3NpbmdcblxuIyBDdXJyZW50IHdvcmtpbmcgZGlyZWN0b3J5XG5wcmludChvcy5nZXRjd2QoKSlcblxuIyBMaXN0IGRpcmVjdG9yeSBjb250ZW50cyAocmV0dXJucyBzdHJpbmdzKVxuZmlsZXMgPSBvcy5saXN0ZGlyKFwiLlwiKVxucHJpbnQoZmlsZXMpXG5cbiMgUmVtb3ZlIGEgZmlsZVxub3MucmVtb3ZlKFwib2xkX2NhdGFsb2cudHh0XCIpXG5cbiMgUmVtb3ZlIGFuIGVtcHR5IGRpcmVjdG9yeVxub3Mucm1kaXIoXCJlbXB0eV9kaXJcIilcblxuIyBXYWxrIGEgZGlyZWN0b3J5IHRyZWUgKHlpZWxkcyBkaXJwYXRoLCBkaXJuYW1lcywgZmlsZW5hbWVzKVxuZm9yIGRpcnBhdGgsIGRpcm5hbWVzLCBmaWxlbmFtZXMgaW4gb3Mud2FsayhcImV4cG9ydHNcIik6XG4gICAgZm9yIGZpbGVuYW1lIGluIGZpbGVuYW1lczpcbiAgICAgICAgcHJpbnQob3MucGF0aC5qb2luKGRpcnBhdGgsIGZpbGVuYW1lKSkifQ"
 width="100%"
></iframe>

## sys: Process-Level Information

`sys` provides access to the Python interpreter itself:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X29zX3N5c19wYXRobGliIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJpbXBvcnQgc3lzXG5cbnByaW50KHN5cy52ZXJzaW9uKSAgICAgICAgICMgUHl0aG9uIHZlcnNpb24gc3RyaW5nXG5wcmludChzeXMucGxhdGZvcm0pICAgICAgICAjICdkYXJ3aW4nLCAnbGludXgnLCAnd2luMzInXG5wcmludChzeXMuZXhlY3V0YWJsZSkgICAgICAjIHBhdGggdG8gdGhlIFB5dGhvbiBiaW5hcnlcbnByaW50KHN5cy5hcmd2KSAgICAgICAgICAgICMgY29tbWFuZC1saW5lIGFyZ3VtZW50c1xucHJpbnQoc3lzLnBhdGgpICAgICAgICAgICAgIyBtb2R1bGUgc2VhcmNoIHBhdGhcblxuIyBFeGl0IHRoZSBwcm9ncmFtOlxuaWYgbm90IGNvbmZpZ19maWxlLmV4aXN0cygpOlxuICAgIHByaW50KFwiQ29uZmlnIGZpbGUgbWlzc2luZ1wiLCBmaWxlPXN5cy5zdGRlcnIpXG4gICAgc3lzLmV4aXQoMSkgICAjIGV4aXQgd2l0aCBlcnJvciBjb2RlIDEifQ"
 width="100%"
></iframe>

`sys.stderr` is the standard error stream. Writing error messages there, rather than to `sys.stdout`, allows shell pipelines to separate output from errors.

## Combining os, sys, and pathlib

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X29zX3N5c19wYXRobGliIGNvZGUgNiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNi5weSIsImNvZGUiOiJpbXBvcnQgb3NcbmltcG9ydCBzeXNcbmZyb20gcGF0aGxpYiBpbXBvcnQgUGF0aFxuXG5kZWYgZ2V0X2RhdGFfZGlyKCkgLT4gUGF0aDpcbiAgICBcIlwiXCJSZXR1cm4gdGhlIGRhdGEgZGlyZWN0b3J5LCBjcmVhdGluZyBpdCBpZiBuZWVkZWQuXCJcIlwiXG4gICAgYmFzZSA9IFBhdGgob3MuZW52aXJvbi5nZXQoXCJMSUJSQVJZX0RBVEFfRElSXCIsIFwiLlwiKSlcbiAgICBkYXRhX2RpciA9IGJhc2UgLyBcImRhdGFcIiAvIFwiY2F0YWxvZ3NcIlxuICAgIGRhdGFfZGlyLm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSlcbiAgICByZXR1cm4gZGF0YV9kaXJcblxuZGVmIHByb2Nlc3NfYWxsX2NhdGFsb2dzKCk6XG4gICAgZGF0YV9kaXIgPSBnZXRfZGF0YV9kaXIoKVxuICAgIGNzdl9maWxlcyA9IGxpc3QoZGF0YV9kaXIucmdsb2IoXCIqLmNzdlwiKSlcbiAgICBpZiBub3QgY3N2X2ZpbGVzOlxuICAgICAgICBwcmludChmXCJObyBjYXRhbG9ncyBmb3VuZCBpbiB7ZGF0YV9kaXJ9XCIsIGZpbGU9c3lzLnN0ZGVycilcbiAgICAgICAgc3lzLmV4aXQoMSlcbiAgICBmb3IgZiBpbiBjc3ZfZmlsZXM6XG4gICAgICAgIHByaW50KGZcIlByb2Nlc3Npbmc6IHtmfVwiKVxuICAgICAgICBjb250ZW50ID0gZi5yZWFkX3RleHQoKVxuICAgICAgICAjIC4uLiBwcm9jZXNzIGNvbnRlbnQifQ"
 width="100%"
></iframe>

## os / sys / pathlib at a Glance

| Tool | When to use |
|---|---|
| `Path("/a") / "b"` | Build cross-platform paths |
| `path.exists()`, `.is_file()`, `.is_dir()` | Check path state |
| `path.mkdir(parents=True, exist_ok=True)` | Create directories safely |
| `path.rglob("*.csv")` | Find files by pattern recursively |
| `path.read_text()`, `.write_text()` | Simple file I/O |
| `os.environ.get("KEY", default)` | Read environment variables |
| `os.walk(dir)` | Recursively iterate directory tree |
| `sys.argv` | Command-line arguments |
| `sys.exit(code)` | Exit with a status code |
| `sys.stderr` | Write error messages |

## Your Turn

Write a function `find_catalogs(base_dir, since_date)` that walks a directory tree looking for CSV files whose names start with a date stamp (`YYYY-MM-DD_catalog.csv`) and returns only those whose date is on or after `since_date`:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X29zX3N5c19wYXRobGliIGNvZGUgNyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNy5weSIsImNvZGUiOiJmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGhcbmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGVcblxuZGVmIGZpbmRfY2F0YWxvZ3MoYmFzZV9kaXIsIHNpbmNlX2RhdGUpOlxuICAgIGJhc2UgPSBQYXRoKGJhc2VfZGlyKVxuICAgIHJlc3VsdCA9IFtdXG4gICAgZm9yIGYgaW4gYmFzZS5yZ2xvYihcIipfY2F0YWxvZy5jc3ZcIik6XG4gICAgICAgIHRyeTpcbiAgICAgICAgICAgIGRhdGVfcGFydCA9IGYuc3RlbS5zcGxpdChcIl9cIilbMF0gICAjIGUuZy4gJzIwMjYtMDctMDEnXG4gICAgICAgICAgICBmaWxlX2RhdGUgPSBkYXRlLmZyb21pc29mb3JtYXQoZGF0ZV9wYXJ0KVxuICAgICAgICAgICAgaWYgZmlsZV9kYXRlID49IHNpbmNlX2RhdGU6XG4gICAgICAgICAgICAgICAgcmVzdWx0LmFwcGVuZChmKVxuICAgICAgICBleGNlcHQgVmFsdWVFcnJvcjpcbiAgICAgICAgICAgIGNvbnRpbnVlICAgIyBza2lwIGZpbGVzIHRoYXQgZG9uJ3QgbWF0Y2ggdGhlIHBhdHRlcm5cbiAgICByZXR1cm4gc29ydGVkKHJlc3VsdCkifQ"
 width="100%"
></iframe>

## Conclusion

`pathlib.Path` is the modern way to handle file paths in Python: cross-platform, readable, and rich with methods for existence checks, globbing, and I/O. `os` fills the gaps where pathlib has no equivalent (environment variables, `os.walk`). `sys` gives access to the interpreter and process-level operations. The next lesson wraps up the standard library unit with `json` and `csv`, the two formats Nadia uses to exchange data with every other system in the consortium.
