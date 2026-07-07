## Introduction

Yuna tried threading for the CPU-intensive part of her indexing job (computing TF-IDF vectors) and found it ran at almost the same speed as single-threaded code, sometimes slower. She expected 4 threads to run 4x faster on a 4-core machine. Her team lead explains: this is the GIL, and it is why Python threads cannot parallelize CPU-bound work.

Understanding the GIL helps you avoid a common mistake: reaching for threads when you need processes, and wasting days debugging a performance regression.

![A diagram showing two CPU cores: with the GIL, one is always blocked (gray) while the other runs Python code (green), resulting in only one core ever active at a time despite having two threads](images/03_the_gil.png)

## What the GIL Is

The GIL (Global Interpreter Lock) is a mutex built into CPython (the reference Python implementation). It ensures that only one thread executes Python bytecode at any given moment. It was designed to protect Python's internal reference-counting garbage collector from concurrent modification, which would corrupt memory.

```
Without GIL (not Python):
CPU 1: Thread A: [===Python code===][===Python code===]
CPU 2: Thread B: [===Python code===][===Python code===]
Both run simultaneously: 2x throughput

With GIL (CPython):
CPU 1: Thread A: [===Python code===][GIL wait..........][===Python code===]
CPU 2: Thread B: [GIL wait..........][===Python code===][GIL wait..........]
One runs at a time: no improvement, context-switch overhead
```

## The GIL and I/O

The GIL is released whenever a thread performs I/O (network, disk, `time.sleep`). During I/O, the thread is not executing Python bytecode, so there is nothing to protect. Another thread acquires the GIL and runs.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-03-the-gil-001-a73575548f.html"
 width="100%"
></iframe>

## Measuring the GIL Effect

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-03-the-gil-002-11f7420ed7.html"
 width="100%"
></iframe>

Running this shows that threading does not speed up CPU-bound code in CPython.

## When the GIL Matters Less

Some operations release the GIL even though they look like computation:

- NumPy operations (NumPy releases the GIL for its C-level operations)
- Calls into C extensions that release the GIL explicitly
- `re` (regex) module for some operations

If your code is mostly NumPy operations, threading may parallelize them, because NumPy releases the GIL during its C code.

## The Alternative: No GIL in Python 3.13+

Python 3.13 introduced an experimental "no-GIL" build (PEP 703). When enabled, threads can run on multiple cores simultaneously. This is expected to become the default in a future version, but as of 2026, most production code still runs on builds with the GIL.

## The GIL at a Glance

| Scenario | GIL behavior | Threading benefit |
|---|---|---|
| Pure Python CPU work | GIL held: one thread at a time | None (or slower) |
| I/O: network, disk, sleep | GIL released: other threads run | Yes: concurrent I/O |
| NumPy / C extension code | GIL often released | Yes: real parallelism |
| Python 3.13+ no-GIL build | No GIL | Yes: CPU parallelism |

## Your Turn

Measure the GIL effect in three scenarios:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-03-the-gil-003-72b207363b.html"
 width="100%"
></iframe>

Compare scenarios 1-2 (threads do not help for CPU) and scenario 3 (threads do help for I/O).

## Conclusion

The GIL ensures only one thread executes Python bytecode at a time. For I/O-bound work, threads are effective because the GIL is released during I/O. For CPU-bound work, threads do not help and may be slower due to contention. The correct tool for CPU-bound parallelism is multiprocessing, where each process has its own GIL.
