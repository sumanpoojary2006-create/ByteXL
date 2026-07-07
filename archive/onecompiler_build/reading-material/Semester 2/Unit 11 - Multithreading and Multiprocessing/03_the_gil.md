## Introduction

Yuna tried threading for the CPU-intensive part of her indexing job (computing TF-IDF vectors) and found it ran at almost the same speed as single-threaded code, sometimes slower. She expected 4 threads to run 4x faster on a 4-core machine. Her team lead explains: this is the GIL, and it is why Python threads cannot parallelize CPU-bound work.

Understanding the GIL helps you avoid a common mistake: reaching for threads when you need processes, and wasting days debugging a performance regression.

![A diagram showing two CPU cores: with the GIL, one is always blocked (gray) while the other runs Python code (green), resulting in only one core ever active at a time despite having two threads](images/03_the_gil.png)

## What the GIL Is

The GIL (Global Interpreter Lock) is a mutex built into CPython (the reference Python implementation). It ensures that only one thread executes Python bytecode at any given moment. It was designed to protect Python's internal reference-counting garbage collector from concurrent modification, which would corrupt memory.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3RoZV9naWwgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6IldpdGhvdXQgR0lMIChub3QgUHl0aG9uKTpcbkNQVSAxOiBUaHJlYWQgQTogWz09PVB5dGhvbiBjb2RlPT09XVs9PT1QeXRob24gY29kZT09PV1cbkNQVSAyOiBUaHJlYWQgQjogWz09PVB5dGhvbiBjb2RlPT09XVs9PT1QeXRob24gY29kZT09PV1cbkJvdGggcnVuIHNpbXVsdGFuZW91c2x5OiAyeCB0aHJvdWdocHV0XG5cbldpdGggR0lMIChDUHl0aG9uKTpcbkNQVSAxOiBUaHJlYWQgQTogWz09PVB5dGhvbiBjb2RlPT09XVtHSUwgd2FpdC4uLi4uLi4uLi5dWz09PVB5dGhvbiBjb2RlPT09XVxuQ1BVIDI6IFRocmVhZCBCOiBbR0lMIHdhaXQuLi4uLi4uLi4uXVs9PT1QeXRob24gY29kZT09PV1bR0lMIHdhaXQuLi4uLi4uLi4uXVxuT25lIHJ1bnMgYXQgYSB0aW1lOiBubyBpbXByb3ZlbWVudCwgY29udGV4dC1zd2l0Y2ggb3ZlcmhlYWQifQ"
 width="100%"
></iframe>

## The GIL and I/O

The GIL is released whenever a thread performs I/O (network, disk, `time.sleep`). During I/O, the thread is not executing Python bytecode, so there is nothing to protect. Another thread acquires the GIL and runs.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3RoZV9naWwgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6ImltcG9ydCB0aHJlYWRpbmdcbmltcG9ydCB0aW1lXG5cbiMgSS9PLWJvdW5kOiBHSUwgaXMgcmVsZWFzZWQgZHVyaW5nIHNsZWVwXG5kZWYgaW9fd29ya2VyKG5hbWUpOlxuICAgIHRpbWUuc2xlZXAoMSkgICAjIEdJTCByZWxlYXNlZCBoZXJlOiBvdGhlciB0aHJlYWRzIHJ1biBkdXJpbmcgdGhpcyBzZWNvbmRcbiAgICBwcmludChmXCJ7bmFtZX0gZG9uZVwiKVxuXG4jIFdpdGggdGhyZWFkcyAoR0lMIHJlbGVhc2VkIGR1cmluZyBJL08pOlxudDEgPSB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1pb193b3JrZXIsIGFyZ3M9KFwiVDFcIiwpKVxudDIgPSB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1pb193b3JrZXIsIGFyZ3M9KFwiVDJcIiwpKVxudDEuc3RhcnQoKTsgdDIuc3RhcnQoKVxudDEuam9pbigpOyB0Mi5qb2luKClcbiMgVG90YWw6IOKJiCAxIHNlY29uZCAoY29uY3VycmVudCBJL08gd2FpdHMpXG5cbiMgQ1BVLWJvdW5kOiBHSUwgaXMgTk9UIHJlbGVhc2VkXG5kZWYgY3B1X3dvcmtlcihuKTpcbiAgICBmb3IgXyBpbiByYW5nZShuKTpcbiAgICAgICAgcGFzcyAgICMgcHVyZSBjb21wdXRhdGlvbiAtLSBHSUwgaGVsZCB0aGUgZW50aXJlIHRpbWVcblxudDEgPSB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1jcHVfd29ya2VyLCBhcmdzPSgxMF8wMDBfMDAwLCkpXG50MiA9IHRocmVhZGluZy5UaHJlYWQodGFyZ2V0PWNwdV93b3JrZXIsIGFyZ3M9KDEwXzAwMF8wMDAsKSlcbnQxLnN0YXJ0KCk7IHQyLnN0YXJ0KClcbnQxLmpvaW4oKTsgdDIuam9pbigpXG4jIFRvdGFsOiDiiYggMnggdGhlIHNpbmdsZS10aHJlYWRlZCB0aW1lIChHSUwgY29udGVudGlvbiBvdmVyaGVhZCkifQ"
 width="100%"
