## Introduction

Kiran's unit is being deployed, and her team asks for three things: timing on every endpoint so they can identify slow calls, caching on expensive database lookups so the same query is not repeated hundreds of times a minute, and structured logging so they can trace what happened when something goes wrong. She has all the pieces from the previous lessons. This final lesson assembles them into production-quality versions of all three, the kind you would actually use in a real codebase.

![Three decorator cards labeled Timer, Cache, and Logger, each shown as a transparent layer wrapping a function body, preserving the original name and signature](images/08_realworld_decorators.png)

## A Production-Grade Timing Decorator

The version from earlier lessons printed timing to stdout. A production timing decorator should go through `logging`, work with `functools.wraps`, and optionally accept a label.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X3JlYWx3b3JsZF9kZWNvcmF0b3JzX3RpbWluZ19jYWNoaW5nX2xvZ2dpbmcgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6ImltcG9ydCB0aW1lXG5pbXBvcnQgbG9nZ2luZ1xuaW1wb3J0IGZ1bmN0b29sc1xuXG5sb2dnZXIgPSBsb2dnaW5nLmdldExvZ2dlcihfX25hbWVfXylcblxuZGVmIHRpbWVkKGZuPU5vbmUsICosIGxhYmVsPU5vbmUpOlxuICAgIGlmIGZuIGlzIE5vbmU6XG4gICAgICAgIHJldHVybiBmdW5jdG9vbHMucGFydGlhbCh0aW1lZCwgbGFiZWw9bGFiZWwpXG5cbiAgICBAZnVuY3Rvb2xzLndyYXBzKGZuKVxuICAgIGRlZiB3cmFwcGVyKCphcmdzLCAqKmt3YXJncyk6XG4gICAgICAgIG5hbWUgPSBsYWJlbCBvciBmbi5fX25hbWVfX1xuICAgICAgICBzdGFydCA9IHRpbWUucGVyZl9jb3VudGVyKClcbiAgICAgICAgdHJ5OlxuICAgICAgICAgICAgcmVzdWx0ID0gZm4oKmFyZ3MsICoqa3dhcmdzKVxuICAgICAgICAgICAgZWxhcHNlZCA9IHRpbWUucGVyZl9jb3VudGVyKCkgLSBzdGFydFxuICAgICAgICAgICAgbG9nZ2VyLmRlYnVnKGZcIntuYW1lfSBjb21wbGV0ZWQgaW4ge2VsYXBzZWQ6LjRmfXNcIilcbiAgICAgICAgICAgIHJldHVybiByZXN1bHRcbiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjpcbiAgICAgICAgICAgIGVsYXBzZWQgPSB0aW1lLnBlcmZfY291bnRlcigpIC0gc3RhcnRcbiAgICAgICAgICAgIGxvZ2dlci53YXJuaW5nKGZcIntuYW1lfSByYWlzZWQgYWZ0ZXIge2VsYXBzZWQ6LjRmfXNcIilcbiAgICAgICAgICAgIHJhaXNlXG4gICAgcmV0dXJuIHdyYXBwZXJcblxubG9nZ2luZy5iYXNpY0NvbmZpZyhsZXZlbD1sb2dnaW5nLkRFQlVHKVxuXG5AdGltZWRcbmRlZiBsb2FkX2NhdGFsb2coc2l6ZSk6XG4gICAgcmV0dXJuIGxpc3QocmFuZ2Uoc2l6ZSkpXG5cbkB0aW1lZChsYWJlbD1cInNlYXJjaC1vcFwiKVxuZGVmIHNlYXJjaChxdWVyeSwgY2F0YWxvZyk6XG4gICAgcmV0dXJuIFt4IGZvciB4IGluIGNhdGFsb2cgaWYgcXVlcnkgaW4gc3RyKHgpXVxuXG5jYXRhbG9nID0gbG9hZF9jYXRhbG9nKDEwMDApXG5yZXN1bHRzID0gc2VhcmNoKFwiNVwiLCBjYXRhbG9nKSJ9"
 width="100%"
></iframe>

Two things to note: `time.perf_counter()` is more precise than `time.time()` for measuring elapsed CPU time; and logging the failure time on exception gives visibility into slow failures, not just slow successes.

## A Caching Decorator: functools.lru_cache

