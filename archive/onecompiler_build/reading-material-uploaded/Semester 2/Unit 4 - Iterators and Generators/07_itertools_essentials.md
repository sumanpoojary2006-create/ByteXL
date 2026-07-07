## Introduction

Leila's import pipeline is running efficiently, but she keeps writing the same small utility patterns: take the first N items from a generator, interleave two sequences, repeat a header row, group consecutive records with the same genre. Nadia shows her a module she has been unaware of: `itertools`. Python ships with it in the standard library, and it contains exactly the lazy building blocks she has been reinventing.

This lesson covers the most useful `itertools` functions, focusing on the ones that appear most often in real data pipelines. All of them work lazily, consuming input one item at a time rather than loading everything into memory.

![A library catalog pipeline passing through itertools stations labeled islice, chain, groupby, and zip_longest, each shown as a small efficient machine](images/07_itertools_essentials.png)

## islice: Take a Slice of a Generator

Regular slicing (`my_list[2:5]`) does not work on generators. `itertools.islice` provides slicing for any iterator, lazily.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-07-itertools-essentials-001-c95ed40587.html"
 width="100%"
></iframe>

`islice(iterable, stop)` or `islice(iterable, start, stop)` or `islice(iterable, start, stop, step)` mirrors the regular slice syntax. The generator is only advanced as far as needed; items after `stop` are never requested.

## chain: Combine Multiple Iterables as One

`itertools.chain` concatenates any number of iterables into one seamless sequence, without building a new list.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-07-itertools-essentials-002-b34f7c4e4a.html"
 width="100%"
></iframe>

This is especially useful when processing data from multiple sources (multiple files, multiple API pages) as if they were one stream:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-07-itertools-essentials-003-1923ba8142.html"
 width="100%"
></iframe>

## groupby: Cluster Consecutive Equal Items

`itertools.groupby` groups consecutive items that share a key. Note the word "consecutive": the input must be sorted by the grouping key first.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-07-itertools-essentials-004-70e9c02f10.html"
 width="100%"
></iframe>

## zip_longest: Pair Two Sequences of Unequal Length

Python's built-in `zip` stops at the shortest sequence. `itertools.zip_longest` continues to the longest, filling missing values with a `fillvalue`.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-07-itertools-essentials-005-83c1569886.html"
 width="100%"
></iframe>

## tee: Clone an Iterator

`itertools.tee(iterable, n)` creates n independent iterators from one source. After calling `tee`, you should not use the original iterator directly, only the returned copies.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-07-itertools-essentials-006-0789775fd0.html"
 width="100%"
></iframe>

`tee` buffers internally: items consumed from one copy are stored until the other copy requests them, so if the two copies diverge significantly, memory use grows. It is best used when both copies will be consumed at roughly the same rate.

## itertools Essentials at a Glance

| Function | What it does | Example use |
|---|---|---|
| `islice(it, stop)` | Take first N items lazily | Paginate a generator |
| `islice(it, start, stop)` | Slice a generator by position | Skip the header row |
| `chain(*iterables)` | Concatenate multiple iterables | Merge pages from an API |
| `groupby(it, key)` | Group consecutive items by key | Aggregate sorted records |
| `zip_longest(*its, fillvalue)` | Zip to the longest sequence | Pair unequal-length lists |
| `tee(it, n)` | Clone one iterator into n copies | Process one stream two ways |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-07-itertools-essentials-007-3001e1ff33.html"
 width="100%"
></iframe>

Predict the output before running it. Then extend the exercise: add genre fields and use `groupby` (after sorting) to group the combined catalog by decade (1940s, 1950s, 1960s, 1980s). You will need a key function that computes `year // 10 * 10`.

## Conclusion

`itertools` provides a toolkit of lazy, composable building blocks: `islice` for slicing generators, `chain` for merging multiple iterables, `groupby` for clustering sorted sequences, `zip_longest` for pairing unequal lengths, and `tee` for cloning iterators. All are lazy and memory-efficient by design. The final lesson of this unit synthesizes everything into a practical guideline: when is a generator the right tool, and when should you use a list instead?
