## Introduction

Leila joined the library network's data team last month. Her first big task: process a catalog import file with over a million book records and update the database. She writes a list comprehension that loads all million records into a Python list and immediately runs out of memory. Her script crashes.

Her senior colleague Nadia looks at the crash report and says: "You do not need all of them at once. You need one at a time." She introduces Leila to iterators, and over the next several lessons, Leila's import script goes from crashing to running comfortably on a machine with 4 GB of RAM.

This lesson starts at the foundation: what Python's iterator protocol actually is, and how the familiar `for` loop is secretly using it every time.

![](images/01_iterator_protocol.png)

## How a for Loop Actually Works

When you write `for item in collection:`, Python does not simply index through a list. It calls two dunder methods: first `__iter__()` to get an **iterator object**, then `__next__()` on that iterator repeatedly to get items one at a time until a `StopIteration` exception is raised.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3RoZV9pdGVyYXRvcl9wcm90b2NvbCBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoibnVtYmVycyA9IFsxMCwgMjAsIDMwXVxuXG4jIFdoYXQgdGhlIGZvciBsb29wIGRvZXMsIHN0ZXAgYnkgc3RlcDpcbml0ZXJhdG9yID0gaXRlcihudW1iZXJzKSAgICAgICAgICMgY2FsbHMgbnVtYmVycy5fX2l0ZXJfXygpXG5wcmludChuZXh0KGl0ZXJhdG9yKSkgICAgICAgICAgICAjIGNhbGxzIGl0ZXJhdG9yLl9fbmV4dF9fKCkgLT4gMTBcbnByaW50KG5leHQoaXRlcmF0b3IpKSAgICAgICAgICAgICMgMjBcbnByaW50KG5leHQoaXRlcmF0b3IpKSAgICAgICAgICAgICMgMzBcbnByaW50KG5leHQoaXRlcmF0b3IpKSAgICAgICAgICAgICMgU3RvcEl0ZXJhdGlvbiEifQ"
 width="100%"
></iframe>

The `for` loop catches `StopIteration` automatically and exits cleanly. The `iter()` and `next()` built-in functions are thin wrappers around `__iter__()` and `__next__()`. You can call them directly in your own code when you need finer control over iteration.

## The Two Parts of the Protocol

The iterator protocol involves two related but different concepts:

An **iterable** is any object that has an `__iter__` method. Lists, tuples, strings, dicts, sets, and files are all iterables. Calling `iter(some_iterable)` returns an **iterator**.

An **iterator** is an object that has both `__iter__` and `__next__`. It remembers where it is in the sequence and returns the next item each time `__next__` is called. Once exhausted, it raises `StopIteration` permanently.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3RoZV9pdGVyYXRvcl9wcm90b2NvbCBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoibnVtYmVycyA9IFsxLCAyLCAzXSAgICAjIGEgbGlzdCBpcyBhbiBpdGVyYWJsZSwgbm90IGFuIGl0ZXJhdG9yXG5cbml0ID0gaXRlcihudW1iZXJzKSAgICAgIyBub3cgaXQgaXMgYW4gaXRlcmF0b3JcbnByaW50KHR5cGUoaXQpKSAgICAgICAgIyA8Y2xhc3MgJ2xpc3RfaXRlcmF0b3InPlxuXG5wcmludChuZXh0KGl0KSkgICAgICAgICMgMVxucHJpbnQobmV4dChpdCkpICAgICAgICAjIDJcblxuIyBBIGZyZXNoIGl0ZXIoKSBjYWxsIHJlc2V0czpcbml0MiA9IGl0ZXIobnVtYmVycylcbnByaW50KG5leHQoaXQyKSkgICAgICAgIyAxIC0tIHN0YXJ0cyBmcm9tIHRoZSBiZWdpbm5pbmcgYWdhaW4ifQ"
 width="100%"
></iframe>

The list itself is not consumed by iteration. A fresh `iter()` call always gives you a new iterator starting from the beginning. This is an important difference from file objects, which are their own iterators and can only be read once without seeking back.

## Proving the Protocol with a File Object

