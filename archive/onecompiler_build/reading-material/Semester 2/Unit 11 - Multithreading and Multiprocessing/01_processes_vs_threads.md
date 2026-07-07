## Introduction

Yuna runs a nightly catalog indexing job for the library consortium. It processes 50,000 book records, computing search vectors and updating the index. On a single core, it takes 22 minutes. The server has 8 cores. She wants to use them. Her question: should she use threads or processes, and what is the difference?

The answer depends on what is actually happening in the code -- whether it is waiting for I/O or doing computation -- and on a Python-specific constraint called the GIL. This lesson explains what processes and threads are, and why Python's threading model behaves differently from what you might expect in other languages.

![A diagram showing a process as a box with its own memory, and threads within that process sharing the same memory space, versus multiple processes each with completely separate memory](images/01_processes_vs_threads.png)

## What a Process Is

A process is an independent program instance managed by the operating system. Each process has:

- Its own memory space (variables, heap, stack)
- Its own Python interpreter
- Its own GIL (global interpreter lock)

Processes are isolated: a crash in one process does not affect others. Communication between processes requires explicit mechanisms (queues, pipes, shared memory).

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3Byb2Nlc3Nlc192c190aHJlYWRzIGNvZGUgMSIsImxhbmd1YWdlIjoiYmFzaCIsImZpbGVuYW1lIjoibWFpbl8wMDEuc2giLCJjb2RlIjoiIyBTdGFydCB0d28gc2VwYXJhdGUgUHl0aG9uIHByb2Nlc3NlczpcbnB5dGhvbiBzY3JpcHQxLnB5ICYgICAjIHByb2Nlc3MgMTogaXRzIG93biBtZW1vcnksIGl0cyBvd24gaW50ZXJwcmV0ZXJcbnB5dGhvbiBzY3JpcHQyLnB5ICYgICAjIHByb2Nlc3MgMjogY29tcGxldGVseSBzZXBhcmF0ZSJ9"
 width="100%"
></iframe>

## What a Thread Is

A thread is a unit of execution within a process. Multiple threads share the same memory space. They can read and write the same variables, lists, and objects directly.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3Byb2Nlc3Nlc192c190aHJlYWRzIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJpbXBvcnQgdGhyZWFkaW5nXG5cbmNvdW50ZXIgPSAwICAjIHNoYXJlZCBiZXR3ZWVuIHRocmVhZHNcblxuZGVmIGluY3JlbWVudCgpOlxuICAgIGdsb2JhbCBjb3VudGVyXG4gICAgY291bnRlciArPSAxXG5cbnQxID0gdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9aW5jcmVtZW50KVxudDIgPSB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1pbmNyZW1lbnQpXG50MS5zdGFydCgpOyB0Mi5zdGFydCgpXG50MS5qb2luKCk7IHQyLmpvaW4oKVxuIyBjb3VudGVyIG1pZ2h0IGJlIDEsIG5vdCAyIChyYWNlIGNvbmRpdGlvbiAtLSBleHBsYWluZWQgaW4gbGVzc29uIDQpIn0"
 width="100%"
></iframe>

## Python's GIL (Global Interpreter Lock)

The GIL is a mutex (lock) that allows only one thread to execute Python bytecode at any given moment, even on a multi-core machine. This is the critical constraint in Python threading.

What the GIL means:

