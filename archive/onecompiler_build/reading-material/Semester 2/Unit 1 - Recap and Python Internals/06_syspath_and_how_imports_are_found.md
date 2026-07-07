## Introduction

Asel runs the internship project from the terminal and everything imports fine. Then she copies one file to a different folder and runs it there, and the same `import` statement crashes with a `ModuleNotFoundError`. Nothing in her code changed. She has hit the `sys.path` problem for the first time, and it is one of the most common sources of confusion for developers moving from small scripts to real projects.

This lesson explains what `sys.path` is, how Python populates it when a script starts, and the correct ways to make your modules findable without breaking other things.

![](images/06_syspath_and_imports.png)

## What sys.path Is

`sys.path` is an ordinary Python list of strings. Each string is a directory. When Python needs to find a module by path-based lookup, it searches these directories in order and uses the first match it finds.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3N5c3BhdGhfYW5kX2hvd19pbXBvcnRzX2FyZV9mb3VuZCBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoiaW1wb3J0IHN5c1xuXG5mb3IgZW50cnkgaW4gc3lzLnBhdGg6XG4gICAgcHJpbnQoZW50cnkpIn0"
 width="100%"
></iframe>

A typical output looks like:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3N5c3BhdGhfYW5kX2hvd19pbXBvcnRzX2FyZV9mb3VuZCBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoiL2hvbWUvYXNlbC9pbnRlcm5zaGlwICAgICAgICAjIHRoZSBkaXJlY3Rvcnkgb2YgdGhlIHJ1bm5pbmcgc2NyaXB0XG4vdXNyL2xpYi9weXRob24zMTEuemlwICAgICAgICMgKHVzdWFsbHkgZW1wdHksIGEgbGVnYWN5IGVudHJ5KVxuL3Vzci9saWIvcHl0aG9uMy4xMSAgICAgICAgICAjIHRoZSBzdGFuZGFyZCBsaWJyYXJ5XG4vdXNyL2xpYi9weXRob24zLjExL2xpYi1keW5sb2FkXG4vaG9tZS9hc2VsLy52ZW52L2xpYi9weXRob24zLjExL3NpdGUtcGFja2FnZXMgICAjIGluc3RhbGxlZCBwYWNrYWdlcyJ9"
 width="100%"
></iframe>

The ordering is significant: the first matching directory wins. If you have a local file called `random.py` and you import `random`, Python will find your file before the standard library's `random` module. This is called **shadowing**, and it is almost always a bug.

## How Python Builds sys.path at Startup

Python builds `sys.path` from three sources, in this order:

1. **The script's own directory** (or `""` for an empty string, representing the current working directory) is prepended automatically. This is why importing a file in the same directory as your script usually works without any configuration.

2. **The `PYTHONPATH` environment variable**, if set, lists additional directories that are inserted after the script's directory.

3. **Installation defaults**: the standard library and site-packages directories for the active Python environment are appended during interpreter startup.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3N5c3BhdGhfYW5kX2hvd19pbXBvcnRzX2FyZV9mb3VuZCBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoiaW1wb3J0IHN5c1xuXG4jIFByaW50IHRoZSBmaXJzdCBlbnRyeSAtLSB1c3VhbGx5IHRoZSBzY3JpcHQgZGlyZWN0b3J5XG5wcmludChzeXMucGF0aFswXSlcblxuIyBTaG93IHdoYXQgUFlUSE9OUEFUSCBjb250cmlidXRlcyAoaWYgc2V0KVxuaW1wb3J0IG9zXG5wcmludChvcy5lbnZpcm9uLmdldChcIlBZVEhPTlBBVEhcIiwgXCJub3Qgc2V0XCIpKSJ9"
 width="100%"
></iframe>

## The Right Way to Make Your Modules Findable

There are three correct approaches for production code, and one that is tempting but should be avoided.

**Use a virtual environment and install your package.** This is the best approach for anything beyond a quick experiment. When your project has a `pyproject.toml` (covered in Unit 14), you can install it into a virtual environment with `pip install -e .`, after which it is importable from anywhere without touching `sys.path` at all.

