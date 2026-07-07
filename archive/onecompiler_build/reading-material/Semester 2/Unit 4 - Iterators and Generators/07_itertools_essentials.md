## Introduction

Leila's import pipeline is running efficiently, but she keeps writing the same small utility patterns: take the first N items from a generator, interleave two sequences, repeat a header row, group consecutive records with the same genre. Nadia shows her a module she has been unaware of: `itertools`. Python ships with it in the standard library, and it contains exactly the lazy building blocks she has been reinventing.

This lesson covers the most useful `itertools` functions, focusing on the ones that appear most often in real data pipelines. All of them work lazily, consuming input one item at a time rather than loading everything into memory.

![A library catalog pipeline passing through itertools stations labeled islice, chain, groupby, and zip_longest, each shown as a small efficient machine](images/07_itertools_essentials.png)

## islice: Take a Slice of a Generator

Regular slicing (`my_list[2:5]`) does not work on generators. `itertools.islice` provides slicing for any iterator, lazily.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2l0ZXJ0b29sc19lc3NlbnRpYWxzIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJpbXBvcnQgaXRlcnRvb2xzXG5cbmRlZiBhbGxfYm9va3MoKTpcbiAgICBjYXRhbG9nID0gW1wiRHVuZVwiLCBcIkZvdW5kYXRpb25cIiwgXCJTaG9ndW5cIiwgXCJOZXVyb21hbmNlclwiLCBcIjE5ODRcIiwgXCJCcmF2ZSBOZXcgV29ybGRcIl1cbiAgICBmb3IgYm9vayBpbiBjYXRhbG9nOlxuICAgICAgICB5aWVsZCBib29rXG5cbiMgVGFrZSBib29rcyAyIHRocm91Z2ggNCAoemVyby1pbmRleGVkKVxuZm9yIHRpdGxlIGluIGl0ZXJ0b29scy5pc2xpY2UoYWxsX2Jvb2tzKCksIDIsIDUpOlxuICAgIHByaW50KHRpdGxlKVxuIyBTaG9ndW5cbiMgTmV1cm9tYW5jZXJcbiMgMTk4NCJ9"
 width="100%"
></iframe>

`islice(iterable, stop)` or `islice(iterable, start, stop)` or `islice(iterable, start, stop, step)` mirrors the regular slice syntax. The generator is only advanced as far as needed; items after `stop` are never requested.

## chain: Combine Multiple Iterables as One

`itertools.chain` concatenates any number of iterables into one seamless sequence, without building a new list.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2l0ZXJ0b29sc19lc3NlbnRpYWxzIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJpbXBvcnQgaXRlcnRvb2xzXG5cbmZpY3Rpb24gPSBbXCJEdW5lXCIsIFwiRm91bmRhdGlvblwiXVxubm9uX2ZpY3Rpb24gPSBbXCJTYXBpZW5zXCIsIFwiQSBCcmllZiBIaXN0b3J5IG9mIFRpbWVcIl1cbnJlZmVyZW5jZSA9IFtcIk94Zm9yZCBFbmdsaXNoIERpY3Rpb25hcnlcIl1cblxuYWxsX2l0ZW1zID0gaXRlcnRvb2xzLmNoYWluKGZpY3Rpb24sIG5vbl9maWN0aW9uLCByZWZlcmVuY2UpXG5mb3IgdGl0bGUgaW4gYWxsX2l0ZW1zOlxuICAgIHByaW50KHRpdGxlKVxuIyBEdW5lLCBGb3VuZGF0aW9uLCBTYXBpZW5zLCBBIEJyaWVmIEhpc3Rvcnkgb2YgVGltZSwgT3hmb3JkIEVuZ2xpc2ggRGljdGlvbmFyeSJ9"
 width="100%"
></iframe>

