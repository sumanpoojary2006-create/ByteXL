## Introduction

Asel runs the internship project from the terminal and everything imports fine. Then she copies one file to a different folder and runs it there, and the same `import` statement crashes with a `ModuleNotFoundError`. Nothing in her code changed. She has hit the `sys.path` problem for the first time, and it is one of the most common sources of confusion for developers moving from small scripts to real projects.

This lesson explains what `sys.path` is, how Python populates it when a script starts, and the correct ways to make your modules findable without breaking other things.

![](images/06_syspath_and_imports.png)

## What sys.path Is

`sys.path` is an ordinary Python list of strings. Each string is a directory. When Python needs to find a module by path-based lookup, it searches these directories in order and uses the first match it finds.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-1-recap-and-python-internals-06-syspath-and-how-imports-are-fo-001-45c5d5dd66.html"
 width="100%"
></iframe>

A typical output looks like:

```
/home/asel/internship        # the directory of the running script
/usr/lib/python311.zip       # (usually empty, a legacy entry)
/usr/lib/python3.11          # the standard library
/usr/lib/python3.11/lib-dynload
/home/asel/.venv/lib/python3.11/site-packages   # installed packages
```

The ordering is significant: the first matching directory wins. If you have a local file called `random.py` and you import `random`, Python will find your file before the standard library's `random` module. This is called **shadowing**, and it is almost always a bug.

## How Python Builds sys.path at Startup

Python builds `sys.path` from three sources, in this order:

1. **The script's own directory** (or `""` for an empty string, representing the current working directory) is prepended automatically. This is why importing a file in the same directory as your script usually works without any configuration.

2. **The `PYTHONPATH` environment variable**, if set, lists additional directories that are inserted after the script's directory.

3. **Installation defaults**: the standard library and site-packages directories for the active Python environment are appended during interpreter startup.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-1-recap-and-python-internals-06-syspath-and-how-imports-are-fo-002-70d49ab9b2.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-1-recap-and-python-internals-06-syspath-and-how-imports-are-fo-003-cca3d65ae0.html"
 width="100%"
></iframe>

## Diagnosing a ModuleNotFoundError

When a `ModuleNotFoundError` appears, the debugging process is always the same: print `sys.path` and check whether the directory containing the module is in the list.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-1-recap-and-python-internals-06-syspath-and-how-imports-are-fo-004-d274d162fc.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-1-recap-and-python-internals-06-syspath-and-how-imports-are-fo-005-ac15c2dee5.html"
 width="100%"
></iframe>

Run this from two different directories and compare the output. Notice that the first entry changes (it tracks the script's location or the current working directory). Then create a file called `greet.py` in a subdirectory and try to import it without modifying `sys.path`. Confirm the `ModuleNotFoundError`, then re-run with `PYTHONPATH=./subdirectory python main.py` and confirm it succeeds.

## Conclusion

`sys.path` is the list Python searches to find modules, built automatically from the script's location, the `PYTHONPATH` environment variable, and installation defaults. The correct long-term solution for making your modules findable is to structure and install them as a proper package rather than appending to `sys.path` in code. The next lesson widens the view from individual files to entire frameworks: what extra files Flask and FastAPI generate and why, and what it means when a framework tells you to run it with a specific command rather than directly with Python.
