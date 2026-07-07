## Introduction

Tara has just written a full class-based context manager. It works perfectly, but she notices it is twelve lines of boilerplate for a straightforward open-then-close pattern. She wonders if Python has a shorter way to write context managers for cases where the setup and teardown fit naturally in a single function.

Python does. The `contextlib` module includes a decorator called `@contextmanager` that lets you write a context manager using a generator function with a single `yield`. No class required.

![A before and after: a class with __enter__ and __exit__ on the left, a generator function with yield on the right, both producing identical behavior](images/04_contextlib_contextmanager.png)

## @contextmanager: the Generator Shortcut

`@contextmanager` turns a generator function into a context manager. The code before `yield` runs as `__enter__`, the yielded value becomes the `as` target, and the code after `yield` runs as `__exit__`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2NvbnRleHRsaWJfYW5kX2NvbnRleHRtYW5hZ2VyIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJmcm9tIGNvbnRleHRsaWIgaW1wb3J0IGNvbnRleHRtYW5hZ2VyXG5cbkBjb250ZXh0bWFuYWdlclxuZGVmIG1hbmFnZWRfY29ubmVjdGlvbihkYl9wYXRoKTpcbiAgICBpbXBvcnQgc3FsaXRlM1xuICAgIGNvbm4gPSBzcWxpdGUzLmNvbm5lY3QoZGJfcGF0aClcbiAgICB0cnk6XG4gICAgICAgIHlpZWxkIGNvbm4gICAgICAgICMgXCJlbnRlclwiOiBjb25uIGlzIGJvdW5kIHRvIHRoZSBhcy12YXJpYWJsZVxuICAgIGZpbmFsbHk6XG4gICAgICAgIGNvbm4uY2xvc2UoKSAgICAgICMgXCJleGl0XCI6IGFsd2F5cyBydW5zXG5cbndpdGggbWFuYWdlZF9jb25uZWN0aW9uKFwiOm1lbW9yeTpcIikgYXMgY29ubjpcbiAgICBjb25uLmV4ZWN1dGUoXCJDUkVBVEUgVEFCTEUgYm9va3MgKGlzYm4gVEVYVCwgdGl0bGUgVEVYVClcIilcbiAgICBwcmludChcIkRvbmVcIilcbiMgY29ubiBpcyBjbG9zZWQgaGVyZSJ9"
 width="100%"
></iframe>

The `try`/`finally` around `yield` is what makes the cleanup unconditional. If an exception is raised inside the `with` block, it is thrown *into* the generator at the `yield` point, the `finally` runs, and the exception propagates.

## Handling Exceptions in @contextmanager

When an exception occurs inside the `with` block, `@contextmanager` re-raises it at the `yield` point inside the generator. Wrapping `yield` in `try`/`except` lets you catch and respond to it, exactly like `__exit__`'s exception arguments.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2NvbnRleHRsaWJfYW5kX2NvbnRleHRtYW5hZ2VyIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJmcm9tIGNvbnRleHRsaWIgaW1wb3J0IGNvbnRleHRtYW5hZ2VyXG5pbXBvcnQgc3FsaXRlM1xuXG5AY29udGV4dG1hbmFnZXJcbmRlZiB0cmFuc2FjdGlvbihjb25uKTpcbiAgICBjdXJzb3IgPSBjb25uLmN1cnNvcigpXG4gICAgdHJ5OlxuICAgICAgICB5aWVsZCBjdXJzb3JcbiAgICAgICAgY29ubi5jb21taXQoKVxuICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZXhjOlxuICAgICAgICBjb25uLnJvbGxiYWNrKClcbiAgICAgICAgcHJpbnQoZlwiUm9sbGVkIGJhY2s6IHtleGN9XCIpXG4gICAgICAgIHJhaXNlICAgIyByZS1yYWlzZSBzbyB0aGUgY2FsbGVyIHN0aWxsIHNlZXMgdGhlIGV4Y2VwdGlvblxuXG5jb25uID0gc3FsaXRlMy5jb25uZWN0KFwiOm1lbW9yeTpcIilcbmNvbm4uZXhlY3V0ZShcIkNSRUFURSBUQUJMRSBib29rcyAoaXNibiBURVhULCB0aXRsZSBURVhUKVwiKVxuXG53aXRoIHRyYW5zYWN0aW9uKGNvbm4pIGFzIGN1cnNvcjpcbiAgICBjdXJzb3IuZXhlY3V0ZShcIklOU0VSVCBJTlRPIGJvb2tzIFZBTFVFUyAoJzk3OC0wMDEnLCAnRHVuZScpXCIpXG4jIGNvbW1pdHRlZFxuXG50cnk6XG4gICAgd2l0aCB0cmFuc2FjdGlvbihjb25uKSBhcyBjdXJzb3I6XG4gICAgICAgIGN1cnNvci5leGVjdXRlKFwiSU5TRVJUIElOVE8gYm9va3MgVkFMVUVTICgnOTc4LTAwMicsICdGb3VuZGF0aW9uJylcIilcbiAgICAgICAgcmFpc2UgUnVudGltZUVycm9yKFwiU2ltdWxhdGVkIGZhaWx1cmVcIilcbmV4Y2VwdCBSdW50aW1lRXJyb3I6XG4gICAgcGFzcyAgICMgcm9sbGVkIGJhY2sifQ"
 width="100%"
