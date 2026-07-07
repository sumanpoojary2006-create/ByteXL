## Introduction

Miguel's availability checker `await`s three coroutines in sequence. They run one after the other, not concurrently. He needs to start all three at the same time so the event loop can run them concurrently while each waits for its I/O. The difference is between `await`ing a coroutine directly and wrapping it in a `Task`.

![Two execution diagrams: awaiting three coroutines in sequence (each waits for the previous), versus creating three tasks and gathering them (all three run concurrently)](images/05_coroutines_tasks.png)

## Coroutines vs Tasks

A coroutine is a function that can be paused and resumed. It does not start until you `await` it or wrap it in a `Task`. When you `await coro()` directly, the current function pauses and waits for `coro()` to finish before continuing. Other tasks cannot run during this time.

A `Task` wraps a coroutine and schedules it to run on the event loop immediately, concurrently with the current coroutine. Creating a task is the way to run multiple coroutines concurrently.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-05-coroutines-and-tasks-001-b89952f399.html"
 width="100%"
></iframe>

## asyncio.create_task

`asyncio.create_task(coro)` wraps a coroutine in a `Task` and schedules it to run. The task starts running as soon as the current coroutine yields (via `await`).

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-05-coroutines-and-tasks-002-a65672d1f3.html"
 width="100%"
></iframe>

## Task Lifecycle

A task can be in one of four states:

- **Pending**: created, not yet done
- **Running**: currently executing on the event loop
- **Done**: completed (success or exception)
- **Cancelled**: explicitly cancelled

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-05-coroutines-and-tasks-003-ab700ae6a9.html"
 width="100%"
></iframe>

## Cancelling Tasks

A task can be cancelled before it completes:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-05-coroutines-and-tasks-004-085afb4e9d.html"
 width="100%"
></iframe>

`task.cancel()` sends a `CancelledError` to the task at its next `await` point. If the coroutine does not handle it, the task is cancelled. If it catches it and does not re-raise, the task continues.

## Timeout with asyncio.wait_for

`asyncio.wait_for` wraps a coroutine with a timeout, raising `asyncio.TimeoutError` if it does not complete in time:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-05-coroutines-and-tasks-005-f5c944e2da.html"
 width="100%"
></iframe>

## Coroutines and Tasks at a Glance

| Concept | What it means |
|---|---|
| `await coro()` | Run coroutine sequentially; current function waits |
| `asyncio.create_task(coro)` | Schedule coroutine concurrently; returns a Task |
| `task.done()` | True if the task has completed |
| `task.result()` | Get the task's return value (raises if not done) |
| `task.cancel()` | Request cancellation |
| `asyncio.wait_for(coro, timeout)` | Run with a timeout; raises `TimeoutError` |

## Your Turn

Write a function `fetch_all_with_timeout(libraries, isbn, timeout)` that creates a task for each library, waits for all of them with a per-library timeout, and returns a dict mapping library ID to result (or `None` if timed out):

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-05-coroutines-and-tasks-006-4db7b966b6.html"
 width="100%"
></iframe>

## Conclusion

`await coro()` is sequential; `asyncio.create_task(coro())` is concurrent. Tasks can be cancelled and wrapped with timeouts using `asyncio.wait_for`. The most common pattern for running multiple async operations concurrently is to create tasks and then `await asyncio.gather(...)`, which is the subject of the next lesson.
