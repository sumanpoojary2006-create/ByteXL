## Introduction

In Unit 4, Nadia learned `islice`, `chain`, `groupby`, and `zip_longest` as building blocks for lazy iteration. Now she is writing real data pipelines for the consortium: flattening multi-level catalog hierarchies, grouping overdue records by month, generating all possible genre pairs for a recommendation engine, and creating sliding windows over borrow histories. Each of these is a few lines with `itertools`, and a mess of nested loops without it.

This lesson goes deeper into `itertools`, covering the combinatoric functions and two additional patterns from the "infinite iterators" and "terminating iterators" categories that are most useful in data work.

![A pipeline diagram showing itertools functions as connectors between a data source and a result: chain connects multiple catalogs, groupby groups them, product generates pairs, and accumulate produces running totals](images/06_itertools_advanced.png)

## Recap: chain, islice, groupby

Before moving to new functions, a quick review of the essentials:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2l0ZXJ0b29sc19hZHZhbmNlZCBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoiaW1wb3J0IGl0ZXJ0b29sc1xuXG4jIGNoYWluOiBtZXJnZSBtdWx0aXBsZSBpdGVyYWJsZXMgaW50byBvbmVcbmFsbF9ib29rcyA9IGxpc3QoaXRlcnRvb2xzLmNoYWluKGZpY3Rpb25fYm9va3MsIG5vbmZpY3Rpb25fYm9va3MsIHNjaV9maV9ib29rcykpXG5cbiMgaXNsaWNlOiB0YWtlIHRoZSBmaXJzdCBOIGZyb20gYW55IGl0ZXJhYmxlIChpbmNsdWRpbmcgZ2VuZXJhdG9ycylcbmZpcnN0X3RlbiA9IGxpc3QoaXRlcnRvb2xzLmlzbGljZShhbGxfYm9va3MsIDEwKSlcblxuIyBncm91cGJ5OiBncm91cCBjb25zZWN1dGl2ZSBlbGVtZW50cyBieSBrZXkgKHJlcXVpcmVzIHNvcnRpbmcgZmlyc3QpXG5yZWNvcmRzX3NvcnRlZCA9IHNvcnRlZChvdmVyZHVlX3JlY29yZHMsIGtleT1sYW1iZGEgcjogcltcIm1vbnRoXCJdKVxuZm9yIG1vbnRoLCBncm91cCBpbiBpdGVydG9vbHMuZ3JvdXBieShyZWNvcmRzX3NvcnRlZCwga2V5PWxhbWJkYSByOiByW1wibW9udGhcIl0pOlxuICAgIHByaW50KGZcInttb250aH06IHtsaXN0KGdyb3VwKX1cIikifQ"
 width="100%"
></iframe>

`groupby` only groups *consecutive* elements, so always sort by the grouping key first.

## product: Cartesian Product

`itertools.product` produces every combination of elements from two or more iterables. It is the nested-loop equivalent without the indentation:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2l0ZXJ0b29sc19hZHZhbmNlZCBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoiaW1wb3J0IGl0ZXJ0b29sc1xuXG5nZW5yZXMgPSBbXCJGaWN0aW9uXCIsIFwiTm9uLUZpY3Rpb25cIiwgXCJTY2llbmNlIEZpY3Rpb25cIl1cbmZvcm1hdHMgPSBbXCJIYXJkY292ZXJcIiwgXCJQYXBlcmJhY2tcIiwgXCJFLWJvb2tcIl1cblxuIyBFdmVyeSBnZW5yZS1mb3JtYXQgcGFpcjpcbmZvciBnZW5yZSwgZm10IGluIGl0ZXJ0b29scy5wcm9kdWN0KGdlbnJlcywgZm9ybWF0cyk6XG4gICAgcHJpbnQoZlwie2dlbnJlfSAvIHtmbXR9XCIpXG4jIEZpY3Rpb24gLyBIYXJkY292ZXJcbiMgRmljdGlvbiAvIFBhcGVyYmFja1xuIyBGaWN0aW9uIC8gRS1ib29rXG4jIE5vbi1GaWN0aW9uIC8gSGFyZGNvdmVyXG4jIC4uLlxuXG4jIFdpdGhvdXQgaXRlcnRvb2xzIC0tIGVxdWl2YWxlbnQgYnV0IG5lc3RlZDpcbmZvciBnZW5yZSBpbiBnZW5yZXM6XG4gICAgZm9yIGZtdCBpbiBmb3JtYXRzOlxuICAgICAgICBwcmludChmXCJ7Z2VucmV9IC8ge2ZtdH1cIikifQ"
 width="100%"
