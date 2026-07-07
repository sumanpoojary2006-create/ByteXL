## Introduction

Asel has been writing Python for almost a year. She can define functions, loop over lists, catch exceptions, and even sketch out a class or two without looking anything up. On her first morning at the internship she expects to open a ticket and get to work. Instead, her senior colleague Rahul hands her a coffee and says: "Before we dive in, I want to know what you think Python is actually doing when you run a script."

Asel realizes she knows how to *use* Python, but has never seriously asked how it *works*. This unit answers that question from the inside out. Before going deeper, though, a fast lap around what you already know is worth taking, because every internal mechanism Semester 2 explores is built on top of the fundamentals you built in Semester 1.

![](images/01_semester1_recap_bridge.png)

## Functions Are First-Class Citizens

In Semester 1 you learned to define functions and call them. The part that matters most going forward is that Python treats functions as ordinary values: they can be stored in variables, passed as arguments, and returned from other functions.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3JlZnJlc2hlcl9mdW5jdGlvbnNfY29sbGVjdGlvbnNfZmlsZXNfYmFzaWNfb29wX2V4IGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJkZWYgZ3JlZXQobmFtZSk6XG4gICAgcmV0dXJuIGZcIkhlbGxvLCB7bmFtZX1cIlxuXG5zYXlfaGkgPSBncmVldCAgICAgICAgICAgICMgYXNzaWduaW5nIGEgZnVuY3Rpb24gdG8gYSB2YXJpYWJsZVxucHJpbnQoc2F5X2hpKFwiQXNlbFwiKSkgICAgICMgSGVsbG8sIEFzZWxcblxuZGVmIGFwcGx5KGZuLCB2YWx1ZSk6XG4gICAgcmV0dXJuIGZuKHZhbHVlKVxuXG5wcmludChhcHBseShncmVldCwgXCJSYWh1bFwiKSkgICAjIEhlbGxvLCBSYWh1bCJ9"
 width="100%"
></iframe>

This property, called first-class functions, is the precise reason decorators (Unit 5) and higher-order patterns work at all. If you remember nothing else from this refresher, remember that a function is just an object.

## Collections and How They Behave

The four core data structures from Semester 1 each have a distinct contract about ordering, mutability, and lookup speed.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3JlZnJlc2hlcl9mdW5jdGlvbnNfY29sbGVjdGlvbnNfZmlsZXNfYmFzaWNfb29wX2V4IGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiIjIGxpc3Q6IG9yZGVyZWQsIG11dGFibGUsIGFsbG93cyBkdXBsaWNhdGVzXG5ib29rcyA9IFtcIkR1bmVcIiwgXCJTaG9ndW5cIiwgXCJEdW5lXCJdXG5cbiMgdHVwbGU6IG9yZGVyZWQsIGltbXV0YWJsZSBzbmFwc2hvdFxuY29vcmQgPSAoMTIuMywgNDUuNilcblxuIyBzZXQ6IHVub3JkZXJlZCwgdW5pcXVlLCBmYXN0IG1lbWJlcnNoaXAgdGVzdGluZ1xuZ2VucmVzID0ge1wic2NpLWZpXCIsIFwiaGlzdG9yeVwiLCBcInNjaS1maVwifSAgICMgc3RvcmVzIG9ubHkgb25lIFwic2NpLWZpXCJcbnByaW50KGdlbnJlcylcblxuIyBkaWN0OiBrZXktdmFsdWUsIG9yZGVyZWQgKFB5dGhvbiAzLjcrKSwgZmFzdCBsb29rdXBcbmNhdGFsb2cgPSB7XCJpc2JuXCI6IFwiOTc4LTBcIiwgXCJ0aXRsZVwiOiBcIkR1bmVcIiwgXCJjb3BpZXNcIjogM30ifQ"
 width="100%"
></iframe>

Knowing which container to reach for, and why, prepares you for the iterator and generator patterns in Unit 4, where you will build custom objects that behave like these sequences without storing everything in memory at once.

## Files, Context Managers, and Exceptions in One Pass

