## Introduction

Kiran is looking at the timing problem from a new angle. She wants a function that takes *another function* as input, runs it, measures how long it takes, and returns the result. She has seen `map()` and `sorted()` take functions as arguments, so she knows Python supports this. Now she needs to write it herself.

This lesson bridges the gap between "functions can be passed around" and "functions can be wrapped." By the end, Kiran will have written something that looks almost exactly like a decorator, without yet using the `@` syntax.

![A timing function receiving an original function and a clock, wrapping both together, and returning the elapsed time alongside the result](images/02_functions_as_arguments_return_values.png)

## Higher-Order Functions

A **higher-order function** is any function that takes a function as an argument or returns a function as a result. Python has many built-in ones:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2Z1bmN0aW9uc19hc19hcmd1bWVudHNfYW5kX3JldHVybl92YWx1ZXMgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6ImJvb2tzID0gW1xuICAgIHtcInRpdGxlXCI6IFwiRHVuZVwiLCBcInllYXJcIjogMTk2NX0sXG4gICAge1widGl0bGVcIjogXCJGb3VuZGF0aW9uXCIsIFwieWVhclwiOiAxOTUxfSxcbiAgICB7XCJ0aXRsZVwiOiBcIk5ldXJvbWFuY2VyXCIsIFwieWVhclwiOiAxOTg0fSxcbl1cblxuIyBzb3J0ZWQoKSB0YWtlcyBhIGtleSBmdW5jdGlvblxuYnlfeWVhciA9IHNvcnRlZChib29rcywga2V5PWxhbWJkYSBiOiBiW1wieWVhclwiXSlcbnByaW50KGJ5X3llYXJbMF1bXCJ0aXRsZVwiXSkgICAjIEZvdW5kYXRpb24gLS0gb2xkZXN0IGZpcnN0XG5cbiMgZmlsdGVyKCkgdGFrZXMgYSBwcmVkaWNhdGUgZnVuY3Rpb25cbnJlY2VudCA9IGxpc3QoZmlsdGVyKGxhbWJkYSBiOiBiW1wieWVhclwiXSA-IDE5NjAsIGJvb2tzKSlcbnByaW50KFtiW1widGl0bGVcIl0gZm9yIGIgaW4gcmVjZW50XSkgICAjIFsnRHVuZScsICdOZXVyb21hbmNlciddIn0"
 width="100%"
></iframe>

Writing your own higher-order function works the same way: accept a function parameter, call it inside, and optionally return a function as the result.

## Accepting a Function, Running It, Returning the Result

The simplest higher-order function Kiran could write for timing:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2Z1bmN0aW9uc19hc19hcmd1bWVudHNfYW5kX3JldHVybl92YWx1ZXMgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6ImltcG9ydCB0aW1lXG5cbmRlZiB0aW1lZChmbiwgKmFyZ3MsICoqa3dhcmdzKTpcbiAgICBzdGFydCA9IHRpbWUudGltZSgpXG4gICAgcmVzdWx0ID0gZm4oKmFyZ3MsICoqa3dhcmdzKVxuICAgIGVsYXBzZWQgPSB0aW1lLnRpbWUoKSAtIHN0YXJ0XG4gICAgcHJpbnQoZlwie2ZuLl9fbmFtZV9ffSB0b29rIHtlbGFwc2VkOi40Zn1zXCIpXG4gICAgcmV0dXJuIHJlc3VsdFxuXG5kZWYgbG9hZF9jYXRhbG9nKHNpemUpOlxuICAgIHRpbWUuc2xlZXAoMC4xKSAgICMgc2ltdWxhdGUgd29ya1xuICAgIHJldHVybiBsaXN0KHJhbmdlKHNpemUpKVxuXG5yZXN1bHQgPSB0aW1lZChsb2FkX2NhdGFsb2csIDEwMClcbiMgbG9hZF9jYXRhbG9nIHRvb2sgMC4xMDAxcyJ9"
 width="100%"
></iframe>

`timed` accepts the function `fn` and any arguments for it, calls `fn(*args, **kwargs)`, measures the wall-clock time, and returns the function's result. This works, but the calling syntax changes: callers must write `timed(load_catalog, 100)` instead of `load_catalog(100)`. The timing logic is now external to the function, but it has not been seamlessly added.

## Returning a New Function: The Wrapper Pattern

A more powerful pattern: instead of calling the function inside `timed`, return a new function that *itself* calls the original. The result is a new function that behaves like the original but also includes timing.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2Z1bmN0aW9uc19hc19hcmd1bWVudHNfYW5kX3JldHVybl92YWx1ZXMgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6ImltcG9ydCB0aW1lXG5cbmRlZiBhZGRfdGltaW5nKGZuKTpcbiAgICBkZWYgd3JhcHBlcigqYXJncywgKiprd2FyZ3MpOlxuICAgICAgICBzdGFydCA9IHRpbWUudGltZSgpXG4gICAgICAgIHJlc3VsdCA9IGZuKCphcmdzLCAqKmt3YXJncylcbiAgICAgICAgZWxhcHNlZCA9IHRpbWUudGltZSgpIC0gc3RhcnRcbiAgICAgICAgcHJpbnQoZlwie2ZuLl9fbmFtZV9ffSB0b29rIHtlbGFwc2VkOi40Zn1zXCIpXG4gICAgICAgIHJldHVybiByZXN1bHRcbiAgICByZXR1cm4gd3JhcHBlclxuXG5kZWYgbG9hZF9jYXRhbG9nKHNpemUpOlxuICAgIHRpbWUuc2xlZXAoMC4xKVxuICAgIHJldHVybiBsaXN0KHJhbmdlKHNpemUpKVxuXG50aW1lZF9sb2FkID0gYWRkX3RpbWluZyhsb2FkX2NhdGFsb2cpICAgIyB0aW1lZF9sb2FkIElTIGEgZnVuY3Rpb25cbnJlc3VsdCA9IHRpbWVkX2xvYWQoMTAwKSAgICAgICAgICAgICAgICAjIGNhbGxlZCBqdXN0IGxpa2UgbG9hZF9jYXRhbG9nXG4jIGxvYWRfY2F0YWxvZyB0b29rIDAuMTAwMXMifQ"
 width="100%"
