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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-06-lazy-evaluation-and-memory-effic-001-2281fb1ea6.html"
 width="100%"
></iframe>

The generator creation time is effectively zero because no computation happened. The list construction time and memory are proportional to the number of elements.

## Lazy Evaluation When You Do Not Need All Items

The starkest advantage of lazy evaluation appears when you stop early. If you need only the first matching item in a large sequence, eager evaluation computes all items even though you use only one.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-06-lazy-evaluation-and-memory-effic-002-7e1875f764.html"
 width="100%"
></iframe>

For a dataset where only the last record matches, the eager version processes everything and stores most of it before giving you one result. The lazy version processes items one by one and stops immediately when it finds a match. With `next()`, you also get a clear `StopIteration` (or a default with `next(..., None)`) when nothing matches, rather than an `IndexError`.

## Processing a File Without Loading It

Files are iterators in Python, which means they support lazy line-by-line reading natively. This is particularly important for large log files or CSV exports:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-06-lazy-evaluation-and-memory-effic-003-cc3f367add.html"
 width="100%"
></iframe>

At no point does Python hold the entire file in memory. The operating system reads one buffer at a time, the file object yields one line at a time, and the counter accumulates. This scales to a file of any size.

## When Laziness Does Not Help (and May Hurt)

Lazy evaluation is not always the right choice. If you need to iterate the same sequence multiple times, you must either make it eager (a list) or call the generator function again for each pass.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-06-lazy-evaluation-and-memory-effic-004-47f3b71739.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-06-lazy-evaluation-and-memory-effic-005-b5f8cb9c15.html"
 width="100%"
></iframe>

Create a small text file `catalog.csv` with a few rows of `isbn,title,copies` data, some with copies below 2 and some above. Call `read_large_catalog` and pipe it through `low_stock`, then consume the pipeline with `for`. Verify that at no point does Python hold a full list of records; you can confirm this by adding a `print(f"Yielding {r['title']}")` inside the generator and watching the interleaved output.

## Conclusion

Lazy evaluation defers computation until values are actually needed, which has three concrete benefits: memory is constant regardless of dataset size, early stopping costs nothing for unprocessed items, and pipelines of generators compose naturally without intermediate collections. The trade-off is single-pass use and no random access. The next lesson introduces `itertools`, Python's standard library module that provides ready-made lazy building blocks for common iteration patterns.
