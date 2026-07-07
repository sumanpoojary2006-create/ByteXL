## Introduction

Naveen is ready to stop copy-pasting and actually write his bill-splitting logic as a proper, reusable function, the way the last lesson previewed. Before he can do that comfortably, he needs the exact rules: what keyword starts a function, what makes Python treat a block as belonging to that function, and how do you actually run it once it exists. None of this is new machinery. It is the same `def`-a-block, indent-the-body pattern you already trust from `if` statements and loops, just with a new keyword at the front.

This lesson is entirely about those rules: **defining** a function once, and **calling** it as many times as you like afterward.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/02_define_once_call_many.png)

## Defining a Function

A function definition starts with the keyword `def`, followed by a name, parentheses, and a colon, with the function's body indented underneath, exactly like an `if` block.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2RlZmluaW5nX2FuZF9jYWxsaW5nX2Z1bmN0aW9ucyBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoiZGVmIGdyZWV0X21lbWJlcigpOlxuICAgIHByaW50KFwiV2VsY29tZSB0byB0aGUgaG9zdGVsIGNvbW1pdHRlZSFcIikifQ"
 width="100%"
></iframe>

Reading this line by line: `def` announces "a function is being defined here." `greet_member` is the name Naveen chose, following the same snake_case naming rules you already know for variables. The empty parentheses mean this particular function takes no input for now. The colon and the indentation mark everything that belongs to the function, exactly as they marked everything belonging to an `if`.

## Defining Does Not Run It

Here is the detail that catches every beginner once. Running the block above prints nothing at all.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2RlZmluaW5nX2FuZF9jYWxsaW5nX2Z1bmN0aW9ucyBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoiZGVmIGdyZWV0X21lbWJlcigpOlxuICAgIHByaW50KFwiV2VsY29tZSB0byB0aGUgaG9zdGVsIGNvbW1pdHRlZSFcIilcblxucHJpbnQoXCJTY3JpcHQgZmluaXNoZWQuXCIpIn0"
 width="100%"
></iframe>

Output:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2RlZmluaW5nX2FuZF9jYWxsaW5nX2Z1bmN0aW9ucyBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoiU2NyaXB0IGZpbmlzaGVkLiJ9"
 width="100%"
></iframe>

The `print` inside `greet_member` never ran, because defining a function only teaches Python the recipe; it does not follow the recipe. A function's body only executes when the function is actually called.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/02_define_does_not_run_call_button.png)


## Calling a Function

To run a function's body, write its name followed by parentheses, exactly the way you have been calling `print()` and `len()` all course.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2RlZmluaW5nX2FuZF9jYWxsaW5nX2Z1bmN0aW9ucyBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoiZGVmIGdyZWV0X21lbWJlcigpOlxuICAgIHByaW50KFwiV2VsY29tZSB0byB0aGUgaG9zdGVsIGNvbW1pdHRlZSFcIilcblxuZ3JlZXRfbWVtYmVyKCkifQ"
 width="100%"
></iframe>

Output:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2RlZmluaW5nX2FuZF9jYWxsaW5nX2Z1bmN0aW9ucyBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoiV2VsY29tZSB0byB0aGUgaG9zdGVsIGNvbW1pdHRlZSEifQ"
 width="100%"
></iframe>

Now the body runs, because `greet_member()`, with the parentheses, is an instruction to actually execute the function, not just refer to it.

## Calling It as Many Times as You Like

The entire point of defining a function once is that you can call it from many places, as many times as you like, without retyping its body.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2RlZmluaW5nX2FuZF9jYWxsaW5nX2Z1bmN0aW9ucyBjb2RlIDYiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDYucHkiLCJjb2RlIjoiZGVmIGdyZWV0X21lbWJlcigpOlxuICAgIHByaW50KFwiV2VsY29tZSB0byB0aGUgaG9zdGVsIGNvbW1pdHRlZSFcIilcblxuZ3JlZXRfbWVtYmVyKClcbmdyZWV0X21lbWJlcigpXG5ncmVldF9tZW1iZXIoKSJ9"
 width="100%"
></iframe>

Three calls, three identical greetings, and the body itself was only ever written once. This is precisely the reuse the last lesson promised: one definition, unlimited calls.

## A Function Must Be Defined Before It Is Called

Python reads your file from top to bottom, so a function must be defined before the line that calls it, or Python will not yet know the name.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2RlZmluaW5nX2FuZF9jYWxsaW5nX2Z1bmN0aW9ucyBjb2RlIDciLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDcucHkiLCJjb2RlIjoic2F5X2hlbGxvKCkgICAgICAgICMgZXJyb3IhIHNheV9oZWxsbyBpcyBub3QgZGVmaW5lZCB5ZXRcblxuZGVmIHNheV9oZWxsbygpOlxuICAgIHByaW50KFwiSGVsbG8hXCIpIn0"
 width="100%"
></iframe>

This raises a `NameError`, complaining that `say_hello` does not exist, because Python had not reached its definition yet when it hit the call. Swapping the two blocks, definition first, then call, fixes it immediately.

## Defining vs Calling at a Glance

| Action | Syntax | What Happens |
|---|---|---|
| Define | `def name():` then an indented body | Teaches Python the recipe; nothing runs yet |
| Call | `name()` | Actually runs the body, right now |
| Call again | `name()` a second time | Runs the same body again, from the same definition |

## Your Turn: Define and Call

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2RlZmluaW5nX2FuZF9jYWxsaW5nX2Z1bmN0aW9ucyBjb2RlIDgiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDgucHkiLCJjb2RlIjoiZGVmIHByaW50X3NlcGFyYXRvcigpOlxuICAgIHByaW50KFwiLS0tLS0tLS0tLS0tLS0tLS0tLS1cIilcblxucHJpbnRfc2VwYXJhdG9yKClcbnByaW50KFwiTWVzcyBCaWxsIFJlcG9ydFwiKVxucHJpbnRfc2VwYXJhdG9yKClcbnByaW50KFwiVG90YWw6IDEyMDBcIilcbnByaW50X3NlcGFyYXRvcigpIn0"
 width="100%"
></iframe>

Run this and watch the same small function dividing up a tidy report, called three times from three different points, with its body written only once.

## Conclusion

A function is defined with `def name():` and an indented body, but that body only runs once the function is actually called by writing its name followed by parentheses: `name()`. Defining a function teaches Python the recipe; calling it follows the recipe, and you can call the same recipe as many times as you need. Every function you have called so far has taken no input and given nothing back; the next lesson opens up both directions, letting you hand information in and get a result out.
