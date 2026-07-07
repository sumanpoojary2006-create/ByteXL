## Introduction

Yuna now has three concurrency tools in her toolkit: `asyncio`, `threading`, and `multiprocessing`. Each solves a different problem. In this final lesson, she builds the complete mental model: which tool for which job, how to profile to confirm the bottleneck, and how to combine tools for programs that have both I/O and CPU work.

![A flowchart decision tree: start with 'what is the bottleneck?' leading to I/O or CPU, then branching to async/threads/processes based on library availability and workload type](images/07_choosing_async_threads_processes.png)

## The Core Question: What Is the Bottleneck?

Profile first, choose second. The correct concurrency tool depends on whether the code is I/O-bound or CPU-bound. Do not guess.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2Nob29zaW5nX2FzeW5jX3RocmVhZHNfcHJvY2Vzc2VzIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJpbXBvcnQgY1Byb2ZpbGVcbmltcG9ydCBwc3RhdHNcblxuIyBQcm9maWxlIHRoZSBzbG93IGZ1bmN0aW9uOlxucHJvZmlsZXIgPSBjUHJvZmlsZS5Qcm9maWxlKClcbnByb2ZpbGVyLmVuYWJsZSgpXG5ydW5fc2xvd19waXBlbGluZSgpICAgIyB0aGUgY29kZSB0byBwcm9maWxlXG5wcm9maWxlci5kaXNhYmxlKClcblxuc3RhdHMgPSBwc3RhdHMuU3RhdHMocHJvZmlsZXIpXG5zdGF0cy5zb3J0X3N0YXRzKFwiY3VtdWxhdGl2ZVwiKVxuc3RhdHMucHJpbnRfc3RhdHMoMTApICAgIyB0b3AgMTAgc2xvd2VzdCBmdW5jdGlvbnMifQ"
 width="100%"
></iframe>

Look at the output: if most time is in `time.sleep`, network calls, or database operations, it is I/O-bound. If it is in computation functions, it is CPU-bound.

## The Decision Framework

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2Nob29zaW5nX2FzeW5jX3RocmVhZHNfcHJvY2Vzc2VzIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJXaGF0IGlzIHRoZSBib3R0bGVuZWNrP1xufFxuKy0tIEkvTyAobmV0d29yaywgZGF0YWJhc2UsIGRpc2spXG58ICAgICAgfFxufCAgICAgICstLSBDYW4gSSB1c2UgYXN5bmMtY29tcGF0aWJsZSBsaWJyYXJpZXMgKGFpb2h0dHAsIGFpb3NxbGl0ZSk_XG58ICAgICAgfCAgICAgIFlFUyAtPiBhc3luY2lvICsgYXN5bmMvYXdhaXQgKGJlc3Q6IHNpbmdsZSB0aHJlYWQsIG5vIG92ZXJoZWFkKVxufCAgICAgIHwgICAgICBOTyAgLT4gdGhyZWFkaW5nICsgVGhyZWFkUG9vbEV4ZWN1dG9yIChHSUwgcmVsZWFzZWQgZHVyaW5nIEkvTylcbnxcbistLSBDUFUgKGNvbXB1dGF0aW9uLCBpbWFnZSBwcm9jZXNzaW5nLCBkYXRhIGNydW5jaGluZylcbiAgICAgICB8XG4gICAgICAgKy0tIG11bHRpcHJvY2Vzc2luZyArIFByb2Nlc3NQb29sRXhlY3V0b3JcbiAgICAgICAgICAgKGVhY2ggcHJvY2VzcyBoYXMgaXRzIG93biBHSUw7IHRydWx5IHBhcmFsbGVsKVxuXG5NaXhlZCBJL08gKyBDUFU_XG4gIC0-IGFzeW5jaW8gZm9yIEkvTywgcnVuX2luX2V4ZWN1dG9yKFByb2Nlc3NQb29sRXhlY3V0b3IpIGZvciBDUFUifQ"
 width="100%"
></iframe>

