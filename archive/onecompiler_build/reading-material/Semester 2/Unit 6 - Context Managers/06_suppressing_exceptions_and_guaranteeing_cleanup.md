## Introduction

Tara's library system runs a background task that exports a daily catalog backup. If the backup fails because the output directory is not mounted, she wants to log the error and continue, rather than crashing the whole service. She knows that her context manager's `__exit__` returns `False`, which propagates exceptions. Now she needs to understand exactly how to suppress specific exceptions, when doing so is safe, and when it is dangerous.

This final lesson in the unit covers exception suppression, the `contextlib.suppress` shortcut, and the guarantee that cleanup code runs even in the worst cases.

![A diagram showing two exit paths from __exit__: return False leading to the exception propagating up the call stack, and return True leading to exception suppressed and execution continuing normally after the with block](images/06_suppressing_exceptions.png)

## Suppressing an Exception in __exit__

When `__exit__` returns `True`, the exception is silently swallowed and the program continues after the `with` block as if nothing happened.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3N1cHByZXNzaW5nX2V4Y2VwdGlvbnNfYW5kX2d1YXJhbnRlZWluZ19jbGVhbnVwIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJjbGFzcyBTdXBwcmVzc0ZpbGVFcnJvcjpcbiAgICBkZWYgX19lbnRlcl9fKHNlbGYpOlxuICAgICAgICByZXR1cm4gc2VsZlxuXG4gICAgZGVmIF9fZXhpdF9fKHNlbGYsIGV4Y190eXBlLCBleGNfdmFsLCBleGNfdGIpOlxuICAgICAgICBpZiBleGNfdHlwZSBpcyBGaWxlTm90Rm91bmRFcnJvcjpcbiAgICAgICAgICAgIHByaW50KGZcIlNraXBwaW5nIG1pc3NpbmcgZmlsZToge2V4Y192YWx9XCIpXG4gICAgICAgICAgICByZXR1cm4gVHJ1ZSAgICMgc3VwcHJlc3MgdGhpcyBleGNlcHRpb24gb25seVxuICAgICAgICByZXR1cm4gRmFsc2UgICAgICAgIyBwcm9wYWdhdGUgZXZlcnl0aGluZyBlbHNlXG5cbndpdGggU3VwcHJlc3NGaWxlRXJyb3IoKTpcbiAgICB3aXRoIG9wZW4oXCJtaXNzaW5nX2NhdGFsb2cudHh0XCIpIGFzIGY6XG4gICAgICAgIHByaW50KGYucmVhZCgpKVxuXG5wcmludChcIkNvbnRpbnVpbmcgYWZ0ZXIgdGhlIGVycm9yXCIpXG4jIE91dHB1dDpcbiMgU2tpcHBpbmcgbWlzc2luZyBmaWxlOiBbRXJybm8gMl0gTm8gc3VjaCBmaWxlIG9yIGRpcmVjdG9yeTogJ21pc3NpbmdfY2F0YWxvZy50eHQnXG4jIENvbnRpbnVpbmcgYWZ0ZXIgdGhlIGVycm9yIn0"
 width="100%"
></iframe>

Suppression is selective: only `FileNotFoundError` is absorbed. Any other exception propagates normally. This selectivity is essential -- a context manager that suppresses `Exception` broadly is almost always a mistake.

## contextlib.suppress: The Shortcut

`contextlib.suppress` is a built-in context manager that suppresses specific exception types without requiring you to write a class:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3N1cHByZXNzaW5nX2V4Y2VwdGlvbnNfYW5kX2d1YXJhbnRlZWluZ19jbGVhbnVwIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJpbXBvcnQgb3NcbmZyb20gY29udGV4dGxpYiBpbXBvcnQgc3VwcHJlc3NcblxuIyBSZW1vdmUgYSBmaWxlLCBxdWlldGx5IGlmIGl0IGRvZXMgbm90IGV4aXN0XG53aXRoIHN1cHByZXNzKEZpbGVOb3RGb3VuZEVycm9yKTpcbiAgICBvcy5yZW1vdmUoXCJvbGRfY2F0YWxvZy50eHRcIilcblxuIyBBY2NlcHQgbXVsdGlwbGUgZXhjZXB0aW9uIHR5cGVzXG53aXRoIHN1cHByZXNzKEZpbGVOb3RGb3VuZEVycm9yLCBQZXJtaXNzaW9uRXJyb3IpOlxuICAgIG9zLnJlbW92ZShcImxvY2tlZF9maWxlLnR4dFwiKSJ9"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3N1cHByZXNzaW5nX2V4Y2VwdGlvbnNfYW5kX2d1YXJhbnRlZWluZ19jbGVhbnVwIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiIjIEFwcHJvcHJpYXRlOiBkZWxldGluZyBhIGZpbGUgdGhhdCBtYXkgb3IgbWF5IG5vdCBleGlzdCBpcyBhIG5vcm1hbCBvcGVyYXRpb25cbndpdGggc3VwcHJlc3MoRmlsZU5vdEZvdW5kRXJyb3IpOlxuICAgIG9zLnJlbW92ZShcInRlbXBfZXhwb3J0LmNzdlwiKVxuXG4jIEluYXBwcm9wcmlhdGU6IHRoaXMgc3dhbGxvd3MgYWxsIGV4Y2VwdGlvbnMgaW5jbHVkaW5nIHJlYWwgYnVnc1xudHJ5OlxuICAgIHByb2Nlc3NfY2F0YWxvZygpXG5leGNlcHQgRXhjZXB0aW9uOlxuICAgIHBhc3MgICAjIHNpbGVudCBhbmQgZGFuZ2Vyb3VzIn0"
 width="100%"
