## Introduction

In the last few lessons you met numbers, strings, and booleans. Real programs constantly move between them. A user types their age, which arrives as text, but you want to do arithmetic with it. A price is a number, but you want to print it inside a sentence. Each type is excellent at its own job and stubborn about doing anyone else's, so the moment two different types need to work together, something has to bend. Turning a value from one type into another is called **type conversion**, or casting, and it is one of the most practical skills in this unit, precisely because keyboards, files, and the internet hand you almost everything as plain text, even when the text is clearly a number to your eyes.

There is also a built in tool, `type()`, that tells you exactly what type a value is, which is invaluable when something behaves unexpectedly.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t82xext/04_input_trap_text_not_number.png)


## Every Type Has a Name, and type() Reveals It

When you are unsure what you are holding, ask Python directly.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3R5cGVfY29udmVyc2lvbl9hbmRfY2FzdGluZyBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoicHJpbnQodHlwZSg0MikpICAgICAgICAjIDxjbGFzcyAnaW50Jz5cbnByaW50KHR5cGUoMy4xNCkpICAgICAgIyA8Y2xhc3MgJ2Zsb2F0Jz5cbnByaW50KHR5cGUoXCJoZWxsb1wiKSkgICAjIDxjbGFzcyAnc3RyJz5cbnByaW50KHR5cGUoVHJ1ZSkpICAgICAgIyA8Y2xhc3MgJ2Jvb2wnPiJ9"
 width="100%"
></iframe>

Each value reports its type. This simple check will rescue you many times when a program misbehaves, because the cause is very often a value that is a different type than you assumed.

## The input() Trap

Here is the single most common surprise for beginners. The `input()` function always returns a string, even when the user types digits. So what do you think this program does?

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3R5cGVfY29udmVyc2lvbl9hbmRfY2FzdGluZyBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoiYWdlID0gaW5wdXQoXCJZb3VyIGFnZTogXCIpXG5wcmludChhZ2UgKyAxKSJ9"
 width="100%"
></iframe>

If you typed 20, you might expect 21. Instead Python stops with an error, because it refuses to add the number 1 to the text "20". The value looks like a number to your eyes, but to Python it is text, no different from the word "hello" as far as the type system is concerned. This is exactly why so many first programs crash on what looks like a perfectly reasonable line of code, and it is almost always the very first error a beginner meets when they start reading user input. Now you know the reason, and more importantly, you know it is not a flaw in your logic. It is a missing conversion.

## Converting Between Types

The cure is to convert the text into the type you actually need, using the matching function: `int()`, `float()`, `str()`, or `bool()`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3R5cGVfY29udmVyc2lvbl9hbmRfY2FzdGluZyBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoiYWdlID0gaW50KGlucHV0KFwiWW91ciBhZ2U6IFwiKSkgICAjIHRleHQgYmVjb21lcyBhIHdob2xlIG51bWJlclxucHJpbnQoYWdlICsgMSkgICAgICAgICAgICAgICAgICAgIyBub3cgdGhpcyB3b3JrcyJ9"
 width="100%"
></iframe>

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t82xext/04_int_conversion_fixes_it.png)


You can convert in the other direction too. To drop a number into a sentence, turn it into a string, or let `print` do it for you with commas.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3R5cGVfY29udmVyc2lvbl9hbmRfY2FzdGluZyBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoicHJpY2UgPSAyNTBcbm1lc3NhZ2UgPSBcIlRoZSBwcmljZSBpcyBcIiArIHN0cihwcmljZSlcbnByaW50KG1lc3NhZ2UpIn0"
 width="100%"
></iframe>

One detail to remember: converting a float to an int does not round, it simply cuts off the decimal part, so `int(7.9)` becomes 7, not 8.

## Conversion Functions at a Glance

| Function | Converts To | Example | Watch Out For |
|---|---|---|---|
| `int()` | Whole number | `int("20")` becomes `20` | Drops any decimal part, does not round |
| `float()` | Decimal number | `float("3.5")` becomes `3.5` | |
| `str()` | Text | `str(250)` becomes `"250"` | Needed before joining a number with `+` |
| `bool()` | True/False | `bool(0)` becomes `False` | Most non-zero, non-empty values become `True` |

## When Conversion Fails

Conversion only works when the value genuinely fits the target type. Asking Python to read "hello" as a number is impossible, and it will say so:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3R5cGVfY29udmVyc2lvbl9hbmRfY2FzdGluZyBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoiaW50KFwiaGVsbG9cIikgICAjIGVycm9yOiBpbnZhbGlkIGxpdGVyYWwgZm9yIGludCgpIn0"
 width="100%"
></iframe>

That is reasonable behaviour, not a flaw. Python would rather stop loudly and immediately than guess at a number that was never really there, and a silent wrong guess would be far more dangerous than an honest error message. Later, in the exception-handling unit, you will learn to catch these situations gracefully so a single bad entry does not crash your whole program.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t82xext/04_conversion_failure_warning.png)


## Your Turn: With and Without Conversion

Run this and watch the difference one function makes.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3R5cGVfY29udmVyc2lvbl9hbmRfY2FzdGluZyBjb2RlIDYiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDYucHkiLCJjb2RlIjoiYSA9IGlucHV0KFwiRmlyc3QgbnVtYmVyOiBcIilcbmIgPSBpbnB1dChcIlNlY29uZCBudW1iZXI6IFwiKVxucHJpbnQoXCJKb2luZWQgYXMgdGV4dDpcIiwgYSArIGIpXG5wcmludChcIkFkZGVkIGFzIG51bWJlcnM6XCIsIGludChhKSArIGludChiKSkifQ"
 width="100%"
></iframe>

Type 7 and 10. The first line prints `710`, because joining two strings places them side by side. The second prints `17`, because converting them to integers lets Python actually add. Same input, two completely different results, decided entirely by type.

## Conclusion

Type conversion turns a value from one type into another with `int()`, `float()`, `str()`, and `bool()`, and `type()` tells you what you are holding. Remember above all that `input()` hands you a string, so numbers from the keyboard must be converted before you do maths with them. Master this one habit and you will avoid the most common crash a beginner ever meets.
