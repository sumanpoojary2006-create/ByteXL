## Introduction

Leila wants to build a `CatalogReader` that iterates over a list of raw records and yields only the ones flagged as "approved" for import. She could filter with a list comprehension, but that loads all approved records into memory first. She wants each record to be processed and yielded one at a time, so the pipeline stays lean regardless of how many records the catalog contains.

The right tool is a class that implements `__iter__` and `__next__` directly. Building one makes the protocol concrete: there is no magic, just two methods and a `StopIteration`.

![](images/03_building_a_custom_iterator.png)

## The Minimal Iterator Class

An iterator class needs exactly two things: an `__iter__` method that returns `self`, and a `__next__` method that returns the next item or raises `StopIteration`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2J1aWxkaW5nX2FfY3VzdG9tX2l0ZXJhdG9yIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJjbGFzcyBDb3VudERvd246XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHN0YXJ0KTpcbiAgICAgICAgc2VsZi5jdXJyZW50ID0gc3RhcnRcblxuICAgIGRlZiBfX2l0ZXJfXyhzZWxmKTpcbiAgICAgICAgcmV0dXJuIHNlbGYgICAjIGFuIGl0ZXJhdG9yIHJldHVybnMgaXRzZWxmXG5cbiAgICBkZWYgX19uZXh0X18oc2VsZik6XG4gICAgICAgIGlmIHNlbGYuY3VycmVudCA8PSAwOlxuICAgICAgICAgICAgcmFpc2UgU3RvcEl0ZXJhdGlvblxuICAgICAgICB2YWx1ZSA9IHNlbGYuY3VycmVudFxuICAgICAgICBzZWxmLmN1cnJlbnQgLT0gMVxuICAgICAgICByZXR1cm4gdmFsdWVcblxuY291bnRkb3duID0gQ291bnREb3duKDMpXG5mb3IgbiBpbiBjb3VudGRvd246XG4gICAgcHJpbnQobilcbiMgM1xuIyAyXG4jIDEifQ"
 width="100%"
></iframe>

`__iter__` returns `self` because `CountDown` is its own iterator. `__next__` checks whether items remain, returns the next one, and raises `StopIteration` when done.

## A Realistic Example: CatalogReader

Leila's actual problem: iterate through a list of raw records and yield only the approved ones, one at a time.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2J1aWxkaW5nX2FfY3VzdG9tX2l0ZXJhdG9yIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJjbGFzcyBDYXRhbG9nUmVhZGVyOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCByZWNvcmRzKTpcbiAgICAgICAgc2VsZi5fcmVjb3JkcyA9IHJlY29yZHNcbiAgICAgICAgc2VsZi5faW5kZXggPSAwXG5cbiAgICBkZWYgX19pdGVyX18oc2VsZik6XG4gICAgICAgIHJldHVybiBzZWxmXG5cbiAgICBkZWYgX19uZXh0X18oc2VsZik6XG4gICAgICAgIHdoaWxlIHNlbGYuX2luZGV4IDwgbGVuKHNlbGYuX3JlY29yZHMpOlxuICAgICAgICAgICAgcmVjb3JkID0gc2VsZi5fcmVjb3Jkc1tzZWxmLl9pbmRleF1cbiAgICAgICAgICAgIHNlbGYuX2luZGV4ICs9IDFcbiAgICAgICAgICAgIGlmIHJlY29yZC5nZXQoXCJhcHByb3ZlZFwiKTpcbiAgICAgICAgICAgICAgICByZXR1cm4gcmVjb3JkXG4gICAgICAgIHJhaXNlIFN0b3BJdGVyYXRpb25cblxucmF3X3JlY29yZHMgPSBbXG4gICAge1widGl0bGVcIjogXCJEdW5lXCIsIFwiYXBwcm92ZWRcIjogVHJ1ZX0sXG4gICAge1widGl0bGVcIjogXCJSb3VnaCBEcmFmdFwiLCBcImFwcHJvdmVkXCI6IEZhbHNlfSxcbiAgICB7XCJ0aXRsZVwiOiBcIkZvdW5kYXRpb25cIiwgXCJhcHByb3ZlZFwiOiBUcnVlfSxcbiAgICB7XCJ0aXRsZVwiOiBcIkluY29tcGxldGVcIiwgXCJhcHByb3ZlZFwiOiBGYWxzZX0sXG4gICAge1widGl0bGVcIjogXCJTaG9ndW5cIiwgXCJhcHByb3ZlZFwiOiBUcnVlfSxcbl1cblxucmVhZGVyID0gQ2F0YWxvZ1JlYWRlcihyYXdfcmVjb3JkcylcbmZvciBib29rIGluIHJlYWRlcjpcbiAgICBwcmludChib29rW1widGl0bGVcIl0pXG4jIER1bmVcbiMgRm91bmRhdGlvblxuIyBTaG9ndW4ifQ"
 width="100%"
