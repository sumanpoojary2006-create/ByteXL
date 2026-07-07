## Introduction

Tara's file-handling code from Semester 1 always used `with open(...)` without really understanding why. She just knew it was the correct way and that forgetting it could leave files open. Now she is writing database code and her connection is leaking: when her query raises an exception, the connection is never closed, and the test environment eventually runs out of connections.

Her tech lead tells her the fix is the same pattern as `with open(...)`, but for her database. The `with` statement is not limited to files. It is a general mechanism for managing *any* resource that needs guaranteed cleanup, and this unit explains exactly how it works and how to build your own.

![A resource shown inside a with-block: a door opens (enter) when the with block starts, the body runs, and the door closes (exit) whether the body succeeded or raised an exception](images/01_with_statement_revisited.png)

## What the with Statement Guarantees

The `with` statement guarantees that a cleanup action runs, regardless of whether the body finishes normally, raises an exception, or even calls `return` inside a function. This guarantee is the entire reason `with open(...)` is preferred over manually calling `file.close()`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3RoZV93aXRoX3N0YXRlbWVudF9yZXZpc2l0ZWQgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6IiMgV2l0aG91dCB3aXRoOiB0aGUgY2xvc2UoKSBpcyBza2lwcGVkIGlmIGFuIGV4Y2VwdGlvbiBvY2N1cnNcbnRyeTpcbiAgICBmaWxlID0gb3BlbihcImNhdGFsb2cudHh0XCIsIFwiclwiKVxuICAgIGNvbnRlbnQgPSBmaWxlLnJlYWQoKVxuICAgIHByb2Nlc3MoY29udGVudCkgICAgICMgaWYgdGhpcyByYWlzZXMsIGNsb3NlKCkgYmVsb3cgbmV2ZXIgcnVuc1xuICAgIGZpbGUuY2xvc2UoKSAgICAgICAgICMgY2FuIGJlIHNraXBwZWRcbmV4Y2VwdCBFeGNlcHRpb246XG4gICAgcGFzc1xuXG4jIFdpdGggd2l0aDogY2xvc2UoKSBhbHdheXMgcnVuc1xud2l0aCBvcGVuKFwiY2F0YWxvZy50eHRcIiwgXCJyXCIpIGFzIGZpbGU6XG4gICAgY29udGVudCA9IGZpbGUucmVhZCgpXG4gICAgcHJvY2Vzcyhjb250ZW50KSAgICAgIyBpZiB0aGlzIHJhaXNlcywgdGhlIGZpbGUgaXMgc3RpbGwgY2xvc2VkIn0"
 width="100%"
></iframe>

The `with` statement's guarantee is unconditional: teardown always runs, even on exceptions, even on `break`, even on `return`. The `try`/`finally` equivalent shows this clearly:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3RoZV93aXRoX3N0YXRlbWVudF9yZXZpc2l0ZWQgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6ImZpbGUgPSBvcGVuKFwiY2F0YWxvZy50eHRcIiwgXCJyXCIpXG50cnk6XG4gICAgY29udGVudCA9IGZpbGUucmVhZCgpXG5maW5hbGx5OlxuICAgIGZpbGUuY2xvc2UoKSAgICMgZ3VhcmFudGVlZCB0byBydW4ifQ"
 width="100%"
></iframe>

`with` is syntactic sugar for this `try`/`finally` pattern, but cleaner and harder to get wrong.

## The Two Pieces: Enter and Exit

The `with` statement works by calling two methods on the object it receives: one to set up the resource (called when the `with` block starts) and one to tear it down (called when the block ends, no matter how).

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3RoZV93aXRoX3N0YXRlbWVudF9yZXZpc2l0ZWQgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6IndpdGggb3BlbihcImNhdGFsb2cudHh0XCIsIFwiclwiKSBhcyBmaWxlOlxuICAgICMgZmlsZSBpcyB0aGUgdmFsdWUgcmV0dXJuZWQgYnkgdGhlIFwiZW50ZXJcIiBzdGVwXG4gICAgY29udGVudCA9IGZpbGUucmVhZCgpXG4jIHRoZSBcImV4aXRcIiBzdGVwIHJ1bnMgaGVyZSwgdW5jb25kaXRpb25hbGx5In0"
 width="100%"
></iframe>

