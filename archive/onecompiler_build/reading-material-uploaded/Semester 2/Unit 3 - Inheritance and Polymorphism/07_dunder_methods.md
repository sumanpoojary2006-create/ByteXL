## Introduction

Dev has a working `Book` class, but using it in daily development keeps feeling slightly awkward. When he prints a book object, the output is `<__main__.Book object at 0x10a3f2340>`, which tells him nothing useful. When he compares two books with the same ISBN, Python says they are not equal because they are different objects in memory. When he tries to add book copies with `+`, Python throws an error.

These are not fundamental limitations of the language. They are gaps in the class's data model contract. The previous units defined the concept of dunder methods; this lesson implements the most useful ones on a real domain object and shows exactly how each one changes the way Python interacts with the class.

![](images/07_dunder_methods.png)

## __repr__ and __str__: Making Objects Readable

`__repr__` is the developer representation, shown in the REPL and `repr()`. It should be unambiguous and ideally reproducible as valid Python. `__str__` is the user-facing representation, used by `print()` and `str()`. If `__str__` is absent, `__repr__` is used as a fallback.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-07-dunder-methods-001-39eab2299f.html"
 width="100%"
></iframe>

Always implement `__repr__` on any class you will use in interactive development. It makes debugging dramatically faster.

## __eq__: Making Objects Comparable

By default, `==` compares identity (whether two references point to the same object in memory). To make objects compare by their data instead, implement `__eq__`.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-07-dunder-methods-002-fc05276395.html"
 width="100%"
></iframe>

Returning `NotImplemented` when the types do not match is the correct protocol: it tells Python to try the comparison from the other side before giving up.

Note: defining `__eq__` makes objects unhashable by default (Python removes the default `__hash__` method). If you want your objects to be usable in sets or as dictionary keys, also define `__hash__`:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-07-dunder-methods-003-96019d42d6.html"
 width="100%"
></iframe>

## __len__: Giving an Object a Length

`__len__` makes `len(obj)` work and also determines truthiness: an object with `__len__` is falsy when its length is zero.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-07-dunder-methods-004-f556837e6d.html"
 width="100%"
></iframe>

## __add__: Supporting the + Operator

When it makes conceptual sense to add two objects together, `__add__` enables the `+` operator. For a `Book`, adding copies from two instances might represent merging stock:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-07-dunder-methods-005-83ae1067e2.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-07-dunder-methods-006-335d127186.html"
 width="100%"
></iframe>

Add `__len__` to return the integer magnitude (use `int(...)` to keep the return type an integer) and `__bool__` to return `False` for the zero vector `Vector(0, 0)`. Test that `len(Vector(3, 4))` gives `5`, `bool(Vector(0, 0))` gives `False`, and `bool(Vector(1, 0))` gives `True`.

## Conclusion

Dunder methods let your objects integrate naturally into Python's syntax and built-ins. `__repr__` and `__str__` give objects readable representations. `__eq__` makes value-based equality work. `__len__` enables `len()` and truthiness. `__add__` supports the `+` operator. Each method is a specific slot in the data model contract that Python calls at a precise moment, and every one you implement makes your class feel more like a first-class Python type. The next lesson introduces `dataclasses`, which can generate `__repr__`, `__eq__`, and more automatically, eliminating boilerplate for classes that primarily hold data.
