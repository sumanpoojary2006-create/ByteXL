## Introduction

Yuna has two pipelines: one that uses threads for I/O-bound work (downloading records), and one that uses processes for CPU-bound work (computing vectors). Each has its own API: `threading.Thread` / `multiprocessing.Pool`. She would like a single, consistent interface that works for both, so she can switch between them as the bottleneck shifts.

`concurrent.futures` provides exactly this: a unified executor API that works the same way for threads and processes, with a cleaner pattern for collecting results.

![Two executors shown side by side with identical API calls: ThreadPoolExecutor for I/O work and ProcessPoolExecutor for CPU work, both using submit() and as_completed()](images/06_concurrent_futures.png)

## The Executor Interface

`concurrent.futures` provides two executors: `ThreadPoolExecutor` (for I/O) and `ProcessPoolExecutor` (for CPU). Both have the same API.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2NvbmN1cnJlbnRfZnV0dXJlcyBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoiZnJvbSBjb25jdXJyZW50LmZ1dHVyZXMgaW1wb3J0IFRocmVhZFBvb2xFeGVjdXRvciwgUHJvY2Vzc1Bvb2xFeGVjdXRvclxuXG5kZWYgZmV0Y2hfcmVjb3JkKHJlY29yZF9pZCk6XG4gICAgaW1wb3J0IHRpbWVcbiAgICB0aW1lLnNsZWVwKDAuMSkgICAjIHNpbXVsYXRlIEkvT1xuICAgIHJldHVybiB7XCJpZFwiOiByZWNvcmRfaWQsIFwidGl0bGVcIjogZlwiQm9vayB7cmVjb3JkX2lkfVwifVxuXG4jIFRocmVhZFBvb2xFeGVjdXRvciBmb3IgSS9PLWJvdW5kIHdvcms6XG53aXRoIFRocmVhZFBvb2xFeGVjdXRvcihtYXhfd29ya2Vycz04KSBhcyBleGVjdXRvcjpcbiAgICBmdXR1cmVzID0gW2V4ZWN1dG9yLnN1Ym1pdChmZXRjaF9yZWNvcmQsIGkpIGZvciBpIGluIHJhbmdlKDIwKV1cbiAgICByZXN1bHRzID0gW2YucmVzdWx0KCkgZm9yIGYgaW4gZnV0dXJlc11cblxucHJpbnQoZlwiRmV0Y2hlZCB7bGVuKHJlc3VsdHMpfSByZWNvcmRzXCIpIn0"
 width="100%"
></iframe>

## executor.submit: Non-Blocking Submission

`submit(fn, *args, **kwargs)` submits a task and returns a `Future` immediately, without waiting for the task to complete. The future is a handle to the pending result.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2NvbmN1cnJlbnRfZnV0dXJlcyBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoiZnJvbSBjb25jdXJyZW50LmZ1dHVyZXMgaW1wb3J0IFByb2Nlc3NQb29sRXhlY3V0b3JcblxuZGVmIGhlYXZ5X2NvbXB1dGUobik6XG4gICAgcmV0dXJuIHN1bShpICoqIDIgZm9yIGkgaW4gcmFuZ2UobikpXG5cbndpdGggUHJvY2Vzc1Bvb2xFeGVjdXRvcihtYXhfd29ya2Vycz00KSBhcyBleGVjdXRvcjpcbiAgICAjIFN1Ym1pdCBhbGwgdGFza3MgaW1tZWRpYXRlbHk6XG4gICAgZjEgPSBleGVjdXRvci5zdWJtaXQoaGVhdnlfY29tcHV0ZSwgMV8wMDBfMDAwKVxuICAgIGYyID0gZXhlY3V0b3Iuc3VibWl0KGhlYXZ5X2NvbXB1dGUsIDJfMDAwXzAwMClcbiAgICBmMyA9IGV4ZWN1dG9yLnN1Ym1pdChoZWF2eV9jb21wdXRlLCA1MDBfMDAwKVxuXG4gICAgIyBHZXQgcmVzdWx0cyAoYmxvY2tzIHVudGlsIGVhY2ggZnV0dXJlIGlzIGRvbmUpOlxuICAgIHIxID0gZjEucmVzdWx0KClcbiAgICByMiA9IGYyLnJlc3VsdCgpXG4gICAgcjMgPSBmMy5yZXN1bHQoKVxuICAgIHByaW50KHIxLCByMiwgcjMpIn0"
 width="100%"
