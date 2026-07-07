## Introduction

Leila is reading more about the iterator protocol and keeps getting confused by the two words: *iterable* and *iterator*. She initially thought they meant the same thing, and the previous lesson showed they do not. But the distinction feels slippery in practice: a list is one, a file is both, and strings are iterable but not iterators. She asks Nadia for a cleaner mental model.

Nadia draws a simple diagram: an iterable is like a bookshelf, it knows where the books are. An iterator is like a reading finger moving along that shelf, it remembers which book you are currently on. The shelf can produce a fresh finger at any time, but the finger itself is always somewhere specific. This lesson makes that distinction precise and shows how to test it in code.

![](images/02_iterables_vs_iterators.png)

## Testing Membership: iter() and next()

The simplest way to check whether an object is an iterable or an iterator is to look at which methods it has:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2l0ZXJhYmxlc192c19pdGVyYXRvcnMgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6ImRlZiBpc19pdGVyYWJsZShvYmopOlxuICAgIHJldHVybiBoYXNhdHRyKG9iaiwgXCJfX2l0ZXJfX1wiKVxuXG5kZWYgaXNfaXRlcmF0b3Iob2JqKTpcbiAgICByZXR1cm4gaGFzYXR0cihvYmosIFwiX19pdGVyX19cIikgYW5kIGhhc2F0dHIob2JqLCBcIl9fbmV4dF9fXCIpXG5cbm15X2xpc3QgPSBbMSwgMiwgM11cbm15X2l0ZXIgPSBpdGVyKG15X2xpc3QpXG5cbnByaW50KGlzX2l0ZXJhYmxlKG15X2xpc3QpKSAgICMgVHJ1ZVxucHJpbnQoaXNfaXRlcmF0b3IobXlfbGlzdCkpICAgIyBGYWxzZSAtLSBsaXN0IGhhcyBfX2l0ZXJfXyBidXQgbm90IF9fbmV4dF9fXG5cbnByaW50KGlzX2l0ZXJhYmxlKG15X2l0ZXIpKSAgICMgVHJ1ZVxucHJpbnQoaXNfaXRlcmF0b3IobXlfaXRlcikpICAgIyBUcnVlIC0tIGxpc3RfaXRlcmF0b3IgaGFzIGJvdGgifQ"
 width="100%"
></iframe>

A list is an iterable but not an iterator. The `list_iterator` object returned by `iter()` is both: it implements `__iter__` (which returns itself) and `__next__` (which advances).

## Why Iterables Return Themselves as Iterators

Iterators implement `__iter__` by returning `self`. This means you can pass an iterator to a `for` loop directly, because the loop calls `iter(obj)` on its target, and for an iterator that just returns itself.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2l0ZXJhYmxlc192c19pdGVyYXRvcnMgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6Im51bWJlcnMgPSBbMSwgMiwgM11cbml0ID0gaXRlcihudW1iZXJzKVxuXG5mb3IgbiBpbiBpdDogICAgICMgZm9yIGNhbGxzIGl0ZXIoaXQpLCB3aGljaCByZXR1cm5zIGl0IChpdHNlbGYpXG4gICAgcHJpbnQobilcbiMgMVxuIyAyXG4jIDNcblxuZm9yIG4gaW4gaXQ6ICAgICAjIGl0ZXJhdG9yIGlzIG5vdyBleGhhdXN0ZWRcbiAgICBwcmludChuKSAgICAgIyBub3RoaW5nIHByaW50ZWQgLS0gYWxyZWFkeSBhdCB0aGUgZW5kIn0"
 width="100%"
></iframe>

The list can be iterated again from scratch (a fresh `iter(numbers)` gives a new iterator). The iterator cannot be rewound: once `StopIteration` is raised, it is permanently done. This is why a file can only be read once unless you `seek(0)` to the beginning.

## Multiple Independent Iterators From One Iterable

