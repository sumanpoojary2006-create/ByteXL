## Introduction

Kiran's timing decorator is in production. A new developer on the team opens the API documentation generation tool and sees something strange: every timed function is listed as `wrapper` in the docs, and every one has an empty docstring. The documentation generator reads `fn.__name__` and `fn.__doc__`, but after decoration, those attributes belong to `wrapper`, not to the original function.

This is a real and irritating problem. The fix is a single import and one additional line: `functools.wraps`.

![A decorated function shown with __name__ pointing to wrapper on the left, and after @wraps the __name__ pointing to the original function name on the right](images/05_functoolswraps_metadata.png)

## The Problem: Wrappers Hide the Original's Identity

When a decorator wraps a function, the name `fn` now points to `wrapper`. This means introspection tools, debuggers, and documentation generators see `wrapper` rather than the original function.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2Z1bmN0b29sc3dyYXBzX2FuZF9wcmVzZXJ2aW5nX21ldGFkYXRhIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJkZWYgYWRkX3RpbWluZyhmbik6XG4gICAgZGVmIHdyYXBwZXIoKmFyZ3MsICoqa3dhcmdzKTpcbiAgICAgICAgaW1wb3J0IHRpbWVcbiAgICAgICAgc3RhcnQgPSB0aW1lLnRpbWUoKVxuICAgICAgICByZXN1bHQgPSBmbigqYXJncywgKiprd2FyZ3MpXG4gICAgICAgIHByaW50KGZcIlJhbiBpbiB7dGltZS50aW1lKCkgLSBzdGFydDouNGZ9c1wiKVxuICAgICAgICByZXR1cm4gcmVzdWx0XG4gICAgcmV0dXJuIHdyYXBwZXJcblxuQGFkZF90aW1pbmdcbmRlZiBsb2FkX2NhdGFsb2coc2l6ZSk6XG4gICAgXCJcIlwiTG9hZCBib29rcyBmcm9tIHRoZSBjYXRhbG9nLlwiXCJcIlxuICAgIHJldHVybiBsaXN0KHJhbmdlKHNpemUpKVxuXG5wcmludChsb2FkX2NhdGFsb2cuX19uYW1lX18pICAgIyB3cmFwcGVyIC0tIHdyb25nIVxucHJpbnQobG9hZF9jYXRhbG9nLl9fZG9jX18pICAgICMgTm9uZSAtLSB3cm9uZyEifQ"
 width="100%"
></iframe>

The function's name, docstring, and signature are all from `wrapper`, not from `load_catalog`.

## The Fix: functools.wraps

`functools.wraps` is a decorator for your wrapper function. It copies the original function's `__name__`, `__qualname__`, `__doc__`, `__dict__`, `__module__`, and `__wrapped__` attributes onto the wrapper, making the wrapper look like the original to every tool that inspects it.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2Z1bmN0b29sc3dyYXBzX2FuZF9wcmVzZXJ2aW5nX21ldGFkYXRhIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJpbXBvcnQgZnVuY3Rvb2xzXG5pbXBvcnQgdGltZVxuXG5kZWYgYWRkX3RpbWluZyhmbik6XG4gICAgQGZ1bmN0b29scy53cmFwcyhmbikgICAgIyBjb3B5IG1ldGFkYXRhIGZyb20gZm4gb250byB3cmFwcGVyXG4gICAgZGVmIHdyYXBwZXIoKmFyZ3MsICoqa3dhcmdzKTpcbiAgICAgICAgc3RhcnQgPSB0aW1lLnRpbWUoKVxuICAgICAgICByZXN1bHQgPSBmbigqYXJncywgKiprd2FyZ3MpXG4gICAgICAgIHByaW50KGZcIntmbi5fX25hbWVfX30gcmFuIGluIHt0aW1lLnRpbWUoKSAtIHN0YXJ0Oi40Zn1zXCIpXG4gICAgICAgIHJldHVybiByZXN1bHRcbiAgICByZXR1cm4gd3JhcHBlclxuXG5AYWRkX3RpbWluZ1xuZGVmIGxvYWRfY2F0YWxvZyhzaXplKTpcbiAgICBcIlwiXCJMb2FkIGJvb2tzIGZyb20gdGhlIGNhdGFsb2cuXCJcIlwiXG4gICAgcmV0dXJuIGxpc3QocmFuZ2Uoc2l6ZSkpXG5cbnByaW50KGxvYWRfY2F0YWxvZy5fX25hbWVfXykgICAjIGxvYWRfY2F0YWxvZyAtLSBjb3JyZWN0XG5wcmludChsb2FkX2NhdGFsb2cuX19kb2NfXykgICAgIyBMb2FkIGJvb2tzIGZyb20gdGhlIGNhdGFsb2cuIC0tIGNvcnJlY3RcbnByaW50KGxvYWRfY2F0YWxvZy5fX3dyYXBwZWRfXykgICMgdGhlIG9yaWdpbmFsIHVud3JhcHBlZCBmdW5jdGlvbiJ9"
 width="100%"
