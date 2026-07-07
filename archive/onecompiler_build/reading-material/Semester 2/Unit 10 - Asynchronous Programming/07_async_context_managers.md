## Introduction

Miguel's async code opens an `aiohttp.ClientSession()` without using a `with` statement. Every example he reads uses `async with session`. He knows from Unit 6 that `with` is for resource management -- but now there is an `async` version. Why? And what is the difference?

The reason is straightforward: in an async program, both acquiring and releasing a resource may require waiting for I/O. Regular `with` calls `__enter__` and `__exit__` synchronously. `async with` calls `__aenter__` and `__aexit__` as coroutines, allowing them to `await` I/O during setup and teardown.

![A comparison of with vs async with: the synchronous version calls __enter__ and __exit__ directly, while the async version awaits __aenter__ and __aexit__ as coroutines](images/07_async_context_managers.png)

## async with: The Async Context Manager

`async with` works like `with`, but it awaits the `__aenter__` and `__aexit__` methods. These must be coroutines (defined with `async def`).

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2FzeW5jX2NvbnRleHRfbWFuYWdlcnMgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6ImltcG9ydCBhc3luY2lvXG5pbXBvcnQgYWlvaHR0cFxuXG5hc3luYyBkZWYgZmV0Y2hfY2F0YWxvZyh1cmwpOlxuICAgIGFzeW5jIHdpdGggYWlvaHR0cC5DbGllbnRTZXNzaW9uKCkgYXMgc2Vzc2lvbjogICMgYXdhaXQgX19hZW50ZXJfX1xuICAgICAgICBhc3luYyB3aXRoIHNlc3Npb24uZ2V0KHVybCkgYXMgcmVzcG9uc2U6ICAgICMgYXdhaXQgX19hZW50ZXJfX1xuICAgICAgICAgICAgZGF0YSA9IGF3YWl0IHJlc3BvbnNlLmpzb24oKVxuICAgICMgQm90aCBzZXNzaW9uIGFuZCByZXNwb25zZSBhcmUgY2xvc2VkIGhlcmUgKGF3YWl0IF9fYWV4aXRfXylcbiAgICByZXR1cm4gZGF0YSJ9"
 width="100%"
></iframe>

`aiohttp.ClientSession` implements `__aenter__` (opens the session) and `__aexit__` (closes it). Because session management may require I/O (like closing open connections), it must be async.

## Writing an Async Context Manager

