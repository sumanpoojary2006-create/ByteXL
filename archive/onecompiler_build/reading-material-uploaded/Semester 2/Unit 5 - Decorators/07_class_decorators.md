## Introduction

Kiran has been thinking of decorators as tools that apply to functions. But Python's `@` syntax works on any object that is callable and takes a single argument, which means it works on class definitions too. When she sees `@dataclass` from Unit 3 in a new light, she realizes she has been using a class decorator all along without knowing the term.

This lesson introduces class decorators: decorators that receive a class object and return a modified class (or a replacement class). It also shows how a class itself can act as a decorator for functions, by implementing `__call__`.

![A class definition being passed into a decorator that adds class-level attributes or modifies methods, returning the modified class](images/07_class_decorators.png)

## Decorating a Class Definition

A class decorator receives the class object itself and returns a class. The simplest use is adding or modifying class attributes.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-5-decorators-07-class-decorators-001-4389677292.html"
 width="100%"
></iframe>

`add_repr` receives `Book`, adds a `__repr__` method to the class object, and returns the modified class. Every instance of `Book` now has a generated `__repr__`.

This is exactly what `@dataclass` does: it receives the class, inspects the field annotations, generates `__init__`, `__repr__`, and `__eq__`, adds them to the class, and returns the modified class.

## A Singleton Class Decorator

A more substantial use of class decorators: enforcing that only one instance of a class can ever exist (the Singleton pattern).

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-5-decorators-07-class-decorators-002-e5fa0b4982.html"
 width="100%"
></iframe>

Note that `singleton` replaces the class with a function (`get_instance`). This means `isinstance(db1, DatabaseConnection)` would be `False` after the replacement. For a production singleton, a more careful implementation would preserve the class object. But this example shows the core idea: the decorator does not have to return the same class it received.

## Using a Class as a Function Decorator

A class with a `__call__` method can act as a decorator for functions. This is useful when the decorator needs to maintain state across calls, because class instances have natural attribute storage.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-5-decorators-07-class-decorators-003-575bd56067.html"
 width="100%"
></iframe>

`@CallCounter` makes `get_book` an instance of `CallCounter`. Calling `get_book(...)` calls `get_book.__call__(...)`. The `call_count` attribute persists naturally on the instance. `functools.update_wrapper(self, fn)` serves the same role as `@functools.wraps(fn)` for class-based wrappers.

## When to Use Class Decorators

Function decorators (closures) are shorter and cover most cases. Class decorators are worth choosing when:
- The decorator needs significant state (a counter, a cache, a configuration object) that would clutter a closure.
- You want the decorated object to have attributes the caller can inspect or modify (like `get_book.call_count`).
- You are decorating a class definition itself to add methods, enforce constraints, or replace the class with a managed version.

## Class Decorators at a Glance

| Use | Pattern | Example |
|---|---|---|
| Decorate a class definition | `def decorator(cls): ...; return cls` | `@add_repr`, `@dataclass`, `@singleton` |
| Class as a function decorator | `class Decorator: def __call__(self, ...)` | `@CallCounter` |
| State in a function decorator | Use a closure with a mutable container | Simpler for light state |
| State in a class decorator | Use `self.attribute` | Cleaner for heavier state |

## Your Turn

Write a `@register` class decorator that keeps a registry of all decorated classes. Each class that receives `@register` is added to a module-level dictionary keyed by the class name.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-5-decorators-07-class-decorators-004-1d264cfc42.html"
 width="100%"
></iframe>

Then add a `@register` to a third class and confirm it appears in the registry without any manual insertion. This pattern is used by plugin systems, ORM field registration, and web framework route registration.

## Conclusion

Class decorators apply the `@` syntax to class definitions, receiving the class object and returning a modified or replacement class. The same mechanism underlies `@dataclass`. Classes with `__call__` can also act as function decorators, providing natural attribute storage for state. The final lesson of this unit collects the most widely-used real-world decorators into one place, showing timing, caching, and logging in production-grade form.
