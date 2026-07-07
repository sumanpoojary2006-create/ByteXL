## Introduction

Miguel's availability checker is now three times faster, and he is enthusiastic about async. He wants to rewrite the entire library system with `async def`. His tech lead slows him down: async is not always better. Converting synchronous code to async has a cost, and for the wrong type of work, the cost yields no benefit. This final lesson provides a decision framework: when does async help, when does it not, and what to use instead?

![A decision tree: Is the code I/O-bound? Yes -> Is it concurrent requests or streams? Yes -> async. No -> threads. If CPU-bound -> multiprocessing.](images/08_when_async_helps.png)

## When async Helps: I/O-Bound Concurrent Operations

Async provides a speedup when:

1. The code spends time waiting for I/O (network, disk, database)
2. Multiple I/O operations can be run concurrently (no dependency between them)

```python
import asyncio
import time

# Good fit: fetch from multiple APIs -- all can run concurrently
async def fetch_one(isbn, delay=0.05):
    """Simulate an async HTTP request to check book availability."""
    await asyncio.sleep(delay)  # non-blocking wait (like a real API call)
    return {"isbn": isbn, "available": True, "library": "Central"}

async def fetch_all(isbns):
    tasks = [fetch_one(isbn) for isbn in isbns]
    return await asyncio.gather(*tasks)   # all run concurrently

isbns = ["978-001", "978-002", "978-003", "978-004", "978-005"]
start = time.perf_counter()
results = asyncio.run(fetch_all(isbns))
elapsed = time.perf_counter() - start

print(f"Fetched {len(results)} books concurrently in {elapsed:.3f}s")
print(f"(Sequential would take ~{len(results) * 0.05:.3f}s -- async saved that time)")
for r in results:
    print(f"  {r['isbn']}: available={r['available']}")
```

## When async Does Not Help: CPU-Bound Work

Async does not help when the bottleneck is computation. The event loop runs in one thread, and `await` only yields during I/O waits. If a function does pure computation with no I/O, `async def` just adds overhead without enabling concurrency.

```python
import asyncio
import time

# BAD FIT: pure computation -- async adds nothing
async def sort_catalog(books):
    return sorted(books, key=lambda b: b["title"])   # no I/O, no benefit from async

# CORRECT FIT: keep CPU-bound functions synchronous
def sort_catalog_sync(books):
    return sorted(books, key=lambda b: b["title"])   # simpler, no async overhead

books = [
    {"isbn": "978-003", "title": "Neuromancer"},
    {"isbn": "978-001", "title": "Dune"},
    {"isbn": "978-002", "title": "Foundation"},
]

# Async version: works, but adds unnecessary complexity
sorted_async = asyncio.run(sort_catalog(books))
print("Async sort (unnecessary overhead):", [b["title"] for b in sorted_async])

# Sync version: simpler and equally fast for CPU-bound work
sorted_sync = sort_catalog_sync(books)
print("Sync sort (correct approach):     ", [b["title"] for b in sorted_sync])

print("\nFor CPU-bound work like sorting, resizing images, or parsing data:")
print("  -> Use multiprocessing, not async")
print("  -> async only helps when the bottleneck is WAITING for I/O")
```

For CPU-bound work, use `multiprocessing` or `concurrent.futures.ProcessPoolExecutor`.

## When async Adds Complexity Without Benefit

Adding `async def` to a function has a cost: its callers must also be `async def` and must `await` it. If a function does not do I/O and is called from synchronous code, converting it to async only adds syntactic complexity:

```python
# Unnecessary async (no I/O, no concurrency benefit)
async def get_title(book):
    return book.title   # just a dict lookup -- async adds nothing

# Callers must now await it
title = await get_title(book)   # unnecessary overhead
print(title)
```

Keep synchronous functions synchronous unless there is a specific reason (I/O, awaitable dependency) to make them async.

## Async vs Threads vs Multiprocessing

The right concurrency tool depends on the type of work:

| Scenario | Tool |
|---|---|
| Many I/O-bound operations, async-compatible libraries | `asyncio` + `async/await` |
| I/O-bound with blocking libraries (can't avoid) | `threading` or `run_in_executor` |
| CPU-bound parallel computation | `multiprocessing` |
| Mixed I/O and CPU in the same program | `asyncio` for I/O, `run_in_executor(ProcessPoolExecutor)` for CPU |

## Migrating an Existing Codebase

Introducing async into a synchronous codebase is often called "async all the way down": to `await` a coroutine, the caller must be `async def`, and so must its caller, all the way up to `asyncio.run`. This means async changes propagate up the call stack.

Practical migration strategy:
1. Identify the I/O bottlenecks (profiling, not guessing)
2. Convert only the I/O-bound hot paths to async
3. Use `run_in_executor` for the blocking boundaries you cannot change
4. Leave CPU-bound functions synchronous

## A Decision Framework

```
Is the function waiting for I/O (network, disk, DB)?
  YES -> Can you use an async-compatible library?
           YES -> async def + await (best choice)
           NO  -> threading or run_in_executor
  NO  -> Is it computationally expensive?
           YES -> multiprocessing
           NO  -> keep it synchronous
```

## When Async Helps at a Glance

| Situation | Async benefit |
|---|---|
| 10 API calls in parallel | High: reduces wait time from sum to max |
| WebSocket / event stream | High: handle events as they arrive |
| Serving many HTTP clients | High: handle thousands concurrently |
| Sorting a list in memory | None: no I/O, no waiting |
| Image processing | None: CPU-bound, not I/O-bound |
| One sequential database query | Minimal: nothing to overlap with |

## Your Turn

Look at the library system code from earlier units and identify two functions that would benefit from being made async and two that would not. For each:

1. State the function and what it does
2. Explain whether the bottleneck is I/O or CPU
3. Decide: async, threading, multiprocessing, or leave synchronous?

For one of the async candidates, rewrite it using `async def` and `await asyncio.sleep` to simulate the I/O.

## Conclusion

Async programming is the right tool for I/O-bound concurrent operations: multiple network calls, database queries, or streams that can overlap. It does not help for CPU-bound computation. Adding `async def` to functions that do not need it adds complexity without benefit. The decision framework is simple: if the code waits for I/O and can be run concurrently, async helps; otherwise, keep it synchronous or reach for threads or multiprocessing. Unit 11 covers those other tools: multithreading and multiprocessing for cases where async is not the answer.
