## Introduction

Asha's bill-splitting protection from the last lesson already caught two different problems, bad text and a zero headcount, with two separate, specifically named `except` blocks, each giving a tailored, helpful message. That was not an accident or extra effort; it was the deliberate, correct way to handle several distinct kinds of failure, and this lesson makes the reasoning behind it explicit.

Different operations fail in different, specifically named ways, and catching each kind separately lets your program respond to each one with exactly the right message, rather than one generic, less helpful catch-all.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-12-exception-handling/04_multiple_specific_exceptions.png)

## Naming Each Exception Type Separately

You already saw this shape in the last lesson's example; here it is again, examined closely.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2hhbmRsaW5nX211bHRpcGxlX2FuZF9zcGVjaWZpY19leGNlcHRpb25zIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJ0cnk6XG4gICAgdG90YWwgPSBpbnQoaW5wdXQoXCJUb3RhbCBiaWxsOiBcIikpXG4gICAgcGVvcGxlID0gaW50KGlucHV0KFwiTnVtYmVyIG9mIHBlb3BsZTogXCIpKVxuICAgIHByaW50KFwiRWFjaCBwYXlzOlwiLCB0b3RhbCAvIHBlb3BsZSlcbmV4Y2VwdCBWYWx1ZUVycm9yOlxuICAgIHByaW50KFwiUGxlYXNlIGVudGVyIHdob2xlIG51bWJlcnMgb25seS5cIilcbmV4Y2VwdCBaZXJvRGl2aXNpb25FcnJvcjpcbiAgICBwcmludChcIk51bWJlciBvZiBwZW9wbGUgY2Fubm90IGJlIHplcm8uXCIpIn0"
 width="100%"
></iframe>

Python checks each `except` in order, top to bottom, and runs the first one whose exception type matches what actually went wrong, exactly the same top-to-bottom, first-match-wins logic from an `elif` chain. A `ValueError` from a bad `int()` conversion is caught by the first; a `ZeroDivisionError` from dividing by zero is caught by the second; neither catches the other's situation by mistake.

## Catching Several Types With One Block

When two or more exception types deserve the exact same response, group them together in one `except`, using a tuple of types.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2hhbmRsaW5nX211bHRpcGxlX2FuZF9zcGVjaWZpY19leGNlcHRpb25zIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJ0cnk6XG4gICAgdmFsdWUgPSBpbnQoaW5wdXQoXCJFbnRlciBhIG51bWJlcjogXCIpKVxuICAgIHJlc3VsdCA9IDEwMCAvIHZhbHVlXG5leGNlcHQgKFZhbHVlRXJyb3IsIFplcm9EaXZpc2lvbkVycm9yKTpcbiAgICBwcmludChcIlBsZWFzZSBlbnRlciBhIHZhbGlkLCBub24temVybyBudW1iZXIuXCIpIn0"
 width="100%"
></iframe>

Here both a bad conversion and a zero division land on the same friendly message, since neither failure deserves a meaningfully different response in this particular script.

## Getting the Error's Own Message

The keyword `as`, used inside an `except` clause, captures the actual exception object, letting you read Python's own message about what happened.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2hhbmRsaW5nX211bHRpcGxlX2FuZF9zcGVjaWZpY19leGNlcHRpb25zIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJ0cnk6XG4gICAgdmFsdWUgPSBpbnQoaW5wdXQoXCJFbnRlciBhIG51bWJlcjogXCIpKVxuZXhjZXB0IFZhbHVlRXJyb3IgYXMgZXJyb3I6XG4gICAgcHJpbnQoXCJDb252ZXJzaW9uIGZhaWxlZDpcIiwgZXJyb3IpIn0"
 width="100%"
></iframe>

Type "abc", and this prints something like `Conversion failed: invalid literal for int() with base 10: 'abc'`, Python's own precise explanation, rather than a message you wrote yourself. This is especially useful while developing and debugging, even if your final, polished message to a real user is usually friendlier and less technical.

## Order Matters: Specific Before General

Exception types in Python form a hierarchy; some are broader categories that include several more specific ones. `Exception` is broad enough to catch almost anything; `ValueError` and `ZeroDivisionError` are specific. If a broad `except` is listed before a specific one, it wins every time, and the specific one never runs at all.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2hhbmRsaW5nX211bHRpcGxlX2FuZF9zcGVjaWZpY19leGNlcHRpb25zIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJ0cnk6XG4gICAgdmFsdWUgPSBpbnQoaW5wdXQoXCJFbnRlciBhIG51bWJlcjogXCIpKVxuZXhjZXB0IEV4Y2VwdGlvbjpcbiAgICBwcmludChcIlNvbWV0aGluZyB3ZW50IHdyb25nLlwiKSAgICAgICAgIyB0aGlzIGFsd2F5cyB3aW5zXG5leGNlcHQgVmFsdWVFcnJvcjpcbiAgICBwcmludChcIlBsZWFzZSBlbnRlciBhIHZhbGlkIG51bWJlci5cIikgICMgdW5yZWFjaGFibGUhIn0"
 width="100%"
></iframe>

Always list the most specific exception types first, and any broader, catch-everything-else type last, exactly the same "most specific condition first" rule from the `elif` lesson back in the control flow unit.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-12-exception-handling/04_specific_before_general.png)


## Multiple Exceptions at a Glance

| Pattern | Syntax | Use When |
|---|---|---|
| Separate, specific handlers | `except ValueError:` then `except ZeroDivisionError:` | Each failure deserves its own distinct response |
| Grouped handler | `except (ValueError, ZeroDivisionError):` | Several failures deserve the exact same response |
| Capture the message | `except ValueError as error:` | You want Python's own explanation of what failed |
| Order | Specific types first, broad types last | A broad type listed first silently steals every match |

## Your Turn: Three Specific Failures

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X2hhbmRsaW5nX211bHRpcGxlX2FuZF9zcGVjaWZpY19leGNlcHRpb25zIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJ0cnk6XG4gICAgYSA9IGludChpbnB1dChcIkZpcnN0IG51bWJlcjogXCIpKVxuICAgIGIgPSBpbnQoaW5wdXQoXCJTZWNvbmQgbnVtYmVyOiBcIikpXG4gICAgcmVzdWx0ID0gYSAvIGJcbiAgICBwcmludChcIlJlc3VsdDpcIiwgcmVzdWx0KVxuZXhjZXB0IFZhbHVlRXJyb3IgYXMgZXJyb3I6XG4gICAgcHJpbnQoXCJJbnZhbGlkIG51bWJlcjpcIiwgZXJyb3IpXG5leGNlcHQgWmVyb0RpdmlzaW9uRXJyb3I6XG4gICAgcHJpbnQoXCJDYW5ub3QgZGl2aWRlIGJ5IHplcm8uXCIpIn0"
 width="100%"
></iframe>

Trigger each failure on a separate run: type letters for the first number, then run again and enter 0 for the second, confirming each lands on its own correctly matched message.

## Conclusion

Different operations fail with different, specifically named exception types, and listing several `except` clauses, most specific first, lets each one get its own tailored response, while a tuple of types in one `except` handles several failures identically when that is genuinely appropriate. The `as` keyword captures the actual exception object, exposing Python's own explanation of what went wrong. With several specific failures now handled cleanly, the next lesson covers two more pieces of the `try` structure: code that should run only on success, and code that should run no matter what.
