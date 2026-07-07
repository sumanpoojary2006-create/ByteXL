## Introduction

Yuna's I/O phase uses threads to download records concurrently. Each thread updates a shared `stats` dictionary (incrementing a counter for each record processed). After a long run, the counter is always slightly off -- it reads 4,987 when 5,000 records were processed. The missing 13 are a race condition: two threads read the counter at the same time, both increment it from the same value, and one update is silently lost.

This is the fundamental problem with shared mutable state in concurrent code, and the solution is synchronization using locks.

![Two threads shown reading the same counter value (5), both incrementing to 6, and both writing 6 -- so one increment is lost. Next to it: the lock-protected version where one thread waits before reading, preventing the lost update](images/04_thread_safety_locks_races.png)

## The Race Condition

A race condition happens when the result of a computation depends on the order in which threads execute, and that order is not controlled.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-04-thread-safety-locks-r-001-f8f88717c3.html"
 width="100%"
></iframe>

`counter += 1` looks atomic but is not. It compiles to three bytecode instructions: load the current value, add 1, store the result. The GIL context-switches between threads at bytecode boundaries, so another thread can read `counter` between the load and the store.

## threading.Lock

A `Lock` is the fundamental synchronization primitive. Only one thread can hold the lock at a time. Any other thread that tries to acquire the lock will block until it is released.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-04-thread-safety-locks-r-002-5ed7521d18.html"
 width="100%"
></iframe>

Always use `with lock:` rather than `lock.acquire()` / `lock.release()`. The `with` statement releases the lock even if an exception occurs.

## threading.RLock: Reentrant Lock

A regular `Lock` cannot be acquired twice by the same thread. An `RLock` (reentrant lock) can:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-04-thread-safety-locks-r-003-c61492b7fe.html"
 width="100%"
></iframe>

Use `RLock` when a locked function calls another function that also needs the same lock.

## threading.Event: Signaling Between Threads

`threading.Event` allows one thread to signal another:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-04-thread-safety-locks-r-004-f337a988e3.html"
 width="100%"
></iframe>

## threading.Queue: Thread-Safe Data Passing

`queue.Queue` is the recommended way to pass data between threads. It is thread-safe and avoids the need for manual locking.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-04-thread-safety-locks-r-005-10e68513e7.html"
 width="100%"
></iframe>

## Thread Safety at a Glance

| Tool | What it does |
|---|---|
| `threading.Lock()` | Mutual exclusion -- only one thread at a time |
| `threading.RLock()` | Reentrant lock -- same thread can acquire multiple times |
| `threading.Event()` | One thread signals another |
| `queue.Queue()` | Thread-safe FIFO queue for inter-thread communication |
| `with lock:` | Safe acquire/release (releases on exception) |

## Your Turn

Rewrite Yuna's stats counter to be thread-safe. Use a `Lock` to protect the increment and a `threading.Event` to signal when all threads have finished their first batch:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-11-multithreading-and-multiprocessing-04-thread-safety-locks-r-006-b26ca842d2.html"
 width="100%"
></iframe>

Verify that `indexed + errors == 100` every time.

## Conclusion

Shared mutable state in threads causes race conditions when multiple threads read and write concurrently. `threading.Lock` provides mutual exclusion: only one thread runs the locked section at a time. `queue.Queue` is the thread-safe channel for passing data between threads. The next lesson shows how to use `multiprocessing` for CPU-bound work, where the GIL cannot be bypassed by threads.
