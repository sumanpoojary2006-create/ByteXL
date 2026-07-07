## Introduction

Dev's manager asks him to generate a checkout summary: for every item in the library catalog, print the title and its checkout policy. Dev has books, ebooks, reference books, and magazines, all stored in one flat list. He writes a loop that calls `item.checkout_policy()` on each one. It just works. He does not need an `if isinstance(item, Book):` branch or a separate function per type.

His manager asks how that works. Dev pauses, because he has been doing it instinctively without being able to name it. The answer is **polymorphism**: the ability to call the same method on objects of different types and get the behavior that is correct for each object's actual type, without the calling code knowing what that type is.

![](images/04_polymorphism_in_practice.png)

## Polymorphism: One Interface, Many Behaviors

Polymorphism (from the Greek for "many forms") means one name, multiple implementations. When Dev's loop calls `item.checkout_policy()`, Python dispatches the call to the version of `checkout_policy` that belongs to the object's actual class, whatever that class is.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3BvbHltb3JwaGlzbV9pbl9wcmFjdGljZSBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoiY2xhc3MgTGlicmFyeUl0ZW06XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHRpdGxlKTpcbiAgICAgICAgc2VsZi50aXRsZSA9IHRpdGxlXG5cbiAgICBkZWYgY2hlY2tvdXRfcG9saWN5KHNlbGYpOlxuICAgICAgICByZXR1cm4gXCIyMS1kYXkgbG9hblwiXG5cbmNsYXNzIEVCb29rKExpYnJhcnlJdGVtKTpcbiAgICBkZWYgY2hlY2tvdXRfcG9saWN5KHNlbGYpOlxuICAgICAgICByZXR1cm4gXCJBbHdheXMgYXZhaWxhYmxlXCJcblxuY2xhc3MgUmVmZXJlbmNlQm9vayhMaWJyYXJ5SXRlbSk6XG4gICAgZGVmIGNoZWNrb3V0X3BvbGljeShzZWxmKTpcbiAgICAgICAgcmV0dXJuIFwiSW4tbGlicmFyeSB1c2Ugb25seVwiXG5cbmNhdGFsb2cgPSBbXG4gICAgTGlicmFyeUl0ZW0oXCJEdW5lXCIpLFxuICAgIEVCb29rKFwiRm91bmRhdGlvblwiKSxcbiAgICBSZWZlcmVuY2VCb29rKFwiRW5jeWNsb3BlZGlhIEJyaXRhbm5pY2FcIiksXG4gICAgTGlicmFyeUl0ZW0oXCJTaG9ndW5cIiksXG5dXG5cbmZvciBpdGVtIGluIGNhdGFsb2c6XG4gICAgcHJpbnQoZlwie2l0ZW0udGl0bGV9OiB7aXRlbS5jaGVja291dF9wb2xpY3koKX1cIilcblxuIyBEdW5lOiAyMS1kYXkgbG9hblxuIyBGb3VuZGF0aW9uOiBBbHdheXMgYXZhaWxhYmxlXG4jIEVuY3ljbG9wZWRpYSBCcml0YW5uaWNhOiBJbi1saWJyYXJ5IHVzZSBvbmx5XG4jIFNob2d1bjogMjEtZGF5IGxvYW4ifQ"
 width="100%"
></iframe>

The loop is four lines. It has no type checks. Every item responds to `checkout_policy()`, each with the behavior appropriate to its class. Adding a new item type in the future requires only defining the new class, not modifying the loop.

## Why Not Just Use isinstance() and if-Branches?

It is tempting to write the equivalent logic with explicit type checks:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3BvbHltb3JwaGlzbV9pbl9wcmFjdGljZSBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoiIyBBbnRpLXBhdHRlcm46IHR5cGUtY2hlY2tpbmcgaW5zdGVhZCBvZiBwb2x5bW9ycGhpc21cbmZvciBpdGVtIGluIGNhdGFsb2c6XG4gICAgaWYgaXNpbnN0YW5jZShpdGVtLCBFQm9vayk6XG4gICAgICAgIHByaW50KGZcIntpdGVtLnRpdGxlfTogQWx3YXlzIGF2YWlsYWJsZVwiKVxuICAgIGVsaWYgaXNpbnN0YW5jZShpdGVtLCBSZWZlcmVuY2VCb29rKTpcbiAgICAgICAgcHJpbnQoZlwie2l0ZW0udGl0bGV9OiBJbi1saWJyYXJ5IHVzZSBvbmx5XCIpXG4gICAgZWxzZTpcbiAgICAgICAgcHJpbnQoZlwie2l0ZW0udGl0bGV9OiAyMS1kYXkgbG9hblwiKSJ9"
 width="100%"
></iframe>

This works, but it breaks when a new type appears. Every place in the codebase that has this pattern needs to be updated when `Audiobook` or `Magazine` is added. With polymorphism, no existing code changes: the new class provides its own `checkout_policy()`, and every existing loop automatically uses it.

The test for whether to use polymorphism or a type check: if adding a new type should require changing the function that uses the objects, you are probably missing polymorphism. If adding a new type should require only writing the new class, polymorphism is the right design.

