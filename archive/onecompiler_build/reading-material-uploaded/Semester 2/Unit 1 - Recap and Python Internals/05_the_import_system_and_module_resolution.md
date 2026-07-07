## Introduction

Asel types `from catalog import Book` and Python finds the right file. She has done this so often it feels as automatic as breathing, but Rahul asks her to describe exactly what Python does between reading that line and making `Book` available in her code. She realizes she cannot.

Understanding the import system is not an academic exercise: it explains why two files with the same name do not always import the same module, why circular imports sometimes fail, why installing a package with `pip` makes it importable everywhere, and how frameworks like Flask and Django hook into your project layout. This lesson covers how Python finds what you ask it to import.

![](images/05_import_system_module_resolution.png)

## What import Actually Does

When Python encounters `import math`, it does not simply read a file. It follows a sequence of steps:

1. Check `sys.modules` (the module cache) for a previously-imported module with that name.
2. If found, return it immediately without reading anything from disk.
3. If not found, search for the module using a series of **finders** registered in `sys.meta_path`.
4. The matching finder returns a **loader** that reads and executes the module source.
5. The resulting module object is stored in `sys.modules` before the caller receives it.

The module cache in step 1 is why importing the same module twice is fast: the second call returns the already-built object without any disk access or compilation.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-1-recap-and-python-internals-05-the-import-system-and-module-r-001-808ccabbf0.html"
 width="100%"
></iframe>

## The Three Kinds of Modules Python Searches For

Python searches for a module in one of three places, in order:

**Built-in modules** are compiled directly into the CPython binary. `sys`, `builtins`, and a handful of others live here. They do not have source files at all.

**Frozen modules** are modules whose bytecode is frozen into the CPython binary at build time. The `importlib` bootstrap code uses this mechanism.

**Path-based modules** are the ones you work with almost exclusively: `.py` files found on the file system using the list of directories in `sys.path`. This is where your own code lives, where third-party packages installed by `pip` live, and where the standard library lives.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-1-recap-and-python-internals-05-the-import-system-and-module-r-002-fed07e5885.html"
 width="100%"
></iframe>

## The Module Object and What Happens When Code Runs

When Python finds a module file and loads it, it creates a `module` object, stores it in `sys.modules`, and then *executes the module's top-level code*. This is an important point: any code at the top level of a module (not inside a function or class) runs at import time, exactly once.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-1-recap-and-python-internals-05-the-import-system-and-module-r-003-8b149c7c6c.html"
 width="100%"
></iframe>

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-1-recap-and-python-internals-05-the-import-system-and-module-r-004-06b9565abb.html"
 width="100%"
></iframe>

This behavior is why expensive setup code (opening a database connection, loading a large file) is better placed inside a function rather than at module level, and why circular imports can cause partially-initialized modules to be returned.

## Relative vs. Absolute Imports

When your project has multiple files, Python supports two import styles:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-1-recap-and-python-internals-05-the-import-system-and-module-r-005-5276d4af94.html"
 width="100%"
></iframe>

Absolute imports are clearer and work from anywhere. Relative imports are useful inside a package when you want to avoid repeating the top-level package name everywhere, but they only work in files that are part of a package (inside a folder with an `__init__.py`).

## The Import System at a Glance

| Step | What happens |
|---|---|
| Check `sys.modules` | Return cached module if already imported |
| Find the module | Search built-ins, frozen modules, then `sys.path` directories |
| Load the module | Read, compile, and execute top-level code |
| Cache the result | Store in `sys.modules` for future imports |
| Return to caller | Bind the name in the importing namespace |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-1-recap-and-python-internals-05-the-import-system-and-module-r-006-50dccfbb42.html"
 width="100%"
></iframe>

Run this and confirm the two `json` references are identical objects. Then look up `sys.modules` to see which standard library modules Python has already imported by the time your script starts running. You will find more than you expect, because the interpreter's own startup imports several modules.

## Conclusion

Every `import` statement triggers a cache check, a module search, top-level code execution, and storage in `sys.modules`. Knowing these steps explains why the second import of a module is instantaneous, why top-level code in a module should be kept cheap, and why circular imports can silently return an incomplete module. The next lesson focuses on the most tunable part of this system: `sys.path`, the list of directories Python searches, and how to control what it finds.
