## Introduction

Dev has a working `Book` class, but using it in daily development keeps feeling slightly awkward. When he prints a book object, the output is `<__main__.Book object at 0x10a3f2340>`, which tells him nothing useful. When he compares two books with the same ISBN, Python says they are not equal because they are different objects in memory. When he tries to add book copies with `+`, Python throws an error.

These are not fundamental limitations of the language. They are gaps in the class's data model contract. The previous units defined the concept of dunder methods; this lesson implements the most useful ones on a real domain object and shows exactly how each one changes the way Python interacts with the class.

![](images/07_dunder_methods.png)

## __repr__ and __str__: Making Objects Readable

`__repr__` is the developer representation, shown in the REPL and `repr()`. It should be unambiguous and ideally reproducible as valid Python. `__str__` is the user-facing representation, used by `print()` and `str()`. If `__str__` is absent, `__repr__` is used as a fallback.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2R1bmRlcl9tZXRob2RzIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJjbGFzcyBCb29rOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCB0aXRsZSwgaXNibiwgY29waWVzKTpcbiAgICAgICAgc2VsZi50aXRsZSA9IHRpdGxlXG4gICAgICAgIHNlbGYuaXNibiA9IGlzYm5cbiAgICAgICAgc2VsZi5fY29waWVzID0gY29waWVzXG5cbiAgICBkZWYgX19yZXByX18oc2VsZik6XG4gICAgICAgIHJldHVybiBmXCJCb29rKHRpdGxlPXtzZWxmLnRpdGxlIXJ9LCBpc2JuPXtzZWxmLmlzYm4hcn0sIGNvcGllcz17c2VsZi5fY29waWVzfSlcIlxuXG4gICAgZGVmIF9fc3RyX18oc2VsZik6XG4gICAgICAgIHJldHVybiBmXCJ7c2VsZi50aXRsZX0gYnkgKElTQk4ge3NlbGYuaXNibn0pLCB7c2VsZi5fY29waWVzfSBjb3B5L2NvcGllcyBhdmFpbGFibGVcIlxuXG5iID0gQm9vayhcIkR1bmVcIiwgXCI5NzgtMDQ0MTAxMzU5M1wiLCAzKVxucHJpbnQocmVwcihiKSkgICAjIEJvb2sodGl0bGU9J0R1bmUnLCBpc2JuPSc5NzgtMDQ0MTAxMzU5MycsIGNvcGllcz0zKVxucHJpbnQoc3RyKGIpKSAgICAjIER1bmUgYnkgKElTQk4gOTc4LTA0NDEwMTM1OTMpLCAzIGNvcHkvY29waWVzIGF2YWlsYWJsZVxucHJpbnQoYikgICAgICAgICAjIER1bmUgYnkgKElTQk4gOTc4LTA0NDEwMTM1OTMpLCAzIGNvcHkvY29waWVzIGF2YWlsYWJsZSJ9"
 width="100%"
></iframe>

Always implement `__repr__` on any class you will use in interactive development. It makes debugging dramatically faster.

## __eq__: Making Objects Comparable

By default, `==` compares identity (whether two references point to the same object in memory). To make objects compare by their data instead, implement `__eq__`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2R1bmRlcl9tZXRob2RzIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJjbGFzcyBCb29rOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCB0aXRsZSwgaXNibiwgY29waWVzKTpcbiAgICAgICAgc2VsZi50aXRsZSA9IHRpdGxlXG4gICAgICAgIHNlbGYuaXNibiA9IGlzYm5cbiAgICAgICAgc2VsZi5fY29waWVzID0gY29waWVzXG5cbiAgICBkZWYgX19yZXByX18oc2VsZik6XG4gICAgICAgIHJldHVybiBmXCJCb29rKHtzZWxmLnRpdGxlIXJ9LCB7c2VsZi5pc2JuIXJ9KVwiXG5cbiAgICBkZWYgX19lcV9fKHNlbGYsIG90aGVyKTpcbiAgICAgICAgaWYgbm90IGlzaW5zdGFuY2Uob3RoZXIsIEJvb2spOlxuICAgICAgICAgICAgcmV0dXJuIE5vdEltcGxlbWVudGVkXG4gICAgICAgIHJldHVybiBzZWxmLmlzYm4gPT0gb3RoZXIuaXNibiAgICAjIGJvb2tzIGFyZSB0aGUgc2FtZSBpZiBzYW1lIElTQk5cblxuYjEgPSBCb29rKFwiRHVuZVwiLCBcIjk3OC0wNDQxMDEzNTkzXCIsIDMpXG5iMiA9IEJvb2soXCJEdW5lXCIsIFwiOTc4LTA0NDEwMTM1OTNcIiwgMSkgICAjIGRpZmZlcmVudCBjb3BpZXMsIHNhbWUgSVNCTlxuXG5wcmludChiMSA9PSBiMikgICAgIyBUcnVlIC0tIHNhbWUgSVNCTlxucHJpbnQoYjEgaXMgYjIpICAgICMgRmFsc2UgLS0gZGlmZmVyZW50IG9iamVjdHMgaW4gbWVtb3J5In0"
 width="100%"
