## Introduction

Tara has just written a full class-based context manager. It works perfectly, but she notices it is twelve lines of boilerplate for a straightforward open-then-close pattern. She wonders if Python has a shorter way to write context managers for cases where the setup and teardown fit naturally in a single function.

Python does. The `contextlib` module includes a decorator called `@contextmanager` that lets you write a context manager using a generator function with a single `yield`. No class required.

![A before and after: a class with __enter__ and __exit__ on the left, a generator function with yield on the right, both producing identical behavior](images/04_contextlib_contextmanager.png)

## @contextmanager: the Generator Shortcut

`@contextmanager` turns a generator function into a context manager. The code before `yield` runs as `__enter__`, the yielded value becomes the `as` target, and the code after `yield` runs as `__exit__`.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-6-context-managers-04-contextlib-and-contextmanager-001-1abda25e2c.html"
 width="100%"
></iframe>

The `try`/`finally` around `yield` is what makes the cleanup unconditional. If an exception is raised inside the `with` block, it is thrown *into* the generator at the `yield` point, the `finally` runs, and the exception propagates.

## Handling Exceptions in @contextmanager

When an exception occurs inside the `with` block, `@contextmanager` re-raises it at the `yield` point inside the generator. Wrapping `yield` in `try`/`except` lets you catch and respond to it, exactly like `__exit__`'s exception arguments.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-6-context-managers-04-contextlib-and-contextmanager-002-72eac5f132.html"
 width="100%"
></iframe>

## When to Use @contextmanager vs a Class

Both approaches implement the same protocol. The choice is stylistic:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-6-context-managers-04-contextlib-and-contextmanager-003-c22bdade6d.html"
 width="100%"
></iframe>

Use `@contextmanager` when the context manager is a single function with a clear before/after pattern. Use a class when the context manager needs multiple helper methods, stores complex state, or wraps a reusable object that already has a lifecycle.

## Other Useful contextlib Tools

`contextlib` provides several ready-made context managers:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-6-context-managers-04-contextlib-and-contextmanager-004-0dc6469678.html"
 width="100%"
></iframe>

`suppress` is covered in more depth in the next lesson.

## contextlib at a Glance

| Tool | What it does |
|---|---|
| `@contextmanager` | Generator shortcut for writing context managers |
| `suppress(ExcType)` | Silently swallow specific exceptions |
| `nullcontext()` | A no-op context manager for optional wrapping |
| `ExitStack` | Dynamically register and compose context managers |

## Your Turn

Rewrite the `TempDirectory` class from the previous lesson as a `@contextmanager` function:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-6-context-managers-04-contextlib-and-contextmanager-005-a3252f44b1.html"
 width="100%"
></iframe>

Run it and confirm the output matches the class-based version. Then add exception handling: inside the `with temp_directory()` block, raise an exception and confirm the directory is still removed.

## Conclusion

`@contextmanager` converts a generator function into a context manager: code before `yield` is setup, the yielded value is the `as` target, and code after `yield` (typically in a `finally`) is teardown. It is the preferred approach for straightforward resource-management patterns. The next lesson covers safe resource management in depth: the patterns that prevent leaks even in the presence of unexpected exceptions and nested resources.
