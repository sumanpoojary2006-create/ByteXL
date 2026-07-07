## Introduction

Miguel converts his sequential code to use `async def` but keeps using the `requests` library for HTTP calls. His tests show no speed improvement. His more experienced colleague looks at the code and points to the problem immediately: `requests` is a blocking library. Wrapping it in an `async def` function does not make it non-blocking. He needs an async-compatible HTTP library instead.

This lesson clarifies what blocking and non-blocking mean, why blocking code inside an async function breaks the event loop, and how to recognize the difference.

![A timeline showing blocking code in an async function: the event loop stops completely during the blocking call, unable to run other tasks, versus non-blocking: the event loop continues running other tasks while waiting for I/O](images/02_blocking_vs_nonblocking_io.png)

## Blocking I/O: The Default

A blocking function does not return until its work is complete. When Python calls a blocking function, the entire thread stops and waits. Nothing else runs.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2Jsb2NraW5nX3ZzX25vbmJsb2NraW5nX2lvIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJpbXBvcnQgcmVxdWVzdHNcbmltcG9ydCB0aW1lXG5cbmRlZiBmZXRjaF9jYXRhbG9nKHVybCk6XG4gICAgcmVzcG9uc2UgPSByZXF1ZXN0cy5nZXQodXJsKSAgICMgQkxPQ0tTOiB0aHJlYWQgc3RvcHMgaGVyZSB1bnRpbCByZXNwb25zZSBhcnJpdmVzXG4gICAgcmV0dXJuIHJlc3BvbnNlLmpzb24oKVxuXG5zdGFydCA9IHRpbWUucGVyZl9jb3VudGVyKClcbmZldGNoX2NhdGFsb2coXCJodHRwczovL2h0dHBiaW4ub3JnL2RlbGF5LzFcIikgICAjIHdhaXRzIDEgc2Vjb25kXG5mZXRjaF9jYXRhbG9nKFwiaHR0cHM6Ly9odHRwYmluLm9yZy9kZWxheS8xXCIpICAgIyB3YWl0cyBhbm90aGVyIHNlY29uZFxucHJpbnQoZlwiVG90YWw6IHt0aW1lLnBlcmZfY291bnRlcigpIC0gc3RhcnQ6LjJmfXNcIikgICAjIOKJiCAyLjBzIn0"
 width="100%"
></iframe>

During the 1-second wait in the first call, no other code runs. The program is frozen at that line.

## The Event Loop and Why Blocking Breaks It

The asyncio event loop runs in a single thread. It switches between tasks at `await` points. If a task runs code that blocks the thread (without `await`), the event loop is frozen: it cannot switch to other tasks, and all pending async operations are stuck.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2Jsb2NraW5nX3ZzX25vbmJsb2NraW5nX2lvIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJpbXBvcnQgYXN5bmNpb1xuaW1wb3J0IHJlcXVlc3RzICAgIyBibG9ja2luZyBsaWJyYXJ5IC0tIFdST05HIHRvIHVzZSBpbnNpZGUgYXN5bmNcblxuYXN5bmMgZGVmIGZldGNoX2Jsb2NraW5nKHVybCk6XG4gICAgIyBUaGlzIFwiYXdhaXRcIiBkb2VzIG5vdGhpbmcgdXNlZnVsIC0tIHJlcXVlc3RzLmdldCBpcyBub3QgYSBjb3JvdXRpbmVcbiAgICAjIFRoZSBldmVudCBsb29wIENBTk5PVCBzd2l0Y2ggdG8gb3RoZXIgdGFza3MgZHVyaW5nIHRoaXMgY2FsbFxuICAgIHJlc3BvbnNlID0gcmVxdWVzdHMuZ2V0KHVybCkgICAjIEJMT0NLUyB0aGUgZXZlbnQgbG9vcCB0aHJlYWRcbiAgICByZXR1cm4gcmVzcG9uc2UuanNvbigpXG5cbmFzeW5jIGRlZiBtYWluKCk6XG4gICAgIyBUaGVzZSBhcHBlYXIgY29uY3VycmVudCBidXQgYWN0dWFsbHkgcnVuIHNlcXVlbnRpYWxseVxuICAgICMgYmVjYXVzZSByZXF1ZXN0cy5nZXQgYmxvY2tzIHRoZSB0aHJlYWQgZWFjaCB0aW1lXG4gICAgdGFza3MgPSBbXG4gICAgICAgIGFzeW5jaW8uY3JlYXRlX3Rhc2soZmV0Y2hfYmxvY2tpbmcoXCJodHRwczovL2h0dHBiaW4ub3JnL2RlbGF5LzFcIikpLFxuICAgICAgICBhc3luY2lvLmNyZWF0ZV90YXNrKGZldGNoX2Jsb2NraW5nKFwiaHR0cHM6Ly9odHRwYmluLm9yZy9kZWxheS8xXCIpKSxcbiAgICBdXG4gICAgYXdhaXQgYXN5bmNpby5nYXRoZXIoKnRhc2tzKVxuICAgICMgVG90YWw6IOKJiCAyLjBzIChzZXF1ZW50aWFsKSwgbm90IOKJiCAxLjBzIChjb25jdXJyZW50KSJ9"
 width="100%"
