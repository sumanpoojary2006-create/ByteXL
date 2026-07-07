## Introduction

Leila is now comfortable writing generator functions. But she notices that many of the generators she writes are simple: filter a collection, or transform each item with a single expression. For these cases, writing a full `def` with a `yield` feels like using a sledgehammer to crack a nut. She asks Nadia if there is a shorter syntax.

There is. Generator expressions are to generators what list comprehensions are to lists: a compact, one-line way to describe a lazy sequence. The only visual difference from a list comprehension is the brackets: parentheses instead of square brackets.

![](images/05_generator_expressions.png)

## Generator Expression Syntax

A generator expression has the same structure as a list comprehension, but uses parentheses:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2dlbmVyYXRvcl9leHByZXNzaW9ucyBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoiIyBMaXN0IGNvbXByZWhlbnNpb246IGV2YWx1YXRlcyBldmVyeXRoaW5nIE5PVywgc3RvcmVzIGEgbGlzdFxuc3F1YXJlc19saXN0ID0gW3ggKiogMiBmb3IgeCBpbiByYW5nZSgxMCldXG5wcmludCh0eXBlKHNxdWFyZXNfbGlzdCkpICAgIyA8Y2xhc3MgJ2xpc3QnPlxucHJpbnQoc3F1YXJlc19saXN0KSAgICAgICAgICMgWzAsIDEsIDQsIDksIDE2LCAyNSwgMzYsIDQ5LCA2NCwgODFdXG5cbiMgR2VuZXJhdG9yIGV4cHJlc3Npb246IGV2YWx1YXRlcyBsYXppbHksIG9uZSBpdGVtIGF0IGEgdGltZVxuc3F1YXJlc19nZW4gPSAoeCAqKiAyIGZvciB4IGluIHJhbmdlKDEwKSlcbnByaW50KHR5cGUoc3F1YXJlc19nZW4pKSAgICAjIDxjbGFzcyAnZ2VuZXJhdG9yJz5cbnByaW50KHNxdWFyZXNfZ2VuKSAgICAgICAgICAjIDxnZW5lcmF0b3Igb2JqZWN0IDxnZW5leHByPiBhdCAweC4uLj4ifQ"
 width="100%"
></iframe>

The generator expression does not compute anything when it is created. It is a promise to compute values as they are requested.

## Using a Generator Expression

Any place that accepts an iterator accepts a generator expression:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2dlbmVyYXRvcl9leHByZXNzaW9ucyBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoiIyBJbiBhIGZvciBsb29wOlxuZm9yIHNxIGluICh4ICoqIDIgZm9yIHggaW4gcmFuZ2UoNSkpOlxuICAgIHByaW50KHNxKSAgICMgMCwgMSwgNCwgOSwgMTZcblxuIyBQYXNzZWQgZGlyZWN0bHkgdG8gYSBmdW5jdGlvbjpcbnRvdGFsID0gc3VtKHggKiogMiBmb3IgeCBpbiByYW5nZSg1KSkgICAjIHBhcmVudGhlc2VzIGFyb3VuZCB0aGUgd2hvbGUgc3VtIGNhbGxcbnByaW50KHRvdGFsKSAgICMgMzBcblxuIyBGaWx0ZXJlZDpcbmFwcHJvdmVkX3RpdGxlcyA9IChyW1widGl0bGVcIl0gZm9yIHIgaW4gcmVjb3JkcyBpZiByW1wiYXBwcm92ZWRcIl0pXG5mb3IgdGl0bGUgaW4gYXBwcm92ZWRfdGl0bGVzOlxuICAgIHByaW50KHRpdGxlKSJ9"
 width="100%"
></iframe>

When a generator expression is the only argument to a function call, the outer parentheses of the call serve double duty and you do not need an extra pair: `sum(x ** 2 for x in range(5))` not `sum((x ** 2 for x in range(5)))`.

## Memory: The Key Difference

The difference between a list comprehension and a generator expression is not syntax; it is memory usage and when computation happens.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2dlbmVyYXRvcl9leHByZXNzaW9ucyBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoiaW1wb3J0IHN5c1xuXG4jIExpc3QgY29tcHJlaGVuc2lvbjogYWxsIDEgbWlsbGlvbiBudW1iZXJzIGluIG1lbW9yeSBhdCBvbmNlXG5iaWdfbGlzdCA9IFt4IGZvciB4IGluIHJhbmdlKDFfMDAwXzAwMCldXG5wcmludChzeXMuZ2V0c2l6ZW9mKGJpZ19saXN0KSkgICAjIH44IE1CXG5cbiMgR2VuZXJhdG9yIGV4cHJlc3Npb246IHRpbnkgb2JqZWN0IHJlZ2FyZGxlc3Mgb2YgcmFuZ2VcbmJpZ19nZW4gPSAoeCBmb3IgeCBpbiByYW5nZSgxXzAwMF8wMDApKVxucHJpbnQoc3lzLmdldHNpemVvZihiaWdfZ2VuKSkgICAgIyB-MTEyIGJ5dGVzIn0"
 width="100%"
></iframe>

The generator object contains only the code to produce the next value and the current state, not the values themselves. For Leila's million-record catalog, this is the difference between running fine and crashing.

## Chaining Generator Expressions