></iframe>

## executor.map: Submit Many, Collect in Order

`map(fn, iterable)` submits one task per item and returns results in input order:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2NvbmN1cnJlbnRfZnV0dXJlcyBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoiZnJvbSBjb25jdXJyZW50LmZ1dHVyZXMgaW1wb3J0IFByb2Nlc3NQb29sRXhlY3V0b3JcblxuZGVmIGNvbXB1dGVfdmVjdG9yKHJlY29yZF9pZCk6XG4gICAgcmV0dXJuIHJlY29yZF9pZCAqKiAyXG5cbmlmIF9fbmFtZV9fID09IFwiX19tYWluX19cIjpcbiAgICByZWNvcmRzID0gbGlzdChyYW5nZSgxMDAwKSlcbiAgICB3aXRoIFByb2Nlc3NQb29sRXhlY3V0b3IobWF4X3dvcmtlcnM9NCkgYXMgZXhlY3V0b3I6XG4gICAgICAgIHZlY3RvcnMgPSBsaXN0KGV4ZWN1dG9yLm1hcChjb21wdXRlX3ZlY3RvciwgcmVjb3JkcykpXG4gICAgcHJpbnQodmVjdG9yc1s6NV0pIn0"
 width="100%"
></iframe>

## as_completed: Process Results as They Arrive

When some tasks finish faster than others, `as_completed` yields futures as they complete, not in submission order:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2NvbmN1cnJlbnRfZnV0dXJlcyBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoiZnJvbSBjb25jdXJyZW50LmZ1dHVyZXMgaW1wb3J0IFRocmVhZFBvb2xFeGVjdXRvciwgYXNfY29tcGxldGVkXG5pbXBvcnQgcmFuZG9tLCB0aW1lXG5cbmRlZiBzbG93X2ZldGNoKGxpYnJhcnlfaWQpOlxuICAgIGRlbGF5ID0gcmFuZG9tLnVuaWZvcm0oMC4xLCAxLjApXG4gICAgdGltZS5zbGVlcChkZWxheSlcbiAgICByZXR1cm4gbGlicmFyeV9pZCwgZGVsYXlcblxud2l0aCBUaHJlYWRQb29sRXhlY3V0b3IobWF4X3dvcmtlcnM9NSkgYXMgZXhlY3V0b3I6XG4gICAgZnV0dXJlcyA9IHtleGVjdXRvci5zdWJtaXQoc2xvd19mZXRjaCwgaSk6IGkgZm9yIGkgaW4gcmFuZ2UoNSl9XG4gICAgZm9yIGZ1dHVyZSBpbiBhc19jb21wbGV0ZWQoZnV0dXJlcyk6XG4gICAgICAgIGxpYnJhcnlfaWQgPSBmdXR1cmVzW2Z1dHVyZV1cbiAgICAgICAgbGliX2lkLCBkZWxheSA9IGZ1dHVyZS5yZXN1bHQoKVxuICAgICAgICBwcmludChmXCJMaWJyYXJ5IHtsaWJfaWR9IGRvbmUgaW4ge2RlbGF5Oi4yZn1zXCIpIn0"
 width="100%"
></iframe>

Using `as_completed` with a `{future: metadata}` dict lets you associate each result with its input when they come back out of order.

## Handling Exceptions in Futures

