## Introduction

Tara now knows that `with open(...)` works because Python calls two methods on the file object. She wants to know exactly what those methods are, what arguments they receive, and what their return values mean, so she can write something that works the same way for her database connection.

This lesson answers those questions precisely. The context manager protocol is two methods: `__enter__` and `__exit__`. Once you know what each one receives and returns, building your own context manager is mechanical.

![A with statement shown as a timeline: __enter__ fires at the left edge, the body runs in the middle, __exit__ fires at the right edge whether the body succeeded or raised](images/02_context_manager_protocol.png)

## __enter__: Setting Up the Resource

`__enter__(self)` is called when the `with` block starts. Its return value is what gets bound to the `as` variable.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3RoZV9jb250ZXh0X21hbmFnZXJfcHJvdG9jb2wgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6ImNsYXNzIFNpbXBsZVJlc291cmNlOlxuICAgIGRlZiBfX2VudGVyX18oc2VsZik6XG4gICAgICAgIHByaW50KFwiU2V0dGluZyB1cFwiKVxuICAgICAgICByZXR1cm4gc2VsZiAgICMgdGhpcyBpcyB3aGF0ICdhcyByZXNvdXJjZScgcmVjZWl2ZXNcblxuICAgIGRlZiBfX2V4aXRfXyhzZWxmLCBleGNfdHlwZSwgZXhjX3ZhbCwgZXhjX3RiKTpcbiAgICAgICAgcHJpbnQoXCJUZWFyaW5nIGRvd25cIilcbiAgICAgICAgcmV0dXJuIEZhbHNlICAjIGRvIG5vdCBzdXBwcmVzcyBleGNlcHRpb25zXG5cbndpdGggU2ltcGxlUmVzb3VyY2UoKSBhcyByZXNvdXJjZTpcbiAgICBwcmludChcIkluc2lkZSB0aGUgd2l0aCBibG9ja1wiKVxuICAgIHByaW50KGZcInJlc291cmNlIGlzOiB7cmVzb3VyY2V9XCIpXG5cbiMgT3V0cHV0OlxuIyBTZXR0aW5nIHVwXG4jIEluc2lkZSB0aGUgd2l0aCBibG9ja1xuIyByZXNvdXJjZSBpczogPF9fbWFpbl9fLlNpbXBsZVJlc291cmNlIG9iamVjdCBhdCAuLi4-XG4jIFRlYXJpbmcgZG93biJ9"
 width="100%"
></iframe>