## Side-by-Side Comparison

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2Nob29zaW5nX2FzeW5jX3RocmVhZHNfcHJvY2Vzc2VzIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJpbXBvcnQgYXN5bmNpb1xuaW1wb3J0IGNvbmN1cnJlbnQuZnV0dXJlc1xuaW1wb3J0IHRpbWVcblxuREFUQSA9IGxpc3QocmFuZ2UoMTAwMCkpXG5cbiMgLS0tIGFzeW5jaW86IGZvciBJL08tYm91bmQgd2l0aCBhc3luYyBsaWJzIC0tLVxuYXN5bmMgZGVmIGFzeW5jX3BpcGVsaW5lKGl0ZW1zKTpcbiAgICBhc3luYyBkZWYgZmV0Y2goaXRlbSk6XG4gICAgICAgIGF3YWl0IGFzeW5jaW8uc2xlZXAoMC4wMSkgICAjIHNpbXVsYXRlIG5ldHdvcmsgSS9PXG4gICAgICAgIHJldHVybiBpdGVtICogMlxuICAgIHJldHVybiBhd2FpdCBhc3luY2lvLmdhdGhlcigqW2ZldGNoKHgpIGZvciB4IGluIGl0ZW1zXSlcblxuIyAtLS0gdGhyZWFkaW5nOiBmb3IgSS9PLWJvdW5kIHdpdGggYmxvY2tpbmcgbGlicyAtLS1cbmRlZiB0aHJlYWRfcGlwZWxpbmUoaXRlbXMpOlxuICAgIGRlZiBmZXRjaChpdGVtKTpcbiAgICAgICAgdGltZS5zbGVlcCgwLjAxKSAgICMgYmxvY2tpbmcgSS9PXG4gICAgICAgIHJldHVybiBpdGVtICogMlxuICAgIHdpdGggY29uY3VycmVudC5mdXR1cmVzLlRocmVhZFBvb2xFeGVjdXRvcihtYXhfd29ya2Vycz0xMCkgYXMgZXg6XG4gICAgICAgIHJldHVybiBsaXN0KGV4Lm1hcChmZXRjaCwgaXRlbXMpKVxuXG4jIC0tLSBtdWx0aXByb2Nlc3Npbmc6IGZvciBDUFUtYm91bmQgLS0tXG5kZWYgY3B1X3dvcmsoaXRlbSk6XG4gICAgcmV0dXJuIHN1bShpICoqIDIgZm9yIGkgaW4gcmFuZ2UoaXRlbSAqIDEwKSlcblxuZGVmIHByb2Nlc3NfcGlwZWxpbmUoaXRlbXMpOlxuICAgIHdpdGggY29uY3VycmVudC5mdXR1cmVzLlByb2Nlc3NQb29sRXhlY3V0b3IoKSBhcyBleDpcbiAgICAgICAgcmV0dXJuIGxpc3QoZXgubWFwKGNwdV93b3JrLCBpdGVtcykpIn0"
 width="100%"
></iframe>

## Combining asyncio and ProcessPoolExecutor

