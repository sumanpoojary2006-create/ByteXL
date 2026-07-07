## Introduction

Tara's connection leak was simple: one connection, one leak. As she builds out the library management system, she starts encountering more complex situations: multiple database connections and log files open at the same time, helper functions that open resources and need to return them to the caller, and code that conditionally opens resources depending on configuration.

These situations all have one thing in common: they make resource management harder to get right by hand. This lesson covers the patterns that keep resources safe even when the code grows complicated.

![A library system with connections, file handles, and locks shown as a stack of colored cards, each labeled with a resource type and held inside a single ExitStack](images/05_managing_resources_safely.png)

## The Golden Rule: Open Resources Inside With Blocks

The safest resource management pattern is to never use a resource outside the `with` block that created it. If a function needs a file, the `with` statement and the usage should both be in the same scope.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-6-context-managers-05-managing-resources-safely-001-1a147d6d28.html"
 width="100%"
></iframe>

When a function returns an open resource to its caller, it shifts responsibility for closing onto the caller, which may forget. The `@contextmanager` pattern avoids this by keeping the lifetime of the resource inside the generator:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-6-context-managers-05-managing-resources-safely-002-20f89ba722.html"
 width="100%"
></iframe>

## Handling Multiple Resources: ExitStack

Opening several resources at once with nested `with` statements works, but becomes hard to read and harder to make conditional:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-6-context-managers-05-managing-resources-safely-003-7f07ce3a9e.html"
 width="100%"
></iframe>

`contextlib.ExitStack` solves this. It holds a stack of context managers and tears them all down in reverse order when the stack exits:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-6-context-managers-05-managing-resources-safely-004-cc1b24947b.html"
 width="100%"
></iframe>

`ExitStack` is especially useful for opening a dynamic number of resources:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-6-context-managers-05-managing-resources-safely-005-84a4d9398c.html"
 width="100%"
></iframe>

## Cleanup When __enter__ Itself Can Fail

When multiple resources are opened one after the other and one of the later ones fails, the ones already opened must still be cleaned up. `ExitStack` handles this automatically: if `enter_context` raises on the third resource, the first two are still closed.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-6-context-managers-05-managing-resources-safely-006-7fe27a34cc.html"
 width="100%"
></iframe>

## Using Locks Safely

Locks from the `threading` module are context managers. The `with` statement acquires the lock on entry and releases it on exit, even if an exception occurs. Without this, a function that raises while holding a lock would cause every other thread to wait forever.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-6-context-managers-05-managing-resources-safely-007-840c89cc20.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-6-context-managers-05-managing-resources-safely-008-b1c12251d3.html"
 width="100%"
></iframe>

Now modify one catalog and confirm the result changes. Then remove one of the test files and observe that `ExitStack` still closes the first file cleanly even though the second `open` raises `FileNotFoundError`.

## Conclusion

The golden rule of resource management is: keep resource lifetimes inside `with` blocks. `ExitStack` removes the need for deeply nested `with` statements and handles dynamic lists of resources. It also guarantees cleanup when opening a later resource fails. The next lesson covers one more special power of context managers: suppressing exceptions selectively and guaranteeing that cleanup code runs even when the most extreme errors occur.