`__enter__` can return anything: `self`, a completely different object (like a file object's `__enter__` returns the file itself), or `None` (if no value is needed).

## __exit__: Tearing Down and Handling Exceptions

`__exit__(self, exc_type, exc_val, exc_tb)` receives three arguments describing any exception that occurred inside the `with` block:

- `exc_type`: the exception class, or `None` if no exception occurred
- `exc_val`: the exception instance, or `None`
- `exc_tb`: the traceback object, or `None`

If the body completed without an exception, all three are `None`. If an exception occurred, all three carry information about it.

The return value of `__exit__` controls what happens to the exception:
- Return `False` (or `None`, or any falsy value): the exception propagates normally.
- Return `True`: the exception is suppressed (swallowed). Use this deliberately and rarely.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3RoZV9jb250ZXh0X21hbmFnZXJfcHJvdG9jb2wgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6ImNsYXNzIFNpbXBsZVJlc291cmNlOlxuICAgIGRlZiBfX2VudGVyX18oc2VsZik6XG4gICAgICAgIHByaW50KFwiU2V0dGluZyB1cFwiKVxuICAgICAgICByZXR1cm4gc2VsZlxuXG4gICAgZGVmIF9fZXhpdF9fKHNlbGYsIGV4Y190eXBlLCBleGNfdmFsLCBleGNfdGIpOlxuICAgICAgICBwcmludChmXCJUZWFyaW5nIGRvd24gfCBleGNlcHRpb246IHtleGNfdHlwZX1cIilcbiAgICAgICAgcmV0dXJuIEZhbHNlICAgIyBkbyBub3Qgc3VwcHJlc3NcblxuIyBObyBleGNlcHRpb246XG53aXRoIFNpbXBsZVJlc291cmNlKCk6XG4gICAgcHJpbnQoXCJOb3JtYWwgZXhpdFwiKVxuIyBTZXR0aW5nIHVwXG4jIE5vcm1hbCBleGl0XG4jIFRlYXJpbmcgZG93biB8IGV4Y2VwdGlvbjogTm9uZVxuXG4jIFdpdGggZXhjZXB0aW9uOlxudHJ5OlxuICAgIHdpdGggU2ltcGxlUmVzb3VyY2UoKTpcbiAgICAgICAgcmFpc2UgVmFsdWVFcnJvcihcIlNvbWV0aGluZyB3ZW50IHdyb25nXCIpXG5leGNlcHQgVmFsdWVFcnJvcjpcbiAgICBwcmludChcIkV4Y2VwdGlvbiBwcm9wYWdhdGVkIGFzIGV4cGVjdGVkXCIpXG4jIFNldHRpbmcgdXBcbiMgVGVhcmluZyBkb3duIHwgZXhjZXB0aW9uOiA8Y2xhc3MgJ1ZhbHVlRXJyb3InPlxuIyBFeGNlcHRpb24gcHJvcGFnYXRlZCBhcyBleHBlY3RlZCJ9"
 width="100%"
></iframe>

`__exit__` always runs. The `try`/`except` outside the `with` block catches the exception *after* `__exit__` has already been called.

## A Practical Protocol Demonstration: Timed Block

Here is a context manager that measures how long a code block takes:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3RoZV9jb250ZXh0X21hbmFnZXJfcHJvdG9jb2wgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6ImltcG9ydCB0aW1lXG5cbmNsYXNzIFRpbWVyOlxuICAgIGRlZiBfX2VudGVyX18oc2VsZik6XG4gICAgICAgIHNlbGYuX3N0YXJ0ID0gdGltZS5wZXJmX2NvdW50ZXIoKVxuICAgICAgICByZXR1cm4gc2VsZiAgICMgZ2l2ZXMgYWNjZXNzIHRvIGVsYXBzZWQgYWZ0ZXIgdGhlIGJsb2NrXG5cbiAgICBkZWYgX19leGl0X18oc2VsZiwgZXhjX3R5cGUsIGV4Y192YWwsIGV4Y190Yik6XG4gICAgICAgIHNlbGYuZWxhcHNlZCA9IHRpbWUucGVyZl9jb3VudGVyKCkgLSBzZWxmLl9zdGFydFxuICAgICAgICBwcmludChmXCJFbGFwc2VkOiB7c2VsZi5lbGFwc2VkOi40Zn1zXCIpXG4gICAgICAgIHJldHVybiBGYWxzZSAgICMgYWx3YXlzIGxldCBleGNlcHRpb25zIHByb3BhZ2F0ZVxuXG53aXRoIFRpbWVyKCkgYXMgdDpcbiAgICB0b3RhbCA9IHN1bShyYW5nZSgxXzAwMF8wMDApKVxuXG5wcmludChmXCJUb3RhbDoge3RvdGFsfSwgdG9vazoge3QuZWxhcHNlZDouNGZ9c1wiKSJ9"
 width="100%"
></iframe>

The `as t` clause makes `t` point to the `Timer` instance returned by `__enter__`. After the block, `t.elapsed` holds the measured time.

## What Makes a Valid Context Manager

An object is a valid context manager if it has both `__enter__` and `__exit__`. The `with` statement calls neither directly; it calls them through the protocol, which means any class implementing both methods works.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3RoZV9jb250ZXh0X21hbmFnZXJfcHJvdG9jb2wgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6ImNsYXNzIE51bGxDb250ZXh0OlxuICAgIFwiXCJcIkEgY29udGV4dCBtYW5hZ2VyIHRoYXQgZG9lcyBub3RoaW5nIC0tIHVzZWZ1bCBmb3Igb3B0aW9uYWwgbmVzdGluZy5cIlwiXCJcbiAgICBkZWYgX19lbnRlcl9fKHNlbGYpOlxuICAgICAgICByZXR1cm4gTm9uZVxuICAgIGRlZiBfX2V4aXRfXyhzZWxmLCAqYXJncyk6XG4gICAgICAgIHJldHVybiBGYWxzZSJ9"
 width="100%"
></iframe>

## The Context Manager Protocol at a Glance

| Method | When called | Arguments | Return value |
|---|---|---|---|
| `__enter__(self)` | When the `with` block starts | None | The value bound to `as` |
| `__exit__(self, exc_type, exc_val, exc_tb)` | When the block ends (any reason) | Exception info or three `None`s | `True` suppresses the exception; falsy propagates it |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3RoZV9jb250ZXh0X21hbmFnZXJfcHJvdG9jb2wgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6ImNsYXNzIFNhZmVXcml0ZXI6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIGZpbGVuYW1lKTpcbiAgICAgICAgc2VsZi5maWxlbmFtZSA9IGZpbGVuYW1lXG4gICAgICAgIHNlbGYuZmlsZSA9IE5vbmVcblxuICAgIGRlZiBfX2VudGVyX18oc2VsZik6XG4gICAgICAgIHNlbGYuZmlsZSA9IG9wZW4oc2VsZi5maWxlbmFtZSwgXCJ3XCIpXG4gICAgICAgIHJldHVybiBzZWxmLmZpbGVcblxuICAgIGRlZiBfX2V4aXRfXyhzZWxmLCBleGNfdHlwZSwgZXhjX3ZhbCwgZXhjX3RiKTpcbiAgICAgICAgaWYgc2VsZi5maWxlOlxuICAgICAgICAgICAgc2VsZi5maWxlLmNsb3NlKClcbiAgICAgICAgICAgIHByaW50KGZcIkNsb3NlZCB7c2VsZi5maWxlbmFtZX1cIilcbiAgICAgICAgaWYgZXhjX3R5cGUgaXMgbm90IE5vbmU6XG4gICAgICAgICAgICBwcmludChmXCJBbiBlcnJvciBvY2N1cnJlZDoge2V4Y192YWx9XCIpXG4gICAgICAgIHJldHVybiBGYWxzZSAgICMgZG8gbm90IHN1cHByZXNzIn0"
 width="100%"
></iframe>

Test this with a successful write (`with SafeWriter("test.txt") as f: f.write("hello")`), then test with a forced exception inside the block. Confirm the file is closed and the message is printed even when an exception occurs.

## Conclusion

`__enter__` runs when the `with` block starts and returns the value bound to `as`. `__exit__` runs unconditionally when the block ends and receives exception information if one occurred. Returning `False` (the default) lets exceptions propagate; returning `True` suppresses them. The next lesson shows how to use these two methods to build a complete, practical context manager for Tara's database connection.