File handling, context managers, and exceptions are closely related: reading or writing a file can fail, and the `with` statement guarantees cleanup even when it does.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3JlZnJlc2hlcl9mdW5jdGlvbnNfY29sbGVjdGlvbnNfZmlsZXNfYmFzaWNfb29wX2V4IGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJ0cnk6XG4gICAgd2l0aCBvcGVuKFwiY2F0YWxvZy50eHRcIiwgXCJyXCIpIGFzIGZpbGU6XG4gICAgICAgIGNvbnRlbnQgPSBmaWxlLnJlYWQoKVxuICAgICAgICBwcmludChjb250ZW50KVxuZXhjZXB0IEZpbGVOb3RGb3VuZEVycm9yIGFzIGVycm9yOlxuICAgIHByaW50KGZcIkNvdWxkIG5vdCBvcGVuIHRoZSBmaWxlOiB7ZXJyb3J9XCIpIn0"
 width="100%"
></iframe>

The `with` keyword calls `__enter__` and `__exit__` methods on the file object behind the scenes. In Unit 6, you will write objects with those same methods yourself. In Unit 12, you will handle exceptions at the boundary of a command-line tool. Both ideas grow directly from what you already know.

## Classes: The Starting Point for Two Units of OOP

Semester 1 introduced classes as blueprints and objects as instances. The core syntax is worth revisiting before Semester 2 pushes it much further.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3JlZnJlc2hlcl9mdW5jdGlvbnNfY29sbGVjdGlvbnNfZmlsZXNfYmFzaWNfb29wX2V4IGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJjbGFzcyBCb29rOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCB0aXRsZSwgY29waWVzKTpcbiAgICAgICAgc2VsZi50aXRsZSA9IHRpdGxlXG4gICAgICAgIHNlbGYuY29waWVzID0gY29waWVzXG5cbiAgICBkZWYgaXNfYXZhaWxhYmxlKHNlbGYpOlxuICAgICAgICByZXR1cm4gc2VsZi5jb3BpZXMgPiAwXG5cbiAgICBkZWYgX19yZXByX18oc2VsZik6XG4gICAgICAgIHJldHVybiBmXCJCb29rKHtzZWxmLnRpdGxlIXJ9LCBjb3BpZXM9e3NlbGYuY29waWVzfSlcIlxuXG5iID0gQm9vayhcIkR1bmVcIiwgMylcbnByaW50KGIuaXNfYXZhaWxhYmxlKCkpICAgIyBUcnVlXG5wcmludChiKSAgICAgICAgICAgICAgICAgICAjIEJvb2soJ0R1bmUnLCBjb3BpZXM9MykifQ"
 width="100%"
></iframe>

Unit 2 will formalize how to *protect* state inside a class (encapsulation and properties). Unit 3 will show how to build hierarchies of classes that share and extend behavior (inheritance and polymorphism). Both units build directly on this foundation.

## Refresher at a Glance

| Concept | What you know | Where it goes in Semester 2 |
|---|---|---|
| First-class functions | Pass and return functions | Decorators (Unit 5) |
| Collections | list, tuple, set, dict | Custom iterators (Unit 4) |
| Context managers | `with open(...)` | Writing `__enter__`/`__exit__` (Unit 6) |
| Exception handling | `try`/`except`/`finally` | Error boundaries in CLI tools (Unit 12) |
| Classes and objects | `__init__`, methods, `self` | Encapsulation, inheritance (Units 2-3) |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3JlZnJlc2hlcl9mdW5jdGlvbnNfY29sbGVjdGlvbnNfZmlsZXNfYmFzaWNfb29wX2V4IGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJkZWYgbWFrZV9jb3VudGVyKHN0YXJ0PTApOlxuICAgIGNvdW50ID0gW3N0YXJ0XVxuICAgIGRlZiBpbmNyZW1lbnQoKTpcbiAgICAgICAgY291bnRbMF0gKz0gMVxuICAgICAgICByZXR1cm4gY291bnRbMF1cbiAgICByZXR1cm4gaW5jcmVtZW50XG5cbmMgPSBtYWtlX2NvdW50ZXIoKVxucHJpbnQoYygpKVxucHJpbnQoYygpKVxucHJpbnQoYygpKSJ9"
 width="100%"
></iframe>

Run this, then explain in one sentence why `count` keeps its value between calls to `increment()`. Your answer will be the exact mental model decorators (Unit 5) rely on. This pattern has a name: a **closure**. Notice it but do not worry about it yet.

## Conclusion

Every concept in this refresher, first-class functions, the four core collections, file and exception handling, and classes, reappears in Semester 2 with a deeper or more powerful form. Nothing is discarded; everything is extended. The next lesson stops treating Python as a black box and asks the question Rahul posed over coffee: what is Python actually doing between the moment you type `python script.py` and the moment the first output appears on screen?
