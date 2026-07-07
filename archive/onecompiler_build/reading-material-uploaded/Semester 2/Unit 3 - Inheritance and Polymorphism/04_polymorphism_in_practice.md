## Introduction

Dev's manager asks him to generate a checkout summary: for every item in the library catalog, print the title and its checkout policy. Dev has books, ebooks, reference books, and magazines, all stored in one flat list. He writes a loop that calls `item.checkout_policy()` on each one. It just works. He does not need an `if isinstance(item, Book):` branch or a separate function per type.

His manager asks how that works. Dev pauses, because he has been doing it instinctively without being able to name it. The answer is **polymorphism**: the ability to call the same method on objects of different types and get the behavior that is correct for each object's actual type, without the calling code knowing what that type is.

![](images/04_polymorphism_in_practice.png)

## Polymorphism: One Interface, Many Behaviors

Polymorphism (from the Greek for "many forms") means one name, multiple implementations. When Dev's loop calls `item.checkout_policy()`, Python dispatches the call to the version of `checkout_policy` that belongs to the object's actual class, whatever that class is.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-04-polymorphism-in-practice-001-2be955ba1a.html"
 width="100%"
></iframe>

The loop is four lines. It has no type checks. Every item responds to `checkout_policy()`, each with the behavior appropriate to its class. Adding a new item type in the future requires only defining the new class, not modifying the loop.

## Why Not Just Use isinstance() and if-Branches?

It is tempting to write the equivalent logic with explicit type checks:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-04-polymorphism-in-practice-002-ed2faa040e.html"
 width="100%"
></iframe>

This works, but it breaks when a new type appears. Every place in the codebase that has this pattern needs to be updated when `Audiobook` or `Magazine` is added. With polymorphism, no existing code changes: the new class provides its own `checkout_policy()`, and every existing loop automatically uses it.

The test for whether to use polymorphism or a type check: if adding a new type should require changing the function that uses the objects, you are probably missing polymorphism. If adding a new type should require only writing the new class, polymorphism is the right design.

## Polymorphism Beyond Inheritance: Duck Typing

Polymorphism in Python does not strictly require inheritance. Because Python uses duck typing (if an object has the right method, it qualifies), objects from completely unrelated class hierarchies can be treated polymorphically as long as they share the same method name.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-04-polymorphism-in-practice-003-70c12d6f97.html"
 width="100%"
></iframe>

This is more flexible than Java-style interface declarations: no shared base class or explicit registration is needed. The trade-off is that the shared interface is informal and invisible until an object is actually used.

## A Practical Example: Generating a Report

Polymorphism makes it easy to write functions that work across an entire collection without knowing the specifics:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-04-polymorphism-in-practice-004-5196f96863.html"
 width="100%"
></iframe>

`print_catalog_report` is written once and works with any mix of item types, now and in the future. Adding `AudioBook` to the system requires only writing `AudioBook.checkout_policy()`. The report function never changes.

## Polymorphism at a Glance

| Concept | What it means |
|---|---|
| Polymorphism | One method name, many implementations |
| Dispatch | Python chooses the implementation based on the object's actual class |
| Why it matters | Adding new types does not require editing existing functions |
| Duck typing | Objects from different hierarchies work polymorphically if they share method names |
| Anti-pattern | `isinstance()` chains are usually a sign that polymorphism is missing |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-3-inheritance-and-polymorphism-04-polymorphism-in-practice-005-77bc84d67d.html"
 width="100%"
></iframe>

Write a function `log_readings(sensors)` that loops over the list and prints each `sensor.read()` without any `isinstance()` checks. Then add a `CO2Sensor` with a `read()` method and pass it into `log_readings` to confirm the function works without any modification.

## Conclusion

Polymorphism means the calling code uses a single, stable method name and lets each object's class determine what the method actually does. The practical effect: adding a new type to a polymorphic system requires only writing the new class, not updating any existing loops or functions. Python's duck typing extends this further, letting unrelated classes participate in a polymorphic interface simply by sharing a method name. The next lesson covers a case that complicates this picture: what happens when a class inherits from more than one parent, and how Python decides which version of a method to use.
