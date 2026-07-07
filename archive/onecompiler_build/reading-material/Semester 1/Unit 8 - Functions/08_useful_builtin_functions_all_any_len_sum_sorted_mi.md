## Introduction

Naveen keeps reinventing small pieces of logic that Python actually already hands him for free. He once wrote a loop just to check whether every single member had paid their dues. He wrote another loop just to find the single largest pending due. He has used `len()` and `sum()` for units now without ever stopping to notice how often they show up. A handful of built-in functions cover almost every one of these everyday questions, and knowing them by name saves you from writing a loop for a job Python has already solved.

This lesson is a tour of the built-ins worth knowing cold: `all`, `any`, `len`, `sum`, `sorted`, `min`, and `max`.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/08_builtin_functions_toolbox.png)

## all(): Is Everything True?

`all` takes a sequence and returns `True` only if every single item in it is truthy.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X3VzZWZ1bF9idWlsdGluX2Z1bmN0aW9uc19hbGxfYW55X2xlbl9zdW1fc29ydGVkX21pIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJwYWlkID0gW1RydWUsIFRydWUsIFRydWUsIEZhbHNlXVxucHJpbnQoYWxsKHBhaWQpKSAgICAjIEZhbHNlLCBiZWNhdXNlIG9uZSBtZW1iZXIgaGFzIG5vdCBwYWlkIn0"
 width="100%"
></iframe>

This replaces the exact loop Naveen used to write by hand: set a flag to `True`, loop through everyone, and flip the flag to `False` the moment one person has not paid. `all()` does that in a single call.

## any(): Is At Least One True?

`any` takes a sequence and returns `True` if at least one item in it is truthy.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X3VzZWZ1bF9idWlsdGluX2Z1bmN0aW9uc19hbGxfYW55X2xlbl9zdW1fc29ydGVkX21pIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJvdmVyZHVlID0gW0ZhbHNlLCBGYWxzZSwgVHJ1ZSwgRmFsc2VdXG5wcmludChhbnkob3ZlcmR1ZSkpICAgICMgVHJ1ZSwgYXQgbGVhc3Qgb25lIG1lbWJlciBpcyBvdmVyZHVlIn0"
 width="100%"
></iframe>

`all` asks "does everyone qualify?" while `any` asks "does anyone qualify at all?" Keeping the two straight is mostly about remembering which word matches which question in plain English: "all of them" versus "any of them."

## len(): How Many Items?

You have used `len()` since the strings unit, and it works identically on lists, tuples, sets, and dictionaries, always counting how many items the collection holds.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X3VzZWZ1bF9idWlsdGluX2Z1bmN0aW9uc19hbGxfYW55X2xlbl9zdW1fc29ydGVkX21pIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJtZW1iZXJzID0gW1wiQXNoYVwiLCBcIlJhdmlcIiwgXCJNZWVyYVwiLCBcIk5hdmVlblwiXVxucHJpbnQobGVuKG1lbWJlcnMpKSAgICAjIDQifQ"
 width="100%"
></iframe>

## sum(): Add Everything Up

`sum()` adds every number in a sequence together, and it accepts an optional second argument as a starting value, useful when you want to begin counting from something other than zero.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X3VzZWZ1bF9idWlsdGluX2Z1bmN0aW9uc19hbGxfYW55X2xlbl9zdW1fc29ydGVkX21pIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJkdWVzID0gWzMwMCwgMTUwLCA0NTAsIDIwMF1cbnByaW50KHN1bShkdWVzKSkgICAgICAgICAgICMgMTEwMFxucHJpbnQoc3VtKGR1ZXMsIDUwMCkpICAgICAgIyAxNjAwLCBzdGFydGluZyBmcm9tIGEgNTAwIGNhcnJ5LW92ZXIgYmFsYW5jZSJ9"
 width="100%"
></iframe>

## sorted(): A New, Ordered List

`sorted()` returns a brand new sorted list from any sequence, leaving the original untouched, exactly as you met it in the lists and tuples unit. It accepts `reverse=True` and a `key` function, which you have already seen paired with a lambda.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X3VzZWZ1bF9idWlsdGluX2Z1bmN0aW9uc19hbGxfYW55X2xlbl9zdW1fc29ydGVkX21pIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJwcmludChzb3J0ZWQoZHVlcykpICAgICAgICAgICAgICAgICAgICAgICAjIFsxNTAsIDIwMCwgMzAwLCA0NTBdXG5wcmludChzb3J0ZWQoZHVlcywgcmV2ZXJzZT1UcnVlKSkgICAgICAgICAjIFs0NTAsIDMwMCwgMjAwLCAxNTBdIn0"
 width="100%"
