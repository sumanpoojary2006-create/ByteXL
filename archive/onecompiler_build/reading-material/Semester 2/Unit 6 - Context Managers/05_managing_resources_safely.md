## Introduction

Tara's connection leak was simple: one connection, one leak. As she builds out the library management system, she starts encountering more complex situations: multiple database connections and log files open at the same time, helper functions that open resources and need to return them to the caller, and code that conditionally opens resources depending on configuration.

These situations all have one thing in common: they make resource management harder to get right by hand. This lesson covers the patterns that keep resources safe even when the code grows complicated.

![A library system with connections, file handles, and locks shown as a stack of colored cards, each labeled with a resource type and held inside a single ExitStack](images/05_managing_resources_safely.png)

## The Golden Rule: Open Resources Inside With Blocks

The safest resource management pattern is to never use a resource outside the `with` block that created it. If a function needs a file, the `with` statement and the usage should both be in the same scope.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X21hbmFnaW5nX3Jlc291cmNlc19zYWZlbHkgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6ImRlZiBleHBvcnRfY2F0YWxvZyhwYXRoKTpcbiAgICB3aXRoIG9wZW4ocGF0aCwgXCJ3XCIpIGFzIGY6XG4gICAgICAgIGZvciBib29rIGluIGdldF9hbGxfYm9va3MoKTpcbiAgICAgICAgICAgIGYud3JpdGUoZlwie2Jvb2suaXNibn0se2Jvb2sudGl0bGV9XFxuXCIpXG4gICAgIyBmIGlzIGNsb3NlZCBoZXJlOyBubyBuZWVkIHRvIHRyYWNrIGl0IGZ1cnRoZXIifQ"
 width="100%"
></iframe>

When a function returns an open resource to its caller, it shifts responsibility for closing onto the caller, which may forget. The `@contextmanager` pattern avoids this by keeping the lifetime of the resource inside the generator:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X21hbmFnaW5nX3Jlc291cmNlc19zYWZlbHkgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6ImZyb20gY29udGV4dGxpYiBpbXBvcnQgY29udGV4dG1hbmFnZXJcblxuQGNvbnRleHRtYW5hZ2VyXG5kZWYgY2F0YWxvZ193cml0ZXIocGF0aCk6XG4gICAgd2l0aCBvcGVuKHBhdGgsIFwid1wiKSBhcyBmOlxuICAgICAgICB5aWVsZCBmICAgIyBjYWxsZXIgZ2V0cyBmLCBidXQgY2xvc2UoKSBpcyBvdXIgcmVzcG9uc2liaWxpdHlcblxuIyBDYWxsZXIgY2Fubm90IGZvcmdldCB0byBjbG9zZSAtLSB0aGUgd2l0aCBibG9jayBoYW5kbGVzIGl0XG53aXRoIGNhdGFsb2dfd3JpdGVyKFwiY2F0YWxvZy5jc3ZcIikgYXMgd3JpdGVyOlxuICAgIGZvciBib29rIGluIGdldF9hbGxfYm9va3MoKTpcbiAgICAgICAgd3JpdGVyLndyaXRlKGZcIntib29rLmlzYm59LHtib29rLnRpdGxlfVxcblwiKSJ9"
 width="100%"
></iframe>

## Handling Multiple Resources: ExitStack

Opening several resources at once with nested `with` statements works, but becomes hard to read and harder to make conditional:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X21hbmFnaW5nX3Jlc291cmNlc19zYWZlbHkgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6IiMgRGVlcGx5IG5lc3RlZCAtLSBmcmFnaWxlIGFuZCBoYXJkIHRvIHJlYWRcbndpdGggb3BlbihcInNvdXJjZS50eHRcIikgYXMgc3JjOlxuICAgIHdpdGggb3BlbihcImRlc3QudHh0XCIsIFwid1wiKSBhcyBkc3Q6XG4gICAgICAgIHdpdGggc3FsaXRlMy5jb25uZWN0KFwibGlicmFyeS5kYlwiKSBhcyBjb25uOlxuICAgICAgICAgICAgcHJvY2VzcyhzcmMsIGRzdCwgY29ubikifQ"
 width="100%"
></iframe>

