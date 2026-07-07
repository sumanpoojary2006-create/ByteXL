## Introduction

Kiran's timing decorator is working well. But now she wants a retry decorator: one that runs a function again if it raises an exception, up to a configurable maximum number of attempts. The number of attempts should be a parameter. She wants to write `@retry(max_attempts=3)` above a function, not a separate decorator for every retry count.

This requires a slightly different pattern: instead of a two-level function (decorator wraps function), she needs three levels: a function that takes the arguments, returns a decorator, which in turn wraps the function.

![Three nested levels: outer factory receives arguments, middle decorator receives the function, inner wrapper calls the function and handles retries](images/04_decorators_with_arguments.png)

## The Three-Level Pattern

A decorator with arguments needs three levels of function nesting:

1. The **decorator factory** accepts the arguments (like `max_attempts=3`) and returns a decorator.
2. The **decorator** accepts the function and returns a wrapper.
3. The **wrapper** contains the actual behavior.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2RlY29yYXRvcnNfd2l0aF9hcmd1bWVudHMgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6ImRlZiByZXRyeShtYXhfYXR0ZW1wdHM9Myk6ICAgICAgICAgICMgbGV2ZWwgMTogZmFjdG9yeVxuICAgIGRlZiBkZWNvcmF0b3IoZm4pOiAgICAgICAgICAgICAgIyBsZXZlbCAyOiBkZWNvcmF0b3JcbiAgICAgICAgZGVmIHdyYXBwZXIoKmFyZ3MsICoqa3dhcmdzKTogICMgbGV2ZWwgMzogd3JhcHBlclxuICAgICAgICAgICAgbGFzdF9lcnJvciA9IE5vbmVcbiAgICAgICAgICAgIGZvciBhdHRlbXB0IGluIHJhbmdlKDEsIG1heF9hdHRlbXB0cyArIDEpOlxuICAgICAgICAgICAgICAgIHRyeTpcbiAgICAgICAgICAgICAgICAgICAgcmV0dXJuIGZuKCphcmdzLCAqKmt3YXJncylcbiAgICAgICAgICAgICAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGVycm9yOlxuICAgICAgICAgICAgICAgICAgICBsYXN0X2Vycm9yID0gZXJyb3JcbiAgICAgICAgICAgICAgICAgICAgcHJpbnQoZlwiQXR0ZW1wdCB7YXR0ZW1wdH0gZmFpbGVkOiB7ZXJyb3J9XCIpXG4gICAgICAgICAgICByYWlzZSBsYXN0X2Vycm9yXG4gICAgICAgIHJldHVybiB3cmFwcGVyXG4gICAgcmV0dXJuIGRlY29yYXRvciJ9"
 width="100%"
></iframe>

When Python sees `@retry(max_attempts=3)`, it evaluates `retry(max_attempts=3)` first, which returns `decorator`. Then it applies `decorator` to the function. The result is exactly the same as a plain `@decorator`, just with the arguments captured in a closure at the first level.

## Applying a Decorator With Arguments

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2RlY29yYXRvcnNfd2l0aF9hcmd1bWVudHMgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6IkByZXRyeShtYXhfYXR0ZW1wdHM9MylcbmRlZiBmZXRjaF9ib29rKGlzYm4pOlxuICAgIGltcG9ydCByYW5kb21cbiAgICBpZiByYW5kb20ucmFuZG9tKCkgPCAwLjc6ICAgIyBmYWlscyA3MCUgb2YgdGhlIHRpbWVcbiAgICAgICAgcmFpc2UgQ29ubmVjdGlvbkVycm9yKFwiTmV0d29yayB1bnJlYWNoYWJsZVwiKVxuICAgIHJldHVybiB7XCJpc2JuXCI6IGlzYm4sIFwidGl0bGVcIjogXCJEdW5lXCJ9XG5cbnRyeTpcbiAgICBib29rID0gZmV0Y2hfYm9vayhcIjk3OC0wNDQxMDEzNTkzXCIpXG4gICAgcHJpbnQoYm9vaylcbmV4Y2VwdCBDb25uZWN0aW9uRXJyb3I6XG4gICAgcHJpbnQoXCJBbGwgYXR0ZW1wdHMgZmFpbGVkXCIpIn0"
 width="100%"
></iframe>

The function is tried up to three times. Each failure is logged. On success, the result is returned normally.

## Common Mistake: Calling vs. Not Calling the Decorator Factory

The easiest way to confuse yourself with parameterized decorators is accidentally writing `@retry` instead of `@retry()`. Without the call, Python passes the function to `retry` directly as the first argument, but `retry` expects `max_attempts`, not a function.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2RlY29yYXRvcnNfd2l0aF9hcmd1bWVudHMgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6IkByZXRyeSAgICAgICAgICAjIFdST05HOiBwYXNzZXMgdGhlIGZ1bmN0aW9uIHRvIHJldHJ5IGFzIG1heF9hdHRlbXB0c1xuZGVmIGZldGNoX2Jvb2soaXNibik6XG4gICAgcGFzc1xuIyBUeXBlRXJyb3I6ICdmdW5jdGlvbicgb2JqZWN0IGNhbm5vdCBiZSBpbnRlcnByZXRlZCBhcyBhbiBpbnRlZ2VyXG5cbkByZXRyeSgpICAgICAgICAjIENPUlJFQ1Q6IHJldHJ5KCkgcmV0dXJucyB0aGUgZGVjb3JhdG9yLCB0aGVuIHRoZSBkZWNvcmF0b3Igd3JhcHMgZm5cbmRlZiBmZXRjaF9ib29rKGlzYm4pOlxuICAgIHBhc3MifQ"
 width="100%"
></iframe>

