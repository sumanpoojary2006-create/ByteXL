## Introduction

Kiran has `load_catalog = add_timing(load_catalog)` working. But applying it to twelve endpoint handlers means writing the same assignment pattern twelve times, which is not much better than the original copy-paste problem. She discovers that Python provides exactly the syntax she needs: the `@` decorator syntax, which applies the wrapper automatically at definition time, in one line, attached to the function itself.

This lesson introduces the `@` syntax, confirms it is exactly what she has already been doing, and applies it to build a real timing decorator.

![A function definition with @add_timing above it, shown as equivalent to writing add_timing(fn) = fn below the definition, with the function card being handed into the decorator box](images/03_writing_a_simple_decorator.png)

## The @ Syntax Is Syntactic Sugar

The decorator syntax `@name` placed above a function definition is exactly equivalent to `fn = name(fn)` placed immediately after the definition. No new language feature is involved; it is a shorthand.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3dyaXRpbmdfYV9zaW1wbGVfZGVjb3JhdG9yIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiIjIFdpdGhvdXQgQCBzeW50YXg6XG5kZWYgbG9hZF9jYXRhbG9nKHNpemUpOlxuICAgIHJldHVybiBsaXN0KHJhbmdlKHNpemUpKVxubG9hZF9jYXRhbG9nID0gYWRkX3RpbWluZyhsb2FkX2NhdGFsb2cpXG5cbiMgV2l0aCBAIHN5bnRheCAoaWRlbnRpY2FsIGJlaGF2aW9yKTpcbkBhZGRfdGltaW5nXG5kZWYgbG9hZF9jYXRhbG9nKHNpemUpOlxuICAgIHJldHVybiBsaXN0KHJhbmdlKHNpemUpKSJ9"
 width="100%"
></iframe>

Python reads the `@add_timing` line, registers it, then when it processes the `def`, it immediately applies `add_timing` to the function object and rebinds the name `load_catalog` to the result. The function definition and the decoration happen at the same place in the source file.

## A Complete Simple Decorator

Here is the full decorator Kiran needs:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3dyaXRpbmdfYV9zaW1wbGVfZGVjb3JhdG9yIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJpbXBvcnQgdGltZVxuXG5kZWYgYWRkX3RpbWluZyhmbik6XG4gICAgZGVmIHdyYXBwZXIoKmFyZ3MsICoqa3dhcmdzKTpcbiAgICAgICAgc3RhcnQgPSB0aW1lLnRpbWUoKVxuICAgICAgICByZXN1bHQgPSBmbigqYXJncywgKiprd2FyZ3MpXG4gICAgICAgIGVsYXBzZWQgPSB0aW1lLnRpbWUoKSAtIHN0YXJ0XG4gICAgICAgIHByaW50KGZcIntmbi5fX25hbWVfX30gcmFuIGluIHtlbGFwc2VkOi40Zn1zXCIpXG4gICAgICAgIHJldHVybiByZXN1bHRcbiAgICByZXR1cm4gd3JhcHBlclxuXG5AYWRkX3RpbWluZ1xuZGVmIGxvYWRfY2F0YWxvZyhzaXplKTpcbiAgICB0aW1lLnNsZWVwKDAuMDUpXG4gICAgcmV0dXJuIGxpc3QocmFuZ2Uoc2l6ZSkpXG5cbkBhZGRfdGltaW5nXG5kZWYgc2VhcmNoX2NhdGFsb2cocXVlcnksIGNhdGFsb2cpOlxuICAgIHJldHVybiBbaXRlbSBmb3IgaXRlbSBpbiBjYXRhbG9nIGlmIHF1ZXJ5IGluIHN0cihpdGVtKV1cblxuY2F0YWxvZyA9IGxvYWRfY2F0YWxvZyg1MClcbiMgbG9hZF9jYXRhbG9nIHJhbiBpbiAwLjA1MDFzXG5cbnJlc3VsdHMgPSBzZWFyY2hfY2F0YWxvZyhcIjFcIiwgY2F0YWxvZylcbiMgc2VhcmNoX2NhdGFsb2cgcmFuIGluIDAuMDAwMHMifQ"
 width="100%"
></iframe>

Both functions are timed without any changes to their bodies. Adding `@add_timing` to the remaining ten endpoint handlers takes ten characters, not ten blocks of boilerplate.

## Decorators Run at Definition Time, Not Call Time

