## Introduction

Miguel is building a book availability checker for the library portal. For each request, the system queries three partner libraries: it asks each one whether they have the requested book available. He wrote the code to call the first library, wait for its response, call the second, wait, call the third, wait. Three calls, three waits, one after the other. The total time per request is the sum of all three wait times.

His teammate asks why he is not calling all three at once. Miguel does not know how, and he is confused by two terms his teammate uses interchangeably: "async" and "parallel." They sound similar but mean different things.

![A timeline showing sequential API calls on the top row -- three calls in series with each wait following the previous -- and concurrent async calls on the bottom -- all three calls started at the same time, overlapping, finishing faster](images/01_concurrency_vs_parallelism.png)

## The Waiting Problem

Most network calls spend the majority of their time waiting: waiting for a DNS lookup, waiting for a TCP connection, waiting for the server to respond, waiting for data to travel over the wire. During this waiting time, the CPU is idle. The program is not doing anything useful.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-01-concurrency-vs-parallelism-001-dde921f6d0.html"
 width="100%"
></iframe>

The program could be doing something useful (like sending the next request) while waiting for the first response.

## Concurrency vs Parallelism

**Parallelism** means two things actually happen at the same moment. Two CPU cores each execute a line of Python code at the same instant. This requires multiple CPU cores.

**Concurrency** means multiple things are *in progress* at the same time, but not necessarily executing at the same instant. One thing pauses while waiting (e.g., for a network response), and another thing runs while the first is paused. A single CPU handles both, switching between them.

```
Parallelism (requires multiple CPUs):
Thread 1 on CPU 1: [=======]
Thread 2 on CPU 2: [=======]
Both run at exactly the same time

Concurrency (single CPU):
Task 1: [===][waiting...][===done]
Task 2:      [=======done]
Task 2 runs during Task 1's wait period
```

Async programming in Python is about **concurrency**, not parallelism. A single Python thread handles many operations by switching between them whenever one is waiting for I/O.

## I/O-Bound vs CPU-Bound Work

The distinction matters for choosing the right tool:

**I/O-bound**: the bottleneck is waiting for input/output (network, disk, database). The CPU is fast but idle, waiting. Async and threading are both effective here.

**CPU-bound**: the bottleneck is computation. The CPU is busy. Async does not help because there is no waiting to overlap. Multiprocessing is needed.

```
I/O-bound (async helps):
- HTTP requests to external APIs
- Database queries
- Reading large files from disk
- Waiting for user input

CPU-bound (async does NOT help):
- Image processing
- Machine learning inference
- Sorting millions of records
- Parsing large XML files
```

## Python's asyncio Model

Python's `asyncio` module implements cooperative concurrency: tasks explicitly yield control (via `await`) when they are waiting for I/O. The event loop then runs another task while the first is waiting.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-01-concurrency-vs-parallelism-002-3375428767.html"
 width="100%"
></iframe>

Three calls, one wait period (the longest of the three), total time reduced from 1500ms to approximately 500ms.

## Concurrency vs Parallelism at a Glance

| Concept | What it means |
|---|---|
| Parallelism | Multiple things run at the exact same instant (requires multiple CPUs) |
| Concurrency | Multiple things are in progress; one runs while another waits |
| I/O-bound | Bottleneck is waiting; async/threading helps |
| CPU-bound | Bottleneck is computation; multiprocessing helps |
| `asyncio` | Python's cooperative concurrency model |
| `await` | Yield control to the event loop while waiting for I/O |

## Your Turn

Draw a timeline for these two scenarios:

**Sequential**: three HTTP requests, each taking 200ms, called one after the other. How long does the total take?

**Concurrent**: the same three requests, started at the same time. How long does the total take if they all take 200ms?

Now imagine one request takes 500ms and the other two take 100ms each. What is the total time in each approach? Which one benefits more from concurrency when request times are unequal?

## Conclusion

Concurrency is not the same as parallelism. Async programming is about managing the waiting time in I/O-bound code by running other tasks while one is paused. Python's `asyncio` implements this through an event loop that switches between tasks at `await` points. The next lesson explains exactly what "blocking" vs "non-blocking" means, and why using a blocking library inside an async function defeats the purpose.
