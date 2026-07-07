## Introduction

Nadia keeps writing the same boilerplate: a `{}` dictionary with a check for missing keys before incrementing, tuples with index-based access like `record[2]` that are impossible to read weeks later, and ordered groupings that lose their order when stored in a plain dict. Each time she types this code, she knows there must be a better way.

The `collections` module is the better way. It provides four data structures -- `Counter`, `defaultdict`, `namedtuple`, and `OrderedDict` -- that solve exactly these patterns with less code and more clarity.

![Four drawers in a filing cabinet labeled Counter, defaultdict, namedtuple, and OrderedDict, each with a brief description of when to use it](images/05_collections.png)

## Counter: Count Occurrences

`Counter` takes an iterable and counts how many times each element appears. It is a subclass of `dict`, so every dict method works on it, plus it adds `most_common()`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2NvbGxlY3Rpb25zX2NvdW50ZXJfZGVmYXVsdGRpY3RfbmFtZWR0dXBsZSBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoiZnJvbSBjb2xsZWN0aW9ucyBpbXBvcnQgQ291bnRlclxuXG5nZW5yZXMgPSBbXG4gICAgXCJGaWN0aW9uXCIsIFwiTm9uLUZpY3Rpb25cIiwgXCJGaWN0aW9uXCIsIFwiU2NpZW5jZSBGaWN0aW9uXCIsXG4gICAgXCJGaWN0aW9uXCIsIFwiQmlvZ3JhcGh5XCIsIFwiU2NpZW5jZSBGaWN0aW9uXCIsIFwiRmljdGlvblwiXG5dXG5cbmNvdW50cyA9IENvdW50ZXIoZ2VucmVzKVxucHJpbnQoY291bnRzKVxuIyBDb3VudGVyKHsnRmljdGlvbic6IDQsICdTY2llbmNlIEZpY3Rpb24nOiAyLCAnTm9uLUZpY3Rpb24nOiAxLCAnQmlvZ3JhcGh5JzogMX0pXG5cbnByaW50KGNvdW50c1tcIkZpY3Rpb25cIl0pICAgICAgIyA0XG5wcmludChjb3VudHNbXCJNaXNzaW5nXCJdKSAgICAgICMgMCAobm90IEtleUVycm9yKVxucHJpbnQoY291bnRzLm1vc3RfY29tbW9uKDIpKSAgIyBbKCdGaWN0aW9uJywgNCksICgnU2NpZW5jZSBGaWN0aW9uJywgMildXG5cbiMgQ29tYmluZSB0d28gQ291bnRlcnM6XG5tb3JlID0gQ291bnRlcihbXCJCaW9ncmFwaHlcIiwgXCJCaW9ncmFwaHlcIiwgXCJGaWN0aW9uXCJdKVxuY29tYmluZWQgPSBjb3VudHMgKyBtb3JlXG5wcmludChjb21iaW5lZFtcIkJpb2dyYXBoeVwiXSkgICMgMyJ9"
 width="100%"
></iframe>

`Counter` also works for individual strings:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2NvbGxlY3Rpb25zX2NvdW50ZXJfZGVmYXVsdGRpY3RfbmFtZWR0dXBsZSBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoibGV0dGVyX2ZyZXEgPSBDb3VudGVyKFwiYWJyYWNhZGFicmFcIilcbnByaW50KGxldHRlcl9mcmVxLm1vc3RfY29tbW9uKDMpKSAgICMgWygnYScsIDUpLCAoJ2InLCAyKSwgKCdyJywgMildIn0"
 width="100%"
></iframe>

## defaultdict: Avoid Missing-Key Checks

