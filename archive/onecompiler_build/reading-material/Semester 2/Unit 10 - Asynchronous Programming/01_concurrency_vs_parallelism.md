## Introduction

Miguel is building a book availability checker for the library portal. For each request, the system queries three partner libraries: it asks each one whether they have the requested book available. He wrote the code to call the first library, wait for its response, call the second, wait, call the third, wait. Three calls, three waits, one after the other. The total time per request is the sum of all three wait times.

His teammate asks why he is not calling all three at once. Miguel does not know how, and he is confused by two terms his teammate uses interchangeably: "async" and "parallel." They sound similar but mean different things.

![A timeline showing sequential API calls on the top row -- three calls in series with each wait following the previous -- and concurrent async calls on the bottom -- all three calls started at the same time, overlapping, finishing faster](images/01_concurrency_vs_parallelism.png)

## The Waiting Problem

Most network calls spend the majority of their time waiting: waiting for a DNS lookup, waiting for a TCP connection, waiting for the server to respond, waiting for data to travel over the wire. During this waiting time, the CPU is idle. The program is not doing anything useful.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX2NvbmN1cnJlbmN5X3ZzX3BhcmFsbGVsaXNtIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiIjIFNlcXVlbnRpYWw6IGVhY2ggY2FsbCB3YWl0cyBmb3IgdGhlIHByZXZpb3VzIG9uZSB0byBjb21wbGV0ZVxuaW1wb3J0IHJlcXVlc3RzXG5cbmRlZiBjaGVja19hdmFpbGFiaWxpdHlfc2VxdWVudGlhbChpc2JuKTpcbiAgICByMSA9IHJlcXVlc3RzLmdldChmXCJodHRwczovL2xpYnJhcnkxLmV4YW1wbGUuY29tL2Jvb2tzL3tpc2JufVwiKVxuICAgIHIyID0gcmVxdWVzdHMuZ2V0KGZcImh0dHBzOi8vbGlicmFyeTIuZXhhbXBsZS5jb20vYm9va3Mve2lzYm59XCIpXG4gICAgcjMgPSByZXF1ZXN0cy5nZXQoZlwiaHR0cHM6Ly9saWJyYXJ5My5leGFtcGxlLmNvbS9ib29rcy97aXNibn1cIilcbiAgICByZXR1cm4gW3IxLmpzb24oKSwgcjIuanNvbigpLCByMy5qc29uKCldXG4jIFRvdGFsIHRpbWUgPSB0aW1lKHIxKSArIHRpbWUocjIpICsgdGltZShyMylcbiMgSWYgZWFjaCB0YWtlcyA1MDBtczogdG90YWwgPSAxNTAwbXMifQ"
 width="100%"
></iframe>

The program could be doing something useful (like sending the next request) while waiting for the first response.

## Concurrency vs Parallelism

**Parallelism** means two things actually happen at the same moment. Two CPU cores each execute a line of Python code at the same instant. This requires multiple CPU cores.

**Concurrency** means multiple things are *in progress* at the same time, but not necessarily executing at the same instant. One thing pauses while waiting (e.g., for a network response), and another thing runs while the first is paused. A single CPU handles both, switching between them.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX2NvbmN1cnJlbmN5X3ZzX3BhcmFsbGVsaXNtIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJQYXJhbGxlbGlzbSAocmVxdWlyZXMgbXVsdGlwbGUgQ1BVcyk6XG5UaHJlYWQgMSBvbiBDUFUgMTogWz09PT09PT1dXG5UaHJlYWQgMiBvbiBDUFUgMjogWz09PT09PT1dXG5Cb3RoIHJ1biBhdCBleGFjdGx5IHRoZSBzYW1lIHRpbWVcblxuQ29uY3VycmVuY3kgKHNpbmdsZSBDUFUpOlxuVGFzayAxOiBbPT09XVt3YWl0aW5nLi4uXVs9PT1kb25lXVxuVGFzayAyOiAgICAgIFs9PT09PT09ZG9uZV1cblRhc2sgMiBydW5zIGR1cmluZyBUYXNrIDEncyB3YWl0IHBlcmlvZCJ9"
 width="100%"
