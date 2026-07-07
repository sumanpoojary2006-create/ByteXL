## Introduction

Naveen has a list of pending dues he wants sorted by amount, just this once, for a single report he is printing right now. Writing a full `def` block, naming it something like `get_amount`, and never using that name again anywhere else in the script feels like a lot of ceremony for a function that exists for exactly one line of work. He just wants to tell Python, right there in the sorting call, "use the amount to compare these."

Python's answer is the **lambda**, a small, anonymous function written in a single expression, used exactly where it is needed and then forgotten.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/06_lambda_inline_function.png)

## The Shape of a Lambda

A lambda is written as the keyword `lambda`, followed by its parameters, a colon, and a single expression whose result it returns automatically.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-8-functions-06-lambda-001-55ec9f81c2.html"
 width="100%"
></iframe>

Compare this to the equivalent `def` version, to see exactly what the lambda is shorthand for.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-8-functions-06-lambda-002-5fd84996d3.html"
 width="100%"
></iframe>

Both do the same job. The `lambda` version skips the `def`, the function name, and the explicit `return`, because a lambda's single expression is always, automatically, what gets returned.

## Lambdas Can Take Several Parameters

Just like an ordinary function, a lambda can take more than one parameter, separated by commas, before the colon.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-8-functions-06-lambda-003-f4c5ba70ea.html"
 width="100%"
></iframe>

There is still only ever one expression after the colon; a lambda cannot hold several lines, a loop, or an `if` statement the way a full `def` function can. That restriction is intentional: a lambda is meant for something this small, and anything bigger belongs in a proper `def` function instead.

## Where Lambdas Actually Shine: As an Argument

Writing `square = lambda x: x * x` and then calling `square(5)` later is legal, but it throws away the lambda's real advantage. A lambda's natural home is being passed directly into another function, on the spot, with no name of its own at all. The clearest example is `sorted()`'s `key` argument, which expects a function that says "what should I compare each item by?"

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-8-functions-06-lambda-004-c9a498b139.html"
 width="100%"
></iframe>

Here the lambda takes one tuple, `person`, and returns its second item, the amount, telling `sorted()` exactly what to compare. Writing a separate, named `def` function purely to be used once, right here, would be more ceremony than the job deserves.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/06_lambda_sort_key.png)


## A Lambda Is Still Just a Value

Because a lambda is an expression, it can be stored in a variable, put inside a list, or passed around exactly like any other value, including a number or a string.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-8-functions-06-lambda-005-5ee4ed4637.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-8-functions-06-lambda-006-529f1d2f3f.html"
 width="100%"
></iframe>

Notice the very same small lambda idea, "compare by the score," answers two different questions here: the full sorted order, and the single best entry.

## Conclusion

A lambda is a small, anonymous, single-expression function, written as `lambda parameters: expression`, whose result is returned automatically with no explicit `return` needed. Lambdas are at their best when passed directly into another function, such as the `key` argument of `sorted()` or `max()`, for a quick comparison that does not deserve a full named definition. Reach for a regular `def` function the moment the logic needs more than one expression. The next lesson puts lambdas to work alongside three classic tools built specifically to take a function as an argument: `map`, `filter`, and `reduce`.