></iframe>

Returning `NotImplemented` when the types do not match is the correct protocol: it tells Python to try the comparison from the other side before giving up.

Note: defining `__eq__` makes objects unhashable by default (Python removes the default `__hash__` method). If you want your objects to be usable in sets or as dictionary keys, also define `__hash__`:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2R1bmRlcl9tZXRob2RzIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJkZWYgX19oYXNoX18oc2VsZik6XG4gICAgcmV0dXJuIGhhc2goc2VsZi5pc2JuKSJ9"
 width="100%"
></iframe>

## __len__: Giving an Object a Length

`__len__` makes `len(obj)` work and also determines truthiness: an object with `__len__` is falsy when its length is zero.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2R1bmRlcl9tZXRob2RzIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJjbGFzcyBTaGVsZjpcbiAgICBkZWYgX19pbml0X18oc2VsZik6XG4gICAgICAgIHNlbGYuX2Jvb2tzID0gW11cblxuICAgIGRlZiBhZGQoc2VsZiwgYm9vayk6XG4gICAgICAgIHNlbGYuX2Jvb2tzLmFwcGVuZChib29rKVxuXG4gICAgZGVmIF9fbGVuX18oc2VsZik6XG4gICAgICAgIHJldHVybiBsZW4oc2VsZi5fYm9va3MpXG5cbiAgICBkZWYgX19yZXByX18oc2VsZik6XG4gICAgICAgIHJldHVybiBmXCJTaGVsZih7bGVuKHNlbGYuX2Jvb2tzKX0gYm9va3MpXCJcblxuc2hlbGYgPSBTaGVsZigpXG5wcmludChsZW4oc2hlbGYpKSAgICMgMFxucHJpbnQoYm9vbChzaGVsZikpICAjIEZhbHNlIC0tIGVtcHR5IHNoZWxmIGlzIGZhbHN5XG5cbnNoZWxmLmFkZChCb29rKFwiRHVuZVwiLCBcIjk3OC0wNDQxMDEzNTkzXCIsIDMpKVxucHJpbnQobGVuKHNoZWxmKSkgICAjIDFcbnByaW50KGJvb2woc2hlbGYpKSAgIyBUcnVlIn0"
 width="100%"
></iframe>

## __add__: Supporting the + Operator