Files are one of the clearest examples of how the protocol works: they implement both `__iter__` and `__next__`, making them usable directly in `for` loops without loading the whole file into memory.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3RoZV9pdGVyYXRvcl9wcm90b2NvbCBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoiIyBDcmVhdGUgYSBzYW1wbGUgZmlsZSB0byByZWFkXG53aXRoIG9wZW4oXCJzYW1wbGUudHh0XCIsIFwid1wiKSBhcyBmOlxuICAgIGYud3JpdGUoXCJCb29rIEFcXG5Cb29rIEJcXG5Cb29rIENcXG5cIilcblxud2l0aCBvcGVuKFwic2FtcGxlLnR4dFwiKSBhcyBmOlxuICAgIHByaW50KGhhc2F0dHIoZiwgXCJfX2l0ZXJfX1wiKSkgICAjIFRydWUgLS0gZmlsZSBpcyBhbiBpdGVyYWJsZVxuICAgIHByaW50KGhhc2F0dHIoZiwgXCJfX25leHRfX1wiKSkgICAjIFRydWUgLS0gZmlsZSBpcyBhbHNvIGl0cyBvd24gaXRlcmF0b3JcbiAgICBmb3IgbGluZSBpbiBmOlxuICAgICAgICBwcmludChsaW5lLnN0cmlwKCkpXG4jIEJvb2sgQVxuIyBCb29rIEJcbiMgQm9vayBDIn0"
 width="100%"
></iframe>

Each `for` iteration calls `f.__next__()`, which reads one line from disk. No line is held in memory beyond the current iteration. This is exactly the pattern Leila needs for her million-record import.

## Separation: Iterables That Return Fresh Iterators

Most collections (lists, tuples, strings) are **iterables** that return a *new* iterator object each time `iter()` is called. This means you can iterate over a list multiple times without resetting anything manually.

A file, by contrast, is its own iterator: the same object is returned by `iter(f)`. Calling `iter(f)` twice gives you the same object at the same position, not a fresh start.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3RoZV9pdGVyYXRvcl9wcm90b2NvbCBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoid29yZHMgPSBbXCJhbHBoYVwiLCBcImJldGFcIiwgXCJnYW1tYVwiXVxuXG5pdDEgPSBpdGVyKHdvcmRzKVxuaXQyID0gaXRlcih3b3JkcykgICAjIGNvbXBsZXRlbHkgaW5kZXBlbmRlbnRcblxucHJpbnQobmV4dChpdDEpKSAgICAjIGFscGhhXG5wcmludChuZXh0KGl0MSkpICAgICMgYmV0YVxucHJpbnQobmV4dChpdDIpKSAgICAjIGFscGhhIC0tIGZyZXNoIHN0YXJ0LCB1bmFmZmVjdGVkIGJ5IGl0MSJ9"
 width="100%"
></iframe>

## The Iterator Protocol at a Glance

| Term | What it means | Example |
|---|---|---|
| Iterable | Has `__iter__`; returns an iterator | list, str, dict, set, file |
| Iterator | Has `__iter__` and `__next__`; remembers position | list_iterator, file |
| `iter(x)` | Calls `x.__iter__()`; returns an iterator | `iter([1,2,3])` |
| `next(it)` | Calls `it.__next__()`; returns next item | `next(iterator)` |
| `StopIteration` | Raised when the iterator is exhausted | `for` loops catch this automatically |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3RoZV9pdGVyYXRvcl9wcm90b2NvbCBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoiY29sb3JzID0gW1wicmVkXCIsIFwiZ3JlZW5cIiwgXCJibHVlXCJdXG5pdCA9IGl0ZXIoY29sb3JzKVxuXG5wcmludChuZXh0KGl0KSlcbnByaW50KG5leHQoaXQpKVxucHJpbnQobmV4dChpdCkpXG5wcmludChuZXh0KGl0KSkgICAjIGVycm9yISJ9"
 width="100%"
></iframe>

Run this and observe the `StopIteration`. Then wrap the last `next(it)` in a `try`/`except StopIteration` block to handle it gracefully. Finally, call `iter(colors)` again and confirm you can iterate from the beginning, proving the original list is unaffected.

## Conclusion

Python's `for` loop is syntactic sugar over the iterator protocol: it calls `__iter__()` once to get an iterator, then `__next__()` repeatedly until `StopIteration` is raised. An iterable has `__iter__`. An iterator has both `__iter__` and `__next__` and remembers its position. The next lesson clarifies the distinction between iterables and iterators more precisely, then the lesson after that shows how to build a custom class that implements the full protocol from scratch.
