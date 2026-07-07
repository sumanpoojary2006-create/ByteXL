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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-04-the-event-loop-001-5c187212be.html"
 width="100%"
></iframe>

Both tasks start, both yield, `B` resumes first (its wait is shorter), then `A` resumes.

## Getting the Event Loop

Inside an async function, `asyncio.get_event_loop()` returns the running event loop. You rarely need to access it directly; it is mainly used in advanced scenarios like scheduling callbacks or integrating with non-async code.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-04-the-event-loop-002-a99a10653c.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-04-the-event-loop-003-e1f2fdcb75.html"
 width="100%"
></iframe>

## Cooperative vs Preemptive Scheduling

In Python's async model, a task that never yields control will freeze all other tasks:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-04-the-event-loop-004-dcb254ad54.html"
 width="100%"
></iframe>

`urgent` cannot run until `runaway` yields. To allow other tasks to run inside a long computation, add `await asyncio.sleep(0)` at intervals. `asyncio.sleep(0)` yields control to the event loop without waiting.

## Mixing Sync and Async Code

An async program has one event loop running in one thread. Synchronous code blocks the loop; only code at `await` points yields. The boundary is always `asyncio.run()` at the top:

```
Synchronous world (regular Python)
    |
    +---> asyncio.run(main())
              |
              +---> Event loop
                        |
                        +---> async tasks, await, I/O
```

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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-10-asynchronous-programming-04-the-event-loop-005-95e0a244c9.html"
 width="100%"
></iframe>

Observe the output order: the cooperative tasks interleave their steps, while `fast_task("C")` cannot start until `slow_hog` finishes.

## Conclusion

The event loop is a single-threaded cooperative scheduler. Tasks run until they `await`, yield control, and resume when their awaited I/O completes. `asyncio.run` manages the loop lifecycle. Tasks that never `await` monopolize the thread and block all other tasks. The next lesson shows how to create, manage, and cancel `asyncio.Task` objects, which are the core unit of work the event loop schedules.