></iframe>

## Guaranteeing Cleanup in Edge Cases

Context managers guarantee cleanup in situations that `try`/`except`/`finally` often gets wrong:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3N1cHByZXNzaW5nX2V4Y2VwdGlvbnNfYW5kX2d1YXJhbnRlZWluZ19jbGVhbnVwIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiIjIERvZXMgZmluYWxseSBydW4gaWYgdGhlcmUncyBhIHJldHVybiBpbnNpZGUgdHJ5P1xuZGVmIGxvYWQoKTpcbiAgICB3aXRoIG9wZW4oXCJjYXRhbG9nLnR4dFwiKSBhcyBmOlxuICAgICAgICByZXR1cm4gZi5yZWFkKCkgICAjIGZpbGUgaXMgc3RpbGwgY2xvc2VkLCBldmVuIHdpdGggZWFybHkgcmV0dXJuXG5cbiMgRG9lcyBfX2V4aXRfXyBydW4gaW5zaWRlIGEgZ2VuZXJhdG9yP1xuZGVmIHJlYWRfbGluZXMoKTpcbiAgICB3aXRoIG9wZW4oXCJjYXRhbG9nLnR4dFwiKSBhcyBmOlxuICAgICAgICBmb3IgbGluZSBpbiBmOlxuICAgICAgICAgICAgeWllbGQgbGluZS5zdHJpcCgpXG4gICAgIyBmaWxlIGlzIGNsb3NlZCB3aGVuIHRoZSBnZW5lcmF0b3IgaXMgZ2FyYmFnZS1jb2xsZWN0ZWQgb3IgZXhoYXVzdGVkXG5cbiMgRG9lcyBfX2V4aXRfXyBydW4gb24gU3lzdGVtRXhpdCBvciBLZXlib2FyZEludGVycnVwdD9cbmNsYXNzIENsZWFudXA6XG4gICAgZGVmIF9fZW50ZXJfXyhzZWxmKTogcmV0dXJuIHNlbGZcbiAgICBkZWYgX19leGl0X18oc2VsZiwgZXhjX3R5cGUsIGV4Y192YWwsIGV4Y190Yik6XG4gICAgICAgIHByaW50KFwiQ2xlYW51cCByYW5cIilcbiAgICAgICAgcmV0dXJuIEZhbHNlXG5cbndpdGggQ2xlYW51cCgpOlxuICAgIHJhaXNlIFN5c3RlbUV4aXQoMClcbiMgXCJDbGVhbnVwIHJhblwiIGlzIHByaW50ZWQgYmVmb3JlIHRoZSBwcm9jZXNzIGV4aXRzIn0"
 width="100%"
></iframe>

`__exit__` is called even when `SystemExit` or `KeyboardInterrupt` is raised, because these are `BaseException` subclasses and the `with` statement does not filter them out. This makes context managers more reliable than manual `try`/`finally` for critical cleanup.

## Combining: Log, Suppress, Clean Up

