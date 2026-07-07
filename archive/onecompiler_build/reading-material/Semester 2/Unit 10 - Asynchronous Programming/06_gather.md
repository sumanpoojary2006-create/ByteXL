## Introduction

Miguel has been creating tasks manually and then `await`ing them one by one. His teammate shows him `asyncio.gather`, which starts multiple coroutines concurrently and collects all their results in a single `await`. It is the most common pattern in async Python and the cleanest way to write fan-out operations: send many requests, wait for all, return all results.

![A funnel diagram: many coroutines fan out from a single gather call, run concurrently, and their results fan back in to a single list when all are done](images/06_gather.png)

## asyncio.gather: Run Many, Collect All

`asyncio.gather` takes a list of coroutines or tasks, runs them concurrently, waits for all of them to finish, and returns their results in the same order as the inputs.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2dhdGhlciBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoiaW1wb3J0IGFzeW5jaW9cblxuYXN5bmMgZGVmIGZldGNoKGxpYnJhcnlfaWQsIGRlbGF5PTAuNSk6XG4gICAgYXdhaXQgYXN5bmNpby5zbGVlcChkZWxheSlcbiAgICByZXR1cm4gZlwibGlicmFyeV97bGlicmFyeV9pZH06IG9rXCJcblxuYXN5bmMgZGVmIG1haW4oKTpcbiAgICByZXN1bHRzID0gYXdhaXQgYXN5bmNpby5nYXRoZXIoXG4gICAgICAgIGZldGNoKDEsIGRlbGF5PTAuMyksXG4gICAgICAgIGZldGNoKDIsIGRlbGF5PTAuNSksXG4gICAgICAgIGZldGNoKDMsIGRlbGF5PTAuMSksXG4gICAgKVxuICAgIHByaW50KHJlc3VsdHMpXG4gICAgIyBbJ2xpYnJhcnlfMTogb2snLCAnbGlicmFyeV8yOiBvaycsICdsaWJyYXJ5XzM6IG9rJ11cbiAgICAjIFJlc3VsdHMgYXJlIGluIGlucHV0IG9yZGVyLCBub3QgY29tcGxldGlvbiBvcmRlclxuXG5hc3luY2lvLnJ1bihtYWluKCkpIn0"
 width="100%"
></iframe>

The total time is approximately 0.5 seconds (the longest), not 0.9 seconds (the sum). Results come back in the same order as the coroutines were passed, regardless of which finished first.

## gather with a List

For a dynamic number of coroutines, unpack a list:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2dhdGhlciBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoiYXN5bmMgZGVmIGNoZWNrX2FsbF9saWJyYXJpZXMoaXNibiwgbGlicmFyeV9pZHMpOlxuICAgIGNvcm91dGluZXMgPSBbZmV0Y2gobGliX2lkKSBmb3IgbGliX2lkIGluIGxpYnJhcnlfaWRzXVxuICAgIHJlc3VsdHMgPSBhd2FpdCBhc3luY2lvLmdhdGhlcigqY29yb3V0aW5lcykgICAjIHVucGFjayB0aGUgbGlzdFxuICAgIHJldHVybiBkaWN0KHppcChsaWJyYXJ5X2lkcywgcmVzdWx0cykpXG5cbmFzeW5jIGRlZiBtYWluKCk6XG4gICAgcmVzdWx0cyA9IGF3YWl0IGNoZWNrX2FsbF9saWJyYXJpZXMoXCI5NzgtMDAxXCIsIFsxLCAyLCAzLCA0LCA1XSlcbiAgICBwcmludChyZXN1bHRzKVxuXG5hc3luY2lvLnJ1bihtYWluKCkpIn0"
 width="100%"
></iframe>

## Handling Exceptions in gather