></iframe>

The `__wrapped__` attribute is a bonus: it points to the original function, which lets tools like `inspect.signature` and testing frameworks reach through the decoration to the real function.

## Why This Matters Beyond Documentation

`functools.wraps` is not just cosmetic. Several important tools depend on the function name and signature:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2Z1bmN0b29sc3dyYXBzX2FuZF9wcmVzZXJ2aW5nX21ldGFkYXRhIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJpbXBvcnQgaW5zcGVjdFxuXG5AYWRkX3RpbWluZ1xuZGVmIHNlYXJjaChxdWVyeSwgbWF4X3Jlc3VsdHM9MTApOlxuICAgIFwiXCJcIlNlYXJjaCB0aGUgY2F0YWxvZyBmb3IgcXVlcnkuXCJcIlwiXG4gICAgcmV0dXJuIFtdXG5cbnByaW50KGluc3BlY3Quc2lnbmF0dXJlKHNlYXJjaCkpICAgIyAocXVlcnksIG1heF9yZXN1bHRzPTEwKSB3aXRoIEB3cmFwc1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAjICgqYXJncywgKiprd2FyZ3MpIHdpdGhvdXQgQHdyYXBzIn0"
 width="100%"
></iframe>

`inspect.signature` is used by FastAPI and other frameworks to generate API schemas from function signatures. Without `@wraps`, every decorated route would have the signature `(*args, **kwargs)`, breaking automatic schema generation.

## Applying @wraps in Parameterized Decorators

`@functools.wraps(fn)` goes on the wrapper function, regardless of how many levels of nesting the decorator has:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2Z1bmN0b29sc3dyYXBzX2FuZF9wcmVzZXJ2aW5nX21ldGFkYXRhIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJpbXBvcnQgZnVuY3Rvb2xzXG5cbmRlZiByZXRyeShtYXhfYXR0ZW1wdHM9Myk6XG4gICAgZGVmIGRlY29yYXRvcihmbik6XG4gICAgICAgIEBmdW5jdG9vbHMud3JhcHMoZm4pICAgICMgd3JhcHMgdGhlIHdyYXBwZXIgYXQgdGhlIGlubmVybW9zdCBsZXZlbFxuICAgICAgICBkZWYgd3JhcHBlcigqYXJncywgKiprd2FyZ3MpOlxuICAgICAgICAgICAgZm9yIGF0dGVtcHQgaW4gcmFuZ2UoMSwgbWF4X2F0dGVtcHRzICsgMSk6XG4gICAgICAgICAgICAgICAgdHJ5OlxuICAgICAgICAgICAgICAgICAgICByZXR1cm4gZm4oKmFyZ3MsICoqa3dhcmdzKVxuICAgICAgICAgICAgICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZTpcbiAgICAgICAgICAgICAgICAgICAgaWYgYXR0ZW1wdCA9PSBtYXhfYXR0ZW1wdHM6XG4gICAgICAgICAgICAgICAgICAgICAgICByYWlzZVxuICAgICAgICAgICAgICAgICAgICBwcmludChmXCJBdHRlbXB0IHthdHRlbXB0fSBmYWlsZWQ6IHtlfVwiKVxuICAgICAgICByZXR1cm4gd3JhcHBlclxuICAgIHJldHVybiBkZWNvcmF0b3JcblxuQHJldHJ5KG1heF9hdHRlbXB0cz0yKVxuZGVmIGZldGNoX2Jvb2soaXNibik6XG4gICAgXCJcIlwiRmV0Y2ggYSBib29rIGJ5IElTQk4gZnJvbSB0aGUgcmVtb3RlIGNhdGFsb2cuXCJcIlwiXG4gICAgcmFpc2UgQ29ubmVjdGlvbkVycm9yKFwiU2ltdWxhdGVkIGZhaWx1cmVcIilcblxucHJpbnQoZmV0Y2hfYm9vay5fX25hbWVfXykgICAjIGZldGNoX2Jvb2tcbnByaW50KGZldGNoX2Jvb2suX19kb2NfXykgICAgIyBGZXRjaCBhIGJvb2sgYnkgSVNCTiBmcm9tIHRoZSByZW1vdGUgY2F0YWxvZy4ifQ"
 width="100%"
