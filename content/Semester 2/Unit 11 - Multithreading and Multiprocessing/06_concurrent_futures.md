## Introduction

Yuna has two pipelines: one that uses threads for I/O-bound work (downloading records), and one that uses processes for CPU-bound work (computing vectors). Each has its own API: `threading.Thread` / `multiprocessing.Pool`. She would like a single, consistent interface that works for both, so she can switch between them as the bottleneck shifts.

`concurrent.futures` provides exactly this: a unified executor API that works the same way for threads and processes, with a cleaner pattern for collecting results.

![Two executors shown side by side with identical API calls: ThreadPoolExecutor for I/O work and ProcessPoolExecutor for CPU work, both using submit() and as_completed()](images/06_concurrent_futures.png)

## The Executor Interface

`concurrent.futures` provides two executors: `ThreadPoolExecutor` (for I/O) and `ProcessPoolExecutor` (for CPU). Both have the same API.

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def fetch_record(record_id):
    import time
    time.sleep(0.1)   # simulate I/O
    return {"id": record_id, "title": f"Book {record_id}"}

# ThreadPoolExecutor for I/O-bound work:
with ThreadPoolExecutor(max_workers=8) as executor:
    futures = [executor.submit(fetch_record, i) for i in range(20)]
    results = [f.result() for f in futures]

print(f"Fetched {len(results)} records")
```

## executor.submit: Non-Blocking Submission

`submit(fn, *args, **kwargs)` submits a task and returns a `Future` immediately, without waiting for the task to complete. The future is a handle to the pending result.

```python
from concurrent.futures import ProcessPoolExecutor

def heavy_compute(n):
    return sum(i ** 2 for i in range(n))

with ProcessPoolExecutor(max_workers=4) as executor:
    # Submit all tasks immediately:
    f1 = executor.submit(heavy_compute, 1_000_000)
    f2 = executor.submit(heavy_compute, 2_000_000)
    f3 = executor.submit(heavy_compute, 500_000)

    # Get results (blocks until each future is done):
    r1 = f1.result()
    r2 = f2.result()
    r3 = f3.result()
    print(r1, r2, r3)
```

## executor.map: Submit Many, Collect in Order

`map(fn, iterable)` submits one task per item and returns results in input order:

```python
from concurrent.futures import ProcessPoolExecutor

def compute_vector(record_id):
    return record_id ** 2

if __name__ == "__main__":
    records = list(range(1000))
    with ProcessPoolExecutor(max_workers=4) as executor:
        vectors = list(executor.map(compute_vector, records))
    print(vectors[:5])
```

## as_completed: Process Results as They Arrive

When some tasks finish faster than others, `as_completed` yields futures as they complete, not in submission order:

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import random, time

def slow_fetch(library_id):
    delay = random.uniform(0.1, 1.0)
    time.sleep(delay)
    return library_id, delay

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = {executor.submit(slow_fetch, i): i for i in range(5)}
    for future in as_completed(futures):
        library_id = futures[future]
        lib_id, delay = future.result()
        print(f"Library {lib_id} done in {delay:.2f}s")
```

Using `as_completed` with a `{future: metadata}` dict lets you associate each result with its input when they come back out of order.

## Handling Exceptions in Futures

If a submitted task raises an exception, the exception is stored in the Future. Calling `future.result()` re-raises it:

```python
from concurrent.futures import ThreadPoolExecutor

def maybe_fail(x):
    if x == 3:
        raise ValueError(f"Failed for {x}")
    return x * 2

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(maybe_fail, i) for i in range(5)]
    for f in futures:
        try:
            print(f.result())
        except ValueError as exc:
            print(f"Error: {exc}")
```

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

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

def fetch_record(record_id):
    time.sleep(0.05)   # simulate I/O
    return {"id": record_id, "title": f"Book {record_id}"}

def compute_vector(record):
    words = record["title"].lower().split()
    return {word: words.count(word) for word in set(words)}

def parallel_fetch_and_index(record_ids, io_workers=8, cpu_workers=4):
    # Phase 1: fetch (I/O-bound)
    with ThreadPoolExecutor(max_workers=io_workers) as executor:
        records = list(executor.map(fetch_record, record_ids))

    # Phase 2: compute (CPU-bound)
    if __name__ == "__main__":
        with ProcessPoolExecutor(max_workers=cpu_workers) as executor:
            vectors = list(executor.map(compute_vector, records))
    return vectors

if __name__ == "__main__":
    import time
    start = time.perf_counter()
    result = parallel_fetch_and_index(range(100))
    print(f"Done in {time.perf_counter() - start:.2f}s, {len(result)} records")
```

## Conclusion

`concurrent.futures` provides a clean, unified API for both thread pools and process pools. `submit` is for individual tasks with individual results; `map` is for uniform processing of a collection; `as_completed` is for handling results as they finish. The final lesson brings all the concurrency tools together with a decision guide.
