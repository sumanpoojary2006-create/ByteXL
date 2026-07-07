## Introduction

Yuna's indexing job is not just CPU work -- it also reads book records from the database (I/O) and updates a search index via an API (I/O). The CPU-bound part is one step; the I/O steps are the bottleneck in the first pass. Threads can help here: while one thread waits for a database response, another can process records already downloaded.

This lesson covers the `threading` module: creating threads, passing arguments, joining (waiting for completion), and using daemon threads.

![A diagram showing five threads created from the main thread, each running an I/O operation concurrently, and the main thread calling join to wait for all of them to complete](images/02_threading_module.png)

## Creating and Starting a Thread

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3RocmVhZGluZ19tb2R1bGUgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6ImltcG9ydCB0aHJlYWRpbmdcbmltcG9ydCB0aW1lXG5cbmRlZiBpbmRleF9iYXRjaChiYXRjaF9pZCwgcmVjb3Jkcyk6XG4gICAgcHJpbnQoZlwiVGhyZWFkIHtiYXRjaF9pZH06IHN0YXJ0aW5nIHtsZW4ocmVjb3Jkcyl9IHJlY29yZHNcIilcbiAgICB0aW1lLnNsZWVwKDAuNSkgICAjIHNpbXVsYXRlIEkvTyAoZGF0YWJhc2UgcmVhZCArIEFQSSB3cml0ZSlcbiAgICBwcmludChmXCJUaHJlYWQge2JhdGNoX2lkfTogZG9uZVwiKVxuXG5yZWNvcmRzID0gbGlzdChyYW5nZSgxMDApKSAgICMgc2ltdWxhdGUgMTAwIHJlY29yZHNcbmJhdGNoZXMgPSBbcmVjb3Jkc1tpOmkrMjBdIGZvciBpIGluIHJhbmdlKDAsIDEwMCwgMjApXSAgICMgNSBiYXRjaGVzIG9mIDIwXG5cbnRocmVhZHMgPSBbXVxuZm9yIGksIGJhdGNoIGluIGVudW1lcmF0ZShiYXRjaGVzKTpcbiAgICB0ID0gdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9aW5kZXhfYmF0Y2gsIGFyZ3M9KGksIGJhdGNoKSlcbiAgICB0aHJlYWRzLmFwcGVuZCh0KVxuICAgIHQuc3RhcnQoKVxuXG4jIFdhaXQgZm9yIGFsbCB0aHJlYWRzIHRvIGNvbXBsZXRlOlxuZm9yIHQgaW4gdGhyZWFkczpcbiAgICB0LmpvaW4oKVxuXG5wcmludChcIkFsbCBiYXRjaGVzIGluZGV4ZWRcIikifQ"
 width="100%"
></iframe>

`threading.Thread(target=fn, args=(arg1, arg2))` creates a thread. `t.start()` starts it. `t.join()` blocks the calling thread until `t` finishes.

## Thread Arguments

The `args` parameter is a tuple of positional arguments; `kwargs` is a dict of keyword arguments:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3RocmVhZGluZ19tb2R1bGUgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6ImRlZiBwcm9jZXNzKHJlY29yZF9pZCwgKiwgcHJpb3JpdHk9XCJub3JtYWxcIik6XG4gICAgcHJpbnQoZlwiUHJvY2Vzc2luZyB7cmVjb3JkX2lkfSBhdCB7cHJpb3JpdHl9IHByaW9yaXR5XCIpXG5cbnQgPSB0aHJlYWRpbmcuVGhyZWFkKFxuICAgIHRhcmdldD1wcm9jZXNzLFxuICAgIGFyZ3M9KDQyLCksXG4gICAga3dhcmdzPXtcInByaW9yaXR5XCI6IFwiaGlnaFwifVxuKVxudC5zdGFydCgpXG50LmpvaW4oKSJ9"
 width="100%"
></iframe>

## threading.current_thread and Names

