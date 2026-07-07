## Introduction

Asel has been writing Python for almost a year. She can define functions, loop over lists, catch exceptions, and even sketch out a class or two without looking anything up. On her first morning at the internship she expects to open a ticket and get to work. Instead, her senior colleague Rahul hands her a coffee and says: "Before we dive in, I want to know what you think Python is actually doing when you run a script."

Asel realizes she knows how to *use* Python, but has never seriously asked how it *works*. This unit answers that question from the inside out. Before going deeper, though, a fast lap around what you already know is worth taking, because every internal mechanism Semester 2 explores is built on top of the fundamentals you built in Semester 1.

![](images/01_semester1_recap_bridge.png)

## Functions Are First-Class Citizens

In Semester 1 you learned to define functions and call them. The part that matters most going forward is that Python treats functions as ordinary values: they can be stored in variables, passed as arguments, and returned from other functions.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-1-recap-and-python-internals-01-refresher-functions-collection-001-f157f7e934.html"
 width="100%"
></iframe>

This property, called first-class functions, is the precise reason decorators (Unit 5) and higher-order patterns work at all. If you remember nothing else from this refresher, remember that a function is just an object.

## Collections and How They Behave

The four core data structures from Semester 1 each have a distinct contract about ordering, mutability, and lookup speed.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-1-recap-and-python-internals-01-refresher-functions-collection-002-786f4a0b9b.html"
 width="100%"
></iframe>

Knowing which container to reach for, and why, prepares you for the iterator and generator patterns in Unit 4, where you will build custom objects that behave like these sequences without storing everything in memory at once.

## Files, Context Managers, and Exceptions in One Pass

File handling, context managers, and exceptions are closely related: reading or writing a file can fail, and the `with` statement guarantees cleanup even when it does.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-1-recap-and-python-internals-01-refresher-functions-collection-003-fb836ff59e.html"
 width="100%"
></iframe>

The `with` keyword calls `__enter__` and `__exit__` methods on the file object behind the scenes. In Unit 6, you will write objects with those same methods yourself. In Unit 12, you will handle exceptions at the boundary of a command-line tool. Both ideas grow directly from what you already know.

## Classes: The Starting Point for Two Units of OOP

Semester 1 introduced classes as blueprints and objects as instances. The core syntax is worth revisiting before Semester 2 pushes it much further.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-1-recap-and-python-internals-01-refresher-functions-collection-004-d3bd6aa16a.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-1-recap-and-python-internals-01-refresher-functions-collection-005-60987c89c5.html"
 width="100%"
></iframe>

Run this, then explain in one sentence why `count` keeps its value between calls to `increment()`. Your answer will be the exact mental model decorators (Unit 5) rely on. This pattern has a name: a **closure**. Notice it but do not worry about it yet.

## Conclusion

Every concept in this refresher, first-class functions, the four core collections, file and exception handling, and classes, reappears in Semester 2 with a deeper or more powerful form. Nothing is discarded; everything is extended. The next lesson stops treating Python as a black box and asks the question Rahul posed over coffee: what is Python actually doing between the moment you type `python script.py` and the moment the first output appears on screen?