`contextlib.ExitStack` solves this. It holds a stack of context managers and tears them all down in reverse order when the stack exits:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X21hbmFnaW5nX3Jlc291cmNlc19zYWZlbHkgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6ImZyb20gY29udGV4dGxpYiBpbXBvcnQgRXhpdFN0YWNrXG5pbXBvcnQgc3FsaXRlM1xuXG5kZWYgc3luY19jYXRhbG9nX3RvX2ZpbGUoZGJfcGF0aCwgb3V0cHV0X3BhdGgpOlxuICAgIHdpdGggRXhpdFN0YWNrKCkgYXMgc3RhY2s6XG4gICAgICAgIGNvbm4gPSBzdGFjay5lbnRlcl9jb250ZXh0KHNxbGl0ZTMuY29ubmVjdChkYl9wYXRoKSlcbiAgICAgICAgb3V0ID0gc3RhY2suZW50ZXJfY29udGV4dChvcGVuKG91dHB1dF9wYXRoLCBcIndcIikpXG5cbiAgICAgICAgYm9va3MgPSBjb25uLmV4ZWN1dGUoXCJTRUxFQ1QgaXNibiwgdGl0bGUgRlJPTSBib29rc1wiKS5mZXRjaGFsbCgpXG4gICAgICAgIGZvciBpc2JuLCB0aXRsZSBpbiBib29rczpcbiAgICAgICAgICAgIG91dC53cml0ZShmXCJ7aXNibn0se3RpdGxlfVxcblwiKVxuICAgICMgY29ubiBhbmQgb3V0IGFyZSBib3RoIGNsb3NlZCBoZXJlLCBpbiByZXZlcnNlIG9yZGVyXG5cbnN5bmNfY2F0YWxvZ190b19maWxlKFwiOm1lbW9yeTpcIiwgXCJjYXRhbG9nLmNzdlwiKSJ9"
 width="100%"
></iframe>

`ExitStack` is especially useful for opening a dynamic number of resources:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X21hbmFnaW5nX3Jlc291cmNlc19zYWZlbHkgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6ImRlZiBtZXJnZV9jYXRhbG9ncyhwYXRocywgb3V0cHV0X3BhdGgpOlxuICAgIHdpdGggRXhpdFN0YWNrKCkgYXMgc3RhY2s6XG4gICAgICAgIGhhbmRsZXMgPSBbc3RhY2suZW50ZXJfY29udGV4dChvcGVuKHApKSBmb3IgcCBpbiBwYXRoc11cbiAgICAgICAgb3V0ID0gc3RhY2suZW50ZXJfY29udGV4dChvcGVuKG91dHB1dF9wYXRoLCBcIndcIikpXG4gICAgICAgIGZvciBoYW5kbGUgaW4gaGFuZGxlczpcbiAgICAgICAgICAgIG91dC53cml0ZShoYW5kbGUucmVhZCgpKSJ9"
 width="100%"
></iframe>

## Cleanup When __enter__ Itself Can Fail

When multiple resources are opened one after the other and one of the later ones fails, the ones already opened must still be cleaned up. `ExitStack` handles this automatically: if `enter_context` raises on the third resource, the first two are still closed.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X21hbmFnaW5nX3Jlc291cmNlc19zYWZlbHkgY29kZSA2IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA2LnB5IiwiY29kZSI6IiMgRnJhZ2lsZTogaWYgb3BlbihcImxvZy50eHRcIikgcmFpc2VzLCBjb25uIGxlYWtzXG5jb25uID0gc3FsaXRlMy5jb25uZWN0KFwibGlicmFyeS5kYlwiKVxubG9nID0gb3BlbihcImxvZy50eHRcIiwgXCJ3XCIpICAgIyB3aGF0IGlmIHRoaXMgcmFpc2VzP1xuXG4jIFNhZmU6IEV4aXRTdGFjayByZWdpc3RlcnMgZWFjaCByZXNvdXJjZSBhcyBpdCBvcGVuczsgYW55IHRoYXQgb3BlbmVkIGFyZSBjbGVhbmVkIHVwXG53aXRoIEV4aXRTdGFjaygpIGFzIHN0YWNrOlxuICAgIGNvbm4gPSBzdGFjay5lbnRlcl9jb250ZXh0KHNxbGl0ZTMuY29ubmVjdChcImxpYnJhcnkuZGJcIikpXG4gICAgbG9nID0gc3RhY2suZW50ZXJfY29udGV4dChvcGVuKFwibG9nLnR4dFwiLCBcIndcIikpXG4gICAgIyBwcm9jZXNzIHVzaW5nIGNvbm4gYW5kIGxvZyJ9"
 width="100%"
></iframe>

## Using Locks Safely

