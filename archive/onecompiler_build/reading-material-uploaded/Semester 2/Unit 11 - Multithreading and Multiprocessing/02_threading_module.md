## Introduction

Yuna's indexing job is not just CPU work -- it also reads book records from the database (I/O) and updates a search index via an API (I/O). The CPU-bound part is one step; the I/O steps are the bottleneck in the first pass. Threads can help here: while one thread waits for a database response, another can process records already downloaded.

This lesson covers the `threading` module: creating threads, passing arguments, joining (waiting for completion), and using daemon threads.

![A diagram showing five threads created from the main thread, each running an I/O operation concurrently, and the main thread calling join to wait for all of them to complete](images/02_threading_module.png)

## Creating and Starting a Thread

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-02-threading-module-001-30972dca75.html"
 width="100%"
></iframe>

`threading.Thread(target=fn, args=(arg1, arg2))` creates a thread. `t.start()` starts it. `t.join()` blocks the calling thread until `t` finishes.

## Thread Arguments

The `args` parameter is a tuple of positional arguments; `kwargs` is a dict of keyword arguments:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-02-threading-module-002-f5e7d9d0ff.html"
 width="100%"
></iframe>

## threading.current_thread and Names

Threads can be named for easier debugging:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-02-threading-module-003-5db473cbb0.html"
 width="100%"
></iframe>

## Daemon Threads

A daemon thread is a background thread that is automatically killed when the main thread exits, without requiring `join()`. Use it for background tasks that should not prevent the program from exiting.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-02-threading-module-004-e38f849f69.html"
 width="100%"
></iframe>

Non-daemon threads (the default) keep the program alive until they finish. If you forget to `join()` a non-daemon thread, the program will not exit until it completes.

## Thread Subclass Pattern

For threads that need more state, subclass `Thread` and override `run()`:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-02-threading-module-005-a23a88cc6d.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-02-threading-module-006-f626192c69.html"
 width="100%"
></iframe>

Note that `results[index] = ...` is used instead of `results.append(...)` to avoid ordering problems when threads finish in different orders.

## Conclusion

`threading.Thread` creates threads; `start()` launches them; `join()` waits for them. Daemon threads are killed when the main thread exits. For I/O-bound work, threads run concurrently because the GIL is released during I/O waits. The next lesson explains the GIL in depth and why it means threads cannot be used for CPU-bound parallelism.
