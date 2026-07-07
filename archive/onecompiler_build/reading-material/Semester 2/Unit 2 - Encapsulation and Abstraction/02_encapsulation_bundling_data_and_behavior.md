## Introduction

After the negative-copies incident, Priya explains the problem to her tech lead. He listens, nods, and says one word: "Encapsulation." He means the idea that a class should own its data completely: the only way to read or change an object's internal state should be through the methods the class deliberately provides. Anyone using the `Book` class should not need to know how it stores the copy count internally, and more importantly, should not be able to reach in and set it to whatever they like.

This is the first and most fundamental principle of object-oriented design in production code, and this lesson makes it concrete.

![](images/02_encapsulation_data_and_behavior.png)

## What Encapsulation Actually Means

Encapsulation has two parts:

**Bundling**: the data (attributes) and the operations that work on that data (methods) live together in one class. A `Book` knows how to check itself out rather than requiring an external function to manipulate its attributes.

**Protection**: the internal representation is hidden from the outside world. Code that uses `Book` objects should not know or care whether copies are stored as an `int`, a list, or a dictionary. The class makes that decision and exposes only a clean interface.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2VuY2Fwc3VsYXRpb25fYnVuZGxpbmdfZGF0YV9hbmRfYmVoYXZpb3IgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6ImNsYXNzIEJvb2s6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHRpdGxlLCBpc2JuLCBjb3BpZXMpOlxuICAgICAgICBzZWxmLnRpdGxlID0gdGl0bGVcbiAgICAgICAgc2VsZi5pc2JuID0gaXNiblxuICAgICAgICBzZWxmLl9jb3BpZXMgPSBjb3BpZXMgICAgICAjIGludGVybmFsOyBjYWxsZXJzIHNob3VsZCBub3QgdG91Y2ggZGlyZWN0bHlcblxuICAgIGRlZiBjaGVja19vdXQoc2VsZik6XG4gICAgICAgIGlmIHNlbGYuX2NvcGllcyA8IDE6XG4gICAgICAgICAgICByYWlzZSBWYWx1ZUVycm9yKGZcIk5vIGNvcGllcyBvZiAne3NlbGYudGl0bGV9JyBhdmFpbGFibGVcIilcbiAgICAgICAgc2VsZi5fY29waWVzIC09IDFcblxuICAgIGRlZiByZXR1cm5fY29weShzZWxmKTpcbiAgICAgICAgc2VsZi5fY29waWVzICs9IDFcblxuICAgIGRlZiBjb3BpZXNfYXZhaWxhYmxlKHNlbGYpOlxuICAgICAgICByZXR1cm4gc2VsZi5fY29waWVzIn0"
 width="100%"
></iframe>

The single underscore on `_copies` is a Python convention meaning "this is an internal implementation detail; please do not touch it from outside this class." Python does not enforce this (unlike Java or C++), but it is a clear signal that respecting it is part of using the class correctly.

## Why the Interface Matters More Than the Implementation

Once Priya wraps `_copies` in methods, something interesting happens: she can change the internal representation without breaking any code that uses `Book`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2VuY2Fwc3VsYXRpb25fYnVuZGxpbmdfZGF0YV9hbmRfYmVoYXZpb3IgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6IiMgVmVyc2lvbiAxOiBjb3BpZXMgaXMgYSBwbGFpbiBpbnRlZ2VyXG5jbGFzcyBCb29rOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCB0aXRsZSwgY29waWVzKTpcbiAgICAgICAgc2VsZi5fY29waWVzID0gY29waWVzXG5cbiAgICBkZWYgY29waWVzX2F2YWlsYWJsZShzZWxmKTpcbiAgICAgICAgcmV0dXJuIHNlbGYuX2NvcGllc1xuXG4jIFZlcnNpb24gMjogY29waWVzIGlzIHN0b3JlZCBwZXItYnJhbmNoIChkaWZmZXJlbnQgaW50ZXJuYWwgcmVwcmVzZW50YXRpb24pXG5jbGFzcyBCb29rOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCB0aXRsZSwgY29waWVzX2J5X2JyYW5jaCk6XG4gICAgICAgIHNlbGYuX2NvcGllc19ieV9icmFuY2ggPSBjb3BpZXNfYnlfYnJhbmNoICAgIyB7XCJtYWluXCI6IDIsIFwid2VzdFwiOiAxfVxuXG4gICAgZGVmIGNvcGllc19hdmFpbGFibGUoc2VsZik6XG4gICAgICAgIHJldHVybiBzdW0oc2VsZi5fY29waWVzX2J5X2JyYW5jaC52YWx1ZXMoKSkifQ"
 width="100%"
