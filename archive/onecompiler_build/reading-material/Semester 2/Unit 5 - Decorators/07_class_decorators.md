## Introduction

Kiran has been thinking of decorators as tools that apply to functions. But Python's `@` syntax works on any object that is callable and takes a single argument, which means it works on class definitions too. When she sees `@dataclass` from Unit 3 in a new light, she realizes she has been using a class decorator all along without knowing the term.

This lesson introduces class decorators: decorators that receive a class object and return a modified class (or a replacement class). It also shows how a class itself can act as a decorator for functions, by implementing `__call__`.

![A class definition being passed into a decorator that adds class-level attributes or modifies methods, returning the modified class](images/07_class_decorators.png)

## Decorating a Class Definition

A class decorator receives the class object itself and returns a class. The simplest use is adding or modifying class attributes.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2NsYXNzX2RlY29yYXRvcnMgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6ImRlZiBhZGRfcmVwcihjbHMpOlxuICAgIGRlZiBfX3JlcHJfXyhzZWxmKTpcbiAgICAgICAgYXR0cnMgPSBcIiwgXCIuam9pbihmXCJ7a309e3Yhcn1cIiBmb3IgaywgdiBpbiBzZWxmLl9fZGljdF9fLml0ZW1zKCkpXG4gICAgICAgIHJldHVybiBmXCJ7Y2xzLl9fbmFtZV9ffSh7YXR0cnN9KVwiXG4gICAgY2xzLl9fcmVwcl9fID0gX19yZXByX19cbiAgICByZXR1cm4gY2xzXG5cbkBhZGRfcmVwclxuY2xhc3MgQm9vazpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgdGl0bGUsIGlzYm4pOlxuICAgICAgICBzZWxmLnRpdGxlID0gdGl0bGVcbiAgICAgICAgc2VsZi5pc2JuID0gaXNiblxuXG5iID0gQm9vayhcIkR1bmVcIiwgXCI5NzgtMDQ0MTAxMzU5M1wiKVxucHJpbnQoYikgICAjIEJvb2sodGl0bGU9J0R1bmUnLCBpc2JuPSc5NzgtMDQ0MTAxMzU5MycpIn0"
 width="100%"
></iframe>

`add_repr` receives `Book`, adds a `__repr__` method to the class object, and returns the modified class. Every instance of `Book` now has a generated `__repr__`.

This is exactly what `@dataclass` does: it receives the class, inspects the field annotations, generates `__init__`, `__repr__`, and `__eq__`, adds them to the class, and returns the modified class.

## A Singleton Class Decorator

A more substantial use of class decorators: enforcing that only one instance of a class can ever exist (the Singleton pattern).

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2NsYXNzX2RlY29yYXRvcnMgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6ImRlZiBzaW5nbGV0b24oY2xzKTpcbiAgICBpbnN0YW5jZXMgPSB7fVxuICAgIGRlZiBnZXRfaW5zdGFuY2UoKmFyZ3MsICoqa3dhcmdzKTpcbiAgICAgICAgaWYgY2xzIG5vdCBpbiBpbnN0YW5jZXM6XG4gICAgICAgICAgICBpbnN0YW5jZXNbY2xzXSA9IGNscygqYXJncywgKiprd2FyZ3MpXG4gICAgICAgIHJldHVybiBpbnN0YW5jZXNbY2xzXVxuICAgIHJldHVybiBnZXRfaW5zdGFuY2VcblxuQHNpbmdsZXRvblxuY2xhc3MgRGF0YWJhc2VDb25uZWN0aW9uOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCB1cmwpOlxuICAgICAgICBzZWxmLnVybCA9IHVybFxuICAgICAgICBwcmludChmXCJDb25uZWN0aW5nIHRvIHt1cmx9XCIpXG5cbmRiMSA9IERhdGFiYXNlQ29ubmVjdGlvbihcInNxbGl0ZTovLy9saWJyYXJ5LmRiXCIpXG4jIENvbm5lY3RpbmcgdG8gc3FsaXRlOi8vL2xpYnJhcnkuZGJcblxuZGIyID0gRGF0YWJhc2VDb25uZWN0aW9uKFwic3FsaXRlOi8vL2xpYnJhcnkuZGJcIilcbiMgKG5vIHNlY29uZCBwcmludCAtLSBzYW1lIG9iamVjdCByZXR1cm5lZClcblxucHJpbnQoZGIxIGlzIGRiMikgICAjIFRydWUifQ"
 width="100%"
></iframe>

Note that `singleton` replaces the class with a function (`get_instance`). This means `isinstance(db1, DatabaseConnection)` would be `False` after the replacement. For a production singleton, a more careful implementation would preserve the class object. But this example shows the core idea: the decorator does not have to return the same class it received.

## Using a Class as a Function Decorator

A class with a `__call__` method can act as a decorator for functions. This is useful when the decorator needs to maintain state across calls, because class instances have natural attribute storage.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2NsYXNzX2RlY29yYXRvcnMgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6ImltcG9ydCBmdW5jdG9vbHNcblxuY2xhc3MgQ2FsbENvdW50ZXI6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGZuKTpcbiAgICAgICAgZnVuY3Rvb2xzLnVwZGF0ZV93cmFwcGVyKHNlbGYsIGZuKVxuICAgICAgICBzZWxmLmZuID0gZm5cbiAgICAgICAgc2VsZi5jYWxsX2NvdW50ID0gMFxuXG4gICAgZGVmIF9fY2FsbF9fKHNlbGYsICphcmdzLCAqKmt3YXJncyk6XG4gICAgICAgIHNlbGYuY2FsbF9jb3VudCArPSAxXG4gICAgICAgIHJldHVybiBzZWxmLmZuKCphcmdzLCAqKmt3YXJncylcblxuQENhbGxDb3VudGVyXG5kZWYgZ2V0X2Jvb2soaXNibik6XG4gICAgcmV0dXJuIHtcImlzYm5cIjogaXNibn1cblxuZ2V0X2Jvb2soXCI5NzgtMDAxXCIpXG5nZXRfYm9vayhcIjk3OC0wMDJcIilcbmdldF9ib29rKFwiOTc4LTAwM1wiKVxuXG5wcmludChnZXRfYm9vay5jYWxsX2NvdW50KSAgICMgMyJ9"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2NsYXNzX2RlY29yYXRvcnMgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6InJlZ2lzdHJ5ID0ge31cblxuZGVmIHJlZ2lzdGVyKGNscyk6XG4gICAgcmVnaXN0cnlbY2xzLl9fbmFtZV9fXSA9IGNsc1xuICAgIHJldHVybiBjbHNcblxuQHJlZ2lzdGVyXG5jbGFzcyBCb29rOlxuICAgIHBhc3NcblxuQHJlZ2lzdGVyXG5jbGFzcyBFQm9vazpcbiAgICBwYXNzXG5cbnByaW50KHJlZ2lzdHJ5KVxuIyB7J0Jvb2snOiA8Y2xhc3MgJ19fbWFpbl9fLkJvb2snPiwgJ0VCb29rJzogPGNsYXNzICdfX21haW5fXy5FQm9vayc-fSJ9"
 width="100%"
></iframe>

Then add a `@register` to a third class and confirm it appears in the registry without any manual insertion. This pattern is used by plugin systems, ORM field registration, and web framework route registration.

## Conclusion

Class decorators apply the `@` syntax to class definitions, receiving the class object and returning a modified or replacement class. The same mechanism underlies `@dataclass`. Classes with `__call__` can also act as function decorators, providing natural attribute storage for state. The final lesson of this unit collects the most widely-used real-world decorators into one place, showing timing, caching, and logging in production-grade form.
