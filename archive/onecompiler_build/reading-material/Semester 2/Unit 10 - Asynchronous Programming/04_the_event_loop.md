## Introduction

Miguel can write `async def` functions and `await` them, but he does not have a mental model for what is actually happening. When three tasks are running "concurrently," what is doing the scheduling? What decides which task runs next when one pauses? The answer is the event loop, and understanding it makes async programs much easier to reason about.

![A circular diagram showing the event loop cycling through ready tasks: run task A until it awaits, suspend A, run task B until it awaits, suspend B, check for completed I/O, wake up A, repeat](images/04_event_loop.png)

## What the Event Loop Is

The event loop is a loop that runs in a single thread. On each iteration, it:

1. Picks a task that is ready to run (not waiting for I/O)
2. Runs it until it either completes or reaches an `await` that is not yet ready
3. If the task reached an `await`, registers it to be resumed when the awaited I/O completes
4. Picks the next ready task and runs it
5. Repeats

This is cooperative scheduling: tasks voluntarily yield control by using `await`. No task can be preempted (forcibly paused) by the event loop.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3RoZV9ldmVudF9sb29wIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJpbXBvcnQgYXN5bmNpb1xuXG5hc3luYyBkZWYgdGFza19hKCk6XG4gICAgcHJpbnQoXCJBOiBzdGFydFwiKVxuICAgIGF3YWl0IGFzeW5jaW8uc2xlZXAoMC41KSAgICMgeWllbGRzIHRvIGV2ZW50IGxvb3AgaGVyZVxuICAgIHByaW50KFwiQTogcmVzdW1lZFwiKVxuXG5hc3luYyBkZWYgdGFza19iKCk6XG4gICAgcHJpbnQoXCJCOiBzdGFydFwiKVxuICAgIGF3YWl0IGFzeW5jaW8uc2xlZXAoMC4xKSAgICMgeWllbGRzIHRvIGV2ZW50IGxvb3AgaGVyZVxuICAgIHByaW50KFwiQjogcmVzdW1lZFwiKVxuXG5hc3luYyBkZWYgbWFpbigpOlxuICAgIGF3YWl0IGFzeW5jaW8uZ2F0aGVyKHRhc2tfYSgpLCB0YXNrX2IoKSlcblxuYXN5bmNpby5ydW4obWFpbigpKVxuIyBPdXRwdXQ6XG4jIEE6IHN0YXJ0XG4jIEI6IHN0YXJ0XG4jIEI6IHJlc3VtZWQgICAgKEIncyBzaG9ydGVyIHdhaXQgY29tcGxldGVzIGZpcnN0KVxuIyBBOiByZXN1bWVkICAgIChBIHJlc3VtZXMgd2hlbiBpdHMgMC41cyB3YWl0IGNvbXBsZXRlcykifQ"
 width="100%"
></iframe>

Both tasks start, both yield, `B` resumes first (its wait is shorter), then `A` resumes.

## Getting the Event Loop

Inside an async function, `asyncio.get_event_loop()` returns the running event loop. You rarely need to access it directly; it is mainly used in advanced scenarios like scheduling callbacks or integrating with non-async code.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3RoZV9ldmVudF9sb29wIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJhc3luYyBkZWYgaW5zcGVjdF9sb29wKCk6XG4gICAgbG9vcCA9IGFzeW5jaW8uZ2V0X2V2ZW50X2xvb3AoKVxuICAgIHByaW50KGZcIlJ1bm5pbmc6IHtsb29wLmlzX3J1bm5pbmcoKX1cIikgICAjIFRydWVcblxuICAgICMgU2NoZWR1bGUgc29tZXRoaW5nIHRvIHJ1biBcInNvb25cIiB3aXRob3V0IHdhaXRpbmcgZm9yIGl0XG4gICAgbG9vcC5jYWxsX3Nvb24obGFtYmRhOiBwcmludChcIlNjaGVkdWxlZCBjYWxsYmFjayByYW5cIikpXG4gICAgYXdhaXQgYXN5bmNpby5zbGVlcCgwKSAgICMgeWllbGQgdG8gbGV0IHRoZSBjYWxsYmFjayBydW4ifQ"
 width="100%"
></iframe>

`asyncio.get_running_loop()` (Python 3.7+) is the preferred, safer version: it raises `RuntimeError` if there is no running event loop, while `get_event_loop()` may create a new one in some contexts.

## asyncio.run and the Event Loop Lifecycle

`asyncio.run(main())`:
1. Creates a new event loop
2. Sets it as the current event loop
3. Runs `main()` to completion
4. Cancels any remaining tasks
5. Closes the event loop

Do not nest `asyncio.run` calls. Do not create multiple event loops manually. `asyncio.run` is the clean entry point.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3RoZV9ldmVudF9sb29wIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiIjIFdST05HOiBuZXN0aW5nIGFzeW5jaW8ucnVuXG5hc3luYyBkZWYgYmFkKCk6XG4gICAgYXN5bmNpby5ydW4oc29tZXRoaW5nX2Vsc2UoKSkgICAjIFJ1bnRpbWVFcnJvcjogYWxyZWFkeSBydW5uaW5nXG5cbiMgQ09SUkVDVDogdXNlIGF3YWl0IGluc3RlYWRcbmFzeW5jIGRlZiBnb29kKCk6XG4gICAgYXdhaXQgc29tZXRoaW5nX2Vsc2UoKSJ9"
 width="100%"
></iframe>

## Cooperative vs Preemptive Scheduling