Any class with `async def __aenter__` and `async def __aexit__` is an async context manager:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2FzeW5jX2NvbnRleHRfbWFuYWdlcnMgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6ImltcG9ydCBhc3luY2lvXG5pbXBvcnQgYWlvc3FsaXRlICAgIyBwaXAgaW5zdGFsbCBhaW9zcWxpdGVcblxuY2xhc3MgQXN5bmNEYXRhYmFzZTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgZGJfcGF0aCk6XG4gICAgICAgIHNlbGYuZGJfcGF0aCA9IGRiX3BhdGhcbiAgICAgICAgc2VsZi5jb25uID0gTm9uZVxuXG4gICAgYXN5bmMgZGVmIF9fYWVudGVyX18oc2VsZik6XG4gICAgICAgIHNlbGYuY29ubiA9IGF3YWl0IGFpb3NxbGl0ZS5jb25uZWN0KHNlbGYuZGJfcGF0aClcbiAgICAgICAgYXdhaXQgc2VsZi5jb25uLmV4ZWN1dGUoXCJQUkFHTUEgam91cm5hbF9tb2RlPVdBTFwiKVxuICAgICAgICByZXR1cm4gc2VsZi5jb25uXG5cbiAgICBhc3luYyBkZWYgX19hZXhpdF9fKHNlbGYsIGV4Y190eXBlLCBleGNfdmFsLCBleGNfdGIpOlxuICAgICAgICBpZiBleGNfdHlwZSBpcyBub3QgTm9uZTpcbiAgICAgICAgICAgIGF3YWl0IHNlbGYuY29ubi5yb2xsYmFjaygpXG4gICAgICAgIGVsc2U6XG4gICAgICAgICAgICBhd2FpdCBzZWxmLmNvbm4uY29tbWl0KClcbiAgICAgICAgYXdhaXQgc2VsZi5jb25uLmNsb3NlKClcbiAgICAgICAgcmV0dXJuIEZhbHNlXG5cbmFzeW5jIGRlZiBtYWluKCk6XG4gICAgYXN5bmMgd2l0aCBBc3luY0RhdGFiYXNlKFwiOm1lbW9yeTpcIikgYXMgY29ubjpcbiAgICAgICAgYXdhaXQgY29ubi5leGVjdXRlKFwiQ1JFQVRFIFRBQkxFIGJvb2tzIChpc2JuIFRFWFQsIHRpdGxlIFRFWFQpXCIpXG4gICAgICAgIGF3YWl0IGNvbm4uZXhlY3V0ZShcIklOU0VSVCBJTlRPIGJvb2tzIFZBTFVFUyAoJzk3OC0wMDEnLCAnRHVuZScpXCIpXG4gICAgICAgIGFzeW5jIHdpdGggY29ubi5leGVjdXRlKFwiU0VMRUNUICogRlJPTSBib29rc1wiKSBhcyBjdXJzb3I6XG4gICAgICAgICAgICByb3dzID0gYXdhaXQgY3Vyc29yLmZldGNoYWxsKClcbiAgICAgICAgICAgIHByaW50KHJvd3MpXG5cbmFzeW5jaW8ucnVuKG1haW4oKSkifQ"
 width="100%"
></iframe>

## contextlib.asynccontextmanager

Just as `@contextmanager` simplifies synchronous context managers, `@asynccontextmanager` simplifies async ones:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2FzeW5jX2NvbnRleHRfbWFuYWdlcnMgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6ImZyb20gY29udGV4dGxpYiBpbXBvcnQgYXN5bmNjb250ZXh0bWFuYWdlclxuaW1wb3J0IGFpb3NxbGl0ZVxuXG5AYXN5bmNjb250ZXh0bWFuYWdlclxuYXN5bmMgZGVmIGFzeW5jX2RiKGRiX3BhdGgpOlxuICAgIGNvbm4gPSBhd2FpdCBhaW9zcWxpdGUuY29ubmVjdChkYl9wYXRoKVxuICAgIHRyeTpcbiAgICAgICAgeWllbGQgY29ublxuICAgICAgICBhd2FpdCBjb25uLmNvbW1pdCgpXG4gICAgZXhjZXB0IEV4Y2VwdGlvbjpcbiAgICAgICAgYXdhaXQgY29ubi5yb2xsYmFjaygpXG4gICAgICAgIHJhaXNlXG4gICAgZmluYWxseTpcbiAgICAgICAgYXdhaXQgY29ubi5jbG9zZSgpXG5cbmFzeW5jIGRlZiBtYWluKCk6XG4gICAgYXN5bmMgd2l0aCBhc3luY19kYihcIjptZW1vcnk6XCIpIGFzIGNvbm46XG4gICAgICAgIGF3YWl0IGNvbm4uZXhlY3V0ZShcIkNSRUFURSBUQUJMRSBib29rcyAoaXNibiBURVhULCB0aXRsZSBURVhUKVwiKSJ9"
 width="100%"
></iframe>

The structure is identical to `@contextmanager`: code before `yield` is setup, `yield` provides the value, and code after is teardown.

## async for: Iterating Over Async Iterables