If you want `@retry` to work *without* parentheses (using a default retry count), you need to detect whether the first argument is a function and handle both cases. This pattern exists but adds complexity; for clarity, always require parentheses with parameterized decorators.

## A Rate-Limiter Decorator With Arguments

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2RlY29yYXRvcnNfd2l0aF9hcmd1bWVudHMgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6ImltcG9ydCB0aW1lXG5cbmRlZiByYXRlX2xpbWl0KGNhbGxzX3Blcl9zZWNvbmQpOlxuICAgIG1pbl9pbnRlcnZhbCA9IDEuMCAvIGNhbGxzX3Blcl9zZWNvbmRcbiAgICBsYXN0X2NhbGxlZCA9IFswLjBdICAgIyBsaXN0IHRvIGFsbG93IG11dGF0aW9uIGluc2lkZSB0aGUgY2xvc3VyZVxuXG4gICAgZGVmIGRlY29yYXRvcihmbik6XG4gICAgICAgIGRlZiB3cmFwcGVyKCphcmdzLCAqKmt3YXJncyk6XG4gICAgICAgICAgICBlbGFwc2VkID0gdGltZS50aW1lKCkgLSBsYXN0X2NhbGxlZFswXVxuICAgICAgICAgICAgaWYgZWxhcHNlZCA8IG1pbl9pbnRlcnZhbDpcbiAgICAgICAgICAgICAgICB0aW1lLnNsZWVwKG1pbl9pbnRlcnZhbCAtIGVsYXBzZWQpXG4gICAgICAgICAgICBsYXN0X2NhbGxlZFswXSA9IHRpbWUudGltZSgpXG4gICAgICAgICAgICByZXR1cm4gZm4oKmFyZ3MsICoqa3dhcmdzKVxuICAgICAgICByZXR1cm4gd3JhcHBlclxuICAgIHJldHVybiBkZWNvcmF0b3JcblxuQHJhdGVfbGltaXQoY2FsbHNfcGVyX3NlY29uZD0yKVxuZGVmIGNhbGxfYXBpKGVuZHBvaW50KTpcbiAgICBwcmludChmXCJDYWxsaW5nIHtlbmRwb2ludH1cIilcblxuY2FsbF9hcGkoXCIvYm9va3NcIilcbmNhbGxfYXBpKFwiL2Jvb2tzXCIpXG5jYWxsX2FwaShcIi9ib29rc1wiKSAgICMgdGhyb3R0bGVkOiB3YWl0cyBiZWZvcmUgdGhlIHRoaXJkIGNhbGwifQ"
 width="100%"
></iframe>

`min_interval` is captured in the closure of `decorator`, and `last_called` is captured in the closure of `wrapper`. Each decorated function gets its own `last_called` counter.

## Decorators With Arguments at a Glance

| Level | Function | Receives | Returns |
|---|---|---|---|
| 1 (factory) | `def retry(max_attempts):` | Decorator arguments | A decorator |
| 2 (decorator) | `def decorator(fn):` | The function to wrap | A wrapper |
| 3 (wrapper) | `def wrapper(*args, **kwargs):` | Call arguments | The result |

## Your Turn

Write a `timeout_after(seconds)` decorator that prints a warning message if the wrapped function takes longer than `seconds` to run. (Use `time.time()` before and after; actually interrupting execution requires threading, so for this exercise just print the warning after the fact.)

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2RlY29yYXRvcnNfd2l0aF9hcmd1bWVudHMgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6ImltcG9ydCB0aW1lXG5cbmRlZiB0aW1lb3V0X2FmdGVyKHNlY29uZHMpOlxuICAgIGRlZiBkZWNvcmF0b3IoZm4pOlxuICAgICAgICBkZWYgd3JhcHBlcigqYXJncywgKiprd2FyZ3MpOlxuICAgICAgICAgICAgc3RhcnQgPSB0aW1lLnRpbWUoKVxuICAgICAgICAgICAgcmVzdWx0ID0gZm4oKmFyZ3MsICoqa3dhcmdzKVxuICAgICAgICAgICAgZWxhcHNlZCA9IHRpbWUudGltZSgpIC0gc3RhcnRcbiAgICAgICAgICAgIGlmIGVsYXBzZWQgPiBzZWNvbmRzOlxuICAgICAgICAgICAgICAgIHByaW50KGZcIldBUk5JTkc6IHtmbi5fX25hbWVfX30gdG9vayB7ZWxhcHNlZDouMmZ9cyAobGltaXQge3NlY29uZHN9cylcIilcbiAgICAgICAgICAgIHJldHVybiByZXN1bHRcbiAgICAgICAgcmV0dXJuIHdyYXBwZXJcbiAgICByZXR1cm4gZGVjb3JhdG9yXG5cbkB0aW1lb3V0X2FmdGVyKDAuMSlcbmRlZiBzbG93X2Z1bmN0aW9uKCk6XG4gICAgdGltZS5zbGVlcCgwLjIpXG4gICAgcmV0dXJuIFwiZG9uZVwiXG5cbnByaW50KHNsb3dfZnVuY3Rpb24oKSkifQ"
 width="100%"
></iframe>

Run this and confirm the warning appears. Then apply `@timeout_after(0.5)` to a second function that sleeps for 0.1 seconds and confirm no warning appears.

## Conclusion

Decorators with arguments use a three-level nesting: the factory receives arguments, the decorator receives the function, and the wrapper contains the behavior. The `@factory(args)` syntax evaluates `factory(args)` first to get a decorator, then applies the decorator to the function. The next lesson covers a subtle issue that affects all decorators: by default, wrapping a function hides its name, docstring, and signature. `functools.wraps` fixes this in one line.
