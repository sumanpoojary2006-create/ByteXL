## Introduction

Nadia keeps writing the same boilerplate: a `{}` dictionary with a check for missing keys before incrementing, tuples with index-based access like `record[2]` that are impossible to read weeks later, and ordered groupings that lose their order when stored in a plain dict. Each time she types this code, she knows there must be a better way.

The `collections` module is the better way. It provides four data structures -- `Counter`, `defaultdict`, `namedtuple`, and `OrderedDict` -- that solve exactly these patterns with less code and more clarity.

![Four drawers in a filing cabinet labeled Counter, defaultdict, namedtuple, and OrderedDict, each with a brief description of when to use it](images/05_collections.png)

## Counter: Count Occurrences

`Counter` takes an iterable and counts how many times each element appears. It is a subclass of `dict`, so every dict method works on it, plus it adds `most_common()`.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-05-collections-counter-defaultdict-namedtup-001-4406483866.html"
 width="100%"
></iframe>

`Counter` also works for individual strings:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-05-collections-counter-defaultdict-namedtup-002-32424c67dd.html"
 width="100%"
></iframe>

## defaultdict: Avoid Missing-Key Checks

`defaultdict` is a dict that calls a factory function to produce a default value for any missing key, instead of raising `KeyError`.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-05-collections-counter-defaultdict-namedtup-003-8e245f930e.html"
 width="100%"
></iframe>

Compare to the manual version:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-05-collections-counter-defaultdict-namedtup-004-8f99be5192.html"
 width="100%"
></iframe>

`defaultdict(int)` (factory produces `0`) is the common pattern for counting:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-05-collections-counter-defaultdict-namedtup-005-baa8a3aa78.html"
 width="100%"
></iframe>

## namedtuple: Readable Tuples

`namedtuple` creates a tuple subclass with named fields. Instead of `record[0]` and `record[2]`, you write `record.isbn` and `record.title`.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-05-collections-counter-defaultdict-namedtup-006-59adef159a.html"
 width="100%"
></iframe>

For new code, the `@dataclass` from Unit 3 provides similar readability with mutability and type hints. `namedtuple` shines when you need something lightweight, immutable, and hashable.

## OrderedDict: Insertion-Order Guaranteed

Since Python 3.7, regular `dict` preserves insertion order. `OrderedDict` is now mainly useful for its `move_to_end()` method, which is helpful for implementing LRU caches:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-05-collections-counter-defaultdict-namedtup-007-66be59ab8e.html"
 width="100%"
></iframe>

## deque: Fast Queue Operations

`collections.deque` (double-ended queue) is a list-like structure with O(1) append and pop from *both* ends, unlike a regular list where `pop(0)` is O(n).

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-05-collections-counter-defaultdict-namedtup-008-2393de9653.html"
 width="100%"
></iframe>

## The collections Module at a Glance

| Class | Use case |
|---|---|
| `Counter(iterable)` | Count occurrences; `.most_common(n)` |
| `defaultdict(factory)` | Dict with auto-created default values |
| `namedtuple("N", fields)` | Readable, immutable, hashable tuple subclass |
| `OrderedDict` | Insertion-order dict with `.move_to_end()` |
| `deque` | O(1) append/pop at both ends |

## Your Turn

Write a `catalog_stats(books)` function that returns a summary dict with:
- `"genre_counts"`: a `Counter` of genres
- `"top_genre"`: the most common genre
- `"by_genre"`: a `defaultdict(list)` mapping genre to a list of titles

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-05-collections-counter-defaultdict-namedtup-009-8e125366da.html"
 width="100%"
></iframe>

## Conclusion

`Counter` eliminates manual frequency counting. `defaultdict` eliminates missing-key boilerplate. `namedtuple` makes tuple fields readable. `deque` enables efficient queue operations. All four are built in, battle-tested, and immediately more expressive than their manual equivalents. The next lesson revisits `itertools`, applying it to the kind of data pipelines Nadia processes daily.
