## Introduction

Kiran has three decorators: `@add_timing`, `@require_auth`, and `@log_call`. She wants to apply all three to one endpoint handler. She writes:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3N0YWNraW5nX211bHRpcGxlX2RlY29yYXRvcnMgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6IkBhZGRfdGltaW5nXG5AcmVxdWlyZV9hdXRoXG5AbG9nX2NhbGxcbmRlZiBnZXRfYm9vayhpc2JuKTpcbiAgICByZXR1cm4gbG9va3VwKGlzYm4pIn0"
 width="100%"
></iframe>

It works. But the next morning she reads a bug report: the timing is measuring not just the function, but also the auth check. She realizes she does not fully know in which order the decorators applied, and whether that order matches her intent. This lesson makes it precise.

![Three decorator layers shown as nested boxes: log_call on the inside, require_auth around it, add_timing around that, with an arrow showing the execution order outward](images/06_stacking_multiple_decorators.png)

## Decorators Apply Bottom-Up at Definition Time

When Python processes a stacked decorator block, it applies the decorators **from bottom to top**: the decorator closest to the `def` runs first, its result is passed to the next decorator above, and so on.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3N0YWNraW5nX211bHRpcGxlX2RlY29yYXRvcnMgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6ImRlZiBmaXJzdChmbik6XG4gICAgcHJpbnQoZlwiQXBwbHlpbmcgZmlyc3QgdG8ge2ZuLl9fbmFtZV9ffVwiKVxuICAgIGRlZiB3cmFwcGVyKCphcmdzLCAqKmt3YXJncyk6XG4gICAgICAgIHByaW50KFwiZmlyc3Q6IGJlZm9yZVwiKVxuICAgICAgICByZXN1bHQgPSBmbigqYXJncywgKiprd2FyZ3MpXG4gICAgICAgIHByaW50KFwiZmlyc3Q6IGFmdGVyXCIpXG4gICAgICAgIHJldHVybiByZXN1bHRcbiAgICByZXR1cm4gd3JhcHBlclxuXG5kZWYgc2Vjb25kKGZuKTpcbiAgICBwcmludChmXCJBcHBseWluZyBzZWNvbmQgdG8ge2ZuLl9fbmFtZV9ffVwiKVxuICAgIGRlZiB3cmFwcGVyKCphcmdzLCAqKmt3YXJncyk6XG4gICAgICAgIHByaW50KFwic2Vjb25kOiBiZWZvcmVcIilcbiAgICAgICAgcmVzdWx0ID0gZm4oKmFyZ3MsICoqa3dhcmdzKVxuICAgICAgICBwcmludChcInNlY29uZDogYWZ0ZXJcIilcbiAgICAgICAgcmV0dXJuIHJlc3VsdFxuICAgIHJldHVybiB3cmFwcGVyXG5cbkBmaXJzdFxuQHNlY29uZFxuZGVmIGdyZWV0KG5hbWUpOlxuICAgIHByaW50KGZcIkhlbGxvLCB7bmFtZX1cIilcbiAgICByZXR1cm4gbmFtZSJ9"
 width="100%"
></iframe>

When Python processes this `def`:
1. `second(greet)` runs first (bottom-up), producing `second_wrapper`.
2. `first(second_wrapper)` runs next, producing `first_wrapper`.
3. `greet` now points to `first_wrapper`.

Calling `greet("Kiran")` produces:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3N0YWNraW5nX211bHRpcGxlX2RlY29yYXRvcnMgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6ImZpcnN0OiBiZWZvcmVcbnNlY29uZDogYmVmb3JlXG5IZWxsbywgS2lyYW5cbnNlY29uZDogYWZ0ZXJcbmZpcnN0OiBhZnRlciJ9"
 width="100%"
></iframe>

**Definition order (bottom-up) is reversed from execution order (top-down).** The outermost decorator in the stack runs first when the function is called.

## A Concrete Example: Auth, Then Log, Then Time

