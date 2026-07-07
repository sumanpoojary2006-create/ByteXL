## Introduction

Leila's million-record import is now running on generators, and it uses a fraction of the memory it used before. But her colleague Arjun is skeptical. He says it must be slower because it is "doing more work." Leila realizes she cannot actually explain why he is wrong without understanding what lazy evaluation costs and what it saves.

This lesson addresses that question directly. Lazy evaluation is not "slower than eager." It is a different trade-off: you pay less upfront to avoid computing things you might never use, and you pay close to nothing in memory regardless of dataset size. Understanding when laziness helps and when it hurts is the practical skill this lesson builds.

![](images/06_lazy_evaluation_memory.png)

## Eager vs. Lazy: A Concrete Comparison

**Eager evaluation** means computing all values immediately and storing them. A list comprehension is eager. `map()` in Python 2 was eager. You pay the full memory cost upfront, but you can revisit any value instantly afterward.

**Lazy evaluation** means computing values only when requested. Generator functions and expressions are lazy. You pay almost no memory, but once a value is used, it is gone unless you saved it elsewhere.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2xhenlfZXZhbHVhdGlvbl9hbmRfbWVtb3J5X2VmZmljaWVuY3kgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6ImltcG9ydCBzeXNcbmltcG9ydCB0aW1lXG5cbiMgRWFnZXI6IGJ1aWxkcyB0aGUgZW50aXJlIGxpc3QgZmlyc3RcbnN0YXJ0ID0gdGltZS50aW1lKClcbmVhZ2VyID0gW3ggKiB4IGZvciB4IGluIHJhbmdlKDFfMDAwXzAwMCldXG5wcmludChmXCJFYWdlciBsaXN0IGJ1aWx0IGluIHt0aW1lLnRpbWUoKSAtIHN0YXJ0Oi4zZn1zXCIpXG5wcmludChmXCJNZW1vcnk6IHtzeXMuZ2V0c2l6ZW9mKGVhZ2VyKTosfSBieXRlc1wiKVxuXG4jIExhenk6IGJ1aWxkcyBub3RoaW5nOyBvbmx5IHRoZSBnZW5lcmF0b3Igb2JqZWN0IGV4aXN0c1xuc3RhcnQgPSB0aW1lLnRpbWUoKVxubGF6eSA9ICh4ICogeCBmb3IgeCBpbiByYW5nZSgxXzAwMF8wMDApKVxucHJpbnQoZlwiTGF6eSBnZW4gY3JlYXRlZCBpbiB7dGltZS50aW1lKCkgLSBzdGFydDouNWZ9c1wiKVxucHJpbnQoZlwiTWVtb3J5OiB7c3lzLmdldHNpemVvZihsYXp5KX0gYnl0ZXNcIikifQ"
 width="100%"
></iframe>

The generator creation time is effectively zero because no computation happened. The list construction time and memory are proportional to the number of elements.

## Lazy Evaluation When You Do Not Need All Items

The starkest advantage of lazy evaluation appears when you stop early. If you need only the first matching item in a large sequence, eager evaluation computes all items even though you use only one.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2xhenlfZXZhbHVhdGlvbl9hbmRfbWVtb3J5X2VmZmljaWVuY3kgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6InJlY29yZHMgPSBbe1wiaXNiblwiOiBzdHIoaSksIFwiYXBwcm92ZWRcIjogaSA9PSA5OTlfOTk5fSBmb3IgaSBpbiByYW5nZSgxXzAwMF8wMDApXVxuXG4jIEVhZ2VyOiBidWlsZHMgYSBmaWx0ZXJlZCBsaXN0IG9mIGFsbCAxLDAwMCwwMDAgcmVjb3JkcywgdGhlbiB0YWtlcyB0aGUgZmlyc3RcbmZpcnN0X2FwcHJvdmVkX2VhZ2VyID0gW3IgZm9yIHIgaW4gcmVjb3JkcyBpZiByW1wiYXBwcm92ZWRcIl1dWzBdXG5cbiMgTGF6eTogc3RvcHMgYXMgc29vbiBhcyB0aGUgZmlyc3QgYXBwcm92ZWQgcmVjb3JkIGlzIGZvdW5kXG5maXJzdF9hcHByb3ZlZF9sYXp5ID0gbmV4dChyIGZvciByIGluIHJlY29yZHMgaWYgcltcImFwcHJvdmVkXCJdKSJ9"
 width="100%"
></iframe>

For a dataset where only the last record matches, the eager version processes everything and stores most of it before giving you one result. The lazy version processes items one by one and stops immediately when it finds a match. With `next()`, you also get a clear `StopIteration` (or a default with `next(..., None)`) when nothing matches, rather than an `IndexError`.

## Processing a File Without Loading It

