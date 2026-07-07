## Introduction

Yuna's I/O phase uses threads to download records concurrently. Each thread updates a shared `stats` dictionary (incrementing a counter for each record processed). After a long run, the counter is always slightly off -- it reads 4,987 when 5,000 records were processed. The missing 13 are a race condition: two threads read the counter at the same time, both increment it from the same value, and one update is silently lost.

This is the fundamental problem with shared mutable state in concurrent code, and the solution is synchronization using locks.

![Two threads shown reading the same counter value (5), both incrementing to 6, and both writing 6 -- so one increment is lost. Next to it: the lock-protected version where one thread waits before reading, preventing the lost update](images/04_thread_safety_locks_races.png)

## The Race Condition

A race condition happens when the result of a computation depends on the order in which threads execute, and that order is not controlled.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3RocmVhZF9zYWZldHlfbG9ja3NfcmFjZXMgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6ImltcG9ydCB0aHJlYWRpbmdcblxuY291bnRlciA9IDBcblxuZGVmIGluY3JlbWVudChuKTpcbiAgICBnbG9iYWwgY291bnRlclxuICAgIGZvciBfIGluIHJhbmdlKG4pOlxuICAgICAgICAjIFRocmVlIG9wZXJhdGlvbnM6IFJFQUQsIEFERCAxLCBXUklURVxuICAgICAgICAjIEFub3RoZXIgdGhyZWFkIGNhbiBpbnRlcnJ1cHQgYmV0d2VlbiBSRUFEIGFuZCBXUklURVxuICAgICAgICBjb3VudGVyICs9IDEgICAjIE5PVCBhdG9taWMgLS0gdGhpcyBpcyBhIHJhY2UgY29uZGl0aW9uXG5cbnRocmVhZHMgPSBbdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9aW5jcmVtZW50LCBhcmdzPSgxMDBfMDAwLCkpIGZvciBfIGluIHJhbmdlKDUpXVxuZm9yIHQgaW4gdGhyZWFkczpcbiAgICB0LnN0YXJ0KClcbmZvciB0IGluIHRocmVhZHM6XG4gICAgdC5qb2luKClcblxucHJpbnQoY291bnRlcikgICAjIGV4cGVjdGVkOiA1MDBfMDAwIC0tIGFjdHVhbDogbGVzcyAobG9zdCB1cGRhdGVzKSJ9"
 width="100%"
></iframe>

`counter += 1` looks atomic but is not. It compiles to three bytecode instructions: load the current value, add 1, store the result. The GIL context-switches between threads at bytecode boundaries, so another thread can read `counter` between the load and the store.

## threading.Lock

A `Lock` is the fundamental synchronization primitive. Only one thread can hold the lock at a time. Any other thread that tries to acquire the lock will block until it is released.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3RocmVhZF9zYWZldHlfbG9ja3NfcmFjZXMgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6ImltcG9ydCB0aHJlYWRpbmdcblxuY291bnRlciA9IDBcbmxvY2sgPSB0aHJlYWRpbmcuTG9jaygpXG5cbmRlZiBzYWZlX2luY3JlbWVudChuKTpcbiAgICBnbG9iYWwgY291bnRlclxuICAgIGZvciBfIGluIHJhbmdlKG4pOlxuICAgICAgICB3aXRoIGxvY2s6XG4gICAgICAgICAgICBjb3VudGVyICs9IDEgICAjIG9ubHkgb25lIHRocmVhZCBpbnNpZGUgYXQgYSB0aW1lXG5cbnRocmVhZHMgPSBbdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9c2FmZV9pbmNyZW1lbnQsIGFyZ3M9KDEwMF8wMDAsKSkgZm9yIF8gaW4gcmFuZ2UoNSldXG5mb3IgdCBpbiB0aHJlYWRzOlxuICAgIHQuc3RhcnQoKVxuZm9yIHQgaW4gdGhyZWFkczpcbiAgICB0LmpvaW4oKVxuXG5wcmludChjb3VudGVyKSAgICMgNTAwXzAwMDogY29ycmVjdCBldmVyeSB0aW1lIn0"
 width="100%"
></iframe>