></iframe>

## When to Use @contextmanager vs a Class

Both approaches implement the same protocol. The choice is stylistic:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2NvbnRleHRsaWJfYW5kX2NvbnRleHRtYW5hZ2VyIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiIjIENsYXNzLWJhc2VkOiBnb29kIHdoZW4gc2V0dXAgaXMgY29tcGxleCwgbXVsdGlwbGUgbWV0aG9kcywgb3Igc3RhdGVcbmNsYXNzIE1hbmFnZWRGaWxlOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBwYXRoLCBtb2RlKTpcbiAgICAgICAgc2VsZi5wYXRoID0gcGF0aFxuICAgICAgICBzZWxmLm1vZGUgPSBtb2RlXG4gICAgICAgIHNlbGYuZmlsZSA9IE5vbmVcblxuICAgIGRlZiBfX2VudGVyX18oc2VsZik6XG4gICAgICAgIHNlbGYuZmlsZSA9IG9wZW4oc2VsZi5wYXRoLCBzZWxmLm1vZGUpXG4gICAgICAgIHJldHVybiBzZWxmLmZpbGVcblxuICAgIGRlZiBfX2V4aXRfXyhzZWxmLCBleGNfdHlwZSwgZXhjX3ZhbCwgZXhjX3RiKTpcbiAgICAgICAgaWYgc2VsZi5maWxlOlxuICAgICAgICAgICAgc2VsZi5maWxlLmNsb3NlKClcbiAgICAgICAgcmV0dXJuIEZhbHNlXG5cbiMgR2VuZXJhdG9yLWJhc2VkOiBnb29kIGZvciBzaW1wbGUgc2V0dXAvdGVhcmRvd24gcGFpcnNcbkBjb250ZXh0bWFuYWdlclxuZGVmIG1hbmFnZWRfZmlsZShwYXRoLCBtb2RlKTpcbiAgICBmID0gb3BlbihwYXRoLCBtb2RlKVxuICAgIHRyeTpcbiAgICAgICAgeWllbGQgZlxuICAgIGZpbmFsbHk6XG4gICAgICAgIGYuY2xvc2UoKSJ9"
 width="100%"
></iframe>

Use `@contextmanager` when the context manager is a single function with a clear before/after pattern. Use a class when the context manager needs multiple helper methods, stores complex state, or wraps a reusable object that already has a lifecycle.

## Other Useful contextlib Tools

