## Introduction

Naveen has a list of pending dues he wants sorted by amount, just this once, for a single report he is printing right now. Writing a full `def` block, naming it something like `get_amount`, and never using that name again anywhere else in the script feels like a lot of ceremony for a function that exists for exactly one line of work. He just wants to tell Python, right there in the sorting call, "use the amount to compare these."

Python's answer is the **lambda**, a small, anonymous function written in a single expression, used exactly where it is needed and then forgotten.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/06_lambda_inline_function.png)

## The Shape of a Lambda

A lambda is written as the keyword `lambda`, followed by its parameters, a colon, and a single expression whose result it returns automatically.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2xhbWJkYSBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoic3F1YXJlID0gbGFtYmRhIHg6IHggKiB4XG5wcmludChzcXVhcmUoNSkpICAgICMgMjUifQ"
 width="100%"
></iframe>

Compare this to the equivalent `def` version, to see exactly what the lambda is shorthand for.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2xhbWJkYSBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoiZGVmIHNxdWFyZSh4KTpcbiAgICByZXR1cm4geCAqIHgifQ"
 width="100%"
></iframe>

Both do the same job. The `lambda` version skips the `def`, the function name, and the explicit `return`, because a lambda's single expression is always, automatically, what gets returned.

## Lambdas Can Take Several Parameters

Just like an ordinary function, a lambda can take more than one parameter, separated by commas, before the colon.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2xhbWJkYSBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoiYWRkID0gbGFtYmRhIGEsIGI6IGEgKyBiXG5wcmludChhZGQoMywgNCkpICAgICMgNyJ9"
 width="100%"
></iframe>

There is still only ever one expression after the colon; a lambda cannot hold several lines, a loop, or an `if` statement the way a full `def` function can. That restriction is intentional: a lambda is meant for something this small, and anything bigger belongs in a proper `def` function instead.

## Where Lambdas Actually Shine: As an Argument

Writing `square = lambda x: x * x` and then calling `square(5)` later is legal, but it throws away the lambda's real advantage. A lambda's natural home is being passed directly into another function, on the spot, with no name of its own at all. The clearest example is `sorted()`'s `key` argument, which expects a function that says "what should I compare each item by?"

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2xhbWJkYSBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoiZHVlcyA9IFsoXCJBc2hhXCIsIDMwMCksIChcIlJhdmlcIiwgMTUwKSwgKFwiTWVlcmFcIiwgNDUwKV1cblxuYnlfYW1vdW50ID0gc29ydGVkKGR1ZXMsIGtleT1sYW1iZGEgcGVyc29uOiBwZXJzb25bMV0pXG5wcmludChieV9hbW91bnQpICAgICMgWygnUmF2aScsIDE1MCksICgnQXNoYScsIDMwMCksICgnTWVlcmEnLCA0NTApXSJ9"
 width="100%"
></iframe>

Here the lambda takes one tuple, `person`, and returns its second item, the amount, telling `sorted()` exactly what to compare. Writing a separate, named `def` function purely to be used once, right here, would be more ceremony than the job deserves.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/06_lambda_sort_key.png)


## A Lambda Is Still Just a Value

Because a lambda is an expression, it can be stored in a variable, put inside a list, or passed around exactly like any other value, including a number or a string.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2xhbWJkYSBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoib3BlcmF0aW9ucyA9IHtcbiAgICBcImFkZFwiOiBsYW1iZGEgYSwgYjogYSArIGIsXG4gICAgXCJzdWJ0cmFjdFwiOiBsYW1iZGEgYSwgYjogYSAtIGIsXG59XG5cbnByaW50KG9wZXJhdGlvbnNbXCJhZGRcIl0oMTAsIDQpKSAgICAgICAgICMgMTRcbnByaW50KG9wZXJhdGlvbnNbXCJzdWJ0cmFjdFwiXSgxMCwgNCkpICAgICMgNiJ9"
 width="100%"
></iframe>

A dictionary of lambdas like this is a neat way to select between several tiny calculations by name, without writing an `if`/`elif` chain to choose between them.

## Lambdas at a Glance

| Situation | Better Choice |
|---|---|
| A single, short expression, used once, often as an argument | Lambda |
| Several lines of logic, a loop, or conditions | A regular `def` function |
| You want to call it again later under a clear name | A regular `def` function |
| Sorting or filtering with a quick custom key | Lambda |

## Your Turn: Sort and Pick With a Lambda

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2xhbWJkYSBjb2RlIDYiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDYucHkiLCJjb2RlIjoic2NvcmVzID0gWyhcIkFzaGFcIiwgOTIpLCAoXCJSYXZpXCIsIDc4KSwgKFwiTWVlcmFcIiwgODgpXVxuXG5oaWdoZXN0X2ZpcnN0ID0gc29ydGVkKHNjb3Jlcywga2V5PWxhbWJkYSBzdHVkZW50OiBzdHVkZW50WzFdLCByZXZlcnNlPVRydWUpXG5wcmludChoaWdoZXN0X2ZpcnN0KVxuXG50b3Bfc2NvcmVyID0gbWF4KHNjb3Jlcywga2V5PWxhbWJkYSBzdHVkZW50OiBzdHVkZW50WzFdKVxucHJpbnQoXCJUb3Agc2NvcmVyOlwiLCB0b3Bfc2NvcmVyKSJ9"
 width="100%"
></iframe>

Notice the very same small lambda idea, "compare by the score," answers two different questions here: the full sorted order, and the single best entry.

## Conclusion

A lambda is a small, anonymous, single-expression function, written as `lambda parameters: expression`, whose result is returned automatically with no explicit `return` needed. Lambdas are at their best when passed directly into another function, such as the `key` argument of `sorted()` or `max()`, for a quick comparison that does not deserve a full named definition. Reach for a regular `def` function the moment the logic needs more than one expression. The next lesson puts lambdas to work alongside three classic tools built specifically to take a function as an argument: `map`, `filter`, and `reduce`.