For Kiran's endpoint, the right design question is: what should happen when an unauthorized request arrives? If `@require_auth` is innermost (closest to `def`), it runs last, meaning timing and logging already ran before auth checked anything. If `@require_auth` is outermost (topmost in the source), it is the first thing called and can reject the request before the others run.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3N0YWNraW5nX211bHRpcGxlX2RlY29yYXRvcnMgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6ImltcG9ydCBmdW5jdG9vbHNcblxuZGVmIHJlcXVpcmVfYXV0aChmbik6XG4gICAgQGZ1bmN0b29scy53cmFwcyhmbilcbiAgICBkZWYgd3JhcHBlcigqYXJncywgKiprd2FyZ3MpOlxuICAgICAgICB0b2tlbiA9IGt3YXJncy5nZXQoXCJ0b2tlblwiKVxuICAgICAgICBpZiB0b2tlbiAhPSBcInZhbGlkLXRva2VuXCI6XG4gICAgICAgICAgICByYWlzZSBQZXJtaXNzaW9uRXJyb3IoXCJVbmF1dGhvcml6ZWRcIilcbiAgICAgICAgcmV0dXJuIGZuKCphcmdzLCAqKmt3YXJncylcbiAgICByZXR1cm4gd3JhcHBlclxuXG5kZWYgYWRkX3RpbWluZyhmbik6XG4gICAgQGZ1bmN0b29scy53cmFwcyhmbilcbiAgICBkZWYgd3JhcHBlcigqYXJncywgKiprd2FyZ3MpOlxuICAgICAgICBpbXBvcnQgdGltZVxuICAgICAgICBzdGFydCA9IHRpbWUudGltZSgpXG4gICAgICAgIHJlc3VsdCA9IGZuKCphcmdzLCAqKmt3YXJncylcbiAgICAgICAgcHJpbnQoZlwie2ZuLl9fbmFtZV9ffSByYW4gaW4ge3RpbWUudGltZSgpIC0gc3RhcnQ6LjRmfXNcIilcbiAgICAgICAgcmV0dXJuIHJlc3VsdFxuICAgIHJldHVybiB3cmFwcGVyXG5cbkBhZGRfdGltaW5nICAgICAgICAgIyBvdXRlcm1vc3Q6IHJ1bnMgZmlyc3Qgb24gY2FsbFxuQHJlcXVpcmVfYXV0aCAgICAgICAjIG1pZGRsZTogcnVucyBzZWNvbmRcbmRlZiBnZXRfYm9vayhpc2JuLCB0b2tlbj1Ob25lKTpcbiAgICByZXR1cm4ge1wiaXNiblwiOiBpc2JuLCBcInRpdGxlXCI6IFwiRHVuZVwifVxuXG4jIENhbGwgd2l0aCB2YWxpZCB0b2tlbjpcbmJvb2sgPSBnZXRfYm9vayhcIjk3OC0wNDQxMDEzNTkzXCIsIHRva2VuPVwidmFsaWQtdG9rZW5cIilcbiMgZ2V0X2Jvb2sgcmFuIGluIDAuMDAwMXNcblxuIyBDYWxsIHdpdGhvdXQgdG9rZW46XG50cnk6XG4gICAgZ2V0X2Jvb2soXCI5NzgtMDQ0MTAxMzU5M1wiKVxuZXhjZXB0IFBlcm1pc3Npb25FcnJvciBhcyBlOlxuICAgIHByaW50KGUpICAgICMgVW5hdXRob3JpemVkIC0tIGFkZF90aW1pbmcgc3RpbGwgcmFuLCBidXQgYXV0aCBzdG9wcGVkIGl0In0"
 width="100%"
></iframe>

If Kiran wants the timer to only measure code that passed auth, she would put `@add_timing` *below* `@require_auth` (closer to `def`):

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3N0YWNraW5nX211bHRpcGxlX2RlY29yYXRvcnMgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6IkByZXF1aXJlX2F1dGggICAgICAgIyBvdXRlcm1vc3Q6IHJlamVjdHMgZWFybHkgYmVmb3JlIHRpbWluZ1xuQGFkZF90aW1pbmcgICAgICAgICAjIGlubmVyOiBvbmx5IHRpbWVzIHdoYXQgcGFzc2VkIGF1dGhcbmRlZiBnZXRfYm9vayhpc2JuLCB0b2tlbj1Ob25lKTpcbiAgICByZXR1cm4ge1wiaXNiblwiOiBpc2JufSJ9"
 width="100%"
