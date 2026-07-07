## Introduction

Miguel knows he needs non-blocking I/O and async-compatible libraries. Now he needs to understand the syntax: `async def`, `await`, and `asyncio.run`. These are three keywords and one function call, and they are the entire surface area of Python's async system from a developer's perspective. Everything else builds on them.

![A coroutine defined with async def, called with await inside another async function, and launched from synchronous code with asyncio.run(), shown as three nested frames](images/03_async_await.png)

## async def: Declaring a Coroutine

Adding `async` before `def` turns a function into a coroutine function. Calling it returns a coroutine object -- it does not execute the function body. The body only runs when the coroutine is awaited.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2FzeW5jX2F3YWl0IGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJpbXBvcnQgYXN5bmNpb1xuXG5hc3luYyBkZWYgZ3JlZXQobmFtZSk6XG4gICAgcHJpbnQoZlwiSGVsbG8sIHtuYW1lfVwiKVxuICAgIHJldHVybiBmXCJHcmVldGVkIHtuYW1lfVwiXG5cbiMgQ2FsbGluZyBpdCByZXR1cm5zIGEgY29yb3V0aW5lIG9iamVjdCAobm90IHRoZSByZXR1cm4gdmFsdWUpOlxuY29ybyA9IGdyZWV0KFwiTWlndWVsXCIpXG5wcmludCh0eXBlKGNvcm8pKSAgICMgPGNsYXNzICdjb3JvdXRpbmUnPlxucHJpbnQoY29ybykgICAgICAgICAjIDxjb3JvdXRpbmUgb2JqZWN0IGdyZWV0IGF0IDB4Li4uPlxuXG4jIFRoZSBjb3JvdXRpbmUgaGFzbid0IHJ1biB5ZXQuIElmIHdlIG5ldmVyIGF3YWl0IGl0OlxuIyBSdW50aW1lV2FybmluZzogY29yb3V0aW5lICdncmVldCcgd2FzIG5ldmVyIGF3YWl0ZWQifQ"
 width="100%"
></iframe>

## await: Running a Coroutine

`await` runs a coroutine and waits for it to complete, yielding control to the event loop while it waits. `await` can only be used inside an `async def` function.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2FzeW5jX2F3YWl0IGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJhc3luYyBkZWYgbWFpbigpOlxuICAgIHJlc3VsdCA9IGF3YWl0IGdyZWV0KFwiTWlndWVsXCIpICAgIyBydW5zIHRoZSBjb3JvdXRpbmUsIGdldHMgdGhlIHJldHVybiB2YWx1ZVxuICAgIHByaW50KHJlc3VsdCkgICAjIFwiR3JlZXRlZCBNaWd1ZWxcIiJ9"
 width="100%"
></iframe>

`await` does two things: it runs the coroutine and it suspends the current function at that point until the awaited thing is done, allowing the event loop to run other tasks.

## asyncio.run: The Entry Point

`asyncio.run` starts the event loop, runs a coroutine, and closes the loop when it finishes. It is the bridge between synchronous and asynchronous code, and it is called only once, at the top level.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2FzeW5jX2F3YWl0IGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJpbXBvcnQgYXN5bmNpb1xuXG5hc3luYyBkZWYgbWFpbigpOlxuICAgIHJlc3VsdCA9IGF3YWl0IGdyZWV0KFwiTWlndWVsXCIpXG4gICAgcHJpbnQocmVzdWx0KVxuXG5hc3luY2lvLnJ1bihtYWluKCkpICAgIyBzdGFydCB0aGUgZXZlbnQgbG9vcCBhbmQgcnVuIG1haW4oKSJ9"
 width="100%"
></iframe>

Do not call `asyncio.run` inside an existing async function; it creates a new event loop and will raise an error if one is already running.

