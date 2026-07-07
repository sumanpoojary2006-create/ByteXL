## Introduction

After fixing the threading race conditions, Yuna still needs to speed up the CPU-intensive TF-IDF computation. She has confirmed with profiling that this step uses 100% CPU and no I/O. Threads cannot help. She needs `multiprocessing`: each worker runs in a separate process with its own GIL, enabling genuine parallel execution on multiple CPU cores.

![Four separate processes shown running on four CPU cores simultaneously, each with its own GIL and memory space, all processing a different slice of the catalog](images/05_multiprocessing.png)

## multiprocessing.Process

`multiprocessing.Process` works like `threading.Thread` but creates a new process instead:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X211bHRpcHJvY2Vzc2luZyBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoiZnJvbSBtdWx0aXByb2Nlc3NpbmcgaW1wb3J0IFByb2Nlc3NcbmltcG9ydCB0aW1lXG5cbmRlZiBjb21wdXRlX3ZlY3RvcnMoYmF0Y2hfaWQsIHJlY29yZHMpOlxuICAgIHByaW50KGZcIlByb2Nlc3Mge2JhdGNoX2lkfTogY29tcHV0aW5nIHZlY3RvcnMgZm9yIHtsZW4ocmVjb3Jkcyl9IHJlY29yZHNcIilcbiAgICB0aW1lLnNsZWVwKDEpICAgIyBzaW11bGF0ZSBDUFUgd29ya1xuICAgIHByaW50KGZcIlByb2Nlc3Mge2JhdGNoX2lkfTogZG9uZVwiKVxuXG5pZiBfX25hbWVfXyA9PSBcIl9fbWFpbl9fXCI6XG4gICAgcmVjb3JkcyA9IGxpc3QocmFuZ2UoMTAwKSlcbiAgICBiYXRjaGVzID0gW3JlY29yZHNbaTppKzI1XSBmb3IgaSBpbiByYW5nZSgwLCAxMDAsIDI1KV1cblxuICAgIHByb2Nlc3NlcyA9IFtcbiAgICAgICAgUHJvY2Vzcyh0YXJnZXQ9Y29tcHV0ZV92ZWN0b3JzLCBhcmdzPShpLCBiYXRjaCkpXG4gICAgICAgIGZvciBpLCBiYXRjaCBpbiBlbnVtZXJhdGUoYmF0Y2hlcylcbiAgICBdXG4gICAgZm9yIHAgaW4gcHJvY2Vzc2VzOlxuICAgICAgICBwLnN0YXJ0KClcbiAgICBmb3IgcCBpbiBwcm9jZXNzZXM6XG4gICAgICAgIHAuam9pbigpXG4gICAgcHJpbnQoXCJBbGwgYmF0Y2hlcyBkb25lXCIpIn0"
 width="100%"
></iframe>

The `if __name__ == "__main__":` guard is required when using `multiprocessing` on Windows and macOS (which use the `spawn` start method). On Linux (which uses `fork`), it is a best practice anyway.

## Passing Results Between Processes