In Python's async model, a task that never yields control will freeze all other tasks:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3RoZV9ldmVudF9sb29wIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJhc3luYyBkZWYgcnVuYXdheSgpOlxuICAgIGZvciBpIGluIHJhbmdlKDFfMDAwXzAwMCk6XG4gICAgICAgICMgTm8gYXdhaXQgaW5zaWRlIC0tIGV2ZW50IGxvb3AgY2Fubm90IHN3aXRjaCB0byBvdGhlciB0YXNrc1xuICAgICAgICByZXN1bHQgPSBpICogaVxuICAgIHByaW50KFwiRmluYWxseSBkb25lXCIpXG5cbmFzeW5jIGRlZiB1cmdlbnQoKTpcbiAgICBhd2FpdCBhc3luY2lvLnNsZWVwKDApICAgIyB5aWVsZHM7IHNob3VsZCBydW4gcXVpY2tseVxuICAgIHByaW50KFwiVXJnZW50IHRhc2sgcmFuXCIpXG5cbmFzeW5jIGRlZiBtYWluKCk6XG4gICAgYXdhaXQgYXN5bmNpby5nYXRoZXIocnVuYXdheSgpLCB1cmdlbnQoKSlcbiAgICAjIFwidXJnZW50XCIgcHJpbnRzIGFmdGVyIFwicnVuYXdheVwiIGZpbmlzaGVzLCBub3QgYmV0d2VlbiBpdGVyYXRpb25zIn0"
 width="100%"
></iframe>

`urgent` cannot run until `runaway` yields. To allow other tasks to run inside a long computation, add `await asyncio.sleep(0)` at intervals. `asyncio.sleep(0)` yields control to the event loop without waiting.

## Mixing Sync and Async Code

An async program has one event loop running in one thread. Synchronous code blocks the loop; only code at `await` points yields. The boundary is always `asyncio.run()` at the top:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3RoZV9ldmVudF9sb29wIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJTeW5jaHJvbm91cyB3b3JsZCAocmVndWxhciBQeXRob24pXG4gICAgfFxuICAgICstLS0-IGFzeW5jaW8ucnVuKG1haW4oKSlcbiAgICAgICAgICAgICAgfFxuICAgICAgICAgICAgICArLS0tPiBFdmVudCBsb29wXG4gICAgICAgICAgICAgICAgICAgICAgICB8XG4gICAgICAgICAgICAgICAgICAgICAgICArLS0tPiBhc3luYyB0YXNrcywgYXdhaXQsIEkvTyJ9"
 width="100%"
></iframe>

You can call sync functions from async code. You cannot call `await` from sync code (outside the event loop).

## The Event Loop at a Glance

| Concept | What it means |
|---|---|
| Event loop | Single-threaded scheduler for async tasks |
| Cooperative scheduling | Tasks yield at `await`; not forcibly preempted |
| `asyncio.run(coro)` | Create loop, run coro, close loop |
| `asyncio.sleep(0)` | Yield control without actually waiting |
| `asyncio.get_running_loop()` | Access the current running loop |
| Runaway task | A task that never yields; freezes other tasks |

## Your Turn

Write an experiment that demonstrates cooperative scheduling:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3RoZV9ldmVudF9sb29wIGNvZGUgNiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNi5weSIsImNvZGUiOiJpbXBvcnQgYXN5bmNpb1xuXG5hc3luYyBkZWYgZmFzdF90YXNrKG5hbWUsIG4pOlxuICAgIGZvciBpIGluIHJhbmdlKG4pOlxuICAgICAgICBhd2FpdCBhc3luY2lvLnNsZWVwKDApICAgIyB5aWVsZCBvbiBlYWNoIGl0ZXJhdGlvblxuICAgICAgICBwcmludChmXCJ7bmFtZX06IHN0ZXAge2l9XCIpXG5cbmFzeW5jIGRlZiBzbG93X2hvZyhuKTpcbiAgICBmb3IgaSBpbiByYW5nZShuKTpcbiAgICAgICAgcGFzcyAgICMgbm8geWllbGQgLS0gbW9ub3BvbGl6ZXMgdGhlIGV2ZW50IGxvb3BcbiAgICBwcmludChcImhvZzogZG9uZVwiKVxuXG5hc3luYyBkZWYgbWFpbigpOlxuICAgIHByaW50KFwiLS0tIGNvb3BlcmF0aXZlIChpbnRlcmxlYXZlZCkgLS0tXCIpXG4gICAgYXdhaXQgYXN5bmNpby5nYXRoZXIoZmFzdF90YXNrKFwiQVwiLCAzKSwgZmFzdF90YXNrKFwiQlwiLCAzKSlcblxuICAgIHByaW50KFwiXFxuLS0tIGhvZyB2cyBmYXN0IHRhc2sgLS0tXCIpXG4gICAgYXdhaXQgYXN5bmNpby5nYXRoZXIoc2xvd19ob2coMV8wMDBfMDAwKSwgZmFzdF90YXNrKFwiQ1wiLCAzKSkifQ"
 width="100%"
></iframe>

Observe the output order: the cooperative tasks interleave their steps, while `fast_task("C")` cannot start until `slow_hog` finishes.

## Conclusion

The event loop is a single-threaded cooperative scheduler. Tasks run until they `await`, yield control, and resume when their awaited I/O completes. `asyncio.run` manages the loop lifecycle. Tasks that never `await` monopolize the thread and block all other tasks. The next lesson shows how to create, manage, and cancel `asyncio.Task` objects, which are the core unit of work the event loop schedules.