Here is the pattern Tara uses for her daily backup task:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3N1cHByZXNzaW5nX2V4Y2VwdGlvbnNfYW5kX2d1YXJhbnRlZWluZ19jbGVhbnVwIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJpbXBvcnQgbG9nZ2luZ1xuZnJvbSBjb250ZXh0bGliIGltcG9ydCBjb250ZXh0bWFuYWdlciwgc3VwcHJlc3NcblxubG9nZ2VyID0gbG9nZ2luZy5nZXRMb2dnZXIoX19uYW1lX18pXG5cbkBjb250ZXh0bWFuYWdlclxuZGVmIHNhZmVfYmFja3VwKHBhdGgpOlxuICAgIGxvZ2dlci5pbmZvKGZcIlN0YXJ0aW5nIGJhY2t1cCB0byB7cGF0aH1cIilcbiAgICB0cnk6XG4gICAgICAgIHlpZWxkIHBhdGhcbiAgICAgICAgbG9nZ2VyLmluZm8oZlwiQmFja3VwIGNvbXBsZXRlZDoge3BhdGh9XCIpXG4gICAgZXhjZXB0IE9TRXJyb3IgYXMgZXhjOlxuICAgICAgICBsb2dnZXIuZXJyb3IoZlwiQmFja3VwIGZhaWxlZDoge2V4Y31cIilcbiAgICAgICAgcmFpc2UgICAjIHJlLXJhaXNlIHNvIHRoZSBzY2hlZHVsZXIga25vd3MgaXQgZmFpbGVkXG4gICAgZmluYWxseTpcbiAgICAgICAgbG9nZ2VyLmRlYnVnKFwiQmFja3VwIGNvbnRleHQgZXhpdGluZ1wiKVxuXG5kZWYgcnVuX2RhaWx5X2JhY2t1cCgpOlxuICAgIHdpdGggc3VwcHJlc3MoT1NFcnJvcik6ICAgICAgICAgICMgb3V0ZXIgc3VwcHJlc3Npb246IGJhY2t1cCBmYWlsdXJlIGlzIG5vbi1mYXRhbCBmb3IgdGhlIHNlcnZpY2VcbiAgICAgICAgd2l0aCBzYWZlX2JhY2t1cChcImJhY2t1cC5jc3ZcIikgYXMgcGF0aDpcbiAgICAgICAgICAgIGV4cG9ydF9jYXRhbG9nKHBhdGgpIn0"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3N1cHByZXNzaW5nX2V4Y2VwdGlvbnNfYW5kX2d1YXJhbnRlZWluZ19jbGVhbnVwIGNvZGUgNiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNi5weSIsImNvZGUiOiJpbXBvcnQgb3NcbmltcG9ydCBsb2dnaW5nXG5mcm9tIGNvbnRleHRsaWIgaW1wb3J0IHN1cHByZXNzXG5cbmxvZ2dlciA9IGxvZ2dpbmcuZ2V0TG9nZ2VyKF9fbmFtZV9fKVxuXG5kZWYgc2FmZV9yZW1vdmVfYWxsKHBhdGhzKTpcbiAgICBmb3IgcGF0aCBpbiBwYXRoczpcbiAgICAgICAgd2l0aCBzdXBwcmVzcyhGaWxlTm90Rm91bmRFcnJvcik6XG4gICAgICAgICAgICB0cnk6XG4gICAgICAgICAgICAgICAgb3MucmVtb3ZlKHBhdGgpXG4gICAgICAgICAgICAgICAgbG9nZ2VyLmluZm8oZlwiUmVtb3ZlZDoge3BhdGh9XCIpXG4gICAgICAgICAgICBleGNlcHQgUGVybWlzc2lvbkVycm9yIGFzIGV4YzpcbiAgICAgICAgICAgICAgICBsb2dnZXIud2FybmluZyhmXCJQZXJtaXNzaW9uIGRlbmllZCBmb3Ige3BhdGh9OiB7ZXhjfVwiKVxuICAgICAgICAgICAgICAgICMgZG8gbm90IHJlLXJhaXNlIC0tIGxvZyBhbmQgY29udGludWVcblxudGVzdF9wYXRocyA9IFtcImEudHh0XCIsIFwibWlzc2luZy50eHRcIiwgXCJiLnR4dFwiXVxuIyBDcmVhdGUgdGhlIG9uZXMgdGhhdCBzaG91bGQgZXhpc3Q6XG5mb3IgcCBpbiBbXCJhLnR4dFwiLCBcImIudHh0XCJdOlxuICAgIG9wZW4ocCwgXCJ3XCIpLmNsb3NlKClcblxubG9nZ2luZy5iYXNpY0NvbmZpZyhsZXZlbD1sb2dnaW5nLkRFQlVHKVxuc2FmZV9yZW1vdmVfYWxsKHRlc3RfcGF0aHMpIn0"
 width="100%"
></iframe>

## Conclusion

Returning `True` from `__exit__` suppresses an exception; `contextlib.suppress` provides a clean one-liner for specific types. Suppression is safe when the error condition is expected, continuation is safe, and the suppression is narrow. Context managers guarantee cleanup even on `return`, `yield`, `SystemExit`, and `KeyboardInterrupt`, making them more reliable than manual `try`/`finally` for critical cleanup. Unit 7 moves from resource management to Python's standard library, exploring the built-in modules that solve common problems so you do not have to write them yourself.