Files are iterators in Python, which means they support lazy line-by-line reading natively. This is particularly important for large log files or CSV exports:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2xhenlfZXZhbHVhdGlvbl9hbmRfbWVtb3J5X2VmZmljaWVuY3kgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6ImRlZiBjb3VudF9hcHByb3ZlZF9pbl9maWxlKGZpbGVwYXRoKTpcbiAgICBjb3VudCA9IDBcbiAgICB3aXRoIG9wZW4oZmlsZXBhdGgpIGFzIGY6XG4gICAgICAgIGZvciBsaW5lIGluIGY6ICAgICAgICAgICAgICAgICMgcmVhZHMgb25lIGxpbmUgYXQgYSB0aW1lXG4gICAgICAgICAgICBpZiBcImFwcHJvdmVkPVRydWVcIiBpbiBsaW5lOlxuICAgICAgICAgICAgICAgIGNvdW50ICs9IDFcbiAgICByZXR1cm4gY291bnQifQ"
 width="100%"
></iframe>

At no point does Python hold the entire file in memory. The operating system reads one buffer at a time, the file object yields one line at a time, and the counter accumulates. This scales to a file of any size.

## When Laziness Does Not Help (and May Hurt)

Lazy evaluation is not always the right choice. If you need to iterate the same sequence multiple times, you must either make it eager (a list) or call the generator function again for each pass.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2xhenlfZXZhbHVhdGlvbl9hbmRfbWVtb3J5X2VmZmljaWVuY3kgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6ImFwcHJvdmVkID0gKHIgZm9yIHIgaW4gcmVjb3JkcyBpZiByW1wiYXBwcm92ZWRcIl0pXG5cbiMgRmlyc3QgcGFzczogd29ya3NcbmZvciByIGluIGFwcHJvdmVkOlxuICAgIHByb2Nlc3MocilcblxuIyBTZWNvbmQgcGFzczogZ2VuZXJhdG9yIGlzIGV4aGF1c3RlZCwgbm90aGluZyBoYXBwZW5zXG5mb3IgciBpbiBhcHByb3ZlZDpcbiAgICBwcmludChcIlRoaXMgbmV2ZXIgcHJpbnRzXCIpIn0"
 width="100%"
></iframe>

If you need random access (e.g., `gen[500]`), `len()`, or sorting, you also need a list. A generator cannot support these operations.

## Memory Efficiency at a Glance

| Scenario | Eager (list) | Lazy (generator) |
|---|---|---|
| Memory usage | Proportional to output size | Constant (generator state only) |
| First item only | Must build everything first | Stops immediately |
| Multiple iterations | Trivial (re-iterate the list) | Must re-call the generator function |
| Random access | Supported (`lst[i]`) | Not supported |
| Early stopping | Still builds full list first | Stops at first matching item |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2xhenlfZXZhbHVhdGlvbl9hbmRfbWVtb3J5X2VmZmljaWVuY3kgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6ImRlZiByZWFkX2xhcmdlX2NhdGFsb2coZmlsZXBhdGgpOlxuICAgIHdpdGggb3BlbihmaWxlcGF0aCkgYXMgZjpcbiAgICAgICAgZm9yIGxpbmUgaW4gZjpcbiAgICAgICAgICAgIHBhcnRzID0gbGluZS5zdHJpcCgpLnNwbGl0KFwiLFwiKVxuICAgICAgICAgICAgaWYgbGVuKHBhcnRzKSA9PSAzOlxuICAgICAgICAgICAgICAgIHlpZWxkIHtcImlzYm5cIjogcGFydHNbMF0sIFwidGl0bGVcIjogcGFydHNbMV0sIFwiY29waWVzXCI6IGludChwYXJ0c1syXSl9XG5cbmRlZiBsb3dfc3RvY2socmVjb3JkcywgdGhyZXNob2xkPTIpOlxuICAgIHJldHVybiAociBmb3IgciBpbiByZWNvcmRzIGlmIHJbXCJjb3BpZXNcIl0gPCB0aHJlc2hvbGQpIn0"
 width="100%"
></iframe>

Create a small text file `catalog.csv` with a few rows of `isbn,title,copies` data, some with copies below 2 and some above. Call `read_large_catalog` and pipe it through `low_stock`, then consume the pipeline with `for`. Verify that at no point does Python hold a full list of records; you can confirm this by adding a `print(f"Yielding {r['title']}")` inside the generator and watching the interleaved output.

## Conclusion

Lazy evaluation defers computation until values are actually needed, which has three concrete benefits: memory is constant regardless of dataset size, early stopping costs nothing for unprocessed items, and pipelines of generators compose naturally without intermediate collections. The trade-off is single-pass use and no random access. The next lesson introduces `itertools`, Python's standard library module that provides ready-made lazy building blocks for common iteration patterns.