The `as file` clause captures the value returned by the setup step. The teardown step is called automatically, with information about whether an exception occurred. The names of these steps are `__enter__` and `__exit__`, and the next lesson explains exactly what they do.

## Multiple Context Managers in One With

Python allows multiple context managers in a single `with` statement, separated by commas. All setup steps run in order; all teardown steps run in reverse order.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3RoZV93aXRoX3N0YXRlbWVudF9yZXZpc2l0ZWQgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6IndpdGggb3BlbihcImlucHV0LnR4dFwiLCBcInJcIikgYXMgc291cmNlLCBvcGVuKFwib3V0cHV0LnR4dFwiLCBcIndcIikgYXMgZGVzdDpcbiAgICBmb3IgbGluZSBpbiBzb3VyY2U6XG4gICAgICAgIGRlc3Qud3JpdGUobGluZS51cHBlcigpKVxuIyBCb3RoIGZpbGVzIGFyZSBjbG9zZWQgaGVyZSwgZXZlbiBpZiBhbiBleGNlcHRpb24gb2NjdXJyZWQgbWlkLWNvcHkifQ"
 width="100%"
></iframe>

This is equivalent to nested `with` statements but more concise.

## The as Clause Is Optional

When a context manager's setup step does not return a useful value, the `as` clause can be omitted:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3RoZV93aXRoX3N0YXRlbWVudF9yZXZpc2l0ZWQgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6IiMgVGhlIGxvY2sgaXMgYWNxdWlyZWQgb24gZW50ZXIsIHJlbGVhc2VkIG9uIGV4aXQ7IG5vIHZhbHVlIGlzIG5lZWRlZFxuaW1wb3J0IHRocmVhZGluZ1xubG9jayA9IHRocmVhZGluZy5Mb2NrKClcblxud2l0aCBsb2NrOlxuICAgICMgY3JpdGljYWwgc2VjdGlvbjogb25seSBvbmUgdGhyZWFkIGF0IGEgdGltZVxuICAgIHVwZGF0ZV9zaGFyZWRfc3RhdGUoKSJ9"
 width="100%"
></iframe>

## The with Statement at a Glance

| Concept | What it means |
|---|---|
| Setup step | Called automatically when the `with` block starts |
| Body | Code inside the `with` block |
| Teardown step | Called automatically when the block ends, exception or not |
| `as name` | Binds the value returned by the setup step |
| Multiple managers | `with A() as a, B() as b:` runs both, tears down in reverse |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3RoZV93aXRoX3N0YXRlbWVudF9yZXZpc2l0ZWQgY29kZSA2IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA2LnB5IiwiY29kZSI6IiMgTWFudWFsIHJlc291cmNlIG1hbmFnZW1lbnQgLS0gZnJhZ2lsZVxuY2F0YWxvZyA9IG9wZW4oXCJjYXRhbG9nLnR4dFwiLCBcIndcIilcbmNhdGFsb2cud3JpdGUoXCJCb29rIEFcXG5Cb29rIEJcXG5cIilcbmNhdGFsb2cuY2xvc2UoKSAgICMgc2tpcHBlZCBpZiB3cml0ZSByYWlzZXNcblxuIyBDb250ZXh0IG1hbmFnZXIgdmVyc2lvblxud2l0aCBvcGVuKFwiY2F0YWxvZy50eHRcIiwgXCJ3XCIpIGFzIGNhdGFsb2c6XG4gICAgY2F0YWxvZy53cml0ZShcIkJvb2sgQVxcbkJvb2sgQlxcblwiKVxuIyBmaWxlIGlzIGNsb3NlZCBoZXJlIHJlZ2FyZGxlc3MifQ"
 width="100%"
></iframe>

Read both versions. Now deliberately cause an exception in the `write` call (e.g., write a non-string type and observe the `TypeError`). Confirm that with the manual version, the file handle may not be flushed or closed; with the `with` version, the cleanup runs correctly. Then look at your own Semester 1 file-handling code and identify any places where you used manual `open`/`close` that could be replaced with `with`.

## Conclusion

The `with` statement guarantees setup and teardown, regardless of exceptions. It is equivalent to `try`/`finally` but cleaner and harder to misuse. It works for any object that implements the two-method protocol Python calls when the block starts and ends. The next lesson names and explains those two methods: `__enter__` and `__exit__`, which together form the context manager protocol.