></iframe>

`product` also accepts a `repeat` argument: `product("ABC", repeat=2)` produces `AA, AB, AC, BA, BB, ...`.

## combinations and combinations_with_replacement

`itertools.combinations` picks all unique ordered subsets of length k from an iterable, without repeating elements:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2l0ZXJ0b29sc19hZHZhbmNlZCBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoiaW1wb3J0IGl0ZXJ0b29sc1xuXG5wYXRyb25zID0gW1wiQWxpY2VcIiwgXCJCb2JcIiwgXCJDYXJvbFwiLCBcIkRpYW5hXCJdXG5cbiMgQWxsIHBhaXJzIG9mIHBhdHJvbnMgZm9yIGEgcmVhZGluZyBncm91cDpcbnBhaXJzID0gbGlzdChpdGVydG9vbHMuY29tYmluYXRpb25zKHBhdHJvbnMsIDIpKVxucHJpbnQocGFpcnMpXG4jIFsoJ0FsaWNlJywgJ0JvYicpLCAoJ0FsaWNlJywgJ0Nhcm9sJyksICgnQWxpY2UnLCAnRGlhbmEnKSxcbiMgICgnQm9iJywgJ0Nhcm9sJyksICgnQm9iJywgJ0RpYW5hJyksICgnQ2Fyb2wnLCAnRGlhbmEnKV1cblxuIyBBbGwgcGFpcnMgaW5jbHVkaW5nIHNhbWUtcGVyc29uIHBhaXJzOlxucGFpcnNfd2l0aF9yZXAgPSBsaXN0KGl0ZXJ0b29scy5jb21iaW5hdGlvbnNfd2l0aF9yZXBsYWNlbWVudChwYXRyb25zLCAyKSlcbnByaW50KHBhaXJzX3dpdGhfcmVwKVxuIyBbKCdBbGljZScsICdBbGljZScpLCAoJ0FsaWNlJywgJ0JvYicpLCAuLi5dIn0"
 width="100%"
></iframe>

## permutations: Ordered Arrangements

`itertools.permutations` produces all ordered arrangements of length k:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2l0ZXJ0b29sc19hZHZhbmNlZCBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoiaW1wb3J0IGl0ZXJ0b29sc1xuXG5zaGVsZl9wb3NpdGlvbnMgPSBbXCJBXCIsIFwiQlwiLCBcIkNcIl1cbmFycmFuZ2VtZW50cyA9IGxpc3QoaXRlcnRvb2xzLnBlcm11dGF0aW9ucyhzaGVsZl9wb3NpdGlvbnMsIDIpKVxucHJpbnQoYXJyYW5nZW1lbnRzKVxuIyBbKCdBJywgJ0InKSwgKCdBJywgJ0MnKSwgKCdCJywgJ0EnKSwgKCdCJywgJ0MnKSwgKCdDJywgJ0EnKSwgKCdDJywgJ0InKV0ifQ"
 width="100%"
></iframe>

