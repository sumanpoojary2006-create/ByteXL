## Introduction

Priya's team has a dilemma. Half the codebase already accesses `book.copies` as a plain attribute. Renaming it to `_copies` and adding a `copies_available()` method would fix the design, but it would break every line of code that already uses `book.copies`. She needs a way to add validation logic to an attribute without changing how callers interact with it, so that `book.copies` still looks like a plain attribute from the outside but secretly runs validation code when read or written.

Python's `@property` decorator solves this exactly. It is one of the most useful tools in Python's object-oriented toolkit, and it is the reason you will almost never see explicit "getter" and "setter" methods in well-designed Python code.

![](images/04_properties_getters_setters.png)

## The Simplest Property: A Computed Read-Only Value

The most basic use of `@property` is turning a method into something that reads like an attribute. Rather than calling `book.is_available()`, callers can read `book.is_available` with no parentheses, and Python calls the method invisibly.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-2-encapsulation-and-abstraction-04-properties-and-getterssette-001-a1e9df935e.html"
 width="100%"
></iframe>

The `@property` decorator tells Python: "when someone reads `obj.is_available`, call this function." The result is a cleaner, more natural interface: `if book.is_available:` reads like English rather than `if book.is_available():`.

## Adding a Setter: Validation on Write

The real power of properties appears when you add a **setter**. A setter runs code whenever someone writes to the attribute, which is exactly where Priya needs to add her validation.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-2-encapsulation-and-abstraction-04-properties-and-getterssette-002-f71c719bc0.html"
 width="100%"
></iframe>

Notice a detail in `__init__`: `self.copies = copies` rather than `self._copies = copies`. This is intentional: by routing through the setter from the very start, validation applies even at object creation time. Any invalid initial value is caught immediately.

## Adding a Deleter (Rarely Needed)

A third decorator, `@name.deleter`, runs code when someone calls `del obj.name`. This is rarely needed but occasionally useful, for example when deletion should trigger cleanup.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-2-encapsulation-and-abstraction-04-properties-and-getterssette-003-5ba08aba3b.html"
 width="100%"
></iframe>

## Why Python Does Not Use get_x() and set_x() Methods

In Java and C++, the standard pattern is to write `getCopies()` and `setCopies()` methods explicitly. Python's `@property` makes this unnecessary: you can start with a plain attribute and add a property later without changing any code that uses the object. This is the Pythonic approach: start simple, add complexity only when you need it.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-2-encapsulation-and-abstraction-04-properties-and-getterssette-004-f2c9fa3b8c.html"
 width="100%"
></iframe>

Every caller that used `book.copies = 2` before the refactor still uses `book.copies = 2` after. Nothing broke. The validation just appeared silently behind the same interface.

## Properties at a Glance

| Decorator | What it defines | When it runs |
|---|---|---|
| `@property` | The getter | When `obj.name` is read |
| `@name.setter` | The setter | When `obj.name = value` is written |
| `@name.deleter` | The deleter | When `del obj.name` is called |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-2-encapsulation-and-abstraction-04-properties-and-getterssette-005-bbe4a6aae8.html"
 width="100%"
></iframe>

Test this class by reading both `celsius` and `fahrenheit` (note: `fahrenheit` is read-only since it has no setter). Try to set `celsius` to `-300` and confirm the error. Then add a `fahrenheit` setter that converts the value back to Celsius and stores it, so that setting `t.fahrenheit = 32` results in `t.celsius == 0`.

## Conclusion

The `@property` decorator transforms method calls into attribute-like access, letting you add validation, computation, and cleanup behind a clean interface without changing any code that uses the object. The getter runs on read, the setter on write, and you can start with a plain attribute and add a property later without breaking anything. The next lesson moves from attribute access to a larger question: how do you design a class that hides not just its data, but the complexity of its entire implementation, presenting only what callers need to know?
