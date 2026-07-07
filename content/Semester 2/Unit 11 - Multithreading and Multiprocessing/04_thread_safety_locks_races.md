## Introduction

Yuna's I/O phase uses threads to download records concurrently. Each thread updates a shared `stats` dictionary (incrementing a counter for each record processed). After a long run, the counter is always slightly off -- it reads 4,987 when 5,000 records were processed. The missing 13 are a race condition: two threads read the counter at the same time, both increment it from the same value, and one update is silently lost.

This is the fundamental problem with shared mutable state in concurrent code, and the solution is synchronization using locks.

![Two threads shown reading the same counter value (5), both incrementing to 6, and both writing 6 -- so one increment is lost. Next to it: the lock-protected version where one thread waits before reading, preventing the lost update](images/04_thread_safety_locks_races.png)

## The Race Condition

A race condition happens when the result of a computation depends on the order in which threads execute, and that order is not controlled.

```python
import threading

counter = 0

def increment(n):
    global counter
    for _ in range(n):
        # Three operations: READ, ADD 1, WRITE
        # Another thread can interrupt between READ and WRITE
        counter += 1   # NOT atomic -- this is a race condition

threads = [threading.Thread(target=increment, args=(100_000,)) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(counter)   # expected: 500_000 -- actual: less (lost updates)
```

`counter += 1` looks atomic but is not. It compiles to three bytecode instructions: load the current value, add 1, store the result. The GIL context-switches between threads at bytecode boundaries, so another thread can read `counter` between the load and the store.

## threading.Lock

A `Lock` is the fundamental synchronization primitive. Only one thread can hold the lock at a time. Any other thread that tries to acquire the lock will block until it is released.

```python
import threading

counter = 0
lock = threading.Lock()

def safe_increment(n):
    global counter
    for _ in range(n):
        with lock:
            counter += 1   # only one thread inside at a time

threads = [threading.Thread(target=safe_increment, args=(100_000,)) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(counter)   # 500_000: correct every time
```

Always use `with lock:` rather than `lock.acquire()` / `lock.release()`. The `with` statement releases the lock even if an exception occurs.

## threading.RLock: Reentrant Lock

A regular `Lock` cannot be acquired twice by the same thread. An `RLock` (reentrant lock) can:

```python
lock = threading.RLock()

def outer():
    with lock:   # acquires lock
        inner()

def inner():
    with lock:   # acquires lock again (would deadlock with regular Lock)
        print("inner")

outer()   # works correctly with RLock
```

Use `RLock` when a locked function calls another function that also needs the same lock.

## threading.Event: Signaling Between Threads

`threading.Event` allows one thread to signal another:

```python
import threading
import time

ready_event = threading.Event()

def loader():
    print("Loading catalog...")
    time.sleep(1)
    print("Catalog ready")
    ready_event.set()   # signal the event

def processor():
    ready_event.wait()   # block until event is set
    print("Processing catalog")

t_load = threading.Thread(target=loader)
t_proc = threading.Thread(target=processor)
t_proc.start()
t_load.start()
t_load.join(); t_proc.join()
```

## threading.Queue: Thread-Safe Data Passing

`queue.Queue` is the recommended way to pass data between threads. It is thread-safe and avoids the need for manual locking.

```python
import threading
import queue

task_queue = queue.Queue()
result_queue = queue.Queue()

def worker():
    while True:
        record = task_queue.get()   # blocks until an item is available
        if record is None:
            break   # sentinel: stop the worker
        result = process(record)
        result_queue.put(result)
        task_queue.task_done()

# Start workers:
workers = [threading.Thread(target=worker, daemon=True) for _ in range(4)]
for w in workers:
    w.start()

# Enqueue tasks:
for record in catalog_records:
    task_queue.put(record)

# Send stop sentinels:
for _ in workers:
    task_queue.put(None)

task_queue.join()   # wait until all tasks are done

# Demo:
result = worker()
print(f"worker() ->", result)
```

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

```python
import threading

class IndexStats:
    def __init__(self):
        self.indexed = 0
        self.errors = 0
        self._lock = threading.Lock()

    def record_success(self):
        with self._lock:
            self.indexed += 1

    def record_error(self):
        with self._lock:
            self.errors += 1

def index_record(stats, record_id):
    import time, random
    time.sleep(random.uniform(0.001, 0.01))
    if record_id % 10 == 0:
        stats.record_error()
    else:
        stats.record_success()

stats = IndexStats()
threads = [threading.Thread(target=index_record, args=(stats, i)) for i in range(100)]
for t in threads: t.start()
for t in threads: t.join()
print(f"Indexed: {stats.indexed}, Errors: {stats.errors}")
```

Verify that `indexed + errors == 100` every time.

## Conclusion

Shared mutable state in threads causes race conditions when multiple threads read and write concurrently. `threading.Lock` provides mutual exclusion: only one thread runs the locked section at a time. `queue.Queue` is the thread-safe channel for passing data between threads. The next lesson shows how to use `multiprocessing` for CPU-bound work, where the GIL cannot be bypassed by threads.
