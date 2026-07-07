## Introduction

Naveen's `greet_member` function from the last lesson always says exactly the same thing, to no one in particular, and his bill-splitting calculation still has no function home at all, because every function he has written so far refuses to take any information in. He wants to write `split_cost` once and feed it a different total and a different headcount every time he calls it, and he wants the function to hand back the actual number so he can use it, not just print it and move on.

Two ideas unlock this: **parameters**, the named placeholders a function declares it needs, and **return values**, the result a function hands back to whoever called it.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/03_parameters_in_value_out.png)

## Parameters: Placeholders in the Definition

A parameter is a name listed inside a function's parentheses, a placeholder for a value that will be supplied later.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3BhcmFtZXRlcnNfYXJndW1lbnRzX2FuZF9yZXR1cm5fdmFsdWVzIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJkZWYgZ3JlZXQobmFtZSk6XG4gICAgcHJpbnQoZlwiV2VsY29tZSwge25hbWV9IVwiKVxuXG5ncmVldChcIkFzaGFcIilcbmdyZWV0KFwiUmF2aVwiKSJ9"
 width="100%"
></iframe>

Output:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3BhcmFtZXRlcnNfYXJndW1lbnRzX2FuZF9yZXR1cm5fdmFsdWVzIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJXZWxjb21lLCBBc2hhIVxuV2VsY29tZSwgUmF2aSEifQ"
 width="100%"
></iframe>

Here `name` is the parameter, the placeholder declared in the definition. "Asha" and "Ravi" are the **arguments**, the actual values supplied at each call. The distinction matters: a parameter is part of the recipe, written once; an argument is the specific ingredient handed over on a particular call.

## Several Parameters at Once

A function can declare as many parameters as it needs, separated by commas, and you supply a matching argument for each, in the same order.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3BhcmFtZXRlcnNfYXJndW1lbnRzX2FuZF9yZXR1cm5fdmFsdWVzIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJkZWYgc3BsaXRfY29zdCh0b3RhbCwgcGVvcGxlKTpcbiAgICBwcmludCh0b3RhbCAvIHBlb3BsZSlcblxuc3BsaXRfY29zdCgxMjAwLCA0KSAgICAjIDMwMC4wXG5zcGxpdF9jb3N0KDYwMCwgMykgICAgICMgMjAwLjAifQ"
 width="100%"
></iframe>

This is finally Naveen's real `split_cost` function: one definition, two parameters, called with whatever numbers actually apply each time.

## Returning a Value: Handing the Result Back

Notice that `split_cost` above only prints its answer; it cannot be used for anything further. A function that uses `return` instead hands its result back to the caller, who can then store it, print it, or use it in another calculation.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3BhcmFtZXRlcnNfYXJndW1lbnRzX2FuZF9yZXR1cm5fdmFsdWVzIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJkZWYgc3BsaXRfY29zdCh0b3RhbCwgcGVvcGxlKTpcbiAgICByZXR1cm4gdG90YWwgLyBwZW9wbGVcblxubWVzc19zaGFyZSA9IHNwbGl0X2Nvc3QoMTIwMCwgNClcbnByaW50KFwiRWFjaCBwZXJzb24gb3dlczpcIiwgbWVzc19zaGFyZSlcbnByaW50KFwiV2l0aCByb3VuZGluZzpcIiwgcm91bmQobWVzc19zaGFyZSwgMikpIn0"
 width="100%"
></iframe>

Because `split_cost` now returns a value, Naveen can capture it in `mess_share` and reuse that number however he likes, exactly the way `len()` or `int()` have always handed a usable result back to you.

## print() Shows a Value; return Hands It Back

