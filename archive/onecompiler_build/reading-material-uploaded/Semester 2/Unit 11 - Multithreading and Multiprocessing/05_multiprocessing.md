## Introduction

After fixing the threading race conditions, Yuna still needs to speed up the CPU-intensive TF-IDF computation. She has confirmed with profiling that this step uses 100% CPU and no I/O. Threads cannot help. She needs `multiprocessing`: each worker runs in a separate process with its own GIL, enabling genuine parallel execution on multiple CPU cores.

![Four separate processes shown running on four CPU cores simultaneously, each with its own GIL and memory space, all processing a different slice of the catalog](images/05_multiprocessing.png)

## multiprocessing.Process

`multiprocessing.Process` works like `threading.Thread` but creates a new process instead:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-05-multiprocessing-001-65c0f0bd0f.html"
 width="100%"
></iframe>

The `if __name__ == "__main__":` guard is required when using `multiprocessing` on Windows and macOS (which use the `spawn` start method). On Linux (which uses `fork`), it is a best practice anyway.

## Passing Results Between Processes

Processes have separate memory. Results cannot be returned directly; they must be communicated through shared structures. `multiprocessing.Queue` is the cleanest option:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-05-multiprocessing-002-91d262e3b9.html"
 width="100%"
></iframe>

## multiprocessing.Pool

`Pool` provides a higher-level interface for parallelism over a collection: split work, run on N workers, collect results.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-05-multiprocessing-003-cbe9fc31e5.html"
 width="100%"
></iframe>

`pool.map(fn, iterable)` splits the iterable across workers and collects results in order. It is the multiprocessing equivalent of `map()`.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-05-multiprocessing-004-ff3d874556.html"
 width="100%"
></iframe>

## Caveats of Multiprocessing

**Pickling**: data passed between processes is serialized using `pickle`. Functions, classes, and arguments must all be picklable. Lambda functions and closures often cannot be pickled.

**Startup overhead**: creating a process is much slower than creating a thread. For short-running tasks, the startup overhead dominates and multiprocessing may be slower than single-threaded.

**Memory**: each process has its own copy of the data. If you pass 1 GB of records to 8 processes, you use 8 GB of memory.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-05-multiprocessing-005-d9dc54afc7.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-05-multiprocessing-006-4bbe557e4e.html"
 width="100%"
></iframe>

## Conclusion

`multiprocessing` creates separate processes that bypass the GIL, enabling true parallel execution on multiple CPU cores. `Pool.map` is the cleanest interface for CPU-bound parallel work over a collection. Watch out for pickle limitations and startup overhead. The next lesson introduces `concurrent.futures`, which provides a unified, higher-level interface for both thread and process pools.