Threads can be named for easier debugging:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3RocmVhZGluZ19tb2R1bGUgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6ImltcG9ydCB0aHJlYWRpbmdcblxuZGVmIHdvcmtlcigpOlxuICAgIG5hbWUgPSB0aHJlYWRpbmcuY3VycmVudF90aHJlYWQoKS5uYW1lXG4gICAgcHJpbnQoZlwiUnVubmluZyBpbiB0aHJlYWQ6IHtuYW1lfVwiKVxuXG50ID0gdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9d29ya2VyLCBuYW1lPVwiaW5kZXhlci0xXCIpXG50LnN0YXJ0KClcbnQuam9pbigpXG4jIFJ1bm5pbmcgaW4gdGhyZWFkOiBpbmRleGVyLTFcblxuIyBUaGUgbWFpbiB0aHJlYWQ6XG5wcmludCh0aHJlYWRpbmcuY3VycmVudF90aHJlYWQoKS5uYW1lKSAgICMgTWFpblRocmVhZFxucHJpbnQodGhyZWFkaW5nLmFjdGl2ZV9jb3VudCgpKSAgICAgICAgICAjIG51bWJlciBvZiB0aHJlYWRzIGN1cnJlbnRseSBhbGl2ZSJ9"
 width="100%"
></iframe>

## Daemon Threads

A daemon thread is a background thread that is automatically killed when the main thread exits, without requiring `join()`. Use it for background tasks that should not prevent the program from exiting.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3RocmVhZGluZ19tb2R1bGUgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6ImltcG9ydCB0aHJlYWRpbmdcbmltcG9ydCB0aW1lXG5cbmRlZiBoZWFydGJlYXQoKTpcbiAgICB3aGlsZSBUcnVlOlxuICAgICAgICBwcmludChcIkxpYnJhcnkgc3lzdGVtOiBhbGl2ZVwiKVxuICAgICAgICB0aW1lLnNsZWVwKDYwKVxuXG4jIERhZW1vbjoga2lsbGVkIHdoZW4gbWFpbiB0aHJlYWQgZXhpdHNcbm1vbml0b3IgPSB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1oZWFydGJlYXQsIGRhZW1vbj1UcnVlKVxubW9uaXRvci5zdGFydCgpXG5cbiMgTWFpbiB3b3JrOlxuaW5kZXhfY2F0YWxvZygpXG4jIFdoZW4gdGhpcyByZXR1cm5zLCB0aGUgZGFlbW9uIHRocmVhZCBpcyBhbHNvIGtpbGxlZCAtLSBubyBuZWVkIHRvIHN0b3AgaXQifQ"
 width="100%"
></iframe>

Non-daemon threads (the default) keep the program alive until they finish. If you forget to `join()` a non-daemon thread, the program will not exit until it completes.

## Thread Subclass Pattern