An important detail: the decorator itself is called when the `def` statement is processed, which is at module import time, not when the decorated function is first called. The function object is passed to the decorator immediately, and the wrapper replaces it.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3dyaXRpbmdfYV9zaW1wbGVfZGVjb3JhdG9yIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJkZWYgYW5ub3VuY2UoZm4pOlxuICAgIHByaW50KGZcIkRlY29yYXRpbmcge2ZuLl9fbmFtZV9ffVwiKSAgICAjIHJ1bnMgYXQgZGVmaW5pdGlvbiB0aW1lXG4gICAgZGVmIHdyYXBwZXIoKmFyZ3MsICoqa3dhcmdzKTpcbiAgICAgICAgcmV0dXJuIGZuKCphcmdzLCAqKmt3YXJncylcbiAgICByZXR1cm4gd3JhcHBlclxuXG5AYW5ub3VuY2VcbmRlZiBncmVldChuYW1lKTpcbiAgICByZXR1cm4gZlwiSGVsbG8sIHtuYW1lfVwiXG5cbiMgXCJEZWNvcmF0aW5nIGdyZWV0XCIgd2FzIGFscmVhZHkgcHJpbnRlZFxucHJpbnQoZ3JlZXQoXCJLaXJhblwiKSkgICAjIEhlbGxvLCBLaXJhbiJ9"
 width="100%"
></iframe>

This matters in practice: if you import a module that contains decorated functions, the decorator runs during the import, not during the first call. If a decorator has expensive setup, that cost is paid at import time.

## Decorators That Do Not Change the Return Value

Not every decorator needs to modify the return value. Some only add side effects: logging, timing, caching checks. The wrapper must still `return result` to not accidentally suppress the return value.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3dyaXRpbmdfYV9zaW1wbGVfZGVjb3JhdG9yIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJkZWYgbG9nX2NhbGwoZm4pOlxuICAgIGRlZiB3cmFwcGVyKCphcmdzLCAqKmt3YXJncyk6XG4gICAgICAgIHByaW50KGZcIkNhbGxpbmcge2ZuLl9fbmFtZV9ffVwiKVxuICAgICAgICByZXN1bHQgPSBmbigqYXJncywgKiprd2FyZ3MpXG4gICAgICAgIHByaW50KGZcIntmbi5fX25hbWVfX30gY29tcGxldGVcIilcbiAgICAgICAgcmV0dXJuIHJlc3VsdCAgICAjIGVzc2VudGlhbDogcGFzcyB0aGUgcmVzdWx0IHRocm91Z2hcbiAgICByZXR1cm4gd3JhcHBlclxuXG5AbG9nX2NhbGxcbmRlZiBhZGRfYm9vayh0aXRsZSwgaXNibik6XG4gICAgcmV0dXJuIHtcInRpdGxlXCI6IHRpdGxlLCBcImlzYm5cIjogaXNibn1cblxuYm9vayA9IGFkZF9ib29rKFwiRHVuZVwiLCBcIjk3OC0wNDQxMDEzNTkzXCIpXG4jIENhbGxpbmcgYWRkX2Jvb2tcbiMgYWRkX2Jvb2sgY29tcGxldGVcbnByaW50KGJvb2spICAgIyB7J3RpdGxlJzogJ0R1bmUnLCAnaXNibic6ICc5NzgtMDQ0MTAxMzU5Myd9In0"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3dyaXRpbmdfYV9zaW1wbGVfZGVjb3JhdG9yIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJkZWYgdmFsaWRhdGVfcG9zaXRpdmUoZm4pOlxuICAgIGRlZiB3cmFwcGVyKCphcmdzLCAqKmt3YXJncyk6XG4gICAgICAgIGZvciBhcmcgaW4gYXJnczpcbiAgICAgICAgICAgIGlmIGlzaW5zdGFuY2UoYXJnLCAoaW50LCBmbG9hdCkpIGFuZCBhcmcgPCAwOlxuICAgICAgICAgICAgICAgIHJhaXNlIFZhbHVlRXJyb3IoZlwiTmVnYXRpdmUgYXJndW1lbnQgbm90IGFsbG93ZWQ6IHthcmd9XCIpXG4gICAgICAgIHJldHVybiBmbigqYXJncywgKiprd2FyZ3MpXG4gICAgcmV0dXJuIHdyYXBwZXJcblxuQHZhbGlkYXRlX3Bvc2l0aXZlXG5kZWYgc2V0X2NvcGllcyhpc2JuLCBjb3VudCk6XG4gICAgcHJpbnQoZlwiU2V0dGluZyB7aXNibn0gdG8ge2NvdW50fSBjb3BpZXNcIilcblxuc2V0X2NvcGllcyhcIjk3OC0wMDFcIiwgMykgICAgICMgd29ya3NcbnNldF9jb3BpZXMoXCI5NzgtMDAxXCIsIC0xKSAgICAjIGVycm9yISJ9"
 width="100%"
></iframe>

Test both calls. Then apply `@validate_positive` to a second function of your choice to confirm it works generically without any modification.

## Conclusion

The `@decorator` syntax is a concise way to write `fn = decorator(fn)`, applied at function-definition time. The decorator receives the original function, creates a wrapper that calls it and adds behavior, and returns the wrapper. Always return the result of `fn(*args, **kwargs)` from the wrapper, or the decorated function will silently return `None`. The next lesson covers the case where the decorator itself needs configuration: how to write decorators that accept arguments.