`combinations` (order doesn't matter) vs `permutations` (order matters): `("Alice", "Bob")` and `("Bob", "Alice")` are the same combination but different permutations.

## accumulate: Running Totals

`itertools.accumulate` produces a running accumulated value. By default it sums, but any two-argument function works:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2l0ZXJ0b29sc19hZHZhbmNlZCBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoiaW1wb3J0IGl0ZXJ0b29sc1xuaW1wb3J0IG9wZXJhdG9yXG5cbmRhaWx5X2JvcnJvd3MgPSBbMTIsIDgsIDIwLCAxNSwgMzAsIDcsIDI1XVxuXG4jIFJ1bm5pbmcgdG90YWw6XG5ydW5uaW5nX3RvdGFsID0gbGlzdChpdGVydG9vbHMuYWNjdW11bGF0ZShkYWlseV9ib3Jyb3dzKSlcbnByaW50KHJ1bm5pbmdfdG90YWwpICAgIyBbMTIsIDIwLCA0MCwgNTUsIDg1LCA5MiwgMTE3XVxuXG4jIFJ1bm5pbmcgbWF4aW11bTpcbnJ1bm5pbmdfbWF4ID0gbGlzdChpdGVydG9vbHMuYWNjdW11bGF0ZShkYWlseV9ib3Jyb3dzLCBmdW5jPW1heCkpXG5wcmludChydW5uaW5nX21heCkgICAgICMgWzEyLCAxMiwgMjAsIDIwLCAzMCwgMzAsIDMwXVxuXG4jIFJ1bm5pbmcgcHJvZHVjdDpcbnJ1bm5pbmdfcHJvZHVjdCA9IGxpc3QoaXRlcnRvb2xzLmFjY3VtdWxhdGUoWzEsIDIsIDMsIDQsIDVdLCBmdW5jPW9wZXJhdG9yLm11bCkpXG5wcmludChydW5uaW5nX3Byb2R1Y3QpICAjIFsxLCAyLCA2LCAyNCwgMTIwXSJ9"
 width="100%"
></iframe>

## takewhile and dropwhile: Condition-Based Slicing

`takewhile` yields elements while the predicate is `True`, then stops. `dropwhile` skips elements while the predicate is `True`, then yields the rest:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2l0ZXJ0b29sc19hZHZhbmNlZCBjb2RlIDYiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDYucHkiLCJjb2RlIjoiaW1wb3J0IGl0ZXJ0b29sc1xuXG5kYWlseV9ib3Jyb3dzID0gWzEyLCA4LCAyMCwgMTUsIDMwLCA3LCAyNV1cblxuIyBUYWtlIHdoaWxlIGJlbG93IHRocmVzaG9sZDpcbmJ1c3kgPSBsaXN0KGl0ZXJ0b29scy50YWtld2hpbGUobGFtYmRhIHg6IHggPj0gMTAsIGRhaWx5X2JvcnJvd3MpKVxucHJpbnQoYnVzeSkgICAjIFsxMl0gICAtLSBzdG9wcyBhdCA4IChmaXJzdCBmYWlsdXJlKVxuXG4jIERyb3Agd2hpbGUgYmVsb3cgdGhyZXNob2xkLCB0YWtlIHRoZSByZXN0OlxuYWZ0ZXJfc2xvdyA9IGxpc3QoaXRlcnRvb2xzLmRyb3B3aGlsZShsYW1iZGEgeDogeCA8IDIwLCBkYWlseV9ib3Jyb3dzKSlcbnByaW50KGFmdGVyX3Nsb3cpICAgIyBbMjAsIDE1LCAzMCwgNywgMjVdICAgLS0gZmlyc3QgaXRlbSA-PSAyMCBhbmQgZXZlcnl0aGluZyBhZnRlciJ9"
 width="100%"
></iframe>

## itertools Advanced at a Glance

| Function | What it produces |
|---|---|
| `product(a, b)` | Every combination of one element from a and one from b |
| `combinations(seq, k)` | All unique unordered subsets of size k |
| `permutations(seq, k)` | All ordered arrangements of size k |
| `accumulate(seq, func)` | Running accumulated values |
| `takewhile(pred, seq)` | Elements while predicate holds |
| `dropwhile(pred, seq)` | Elements after predicate first fails |

## Your Turn

Given a catalog of books and a list of patron IDs, use `itertools.product` to generate all `(patron, book)` pairs for a recommendation engine, then use `islice` to return only the first 10 pairs:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2l0ZXJ0b29sc19hZHZhbmNlZCBjb2RlIDciLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDcucHkiLCJjb2RlIjoiaW1wb3J0IGl0ZXJ0b29sc1xuXG5wYXRyb25zID0gW1wiUDAwMVwiLCBcIlAwMDJcIiwgXCJQMDAzXCJdXG5ib29rcyA9IFtcIjk3OC0wMDFcIiwgXCI5NzgtMDAyXCIsIFwiOTc4LTAwM1wiLCBcIjk3OC0wMDRcIl1cblxuZmlyc3RfdGVuID0gbGlzdChpdGVydG9vbHMuaXNsaWNlKGl0ZXJ0b29scy5wcm9kdWN0KHBhdHJvbnMsIGJvb2tzKSwgMTApKVxuZm9yIHBhdHJvbiwgYm9vayBpbiBmaXJzdF90ZW46XG4gICAgcHJpbnQoZlwie3BhdHJvbn0gLT4ge2Jvb2t9XCIpIn0"
 width="100%"
></iframe>

Then use `accumulate` to compute the running total of books borrowed over a 7-day period, and identify the first day the total exceeded 50.

## Conclusion

`itertools` provides lazy, composable iteration tools that eliminate nested loops and intermediate lists. `product`, `combinations`, and `permutations` handle combinatorial problems. `accumulate` builds running aggregations. `takewhile` and `dropwhile` provide condition-based slicing. The next lesson looks at `os`, `sys`, and `pathlib` for file system operations.