Alongside `async with`, Python provides `async for` for iterating over objects that yield values asynchronously (e.g., a database cursor, a paginated API, a WebSocket stream):

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2FzeW5jX2NvbnRleHRfbWFuYWdlcnMgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6ImltcG9ydCBhaW9zcWxpdGVcblxuYXN5bmMgZGVmIHN0cmVhbV9ib29rcyhkYl9wYXRoKTpcbiAgICBhc3luYyB3aXRoIGFpb3NxbGl0ZS5jb25uZWN0KGRiX3BhdGgpIGFzIGNvbm46XG4gICAgICAgIGFzeW5jIHdpdGggY29ubi5leGVjdXRlKFwiU0VMRUNUIGlzYm4sIHRpdGxlIEZST00gYm9va3NcIikgYXMgY3Vyc29yOlxuICAgICAgICAgICAgYXN5bmMgZm9yIHJvdyBpbiBjdXJzb3I6ICAgIyByb3dzIGFycml2ZSBhc3luY2hyb25vdXNseVxuICAgICAgICAgICAgICAgIHlpZWxkIHJvd1xuXG5hc3luYyBkZWYgbWFpbigpOlxuICAgIGFzeW5jIGZvciBpc2JuLCB0aXRsZSBpbiBzdHJlYW1fYm9va3MoXCI6bWVtb3J5OlwiKTpcbiAgICAgICAgcHJpbnQoZlwie2lzYm59OiB7dGl0bGV9XCIpIn0"
 width="100%"
></iframe>

`async for` calls `__aiter__` and `__anext__` as coroutines, allowing each "next item" request to suspend until the item is available.

## Async Context Managers at a Glance

| Feature | Sync version | Async version |
|---|---|---|
| Context manager | `with obj:` / `__enter__` / `__exit__` | `async with obj:` / `__aenter__` / `__aexit__` |
| Generator shortcut | `@contextmanager` | `@asynccontextmanager` |
| Iteration | `for x in iterable:` | `async for x in async_iterable:` |

## Your Turn

Write an `async_timer` context manager using `@asynccontextmanager` that measures how long an async block takes:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2FzeW5jX2NvbnRleHRfbWFuYWdlcnMgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6ImltcG9ydCBhc3luY2lvXG5pbXBvcnQgdGltZVxuZnJvbSBjb250ZXh0bGliIGltcG9ydCBhc3luY2NvbnRleHRtYW5hZ2VyXG5cbkBhc3luY2NvbnRleHRtYW5hZ2VyXG5hc3luYyBkZWYgYXN5bmNfdGltZXIobGFiZWw9XCJvcGVyYXRpb25cIik6XG4gICAgc3RhcnQgPSB0aW1lLnBlcmZfY291bnRlcigpXG4gICAgdHJ5OlxuICAgICAgICB5aWVsZFxuICAgIGZpbmFsbHk6XG4gICAgICAgIGVsYXBzZWQgPSB0aW1lLnBlcmZfY291bnRlcigpIC0gc3RhcnRcbiAgICAgICAgcHJpbnQoZlwie2xhYmVsfToge2VsYXBzZWQ6LjRmfXNcIilcblxuYXN5bmMgZGVmIG1haW4oKTpcbiAgICBhc3luYyB3aXRoIGFzeW5jX3RpbWVyKFwiYmF0Y2ggZmV0Y2hcIik6XG4gICAgICAgIGF3YWl0IGFzeW5jaW8uZ2F0aGVyKFxuICAgICAgICAgICAgYXN5bmNpby5zbGVlcCgwLjMpLFxuICAgICAgICAgICAgYXN5bmNpby5zbGVlcCgwLjUpLFxuICAgICAgICAgICAgYXN5bmNpby5zbGVlcCgwLjEpLFxuICAgICAgICApXG4gICAgIyBwcmludHM6IGJhdGNoIGZldGNoOiAwLjUwMDBzIChhcHByb3hpbWF0ZWx5KVxuXG5hc3luY2lvLnJ1bihtYWluKCkpIn0"
 width="100%"
></iframe>

## Conclusion

Async context managers work like synchronous ones, but `__aenter__` and `__aexit__` are coroutines. Use `async with` for any resource that needs asynchronous setup or teardown. `@asynccontextmanager` provides the generator shortcut. `async for` iterates over async iterables. The final lesson in this unit answers the question Miguel started with: when does async actually help, and when is it the wrong tool?
