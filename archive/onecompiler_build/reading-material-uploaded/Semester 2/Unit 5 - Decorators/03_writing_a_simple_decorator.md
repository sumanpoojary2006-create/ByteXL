## Introduction

Kiran has `load_catalog = add_timing(load_catalog)` working. But applying it to twelve endpoint handlers means writing the same assignment pattern twelve times, which is not much better than the original copy-paste problem. She discovers that Python provides exactly the syntax she needs: the `@` decorator syntax, which applies the wrapper automatically at definition time, in one line, attached to the function itself.

This lesson introduces the `@` syntax, confirms it is exactly what she has already been doing, and applies it to build a real timing decorator.

![A function definition with @add_timing above it, shown as equivalent to writing add_timing(fn) = fn below the definition, with the function card being handed into the decorator box](images/03_writing_a_simple_decorator.png)

## The @ Syntax Is Syntactic Sugar

The decorator syntax `@name` placed above a function definition is exactly equivalent to `fn = name(fn)` placed immediately after the definition. No new language feature is involved; it is a shorthand.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-5-decorators-03-writing-a-simple-decorator-001-74852065a1.html"
 width="100%"
></iframe>

Python reads the `@add_timing` line, registers it, then when it processes the `def`, it immediately applies `add_timing` to the function object and rebinds the name `load_catalog` to the result. The function definition and the decoration happen at the same place in the source file.

## A Complete Simple Decorator

Here is the full decorator Kiran needs:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-5-decorators-03-writing-a-simple-decorator-002-dbfdb9a85e.html"
 width="100%"
></iframe>

Both functions are timed without any changes to their bodies. Adding `@add_timing` to the remaining ten endpoint handlers takes ten characters, not ten blocks of boilerplate.

## Decorators Run at Definition Time, Not Call Time

An important detail: the decorator itself is called when the `def` statement is processed, which is at module import time, not when the decorated function is first called. The function object is passed to the decorator immediately, and the wrapper replaces it.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-5-decorators-03-writing-a-simple-decorator-003-70da34a5f6.html"
 width="100%"
></iframe>

This matters in practice: if you import a module that contains decorated functions, the decorator runs during the import, not during the first call. If a decorator has expensive setup, that cost is paid at import time.

## Decorators That Do Not Change the Return Value

Not every decorator needs to modify the return value. Some only add side effects: logging, timing, caching checks. The wrapper must still `return result` to not accidentally suppress the return value.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-5-decorators-03-writing-a-simple-decorator-004-5834095e1d.html"
 width="100%"
></iframe>

Forgetting `return result` in the wrapper causes the decorated function to silently return `None`, which is one of the most common bugs when first writing decorators.

## Writing a Simple Decorator at a Glance

| Step | Code |
|---|---|
| Define the outer function | `def my_decorator(fn):` |
| Define the wrapper | `def wrapper(*args, **kwargs):` |
| Call the original | `result = fn(*args, **kwargs)` |
| Return the result | `return result` |
| Return the wrapper | `return wrapper` |
| Apply with @ | `@my_decorator` above the `def` |

## Your Turn

Write a `validate_positive` decorator that raises a `ValueError` if any positional argument passed to the decorated function is negative:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-5-decorators-03-writing-a-simple-decorator-005-8ac3dbe24a.html"
 width="100%"
></iframe>

Test both calls. Then apply `@validate_positive` to a second function of your choice to confirm it works generically without any modification.

## Conclusion

The `@decorator` syntax is a concise way to write `fn = decorator(fn)`, applied at function-definition time. The decorator receives the original function, creates a wrapper that calls it and adds behavior, and returns the wrapper. Always return the result of `fn(*args, **kwargs)` from the wrapper, or the decorated function will silently return `None`. The next lesson covers the case where the decorator itself needs configuration: how to write decorators that accept arguments.
