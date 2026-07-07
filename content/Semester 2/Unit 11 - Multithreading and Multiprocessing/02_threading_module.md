## Introduction

Yuna's indexing job is not just CPU work -- it also reads book records from the database (I/O) and updates a search index via an API (I/O). The CPU-bound part is one step; the I/O steps are the bottleneck in the first pass. Threads can help here: while one thread waits for a database response, another can process records already downloaded.

This lesson covers the `threading` module: creating threads, passing arguments, joining (waiting for completion), and using daemon threads.

![A diagram showing five threads created from the main thread, each running an I/O operation concurrently, and the main thread calling join to wait for all of them to complete](images/02_threading_module.png)

## Creating and Starting a Thread

```python
import threading
import time

def index_batch(batch_id, records):
    print(f"Thread {batch_id}: starting {len(records)} records")
    time.sleep(0.5)   # simulate I/O (database read + API write)
    print(f"Thread {batch_id}: done")

records = list(range(100))   # simulate 100 records
batches = [records[i:i+20] for i in range(0, 100, 20)]   # 5 batches of 20

threads = []
for i, batch in enumerate(batches):
    t = threading.Thread(target=index_batch, args=(i, batch))
    threads.append(t)
    t.start()

# Wait for all threads to complete:
for t in threads:
    t.join()

print("All batches indexed")
```

`threading.Thread(target=fn, args=(arg1, arg2))` creates a thread. `t.start()` starts it. `t.join()` blocks the calling thread until `t` finishes.

## Thread Arguments

The `args` parameter is a tuple of positional arguments; `kwargs` is a dict of keyword arguments:

```python
def process(record_id, *, priority="normal"):
    print(f"Processing {record_id} at {priority} priority")

t = threading.Thread(
    target=process,
    args=(42,),
    kwargs={"priority": "high"}
)
t.start()
t.join()
```

## threading.current_thread and Names

Threads can be named for easier debugging:

```python
import threading

def worker():
    name = threading.current_thread().name
    print(f"Running in thread: {name}")

t = threading.Thread(target=worker, name="indexer-1")
t.start()
t.join()
# Running in thread: indexer-1

# The main thread:
print(threading.current_thread().name)   # MainThread
print(threading.active_count())          # number of threads currently alive
```

## Daemon Threads

A daemon thread is a background thread that is automatically killed when the main thread exits, without requiring `join()`. Use it for background tasks that should not prevent the program from exiting.

```python
import threading
import time

def heartbeat():
    while True:
        print("Library system: alive")
        time.sleep(60)

# Daemon: killed when main thread exits
monitor = threading.Thread(target=heartbeat, daemon=True)
monitor.start()

# Main work:
index_catalog()
# When this returns, the daemon thread is also killed -- no need to stop it
```

Non-daemon threads (the default) keep the program alive until they finish. If you forget to `join()` a non-daemon thread, the program will not exit until it completes.

## Thread Subclass Pattern

For threads that need more state, subclass `Thread` and override `run()`:

```python
import threading

class IndexerThread(threading.Thread):
    def __init__(self, batch_id, records):
        super().__init__(name=f"indexer-{batch_id}")
        self.batch_id = batch_id
        self.records = records
        self.indexed_count = 0

    def run(self):
        for record in self.records:
            self.index_record(record)
            self.indexed_count += 1
        print(f"Batch {self.batch_id}: indexed {self.indexed_count} records")

    def index_record(self, record):
        import time
        time.sleep(0.001)   # simulate I/O

threads = [IndexerThread(i, batch) for i, batch in enumerate(batches)]
for t in threads:
    t.start()
for t in threads:
    t.join()

total = sum(t.indexed_count for t in threads)
print(f"Total indexed: {total}")
```

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

```python
import threading
import time

def parallel_download(urls):
    results = [None] * len(urls)

    def fetch(index, url):
        time.sleep(0.05)   # simulate network I/O
        results[index] = f"<response from {url}>"

    threads = [
        threading.Thread(target=fetch, args=(i, url))
        for i, url in enumerate(urls)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return results

# Demo:
urls = ["http://api/books/1", "http://api/books/2", "http://api/books/3"]
result = parallel_download(urls)
for url, resp in zip(urls, result):
    print(f"  {url} -> {resp!r}")
```

Note that `results[index] = ...` is used instead of `results.append(...)` to avoid ordering problems when threads finish in different orders.

## Conclusion

`threading.Thread` creates threads; `start()` launches them; `join()` waits for them. Daemon threads are killed when the main thread exits. For I/O-bound work, threads run concurrently because the GIL is released during I/O waits. The next lesson explains the GIL in depth and why it means threads cannot be used for CPU-bound parallelism.