></iframe>

Async programming in Python is about **concurrency**, not parallelism. A single Python thread handles many operations by switching between them whenever one is waiting for I/O.

## I/O-Bound vs CPU-Bound Work

The distinction matters for choosing the right tool:

**I/O-bound**: the bottleneck is waiting for input/output (network, disk, database). The CPU is fast but idle, waiting. Async and threading are both effective here.

**CPU-bound**: the bottleneck is computation. The CPU is busy. Async does not help because there is no waiting to overlap. Multiprocessing is needed.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX2NvbmN1cnJlbmN5X3ZzX3BhcmFsbGVsaXNtIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJJL08tYm91bmQgKGFzeW5jIGhlbHBzKTpcbi0gSFRUUCByZXF1ZXN0cyB0byBleHRlcm5hbCBBUElzXG4tIERhdGFiYXNlIHF1ZXJpZXNcbi0gUmVhZGluZyBsYXJnZSBmaWxlcyBmcm9tIGRpc2tcbi0gV2FpdGluZyBmb3IgdXNlciBpbnB1dFxuXG5DUFUtYm91bmQgKGFzeW5jIGRvZXMgTk9UIGhlbHApOlxuLSBJbWFnZSBwcm9jZXNzaW5nXG4tIE1hY2hpbmUgbGVhcm5pbmcgaW5mZXJlbmNlXG4tIFNvcnRpbmcgbWlsbGlvbnMgb2YgcmVjb3Jkc1xuLSBQYXJzaW5nIGxhcmdlIFhNTCBmaWxlcyJ9"
 width="100%"
></iframe>

## Python's asyncio Model

Python's `asyncio` module implements cooperative concurrency: tasks explicitly yield control (via `await`) when they are waiting for I/O. The event loop then runs another task while the first is waiting.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX2NvbmN1cnJlbmN5X3ZzX3BhcmFsbGVsaXNtIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJpbXBvcnQgYXN5bmNpb1xuaW1wb3J0IGFpb2h0dHAgICAjIGFzeW5jLWNvbXBhdGlibGUgSFRUUCBsaWJyYXJ5XG5cbmFzeW5jIGRlZiBjaGVja19hdmFpbGFiaWxpdHlfY29uY3VycmVudChpc2JuKTpcbiAgICBhc3luYyB3aXRoIGFpb2h0dHAuQ2xpZW50U2Vzc2lvbigpIGFzIHNlc3Npb246XG4gICAgICAgIHRhc2tzID0gW1xuICAgICAgICAgICAgc2Vzc2lvbi5nZXQoZlwiaHR0cHM6Ly9saWJyYXJ5MS5leGFtcGxlLmNvbS9ib29rcy97aXNibn1cIiksXG4gICAgICAgICAgICBzZXNzaW9uLmdldChmXCJodHRwczovL2xpYnJhcnkyLmV4YW1wbGUuY29tL2Jvb2tzL3tpc2JufVwiKSxcbiAgICAgICAgICAgIHNlc3Npb24uZ2V0KGZcImh0dHBzOi8vbGlicmFyeTMuZXhhbXBsZS5jb20vYm9va3Mve2lzYm59XCIpLFxuICAgICAgICBdXG4gICAgICAgIHJlc3BvbnNlcyA9IGF3YWl0IGFzeW5jaW8uZ2F0aGVyKCp0YXNrcykgICAjIHJ1biBhbGwgdGhyZWUgY29uY3VycmVudGx5XG4gICAgICAgIHJldHVybiBbYXdhaXQgci5qc29uKCkgZm9yIHIgaW4gcmVzcG9uc2VzXVxuIyBUb3RhbCB0aW1lIOKJiCBtYXgodGltZShyMSksIHRpbWUocjIpLCB0aW1lKHIzKSlcbiMgSWYgZWFjaCB0YWtlcyA1MDBtczogdG90YWwg4omIIDUwMG1zIn0"
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