Always use `with lock:` rather than `lock.acquire()` / `lock.release()`. The `with` statement releases the lock even if an exception occurs.

## threading.RLock: Reentrant Lock

A regular `Lock` cannot be acquired twice by the same thread. An `RLock` (reentrant lock) can:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3RocmVhZF9zYWZldHlfbG9ja3NfcmFjZXMgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6ImxvY2sgPSB0aHJlYWRpbmcuUkxvY2soKVxuXG5kZWYgb3V0ZXIoKTpcbiAgICB3aXRoIGxvY2s6ICAgIyBhY3F1aXJlcyBsb2NrXG4gICAgICAgIGlubmVyKClcblxuZGVmIGlubmVyKCk6XG4gICAgd2l0aCBsb2NrOiAgICMgYWNxdWlyZXMgbG9jayBhZ2FpbiAod291bGQgZGVhZGxvY2sgd2l0aCByZWd1bGFyIExvY2spXG4gICAgICAgIHByaW50KFwiaW5uZXJcIilcblxub3V0ZXIoKSAgICMgd29ya3MgY29ycmVjdGx5IHdpdGggUkxvY2sifQ"
 width="100%"
></iframe>

Use `RLock` when a locked function calls another function that also needs the same lock.

## threading.Event: Signaling Between Threads

`threading.Event` allows one thread to signal another:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3RocmVhZF9zYWZldHlfbG9ja3NfcmFjZXMgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6ImltcG9ydCB0aHJlYWRpbmdcbmltcG9ydCB0aW1lXG5cbnJlYWR5X2V2ZW50ID0gdGhyZWFkaW5nLkV2ZW50KClcblxuZGVmIGxvYWRlcigpOlxuICAgIHByaW50KFwiTG9hZGluZyBjYXRhbG9nLi4uXCIpXG4gICAgdGltZS5zbGVlcCgxKVxuICAgIHByaW50KFwiQ2F0YWxvZyByZWFkeVwiKVxuICAgIHJlYWR5X2V2ZW50LnNldCgpICAgIyBzaWduYWwgdGhlIGV2ZW50XG5cbmRlZiBwcm9jZXNzb3IoKTpcbiAgICByZWFkeV9ldmVudC53YWl0KCkgICAjIGJsb2NrIHVudGlsIGV2ZW50IGlzIHNldFxuICAgIHByaW50KFwiUHJvY2Vzc2luZyBjYXRhbG9nXCIpXG5cbnRfbG9hZCA9IHRocmVhZGluZy5UaHJlYWQodGFyZ2V0PWxvYWRlcilcbnRfcHJvYyA9IHRocmVhZGluZy5UaHJlYWQodGFyZ2V0PXByb2Nlc3NvcilcbnRfcHJvYy5zdGFydCgpXG50X2xvYWQuc3RhcnQoKVxudF9sb2FkLmpvaW4oKTsgdF9wcm9jLmpvaW4oKSJ9"
 width="100%"
></iframe>

## threading.Queue: Thread-Safe Data Passing

