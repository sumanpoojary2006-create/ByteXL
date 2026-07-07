## Introduction

Miguel's async code opens an `aiohttp.ClientSession()` without using a `with` statement. Every example he reads uses `async with session`. He knows from Unit 6 that `with` is for resource management -- but now there is an `async` version. Why? And what is the difference?

The reason is straightforward: in an async program, both acquiring and releasing a resource may require waiting for I/O. Regular `with` calls `__enter__` and `__exit__` synchronously. `async with` calls `__aenter__` and `__aexit__` as coroutines, allowing them to `await` I/O during setup and teardown.

![A comparison of with vs async with: the synchronous version calls __enter__ and __exit__ directly, while the async version awaits __aenter__ and __aexit__ as coroutines](images/07_async_context_managers.png)

## async with: The Async Context Manager

`async with` works like `with`, but it awaits the `__aenter__` and `__aexit__` methods. These must be coroutines (defined with `async def`).

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-07-async-context-managers-001-acc340410c.html"
 width="100%"
></iframe>

`aiohttp.ClientSession` implements `__aenter__` (opens the session) and `__aexit__` (closes it). Because session management may require I/O (like closing open connections), it must be async.

## Writing an Async Context Manager

Any class with `async def __aenter__` and `async def __aexit__` is an async context manager:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-07-async-context-managers-002-bda5a2bc95.html"
 width="100%"
></iframe>

## contextlib.asynccontextmanager

Just as `@contextmanager` simplifies synchronous context managers, `@asynccontextmanager` simplifies async ones:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-07-async-context-managers-003-51ee769284.html"
 width="100%"
></iframe>

The structure is identical to `@contextmanager`: code before `yield` is setup, `yield` provides the value, and code after is teardown.

## async for: Iterating Over Async Iterables

Alongside `async with`, Python provides `async for` for iterating over objects that yield values asynchronously (e.g., a database cursor, a paginated API, a WebSocket stream):

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-07-async-context-managers-004-f3950ef766.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-07-async-context-managers-005-445ca0328f.html"
 width="100%"
></iframe>

## Conclusion

Async context managers work like synchronous ones, but `__aenter__` and `__aexit__` are coroutines. Use `async with` for any resource that needs asynchronous setup or teardown. `@asynccontextmanager` provides the generator shortcut. `async for` iterates over async iterables. The final lesson in this unit answers the question Miguel started with: when does async actually help, and when is it the wrong tool?