`defaultdict` is a dict that calls a factory function to produce a default value for any missing key, instead of raising `KeyError`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2NvbGxlY3Rpb25zX2NvdW50ZXJfZGVmYXVsdGRpY3RfbmFtZWR0dXBsZSBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoiZnJvbSBjb2xsZWN0aW9ucyBpbXBvcnQgZGVmYXVsdGRpY3RcblxuIyBHcm91cCBib29rcyBieSBnZW5yZSB3aXRob3V0IGNoZWNraW5nIGlmIHRoZSBrZXkgZXhpc3RzIGZpcnN0OlxuYm9va3MgPSBbXG4gICAgKFwiOTc4LTAwMVwiLCBcIkR1bmVcIiwgXCJTY2llbmNlIEZpY3Rpb25cIiksXG4gICAgKFwiOTc4LTAwMlwiLCBcIkZvdW5kYXRpb25cIiwgXCJTY2llbmNlIEZpY3Rpb25cIiksXG4gICAgKFwiOTc4LTAwM1wiLCBcIjE5ODRcIiwgXCJGaWN0aW9uXCIpLFxuICAgIChcIjk3OC0wMDRcIiwgXCJOZXVyb21hbmNlclwiLCBcIlNjaWVuY2UgRmljdGlvblwiKSxcbl1cblxuYnlfZ2VucmUgPSBkZWZhdWx0ZGljdChsaXN0KSAgICMgZGVmYXVsdCBmYWN0b3J5OiBsaXN0KClcbmZvciBpc2JuLCB0aXRsZSwgZ2VucmUgaW4gYm9va3M6XG4gICAgYnlfZ2VucmVbZ2VucmVdLmFwcGVuZCh0aXRsZSlcblxucHJpbnQoZGljdChieV9nZW5yZSkpXG4jIHsnU2NpZW5jZSBGaWN0aW9uJzogWydEdW5lJywgJ0ZvdW5kYXRpb24nLCAnTmV1cm9tYW5jZXInXSwgJ0ZpY3Rpb24nOiBbJzE5ODQnXX0ifQ"
 width="100%"
></iframe>

Compare to the manual version:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2NvbGxlY3Rpb25zX2NvdW50ZXJfZGVmYXVsdGRpY3RfbmFtZWR0dXBsZSBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoiIyBXaXRob3V0IGRlZmF1bHRkaWN0OiB2ZXJib3NlIGtleS1leGlzdGVuY2UgY2hlY2sgZXZlcnkgdGltZVxuYnlfZ2VucmUgPSB7fVxuZm9yIGlzYm4sIHRpdGxlLCBnZW5yZSBpbiBib29rczpcbiAgICBpZiBnZW5yZSBub3QgaW4gYnlfZ2VucmU6XG4gICAgICAgIGJ5X2dlbnJlW2dlbnJlXSA9IFtdXG4gICAgYnlfZ2VucmVbZ2VucmVdLmFwcGVuZCh0aXRsZSkifQ"
 width="100%"
></iframe>

`defaultdict(int)` (factory produces `0`) is the common pattern for counting:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2NvbGxlY3Rpb25zX2NvdW50ZXJfZGVmYXVsdGRpY3RfbmFtZWR0dXBsZSBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoiZnJvbSBjb2xsZWN0aW9ucyBpbXBvcnQgZGVmYXVsdGRpY3RcblxucGF0cm9uX2JvcnJvd3MgPSBkZWZhdWx0ZGljdChpbnQpXG5ldmVudHMgPSBbXCJQMDAxXCIsIFwiUDAwMlwiLCBcIlAwMDFcIiwgXCJQMDAxXCIsIFwiUDAwM1wiLCBcIlAwMDJcIl1cbmZvciBwYXRyb24gaW4gZXZlbnRzOlxuICAgIHBhdHJvbl9ib3Jyb3dzW3BhdHJvbl0gKz0gMSAgICMgbm8gS2V5RXJyb3IgaWYgcGF0cm9uIGlzIG5ld1xuXG5wcmludChkaWN0KHBhdHJvbl9ib3Jyb3dzKSkgICMgeydQMDAxJzogMywgJ1AwMDInOiAyLCAnUDAwMyc6IDF9In0"
 width="100%"
></iframe>

## namedtuple: Readable Tuples

