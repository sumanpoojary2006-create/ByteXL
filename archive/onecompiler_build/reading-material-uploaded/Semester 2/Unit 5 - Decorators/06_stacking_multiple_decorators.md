## Introduction

Kiran has three decorators: `@add_timing`, `@require_auth`, and `@log_call`. She wants to apply all three to one endpoint handler. She writes:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-5-decorators-06-stacking-multiple-decorators-001-d907ab2070.html"
 width="100%"
></iframe>

It works. But the next morning she reads a bug report: the timing is measuring not just the function, but also the auth check. She realizes she does not fully know in which order the decorators applied, and whether that order matches her intent. This lesson makes it precise.

![Three decorator layers shown as nested boxes: log_call on the inside, require_auth around it, add_timing around that, with an arrow showing the execution order outward](images/06_stacking_multiple_decorators.png)

## Decorators Apply Bottom-Up at Definition Time

When Python processes a stacked decorator block, it applies the decorators **from bottom to top**: the decorator closest to the `def` runs first, its result is passed to the next decorator above, and so on.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-5-decorators-06-stacking-multiple-decorators-002-da74da4738.html"
 width="100%"
></iframe>

When Python processes this `def`:
1. `second(greet)` runs first (bottom-up), producing `second_wrapper`.
2. `first(second_wrapper)` runs next, producing `first_wrapper`.
3. `greet` now points to `first_wrapper`.

Calling `greet("Kiran")` produces:

```
first: before
second: before
Hello, Kiran
second: after
first: after
```

**Definition order (bottom-up) is reversed from execution order (top-down).** The outermost decorator in the stack runs first when the function is called.

## A Concrete Example: Auth, Then Log, Then Time

For Kiran's endpoint, the right design question is: what should happen when an unauthorized request arrives? If `@require_auth` is innermost (closest to `def`), it runs last, meaning timing and logging already ran before auth checked anything. If `@require_auth` is outermost (topmost in the source), it is the first thing called and can reject the request before the others run.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-5-decorators-06-stacking-multiple-decorators-003-367b521921.html"
 width="100%"
></iframe>

If Kiran wants the timer to only measure code that passed auth, she would put `@add_timing` *below* `@require_auth` (closer to `def`):

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-5-decorators-06-stacking-multiple-decorators-004-04ae19de3c.html"
 width="100%"
></iframe>

## The Mental Model: Nested Boxes

The clearest mental model is nested boxes. The decorator closest to `def` is the innermost box. Each decorator above it wraps around the previous layer.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-5-decorators-06-stacking-multiple-decorators-005-7a2baf1e45.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-5-decorators-06-stacking-multiple-decorators-006-b67facf294.html"
 width="100%"
></iframe>

Run `process(1000000)` and read the output. Then swap the decorator order to `@timed @logged` and run again. Note the difference in which message appears first. Explain which order makes `@logged` measure only the function's own time (not the overhead of `@timed`).

## Conclusion

Stacking decorators applies them bottom-up at definition time, creating a nesting of wrappers where the topmost decorator is the outermost layer at call time. The order has real semantic consequences: an auth check placed outermost can short-circuit before timing or logging run, while an auth check placed innermost is passed over until after other decorators have already done their work. The next lesson introduces class decorators: decorating a class definition itself rather than a function.