></iframe>

## min() and max(): The Smallest and Largest

`min()` and `max()` find the smallest and largest values in a sequence directly, no loop and no "best so far" variable required.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X3VzZWZ1bF9idWlsdGluX2Z1bmN0aW9uc19hbGxfYW55X2xlbl9zdW1fc29ydGVkX21pIGNvZGUgNiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNi5weSIsImNvZGUiOiJwcmludChtaW4oZHVlcykpICAgICMgMTUwXG5wcmludChtYXgoZHVlcykpICAgICMgNDUwIn0"
 width="100%"
></iframe>

Both also accept a `key` argument, exactly like `sorted()`, letting you find the minimum or maximum by some derived value rather than the raw value itself.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/08_builtin_function_selector.png)


<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X3VzZWZ1bF9idWlsdGluX2Z1bmN0aW9uc19hbGxfYW55X2xlbl9zdW1fc29ydGVkX21pIGNvZGUgNyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNy5weSIsImNvZGUiOiJtZW1iZXJzX3dpdGhfZHVlcyA9IFsoXCJBc2hhXCIsIDMwMCksIChcIlJhdmlcIiwgMTUwKSwgKFwiTWVlcmFcIiwgNDUwKV1cbnByaW50KG1heChtZW1iZXJzX3dpdGhfZHVlcywga2V5PWxhbWJkYSBtOiBtWzFdKSkgICAgIyAoJ01lZXJhJywgNDUwKSJ9"
 width="100%"
></iframe>

## Built-ins at a Glance

| Function | Answers | Example |
|---|---|---|
| `all(seq)` | Is every item truthy? | `all(paid)` |
| `any(seq)` | Is at least one item truthy? | `any(overdue)` |
| `len(seq)` | How many items? | `len(members)` |
| `sum(seq)` | What is the total? | `sum(dues)` |
| `sorted(seq)` | What is the ordered version? | `sorted(dues, reverse=True)` |
| `min(seq)` | What is the smallest? | `min(dues)` |
| `max(seq)` | What is the largest? | `max(dues)` |

## Your Turn: A One-Glance Dues Report

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X3VzZWZ1bF9idWlsdGluX2Z1bmN0aW9uc19hbGxfYW55X2xlbl9zdW1fc29ydGVkX21pIGNvZGUgOCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwOC5weSIsImNvZGUiOiJkdWVzID0gWzMwMCwgMTUwLCA0NTAsIDIwMCwgMF1cblxucHJpbnQoXCJUb3RhbCBjb2xsZWN0ZWQgc28gZmFyOlwiLCBzdW0oZHVlcykpXG5wcmludChcIkxhcmdlc3QgcGVuZGluZyBkdWU6XCIsIG1heChkdWVzKSlcbnByaW50KFwiU21hbGxlc3QgcGVuZGluZyBkdWU6XCIsIG1pbihkdWVzKSlcbnByaW50KFwiSGFzIGV2ZXJ5b25lIHBhaWQgc29tZXRoaW5nP1wiLCBhbGwoYW1vdW50ID4gMCBmb3IgYW1vdW50IGluIGR1ZXMpKVxucHJpbnQoXCJJcyBhbnlvbmUgZnVsbHkgY2xlYXJlZCBhdCB6ZXJvP1wiLCBhbnkoYW1vdW50ID09IDAgZm9yIGFtb3VudCBpbiBkdWVzKSlcbnByaW50KFwiU29ydGVkLCBoaWdoZXN0IGZpcnN0OlwiLCBzb3J0ZWQoZHVlcywgcmV2ZXJzZT1UcnVlKSkifQ"
 width="100%"
></iframe>

Notice `all` and `any` here are fed a generator expression, written just like a list comprehension but without the square brackets, which is a common, efficient way to feed a quick condition straight into these two functions.

## Conclusion

`all` and `any` answer "does everyone" and "does anyone" without a hand-written loop, `len` and `sum` count and total a sequence, and `sorted`, `min`, and `max` order and extract extremes, all accepting an optional `key` for custom comparisons. Recognising and reaching for these built-ins, rather than rebuilding their logic from scratch with a loop, is one of the fastest ways to write shorter, more reliable code. The next lesson turns from these ready-made tools to a technique for organising your own functions: defining one function inside another.