></iframe>

Any code that calls `book.copies_available()` works identically in both versions. The caller never knew how copies were stored, so they are unaffected by the change. This is the practical payoff of encapsulation: it decouples the implementation from the interface, making the class's internals changeable without cascading edits throughout the codebase.

## Validation at the Point of Entry

Encapsulation also lets you validate data at the one place where it enters the object rather than trusting callers to pass valid values. If the copy count can only be set through `__init__` and `return_copy`, you can add checks in exactly those places and know they will always run.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2VuY2Fwc3VsYXRpb25fYnVuZGxpbmdfZGF0YV9hbmRfYmVoYXZpb3IgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6ImNsYXNzIEJvb2s6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHRpdGxlLCBjb3BpZXMpOlxuICAgICAgICBpZiBjb3BpZXMgPCAwOlxuICAgICAgICAgICAgcmFpc2UgVmFsdWVFcnJvcihmXCJjb3BpZXMgbXVzdCBiZSBub24tbmVnYXRpdmUsIGdvdCB7Y29waWVzfVwiKVxuICAgICAgICBzZWxmLnRpdGxlID0gdGl0bGVcbiAgICAgICAgc2VsZi5fY29waWVzID0gY29waWVzXG5cbiAgICBkZWYgcmV0dXJuX2NvcHkoc2VsZik6XG4gICAgICAgIHNlbGYuX2NvcGllcyArPSAxXG5cbiAgICBkZWYgY2hlY2tfb3V0KHNlbGYpOlxuICAgICAgICBpZiBzZWxmLl9jb3BpZXMgPCAxOlxuICAgICAgICAgICAgcmFpc2UgVmFsdWVFcnJvcihmXCJObyBjb3BpZXMgb2YgJ3tzZWxmLnRpdGxlfScgYXZhaWxhYmxlXCIpXG4gICAgICAgIHNlbGYuX2NvcGllcyAtPSAxXG5cbiAgICBkZWYgY29waWVzX2F2YWlsYWJsZShzZWxmKTpcbiAgICAgICAgcmV0dXJuIHNlbGYuX2NvcGllc1xuXG5iID0gQm9vayhcIkR1bmVcIiwgLTEpICAgIyBlcnJvciEifQ"
 width="100%"
></iframe>

The `ValueError` is raised at object creation, not somewhere later when the negative count causes a mysterious failure. The problem is caught where it is introduced, not where it first manifests.

## Encapsulation Is Not Just About Hiding