Processes have separate memory. Results cannot be returned directly; they must be communicated through shared structures. `multiprocessing.Queue` is the cleanest option:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X211bHRpcHJvY2Vzc2luZyBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoiZnJvbSBtdWx0aXByb2Nlc3NpbmcgaW1wb3J0IFByb2Nlc3MsIFF1ZXVlXG5cbmRlZiBjb21wdXRlX2FuZF9yZXR1cm4oYmF0Y2hfaWQsIHJlY29yZHMsIHJlc3VsdF9xdWV1ZSk6XG4gICAgcmVzdWx0ID0gc3VtKHIgKiogMiBmb3IgciBpbiByZWNvcmRzKSAgICMgQ1BVLWJvdW5kIGNvbXB1dGF0aW9uXG4gICAgcmVzdWx0X3F1ZXVlLnB1dCgoYmF0Y2hfaWQsIHJlc3VsdCkpXG5cbmlmIF9fbmFtZV9fID09IFwiX19tYWluX19cIjpcbiAgICByZWNvcmRzID0gbGlzdChyYW5nZSgxMDAwKSlcbiAgICBiYXRjaGVzID0gW3JlY29yZHNbaTppKzI1MF0gZm9yIGkgaW4gcmFuZ2UoMCwgMTAwMCwgMjUwKV1cbiAgICByZXN1bHRfcXVldWUgPSBRdWV1ZSgpXG5cbiAgICBwcm9jZXNzZXMgPSBbXG4gICAgICAgIFByb2Nlc3ModGFyZ2V0PWNvbXB1dGVfYW5kX3JldHVybiwgYXJncz0oaSwgYmF0Y2gsIHJlc3VsdF9xdWV1ZSkpXG4gICAgICAgIGZvciBpLCBiYXRjaCBpbiBlbnVtZXJhdGUoYmF0Y2hlcylcbiAgICBdXG4gICAgZm9yIHAgaW4gcHJvY2Vzc2VzOlxuICAgICAgICBwLnN0YXJ0KClcbiAgICBmb3IgcCBpbiBwcm9jZXNzZXM6XG4gICAgICAgIHAuam9pbigpXG5cbiAgICByZXN1bHRzID0ge31cbiAgICB3aGlsZSBub3QgcmVzdWx0X3F1ZXVlLmVtcHR5KCk6XG4gICAgICAgIGJhdGNoX2lkLCByZXN1bHQgPSByZXN1bHRfcXVldWUuZ2V0KClcbiAgICAgICAgcmVzdWx0c1tiYXRjaF9pZF0gPSByZXN1bHRcbiAgICBwcmludChyZXN1bHRzKSJ9"
 width="100%"
></iframe>

## multiprocessing.Pool

`Pool` provides a higher-level interface for parallelism over a collection: split work, run on N workers, collect results.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X211bHRpcHJvY2Vzc2luZyBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoiZnJvbSBtdWx0aXByb2Nlc3NpbmcgaW1wb3J0IFBvb2xcblxuZGVmIGNvbXB1dGVfdmVjdG9yKHJlY29yZF9pZCk6XG4gICAgcmV0dXJuIHJlY29yZF9pZCAqKiAyICAgIyBDUFUtYm91bmQgcGVyLXJlY29yZCBjb21wdXRhdGlvblxuXG5pZiBfX25hbWVfXyA9PSBcIl9fbWFpbl9fXCI6XG4gICAgcmVjb3JkcyA9IGxpc3QocmFuZ2UoMTAwMCkpXG5cbiAgICB3aXRoIFBvb2wocHJvY2Vzc2VzPTQpIGFzIHBvb2w6XG4gICAgICAgIHJlc3VsdHMgPSBwb29sLm1hcChjb21wdXRlX3ZlY3RvciwgcmVjb3JkcylcbiAgICAjIHJlc3VsdHMgaXMgYSBsaXN0IGluIHRoZSBzYW1lIG9yZGVyIGFzIHJlY29yZHNcbiAgICBwcmludChmXCJGaXJzdCA1OiB7cmVzdWx0c1s6NV19XCIpIn0"
 width="100%"
></iframe>

`pool.map(fn, iterable)` splits the iterable across workers and collects results in order. It is the multiprocessing equivalent of `map()`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X211bHRpcHJvY2Vzc2luZyBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoiIyBGb3IgY2h1bmtlZCBwcm9jZXNzaW5nIChiZXR0ZXIgZm9yIGxhcmdlIGl0ZXJhYmxlcyk6XG53aXRoIFBvb2wocHJvY2Vzc2VzPTQpIGFzIHBvb2w6XG4gICAgcmVzdWx0cyA9IHBvb2wubWFwKGNvbXB1dGVfdmVjdG9yLCByZWNvcmRzLCBjaHVua3NpemU9NTApXG4jIGNodW5rc2l6ZT01MDogZWFjaCB3b3JrZXIgcmVjZWl2ZXMgNTAgaXRlbXMgYXQgYSB0aW1lIGluc3RlYWQgb2YgMSJ9"
 width="100%"
></iframe>

## Caveats of Multiprocessing

**Pickling**: data passed between processes is serialized using `pickle`. Functions, classes, and arguments must all be picklable. Lambda functions and closures often cannot be pickled.

**Startup overhead**: creating a process is much slower than creating a thread. For short-running tasks, the startup overhead dominates and multiprocessing may be slower than single-threaded.