## Polymorphism Beyond Inheritance: Duck Typing

Polymorphism in Python does not strictly require inheritance. Because Python uses duck typing (if an object has the right method, it qualifies), objects from completely unrelated class hierarchies can be treated polymorphically as long as they share the same method name.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3BvbHltb3JwaGlzbV9pbl9wcmFjdGljZSBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoiY2xhc3MgQm9va0FQSTpcbiAgICBkZWYgY2hlY2tvdXRfcG9saWN5KHNlbGYpOlxuICAgICAgICByZXR1cm4gXCIyMS1kYXkgbG9hbiAoZGlnaXRhbCByZWNvcmQpXCJcblxuY2xhc3MgUGh5c2ljYWxCb29rOlxuICAgIGRlZiBjaGVja291dF9wb2xpY3koc2VsZik6XG4gICAgICAgIHJldHVybiBcIjIxLWRheSBsb2FuIChwaHlzaWNhbClcIlxuXG4jIE5laXRoZXIgaW5oZXJpdHMgZnJvbSBMaWJyYXJ5SXRlbSwgeWV0IGJvdGggd29yayBpbiB0aGUgc2FtZSBsb29wOlxuaXRlbXMgPSBbQm9va0FQSSgpLCBQaHlzaWNhbEJvb2soKV1cbmZvciBpdGVtIGluIGl0ZW1zOlxuICAgIHByaW50KGl0ZW0uY2hlY2tvdXRfcG9saWN5KCkpIn0"
 width="100%"
></iframe>

This is more flexible than Java-style interface declarations: no shared base class or explicit registration is needed. The trade-off is that the shared interface is informal and invisible until an object is actually used.

## A Practical Example: Generating a Report

Polymorphism makes it easy to write functions that work across an entire collection without knowing the specifics:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3BvbHltb3JwaGlzbV9pbl9wcmFjdGljZSBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoiZGVmIHByaW50X2NhdGFsb2dfcmVwb3J0KGl0ZW1zKTpcbiAgICBwcmludChcIj09PSBDYXRhbG9nIFJlcG9ydCA9PT1cIilcbiAgICBmb3IgaXRlbSBpbiBpdGVtczpcbiAgICAgICAgcG9saWN5ID0gaXRlbS5jaGVja291dF9wb2xpY3koKVxuICAgICAgICBwcmludChmXCIgIHtpdGVtLnRpdGxlOjw0MH0ge3BvbGljeX1cIilcbiAgICBwcmludChmXCJUb3RhbCBpdGVtczoge2xlbihpdGVtcyl9XCIpIn0"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3BvbHltb3JwaGlzbV9pbl9wcmFjdGljZSBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoiY2xhc3MgU2Vuc29yOlxuICAgIGRlZiByZWFkKHNlbGYpOlxuICAgICAgICByZXR1cm4gMC4wXG5cbmNsYXNzIFRlbXBlcmF0dXJlU2Vuc29yKFNlbnNvcik6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHZhbHVlX2NlbHNpdXMpOlxuICAgICAgICBzZWxmLnZhbHVlID0gdmFsdWVfY2Vsc2l1c1xuXG4gICAgZGVmIHJlYWQoc2VsZik6XG4gICAgICAgIHJldHVybiBzZWxmLnZhbHVlXG5cbmNsYXNzIEh1bWlkaXR5U2Vuc29yKFNlbnNvcik6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHBlcmNlbnQpOlxuICAgICAgICBzZWxmLnBlcmNlbnQgPSBwZXJjZW50XG5cbiAgICBkZWYgcmVhZChzZWxmKTpcbiAgICAgICAgcmV0dXJuIHNlbGYucGVyY2VudFxuXG5jbGFzcyBQcmVzc3VyZVNlbnNvcihTZW5zb3IpOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBocGEpOlxuICAgICAgICBzZWxmLmhwYSA9IGhwYVxuXG4gICAgZGVmIHJlYWQoc2VsZik6XG4gICAgICAgIHJldHVybiBzZWxmLmhwYVxuXG5zZW5zb3JzID0gW1xuICAgIFRlbXBlcmF0dXJlU2Vuc29yKDIzLjUpLFxuICAgIEh1bWlkaXR5U2Vuc29yKDY1LjApLFxuICAgIFByZXNzdXJlU2Vuc29yKDEwMTMuMjUpLFxuXSJ9"
 width="100%"
></iframe>

Write a function `log_readings(sensors)` that loops over the list and prints each `sensor.read()` without any `isinstance()` checks. Then add a `CO2Sensor` with a `read()` method and pass it into `log_readings` to confirm the function works without any modification.

## Conclusion

Polymorphism means the calling code uses a single, stable method name and lets each object's class determine what the method actually does. The practical effect: adding a new type to a polymorphic system requires only writing the new class, not updating any existing loops or functions. Python's duck typing extends this further, letting unrelated classes participate in a polymorphic interface simply by sharing a method name. The next lesson covers a case that complicates this picture: what happens when a class inherits from more than one parent, and how Python decides which version of a method to use.