If a submitted task raises an exception, the exception is stored in the Future. Calling `future.result()` re-raises it:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2NvbmN1cnJlbnRfZnV0dXJlcyBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoiZnJvbSBjb25jdXJyZW50LmZ1dHVyZXMgaW1wb3J0IFRocmVhZFBvb2xFeGVjdXRvclxuXG5kZWYgbWF5YmVfZmFpbCh4KTpcbiAgICBpZiB4ID09IDM6XG4gICAgICAgIHJhaXNlIFZhbHVlRXJyb3IoZlwiRmFpbGVkIGZvciB7eH1cIilcbiAgICByZXR1cm4geCAqIDJcblxud2l0aCBUaHJlYWRQb29sRXhlY3V0b3IobWF4X3dvcmtlcnM9NCkgYXMgZXhlY3V0b3I6XG4gICAgZnV0dXJlcyA9IFtleGVjdXRvci5zdWJtaXQobWF5YmVfZmFpbCwgaSkgZm9yIGkgaW4gcmFuZ2UoNSldXG4gICAgZm9yIGYgaW4gZnV0dXJlczpcbiAgICAgICAgdHJ5OlxuICAgICAgICAgICAgcHJpbnQoZi5yZXN1bHQoKSlcbiAgICAgICAgZXhjZXB0IFZhbHVlRXJyb3IgYXMgZXhjOlxuICAgICAgICAgICAgcHJpbnQoZlwiRXJyb3I6IHtleGN9XCIpIn0"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2NvbmN1cnJlbnRfZnV0dXJlcyBjb2RlIDYiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDYucHkiLCJjb2RlIjoiZnJvbSBjb25jdXJyZW50LmZ1dHVyZXMgaW1wb3J0IFRocmVhZFBvb2xFeGVjdXRvciwgUHJvY2Vzc1Bvb2xFeGVjdXRvclxuaW1wb3J0IHRpbWVcblxuZGVmIGZldGNoX3JlY29yZChyZWNvcmRfaWQpOlxuICAgIHRpbWUuc2xlZXAoMC4wNSkgICAjIHNpbXVsYXRlIEkvT1xuICAgIHJldHVybiB7XCJpZFwiOiByZWNvcmRfaWQsIFwidGl0bGVcIjogZlwiQm9vayB7cmVjb3JkX2lkfVwifVxuXG5kZWYgY29tcHV0ZV92ZWN0b3IocmVjb3JkKTpcbiAgICB3b3JkcyA9IHJlY29yZFtcInRpdGxlXCJdLmxvd2VyKCkuc3BsaXQoKVxuICAgIHJldHVybiB7d29yZDogd29yZHMuY291bnQod29yZCkgZm9yIHdvcmQgaW4gc2V0KHdvcmRzKX1cblxuZGVmIHBhcmFsbGVsX2ZldGNoX2FuZF9pbmRleChyZWNvcmRfaWRzLCBpb193b3JrZXJzPTgsIGNwdV93b3JrZXJzPTQpOlxuICAgICMgUGhhc2UgMTogZmV0Y2ggKEkvTy1ib3VuZClcbiAgICB3aXRoIFRocmVhZFBvb2xFeGVjdXRvcihtYXhfd29ya2Vycz1pb193b3JrZXJzKSBhcyBleGVjdXRvcjpcbiAgICAgICAgcmVjb3JkcyA9IGxpc3QoZXhlY3V0b3IubWFwKGZldGNoX3JlY29yZCwgcmVjb3JkX2lkcykpXG5cbiAgICAjIFBoYXNlIDI6IGNvbXB1dGUgKENQVS1ib3VuZClcbiAgICBpZiBfX25hbWVfXyA9PSBcIl9fbWFpbl9fXCI6XG4gICAgICAgIHdpdGggUHJvY2Vzc1Bvb2xFeGVjdXRvcihtYXhfd29ya2Vycz1jcHVfd29ya2VycykgYXMgZXhlY3V0b3I6XG4gICAgICAgICAgICB2ZWN0b3JzID0gbGlzdChleGVjdXRvci5tYXAoY29tcHV0ZV92ZWN0b3IsIHJlY29yZHMpKVxuICAgIHJldHVybiB2ZWN0b3JzXG5cbmlmIF9fbmFtZV9fID09IFwiX19tYWluX19cIjpcbiAgICBpbXBvcnQgdGltZVxuICAgIHN0YXJ0ID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuICAgIHJlc3VsdCA9IHBhcmFsbGVsX2ZldGNoX2FuZF9pbmRleChyYW5nZSgxMDApKVxuICAgIHByaW50KGZcIkRvbmUgaW4ge3RpbWUucGVyZl9jb3VudGVyKCkgLSBzdGFydDouMmZ9cywge2xlbihyZXN1bHQpfSByZWNvcmRzXCIpIn0"
 width="100%"
></iframe>

## Conclusion

`concurrent.futures` provides a clean, unified API for both thread pools and process pools. `submit` is for individual tasks with individual results; `map` is for uniform processing of a collection; `as_completed` is for handling results as they finish. The final lesson brings all the concurrency tools together with a decision guide.
