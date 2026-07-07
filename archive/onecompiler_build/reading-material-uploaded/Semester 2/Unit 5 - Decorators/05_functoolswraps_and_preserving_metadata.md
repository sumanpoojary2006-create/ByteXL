## Introduction

Kiran's timing decorator is in production. A new developer on the team opens the API documentation generation tool and sees something strange: every timed function is listed as `wrapper` in the docs, and every one has an empty docstring. The documentation generator reads `fn.__name__` and `fn.__doc__`, but after decoration, those attributes belong to `wrapper`, not to the original function.

This is a real and irritating problem. The fix is a single import and one additional line: `functools.wraps`.

![A decorated function shown with __name__ pointing to wrapper on the left, and after @wraps the __name__ pointing to the original function name on the right](images/05_functoolswraps_metadata.png)

## The Problem: Wrappers Hide the Original's Identity

When a decorator wraps a function, the name `fn` now points to `wrapper`. This means introspection tools, debuggers, and documentation generators see `wrapper` rather than the original function.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-5-decorators-05-functoolswraps-and-preserving-metadata-001-4a7c13852c.html"
 width="100%"
></iframe>

The function's name, docstring, and signature are all from `wrapper`, not from `load_catalog`.

## The Fix: functools.wraps

`functools.wraps` is a decorator for your wrapper function. It copies the original function's `__name__`, `__qualname__`, `__doc__`, `__dict__`, `__module__`, and `__wrapped__` attributes onto the wrapper, making the wrapper look like the original to every tool that inspects it.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-5-decorators-05-functoolswraps-and-preserving-metadata-002-93033734d0.html"
 width="100%"
></iframe>

The `__wrapped__` attribute is a bonus: it points to the original function, which lets tools like `inspect.signature` and testing frameworks reach through the decoration to the real function.

## Why This Matters Beyond Documentation

`functools.wraps` is not just cosmetic. Several important tools depend on the function name and signature:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-5-decorators-05-functoolswraps-and-preserving-metadata-003-8951c0a65e.html"
 width="100%"
></iframe>

`inspect.signature` is used by FastAPI and other frameworks to generate API schemas from function signatures. Without `@wraps`, every decorated route would have the signature `(*args, **kwargs)`, breaking automatic schema generation.

## Applying @wraps in Parameterized Decorators

`@functools.wraps(fn)` goes on the wrapper function, regardless of how many levels of nesting the decorator has:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-5-decorators-05-functoolswraps-and-preserving-metadata-004-2b1434d712.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-5-decorators-05-functoolswraps-and-preserving-metadata-005-380e6bc897.html"
 width="100%"
></iframe>

## Conclusion

Every decorator should include `@functools.wraps(fn)` on the wrapper function. Without it, the wrapped function loses its name, docstring, and signature, breaking documentation generators, testing frameworks, and API schema tools. `@wraps` is not optional polish; it is part of writing a complete, correct decorator. The next lesson covers what happens when you stack multiple decorators on the same function: the order matters, and understanding it prevents surprising behavior.