Because iterables return fresh iterators on each `iter()` call, you can have multiple iterators in flight at the same time, each at a different position in the same source collection.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2l0ZXJhYmxlc192c19pdGVyYXRvcnMgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6ImNhdGFsb2cgPSBbXCJCb29rIEFcIiwgXCJCb29rIEJcIiwgXCJCb29rIENcIiwgXCJCb29rIERcIl1cblxuaXQxID0gaXRlcihjYXRhbG9nKVxuaXQyID0gaXRlcihjYXRhbG9nKVxuXG5wcmludChuZXh0KGl0MSkpICAgIyBCb29rIEFcbnByaW50KG5leHQoaXQxKSkgICAjIEJvb2sgQlxucHJpbnQobmV4dChpdDIpKSAgICMgQm9vayBBIC0tIGl0MiBpcyBpbmRlcGVuZGVudFxucHJpbnQobmV4dChpdDEpKSAgICMgQm9vayBDIC0tIGl0MSBjb250aW51ZXMifQ"
 width="100%"
></iframe>

This is useful when you want to compare two positions in the same sequence, or when two separate loops process the same collection concurrently.

## What Strings Are

Strings are iterable (they have `__iter__`) but not iterators. Each character is a unit of iteration, and each `iter(string_obj)` returns a fresh iterator object.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2l0ZXJhYmxlc192c19pdGVyYXRvcnMgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6InRleHQgPSBcImFiY1wiXG5wcmludChpc19pdGVyYWJsZSh0ZXh0KSkgICAjIFRydWVcbnByaW50KGlzX2l0ZXJhdG9yKHRleHQpKSAgICMgRmFsc2VcblxuaXQgPSBpdGVyKHRleHQpXG5wcmludChuZXh0KGl0KSkgICAjIGFcbnByaW50KG5leHQoaXQpKSAgICMgYlxucHJpbnQobmV4dChpdCkpICAgIyBjIn0"
 width="100%"
></iframe>

## What generators Are (Preview)

Generators, covered in lesson 4, are iterators that compute their values on demand rather than storing them. They implement `__iter__` and `__next__`, making them both iterables and iterators, with the special property that their values are produced lazily as needed rather than pre-computed and stored.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2l0ZXJhYmxlc192c19pdGVyYXRvcnMgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6IiMgQSBnZW5lcmF0b3IgZXhwcmVzc2lvbiAocHJldmlldyAtLSBmdWxsIGxlc3NvbiBsYXRlcilcbmdlbiA9ICh4ICoqIDIgZm9yIHggaW4gcmFuZ2UoNSkpXG5wcmludChpc19pdGVyYXRvcihnZW4pKSAgICMgVHJ1ZSAtLSBnZW5lcmF0b3JzIGFyZSBpdGVyYXRvcnNcblxucHJpbnQobmV4dChnZW4pKSAgICMgMFxucHJpbnQobmV4dChnZW4pKSAgICMgMVxucHJpbnQobmV4dChnZW4pKSAgICMgNCJ9"
 width="100%"
></iframe>

## Iterables vs. Iterators at a Glance

| Type | `__iter__`? | `__next__`? | Reusable? | Examples |
|---|---|---|---|---|
| Iterable | Yes | No | Yes (fresh iterator each time) | list, str, tuple, dict, set |
| Iterator | Yes (returns self) | Yes | No (exhausted after one pass) | list_iterator, file, generator |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2l0ZXJhYmxlc192c19pdGVyYXRvcnMgY29kZSA2IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA2LnB5IiwiY29kZSI6InRleHQgPSBcImhlbGxvXCJcbm51bWJlcnMgPSBbMTAsIDIwLCAzMF1cblxudGV4dF9pdGVyID0gaXRlcih0ZXh0KVxubnVtYmVyc19pdGVyID0gaXRlcihudW1iZXJzKVxuXG5wcmludChuZXh0KHRleHRfaXRlcikpXG5wcmludChuZXh0KG51bWJlcnNfaXRlcikpXG5wcmludChuZXh0KHRleHRfaXRlcikpXG5wcmludChuZXh0KG51bWJlcnNfaXRlcikpIn0"
 width="100%"
></iframe>

Run this and predict the output before running it. Then create a second `iter()` on `numbers` while `numbers_iter` is mid-way through, and advance both independently to prove they are genuinely independent. Finally, call `iter(numbers_iter)` (calling iter on an iterator) and confirm it returns the same object (iterators return `self` from `__iter__`).

## Conclusion

An iterable is any object that can produce an iterator via `__iter__`. An iterator is an object that produces items on demand via `__next__` and signals completion with `StopIteration`. Iterables are generally reusable (each `iter()` call returns a fresh iterator); iterators are not (they are exhausted after one pass). The next lesson builds a custom iterator class from scratch, implementing both methods explicitly, to make the protocol concrete rather than abstract.
