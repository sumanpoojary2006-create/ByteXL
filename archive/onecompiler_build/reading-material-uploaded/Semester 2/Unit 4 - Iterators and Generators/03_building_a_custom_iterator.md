## Introduction

Leila wants to build a `CatalogReader` that iterates over a list of raw records and yields only the ones flagged as "approved" for import. She could filter with a list comprehension, but that loads all approved records into memory first. She wants each record to be processed and yielded one at a time, so the pipeline stays lean regardless of how many records the catalog contains.

The right tool is a class that implements `__iter__` and `__next__` directly. Building one makes the protocol concrete: there is no magic, just two methods and a `StopIteration`.

![](images/03_building_a_custom_iterator.png)

## The Minimal Iterator Class

An iterator class needs exactly two things: an `__iter__` method that returns `self`, and a `__next__` method that returns the next item or raises `StopIteration`.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-03-building-a-custom-iterator-001-a3bc1253ff.html"
 width="100%"
></iframe>

`__iter__` returns `self` because `CountDown` is its own iterator. `__next__` checks whether items remain, returns the next one, and raises `StopIteration` when done.

## A Realistic Example: CatalogReader

Leila's actual problem: iterate through a list of raw records and yield only the approved ones, one at a time.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-03-building-a-custom-iterator-002-a5786f1b0e.html"
 width="100%"
></iframe>

The `while` loop in `__next__` skips unapproved records and returns the next approved one. The caller's `for` loop does not need to know filtering is happening; it just receives items one by one.

## The One-Pass Limitation

Because `CatalogReader` returns `self` from `__iter__`, it is its own iterator and is exhausted after one pass. Calling the `for` loop a second time produces nothing:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-03-building-a-custom-iterator-003-83b53274da.html"
 width="100%"
></iframe>

If you want multiple passes, you have two options: reset `_index` to zero in a method, or make `CatalogReader` an *iterable* rather than an iterator by returning a *new* iterator object from `__iter__`.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-03-building-a-custom-iterator-004-3377f8ab1e.html"
 width="100%"
></iframe>

This is the same pattern as a list: the list itself returns a fresh `list_iterator` each time. `CatalogIterable` returns a fresh `CatalogReader` each time.

## When a Custom Iterator Is Worth Writing

Custom iterator classes are most useful when:
- The next item requires computation or filtering, not just indexing
- The data source is external (a file, a database cursor, a network stream)
- You want to separate the *source* of data from the *logic* that processes it

For simpler cases, a generator function (the next lesson) is usually shorter and clearer. But understanding the class-based protocol shows that generators are not magic; they are a convenient syntax for the same two-method protocol.

## Custom Iterators at a Glance

| Requirement | Code |
|---|---|
| Implement `__iter__` | Return `self` (for an iterator) or a new iterator (for an iterable) |
| Implement `__next__` | Return next item or raise `StopIteration` |
| Track position | Use an instance attribute like `self._index` |
| Skip items | Use `while` or `if` inside `__next__` |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-03-building-a-custom-iterator-005-c32378fc33.html"
 width="100%"
></iframe>

Extend this so `EvenNumbers` also supports `len()` (implement `__len__` to return how many even numbers are in the range). Then modify the class so a second `for` loop over the same instance restarts from 0, by resetting `self.current` to 0 at the top of `__iter__` instead of returning `self` (making each `iter()` call produce a fresh traversal).

## Conclusion

A custom iterator class implements `__iter__` (returning `self`) and `__next__` (returning the next item or raising `StopIteration`). It is the cleanest way to produce items from a complex or filtered source one at a time. For cases where writing a class is more boilerplate than the problem warrants, the next lesson introduces generator functions, which achieve the same result with a fraction of the code using the `yield` keyword.
