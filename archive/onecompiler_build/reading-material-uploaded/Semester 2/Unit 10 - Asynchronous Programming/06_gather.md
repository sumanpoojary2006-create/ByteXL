## Introduction

Miguel has been creating tasks manually and then `await`ing them one by one. His teammate shows him `asyncio.gather`, which starts multiple coroutines concurrently and collects all their results in a single `await`. It is the most common pattern in async Python and the cleanest way to write fan-out operations: send many requests, wait for all, return all results.

![A funnel diagram: many coroutines fan out from a single gather call, run concurrently, and their results fan back in to a single list when all are done](images/06_gather.png)

## asyncio.gather: Run Many, Collect All

`asyncio.gather` takes a list of coroutines or tasks, runs them concurrently, waits for all of them to finish, and returns their results in the same order as the inputs.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-06-gather-001-3d6708c1c8.html"
 width="100%"
></iframe>

The total time is approximately 0.5 seconds (the longest), not 0.9 seconds (the sum). Results come back in the same order as the coroutines were passed, regardless of which finished first.

## gather with a List

For a dynamic number of coroutines, unpack a list:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-06-gather-002-bf41768b28.html"
 width="100%"
></iframe>

## Handling Exceptions in gather

By default, if any coroutine raises an exception, `gather` immediately cancels the remaining coroutines and re-raises the first exception. The other results are lost.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-06-gather-003-340fc0012d.html"
 width="100%"
></iframe>

Use `return_exceptions=True` to capture exceptions as return values instead of raising:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-06-gather-004-88e4fc8793.html"
 width="100%"
></iframe>

`return_exceptions=True` is the right choice when you want all results, even if some fail, and you will check them individually.

## asyncio.gather vs asyncio.wait

`asyncio.wait` is a lower-level function that gives more control: you can wait for the first result to come in, or wait until all are done, and you get sets of done/pending tasks.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-06-gather-005-5f78d8ef7d.html"
 width="100%"
></iframe>

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

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-06-gather-006-8cb6cb7fac.html"
 width="100%"
></iframe>

## Conclusion

`asyncio.gather` is the main tool for running multiple coroutines concurrently and collecting all their results. Use `return_exceptions=True` when some may fail and you want all results. Use `asyncio.wait` when you need fine-grained control over which tasks finish first. The next lesson covers async context managers, which allow resources like database connections and HTTP sessions to be used safely in async code.