`queue.Queue` is the recommended way to pass data between threads. It is thread-safe and avoids the need for manual locking.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3RocmVhZF9zYWZldHlfbG9ja3NfcmFjZXMgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6ImltcG9ydCB0aHJlYWRpbmdcbmltcG9ydCBxdWV1ZVxuXG50YXNrX3F1ZXVlID0gcXVldWUuUXVldWUoKVxucmVzdWx0X3F1ZXVlID0gcXVldWUuUXVldWUoKVxuXG5kZWYgd29ya2VyKCk6XG4gICAgd2hpbGUgVHJ1ZTpcbiAgICAgICAgcmVjb3JkID0gdGFza19xdWV1ZS5nZXQoKSAgICMgYmxvY2tzIHVudGlsIGFuIGl0ZW0gaXMgYXZhaWxhYmxlXG4gICAgICAgIGlmIHJlY29yZCBpcyBOb25lOlxuICAgICAgICAgICAgYnJlYWsgICAjIHNlbnRpbmVsOiBzdG9wIHRoZSB3b3JrZXJcbiAgICAgICAgcmVzdWx0ID0gcHJvY2VzcyhyZWNvcmQpXG4gICAgICAgIHJlc3VsdF9xdWV1ZS5wdXQocmVzdWx0KVxuICAgICAgICB0YXNrX3F1ZXVlLnRhc2tfZG9uZSgpXG5cbiMgU3RhcnQgd29ya2VyczpcbndvcmtlcnMgPSBbdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9d29ya2VyLCBkYWVtb249VHJ1ZSkgZm9yIF8gaW4gcmFuZ2UoNCldXG5mb3IgdyBpbiB3b3JrZXJzOlxuICAgIHcuc3RhcnQoKVxuXG4jIEVucXVldWUgdGFza3M6XG5mb3IgcmVjb3JkIGluIGNhdGFsb2dfcmVjb3JkczpcbiAgICB0YXNrX3F1ZXVlLnB1dChyZWNvcmQpXG5cbiMgU2VuZCBzdG9wIHNlbnRpbmVsczpcbmZvciBfIGluIHdvcmtlcnM6XG4gICAgdGFza19xdWV1ZS5wdXQoTm9uZSlcblxudGFza19xdWV1ZS5qb2luKCkgICAjIHdhaXQgdW50aWwgYWxsIHRhc2tzIGFyZSBkb25lIn0"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3RocmVhZF9zYWZldHlfbG9ja3NfcmFjZXMgY29kZSA2IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA2LnB5IiwiY29kZSI6ImltcG9ydCB0aHJlYWRpbmdcblxuY2xhc3MgSW5kZXhTdGF0czpcbiAgICBkZWYgX19pbml0X18oc2VsZik6XG4gICAgICAgIHNlbGYuaW5kZXhlZCA9IDBcbiAgICAgICAgc2VsZi5lcnJvcnMgPSAwXG4gICAgICAgIHNlbGYuX2xvY2sgPSB0aHJlYWRpbmcuTG9jaygpXG5cbiAgICBkZWYgcmVjb3JkX3N1Y2Nlc3Moc2VsZik6XG4gICAgICAgIHdpdGggc2VsZi5fbG9jazpcbiAgICAgICAgICAgIHNlbGYuaW5kZXhlZCArPSAxXG5cbiAgICBkZWYgcmVjb3JkX2Vycm9yKHNlbGYpOlxuICAgICAgICB3aXRoIHNlbGYuX2xvY2s6XG4gICAgICAgICAgICBzZWxmLmVycm9ycyArPSAxXG5cbmRlZiBpbmRleF9yZWNvcmQoc3RhdHMsIHJlY29yZF9pZCk6XG4gICAgaW1wb3J0IHRpbWUsIHJhbmRvbVxuICAgIHRpbWUuc2xlZXAocmFuZG9tLnVuaWZvcm0oMC4wMDEsIDAuMDEpKVxuICAgIGlmIHJlY29yZF9pZCAlIDEwID09IDA6XG4gICAgICAgIHN0YXRzLnJlY29yZF9lcnJvcigpXG4gICAgZWxzZTpcbiAgICAgICAgc3RhdHMucmVjb3JkX3N1Y2Nlc3MoKVxuXG5zdGF0cyA9IEluZGV4U3RhdHMoKVxudGhyZWFkcyA9IFt0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1pbmRleF9yZWNvcmQsIGFyZ3M9KHN0YXRzLCBpKSkgZm9yIGkgaW4gcmFuZ2UoMTAwKV1cbmZvciB0IGluIHRocmVhZHM6IHQuc3RhcnQoKVxuZm9yIHQgaW4gdGhyZWFkczogdC5qb2luKClcbnByaW50KGZcIkluZGV4ZWQ6IHtzdGF0cy5pbmRleGVkfSwgRXJyb3JzOiB7c3RhdHMuZXJyb3JzfVwiKSJ9"
 width="100%"
></iframe>

Verify that `indexed + errors == 100` every time.

## Conclusion

Shared mutable state in threads causes race conditions when multiple threads read and write concurrently. `threading.Lock` provides mutual exclusion: only one thread runs the locked section at a time. `queue.Queue` is the thread-safe channel for passing data between threads. The next lesson shows how to use `multiprocessing` for CPU-bound work, where the GIL cannot be bypassed by threads.