></iframe>

## The Mental Model: Nested Boxes

The clearest mental model is nested boxes. The decorator closest to `def` is the innermost box. Each decorator above it wraps around the previous layer.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3N0YWNraW5nX211bHRpcGxlX2RlY29yYXRvcnMgY29kZSA2IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA2LnB5IiwiY29kZSI6IkBBXG5AQlxuQENcbmRlZiBmbigpOlxuICAgIHBhc3NcblxuIyBmbiA9IEEoQihDKGZuKSkpXG4jIENhbGwgY2hhaW46IEEud3JhcHBlciAtPiBCLndyYXBwZXIgLT4gQy53cmFwcGVyIC0-IGZuIn0"
 width="100%"
></iframe>

Reading `@A @B @C def fn` translates directly to `fn = A(B(C(fn)))`, which is the exact mathematical composition.

## Stacking Decorators at a Glance

| Rule | Detail |
|---|---|
| Application order | Bottom-up: decorator closest to `def` runs first |
| Execution order | Top-down: outermost decorator runs first on call |
| Equivalent expression | `@A @B @C def fn` = `fn = A(B(C(fn)))` |
| Practical effect | Outermost decorator controls entry and can short-circuit |
| Best practice | Use `@functools.wraps(fn)` at every level |

## Your Turn

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3N0YWNraW5nX211bHRpcGxlX2RlY29yYXRvcnMgY29kZSA3IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA3LnB5IiwiY29kZSI6ImltcG9ydCBmdW5jdG9vbHNcblxuZGVmIGxvZ2dlZChmbik6XG4gICAgQGZ1bmN0b29scy53cmFwcyhmbilcbiAgICBkZWYgd3JhcHBlcigqYXJncywgKiprd2FyZ3MpOlxuICAgICAgICBwcmludChmXCJMT0c6IHtmbi5fX25hbWVfX30gY2FsbGVkXCIpXG4gICAgICAgIHJldHVybiBmbigqYXJncywgKiprd2FyZ3MpXG4gICAgcmV0dXJuIHdyYXBwZXJcblxuZGVmIHRpbWVkKGZuKTpcbiAgICBAZnVuY3Rvb2xzLndyYXBzKGZuKVxuICAgIGRlZiB3cmFwcGVyKCphcmdzLCAqKmt3YXJncyk6XG4gICAgICAgIGltcG9ydCB0aW1lXG4gICAgICAgIHN0YXJ0ID0gdGltZS50aW1lKClcbiAgICAgICAgcmVzdWx0ID0gZm4oKmFyZ3MsICoqa3dhcmdzKVxuICAgICAgICBwcmludChmXCJUSU1FOiB7Zm4uX19uYW1lX199ID0ge3RpbWUudGltZSgpIC0gc3RhcnQ6LjRmfXNcIilcbiAgICAgICAgcmV0dXJuIHJlc3VsdFxuICAgIHJldHVybiB3cmFwcGVyXG5cbkBsb2dnZWRcbkB0aW1lZFxuZGVmIHByb2Nlc3Mobik6XG4gICAgcmV0dXJuIHN1bShyYW5nZShuKSkifQ"
 width="100%"
></iframe>

Run `process(1000000)` and read the output. Then swap the decorator order to `@timed @logged` and run again. Note the difference in which message appears first. Explain which order makes `@logged` measure only the function's own time (not the overhead of `@timed`).

## Conclusion

Stacking decorators applies them bottom-up at definition time, creating a nesting of wrappers where the topmost decorator is the outermost layer at call time. The order has real semantic consequences: an auth check placed outermost can short-circuit before timing or logging run, while an auth check placed innermost is passed over until after other decorators have already done their work. The next lesson introduces class decorators: decorating a class definition itself rather than a function.
