## Introduction

Miguel knows he needs non-blocking I/O and async-compatible libraries. Now he needs to understand the syntax: `async def`, `await`, and `asyncio.run`. These are three keywords and one function call, and they are the entire surface area of Python's async system from a developer's perspective. Everything else builds on them.

![A coroutine defined with async def, called with await inside another async function, and launched from synchronous code with asyncio.run(), shown as three nested frames](images/03_async_await.png)

## async def: Declaring a Coroutine

Adding `async` before `def` turns a function into a coroutine function. Calling it returns a coroutine object -- it does not execute the function body. The body only runs when the coroutine is awaited.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-03-async-await-001-57696e0984.html"
 width="100%"
></iframe>

## await: Running a Coroutine

`await` runs a coroutine and waits for it to complete, yielding control to the event loop while it waits. `await` can only be used inside an `async def` function.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-03-async-await-002-9e3d3ca575.html"
 width="100%"
></iframe>

`await` does two things: it runs the coroutine and it suspends the current function at that point until the awaited thing is done, allowing the event loop to run other tasks.

## asyncio.run: The Entry Point

`asyncio.run` starts the event loop, runs a coroutine, and closes the loop when it finishes. It is the bridge between synchronous and asynchronous code, and it is called only once, at the top level.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-03-async-await-003-62ed4ddc49.html"
 width="100%"
></iframe>

Do not call `asyncio.run` inside an existing async function; it creates a new event loop and will raise an error if one is already running.

## A Complete Async Example

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-03-async-await-004-37da712759.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-03-async-await-005-4008e583f9.html"
 width="100%"
></iframe>

## Simulating I/O with asyncio.sleep

In examples and tests, use `asyncio.sleep` to simulate I/O wait:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-03-async-await-006-4c011b234f.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-03-async-await-007-6b8d46e771.html"
 width="100%"
></iframe>

Measure the total time. Confirm it is approximately 0.3 seconds (the longest delay), not 0.6 seconds (the sum).

## Conclusion

`async def` declares a coroutine. `await` runs it and yields to the event loop while waiting. `asyncio.run` is the entry point that starts the event loop for synchronous code. The next lesson explains the event loop in more depth: what it is, how it manages tasks, and how to think about execution flow in async programs.
