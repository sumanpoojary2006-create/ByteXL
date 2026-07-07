## Introduction

Yuna now has three concurrency tools in her toolkit: `asyncio`, `threading`, and `multiprocessing`. Each solves a different problem. In this final lesson, she builds the complete mental model: which tool for which job, how to profile to confirm the bottleneck, and how to combine tools for programs that have both I/O and CPU work.

![A flowchart decision tree: start with 'what is the bottleneck?' leading to I/O or CPU, then branching to async/threads/processes based on library availability and workload type](images/07_choosing_async_threads_processes.png)

## The Core Question: What Is the Bottleneck?

Profile first, choose second. The correct concurrency tool depends on whether the code is I/O-bound or CPU-bound. Do not guess.

```python
import cProfile
import pstats

# Profile the slow function:
profiler = cProfile.Profile()
profiler.enable()
run_slow_pipeline()   # the code to profile
profiler.disable()

stats = pstats.Stats(profiler)
stats.sort_stats("cumulative")
stats.print_stats(10)   # top 10 slowest functions
print(stats)
```

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

```python
import asyncio
import concurrent.futures
import time

DATA = list(range(1000))

# --- asyncio: for I/O-bound with async libs ---
async def async_pipeline(items):
    async def fetch(item):
        await asyncio.sleep(0.01)   # simulate network I/O
        return item * 2
    return await asyncio.gather(*[fetch(x) for x in items])

# --- threading: for I/O-bound with blocking libs ---
def thread_pipeline(items):
    def fetch(item):
        time.sleep(0.01)   # blocking I/O
        return item * 2
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
        return list(ex.map(fetch, items))

# --- multiprocessing: for CPU-bound ---
def cpu_work(item):
    return sum(i ** 2 for i in range(item * 10))

def process_pipeline(items):
    with concurrent.futures.ProcessPoolExecutor() as ex:
        return list(ex.map(cpu_work, items))

# Demo:
result = thread_pipeline([1, 2, 3])
print(f"thread_pipeline([1, 2, 3]) -> {result}")
result = cpu_work(1000)
print(f"cpu_work(1000) -> {result}")
```

## Combining asyncio and ProcessPoolExecutor

For programs with both heavy I/O and heavy CPU, run async for I/O and offload CPU work to a process pool via `asyncio.run_in_executor`:

```python
import asyncio
import concurrent.futures

def heavy_cpu(record):
    return sum(i ** 2 for i in range(record["size"]))

async def pipeline(records):
    loop = asyncio.get_running_loop()
    cpu_pool = concurrent.futures.ProcessPoolExecutor()

    # I/O phase: fetch all records concurrently (async)
    async def fetch(r):
        await asyncio.sleep(0.05)   # simulate network
        return r

    fetched = await asyncio.gather(*[fetch(r) for r in records])

    # CPU phase: process records in parallel processes
    results = await asyncio.gather(*[
        loop.run_in_executor(cpu_pool, heavy_cpu, r)
        for r in fetched
    ])
    cpu_pool.shutdown()
    return results

if __name__ == "__main__":
    records = [{"size": 10_000, "id": i} for i in range(20)]
    results = asyncio.run(pipeline(records))
    print(f"Done: {len(results)} results")
```

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

```python
import time

def run_slow_pipeline():
    records = []
    for i in range(100):
        time.sleep(0.01)   # I/O bottleneck: simulate fetching
        records.append(sum(j ** 2 for j in range(i * 10)))   # CPU work
    return records

start = time.perf_counter()
run_slow_pipeline()
print(f"Baseline: {time.perf_counter() - start:.2f}s")
```

Then rewrite with `ThreadPoolExecutor` for the I/O phase and `ProcessPoolExecutor` for the CPU phase.

## Conclusion

Profile before choosing a concurrency tool. `asyncio` is the right choice for I/O-bound code with async-compatible libraries. `ThreadPoolExecutor` handles I/O-bound code with blocking libraries. `ProcessPoolExecutor` handles CPU-bound parallelism. Combining asyncio with `run_in_executor(ProcessPoolExecutor)` handles programs with both I/O and CPU bottlenecks. Unit 12 moves from performance to usability: building command-line interfaces that make the library system accessible to non-programmers.