## A Complete Async Example

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2FzeW5jX2F3YWl0IGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJpbXBvcnQgYXN5bmNpb1xuaW1wb3J0IGFpb2h0dHBcblxuYXN5bmMgZGVmIGZldGNoX2Jvb2tfc3RhdHVzKHNlc3Npb24sIGxpYnJhcnlfaWQsIGlzYm4pOlxuICAgIHVybCA9IGZcImh0dHBzOi8vYXBpLmxpYnJhcnl7bGlicmFyeV9pZH0uZXhhbXBsZS5jb20vYm9va3Mve2lzYm59XCJcbiAgICBhc3luYyB3aXRoIHNlc3Npb24uZ2V0KHVybCkgYXMgcmVzcG9uc2U6XG4gICAgICAgIGRhdGEgPSBhd2FpdCByZXNwb25zZS5qc29uKClcbiAgICAgICAgcmV0dXJuIGxpYnJhcnlfaWQsIGRhdGEuZ2V0KFwiYXZhaWxhYmxlXCIsIEZhbHNlKVxuXG5hc3luYyBkZWYgY2hlY2tfYXZhaWxhYmlsaXR5KGlzYm4pOlxuICAgIGFzeW5jIHdpdGggYWlvaHR0cC5DbGllbnRTZXNzaW9uKCkgYXMgc2Vzc2lvbjpcbiAgICAgICAgdGFzazEgPSBhc3luY2lvLmNyZWF0ZV90YXNrKGZldGNoX2Jvb2tfc3RhdHVzKHNlc3Npb24sIDEsIGlzYm4pKVxuICAgICAgICB0YXNrMiA9IGFzeW5jaW8uY3JlYXRlX3Rhc2soZmV0Y2hfYm9va19zdGF0dXMoc2Vzc2lvbiwgMiwgaXNibikpXG4gICAgICAgIHRhc2szID0gYXN5bmNpby5jcmVhdGVfdGFzayhmZXRjaF9ib29rX3N0YXR1cyhzZXNzaW9uLCAzLCBpc2JuKSlcblxuICAgICAgICByZXN1bHRzID0gYXdhaXQgYXN5bmNpby5nYXRoZXIodGFzazEsIHRhc2syLCB0YXNrMylcblxuICAgIGF2YWlsYWJsZV9hdCA9IFtsaWJfaWQgZm9yIGxpYl9pZCwgYXZhaWwgaW4gcmVzdWx0cyBpZiBhdmFpbF1cbiAgICByZXR1cm4gYXZhaWxhYmxlX2F0XG5cbmlmIF9fbmFtZV9fID09IFwiX19tYWluX19cIjpcbiAgICByZXN1bHQgPSBhc3luY2lvLnJ1bihjaGVja19hdmFpbGFiaWxpdHkoXCI5NzgtMDAxXCIpKVxuICAgIHByaW50KGZcIkF2YWlsYWJsZSBhdCBsaWJyYXJpZXM6IHtyZXN1bHR9XCIpIn0"
 width="100%"
></iframe>

## await Can Only Wait on Awaitables

`await` works on:
- Coroutines (returned by `async def` functions)
- `asyncio.Task` objects
- `asyncio.Future` objects
- Any object implementing `__await__`

`await` cannot wait on regular (non-async) functions. Trying to `await requests.get(url)` raises `TypeError: object Response can't be used in 'await' expression`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2FzeW5jX2F3YWl0IGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJhc3luYyBkZWYgd3JvbmdfdXNhZ2UoKTpcbiAgICBpbXBvcnQgcmVxdWVzdHNcbiAgICBhd2FpdCByZXF1ZXN0cy5nZXQoXCIuLi5cIikgICAjIFR5cGVFcnJvcjogcmVxdWVzdHMuUmVzcG9uc2UgaXMgbm90IGF3YWl0YWJsZVxuXG5hc3luYyBkZWYgY29ycmVjdF91c2FnZSgpOlxuICAgIGltcG9ydCBhaW9odHRwXG4gICAgYXN5bmMgd2l0aCBhaW9odHRwLkNsaWVudFNlc3Npb24oKSBhcyBzOlxuICAgICAgICBhc3luYyB3aXRoIHMuZ2V0KFwiLi4uXCIpIGFzIHJlc3A6ICAgIyByZXNwIGlzIGF3YWl0YWJsZVxuICAgICAgICAgICAgcmV0dXJuIGF3YWl0IHJlc3AuanNvbigpIn0"
 width="100%"
