## Introduction

Yuna now has three concurrency tools in her toolkit: `asyncio`, `threading`, and `multiprocessing`. Each solves a different problem. In this final lesson, she builds the complete mental model: which tool for which job, how to profile to confirm the bottleneck, and how to combine tools for programs that have both I/O and CPU work.

![A flowchart decision tree: start with 'what is the bottleneck?' leading to I/O or CPU, then branching to async/threads/processes based on library availability and workload type](images/07_choosing_async_threads_processes.png)

## The Core Question: What Is the Bottleneck?

Profile first, choose second. The correct concurrency tool depends on whether the code is I/O-bound or CPU-bound. Do not guess.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-07-choosing-async-thread-001-0eacc9d119.html"
 width="100%"
></iframe>

Look at the output: if most time is in `time.sleep`, network calls, or database operations, it is I/O-bound. If it is in computation functions, it is CPU-bound.

## The Decision Framework

```
What is the bottleneck?
|
+-- I/O (network, database, disk)
|      |
|      +-- Can I use async-compatible libraries (aiohttp, aiosqlite)?
|      |      YES -> asyncio + async/await (best: single thread, no overhead)
|      |      NO  -> threading + ThreadPoolExecutor (GIL released during I/O)
|
+-- CPU (computation, image processing, data crunching)
       |
       +-- multiprocessing + ProcessPoolExecutor
           (each process has its own GIL; truly parallel)

Mixed I/O + CPU?
  -> asyncio for I/O, run_in_executor(ProcessPoolExecutor) for CPU
```

## Side-by-Side Comparison

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-07-choosing-async-thread-002-cf0dfca64b.html"
 width="100%"
></iframe>

## Combining asyncio and ProcessPoolExecutor

For programs with both heavy I/O and heavy CPU, run async for I/O and offload CPU work to a process pool via `asyncio.run_in_executor`:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-07-choosing-async-thread-003-add61d560d.html"
 width="100%"
></iframe>

`loop.run_in_executor(pool, fn, arg)` submits `fn(arg)` to the pool and returns an awaitable future. The event loop continues handling I/O while processes compute.

## Common Mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Using threads for CPU work | No speedup; GIL serializes | Use `ProcessPoolExecutor` |
| Using blocking I/O in async | Event loop blocked; no concurrency | Use async libs or `run_in_executor` |
| Not guarding with `__name__` | `ProcessPoolExecutor` spawns recursively on Windows | Always add `if __name__ == "__main__":` |
| Sharing mutable state between threads | Race conditions | Use `Lock`, `Queue`, or immutable data |
| Over-parallelizing tiny tasks | Process startup overhead dominates | Batch work; tune `chunksize` |

## Summary Table

| Tool | Best for | Library | Key limitation |
|---|---|---|---|
| `asyncio` | I/O-bound, async-compatible | Standard library | Must use async-compatible libs |
| `ThreadPoolExecutor` | I/O-bound, blocking libs | `concurrent.futures` | GIL prevents CPU parallelism |
| `ProcessPoolExecutor` | CPU-bound | `concurrent.futures` | Startup overhead; pickle required |
| `multiprocessing.Pool` | CPU-bound (more control) | `multiprocessing` | Same as above |

## Your Turn

Profile `run_slow_pipeline()` (a function you write that mixes I/O and CPU work) using `cProfile`. Based on where time is spent, choose the appropriate tool from the decision framework and rewrite the pipeline to use it. Measure the before and after wall-clock time.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-07-choosing-async-thread-004-b9500c96b0.html"
 width="100%"
></iframe>

Then rewrite with `ThreadPoolExecutor` for the I/O phase and `ProcessPoolExecutor` for the CPU phase.

## Conclusion

Profile before choosing a concurrency tool. `asyncio` is the right choice for I/O-bound code with async-compatible libraries. `ThreadPoolExecutor` handles I/O-bound code with blocking libraries. `ProcessPoolExecutor` handles CPU-bound parallelism. Combining asyncio with `run_in_executor(ProcessPoolExecutor)` handles programs with both I/O and CPU bottlenecks. Unit 12 moves from performance to usability: building command-line interfaces that make the library system accessible to non-programmers.