By default, if any coroutine raises an exception, `gather` immediately cancels the remaining coroutines and re-raises the first exception. The other results are lost.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2dhdGhlciBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoiYXN5bmMgZGVmIGZsYWt5X2ZldGNoKGxpYnJhcnlfaWQpOlxuICAgIGlmIGxpYnJhcnlfaWQgPT0gMjpcbiAgICAgICAgcmFpc2UgQ29ubmVjdGlvbkVycm9yKGZcIkxpYnJhcnkge2xpYnJhcnlfaWR9IGlzIGRvd25cIilcbiAgICBhd2FpdCBhc3luY2lvLnNsZWVwKDAuMSlcbiAgICByZXR1cm4gZlwibGlicmFyeV97bGlicmFyeV9pZH06IG9rXCJcblxuYXN5bmMgZGVmIG1haW4oKTpcbiAgICB0cnk6XG4gICAgICAgIHJlc3VsdHMgPSBhd2FpdCBhc3luY2lvLmdhdGhlcihcbiAgICAgICAgICAgIGZsYWt5X2ZldGNoKDEpLFxuICAgICAgICAgICAgZmxha3lfZmV0Y2goMiksICAgIyB3aWxsIHJhaXNlXG4gICAgICAgICAgICBmbGFreV9mZXRjaCgzKSxcbiAgICAgICAgKVxuICAgIGV4Y2VwdCBDb25uZWN0aW9uRXJyb3IgYXMgZXhjOlxuICAgICAgICBwcmludChmXCJGYWlsZWQ6IHtleGN9XCIpXG4gICAgICAgICMgUmVzdWx0cyBmcm9tIGxpYnJhcnkgMSBhbmQgMyBhcmUgZGlzY2FyZGVkIn0"
 width="100%"
></iframe>

Use `return_exceptions=True` to capture exceptions as return values instead of raising:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2dhdGhlciBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoiYXN5bmMgZGVmIG1haW4oKTpcbiAgICByZXN1bHRzID0gYXdhaXQgYXN5bmNpby5nYXRoZXIoXG4gICAgICAgIGZsYWt5X2ZldGNoKDEpLFxuICAgICAgICBmbGFreV9mZXRjaCgyKSwgICAjIHJhaXNlcyBDb25uZWN0aW9uRXJyb3JcbiAgICAgICAgZmxha3lfZmV0Y2goMyksXG4gICAgICAgIHJldHVybl9leGNlcHRpb25zPVRydWVcbiAgICApXG4gICAgZm9yIGksIHJlc3VsdCBpbiBlbnVtZXJhdGUocmVzdWx0cywgc3RhcnQ9MSk6XG4gICAgICAgIGlmIGlzaW5zdGFuY2UocmVzdWx0LCBFeGNlcHRpb24pOlxuICAgICAgICAgICAgcHJpbnQoZlwiTGlicmFyeSB7aX0gZmFpbGVkOiB7cmVzdWx0fVwiKVxuICAgICAgICBlbHNlOlxuICAgICAgICAgICAgcHJpbnQoZlwiTGlicmFyeSB7aX06IHtyZXN1bHR9XCIpXG4jIExpYnJhcnkgMTogbGlicmFyeV8xOiBva1xuIyBMaWJyYXJ5IDIgZmFpbGVkOiBMaWJyYXJ5IDIgaXMgZG93blxuIyBMaWJyYXJ5IDM6IGxpYnJhcnlfMzogb2sifQ"
 width="100%"
></iframe>

`return_exceptions=True` is the right choice when you want all results, even if some fail, and you will check them individually.

## asyncio.gather vs asyncio.wait

`asyncio.wait` is a lower-level function that gives more control: you can wait for the first result to come in, or wait until all are done, and you get sets of done/pending tasks.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2dhdGhlciBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoiaW1wb3J0IGFzeW5jaW9cblxuYXN5bmMgZGVmIG1haW4oKTpcbiAgICB0YXNrcyA9IFtcbiAgICAgICAgYXN5bmNpby5jcmVhdGVfdGFzayhmZXRjaCgxLCBkZWxheT0wLjUpKSxcbiAgICAgICAgYXN5bmNpby5jcmVhdGVfdGFzayhmZXRjaCgyLCBkZWxheT0wLjEpKSxcbiAgICAgICAgYXN5bmNpby5jcmVhdGVfdGFzayhmZXRjaCgzLCBkZWxheT0wLjMpKSxcbiAgICBdXG4gICAgIyBXYWl0IGZvciB0aGUgZmlyc3Qgb25lIHRvIGNvbXBsZXRlOlxuICAgIGRvbmUsIHBlbmRpbmcgPSBhd2FpdCBhc3luY2lvLndhaXQodGFza3MsIHJldHVybl93aGVuPWFzeW5jaW8uRklSU1RfQ09NUExFVEVEKVxuICAgIGZpcnN0ID0gZG9uZS5wb3AoKS5yZXN1bHQoKVxuICAgIHByaW50KGZcIkZpcnN0IGNvbXBsZXRlZDoge2ZpcnN0fVwiKVxuXG4gICAgIyBDYW5jZWwgcmVtYWluaW5nOlxuICAgIGZvciB0IGluIHBlbmRpbmc6XG4gICAgICAgIHQuY2FuY2VsKCkifQ"
 width="100%"
