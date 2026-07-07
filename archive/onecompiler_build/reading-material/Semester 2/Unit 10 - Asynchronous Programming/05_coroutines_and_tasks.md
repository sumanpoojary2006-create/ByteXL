## Introduction

Miguel's availability checker `await`s three coroutines in sequence. They run one after the other, not concurrently. He needs to start all three at the same time so the event loop can run them concurrently while each waits for its I/O. The difference is between `await`ing a coroutine directly and wrapping it in a `Task`.

![Two execution diagrams: awaiting three coroutines in sequence (each waits for the previous), versus creating three tasks and gathering them (all three run concurrently)](images/05_coroutines_tasks.png)

## Coroutines vs Tasks

A coroutine is a function that can be paused and resumed. It does not start until you `await` it or wrap it in a `Task`. When you `await coro()` directly, the current function pauses and waits for `coro()` to finish before continuing. Other tasks cannot run during this time.

A `Task` wraps a coroutine and schedules it to run on the event loop immediately, concurrently with the current coroutine. Creating a task is the way to run multiple coroutines concurrently.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2Nvcm91dGluZXNfYW5kX3Rhc2tzIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJpbXBvcnQgYXN5bmNpb1xuXG5hc3luYyBkZWYgZmV0Y2gobGlicmFyeV9pZCk6XG4gICAgYXdhaXQgYXN5bmNpby5zbGVlcCgwLjUpICAgIyBzaW11bGF0ZSBJL09cbiAgICByZXR1cm4gZlwibGlicmFyeV97bGlicmFyeV9pZH06IGF2YWlsYWJsZVwiXG5cbmFzeW5jIGRlZiBzZXF1ZW50aWFsKCk6XG4gICAgIyBBd2FpdGluZyBkaXJlY3RseTogb25lIGF0IGEgdGltZVxuICAgIHIxID0gYXdhaXQgZmV0Y2goMSlcbiAgICByMiA9IGF3YWl0IGZldGNoKDIpXG4gICAgcjMgPSBhd2FpdCBmZXRjaCgzKVxuICAgIHJldHVybiBbcjEsIHIyLCByM11cbiMgVG90YWwgdGltZTogMS41c1xuXG5hc3luYyBkZWYgY29uY3VycmVudCgpOlxuICAgICMgVGFza3M6IGFsbCB0aHJlZSBydW4gYXQgb25jZVxuICAgIHQxID0gYXN5bmNpby5jcmVhdGVfdGFzayhmZXRjaCgxKSlcbiAgICB0MiA9IGFzeW5jaW8uY3JlYXRlX3Rhc2soZmV0Y2goMikpXG4gICAgdDMgPSBhc3luY2lvLmNyZWF0ZV90YXNrKGZldGNoKDMpKVxuICAgIHJldHVybiBhd2FpdCBhc3luY2lvLmdhdGhlcih0MSwgdDIsIHQzKVxuIyBUb3RhbCB0aW1lOiAwLjVzXG5cbmltcG9ydCB0aW1lXG5hc3luYyBkZWYgbWFpbigpOlxuICAgIHN0YXJ0ID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuICAgIGF3YWl0IHNlcXVlbnRpYWwoKVxuICAgIHByaW50KGZcIlNlcXVlbnRpYWw6IHt0aW1lLnBlcmZfY291bnRlcigpIC0gc3RhcnQ6LjJmfXNcIilcblxuICAgIHN0YXJ0ID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuICAgIGF3YWl0IGNvbmN1cnJlbnQoKVxuICAgIHByaW50KGZcIkNvbmN1cnJlbnQ6IHt0aW1lLnBlcmZfY291bnRlcigpIC0gc3RhcnQ6LjJmfXNcIilcblxuYXN5bmNpby5ydW4obWFpbigpKSJ9"
 width="100%"
></iframe>

## asyncio.create_task

`asyncio.create_task(coro)` wraps a coroutine in a `Task` and schedules it to run. The task starts running as soon as the current coroutine yields (via `await`).

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2Nvcm91dGluZXNfYW5kX3Rhc2tzIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJhc3luYyBkZWYgbWFpbigpOlxuICAgICMgVGFzayBpcyBjcmVhdGVkIGFuZCBzY2hlZHVsZWQgaW1tZWRpYXRlbHlcbiAgICB0YXNrID0gYXN5bmNpby5jcmVhdGVfdGFzayhmZXRjaCgxKSlcbiAgICBwcmludChmXCJUYXNrIGNyZWF0ZWQ6IHt0YXNrfVwiKVxuXG4gICAgIyBEbyBvdGhlciB3b3JrIHdoaWxlIHRhc2sgcnVucyBpbiBiYWNrZ3JvdW5kXG4gICAgYXdhaXQgYXN5bmNpby5zbGVlcCgwLjEpXG5cbiAgICAjIEJ5IG5vdywgZmV0Y2goMSkgbWF5IGhhdmUgYWxyZWFkeSBjb21wbGV0ZWRcbiAgICByZXN1bHQgPSBhd2FpdCB0YXNrICAgIyBhd2FpdCB0aGUgdGFzayB0byBnZXQgaXRzIHJldHVybiB2YWx1ZVxuICAgIHByaW50KGZcIlJlc3VsdDoge3Jlc3VsdH1cIikifQ"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2Nvcm91dGluZXNfYW5kX3Rhc2tzIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJhc3luYyBkZWYgbWFpbigpOlxuICAgIHRhc2sgPSBhc3luY2lvLmNyZWF0ZV90YXNrKGZldGNoKDEpKVxuICAgIHByaW50KGZcIkRvbmUgYmVmb3JlOiB7dGFzay5kb25lKCl9XCIpICAgIyBGYWxzZVxuICAgIHJlc3VsdCA9IGF3YWl0IHRhc2tcbiAgICBwcmludChmXCJEb25lIGFmdGVyOiB7dGFzay5kb25lKCl9XCIpICAgICMgVHJ1ZVxuICAgIHByaW50KGZcIlJlc3VsdDoge3Rhc2sucmVzdWx0KCl9XCIpICAgICAgIyBcImxpYnJhcnlfMTogYXZhaWxhYmxlXCIifQ"
 width="100%"