></iframe>

`add_timing` takes the original function, creates a `wrapper` closure that captures `fn`, and returns the wrapper. Callers can now call `timed_load(100)` exactly as they would call `load_catalog(100)`. The timing is invisible.

## Replacing the Original With the Wrapped Version

The final step is to replace the original name with the wrapped version, so every call to `load_catalog` automatically includes timing:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2Z1bmN0aW9uc19hc19hcmd1bWVudHNfYW5kX3JldHVybl92YWx1ZXMgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6ImxvYWRfY2F0YWxvZyA9IGFkZF90aW1pbmcobG9hZF9jYXRhbG9nKSAgICMgcmVwbGFjZSB0aGUgb3JpZ2luYWxcbnJlc3VsdCA9IGxvYWRfY2F0YWxvZygxMDApICAgICAgICAgICAgICAgICMgbm93IGluY2x1ZGVzIHRpbWluZyBhdXRvbWF0aWNhbGx5XG4jIGxvYWRfY2F0YWxvZyB0b29rIDAuMTAwMXMifQ"
 width="100%"
></iframe>

This single line, `load_catalog = add_timing(load_catalog)`, is exactly what the `@add_timing` syntax does. The decorator syntax introduced in the next lesson is purely a shorthand for this pattern.

## *args and **kwargs: Why They Matter in Wrappers

The `wrapper` function uses `*args` and `**kwargs` to accept any arguments without knowing the signature of the wrapped function. This makes the wrapper generic: it works with functions that take no arguments, positional arguments, keyword arguments, or any combination.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2Z1bmN0aW9uc19hc19hcmd1bWVudHNfYW5kX3JldHVybl92YWx1ZXMgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6ImRlZiBhZGRfdGltaW5nKGZuKTpcbiAgICBkZWYgd3JhcHBlcigqYXJncywgKiprd2FyZ3MpOiAgICMgYWNjZXB0cyBhbnl0aGluZ1xuICAgICAgICBzdGFydCA9IHRpbWUudGltZSgpXG4gICAgICAgIHJlc3VsdCA9IGZuKCphcmdzLCAqKmt3YXJncykgICMgcGFzc2VzIGV2ZXJ5dGhpbmcgdGhyb3VnaFxuICAgICAgICBlbGFwc2VkID0gdGltZS50aW1lKCkgLSBzdGFydFxuICAgICAgICBwcmludChmXCJ7Zm4uX19uYW1lX199IHRvb2sge2VsYXBzZWQ6LjRmfXNcIilcbiAgICAgICAgcmV0dXJuIHJlc3VsdFxuICAgIHJldHVybiB3cmFwcGVyIn0"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2Z1bmN0aW9uc19hc19hcmd1bWVudHNfYW5kX3JldHVybl92YWx1ZXMgY29kZSA2IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA2LnB5IiwiY29kZSI6ImRlZiBhZGRfbG9nZ2luZyhmbik6XG4gICAgZGVmIHdyYXBwZXIoKmFyZ3MsICoqa3dhcmdzKTpcbiAgICAgICAgcHJpbnQoZlwiQ2FsbGluZyB7Zm4uX19uYW1lX199IHdpdGggYXJncz17YXJnc30ga3dhcmdzPXtrd2FyZ3N9XCIpXG4gICAgICAgIHJlc3VsdCA9IGZuKCphcmdzLCAqKmt3YXJncylcbiAgICAgICAgcHJpbnQoZlwie2ZuLl9fbmFtZV9ffSByZXR1cm5lZCB7cmVzdWx0IXJ9XCIpXG4gICAgICAgIHJldHVybiByZXN1bHRcbiAgICByZXR1cm4gd3JhcHBlclxuXG5kZWYgY2FsY3VsYXRlX2ZpbmUoZGF5c19vdmVyZHVlLCBkYWlseV9yYXRlPTAuNTApOlxuICAgIHJldHVybiBkYXlzX292ZXJkdWUgKiBkYWlseV9yYXRlXG5cbmxvZ2dlZF9maW5lID0gYWRkX2xvZ2dpbmcoY2FsY3VsYXRlX2ZpbmUpXG5sb2dnZWRfZmluZSg1KVxubG9nZ2VkX2ZpbmUoMTAsIGRhaWx5X3JhdGU9MC43NSkifQ"
 width="100%"
></iframe>

Run this and read the output carefully. Then replace `logged_fine = add_logging(calculate_fine)` with `calculate_fine = add_logging(calculate_fine)` to permanently apply the wrapper, and confirm that `calculate_fine(5)` now logs automatically.

## Conclusion

Higher-order functions accept or return other functions. A wrapper is an inner function that calls the original, adding behavior before or after. `*args` and `**kwargs` make wrappers work with any function signature. Replacing a function with its wrapped version, `fn = add_wrapper(fn)`, is the exact pattern the `@decorator` syntax automates. The next lesson introduces that syntax.
