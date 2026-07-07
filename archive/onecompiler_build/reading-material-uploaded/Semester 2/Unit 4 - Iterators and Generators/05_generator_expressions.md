## Introduction

Leila is now comfortable writing generator functions. But she notices that many of the generators she writes are simple: filter a collection, or transform each item with a single expression. For these cases, writing a full `def` with a `yield` feels like using a sledgehammer to crack a nut. She asks Nadia if there is a shorter syntax.

There is. Generator expressions are to generators what list comprehensions are to lists: a compact, one-line way to describe a lazy sequence. The only visual difference from a list comprehension is the brackets: parentheses instead of square brackets.

![](images/05_generator_expressions.png)

## Generator Expression Syntax

A generator expression has the same structure as a list comprehension, but uses parentheses:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-05-generator-expressions-001-f852f44546.html"
 width="100%"
></iframe>

The generator expression does not compute anything when it is created. It is a promise to compute values as they are requested.

## Using a Generator Expression

Any place that accepts an iterator accepts a generator expression:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-05-generator-expressions-002-8a477a2f98.html"
 width="100%"
></iframe>

When a generator expression is the only argument to a function call, the outer parentheses of the call serve double duty and you do not need an extra pair: `sum(x ** 2 for x in range(5))` not `sum((x ** 2 for x in range(5)))`.

## Memory: The Key Difference

The difference between a list comprehension and a generator expression is not syntax; it is memory usage and when computation happens.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-05-generator-expressions-003-a6c7811c58.html"
 width="100%"
></iframe>

The generator object contains only the code to produce the next value and the current state, not the values themselves. For Leila's million-record catalog, this is the difference between running fine and crashing.

## Chaining Generator Expressions

Generator expressions can be chained: one feeds another, creating a lazy pipeline where data flows through transformation and filtering steps one item at a time.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-05-generator-expressions-004-ca3ac02eb5.html"
 width="100%"
></iframe>

Each generator in the chain produces items only when the next one requests them. Processing happens left to right through all three filters for one item before the next item is even looked at. No intermediate lists are created.

## When to Choose a Generator Expression vs. a List Comprehension

Use a **list comprehension** when you need to iterate over the result more than once, need to know the length, or need to index into specific positions. Use a **generator expression** when you process results once in a pipeline, the sequence could be very large, or you pass it directly to a function like `sum()`, `max()`, or `any()`.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-05-generator-expressions-005-c1c0d7f0c3.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-4-iterators-and-generators-05-generator-expressions-006-2572723b5f.html"
 width="100%"
></iframe>

Without building any intermediate lists, use generator expressions to:
1. Print all approved titles with `for`.
2. Compute the total cost of approved books with `sum()`.
3. Find the most expensive approved book with `max()` using `max(..., key=lambda r: r["price"])`.

Each of these should be a single expression with a generator inside.

## Conclusion

Generator expressions use parentheses instead of square brackets to describe lazy sequences that compute values on demand. They are memory-efficient for large data, chainable into pipelines, and pass directly to built-in functions like `sum()` and `max()`. The trade-off: a generator is exhausted after one pass and does not support indexing or length queries. The next lesson looks at why lazy evaluation matters beyond convenience: the memory and time implications for large datasets.