></iframe>

The event loop is cooperatively scheduled. If one task never yields (`await`s), other tasks never run.

## Non-Blocking I/O: The Async Way

A non-blocking I/O operation tells the OS to start the operation and returns control immediately. The event loop registers a callback and runs other tasks until the OS signals that the operation is complete.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2Jsb2NraW5nX3ZzX25vbmJsb2NraW5nX2lvIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJpbXBvcnQgYXN5bmNpb1xuaW1wb3J0IGFpb2h0dHAgICAjIGFzeW5jLWNvbXBhdGlibGUgSFRUUCBsaWJyYXJ5XG5cbmFzeW5jIGRlZiBmZXRjaF9ub25ibG9ja2luZyhzZXNzaW9uLCB1cmwpOlxuICAgIGFzeW5jIHdpdGggc2Vzc2lvbi5nZXQodXJsKSBhcyByZXNwb25zZTogICAjIFlJRUxEUyBhdCBJL086IGV2ZW50IGxvb3AgY2FuIHJ1biBvdGhlcnNcbiAgICAgICAgcmV0dXJuIGF3YWl0IHJlc3BvbnNlLmpzb24oKVxuXG5hc3luYyBkZWYgbWFpbigpOlxuICAgIGFzeW5jIHdpdGggYWlvaHR0cC5DbGllbnRTZXNzaW9uKCkgYXMgc2Vzc2lvbjpcbiAgICAgICAgdGFza3MgPSBbXG4gICAgICAgICAgICBhc3luY2lvLmNyZWF0ZV90YXNrKGZldGNoX25vbmJsb2NraW5nKHNlc3Npb24sIFwiaHR0cHM6Ly9odHRwYmluLm9yZy9kZWxheS8xXCIpKSxcbiAgICAgICAgICAgIGFzeW5jaW8uY3JlYXRlX3Rhc2soZmV0Y2hfbm9uYmxvY2tpbmcoc2Vzc2lvbiwgXCJodHRwczovL2h0dHBiaW4ub3JnL2RlbGF5LzFcIikpLFxuICAgICAgICBdXG4gICAgICAgIHJlc3VsdHMgPSBhd2FpdCBhc3luY2lvLmdhdGhlcigqdGFza3MpXG4gICAgIyBUb3RhbDog4omIIDEuMHMgKHRydWx5IGNvbmN1cnJlbnQpXG5cbmFzeW5jaW8ucnVuKG1haW4oKSkifQ"
 width="100%"
></iframe>

`aiohttp` uses non-blocking socket operations. When `session.get` waits for the network, it yields control to the event loop, which runs the second task. Both complete in approximately the time of the single slowest call.

## Recognizing Blocking vs Non-Blocking

The rule: any function that does I/O must be async and awaitable for use inside an async function. If it is not, it blocks the event loop.

| Blocking (cannot use in async safely) | Non-blocking async equivalent |
|---|---|
| `requests.get(url)` | `aiohttp.ClientSession.get(url)` |
| `open(path).read()` | `aiofiles.open(path)` |
| `time.sleep(n)` | `asyncio.sleep(n)` |
| `sqlite3.connect(...)` | `aiosqlite.connect(...)` |

