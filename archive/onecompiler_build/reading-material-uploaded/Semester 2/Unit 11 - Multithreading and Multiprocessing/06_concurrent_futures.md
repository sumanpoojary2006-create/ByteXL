## Introduction

Yuna has two pipelines: one that uses threads for I/O-bound work (downloading records), and one that uses processes for CPU-bound work (computing vectors). Each has its own API: `threading.Thread` / `multiprocessing.Pool`. She would like a single, consistent interface that works for both, so she can switch between them as the bottleneck shifts.

`concurrent.futures` provides exactly this: a unified executor API that works the same way for threads and processes, with a cleaner pattern for collecting results.

![Two executors shown side by side with identical API calls: ThreadPoolExecutor for I/O work and ProcessPoolExecutor for CPU work, both using submit() and as_completed()](images/06_concurrent_futures.png)

## The Executor Interface

`concurrent.futures` provides two executors: `ThreadPoolExecutor` (for I/O) and `ProcessPoolExecutor` (for CPU). Both have the same API.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-06-concurrent-futures-001-4128c0836c.html"
 width="100%"
></iframe>

## executor.submit: Non-Blocking Submission

`submit(fn, *args, **kwargs)` submits a task and returns a `Future` immediately, without waiting for the task to complete. The future is a handle to the pending result.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-06-concurrent-futures-002-2405ac5399.html"
 width="100%"
></iframe>

## executor.map: Submit Many, Collect in Order

`map(fn, iterable)` submits one task per item and returns results in input order:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-06-concurrent-futures-003-2278838f85.html"
 width="100%"
></iframe>

## as_completed: Process Results as They Arrive

When some tasks finish faster than others, `as_completed` yields futures as they complete, not in submission order:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-06-concurrent-futures-004-1b9fdaafdb.html"
 width="100%"
></iframe>

Using `as_completed` with a `{future: metadata}` dict lets you associate each result with its input when they come back out of order.

## Handling Exceptions in Futures

If a submitted task raises an exception, the exception is stored in the Future. Calling `future.result()` re-raises it:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-06-concurrent-futures-005-9e2afdad00.html"
 width="100%"
></iframe>

## concurrent.futures at a Glance

| Feature | What it does |
|---|---|
| `ThreadPoolExecutor(max_workers)` | Thread pool for I/O-bound work |
| `ProcessPoolExecutor(max_workers)` | Process pool for CPU-bound work |
| `executor.submit(fn, *args)` | Submit one task, return a Future |
| `executor.map(fn, iterable)` | Submit many tasks, return results in order |
| `future.result()` | Get the result (blocks until done, raises on exception) |
| `as_completed(futures)` | Yield futures as they finish (not submission order) |

## Your Turn

Write `parallel_fetch_and_index(records)` that:
1. Uses `ThreadPoolExecutor` to fetch all records concurrently (simulate with `time.sleep`)
2. Uses `ProcessPoolExecutor` to compute vectors for the fetched records in parallel

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-06-concurrent-futures-006-9703442828.html"
 width="100%"
></iframe>

## Conclusion

`concurrent.futures` provides a clean, unified API for both thread pools and process pools. `submit` is for individual tasks with individual results; `map` is for uniform processing of a collection; `as_completed` is for handling results as they finish. The final lesson brings all the concurrency tools together with a decision guide.