></iframe>

## Cancelling Tasks

A task can be cancelled before it completes:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2Nvcm91dGluZXNfYW5kX3Rhc2tzIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJhc3luYyBkZWYgc2xvd19mZXRjaChsaWJyYXJ5X2lkKTpcbiAgICBhd2FpdCBhc3luY2lvLnNsZWVwKDEwKSAgICMgc2ltdWxhdGVzIGEgdmVyeSBzbG93IEFQSVxuICAgIHJldHVybiBmXCJsaWJyYXJ5X3tsaWJyYXJ5X2lkfTogYXZhaWxhYmxlXCJcblxuYXN5bmMgZGVmIG1haW4oKTpcbiAgICB0YXNrID0gYXN5bmNpby5jcmVhdGVfdGFzayhzbG93X2ZldGNoKDEpKVxuXG4gICAgYXdhaXQgYXN5bmNpby5zbGVlcCgwLjUpICAgIyB3YWl0IGEgYml0LCB0aGVuIGNhbmNlbFxuICAgIHRhc2suY2FuY2VsKClcblxuICAgIHRyeTpcbiAgICAgICAgcmVzdWx0ID0gYXdhaXQgdGFza1xuICAgIGV4Y2VwdCBhc3luY2lvLkNhbmNlbGxlZEVycm9yOlxuICAgICAgICBwcmludChcIlRhc2sgd2FzIGNhbmNlbGxlZFwiKSJ9"
 width="100%"
></iframe>

`task.cancel()` sends a `CancelledError` to the task at its next `await` point. If the coroutine does not handle it, the task is cancelled. If it catches it and does not re-raise, the task continues.

## Timeout with asyncio.wait_for

`asyncio.wait_for` wraps a coroutine with a timeout, raising `asyncio.TimeoutError` if it does not complete in time:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2Nvcm91dGluZXNfYW5kX3Rhc2tzIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJhc3luYyBkZWYgbWFpbigpOlxuICAgIHRyeTpcbiAgICAgICAgcmVzdWx0ID0gYXdhaXQgYXN5bmNpby53YWl0X2ZvcihmZXRjaCgxKSwgdGltZW91dD0wLjEpXG4gICAgICAgICMgZmV0Y2ggdGFrZXMgMC41czsgdGltZW91dCBpcyAwLjFzIOKGkiBUaW1lb3V0RXJyb3JcbiAgICBleGNlcHQgYXN5bmNpby5UaW1lb3V0RXJyb3I6XG4gICAgICAgIHByaW50KFwiUmVxdWVzdCB0aW1lZCBvdXRcIikifQ"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2Nvcm91dGluZXNfYW5kX3Rhc2tzIGNvZGUgNiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNi5weSIsImNvZGUiOiJpbXBvcnQgYXN5bmNpb1xuXG5hc3luYyBkZWYgZmV0Y2hfd2l0aF90aW1lb3V0KGxpYnJhcnlfaWQsIGlzYm4sIHRpbWVvdXQpOlxuICAgIHRyeTpcbiAgICAgICAgcmV0dXJuIGF3YWl0IGFzeW5jaW8ud2FpdF9mb3IoXG4gICAgICAgICAgICBzaW11bGF0ZV9saWJyYXJ5X2NoZWNrKGxpYnJhcnlfaWQsIGlzYm4pLFxuICAgICAgICAgICAgdGltZW91dD10aW1lb3V0XG4gICAgICAgIClcbiAgICBleGNlcHQgYXN5bmNpby5UaW1lb3V0RXJyb3I6XG4gICAgICAgIHJldHVybiBOb25lXG5cbmFzeW5jIGRlZiBmZXRjaF9hbGxfd2l0aF90aW1lb3V0KGxpYnJhcmllcywgaXNibiwgdGltZW91dCk6XG4gICAgdGFza3MgPSB7XG4gICAgICAgIGxpYjogYXN5bmNpby5jcmVhdGVfdGFzayhmZXRjaF93aXRoX3RpbWVvdXQobGliLCBpc2JuLCB0aW1lb3V0KSlcbiAgICAgICAgZm9yIGxpYiBpbiBsaWJyYXJpZXNcbiAgICB9XG4gICAgcmVzdWx0cyA9IGF3YWl0IGFzeW5jaW8uZ2F0aGVyKCp0YXNrcy52YWx1ZXMoKSwgcmV0dXJuX2V4Y2VwdGlvbnM9VHJ1ZSlcbiAgICByZXR1cm4gZGljdCh6aXAodGFza3Mua2V5cygpLCByZXN1bHRzKSkifQ"
 width="100%"
></iframe>

## Conclusion

`await coro()` is sequential; `asyncio.create_task(coro())` is concurrent. Tasks can be cancelled and wrapped with timeouts using `asyncio.wait_for`. The most common pattern for running multiple async operations concurrently is to create tasks and then `await asyncio.gather(...)`, which is the subject of the next lesson.