This is the single most important distinction in this lesson, and it trips up nearly every beginner once. `print()` only displays something on screen; it does not give the rest of the program anything to work with.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3BhcmFtZXRlcnNfYXJndW1lbnRzX2FuZF9yZXR1cm5fdmFsdWVzIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJkZWYgYWRkX25vX3JldHVybihhLCBiKTpcbiAgICBwcmludChhICsgYilcblxuZGVmIGFkZF93aXRoX3JldHVybihhLCBiKTpcbiAgICByZXR1cm4gYSArIGJcblxucmVzdWx0ID0gYWRkX25vX3JldHVybigzLCA0KSAgICAjIHByaW50cyA3XG5wcmludChyZXN1bHQpICAgICAgICAgICAgICAgICAgICAjIE5vbmUgLSBub3RoaW5nIHdhcyByZXR1cm5lZCFcblxucmVzdWx0ID0gYWRkX3dpdGhfcmV0dXJuKDMsIDQpICAjIHByaW50cyBub3RoaW5nIG9uIGl0cyBvd25cbnByaW50KHJlc3VsdCkgICAgICAgICAgICAgICAgICAgICMgNyJ9"
 width="100%"
></iframe>

`add_no_return` displayed 7 on screen, but handed nothing back, so `result` ends up holding `None`. `add_with_return` displayed nothing by itself, but handed 7 back, ready for `result` to actually use. If you ever see a mysterious `None` where you expected a number, missing a `return` is almost always the reason.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/03_print_vs_return.png)


## A Function Without return Still Returns None

Every Python function returns something, even if you never write the word `return`. With no explicit `return`, a function quietly hands back `None` when it finishes.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3BhcmFtZXRlcnNfYXJndW1lbnRzX2FuZF9yZXR1cm5fdmFsdWVzIGNvZGUgNiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNi5weSIsImNvZGUiOiJkZWYgbG9nX21lc3NhZ2UodGV4dCk6XG4gICAgcHJpbnQoXCJMT0c6XCIsIHRleHQpXG5cbm91dGNvbWUgPSBsb2dfbWVzc2FnZShcIkJpbGwgY2FsY3VsYXRlZFwiKVxucHJpbnQob3V0Y29tZSkgICAgIyBOb25lIn0"
 width="100%"
></iframe>

This is fine when you only ever wanted the side effect, the printed log line, and never planned to use a result. It becomes a bug only when you forget that a function without `return` cannot hand anything useful back.

## Parameters, Arguments, and Return at a Glance

| Term | What It Is | Example |
|---|---|---|
| Parameter | A named placeholder in the definition | `def split_cost(total, people):` |
| Argument | The actual value supplied at a call | `split_cost(1200, 4)` |
| `return value` | Hands a result back to the caller | `return total / people` |
| No `return` | Function still returns `None` | A print-only function |

## Your Turn: A Function That Gives Something Back

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3BhcmFtZXRlcnNfYXJndW1lbnRzX2FuZF9yZXR1cm5fdmFsdWVzIGNvZGUgNyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNy5weSIsImNvZGUiOiJkZWYgY2FsY3VsYXRlX3RvdGFsKHByaWNlLCBxdWFudGl0eSk6XG4gICAgcmV0dXJuIHByaWNlICogcXVhbnRpdHlcblxuc2hpcnRfdG90YWwgPSBjYWxjdWxhdGVfdG90YWwoMzUwLCAyKVxubXVnX3RvdGFsID0gY2FsY3VsYXRlX3RvdGFsKDE1MCwgMylcbmdyYW5kX3RvdGFsID0gc2hpcnRfdG90YWwgKyBtdWdfdG90YWxcblxucHJpbnQoXCJTaGlydCB0b3RhbDpcIiwgc2hpcnRfdG90YWwpXG5wcmludChcIk11ZyB0b3RhbDpcIiwgbXVnX3RvdGFsKVxucHJpbnQoXCJHcmFuZCB0b3RhbDpcIiwgZ3JhbmRfdG90YWwpIn0"
 width="100%"
></iframe>

Notice the last line could only work because `calculate_total` actually returned its result; a print-only version would have left `grand_total` with nothing real to add together.

## Conclusion

Parameters are the named placeholders a function declares in its definition, and arguments are the actual values you supply at each call. A function hands a usable result back to its caller with `return`, while `print()` only displays something and gives nothing back; without an explicit `return`, a function quietly returns `None`. With values flowing both in and out, the next lesson looks at making some of those parameters optional, and giving you more flexible ways to supply arguments.