This is especially useful when processing data from multiple sources (multiple files, multiple API pages) as if they were one stream:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2l0ZXJ0b29sc19lc3NlbnRpYWxzIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJpbXBvcnQgaXRlcnRvb2xzXG5cbmRlZiBwYWdlX29uZSgpOlxuICAgIHlpZWxkIHtcImlzYm5cIjogXCIwMDFcIiwgXCJ0aXRsZVwiOiBcIkR1bmVcIn1cbiAgICB5aWVsZCB7XCJpc2JuXCI6IFwiMDAyXCIsIFwidGl0bGVcIjogXCJGb3VuZGF0aW9uXCJ9XG5cbmRlZiBwYWdlX3R3bygpOlxuICAgIHlpZWxkIHtcImlzYm5cIjogXCIwMDNcIiwgXCJ0aXRsZVwiOiBcIlNob2d1blwifVxuXG5mb3IgcmVjb3JkIGluIGl0ZXJ0b29scy5jaGFpbihwYWdlX29uZSgpLCBwYWdlX3R3bygpKTpcbiAgICBwcmludChyZWNvcmRbXCJ0aXRsZVwiXSkifQ"
 width="100%"
></iframe>

## groupby: Cluster Consecutive Equal Items

`itertools.groupby` groups consecutive items that share a key. Note the word "consecutive": the input must be sorted by the grouping key first.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2l0ZXJ0b29sc19lc3NlbnRpYWxzIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJpbXBvcnQgaXRlcnRvb2xzXG5cbmNhdGFsb2cgPSBbXG4gICAge1widGl0bGVcIjogXCJEdW5lXCIsIFwiZ2VucmVcIjogXCJzY2ktZmlcIn0sXG4gICAge1widGl0bGVcIjogXCJGb3VuZGF0aW9uXCIsIFwiZ2VucmVcIjogXCJzY2ktZmlcIn0sXG4gICAge1widGl0bGVcIjogXCJTaG9ndW5cIiwgXCJnZW5yZVwiOiBcImhpc3RvcmljYWxcIn0sXG4gICAge1widGl0bGVcIjogXCJTYXBpZW5zXCIsIFwiZ2VucmVcIjogXCJub24tZmljdGlvblwifSxcbiAgICB7XCJ0aXRsZVwiOiBcIkJyaWVmIEhpc3RvcnlcIiwgXCJnZW5yZVwiOiBcIm5vbi1maWN0aW9uXCJ9LFxuXVxuXG4jIFNvcnQgYnkgZ2VucmUgZmlyc3QgKHJlcXVpcmVkKVxuY2F0YWxvZy5zb3J0KGtleT1sYW1iZGEgcjogcltcImdlbnJlXCJdKVxuXG5mb3IgZ2VucmUsIGl0ZW1zIGluIGl0ZXJ0b29scy5ncm91cGJ5KGNhdGFsb2csIGtleT1sYW1iZGEgcjogcltcImdlbnJlXCJdKTpcbiAgICBwcmludChmXCJ7Z2VucmV9OiB7W2l0ZW1bJ3RpdGxlJ10gZm9yIGl0ZW0gaW4gaXRlbXNdfVwiKVxuIyBoaXN0b3JpY2FsOiBbJ1Nob2d1biddXG4jIG5vbi1maWN0aW9uOiBbJ1NhcGllbnMnLCAnQnJpZWYgSGlzdG9yeSddXG4jIHNjaS1maTogWydEdW5lJywgJ0ZvdW5kYXRpb24nXSJ9"
 width="100%"
></iframe>

## zip_longest: Pair Two Sequences of Unequal Length

Python's built-in `zip` stops at the shortest sequence. `itertools.zip_longest` continues to the longest, filling missing values with a `fillvalue`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2l0ZXJ0b29sc19lc3NlbnRpYWxzIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJpbXBvcnQgaXRlcnRvb2xzXG5cbmlzYm5zID0gW1wiOTc4LTAwMVwiLCBcIjk3OC0wMDJcIiwgXCI5NzgtMDAzXCJdXG50aXRsZXMgPSBbXCJEdW5lXCIsIFwiRm91bmRhdGlvblwiXSAgICAjIG9uZSBzaG9ydGVyIHRoYW4gaXNibnNcblxuZm9yIGlzYm4sIHRpdGxlIGluIGl0ZXJ0b29scy56aXBfbG9uZ2VzdChpc2JucywgdGl0bGVzLCBmaWxsdmFsdWU9XCJVTktOT1dOXCIpOlxuICAgIHByaW50KGlzYm4sIHRpdGxlKVxuIyA5NzgtMDAxIER1bmVcbiMgOTc4LTAwMiBGb3VuZGF0aW9uXG4jIDk3OC0wMDMgVU5LTk9XTiJ9"
 width="100%"