## Running Blocking Code Safely

When you must use a blocking library in an async context, run it in a thread pool so it does not block the event loop:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2Jsb2NraW5nX3ZzX25vbmJsb2NraW5nX2lvIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJpbXBvcnQgYXN5bmNpb1xuaW1wb3J0IHJlcXVlc3RzXG5cbmFzeW5jIGRlZiBmZXRjaF93aXRoX3RocmVhZCh1cmwpOlxuICAgIGxvb3AgPSBhc3luY2lvLmdldF9ldmVudF9sb29wKClcbiAgICByZXNwb25zZSA9IGF3YWl0IGxvb3AucnVuX2luX2V4ZWN1dG9yKE5vbmUsIHJlcXVlc3RzLmdldCwgdXJsKVxuICAgIHJldHVybiByZXNwb25zZS5qc29uKCkifQ"
 width="100%"
></iframe>

`run_in_executor` runs the blocking function in a separate thread, yielding control to the event loop while the thread waits.

## Blocking vs Non-Blocking at a Glance

| Concept | What it means |
|---|---|
| Blocking I/O | Thread stops; event loop cannot switch to other tasks |
| Non-blocking I/O | Thread yields at `await`; event loop runs other tasks |
| `asyncio.sleep(n)` | Non-blocking pause (yields to event loop) |
| `time.sleep(n)` | Blocking pause (freezes event loop) |
| `run_in_executor` | Run blocking code in a thread without freezing the event loop |

## Your Turn

Compare these two implementations:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2Jsb2NraW5nX3ZzX25vbmJsb2NraW5nX2lvIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJpbXBvcnQgYXN5bmNpb1xuaW1wb3J0IHRpbWVcblxuYXN5bmMgZGVmIGJhZF9wYXVzZSgpOlxuICAgIHRpbWUuc2xlZXAoMSkgICAjIFdST05HOiBibG9ja3MgdGhlIGV2ZW50IGxvb3BcblxuYXN5bmMgZGVmIGdvb2RfcGF1c2UoKTpcbiAgICBhd2FpdCBhc3luY2lvLnNsZWVwKDEpICAgIyBSSUdIVDogeWllbGRzIHRvIGV2ZW50IGxvb3BcblxuYXN5bmMgZGVmIG1haW4oKTpcbiAgICBpbXBvcnQgdGltZVxuICAgIHN0YXJ0ID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuICAgIGF3YWl0IGFzeW5jaW8uZ2F0aGVyKGdvb2RfcGF1c2UoKSwgZ29vZF9wYXVzZSgpLCBnb29kX3BhdXNlKCkpXG4gICAgcHJpbnQoZlwiZ29vZF9wYXVzZSB4Mzoge3RpbWUucGVyZl9jb3VudGVyKCkgLSBzdGFydDouMmZ9c1wiKVxuXG4gICAgc3RhcnQgPSB0aW1lLnBlcmZfY291bnRlcigpXG4gICAgYXdhaXQgYXN5bmNpby5nYXRoZXIoYmFkX3BhdXNlKCksIGJhZF9wYXVzZSgpLCBiYWRfcGF1c2UoKSlcbiAgICBwcmludChmXCJiYWRfcGF1c2UgeDM6IHt0aW1lLnBlcmZfY291bnRlcigpIC0gc3RhcnQ6LjJmfXNcIilcblxuYXN5bmNpby5ydW4obWFpbigpKSJ9"
 width="100%"
></iframe>

Run this and observe the difference in timing. `good_pause` x3 should take approximately 1 second total; `bad_pause` x3 should take approximately 3 seconds.

## Conclusion

Blocking code in an async function freezes the event loop and eliminates any benefit from concurrency. Always use async-compatible libraries (`aiohttp` instead of `requests`, `asyncio.sleep` instead of `time.sleep`, `aiosqlite` instead of `sqlite3`) inside async functions. Use `run_in_executor` when you must call a blocking library. The next lesson introduces `async def` and `await` in detail, showing exactly how to write and run async functions.