Python's standard library provides a battle-tested caching decorator. `@functools.lru_cache` memoizes a function's return values by argument, evicting the Least Recently Used entry when the cache hits its size limit.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X3JlYWx3b3JsZF9kZWNvcmF0b3JzX3RpbWluZ19jYWNoaW5nX2xvZ2dpbmcgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6ImltcG9ydCBmdW5jdG9vbHNcblxuQGZ1bmN0b29scy5scnVfY2FjaGUobWF4c2l6ZT0xMjgpXG5kZWYgbG9va3VwX2Jvb2soaXNibik6XG4gICAgcHJpbnQoZlwiICBbREIgcXVlcnkgZm9yIHtpc2JufV1cIikgICAjIG9ubHkgcnVucyBvbiBjYWNoZSBtaXNzXG4gICAgcmV0dXJuIHtcImlzYm5cIjogaXNibiwgXCJ0aXRsZVwiOiBmXCJCb29rIHtpc2JufVwifVxuXG5wcmludChsb29rdXBfYm9vayhcIjk3OC0wMDFcIikpICAgIyBbREIgcXVlcnkgZm9yIDk3OC0wMDFdIC0tIGNhY2hlIG1pc3NcbnByaW50KGxvb2t1cF9ib29rKFwiOTc4LTAwMlwiKSkgICAjIFtEQiBxdWVyeSBmb3IgOTc4LTAwMl0gLS0gY2FjaGUgbWlzc1xucHJpbnQobG9va3VwX2Jvb2soXCI5NzgtMDAxXCIpKSAgICMgKG5vIHF1ZXJ5KSAtLSBjYWNoZSBoaXRcbnByaW50KGxvb2t1cF9ib29rKFwiOTc4LTAwMVwiKSkgICAjIChubyBxdWVyeSkgLS0gY2FjaGUgaGl0XG5cbnByaW50KGxvb2t1cF9ib29rLmNhY2hlX2luZm8oKSlcbiMgQ2FjaGVJbmZvKGhpdHM9MiwgbWlzc2VzPTIsIG1heHNpemU9MTI4LCBjdXJyc2l6ZT0yKSJ9"
 width="100%"
></iframe>

`lru_cache` requires the function's arguments to be hashable (no lists or dicts as arguments, since they cannot be used as dictionary keys). For mutable arguments, build a custom key and use a dictionary, or use `functools.cache` (Python 3.9+, equivalent to `lru_cache(maxsize=None)`).

## A Structured Logging Decorator

Beyond timing, a logging decorator can record the function name, arguments, result, and any exception, producing a structured trace that is searchable in a log aggregation system.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X3JlYWx3b3JsZF9kZWNvcmF0b3JzX3RpbWluZ19jYWNoaW5nX2xvZ2dpbmcgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6ImltcG9ydCBmdW5jdG9vbHNcbmltcG9ydCBsb2dnaW5nXG5cbmRlZiBsb2dfY2FsbChmbik6XG4gICAgQGZ1bmN0b29scy53cmFwcyhmbilcbiAgICBkZWYgd3JhcHBlcigqYXJncywgKiprd2FyZ3MpOlxuICAgICAgICBsb2dnaW5nLmluZm8oZlwiRU5URVIge2ZuLl9fbmFtZV9ffSB8IGFyZ3M9e2FyZ3N9IGt3YXJncz17a3dhcmdzfVwiKVxuICAgICAgICB0cnk6XG4gICAgICAgICAgICByZXN1bHQgPSBmbigqYXJncywgKiprd2FyZ3MpXG4gICAgICAgICAgICBsb2dnaW5nLmluZm8oZlwiRVhJVCAge2ZuLl9fbmFtZV9ffSB8IHJlc3VsdD17cmVzdWx0IXJ9XCIpXG4gICAgICAgICAgICByZXR1cm4gcmVzdWx0XG4gICAgICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZXhjOlxuICAgICAgICAgICAgbG9nZ2luZy5lcnJvcihmXCJFUlJPUiB7Zm4uX19uYW1lX199IHwge3R5cGUoZXhjKS5fX25hbWVfX306IHtleGN9XCIpXG4gICAgICAgICAgICByYWlzZVxuICAgIHJldHVybiB3cmFwcGVyXG5cbmxvZ2dpbmcuYmFzaWNDb25maWcobGV2ZWw9bG9nZ2luZy5JTkZPKVxuXG5AbG9nX2NhbGxcbmRlZiByZXNlcnZlX2Jvb2soaXNibiwgcGF0cm9uX2lkKTpcbiAgICBpZiBub3QgaXNibi5zdGFydHN3aXRoKFwiOTc4XCIpOlxuICAgICAgICByYWlzZSBWYWx1ZUVycm9yKGZcIkludmFsaWQgSVNCTjoge2lzYm59XCIpXG4gICAgcmV0dXJuIHtcImlzYm5cIjogaXNibiwgXCJwYXRyb25cIjogcGF0cm9uX2lkLCBcInN0YXR1c1wiOiBcInJlc2VydmVkXCJ9XG5cbnJlc2VydmVfYm9vayhcIjk3OC0wNDQxMDEzNTkzXCIsIFwiUDAwMVwiKVxucmVzZXJ2ZV9ib29rKFwiaW52YWxpZFwiLCBcIlAwMDJcIikgICAjIGVycm9yISJ9"
 width="100%"