For threads that need more state, subclass `Thread` and override `run()`:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3RocmVhZGluZ19tb2R1bGUgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6ImltcG9ydCB0aHJlYWRpbmdcblxuY2xhc3MgSW5kZXhlclRocmVhZCh0aHJlYWRpbmcuVGhyZWFkKTpcbiAgICBkZWYgX19pbml0X18oc2VsZiwgYmF0Y2hfaWQsIHJlY29yZHMpOlxuICAgICAgICBzdXBlcigpLl9faW5pdF9fKG5hbWU9ZlwiaW5kZXhlci17YmF0Y2hfaWR9XCIpXG4gICAgICAgIHNlbGYuYmF0Y2hfaWQgPSBiYXRjaF9pZFxuICAgICAgICBzZWxmLnJlY29yZHMgPSByZWNvcmRzXG4gICAgICAgIHNlbGYuaW5kZXhlZF9jb3VudCA9IDBcblxuICAgIGRlZiBydW4oc2VsZik6XG4gICAgICAgIGZvciByZWNvcmQgaW4gc2VsZi5yZWNvcmRzOlxuICAgICAgICAgICAgc2VsZi5pbmRleF9yZWNvcmQocmVjb3JkKVxuICAgICAgICAgICAgc2VsZi5pbmRleGVkX2NvdW50ICs9IDFcbiAgICAgICAgcHJpbnQoZlwiQmF0Y2gge3NlbGYuYmF0Y2hfaWR9OiBpbmRleGVkIHtzZWxmLmluZGV4ZWRfY291bnR9IHJlY29yZHNcIilcblxuICAgIGRlZiBpbmRleF9yZWNvcmQoc2VsZiwgcmVjb3JkKTpcbiAgICAgICAgaW1wb3J0IHRpbWVcbiAgICAgICAgdGltZS5zbGVlcCgwLjAwMSkgICAjIHNpbXVsYXRlIEkvT1xuXG50aHJlYWRzID0gW0luZGV4ZXJUaHJlYWQoaSwgYmF0Y2gpIGZvciBpLCBiYXRjaCBpbiBlbnVtZXJhdGUoYmF0Y2hlcyldXG5mb3IgdCBpbiB0aHJlYWRzOlxuICAgIHQuc3RhcnQoKVxuZm9yIHQgaW4gdGhyZWFkczpcbiAgICB0LmpvaW4oKVxuXG50b3RhbCA9IHN1bSh0LmluZGV4ZWRfY291bnQgZm9yIHQgaW4gdGhyZWFkcylcbnByaW50KGZcIlRvdGFsIGluZGV4ZWQ6IHt0b3RhbH1cIikifQ"
 width="100%"
></iframe>

## The threading Module at a Glance

| Feature | What it does |
|---|---|
| `threading.Thread(target, args)` | Create a thread |
| `t.start()` | Start the thread |
| `t.join()` | Wait for the thread to finish |
| `t.daemon = True` | Mark as daemon (killed on main exit) |
| `threading.current_thread()` | The current thread object |
| `threading.active_count()` | Number of live threads |

## Your Turn

Write a function `parallel_download(urls)` that downloads all URLs concurrently using threads and returns a list of response texts:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3RocmVhZGluZ19tb2R1bGUgY29kZSA2IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA2LnB5IiwiY29kZSI6ImltcG9ydCB0aHJlYWRpbmdcbmltcG9ydCB1cmxsaWIucmVxdWVzdFxuXG5kZWYgcGFyYWxsZWxfZG93bmxvYWQodXJscyk6XG4gICAgcmVzdWx0cyA9IFtOb25lXSAqIGxlbih1cmxzKVxuXG4gICAgZGVmIGRvd25sb2FkKGluZGV4LCB1cmwpOlxuICAgICAgICB3aXRoIHVybGxpYi5yZXF1ZXN0LnVybG9wZW4odXJsKSBhcyByZXNwOlxuICAgICAgICAgICAgcmVzdWx0c1tpbmRleF0gPSByZXNwLnJlYWQoKS5kZWNvZGUoKVxuXG4gICAgdGhyZWFkcyA9IFtcbiAgICAgICAgdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9ZG93bmxvYWQsIGFyZ3M9KGksIHVybCkpXG4gICAgICAgIGZvciBpLCB1cmwgaW4gZW51bWVyYXRlKHVybHMpXG4gICAgXVxuICAgIGZvciB0IGluIHRocmVhZHM6XG4gICAgICAgIHQuc3RhcnQoKVxuICAgIGZvciB0IGluIHRocmVhZHM6XG4gICAgICAgIHQuam9pbigpXG4gICAgcmV0dXJuIHJlc3VsdHMifQ"
 width="100%"
></iframe>

Note that `results[index] = ...` is used instead of `results.append(...)` to avoid ordering problems when threads finish in different orders.

## Conclusion

`threading.Thread` creates threads; `start()` launches them; `join()` waits for them. Daemon threads are killed when the main thread exits. For I/O-bound work, threads run concurrently because the GIL is released during I/O waits. The next lesson explains the GIL in depth and why it means threads cannot be used for CPU-bound parallelism.