></iframe>

## Measuring the GIL Effect

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3RoZV9naWwgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6ImltcG9ydCB0aHJlYWRpbmdcbmltcG9ydCB0aW1lXG5cbmRlZiBjb3VudChuKTpcbiAgICBmb3IgXyBpbiByYW5nZShuKTpcbiAgICAgICAgcGFzc1xuXG5OID0gNTBfMDAwXzAwMFxuXG4jIFNpbmdsZS10aHJlYWRlZDpcbnN0YXJ0ID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuY291bnQoTilcbnByaW50KGZcIlNpbmdsZS10aHJlYWRlZDoge3RpbWUucGVyZl9jb3VudGVyKCkgLSBzdGFydDouMmZ9c1wiKVxuXG4jIFR3byB0aHJlYWRzIChDUFUtYm91bmQpOlxuc3RhcnQgPSB0aW1lLnBlcmZfY291bnRlcigpXG50MSA9IHRocmVhZGluZy5UaHJlYWQodGFyZ2V0PWNvdW50LCBhcmdzPShOIC8vIDIsKSlcbnQyID0gdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9Y291bnQsIGFyZ3M9KE4gLy8gMiwpKVxudDEuc3RhcnQoKTsgdDIuc3RhcnQoKVxudDEuam9pbigpOyB0Mi5qb2luKClcbnByaW50KGZcIlR3byB0aHJlYWRzOiAgICAge3RpbWUucGVyZl9jb3VudGVyKCkgLSBzdGFydDouMmZ9c1wiKVxuIyBUd28gdGhyZWFkcyB0YWtlIHJvdWdobHkgdGhlIHNhbWUgdGltZSBhcyBzaW5nbGUtdGhyZWFkZWQsIG9yIHNsaWdodGx5IG1vcmUifQ"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3RoZV9naWwgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6ImltcG9ydCB0aHJlYWRpbmdcbmltcG9ydCB0aW1lXG5cbmRlZiBjcHVfdGFzayhuKTpcbiAgICByZXR1cm4gc3VtKHJhbmdlKG4pKVxuXG5kZWYgaW9fdGFzayhkZWxheSk6XG4gICAgdGltZS5zbGVlcChkZWxheSlcbiAgICByZXR1cm4gZGVsYXlcblxuTiA9IDEwXzAwMF8wMDBcbkRFTEFZID0gMS4wXG5cbiMgU2NlbmFyaW8gMTogc2luZ2xlLXRocmVhZGVkIENQVVxuc3RhcnQgPSB0aW1lLnBlcmZfY291bnRlcigpXG5jcHVfdGFzayhOKTsgY3B1X3Rhc2soTilcbnByaW50KGZcIkNQVSBzaW5nbGU6IHt0aW1lLnBlcmZfY291bnRlcigpIC0gc3RhcnQ6LjJmfXNcIilcblxuIyBTY2VuYXJpbyAyOiB0d28gdGhyZWFkcyBDUFVcbnN0YXJ0ID0gdGltZS5wZXJmX2NvdW50ZXIoKVxudDEgPSB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1jcHVfdGFzaywgYXJncz0oTiwpKVxudDIgPSB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1jcHVfdGFzaywgYXJncz0oTiwpKVxudDEuc3RhcnQoKTsgdDIuc3RhcnQoKTsgdDEuam9pbigpOyB0Mi5qb2luKClcbnByaW50KGZcIkNQVSB0aHJlYWRzOiB7dGltZS5wZXJmX2NvdW50ZXIoKSAtIHN0YXJ0Oi4yZn1zXCIpXG5cbiMgU2NlbmFyaW8gMzogdHdvIHRocmVhZHMgSS9PXG5zdGFydCA9IHRpbWUucGVyZl9jb3VudGVyKClcbnQxID0gdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9aW9fdGFzaywgYXJncz0oREVMQVksKSlcbnQyID0gdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9aW9fdGFzaywgYXJncz0oREVMQVksKSlcbnQxLnN0YXJ0KCk7IHQyLnN0YXJ0KCk7IHQxLmpvaW4oKTsgdDIuam9pbigpXG5wcmludChmXCJJL08gdGhyZWFkczoge3RpbWUucGVyZl9jb3VudGVyKCkgLSBzdGFydDouMmZ9c1wiKSJ9"
 width="100%"
></iframe>

Compare scenarios 1-2 (threads do not help for CPU) and scenario 3 (threads do help for I/O).

## Conclusion

The GIL ensures only one thread executes Python bytecode at a time. For I/O-bound work, threads are effective because the GIL is released during I/O. For CPU-bound work, threads do not help and may be slower due to contention. The correct tool for CPU-bound parallelism is multiprocessing, where each process has its own GIL.