When it makes conceptual sense to add two objects together, `__add__` enables the `+` operator. For a `Book`, adding copies from two instances might represent merging stock:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2R1bmRlcl9tZXRob2RzIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJjbGFzcyBCb29rOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCB0aXRsZSwgaXNibiwgY29waWVzKTpcbiAgICAgICAgc2VsZi50aXRsZSA9IHRpdGxlXG4gICAgICAgIHNlbGYuaXNibiA9IGlzYm5cbiAgICAgICAgc2VsZi5fY29waWVzID0gY29waWVzXG5cbiAgICBkZWYgX19hZGRfXyhzZWxmLCBvdGhlcik6XG4gICAgICAgIGlmIG5vdCBpc2luc3RhbmNlKG90aGVyLCBCb29rKSBvciBzZWxmLmlzYm4gIT0gb3RoZXIuaXNibjpcbiAgICAgICAgICAgIHJldHVybiBOb3RJbXBsZW1lbnRlZFxuICAgICAgICByZXR1cm4gQm9vayhzZWxmLnRpdGxlLCBzZWxmLmlzYm4sIHNlbGYuX2NvcGllcyArIG90aGVyLl9jb3BpZXMpXG5cbiAgICBkZWYgX19yZXByX18oc2VsZik6XG4gICAgICAgIHJldHVybiBmXCJCb29rKHtzZWxmLnRpdGxlIXJ9LCBjb3BpZXM9e3NlbGYuX2NvcGllc30pXCJcblxuYjEgPSBCb29rKFwiRHVuZVwiLCBcIjk3OC0wNDQxMDEzNTkzXCIsIDIpXG5iMiA9IEJvb2soXCJEdW5lXCIsIFwiOTc4LTA0NDEwMTM1OTNcIiwgMSlcbmNvbWJpbmVkID0gYjEgKyBiMlxucHJpbnQoY29tYmluZWQpICAgIyBCb29rKCdEdW5lJywgY29waWVzPTMpIn0"
 width="100%"
></iframe>

Only implement `__add__` when addition is a meaningful, unsurprising operation for the type. For `Book`, merging copies is reasonable. For an `Invoice`, addition might be confusing.

## Dunder Methods at a Glance

| Method | Enables | Called by |
|---|---|---|
| `__repr__` | Developer-readable string | `repr()`, REPL, logging |
| `__str__` | User-readable string | `print()`, `str()` |
| `__eq__` | `==` comparison by value | `==` operator |
| `__hash__` | Use as dict key or set member | `hash()`, `set`, `dict` |
| `__len__` | `len()` and truthiness | `len()`, `if obj:` |
| `__add__` | `+` operator | `+` |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2R1bmRlcl9tZXRob2RzIGNvZGUgNiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNi5weSIsImNvZGUiOiJjbGFzcyBWZWN0b3I6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHgsIHkpOlxuICAgICAgICBzZWxmLnggPSB4XG4gICAgICAgIHNlbGYueSA9IHlcblxuICAgIGRlZiBfX3JlcHJfXyhzZWxmKTpcbiAgICAgICAgcmV0dXJuIGZcIlZlY3Rvcih7c2VsZi54fSwge3NlbGYueX0pXCJcblxuICAgIGRlZiBfX2VxX18oc2VsZiwgb3RoZXIpOlxuICAgICAgICBpZiBub3QgaXNpbnN0YW5jZShvdGhlciwgVmVjdG9yKTpcbiAgICAgICAgICAgIHJldHVybiBOb3RJbXBsZW1lbnRlZFxuICAgICAgICByZXR1cm4gc2VsZi54ID09IG90aGVyLnggYW5kIHNlbGYueSA9PSBvdGhlci55XG5cbiAgICBkZWYgX19hZGRfXyhzZWxmLCBvdGhlcik6XG4gICAgICAgIGlmIG5vdCBpc2luc3RhbmNlKG90aGVyLCBWZWN0b3IpOlxuICAgICAgICAgICAgcmV0dXJuIE5vdEltcGxlbWVudGVkXG4gICAgICAgIHJldHVybiBWZWN0b3Ioc2VsZi54ICsgb3RoZXIueCwgc2VsZi55ICsgb3RoZXIueSkifQ"
 width="100%"
></iframe>

Add `__len__` to return the integer magnitude (use `int(...)` to keep the return type an integer) and `__bool__` to return `False` for the zero vector `Vector(0, 0)`. Test that `len(Vector(3, 4))` gives `5`, `bool(Vector(0, 0))` gives `False`, and `bool(Vector(1, 0))` gives `True`.

## Conclusion

Dunder methods let your objects integrate naturally into Python's syntax and built-ins. `__repr__` and `__str__` give objects readable representations. `__eq__` makes value-based equality work. `__len__` enables `len()` and truthiness. `__add__` supports the `+` operator. Each method is a specific slot in the data model contract that Python calls at a precise moment, and every one you implement makes your class feel more like a first-class Python type. The next lesson introduces `dataclasses`, which can generate `__repr__`, `__eq__`, and more automatically, eliminating boilerplate for classes that primarily hold data.