></iframe>

## functools.wraps at a Glance

| Without `@wraps` | With `@wraps(fn)` |
|---|---|
| `fn.__name__` is `"wrapper"` | `fn.__name__` is the original function's name |
| `fn.__doc__` is `None` | `fn.__doc__` is the original docstring |
| `inspect.signature(fn)` is `(*args, **kwargs)` | Shows the original signature |
| `fn.__wrapped__` does not exist | Points to the original function |

## Your Turn

Take the `validate_positive` decorator from lesson 3 and add `@functools.wraps(fn)` to the wrapper. Before adding it, print `validate_positive.__name__` and `validate_positive.__doc__` (add a docstring to the decorated function). After adding `@wraps`, print them again and confirm they now reflect the original function's identity.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2Z1bmN0b29sc3dyYXBzX2FuZF9wcmVzZXJ2aW5nX21ldGFkYXRhIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJpbXBvcnQgZnVuY3Rvb2xzXG5cbmRlZiB2YWxpZGF0ZV9wb3NpdGl2ZShmbik6XG4gICAgQGZ1bmN0b29scy53cmFwcyhmbilcbiAgICBkZWYgd3JhcHBlcigqYXJncywgKiprd2FyZ3MpOlxuICAgICAgICBmb3IgYXJnIGluIGFyZ3M6XG4gICAgICAgICAgICBpZiBpc2luc3RhbmNlKGFyZywgKGludCwgZmxvYXQpKSBhbmQgYXJnIDwgMDpcbiAgICAgICAgICAgICAgICByYWlzZSBWYWx1ZUVycm9yKGZcIk5lZ2F0aXZlIGFyZ3VtZW50OiB7YXJnfVwiKVxuICAgICAgICByZXR1cm4gZm4oKmFyZ3MsICoqa3dhcmdzKVxuICAgIHJldHVybiB3cmFwcGVyXG5cbkB2YWxpZGF0ZV9wb3NpdGl2ZVxuZGVmIHNldF9jb3BpZXMoaXNibiwgY291bnQpOlxuICAgIFwiXCJcIlNldCB0aGUgbnVtYmVyIG9mIGNvcGllcyBmb3IgYSBnaXZlbiBJU0JOLlwiXCJcIlxuICAgIHByaW50KGZcIntpc2JufToge2NvdW50fSBjb3BpZXNcIilcblxucHJpbnQoc2V0X2NvcGllcy5fX25hbWVfXykgICAjIHNldF9jb3BpZXNcbnByaW50KHNldF9jb3BpZXMuX19kb2NfXykgICAgIyBTZXQgdGhlIG51bWJlciBvZiBjb3BpZXMgZm9yIGEgZ2l2ZW4gSVNCTi4ifQ"
 width="100%"
></iframe>

## Conclusion

Every decorator should include `@functools.wraps(fn)` on the wrapper function. Without it, the wrapped function loses its name, docstring, and signature, breaking documentation generators, testing frameworks, and API schema tools. `@wraps` is not optional polish; it is part of writing a complete, correct decorator. The next lesson covers what happens when you stack multiple decorators on the same function: the order matters, and understanding it prevents surprising behavior.