></iframe>

## Simulating I/O with asyncio.sleep

In examples and tests, use `asyncio.sleep` to simulate I/O wait:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2FzeW5jX2F3YWl0IGNvZGUgNiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNi5weSIsImNvZGUiOiJpbXBvcnQgYXN5bmNpb1xuXG5hc3luYyBkZWYgZmV0Y2hfZnJvbV9kYXRhYmFzZShxdWVyeSk6XG4gICAgYXdhaXQgYXN5bmNpby5zbGVlcCgwLjUpICAgIyBzaW11bGF0ZSA1MDBtcyBkYXRhYmFzZSBxdWVyeVxuICAgIHJldHVybiB7XCJxdWVyeVwiOiBxdWVyeSwgXCJyZXN1bHRcIjogXCJEdW5lXCJ9XG5cbmFzeW5jIGRlZiBtYWluKCk6XG4gICAgcmVzdWx0ID0gYXdhaXQgZmV0Y2hfZnJvbV9kYXRhYmFzZShcImlzYm49OTc4LTAwMVwiKVxuICAgIHByaW50KHJlc3VsdClcblxuYXN5bmNpby5ydW4obWFpbigpKSJ9"
 width="100%"
></iframe>

## async / await at a Glance

| Keyword / Function | What it does |
|---|---|
| `async def fn()` | Define a coroutine function |
| `fn()` | Create a coroutine object (does not run yet) |
| `await fn()` | Run the coroutine and wait for its result |
| `asyncio.run(main())` | Start the event loop and run `main()` |
| `asyncio.sleep(n)` | Async sleep (yields to event loop) |

## Your Turn

Write an async function `simulate_library_check(library_id, delay)` that simulates an API call with `asyncio.sleep(delay)` and returns `{"library": library_id, "available": library_id % 2 == 0}`. Then write an async `main` that calls it three times with different delays and prints the combined result.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2FzeW5jX2F3YWl0IGNvZGUgNyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNy5weSIsImNvZGUiOiJpbXBvcnQgYXN5bmNpb1xuXG5hc3luYyBkZWYgc2ltdWxhdGVfbGlicmFyeV9jaGVjayhsaWJyYXJ5X2lkLCBkZWxheSk6XG4gICAgYXdhaXQgYXN5bmNpby5zbGVlcChkZWxheSlcbiAgICByZXR1cm4ge1wibGlicmFyeVwiOiBsaWJyYXJ5X2lkLCBcImF2YWlsYWJsZVwiOiBsaWJyYXJ5X2lkICUgMiA9PSAwfVxuXG5hc3luYyBkZWYgbWFpbigpOlxuICAgIHJlc3VsdHMgPSBhd2FpdCBhc3luY2lvLmdhdGhlcihcbiAgICAgICAgc2ltdWxhdGVfbGlicmFyeV9jaGVjaygxLCAwLjMpLFxuICAgICAgICBzaW11bGF0ZV9saWJyYXJ5X2NoZWNrKDIsIDAuMSksXG4gICAgICAgIHNpbXVsYXRlX2xpYnJhcnlfY2hlY2soMywgMC4yKSxcbiAgICApXG4gICAgZm9yIHIgaW4gcmVzdWx0czpcbiAgICAgICAgcHJpbnQocilcblxuYXN5bmNpby5ydW4obWFpbigpKSJ9"
 width="100%"
></iframe>

Measure the total time. Confirm it is approximately 0.3 seconds (the longest delay), not 0.6 seconds (the sum).

## Conclusion

`async def` declares a coroutine. `await` runs it and yields to the event loop while waiting. `asyncio.run` is the entry point that starts the event loop for synchronous code. The next lesson explains the event loop in more depth: what it is, how it manages tasks, and how to think about execution flow in async programs.