Generator expressions can be chained: one feeds another, creating a lazy pipeline where data flows through transformation and filtering steps one item at a time.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2dlbmVyYXRvcl9leHByZXNzaW9ucyBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoicmVjb3JkcyA9IFtcbiAgICB7XCJ0aXRsZVwiOiBcIkR1bmVcIiwgXCJjb3BpZXNcIjogMywgXCJhcHByb3ZlZFwiOiBUcnVlfSxcbiAgICB7XCJ0aXRsZVwiOiBcIlJvdWdoIERyYWZ0XCIsIFwiY29waWVzXCI6IDAsIFwiYXBwcm92ZWRcIjogRmFsc2V9LFxuICAgIHtcInRpdGxlXCI6IFwiRm91bmRhdGlvblwiLCBcImNvcGllc1wiOiAxLCBcImFwcHJvdmVkXCI6IFRydWV9LFxuICAgIHtcInRpdGxlXCI6IFwiT3V0IG9mIFN0b2NrXCIsIFwiY29waWVzXCI6IDAsIFwiYXBwcm92ZWRcIjogVHJ1ZX0sXG5dXG5cbiMgUGlwZWxpbmU6IGFwcHJvdmVkLCB0aGVuIGF2YWlsYWJsZSAoY29waWVzID4gMCksIHRoZW4gZXh0cmFjdCB0aXRsZVxuYXBwcm92ZWQgPSAociBmb3IgciBpbiByZWNvcmRzIGlmIHJbXCJhcHByb3ZlZFwiXSlcbmF2YWlsYWJsZSA9IChyIGZvciByIGluIGFwcHJvdmVkIGlmIHJbXCJjb3BpZXNcIl0gPiAwKVxudGl0bGVzID0gKHJbXCJ0aXRsZVwiXSBmb3IgciBpbiBhdmFpbGFibGUpXG5cbmZvciB0aXRsZSBpbiB0aXRsZXM6XG4gICAgcHJpbnQodGl0bGUpXG4jIER1bmVcbiMgRm91bmRhdGlvbiJ9"
 width="100%"
></iframe>

Each generator in the chain produces items only when the next one requests them. Processing happens left to right through all three filters for one item before the next item is even looked at. No intermediate lists are created.

## When to Choose a Generator Expression vs. a List Comprehension

Use a **list comprehension** when you need to iterate over the result more than once, need to know the length, or need to index into specific positions. Use a **generator expression** when you process results once in a pipeline, the sequence could be very large, or you pass it directly to a function like `sum()`, `max()`, or `any()`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2dlbmVyYXRvcl9leHByZXNzaW9ucyBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoiIyBVc2UgYSBsaXN0IGlmIHlvdSBuZWVkIHRvIHJldXNlIHRoZSByZXN1bHQ6XG5hcHByb3ZlZCA9IFtyIGZvciByIGluIHJlY29yZHMgaWYgcltcImFwcHJvdmVkXCJdXVxucHJpbnQobGVuKGFwcHJvdmVkKSkgICAgICAgICAgIyBuZWVkcyBhIGxpc3RcbnByaW50KGFwcHJvdmVkWzBdKSAgICAgICAgICAgICMgaW5kZXhpbmcgbmVlZHMgYSBsaXN0XG5cbiMgVXNlIGEgZ2VuZXJhdG9yIGlmIHlvdSBjb25zdW1lIGl0IG9uY2U6XG5wcmludChzdW0ocltcImNvcGllc1wiXSBmb3IgciBpbiByZWNvcmRzIGlmIHJbXCJhcHByb3ZlZFwiXSkpICAgIyBubyBsaXN0IG5lZWRlZCJ9"
 width="100%"
></iframe>

## Generator Expressions at a Glance

| Feature | List comprehension `[...]` | Generator expression `(...)` |
|---|---|---|
| Evaluated | Immediately, all at once | Lazily, one item at a time |
| Memory | Proportional to the output size | Constant (just the generator state) |
| Reusable | Yes | No (exhausted after one pass) |
| Supports `len()` | Yes | No |
| Best for | Multiple iterations, indexing | Single-pass processing, large data |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2dlbmVyYXRvcl9leHByZXNzaW9ucyBjb2RlIDYiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDYucHkiLCJjb2RlIjoicmVjb3JkcyA9IFtcbiAgICB7XCJ0aXRsZVwiOiBcIkR1bmVcIiwgXCJwcmljZVwiOiAxNS45OSwgXCJhcHByb3ZlZFwiOiBUcnVlfSxcbiAgICB7XCJ0aXRsZVwiOiBcIkRyYWZ0XCIsIFwicHJpY2VcIjogOS45OSwgXCJhcHByb3ZlZFwiOiBGYWxzZX0sXG4gICAge1widGl0bGVcIjogXCJGb3VuZGF0aW9uXCIsIFwicHJpY2VcIjogMTIuNTAsIFwiYXBwcm92ZWRcIjogVHJ1ZX0sXG4gICAge1widGl0bGVcIjogXCJTaG9ndW5cIiwgXCJwcmljZVwiOiAxOC4wMCwgXCJhcHByb3ZlZFwiOiBUcnVlfSxcbl0ifQ"
 width="100%"
></iframe>

Without building any intermediate lists, use generator expressions to:
1. Print all approved titles with `for`.
2. Compute the total cost of approved books with `sum()`.
3. Find the most expensive approved book with `max()` using `max(..., key=lambda r: r["price"])`.

Each of these should be a single expression with a generator inside.

## Conclusion

Generator expressions use parentheses instead of square brackets to describe lazy sequences that compute values on demand. They are memory-efficient for large data, chainable into pipelines, and pass directly to built-in functions like `sum()` and `max()`. The trade-off: a generator is exhausted after one pass and does not support indexing or length queries. The next lesson looks at why lazy evaluation matters beyond convenience: the memory and time implications for large datasets.