**Use the PYTHONPATH environment variable** for development, not production. Setting `PYTHONPATH=/path/to/my/project python main.py` adds your project root to the search path for that single invocation. It is fine for local development but should not appear in deployment configuration.

**Structure your code as a package** (a directory with `__init__.py`). Python finds packages the same way it finds modules: by searching `sys.path` for a directory with that name.

**Do not append to sys.path in code** in any file that other people will import. Doing so has side effects that persist for the entire lifetime of the interpreter process, and it makes your code's behavior depend on where it was run from.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3N5c3BhdGhfYW5kX2hvd19pbXBvcnRzX2FyZV9mb3VuZCBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoiIyBBdm9pZCB0aGlzIHBhdHRlcm4gaW4gbGlicmFyeSBjb2RlOlxuaW1wb3J0IHN5c1xuc3lzLnBhdGguYXBwZW5kKFwiL3NvbWUvYWJzb2x1dGUvcGF0aFwiKSAgICMgZnJhZ2lsZSwgbm9uLXBvcnRhYmxlXG5cbiMgUHJlZmVyIGluc3RlYWQ6IGluc3RhbGwgdGhlIHBhY2thZ2UsIG9yIHVzZSBQWVRIT05QQVRIIn0"
 width="100%"
></iframe>

## Diagnosing a ModuleNotFoundError

When a `ModuleNotFoundError` appears, the debugging process is always the same: print `sys.path` and check whether the directory containing the module is in the list.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3N5c3BhdGhfYW5kX2hvd19pbXBvcnRzX2FyZV9mb3VuZCBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoiaW1wb3J0IHN5c1xuXG50cnk6XG4gICAgaW1wb3J0IG15X2xpYnJhcnlcbmV4Y2VwdCBNb2R1bGVOb3RGb3VuZEVycm9yOlxuICAgIHByaW50KFwiU2VhcmNoIHBhdGggd2FzOlwiKVxuICAgIGZvciBwIGluIHN5cy5wYXRoOlxuICAgICAgICBwcmludChcIiBcIiwgcClcbiAgICBwcmludChcIm15X2xpYnJhcnkgd2FzIG5vdCBmb3VuZCBpbiBhbnkgb2YgdGhlIGFib3ZlLlwiKSJ9"
 width="100%"
></iframe>

Nine times out of ten, the directory you expected to be there is missing, either because you ran the script from the wrong working directory, or because the virtual environment was not activated.

## sys.path at a Glance

| Source | When it is added |
|---|---|
| Script directory | Always, as the first entry (`""` or the actual path) |
| `PYTHONPATH` | If the environment variable is set |
| Standard library | Added by interpreter startup |
| `site-packages` | Added by the `site` module at startup |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3N5c3BhdGhfYW5kX2hvd19pbXBvcnRzX2FyZV9mb3VuZCBjb2RlIDYiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDYucHkiLCJjb2RlIjoiaW1wb3J0IHN5c1xuXG5wcmludChcInN5cy5wYXRoIGVudHJpZXM6XCIpXG5mb3IgaSwgcCBpbiBlbnVtZXJhdGUoc3lzLnBhdGgpOlxuICAgIHByaW50KGZcIiAgW3tpfV0ge3B9XCIpIn0"
 width="100%"
></iframe>

Run this from two different directories and compare the output. Notice that the first entry changes (it tracks the script's location or the current working directory). Then create a file called `greet.py` in a subdirectory and try to import it without modifying `sys.path`. Confirm the `ModuleNotFoundError`, then re-run with `PYTHONPATH=./subdirectory python main.py` and confirm it succeeds.

## Conclusion

`sys.path` is the list Python searches to find modules, built automatically from the script's location, the `PYTHONPATH` environment variable, and installation defaults. The correct long-term solution for making your modules findable is to structure and install them as a proper package rather than appending to `sys.path` in code. The next lesson widens the view from individual files to entire frameworks: what extra files Flask and FastAPI generate and why, and what it means when a framework tells you to run it with a specific command rather than directly with Python.
