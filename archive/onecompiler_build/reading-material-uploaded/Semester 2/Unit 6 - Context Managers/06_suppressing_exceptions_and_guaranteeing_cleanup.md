## Introduction

Tara's library system runs a background task that exports a daily catalog backup. If the backup fails because the output directory is not mounted, she wants to log the error and continue, rather than crashing the whole service. She knows that her context manager's `__exit__` returns `False`, which propagates exceptions. Now she needs to understand exactly how to suppress specific exceptions, when doing so is safe, and when it is dangerous.

This final lesson in the unit covers exception suppression, the `contextlib.suppress` shortcut, and the guarantee that cleanup code runs even in the worst cases.

![A diagram showing two exit paths from __exit__: return False leading to the exception propagating up the call stack, and return True leading to exception suppressed and execution continuing normally after the with block](images/06_suppressing_exceptions.png)

## Suppressing an Exception in __exit__

When `__exit__` returns `True`, the exception is silently swallowed and the program continues after the `with` block as if nothing happened.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-6-context-managers-06-suppressing-exceptions-and-guaranteeing-001-252cffe93b.html"
 width="100%"
></iframe>

Suppression is selective: only `FileNotFoundError` is absorbed. Any other exception propagates normally. This selectivity is essential -- a context manager that suppresses `Exception` broadly is almost always a mistake.

## contextlib.suppress: The Shortcut

`contextlib.suppress` is a built-in context manager that suppresses specific exception types without requiring you to write a class:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-6-context-managers-06-suppressing-exceptions-and-guaranteeing-002-f1a54f479d.html"
 width="100%"
></iframe>

`suppress` is equivalent to writing `except ExcType: pass` but makes the intent explicit and removes the need for an extra `try`/`except` block when the only response to the error is "move on."

## When Suppression Is Appropriate

Exception suppression should be used sparingly and intentionally. Before suppressing, ask three questions:

1. Is this error condition expected and normal in the intended use of the code?
2. Is continuing after this error safe, with no inconsistent state left behind?
3. Am I suppressing only the specific exception type I expect, not a broad base class?

If all three answers are yes, suppression may be appropriate:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-6-context-managers-06-suppressing-exceptions-and-guaranteeing-003-ea9018b48f.html"
 width="100%"
></iframe>

## Guaranteeing Cleanup in Edge Cases

Context managers guarantee cleanup in situations that `try`/`except`/`finally` often gets wrong:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-6-context-managers-06-suppressing-exceptions-and-guaranteeing-004-b7e6810fe4.html"
 width="100%"
></iframe>

`__exit__` is called even when `SystemExit` or `KeyboardInterrupt` is raised, because these are `BaseException` subclasses and the `with` statement does not filter them out. This makes context managers more reliable than manual `try`/`finally` for critical cleanup.

## Combining: Log, Suppress, Clean Up

Here is the pattern Tara uses for her daily backup task:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-6-context-managers-06-suppressing-exceptions-and-guaranteeing-005-1ad04494c6.html"
 width="100%"
></iframe>

The separation of concerns is clear: `safe_backup` handles logging, `suppress(OSError)` handles the "non-fatal failure" policy, and `export_catalog` handles the actual export.

## Suppressing Exceptions at a Glance

| Pattern | When to use |
|---|---|
| Return `True` from `__exit__` | Suppress exception in a class-based manager |
| `contextlib.suppress(ExcType)` | Suppress a specific exception in-place |
| `try`/`except` inside `@contextmanager` | Suppress/log and re-raise in a generator manager |
| Log then re-raise | Observe an exception without changing its propagation |

## Your Turn

Write a function `safe_remove_all(paths)` that attempts to delete each file in a list, suppresses `FileNotFoundError` for files that are already gone, logs a warning for `PermissionError`, and re-raises any other exception.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-6-context-managers-06-suppressing-exceptions-and-guaranteeing-006-85b4ece3d0.html"
 width="100%"
></iframe>

## Conclusion

Returning `True` from `__exit__` suppresses an exception; `contextlib.suppress` provides a clean one-liner for specific types. Suppression is safe when the error condition is expected, continuation is safe, and the suppression is narrow. Context managers guarantee cleanup even on `return`, `yield`, `SystemExit`, and `KeyboardInterrupt`, making them more reliable than manual `try`/`finally` for critical cleanup. Unit 7 moves from resource management to Python's standard library, exploring the built-in modules that solve common problems so you do not have to write them yourself.