></iframe>

The `while` loop in `__next__` skips unapproved records and returns the next approved one. The caller's `for` loop does not need to know filtering is happening; it just receives items one by one.

## The One-Pass Limitation

Because `CatalogReader` returns `self` from `__iter__`, it is its own iterator and is exhausted after one pass. Calling the `for` loop a second time produces nothing:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2J1aWxkaW5nX2FfY3VzdG9tX2l0ZXJhdG9yIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJyZWFkZXIgPSBDYXRhbG9nUmVhZGVyKHJhd19yZWNvcmRzKVxuXG5mb3IgYm9vayBpbiByZWFkZXI6XG4gICAgcHJpbnQoYm9va1tcInRpdGxlXCJdKVxuIyBEdW5lLCBGb3VuZGF0aW9uLCBTaG9ndW5cblxuZm9yIGJvb2sgaW4gcmVhZGVyOlxuICAgIHByaW50KGJvb2tbXCJ0aXRsZVwiXSlcbiMgKG5vdGhpbmcgLS0gaXRlcmF0b3IgZXhoYXVzdGVkKSJ9"
 width="100%"
></iframe>

If you want multiple passes, you have two options: reset `_index` to zero in a method, or make `CatalogReader` an *iterable* rather than an iterator by returning a *new* iterator object from `__iter__`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2J1aWxkaW5nX2FfY3VzdG9tX2l0ZXJhdG9yIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJjbGFzcyBDYXRhbG9nSXRlcmFibGU6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIHJlY29yZHMpOlxuICAgICAgICBzZWxmLl9yZWNvcmRzID0gcmVjb3Jkc1xuXG4gICAgZGVmIF9faXRlcl9fKHNlbGYpOlxuICAgICAgICAjIFJldHVybiBhIE5FVyBpdGVyYXRvciBlYWNoIHRpbWVcbiAgICAgICAgcmV0dXJuIENhdGFsb2dSZWFkZXIoc2VsZi5fcmVjb3JkcylcblxuY2F0YWxvZyA9IENhdGFsb2dJdGVyYWJsZShyYXdfcmVjb3JkcylcbmZvciBib29rIGluIGNhdGFsb2c6XG4gICAgcHJpbnQoYm9va1tcInRpdGxlXCJdKSAgICMgRHVuZSwgRm91bmRhdGlvbiwgU2hvZ3VuXG5mb3IgYm9vayBpbiBjYXRhbG9nOlxuICAgIHByaW50KGJvb2tbXCJ0aXRsZVwiXSkgICAjIER1bmUsIEZvdW5kYXRpb24sIFNob2d1biAtLSB3b3JrcyBhZ2FpbiJ9"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2J1aWxkaW5nX2FfY3VzdG9tX2l0ZXJhdG9yIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJjbGFzcyBFdmVuTnVtYmVyczpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgbGltaXQpOlxuICAgICAgICBzZWxmLmN1cnJlbnQgPSAwXG4gICAgICAgIHNlbGYubGltaXQgPSBsaW1pdFxuXG4gICAgZGVmIF9faXRlcl9fKHNlbGYpOlxuICAgICAgICByZXR1cm4gc2VsZlxuXG4gICAgZGVmIF9fbmV4dF9fKHNlbGYpOlxuICAgICAgICBpZiBzZWxmLmN1cnJlbnQgPiBzZWxmLmxpbWl0OlxuICAgICAgICAgICAgcmFpc2UgU3RvcEl0ZXJhdGlvblxuICAgICAgICB2YWx1ZSA9IHNlbGYuY3VycmVudFxuICAgICAgICBzZWxmLmN1cnJlbnQgKz0gMlxuICAgICAgICByZXR1cm4gdmFsdWVcblxuZm9yIG4gaW4gRXZlbk51bWJlcnMoMTApOlxuICAgIHByaW50KG4pICAgIyAwLCAyLCA0LCA2LCA4LCAxMCJ9"
 width="100%"
></iframe>

Extend this so `EvenNumbers` also supports `len()` (implement `__len__` to return how many even numbers are in the range). Then modify the class so a second `for` loop over the same instance restarts from 0, by resetting `self.current` to 0 at the top of `__iter__` instead of returning `self` (making each `iter()` call produce a fresh traversal).

## Conclusion

A custom iterator class implements `__iter__` (returning `self`) and `__next__` (returning the next item or raising `StopIteration`). It is the cleanest way to produce items from a complex or filtered source one at a time. For cases where writing a class is more boilerplate than the problem warrants, the next lesson introduces generator functions, which achieve the same result with a fraction of the code using the `yield` keyword.