`namedtuple` creates a tuple subclass with named fields. Instead of `record[0]` and `record[2]`, you write `record.isbn` and `record.title`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2NvbGxlY3Rpb25zX2NvdW50ZXJfZGVmYXVsdGRpY3RfbmFtZWR0dXBsZSBjb2RlIDYiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDYucHkiLCJjb2RlIjoiZnJvbSBjb2xsZWN0aW9ucyBpbXBvcnQgbmFtZWR0dXBsZVxuXG5Cb29rID0gbmFtZWR0dXBsZShcIkJvb2tcIiwgW1wiaXNiblwiLCBcInRpdGxlXCIsIFwiZ2VucmVcIiwgXCJjb3BpZXNcIl0pXG5cbmIgPSBCb29rKFwiOTc4LTAwMVwiLCBcIkR1bmVcIiwgXCJTY2llbmNlIEZpY3Rpb25cIiwgMylcbnByaW50KGIuaXNibikgICAgICMgJzk3OC0wMDEnXG5wcmludChiLnRpdGxlKSAgICAjICdEdW5lJ1xucHJpbnQoYlswXSkgICAgICAgIyAnOTc4LTAwMScgLS0gc3RpbGwgd29ya3MgYXMgYSB0dXBsZVxucHJpbnQoYikgICAgICAgICAgIyBCb29rKGlzYm49Jzk3OC0wMDEnLCB0aXRsZT0nRHVuZScsIGdlbnJlPSdTY2llbmNlIEZpY3Rpb24nLCBjb3BpZXM9MylcblxuIyBOYW1lZHR1cGxlcyBhcmUgaW1tdXRhYmxlIGFuZCBoYXNoYWJsZSAtLSBjYW4gYmUgdXNlZCBhcyBkaWN0IGtleXNcbmJvb2tfZGljdCA9IHtiOiBcImF2YWlsYWJsZVwifSJ9"
 width="100%"
></iframe>

For new code, the `@dataclass` from Unit 3 provides similar readability with mutability and type hints. `namedtuple` shines when you need something lightweight, immutable, and hashable.

## OrderedDict: Insertion-Order Guaranteed

Since Python 3.7, regular `dict` preserves insertion order. `OrderedDict` is now mainly useful for its `move_to_end()` method, which is helpful for implementing LRU caches:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2NvbGxlY3Rpb25zX2NvdW50ZXJfZGVmYXVsdGRpY3RfbmFtZWR0dXBsZSBjb2RlIDciLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDcucHkiLCJjb2RlIjoiZnJvbSBjb2xsZWN0aW9ucyBpbXBvcnQgT3JkZXJlZERpY3RcblxuY2FjaGUgPSBPcmRlcmVkRGljdCgpXG5jYWNoZVtcIjk3OC0wMDFcIl0gPSB7XCJ0aXRsZVwiOiBcIkR1bmVcIn1cbmNhY2hlW1wiOTc4LTAwMlwiXSA9IHtcInRpdGxlXCI6IFwiRm91bmRhdGlvblwifVxuY2FjaGVbXCI5NzgtMDAzXCJdID0ge1widGl0bGVcIjogXCJOZXVyb21hbmNlclwifVxuXG4jIE1vdmUgbW9zdCByZWNlbnRseSBhY2Nlc3NlZCB0byB0aGUgZW5kIChMUlUgcGF0dGVybilcbmNhY2hlLm1vdmVfdG9fZW5kKFwiOTc4LTAwMVwiKVxucHJpbnQobGlzdChjYWNoZS5rZXlzKCkpKSAgICMgWyc5NzgtMDAyJywgJzk3OC0wMDMnLCAnOTc4LTAwMSddXG5cbiMgRXZpY3QgdGhlIGxlYXN0IHJlY2VudGx5IHVzZWQgKGZyb20gdGhlIGZyb250KVxub2xkZXN0X2tleSA9IG5leHQoaXRlcihjYWNoZSkpXG5kZWwgY2FjaGVbb2xkZXN0X2tleV0ifQ"
 width="100%"
></iframe>

## deque: Fast Queue Operations