**Memory**: each process has its own copy of the data. If you pass 1 GB of records to 8 processes, you use 8 GB of memory.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X211bHRpcHJvY2Vzc2luZyBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoiIyBXUk9ORzogbGFtYmRhIGZ1bmN0aW9ucyBjYW5ub3QgYmUgcGlja2xlZFxud2l0aCBQb29sKDQpIGFzIHBvb2w6XG4gICAgcmVzdWx0cyA9IHBvb2wubWFwKGxhbWJkYSB4OiB4ICoqIDIsIHJlY29yZHMpICAgIyBQaWNrbGluZ0Vycm9yXG5cbiMgQ09SUkVDVDogdXNlIGEgbmFtZWQgZnVuY3Rpb25cbmRlZiBzcXVhcmUoeCk6XG4gICAgcmV0dXJuIHggKiogMlxuXG53aXRoIFBvb2woNCkgYXMgcG9vbDpcbiAgICByZXN1bHRzID0gcG9vbC5tYXAoc3F1YXJlLCByZWNvcmRzKSJ9"
 width="100%"
></iframe>

## multiprocessing at a Glance

| Feature | What it does |
|---|---|
| `Process(target, args)` | Create a new process |
| `p.start()` / `p.join()` | Start and wait for a process |
| `multiprocessing.Queue` | Thread+process-safe data passing |
| `Pool(n)` | Create N worker processes |
| `pool.map(fn, iterable)` | Apply fn to iterable in parallel |
| `if __name__ == "__main__":` | Required guard on Windows/macOS |

## Your Turn

Write a function `parallel_index(records, n_workers)` that uses `Pool.map` to compute a vector for each record in parallel:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X211bHRpcHJvY2Vzc2luZyBjb2RlIDYiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDYucHkiLCJjb2RlIjoiZnJvbSBtdWx0aXByb2Nlc3NpbmcgaW1wb3J0IFBvb2xcblxuZGVmIGNvbXB1dGVfc2VhcmNoX3ZlY3RvcihyZWNvcmQpOlxuICAgIHdvcmRzID0gcmVjb3JkW1widGl0bGVcIl0ubG93ZXIoKS5zcGxpdCgpXG4gICAgcmV0dXJuIHt3b3JkOiB3b3Jkcy5jb3VudCh3b3JkKSBmb3Igd29yZCBpbiBzZXQod29yZHMpfVxuXG5kZWYgcGFyYWxsZWxfaW5kZXgocmVjb3Jkcywgbl93b3JrZXJzPTQpOlxuICAgIHdpdGggUG9vbChwcm9jZXNzZXM9bl93b3JrZXJzKSBhcyBwb29sOlxuICAgICAgICB2ZWN0b3JzID0gcG9vbC5tYXAoY29tcHV0ZV9zZWFyY2hfdmVjdG9yLCByZWNvcmRzKVxuICAgIHJldHVybiBkaWN0KHppcChyYW5nZShsZW4ocmVjb3JkcykpLCB2ZWN0b3JzKSlcblxuaWYgX19uYW1lX18gPT0gXCJfX21haW5fX1wiOlxuICAgIGNhdGFsb2cgPSBbXG4gICAgICAgIHtcImlkXCI6IDEsIFwidGl0bGVcIjogXCJEdW5lIHRoZSBncmVhdCBub3ZlbFwifSxcbiAgICAgICAge1wiaWRcIjogMiwgXCJ0aXRsZVwiOiBcIkZvdW5kYXRpb24gYSBncmVhdCBib29rXCJ9LFxuICAgIF1cbiAgICByZXN1bHQgPSBwYXJhbGxlbF9pbmRleChjYXRhbG9nLCBuX3dvcmtlcnM9MilcbiAgICBwcmludChyZXN1bHQpIn0"
 width="100%"
></iframe>

## Conclusion

`multiprocessing` creates separate processes that bypass the GIL, enabling true parallel execution on multiple CPU cores. `Pool.map` is the cleanest interface for CPU-bound parallel work over a collection. Watch out for pickle limitations and startup overhead. The next lesson introduces `concurrent.futures`, which provides a unified, higher-level interface for both thread and process pools.