For programs with both heavy I/O and heavy CPU, run async for I/O and offload CPU work to a process pool via `asyncio.run_in_executor`:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2Nob29zaW5nX2FzeW5jX3RocmVhZHNfcHJvY2Vzc2VzIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJpbXBvcnQgYXN5bmNpb1xuaW1wb3J0IGNvbmN1cnJlbnQuZnV0dXJlc1xuXG5kZWYgaGVhdnlfY3B1KHJlY29yZCk6XG4gICAgcmV0dXJuIHN1bShpICoqIDIgZm9yIGkgaW4gcmFuZ2UocmVjb3JkW1wic2l6ZVwiXSkpXG5cbmFzeW5jIGRlZiBwaXBlbGluZShyZWNvcmRzKTpcbiAgICBsb29wID0gYXN5bmNpby5nZXRfcnVubmluZ19sb29wKClcbiAgICBjcHVfcG9vbCA9IGNvbmN1cnJlbnQuZnV0dXJlcy5Qcm9jZXNzUG9vbEV4ZWN1dG9yKClcblxuICAgICMgSS9PIHBoYXNlOiBmZXRjaCBhbGwgcmVjb3JkcyBjb25jdXJyZW50bHkgKGFzeW5jKVxuICAgIGFzeW5jIGRlZiBmZXRjaChyKTpcbiAgICAgICAgYXdhaXQgYXN5bmNpby5zbGVlcCgwLjA1KSAgICMgc2ltdWxhdGUgbmV0d29ya1xuICAgICAgICByZXR1cm4gclxuXG4gICAgZmV0Y2hlZCA9IGF3YWl0IGFzeW5jaW8uZ2F0aGVyKCpbZmV0Y2gocikgZm9yIHIgaW4gcmVjb3Jkc10pXG5cbiAgICAjIENQVSBwaGFzZTogcHJvY2VzcyByZWNvcmRzIGluIHBhcmFsbGVsIHByb2Nlc3Nlc1xuICAgIHJlc3VsdHMgPSBhd2FpdCBhc3luY2lvLmdhdGhlcigqW1xuICAgICAgICBsb29wLnJ1bl9pbl9leGVjdXRvcihjcHVfcG9vbCwgaGVhdnlfY3B1LCByKVxuICAgICAgICBmb3IgciBpbiBmZXRjaGVkXG4gICAgXSlcbiAgICBjcHVfcG9vbC5zaHV0ZG93bigpXG4gICAgcmV0dXJuIHJlc3VsdHNcblxuaWYgX19uYW1lX18gPT0gXCJfX21haW5fX1wiOlxuICAgIHJlY29yZHMgPSBbe1wic2l6ZVwiOiAxMF8wMDAsIFwiaWRcIjogaX0gZm9yIGkgaW4gcmFuZ2UoMjApXVxuICAgIHJlc3VsdHMgPSBhc3luY2lvLnJ1bihwaXBlbGluZShyZWNvcmRzKSlcbiAgICBwcmludChmXCJEb25lOiB7bGVuKHJlc3VsdHMpfSByZXN1bHRzXCIpIn0"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2Nob29zaW5nX2FzeW5jX3RocmVhZHNfcHJvY2Vzc2VzIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJpbXBvcnQgdGltZVxuXG5kZWYgcnVuX3Nsb3dfcGlwZWxpbmUoKTpcbiAgICByZWNvcmRzID0gW11cbiAgICBmb3IgaSBpbiByYW5nZSgxMDApOlxuICAgICAgICB0aW1lLnNsZWVwKDAuMDEpICAgIyBJL08gYm90dGxlbmVjazogc2ltdWxhdGUgZmV0Y2hpbmdcbiAgICAgICAgcmVjb3Jkcy5hcHBlbmQoc3VtKGogKiogMiBmb3IgaiBpbiByYW5nZShpICogMTApKSkgICAjIENQVSB3b3JrXG4gICAgcmV0dXJuIHJlY29yZHNcblxuc3RhcnQgPSB0aW1lLnBlcmZfY291bnRlcigpXG5ydW5fc2xvd19waXBlbGluZSgpXG5wcmludChmXCJCYXNlbGluZToge3RpbWUucGVyZl9jb3VudGVyKCkgLSBzdGFydDouMmZ9c1wiKSJ9"
 width="100%"
></iframe>

Then rewrite with `ThreadPoolExecutor` for the I/O phase and `ProcessPoolExecutor` for the CPU phase.

## Conclusion

Profile before choosing a concurrency tool. `asyncio` is the right choice for I/O-bound code with async-compatible libraries. `ThreadPoolExecutor` handles I/O-bound code with blocking libraries. `ProcessPoolExecutor` handles CPU-bound parallelism. Combining asyncio with `run_in_executor(ProcessPoolExecutor)` handles programs with both I/O and CPU bottlenecks. Unit 12 moves from performance to usability: building command-line interfaces that make the library system accessible to non-programmers.