></iframe>

`gather` is simpler for "run all, collect all." `wait` is for more complex scheduling.

## gather at a Glance

| Pattern | Use |
|---|---|
| `await asyncio.gather(c1, c2, c3)` | Run three coroutines concurrently, collect results in order |
| `await asyncio.gather(*coros)` | Unpack a dynamic list of coroutines |
| `gather(..., return_exceptions=True)` | Capture exceptions as return values, don't raise |
| `asyncio.wait(..., FIRST_COMPLETED)` | Wait for the first to finish, cancel the rest |

## Your Turn

Write a `batch_check(isbns, library_id)` function that checks all ISBNs in a list concurrently for a single library, and returns a dict mapping each ISBN to whether it is available:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2dhdGhlciBjb2RlIDYiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDYucHkiLCJjb2RlIjoiaW1wb3J0IGFzeW5jaW9cblxuYXN5bmMgZGVmIGNoZWNrX2lzYm4obGlicmFyeV9pZCwgaXNibik6XG4gICAgYXdhaXQgYXN5bmNpby5zbGVlcCgwLjEpICAgIyBzaW11bGF0ZSBBUEkgY2FsbFxuICAgIHJldHVybiBpc2JuLCBsZW4oaXNibikgJSAyID09IDAgICMgbW9jazogZXZlbi1sZW5ndGggSVNCTnMgYXJlIGF2YWlsYWJsZVxuXG5hc3luYyBkZWYgYmF0Y2hfY2hlY2soaXNibnMsIGxpYnJhcnlfaWQpOlxuICAgIHJlc3VsdHMgPSBhd2FpdCBhc3luY2lvLmdhdGhlcihcbiAgICAgICAgKltjaGVja19pc2JuKGxpYnJhcnlfaWQsIGlzYm4pIGZvciBpc2JuIGluIGlzYm5zXSxcbiAgICAgICAgcmV0dXJuX2V4Y2VwdGlvbnM9VHJ1ZVxuICAgIClcbiAgICByZXR1cm4ge1xuICAgICAgICBpc2JuOiBhdmFpbGFibGVcbiAgICAgICAgZm9yIHJlc3VsdCBpbiByZXN1bHRzXG4gICAgICAgIGlmIG5vdCBpc2luc3RhbmNlKHJlc3VsdCwgRXhjZXB0aW9uKVxuICAgICAgICBmb3IgaXNibiwgYXZhaWxhYmxlIGluIFtyZXN1bHRdXG4gICAgfVxuXG5hc3luYyBkZWYgbWFpbigpOlxuICAgIGNhdGFsb2cgPSBbXCI5NzgtMDAxXCIsIFwiOTc4LTAwMlwiLCBcIjk3OC0wMDNcIiwgXCI5NzgtMDA0XCJdXG4gICAgc3RhdHVzID0gYXdhaXQgYmF0Y2hfY2hlY2soY2F0YWxvZywgbGlicmFyeV9pZD0xKVxuICAgIHByaW50KHN0YXR1cylcblxuYXN5bmNpby5ydW4obWFpbigpKSJ9"
 width="100%"
></iframe>

## Conclusion

`asyncio.gather` is the main tool for running multiple coroutines concurrently and collecting all their results. Use `return_exceptions=True` when some may fail and you want all results. Use `asyncio.wait` when you need fine-grained control over which tasks finish first. The next lesson covers async context managers, which allow resources like database connections and HTTP sessions to be used safely in async code.