></iframe>

## tee: Clone an Iterator

`itertools.tee(iterable, n)` creates n independent iterators from one source. After calling `tee`, you should not use the original iterator directly, only the returned copies.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2l0ZXJ0b29sc19lc3NlbnRpYWxzIGNvZGUgNiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNi5weSIsImNvZGUiOiJpbXBvcnQgaXRlcnRvb2xzXG5cbmRlZiBhcHByb3ZlZF9yZWNvcmRzKHJlY29yZHMpOlxuICAgIGZvciByIGluIHJlY29yZHM6XG4gICAgICAgIGlmIHIuZ2V0KFwiYXBwcm92ZWRcIik6XG4gICAgICAgICAgICB5aWVsZCByXG5cbnJlY29yZHMgPSBbXG4gICAge1widGl0bGVcIjogXCJEdW5lXCIsIFwiYXBwcm92ZWRcIjogVHJ1ZX0sXG4gICAge1widGl0bGVcIjogXCJGb3VuZGF0aW9uXCIsIFwiYXBwcm92ZWRcIjogVHJ1ZX0sXG5dXG5cbmdlbjEsIGdlbjIgPSBpdGVydG9vbHMudGVlKGFwcHJvdmVkX3JlY29yZHMocmVjb3JkcyksIDIpXG4jIGdlbjEgYW5kIGdlbjIgYXJlIGluZGVwZW5kZW50XG5wcmludChuZXh0KGdlbjEpW1widGl0bGVcIl0pICAgIyBEdW5lXG5wcmludChuZXh0KGdlbjIpW1widGl0bGVcIl0pICAgIyBEdW5lIC0tIGdlbjIgaGFzIGl0cyBvd24gY3Vyc29yIn0"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2l0ZXJ0b29sc19lc3NlbnRpYWxzIGNvZGUgNyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNy5weSIsImNvZGUiOiJpbXBvcnQgaXRlcnRvb2xzXG5cbmJvb2tzX2EgPSBbe1widGl0bGVcIjogXCJEdW5lXCIsIFwieWVhclwiOiAxOTY1fSwge1widGl0bGVcIjogXCJGb3VuZGF0aW9uXCIsIFwieWVhclwiOiAxOTUxfV1cbmJvb2tzX2IgPSBbe1widGl0bGVcIjogXCJOZXVyb21hbmNlclwiLCBcInllYXJcIjogMTk4NH1dXG5cbmNvbWJpbmVkID0gaXRlcnRvb2xzLmNoYWluKGJvb2tzX2EsIGJvb2tzX2IpXG5maXJzdF90d28gPSBpdGVydG9vbHMuaXNsaWNlKGNvbWJpbmVkLCAyKVxuXG5mb3IgYm9vayBpbiBmaXJzdF90d286XG4gICAgcHJpbnQoYm9va1tcInRpdGxlXCJdKSJ9"
 width="100%"
></iframe>

Predict the output before running it. Then extend the exercise: add genre fields and use `groupby` (after sorting) to group the combined catalog by decade (1940s, 1950s, 1960s, 1980s). You will need a key function that computes `year // 10 * 10`.

## Conclusion

`itertools` provides a toolkit of lazy, composable building blocks: `islice` for slicing generators, `chain` for merging multiple iterables, `groupby` for clustering sorted sequences, `zip_longest` for pairing unequal lengths, and `tee` for cloning iterators. All are lazy and memory-efficient by design. The final lesson of this unit synthesizes everything into a practical guideline: when is a generator the right tool, and when should you use a list instead?
