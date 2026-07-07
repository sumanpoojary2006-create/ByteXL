## Introduction

Naveen has a list of pending dues and three quick jobs to do with it before the meeting: apply a 5 percent late fee to every single amount, pull out only the dues that are still above 200 after that fee, and finally collapse the whole list down into one grand total. Each job takes a list in and produces something new out, by applying the same small rule to every item. You already know one way to do this, the list comprehension from two units ago, but Python also offers three classic, purpose-built tools that do exactly these three jobs by name, and they pair naturally with the lambdas from the last lesson.

`map`, `filter`, and `reduce` each take a function and a sequence, and each does one very specific thing with that pairing.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/07_map_filter_reduce_pipeline.png)

## map: Apply a Function to Every Item

`map` takes a function and a sequence, and applies that function to every item, handing back a `map` object that you usually wrap in `list()` to actually see.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-8-functions-07-map-filter-and-reduce-001-2bf5f0de6f.html"
 width="100%"
></iframe>

Every single amount passed through the same lambda, each multiplied by 1.05 on its own. This is the exact same outcome a list comprehension would give you.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-8-functions-07-map-filter-and-reduce-002-a625cbc8cb.html"
 width="100%"
></iframe>

Both lines do the same job. `map` is simply the older, function-first way of saying it, and you will meet it often enough in other people's code that recognising it matters, even if a comprehension often reads more naturally to a Python programmer today.

## filter: Keep Only What Passes a Test

`filter` takes a function that returns `True` or `False`, and keeps only the items for which it returns `True`.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-8-functions-07-map-filter-and-reduce-003-e220f60428.html"
 width="100%"
></iframe>

Every amount is tested by the lambda, and only the ones that pass survive into the result. Once again, a list comprehension can say the same thing.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-8-functions-07-map-filter-and-reduce-004-0a6527f0ed.html"
 width="100%"
></iframe>

## reduce: Collapse a Sequence Into One Value

`reduce` is different from the other two: instead of producing a new sequence, it collapses an entire sequence down into a single value, by repeatedly combining items two at a time. Unlike `map` and `filter`, it is not built in directly; it lives in the `functools` module, so it needs an import.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-8-functions-07-map-filter-and-reduce-005-b0291d8f24.html"
 width="100%"
></iframe>

Read the lambda as "take the running total so far and the next amount, and combine them into a new running total." `reduce` starts with the first two items, combines them, then keeps combining the result with the next item, and the next, until only one value is left.

## Most of the Time, sum() Already Does This

For the specific, extremely common case of adding everything up, Python's built-in `sum()` does exactly what the `reduce` example above did, with far less ceremony.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-8-functions-07-map-filter-and-reduce-006-f45c0452c4.html"
 width="100%"
></iframe>

`reduce` is genuinely useful for combining logic, like multiplying everything together, or finding the longest string, that does not have its own dedicated built-in function. For plain addition, `sum()` is simpler and is what experienced Python programmers actually reach for.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/07_map_filter_reduce_vs_loop.png)


## map, filter, and reduce at a Glance

| Tool | Job | Often Replaced By |
|---|---|---|
| `map(func, seq)` | Transform every item | `[func(x) for x in seq]` |
| `filter(func, seq)` | Keep items passing a test | `[x for x in seq if func(x)]` |
| `reduce(func, seq)` | Collapse to one value | `sum()`, `max()`, or a plain loop, depending on the job |

Knowing all three matters for reading other people's code and for understanding the ideas underneath comprehensions, even where a comprehension is the more natural choice for new code.

## Your Turn: The Full Pipeline

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-8-functions-07-map-filter-and-reduce-007-973c63d906.html"
 width="100%"
></iframe>

Run all three stages in sequence and notice each tool did exactly one job, handing its result to the next.

## Conclusion

`map` transforms every item in a sequence, `filter` keeps only the items that pass a test, and `reduce`, imported from `functools`, collapses a whole sequence down to one value by combining items two at a time, though `sum()`, `max()`, and `min()` already cover the most common reductions directly. List comprehensions often express the same ideas more readably in modern Python, but recognising these three by name is essential for reading real code. With several ways now to process a sequence in one line, the next lesson tours a handful of built-in functions worth knowing by heart.
