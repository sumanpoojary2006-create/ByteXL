## Introduction

Asel notices something odd in the project folder at the internship: a directory called `__pycache__` that nobody created and nobody seems to talk about. Inside it are files with names like `app.cpython-311.pyc`. She asks Rahul what they are. He tells her to guess first.

She figures they must be related to the compilation step from the previous lesson, since Python compiles to bytecode before running. She is right. This lesson explains exactly what `__pycache__` contains, why it exists, when Python uses it versus recompiling, and when you should care about it.

![](images/04_pycache_and_pyc_files.png)

## What a .pyc File Contains

When Python imports or runs a module for the first time, it saves the compiled bytecode to a `.pyc` file inside `__pycache__`. The filename encodes both the module name and the Python version:

```
__pycache__/
    catalog.cpython-311.pyc
    utils.cpython-311.pyc
```

The `.pyc` file has three parts: a **magic number** that encodes the Python version (so Python 3.11 will not accidentally use bytecode compiled by Python 3.10), a **timestamp** or hash of the original source file, and the **bytecode** itself in Python's `marshal` binary format.

The next time you run the program, Python checks whether the `.pyc` is still valid before recompiling.

## When Python Recompiles vs. Reuses

Python's validation logic is straightforward. If the `.pyc` file exists and its timestamp matches the source file's last-modified time (and the magic number matches the interpreter version), Python loads the bytecode directly, skipping the lex-parse-compile pipeline entirely. If anything has changed, Python recompiles and overwrites the `.pyc`.

You can verify this yourself:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-1-recap-and-python-internals-04-the-pycache-folder-and-pyc-fil-001-fb6332b338.html"
 width="100%"
></iframe>

The practical effect: the first `import` of a large module takes slightly longer because Python must compile it. Every subsequent import is fast because Python reads pre-compiled bytecode. For the tiny scripts you write during development this speedup is invisible, but for a framework like Django with thousands of modules, the `__pycache__` speedup is measurable.

## The Magic Number in Practice

The magic number matters more than it might seem. If you switch Python versions, the old `.pyc` files are not valid for the new interpreter. Python handles this automatically by including the version string in the filename (`cpython-311` vs `cpython-312`) so `.pyc` files for different versions coexist in `__pycache__` without conflict.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-1-recap-and-python-internals-04-the-pycache-folder-and-pyc-fil-002-af74fa6db6.html"
 width="100%"
></iframe>

You will never need to compute or check this manually; knowing it exists explains why changing your Python version does not break the cache silently.

## When __pycache__ Is Not Created

Python only creates `__pycache__` for *imported* modules. Running a script directly with `python script.py` does compile it to bytecode internally, but the bytecode is discarded rather than cached, because Python assumes a top-level script changes between runs more often than a library module does.

This distinction matters in practice: if you are trying to speed up a frequently-imported utility module, it will be cached. If you are trying to speed up a main entry point, it will not.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-1-recap-and-python-internals-04-the-pycache-folder-and-pyc-fil-003-80d6057301.html"
 width="100%"
></iframe>

## Should You Commit __pycache__ to Git?

No. The files are machine-specific, Python-version-specific, and fully reproducible by anyone who runs the project. The standard `.gitignore` for Python projects excludes `__pycache__/` and `*.pyc` for exactly this reason. If you ever delete `__pycache__` entirely, Python silently recreates it the next time the module is imported.

## __pycache__ at a Glance

| Fact | Detail |
|---|---|
| What `.pyc` contains | Magic number, source timestamp, compiled bytecode |
| Freshness check | Timestamp match + magic number match |
| When cache is skipped | Running a script directly (`python main.py`) |
| Version isolation | Python version encoded in the filename (`cpython-311`) |
| Version control | Exclude from git; it is auto-regenerated |

## Your Turn

Create a file called `greeting.py` with a single function:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-1-recap-and-python-internals-04-the-pycache-folder-and-pyc-fil-004-926cde49cc.html"
 width="100%"
></iframe>

Then open a Python REPL and run `import greeting`. Check that a `__pycache__` folder appeared. Modify `greeting.py` (change the string to `"Hi, {name}!"`), save it, and import again. Check the `.pyc` file's modification time to confirm it was regenerated.

## Conclusion

Python caches compiled bytecode in `__pycache__` to avoid recompiling unchanged modules on every run. The cache is validated by a magic number encoding the Python version and a timestamp matching the source file. It is created only for imported modules, not for scripts run directly, and it should be excluded from version control. The next lesson moves up one level: instead of asking "how is bytecode cached," it asks "how does Python decide which file to import in the first place," starting with the import system and module resolution.