></iframe>

## Combining All Three

With `@functools.wraps` applied at every level, these decorators compose correctly:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X3JlYWx3b3JsZF9kZWNvcmF0b3JzX3RpbWluZ19jYWNoaW5nX2xvZ2dpbmcgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6IkB0aW1lZFxuQGxvZ19jYWxsXG5AZnVuY3Rvb2xzLmxydV9jYWNoZShtYXhzaXplPTY0KVxuZGVmIGdldF9ib29rX3dpdGhfZGV0YWlscyhpc2JuKTpcbiAgICBcIlwiXCJGZXRjaCBib29rIGRldGFpbHMgYnkgSVNCTi5cIlwiXCJcbiAgICByZXR1cm4ge1wiaXNiblwiOiBpc2JuLCBcInRpdGxlXCI6IGZcIkJvb2sge2lzYm59XCJ9XG5cbmJvb2sgPSBnZXRfYm9va193aXRoX2RldGFpbHMoXCI5NzgtMDAxXCIpIn0"
 width="100%"
></iframe>

The `@lru_cache` is innermost (checks and populates the cache). `@log_call` wraps around it (logs each call, including cache hits). `@timed` is outermost (measures total time including logging overhead). The function's name and docstring are preserved throughout.

## Real-World Decorators at a Glance

| Decorator | Standard library | What it adds |
|---|---|---|
| Timing | Roll your own with `time.perf_counter` and `logging` | Elapsed time per call |
| Caching | `@functools.lru_cache(maxsize=N)` | Memoize by arguments |
| Logging | Roll your own with the `logging` module | ENTER/EXIT/ERROR trace |
| Retrying | Roll your own with a for-loop and try/except | Retry on exception |

## Your Turn

Apply all three production-quality decorators to a single function:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X3JlYWx3b3JsZF9kZWNvcmF0b3JzX3RpbWluZ19jYWNoaW5nX2xvZ2dpbmcgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6IkB0aW1lZFxuQGxvZ19jYWxsXG5AZnVuY3Rvb2xzLmxydV9jYWNoZShtYXhzaXplPTMyKVxuZGVmIGxvYWRfcGF0cm9uKHBhdHJvbl9pZCk6XG4gICAgXCJcIlwiRmV0Y2ggcGF0cm9uIGRldGFpbHMgYnkgSUQuXCJcIlwiXG4gICAgcmV0dXJuIHtcImlkXCI6IHBhdHJvbl9pZCwgXCJuYW1lXCI6IGZcIlBhdHJvbiB7cGF0cm9uX2lkfVwifVxuXG5sb2FkX3BhdHJvbihcIlAwMDFcIilcbmxvYWRfcGF0cm9uKFwiUDAwMlwiKVxubG9hZF9wYXRyb24oXCJQMDAxXCIpICAgIyBzaG91bGQgYmUgYSBjYWNoZSBoaXRcbnByaW50KGxvYWRfcGF0cm9uLmNhY2hlX2luZm8oKSkifQ"
 width="100%"
></iframe>

Confirm that the second call to `"P001"` does not log `ENTER` again (it is a cache hit; the wrapped function is not called). If your `@log_call` decorator logs the hit, discuss why: `@log_call` is outside `@lru_cache`, so it runs on every call regardless of the cache. Explain which order places `@log_call` inside the cache (so only misses log).

## Conclusion

Production decorators combine `functools.wraps` for identity preservation, the `logging` module for output, `time.perf_counter` for precision timing, and `functools.lru_cache` for memoization. Stacking them composes these capabilities without changing the decorated function itself. Unit 6 moves from wrapping functions to wrapping resource acquisition and release: context managers, which guarantee cleanup runs even when exceptions occur.