Locks from the `threading` module are context managers. The `with` statement acquires the lock on entry and releases it on exit, even if an exception occurs. Without this, a function that raises while holding a lock would cause every other thread to wait forever.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X21hbmFnaW5nX3Jlc291cmNlc19zYWZlbHkgY29kZSA3IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA3LnB5IiwiY29kZSI6ImltcG9ydCB0aHJlYWRpbmdcblxuX2NhdGFsb2dfbG9jayA9IHRocmVhZGluZy5Mb2NrKClcbl9jYXRhbG9nOiBsaXN0ID0gW11cblxuZGVmIGFkZF9ib29rKGJvb2spOlxuICAgIHdpdGggX2NhdGFsb2dfbG9jazpcbiAgICAgICAgX2NhdGFsb2cuYXBwZW5kKGJvb2spICAgIyBsb2NrIGhlbGQgb25seSB3aGlsZSBhcHBlbmRpbmdcbiAgICAjIGxvY2sgcmVsZWFzZWQgaGVyZSwgZXZlbiBpZiBhcHBlbmQgc29tZWhvdyByYWlzZXNcblxuZGVmIGdldF9hbGxfYm9va3MoKTpcbiAgICB3aXRoIF9jYXRhbG9nX2xvY2s6XG4gICAgICAgIHJldHVybiBsaXN0KF9jYXRhbG9nKSAgICMgc25hcHNob3Qgd2hpbGUgaG9sZGluZyB0aGUgbG9jayJ9"
 width="100%"
></iframe>

## Resource Management at a Glance

| Scenario | Pattern |
|---|---|
| Single resource | `with open(path) as f:` |
| Resource returned to caller | `@contextmanager` that `yield`s it |
| Multiple resources | `ExitStack` with `enter_context` |
| Dynamic number of resources | `[stack.enter_context(open(p)) for p in paths]` |
| Thread lock | `with lock:` |

## Your Turn

Write a function `compare_catalogs(path_a, path_b)` that opens both files simultaneously using `ExitStack`, reads them, and returns whether they have the same content. Make sure both files are always closed, even if reading one of them raises an exception.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X21hbmFnaW5nX3Jlc291cmNlc19zYWZlbHkgY29kZSA4IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA4LnB5IiwiY29kZSI6ImZyb20gY29udGV4dGxpYiBpbXBvcnQgRXhpdFN0YWNrXG5cbmRlZiBjb21wYXJlX2NhdGFsb2dzKHBhdGhfYSwgcGF0aF9iKTpcbiAgICB3aXRoIEV4aXRTdGFjaygpIGFzIHN0YWNrOlxuICAgICAgICBmX2EgPSBzdGFjay5lbnRlcl9jb250ZXh0KG9wZW4ocGF0aF9hLCBcInJcIikpXG4gICAgICAgIGZfYiA9IHN0YWNrLmVudGVyX2NvbnRleHQob3BlbihwYXRoX2IsIFwiclwiKSlcbiAgICAgICAgcmV0dXJuIGZfYS5yZWFkKCkgPT0gZl9iLnJlYWQoKVxuXG4jIFRlc3QgaXQ6XG53aXRoIG9wZW4oXCJjYXRhbG9nX2EudHh0XCIsIFwid1wiKSBhcyBmOlxuICAgIGYud3JpdGUoXCJCb29rIEFcXG5Cb29rIEJcXG5cIilcbndpdGggb3BlbihcImNhdGFsb2dfYi50eHRcIiwgXCJ3XCIpIGFzIGY6XG4gICAgZi53cml0ZShcIkJvb2sgQVxcbkJvb2sgQlxcblwiKVxuXG5wcmludChjb21wYXJlX2NhdGFsb2dzKFwiY2F0YWxvZ19hLnR4dFwiLCBcImNhdGFsb2dfYi50eHRcIikpICAjIFRydWUifQ"
 width="100%"
></iframe>

Now modify one catalog and confirm the result changes. Then remove one of the test files and observe that `ExitStack` still closes the first file cleanly even though the second `open` raises `FileNotFoundError`.

## Conclusion

The golden rule of resource management is: keep resource lifetimes inside `with` blocks. `ExitStack` removes the need for deeply nested `with` statements and handles dynamic lists of resources. It also guarantees cleanup when opening a later resource fails. The next lesson covers one more special power of context managers: suppressing exceptions selectively and guaranteeing that cleanup code runs even when the most extreme errors occur.