- Python threads cannot execute CPU-bound code in true parallel on multiple cores
- Python threads CAN run concurrently during I/O waits (the GIL is released during I/O)
- For I/O-bound code, threading can speed things up
- For CPU-bound code, threading does NOT speed things up (and may be slightly slower)

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3Byb2Nlc3Nlc192c190aHJlYWRzIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJDUFUtYm91bmQgd2l0aCB0aHJlYWRzIChHSUwpOiAgICAgICAgICBJL08tYm91bmQgd2l0aCB0aHJlYWRzIChHSUwgcmVsZWFzZWQpOlxuVGhyZWFkIDE6IFs9PT09PVtHXVs9PT09PVtHXVs9PT09PV0gICAgVGhyZWFkIDE6IFtJL08gd2FpdC4uLl1bPT09XVtJL08gd2FpdC4uLl1cblRocmVhZCAyOiAgICAgIFtHXVs9PT09PVtHXVs9PT09PV0gICAgIFRocmVhZCAyOiBbPT09XVtJL08gd2FpdC4uLl1bPT09XVxuT25seSBvbmUgcnVucyBhdCBhIHRpbWUgICAgICAgICAgICAgICBCb3RoIHJ1biBkdXJpbmcgZWFjaCBvdGhlcidzIHdhaXRzIn0"
 width="100%"
></iframe>

## Processes Bypass the GIL

Each process has its own GIL. Multiple processes can run Python code on separate cores simultaneously, without any interference. This is why `multiprocessing` is the solution for CPU-bound parallel work.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3Byb2Nlc3Nlc192c190aHJlYWRzIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJDUFUtYm91bmQgd2l0aCBtdWx0aXByb2Nlc3Npbmc6XG5Qcm9jZXNzIDEgb24gQ1BVIDE6IFs9PT09PT09PT09PT09PT09PT09PT1dXG5Qcm9jZXNzIDIgb24gQ1BVIDI6IFs9PT09PT09PT09PT09PT09PT09PT1dXG5Qcm9jZXNzIDMgb24gQ1BVIDM6IFs9PT09PT09PT09PT09PT09PT09PT1dXG5BbGwgcnVuIHRydWx5IGluIHBhcmFsbGVsIn0"
 width="100%"
></iframe>

## The Decision Matrix

| Work type | Best tool | Why |
|---|---|---|
| I/O-bound, async-compatible libs | `asyncio` | Most efficient; single thread |
| I/O-bound, blocking libs | `threading` | GIL released during I/O waits |
| CPU-bound | `multiprocessing` | Each process has its own GIL |
| Mix of I/O and CPU | `asyncio` + `ProcessPoolExecutor` | Async for I/O, processes for CPU |

## Processes vs Threads at a Glance

| | Threads | Processes |
|---|---|---|
| Memory | Shared | Isolated |
| Communication | Direct (shared objects) | Queues, pipes, shared memory |
| Crash isolation | None | Yes |
| CPU parallelism in Python | No (GIL blocks) | Yes |
| I/O concurrency | Yes (GIL released) | Yes |
| Startup overhead | Low | Higher |

## Your Turn

Open two terminal windows. In each one, run `python -c "import os; print(os.getpid())"`. Observe that each command produces a different PID (process ID) -- they are separate processes.

Now run a Python script that creates two threads and prints their thread IDs:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3Byb2Nlc3Nlc192c190aHJlYWRzIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJpbXBvcnQgdGhyZWFkaW5nXG5cbmRlZiBzaG93X2lkKCk6XG4gICAgcHJpbnQoZlwiVGhyZWFkIElEOiB7dGhyZWFkaW5nLmdldF9pZGVudCgpfSwgUElEOiB7X19pbXBvcnRfXygnb3MnKS5nZXRwaWQoKX1cIilcblxudDEgPSB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1zaG93X2lkKVxudDIgPSB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1zaG93X2lkKVxudDEuc3RhcnQoKTsgdDIuc3RhcnQoKVxudDEuam9pbigpOyB0Mi5qb2luKClcbnNob3dfaWQoKSAgIyBtYWluIHRocmVhZCJ9"
 width="100%"
></iframe>

Observe that all three threads have the same PID but different thread IDs -- they share the same process.

## Conclusion

Processes are isolated units with separate memory and their own Python interpreter. Threads share memory within a process. Python's GIL prevents multiple threads from executing Python bytecode simultaneously, making threading useless for CPU-bound parallelism but still effective for I/O concurrency. Processes bypass the GIL and are the correct tool for CPU-bound parallel work. The next lesson shows how to use Python's `threading` module to create and manage threads.