`collections.deque` (double-ended queue) is a list-like structure with O(1) append and pop from *both* ends, unlike a regular list where `pop(0)` is O(n).

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2NvbGxlY3Rpb25zX2NvdW50ZXJfZGVmYXVsdGRpY3RfbmFtZWR0dXBsZSBjb2RlIDgiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDgucHkiLCJjb2RlIjoiZnJvbSBjb2xsZWN0aW9ucyBpbXBvcnQgZGVxdWVcblxud2FpdF9saXN0ID0gZGVxdWUoKVxud2FpdF9saXN0LmFwcGVuZChcIlBhdHJvbiBBXCIpICAgICAjIGFkZCB0byByaWdodFxud2FpdF9saXN0LmFwcGVuZChcIlBhdHJvbiBCXCIpXG53YWl0X2xpc3QuYXBwZW5kbGVmdChcIlBhdHJvbiBaXCIpICMgYWRkIHRvIGxlZnQgKHByaW9yaXR5KVxuXG5wcmludCh3YWl0X2xpc3QucG9wbGVmdCgpKSAgIyAnUGF0cm9uIFonIC0tIE8oMSlcbnByaW50KHdhaXRfbGlzdC5wb3BsZWZ0KCkpICAjICdQYXRyb24gQScgLS0gTygxKSJ9"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2NvbGxlY3Rpb25zX2NvdW50ZXJfZGVmYXVsdGRpY3RfbmFtZWR0dXBsZSBjb2RlIDkiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDkucHkiLCJjb2RlIjoiZnJvbSBjb2xsZWN0aW9ucyBpbXBvcnQgQ291bnRlciwgZGVmYXVsdGRpY3RcblxuZGVmIGNhdGFsb2dfc3RhdHMoYm9va3MpOlxuICAgIGdlbnJlX2NvdW50cyA9IENvdW50ZXIoYi5nZW5yZSBmb3IgYiBpbiBib29rcylcbiAgICBieV9nZW5yZSA9IGRlZmF1bHRkaWN0KGxpc3QpXG4gICAgZm9yIGIgaW4gYm9va3M6XG4gICAgICAgIGJ5X2dlbnJlW2IuZ2VucmVdLmFwcGVuZChiLnRpdGxlKVxuICAgIHJldHVybiB7XG4gICAgICAgIFwiZ2VucmVfY291bnRzXCI6IGdlbnJlX2NvdW50cyxcbiAgICAgICAgXCJ0b3BfZ2VucmVcIjogZ2VucmVfY291bnRzLm1vc3RfY29tbW9uKDEpWzBdWzBdLFxuICAgICAgICBcImJ5X2dlbnJlXCI6IGRpY3QoYnlfZ2VucmUpLFxuICAgIH1cblxuZnJvbSBjb2xsZWN0aW9ucyBpbXBvcnQgbmFtZWR0dXBsZVxuQm9vayA9IG5hbWVkdHVwbGUoXCJCb29rXCIsIFtcImlzYm5cIiwgXCJ0aXRsZVwiLCBcImdlbnJlXCJdKVxuY2F0YWxvZyA9IFtcbiAgICBCb29rKFwiOTc4LTAwMVwiLCBcIkR1bmVcIiwgXCJTY2ktRmlcIiksXG4gICAgQm9vayhcIjk3OC0wMDJcIiwgXCJGb3VuZGF0aW9uXCIsIFwiU2NpLUZpXCIpLFxuICAgIEJvb2soXCI5NzgtMDAzXCIsIFwiMTk4NFwiLCBcIkZpY3Rpb25cIiksXG5dXG5wcmludChjYXRhbG9nX3N0YXRzKGNhdGFsb2cpKSJ9"
 width="100%"
></iframe>

## Conclusion

`Counter` eliminates manual frequency counting. `defaultdict` eliminates missing-key boilerplate. `namedtuple` makes tuple fields readable. `deque` enables efficient queue operations. All four are built in, battle-tested, and immediately more expressive than their manual equivalents. The next lesson revisits `itertools`, applying it to the kind of data pipelines Nadia processes daily.
