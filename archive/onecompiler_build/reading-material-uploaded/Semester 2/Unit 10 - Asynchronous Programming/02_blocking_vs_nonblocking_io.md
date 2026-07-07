## Introduction

Miguel converts his sequential code to use `async def` but keeps using the `requests` library for HTTP calls. His tests show no speed improvement. His more experienced colleague looks at the code and points to the problem immediately: `requests` is a blocking library. Wrapping it in an `async def` function does not make it non-blocking. He needs an async-compatible HTTP library instead.

This lesson clarifies what blocking and non-blocking mean, why blocking code inside an async function breaks the event loop, and how to recognize the difference.

![A timeline showing blocking code in an async function: the event loop stops completely during the blocking call, unable to run other tasks, versus non-blocking: the event loop continues running other tasks while waiting for I/O](images/02_blocking_vs_nonblocking_io.png)

## Blocking I/O: The Default

A blocking function does not return until its work is complete. When Python calls a blocking function, the entire thread stops and waits. Nothing else runs.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-02-blocking-vs-nonblocking-io-001-ca32e9187a.html"
 width="100%"
></iframe>

During the 1-second wait in the first call, no other code runs. The program is frozen at that line.

## The Event Loop and Why Blocking Breaks It

The asyncio event loop runs in a single thread. It switches between tasks at `await` points. If a task runs code that blocks the thread (without `await`), the event loop is frozen: it cannot switch to other tasks, and all pending async operations are stuck.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-02-blocking-vs-nonblocking-io-002-466e5178ee.html"
 width="100%"
></iframe>

The event loop is cooperatively scheduled. If one task never yields (`await`s), other tasks never run.

## Non-Blocking I/O: The Async Way

A non-blocking I/O operation tells the OS to start the operation and returns control immediately. The event loop registers a callback and runs other tasks until the OS signals that the operation is complete.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-02-blocking-vs-nonblocking-io-003-b7ba7794f7.html"
 width="100%"
></iframe>

`aiohttp` uses non-blocking socket operations. When `session.get` waits for the network, it yields control to the event loop, which runs the second task. Both complete in approximately the time of the single slowest call.

## Recognizing Blocking vs Non-Blocking

The rule: any function that does I/O must be async and awaitable for use inside an async function. If it is not, it blocks the event loop.

| Blocking (cannot use in async safely) | Non-blocking async equivalent |
|---|---|
| `requests.get(url)` | `aiohttp.ClientSession.get(url)` |
| `open(path).read()` | `aiofiles.open(path)` |
| `time.sleep(n)` | `asyncio.sleep(n)` |
| `sqlite3.connect(...)` | `aiosqlite.connect(...)` |

## Running Blocking Code Safely

When you must use a blocking library in an async context, run it in a thread pool so it does not block the event loop:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-02-blocking-vs-nonblocking-io-004-99f2ae1d15.html"
 width="100%"
></iframe>

`run_in_executor` runs the blocking function in a separate thread, yielding control to the event loop while the thread waits.

## Blocking vs Non-Blocking at a Glance

| Concept | What it means |
|---|---|
| Blocking I/O | Thread stops; event loop cannot switch to other tasks |
| Non-blocking I/O | Thread yields at `await`; event loop runs other tasks |
| `asyncio.sleep(n)` | Non-blocking pause (yields to event loop) |
| `time.sleep(n)` | Blocking pause (freezes event loop) |
| `run_in_executor` | Run blocking code in a thread without freezing the event loop |

## Your Turn

Compare these two implementations:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-02-blocking-vs-nonblocking-io-005-7f75a03b8d.html"
 width="100%"
></iframe>

Run this and observe the difference in timing. `good_pause` x3 should take approximately 1 second total; `bad_pause` x3 should take approximately 3 seconds.

## Conclusion

Blocking code in an async function freezes the event loop and eliminates any benefit from concurrency. Always use async-compatible libraries (`aiohttp` instead of `requests`, `asyncio.sleep` instead of `time.sleep`, `aiosqlite` instead of `sqlite3`) inside async functions. Use `run_in_executor` when you must call a blocking library. The next lesson introduces `async def` and `await` in detail, showing exactly how to write and run async functions.
