## Introduction

Tara is ready to fix the leaking database connection. She knows `__enter__` opens the connection and `__exit__` closes it. She needs to make sure the connection is closed even if a query raises an exception. And since she is working with a real database, she also needs `__exit__` to roll back any in-progress transaction when an exception occurs, rather than leaving it in a half-committed state.

This lesson builds the full class-based context manager she needs, handling both the success path and the exception path correctly.

![A DBConnection context manager with __enter__ opening the connection and __exit__ closing it with a rollback path for exceptions and a commit path for success](images/03_class_based_context_manager.png)

## A Database Connection Context Manager

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-6-context-managers-03-writing-a-classbased-context-manager-001-978aaec502.html"
 width="100%"
></iframe>

The second block rolls back automatically. Without `ManagedConnection`, the connection would be left open and the half-completed transaction would need to be manually rolled back, or worse, left in an inconsistent state.

## Making the Connection Reusable With a Pattern

If the same connection is used across many operations, a context manager that closes the connection every time is too aggressive. A better pattern is a transaction manager that shares a long-lived connection but commits or rolls back individual transactions:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-6-context-managers-03-writing-a-classbased-context-manager-002-5916a7cded.html"
 width="100%"
></iframe>

## Tracking State Across Enter and Exit

`__enter__` and `__exit__` share state through `self`. Any data stored on the instance in `__enter__` is accessible in `__exit__`. This is the clean solution to the problem that `try`/`finally` often forces: declaring variables outside the `try` block and using them inside `finally`.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-6-context-managers-03-writing-a-classbased-context-manager-003-08b2507ba8.html"
 width="100%"
></iframe>

## Class-Based Context Manager at a Glance

| Step | Method | Typical actions |
|---|---|---|
| Setup | `__enter__` | Open file, acquire lock, start transaction, record time |
| Success path | `__exit__` with `exc_type is None` | Commit, flush, release cleanly |
| Failure path | `__exit__` with `exc_type` set | Rollback, log error, release anyway |
| Suppress exception | Return `True` from `__exit__` | Use deliberately and rarely |
| Propagate exception | Return `False` from `__exit__` | The usual behavior |

## Your Turn

Write a `TempDirectory` context manager that creates a temporary directory in `__enter__` (using the `tempfile` module: `tempfile.mkdtemp()`) and removes it with all its contents in `__exit__` (using `shutil.rmtree()`). Test it by creating a file inside the temporary directory during the `with` block, then confirming the directory and the file are both gone after the block exits.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-6-context-managers-03-writing-a-classbased-context-manager-004-8a217e9b1f.html"
 width="100%"
></iframe>

## Conclusion

A class-based context manager implements `__enter__` for setup and `__exit__` for teardown, with the exception arguments in `__exit__` allowing different behavior on success versus failure. State is shared between the two methods via `self`. This pattern is ideal when the setup involves multiple steps, the teardown is complex, or the manager needs to expose attributes (like `timer.elapsed`) after the block completes. The next lesson shows a shorter way to write simple context managers using `contextlib.contextmanager` and `yield`.