A common misconception is that encapsulation is mainly about making things private. It is actually about **keeping related things together**. The `check_out` logic belongs in `Book` because it is intimately tied to what `_copies` means. Spreading that logic across multiple files or modules means changes to the copy-counting mechanism require hunting down every place copies are manipulated.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2VuY2Fwc3VsYXRpb25fYnVuZGxpbmdfZGF0YV9hbmRfYmVoYXZpb3IgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6IiMgRnJhZ21lbnRlZCAobm90IGVuY2Fwc3VsYXRlZCk6XG5kZWYgY2hlY2tfb3V0X2Jvb2soYm9vaywgdXNlcik6XG4gICAgYm9vay5jb3BpZXMgLT0gMSAgICAgICAgICAjIHJlYWNoZXMgaW4gZGlyZWN0bHlcbiAgICB1c2VyLmJvcnJvd2VkLmFwcGVuZChib29rKVxuXG4jIEVuY2Fwc3VsYXRlZDpcbmRlZiBjaGVja19vdXRfYm9vayhib29rLCB1c2VyKTpcbiAgICBib29rLmNoZWNrX291dCgpICAgICAgICAgICMgYm9vayBtYW5hZ2VzIGl0cyBvd24gc3RhdGVcbiAgICB1c2VyLmJvcnJvdyhib29rKSAgICAgICAgICMgdXNlciBtYW5hZ2VzIGl0cyBvd24gc3RhdGUifQ"
 width="100%"
></iframe>

The encapsulated version lets each object change its own internal implementation without the function that coordinates them ever needing to know about it.

## Encapsulation at a Glance

| Principle | What it means in practice |
|---|---|
| Bundling | Data and the methods that operate on it live in the same class |
| Protection | Internal attributes are prefixed with `_` as a "do not touch" signal |
| Validation | Check invariants at the point data enters the object |
| Interface stability | Callers use methods, not attributes; internal representation can change freely |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2VuY2Fwc3VsYXRpb25fYnVuZGxpbmdfZGF0YV9hbmRfYmVoYXZpb3IgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6ImNsYXNzIEJhbmtBY2NvdW50OlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBvd25lciwgaW5pdGlhbF9iYWxhbmNlKTpcbiAgICAgICAgc2VsZi5vd25lciA9IG93bmVyXG4gICAgICAgIHNlbGYuX2JhbGFuY2UgPSBpbml0aWFsX2JhbGFuY2VcblxuICAgIGRlZiBkZXBvc2l0KHNlbGYsIGFtb3VudCk6XG4gICAgICAgIGlmIGFtb3VudCA8PSAwOlxuICAgICAgICAgICAgcmFpc2UgVmFsdWVFcnJvcihcIkRlcG9zaXQgYW1vdW50IG11c3QgYmUgcG9zaXRpdmVcIilcbiAgICAgICAgc2VsZi5fYmFsYW5jZSArPSBhbW91bnRcblxuICAgIGRlZiB3aXRoZHJhdyhzZWxmLCBhbW91bnQpOlxuICAgICAgICBpZiBhbW91bnQgPD0gMDpcbiAgICAgICAgICAgIHJhaXNlIFZhbHVlRXJyb3IoXCJXaXRoZHJhd2FsIGFtb3VudCBtdXN0IGJlIHBvc2l0aXZlXCIpXG4gICAgICAgIGlmIGFtb3VudCA-IHNlbGYuX2JhbGFuY2U6XG4gICAgICAgICAgICByYWlzZSBWYWx1ZUVycm9yKFwiSW5zdWZmaWNpZW50IGZ1bmRzXCIpXG4gICAgICAgIHNlbGYuX2JhbGFuY2UgLT0gYW1vdW50XG5cbiAgICBkZWYgYmFsYW5jZShzZWxmKTpcbiAgICAgICAgcmV0dXJuIHNlbGYuX2JhbGFuY2UifQ"
 width="100%"
></iframe>

Test this by creating an account with a starting balance, depositing and withdrawing valid amounts, then try to trigger each `ValueError`. Finally, confirm that `account._balance = -9999` still "works" from outside (Python does not stop you), and explain why the single-underscore convention relies on team discipline rather than language enforcement.

## Conclusion

Encapsulation means that a class owns its state completely: callers interact only through the methods the class provides, internal attributes are marked with a leading underscore to signal they should not be touched directly, and validation lives at the point where data enters the object. This decouples the class's interface from its implementation, so the internal representation can change without affecting every piece of code that uses it. The next lesson introduces a stronger form of access control: name mangling with a double underscore, which does provide a technical barrier, not just a convention.
