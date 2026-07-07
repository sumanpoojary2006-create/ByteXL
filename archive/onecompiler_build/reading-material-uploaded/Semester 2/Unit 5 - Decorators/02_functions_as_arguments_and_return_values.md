## Introduction

Kiran is looking at the timing problem from a new angle. She wants a function that takes *another function* as input, runs it, measures how long it takes, and returns the result. She has seen `map()` and `sorted()` take functions as arguments, so she knows Python supports this. Now she needs to write it herself.

This lesson bridges the gap between "functions can be passed around" and "functions can be wrapped." By the end, Kiran will have written something that looks almost exactly like a decorator, without yet using the `@` syntax.

![A timing function receiving an original function and a clock, wrapping both together, and returning the elapsed time alongside the result](images/02_functions_as_arguments_return_values.png)

## Higher-Order Functions

A **higher-order function** is any function that takes a function as an argument or returns a function as a result. Python has many built-in ones:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-5-decorators-02-functions-as-arguments-and-return-values-001-82d93db399.html"
 width="100%"
></iframe>

Writing your own higher-order function works the same way: accept a function parameter, call it inside, and optionally return a function as the result.

## Accepting a Function, Running It, Returning the Result

The simplest higher-order function Kiran could write for timing:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-5-decorators-02-functions-as-arguments-and-return-values-002-18ff4c0cf2.html"
 width="100%"
></iframe>

`timed` accepts the function `fn` and any arguments for it, calls `fn(*args, **kwargs)`, measures the wall-clock time, and returns the function's result. This works, but the calling syntax changes: callers must write `timed(load_catalog, 100)` instead of `load_catalog(100)`. The timing logic is now external to the function, but it has not been seamlessly added.

## Returning a New Function: The Wrapper Pattern

A more powerful pattern: instead of calling the function inside `timed`, return a new function that *itself* calls the original. The result is a new function that behaves like the original but also includes timing.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-5-decorators-02-functions-as-arguments-and-return-values-003-47e65de28c.html"
 width="100%"
></iframe>

`add_timing` takes the original function, creates a `wrapper` closure that captures `fn`, and returns the wrapper. Callers can now call `timed_load(100)` exactly as they would call `load_catalog(100)`. The timing is invisible.

## Replacing the Original With the Wrapped Version

The final step is to replace the original name with the wrapped version, so every call to `load_catalog` automatically includes timing:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-5-decorators-02-functions-as-arguments-and-return-values-004-ba04087acc.html"
 width="100%"
></iframe>

This single line, `load_catalog = add_timing(load_catalog)`, is exactly what the `@add_timing` syntax does. The decorator syntax introduced in the next lesson is purely a shorthand for this pattern.

## *args and **kwargs: Why They Matter in Wrappers

The `wrapper` function uses `*args` and `**kwargs` to accept any arguments without knowing the signature of the wrapped function. This makes the wrapper generic: it works with functions that take no arguments, positional arguments, keyword arguments, or any combination.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-5-decorators-02-functions-as-arguments-and-return-values-005-c71a81d25e.html"
 width="100%"
></iframe>

Without `*args` and `**kwargs`, you would have to write a separate timing function for every function signature. With them, one wrapper works universally.

## Functions as Arguments and Return Values at a Glance

| Pattern | What it does |
|---|---|
| Higher-order function | Takes a function as argument or returns one |
| Wrapper | An inner function that calls `fn(*args, **kwargs)` |
| `*args, **kwargs` | Makes a wrapper accept any function signature |
| Replacing the original | `fn = add_behavior(fn)` applies the wrapper permanently |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-5-decorators-02-functions-as-arguments-and-return-values-006-df6462e9b4.html"
 width="100%"
></iframe>

Run this and read the output carefully. Then replace `logged_fine = add_logging(calculate_fine)` with `calculate_fine = add_logging(calculate_fine)` to permanently apply the wrapper, and confirm that `calculate_fine(5)` now logs automatically.

## Conclusion

Higher-order functions accept or return other functions. A wrapper is an inner function that calls the original, adding behavior before or after. `*args` and `**kwargs` make wrappers work with any function signature. Replacing a function with its wrapped version, `fn = add_wrapper(fn)`, is the exact pattern the `@decorator` syntax automates. The next lesson introduces that syntax.
