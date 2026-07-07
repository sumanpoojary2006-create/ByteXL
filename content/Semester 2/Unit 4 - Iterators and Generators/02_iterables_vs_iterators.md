## Introduction

Leila is reading more about the iterator protocol and keeps getting confused by the two words: *iterable* and *iterator*. She initially thought they meant the same thing, and the previous lesson showed they do not. But the distinction feels slippery in practice: a list is one, a file is both, and strings are iterable but not iterators. She asks Nadia for a cleaner mental model.

Nadia draws a simple diagram: an iterable is like a bookshelf, it knows where the books are. An iterator is like a reading finger moving along that shelf, it remembers which book you are currently on. The shelf can produce a fresh finger at any time, but the finger itself is always somewhere specific. This lesson makes that distinction precise and shows how to test it in code.

![](images/02_iterables_vs_iterators.png)

## Testing Membership: iter() and next()

The simplest way to check whether an object is an iterable or an iterator is to look at which methods it has:

```python
def is_iterable(obj):
    return hasattr(obj, "__iter__")

def is_iterator(obj):
    return hasattr(obj, "__iter__") and hasattr(obj, "__next__")

my_list = [1, 2, 3]
my_iter = iter(my_list)

print(is_iterable(my_list))   # True
print(is_iterator(my_list))   # False -- list has __iter__ but not __next__

print(is_iterable(my_iter))   # True
print(is_iterator(my_iter))   # True -- list_iterator has both
```

A list is an iterable but not an iterator. The `list_iterator` object returned by `iter()` is both: it implements `__iter__` (which returns itself) and `__next__` (which advances).

## Why Iterables Return Themselves as Iterators

Iterators implement `__iter__` by returning `self`. This means you can pass an iterator to a `for` loop directly, because the loop calls `iter(obj)` on its target, and for an iterator that just returns itself.

```python
numbers = [1, 2, 3]
it = iter(numbers)

for n in it:     # for calls iter(it), which returns it (itself)
    print(n)
# 1
# 2
# 3

for n in it:     # iterator is now exhausted
    print(n)     # nothing printed -- already at the end
```

The list can be iterated again from scratch (a fresh `iter(numbers)` gives a new iterator). The iterator cannot be rewound: once `StopIteration` is raised, it is permanently done. This is why a file can only be read once unless you `seek(0)` to the beginning.

## Multiple Independent Iterators From One Iterable

Because iterables return fresh iterators on each `iter()` call, you can have multiple iterators in flight at the same time, each at a different position in the same source collection.

```python
catalog = ["Book A", "Book B", "Book C", "Book D"]

it1 = iter(catalog)
it2 = iter(catalog)

print(next(it1))   # Book A
print(next(it1))   # Book B
print(next(it2))   # Book A -- it2 is independent
print(next(it1))   # Book C -- it1 continues
```

This is useful when you want to compare two positions in the same sequence, or when two separate loops process the same collection concurrently.

## What Strings Are

Strings are iterable (they have `__iter__`) but not iterators. Each character is a unit of iteration, and each `iter(string_obj)` returns a fresh iterator object.

```python
text = "abc"
print(is_iterable(text))   # True
print(is_iterator(text))   # False

it = iter(text)
print(next(it))   # a
print(next(it))   # b
print(next(it))   # c
```

## What generators Are (Preview)

Generators, covered in lesson 4, are iterators that compute their values on demand rather than storing them. They implement `__iter__` and `__next__`, making them both iterables and iterators, with the special property that their values are produced lazily as needed rather than pre-computed and stored.

```python
# A generator expression (preview -- full lesson later)
gen = (x ** 2 for x in range(5))
print(is_iterator(gen))   # True -- generators are iterators

print(next(gen))   # 0
print(next(gen))   # 1
print(next(gen))   # 4
```

## Iterables vs. Iterators at a Glance

| Type | `__iter__`? | `__next__`? | Reusable? | Examples |
|---|---|---|---|---|
| Iterable | Yes | No | Yes (fresh iterator each time) | list, str, tuple, dict, set |
| Iterator | Yes (returns self) | Yes | No (exhausted after one pass) | list_iterator, file, generator |

## Your Turn

```python
text = "hello"
numbers = [10, 20, 30]

text_iter = iter(text)
numbers_iter = iter(numbers)

print(next(text_iter))
print(next(numbers_iter))
print(next(text_iter))
print(next(numbers_iter))
```

Run this and predict the output before running it. Then create a second `iter()` on `numbers` while `numbers_iter` is mid-way through, and advance both independently to prove they are genuinely independent. Finally, call `iter(numbers_iter)` (calling iter on an iterator) and confirm it returns the same object (iterators return `self` from `__iter__`).

## Conclusion

An iterable is any object that can produce an iterator via `__iter__`. An iterator is an object that produces items on demand via `__next__` and signals completion with `StopIteration`. Iterables are generally reusable (each `iter()` call returns a fresh iterator); iterators are not (they are exhausted after one pass). The next lesson builds a custom iterator class from scratch, implementing both methods explicitly, to make the protocol concrete rather than abstract.