`contextlib` provides several ready-made context managers:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2NvbnRleHRsaWJfYW5kX2NvbnRleHRtYW5hZ2VyIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJmcm9tIGNvbnRleHRsaWIgaW1wb3J0IHN1cHByZXNzLCBudWxsY29udGV4dCwgRXhpdFN0YWNrXG5cbiMgc3VwcHJlc3M6IHNpbGVudGx5IGlnbm9yZSBzcGVjaWZpYyBleGNlcHRpb25zXG53aXRoIHN1cHByZXNzKEZpbGVOb3RGb3VuZEVycm9yKTpcbiAgICBvcy5yZW1vdmUoXCJtYXliZV9leGlzdHMudHh0XCIpICAgIyBubyBlcnJvciBpZiBmaWxlIGlzIGFic2VudFxuXG4jIG51bGxjb250ZXh0OiBhIGNvbnRleHQgbWFuYWdlciB0aGF0IGRvZXMgbm90aGluZyAodXNlZnVsIGZvciBvcHRpb25hbCB3cmFwcGluZylcbmRlZiBwcm9jZXNzKGNvbm4sIGluX3RyYW5zYWN0aW9uPUZhbHNlKTpcbiAgICBjdHggPSBudWxsY29udGV4dCgpIGlmIGluX3RyYW5zYWN0aW9uIGVsc2UgdHJhbnNhY3Rpb24oY29ubilcbiAgICB3aXRoIGN0eDpcbiAgICAgICAgZG9fd29yayhjb25uKVxuXG4jIEV4aXRTdGFjazogZHluYW1pY2FsbHkgY29tcG9zZSBjb250ZXh0IG1hbmFnZXJzXG5maWxlX2xpc3QgPSBbXCJhLnR4dFwiLCBcImIudHh0XCIsIFwiYy50eHRcIl1cbndpdGggRXhpdFN0YWNrKCkgYXMgc3RhY2s6XG4gICAgaGFuZGxlcyA9IFtzdGFjay5lbnRlcl9jb250ZXh0KG9wZW4oZikpIGZvciBmIGluIGZpbGVfbGlzdF1cbiAgICAjIGFsbCB0aHJlZSBmaWxlcyBhcmUgb3BlbjsgYWxsIGNsb3NlZCB3aGVuIHRoZSB3aXRoIGJsb2NrIGV4aXRzIn0"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2NvbnRleHRsaWJfYW5kX2NvbnRleHRtYW5hZ2VyIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJmcm9tIGNvbnRleHRsaWIgaW1wb3J0IGNvbnRleHRtYW5hZ2VyXG5pbXBvcnQgdGVtcGZpbGUsIHNodXRpbFxuXG5AY29udGV4dG1hbmFnZXJcbmRlZiB0ZW1wX2RpcmVjdG9yeSgpOlxuICAgIHBhdGggPSB0ZW1wZmlsZS5ta2R0ZW1wKClcbiAgICBwcmludChmXCJDcmVhdGVkOiB7cGF0aH1cIilcbiAgICB0cnk6XG4gICAgICAgIHlpZWxkIHBhdGhcbiAgICBmaW5hbGx5OlxuICAgICAgICBzaHV0aWwucm10cmVlKHBhdGgpXG4gICAgICAgIHByaW50KGZcIlJlbW92ZWQ6IHtwYXRofVwiKVxuXG5pbXBvcnQgb3NcbndpdGggdGVtcF9kaXJlY3RvcnkoKSBhcyB0bXBkaXI6XG4gICAgZmlsZXBhdGggPSBvcy5wYXRoLmpvaW4odG1wZGlyLCBcInRlc3QudHh0XCIpXG4gICAgd2l0aCBvcGVuKGZpbGVwYXRoLCBcIndcIikgYXMgZjpcbiAgICAgICAgZi53cml0ZShcInRlbXBvcmFyeSBkYXRhXCIpXG4gICAgcHJpbnQoZlwiRmlsZSBleGlzdHM6IHtvcy5wYXRoLmV4aXN0cyhmaWxlcGF0aCl9XCIpXG5cbnByaW50KGZcIkRpciBleGlzdHMgYWZ0ZXI6IHtvcy5wYXRoLmV4aXN0cyh0bXBkaXIpfVwiKSJ9"
 width="100%"
></iframe>

Run it and confirm the output matches the class-based version. Then add exception handling: inside the `with temp_directory()` block, raise an exception and confirm the directory is still removed.

## Conclusion

`@contextmanager` converts a generator function into a context manager: code before `yield` is setup, the yielded value is the `as` target, and code after `yield` (typically in a `finally`) is teardown. It is the preferred approach for straightforward resource-management patterns. The next lesson covers safe resource management in depth: the patterns that prevent leaks even in the presence of unexpected exceptions and nested resources.
