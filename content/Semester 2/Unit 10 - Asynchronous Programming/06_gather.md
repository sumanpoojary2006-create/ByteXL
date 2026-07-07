## Introduction

Miguel has been creating tasks manually and then `await`ing them one by one. His teammate shows him `asyncio.gather`, which starts multiple coroutines concurrently and collects all their results in a single `await`. It is the most common pattern in async Python and the cleanest way to write fan-out operations: send many requests, wait for all, return all results.

![A funnel diagram: many coroutines fan out from a single gather call, run concurrently, and their results fan back in to a single list when all are done](images/06_gather.png)

## asyncio.gather: Run Many, Collect All

`asyncio.gather` takes a list of coroutines or tasks, runs them concurrently, waits for all of them to finish, and returns their results in the same order as the inputs.

```python
import asyncio

async def fetch(library_id, delay=0.5):
    await asyncio.sleep(delay)
    return f"library_{library_id}: ok"

async def main():
    results = await asyncio.gather(
        fetch(1, delay=0.3),
        fetch(2, delay=0.5),
        fetch(3, delay=0.1),
    )
    print(results)
    # ['library_1: ok', 'library_2: ok', 'library_3: ok']
    # Results are in input order, not completion order

asyncio.run(main())
```

The total time is approximately 0.5 seconds (the longest), not 0.9 seconds (the sum). Results come back in the same order as the coroutines were passed, regardless of which finished first.

## gather with a List

For a dynamic number of coroutines, unpack a list:

```python
async def check_all_libraries(isbn, library_ids):
    coroutines = [fetch(lib_id) for lib_id in library_ids]
    results = await asyncio.gather(*coroutines)   # unpack the list
    return dict(zip(library_ids, results))

async def main():
    results = await check_all_libraries("978-001", [1, 2, 3, 4, 5])
    print(results)

asyncio.run(main())
```

## Handling Exceptions in gather

By default, if any coroutine raises an exception, `gather` immediately cancels the remaining coroutines and re-raises the first exception. The other results are lost.

```python
async def flaky_fetch(library_id):
    if library_id == 2:
        raise ConnectionError(f"Library {library_id} is down")
    await asyncio.sleep(0.1)
    return f"library_{library_id}: ok"

async def main():
    try:
        results = await asyncio.gather(
            flaky_fetch(1),
            flaky_fetch(2),   # will raise
            flaky_fetch(3),
        )
    except ConnectionError as exc:
        print(f"Failed: {exc}")
        # Results from library 1 and 3 are discarded
```

Use `return_exceptions=True` to capture exceptions as return values instead of raising:

```python
import asyncio

async def flaky_fetch(library_id):
    if library_id == 2:
        raise ConnectionError(f"Library {library_id} is down")
    await asyncio.sleep(0.05)
    return f"library_{library_id}: ok"

async def main():
    results = await asyncio.gather(
        flaky_fetch(1),
        flaky_fetch(2),   # raises ConnectionError
        flaky_fetch(3),
        return_exceptions=True
    )
    for i, result in enumerate(results, start=1):
        if isinstance(result, Exception):
            print(f"Library {i} failed: {result}")
        else:
            print(f"Library {i}: {result}")

asyncio.run(main())
# Library 1: library_1: ok
# Library 2 failed: Library 2 is down
# Library 3: library_3: ok
```

`return_exceptions=True` is the right choice when you want all results, even if some fail, and you will check them individually.

## asyncio.gather vs asyncio.wait

`asyncio.wait` is a lower-level function that gives more control: you can wait for the first result to come in, or wait until all are done, and you get sets of done/pending tasks.

```python
import asyncio

async def main():
    tasks = [
        asyncio.create_task(fetch(1, delay=0.5)),
        asyncio.create_task(fetch(2, delay=0.1)),
        asyncio.create_task(fetch(3, delay=0.3)),
    ]
    # Wait for the first one to complete:
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    first = done.pop().result()
    print(f"First completed: {first}")

    # Cancel remaining:
    for t in pending:
        t.cancel()
```

`gather` is simpler for "run all, collect all." `wait` is for more complex scheduling.

## gather at a Glance

| Pattern | Use |
|---|---|
| `await asyncio.gather(c1, c2, c3)` | Run three coroutines concurrently, collect results in order |
| `await asyncio.gather(*coros)` | Unpack a dynamic list of coroutines |
| `gather(..., return_exceptions=True)` | Capture exceptions as return values, don't raise |
| `asyncio.wait(..., FIRST_COMPLETED)` | Wait for the first to finish, cancel the rest |

## Your Turn

Write a `batch_check(isbns, library_id)` function that checks all ISBNs in a list concurrently for a single library, and returns a dict mapping each ISBN to whether it is available:

```python
import asyncio

async def check_isbn(library_id, isbn):
    await asyncio.sleep(0.1)   # simulate API call
    return isbn, len(isbn) % 2 == 0  # mock: even-length ISBNs are available

async def batch_check(isbns, library_id):
    results = await asyncio.gather(
        *[check_isbn(library_id, isbn) for isbn in isbns],
        return_exceptions=True
    )
    return {
        isbn: available
        for result in results
        if not isinstance(result, Exception)
        for isbn, available in [result]
    }

async def main():
    catalog = ["978-001", "978-002", "978-003", "978-004"]
    status = await batch_check(catalog, library_id=1)
    print(status)

asyncio.run(main())
```

## Conclusion

`asyncio.gather` is the main tool for running multiple coroutines concurrently and collecting all their results. Use `return_exceptions=True` when some may fail and you want all results. Use `asyncio.wait` when you need fine-grained control over which tasks finish first. The next lesson covers async context managers, which allow resources like database connections and HTTP sessions to be used safely in async code.
