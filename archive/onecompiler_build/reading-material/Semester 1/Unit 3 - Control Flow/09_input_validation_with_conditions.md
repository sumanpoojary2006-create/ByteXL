## Introduction

Asha is filling a college event signup form on her phone, and it keeps stopping her. She types "abc" in the age field and it flashes red. She tries "200" and it refuses again. She leaves a field blank and it will not submit. The form simply will not trust whatever she types until it makes sense. People leave fields blank, type letters where numbers belong, enter an age of 200, or paste in extra spaces, and a program that blindly trusts whatever it is given will sooner or later crash or, worse, produce a confidently wrong result.

The form on Asha's screen was not being difficult for its own sake; it was refusing to move forward with data it could not trust, exactly the discipline a well-written program needs. Input validation is the habit of checking input before you rely on it, and it brings together every idea in this unit: conditions, comparisons, truthiness, and clear branching.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t8hpwft/09_input_validation_gatekeeper.png)

## Never Trust Raw Input

Recall a trap from an earlier unit. The `input` function always returns text, so converting it to a number with `int` only works if the text actually looks like a number.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X2lucHV0X3ZhbGlkYXRpb25fd2l0aF9jb25kaXRpb25zIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJhZ2UgPSBpbnQoaW5wdXQoXCJZb3VyIGFnZTogXCIpKSAgICAjIGNyYXNoZXMgaWYgdGhlIHVzZXIgdHlwZXMgXCJhYmNcIiJ9"
 width="100%"
></iframe>

If someone types "abc", this line stops the whole program with an error. The fix is not to hope users behave, but to check first and respond gracefully.

## Check Before You Use

A useful tool here is the string method `.isdigit()`, which returns `True` only when the text is made entirely of digits. You can test the input before trusting it, then apply range checks once you know it is a number.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X2lucHV0X3ZhbGlkYXRpb25fd2l0aF9jb25kaXRpb25zIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJlbnRyeSA9IGlucHV0KFwiWW91ciBhZ2U6IFwiKVxuXG5pZiBub3QgZW50cnkuaXNkaWdpdCgpOlxuICAgIHByaW50KFwiUGxlYXNlIGVudGVyIGRpZ2l0cyBvbmx5LlwiKVxuZWxzZTpcbiAgICBhZ2UgPSBpbnQoZW50cnkpXG4gICAgaWYgYWdlIDwgMSBvciBhZ2UgPiAxMjA6XG4gICAgICAgIHByaW50KFwiVGhhdCBhZ2UgaXMgb3V0IG9mIHJhbmdlLlwiKVxuICAgIGVsc2U6XG4gICAgICAgIHByaW50KGZcIlRoYW5rIHlvdS4gWW91ciBhZ2UgaXMge2FnZX0uXCIpIn0"
 width="100%"
></iframe>

Notice the layering. The first check guards against non-numbers, and only inside the safe branch do we convert and then check the range. This is the guard-clause idea from earlier in the unit, applied to keep bad data out. Each rejected entry on Asha's form, the letters, the impossible age, was really just one of these guard checks firing and stopping the next, riskier step from ever running.

## What This Cannot Do Yet

There is an honest limit to validation with conditions alone.

| Limitation | Solved By | Coming Up |
|---|---|---|
| Cannot politely ask again after a bad entry | Loops | The very next unit |
| Cannot catch every possible error cleanly | Exception handling | A later unit |

For now, checking with conditions and giving a clear message is a solid, real step toward robust programs.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t8hpwft/09_validate_before_using_input.png)


## Your Turn: A Validated Entry

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X2lucHV0X3ZhbGlkYXRpb25fd2l0aF9jb25kaXRpb25zIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJtYXJrcyA9IGlucHV0KFwiRW50ZXIgbWFya3MgKDAgdG8gMTAwKTogXCIpXG5cbmlmIG5vdCBtYXJrcy5pc2RpZ2l0KCk6XG4gICAgcHJpbnQoXCJJbnZhbGlkOiBtYXJrcyBtdXN0IGJlIGEgd2hvbGUgbnVtYmVyLlwiKVxuZWxpZiBpbnQobWFya3MpID4gMTAwOlxuICAgIHByaW50KFwiSW52YWxpZDogbWFya3MgY2Fubm90IGV4Y2VlZCAxMDAuXCIpXG5lbHNlOlxuICAgIHByaW50KGZcIk1hcmtzIGFjY2VwdGVkOiB7bWFya3N9XCIpIn0"
 width="100%"
></iframe>

Test it with "abc", then "150", then "85". Each bad case is caught with its own clear message, and only sensible input is accepted. You have just made a program that defends itself.

## Conclusion

Input validation means checking data before you use it, because users will inevitably enter the unexpected. Combine the tools of this unit: test the shape of the input (for example with `.isdigit()`), apply range checks, and branch clearly to reject bad values with helpful messages. Conditions alone cannot re-ask or catch every error yet, and loops and exception handling will complete the picture in later units. But the mindset starts now: never trust raw input, always check it first. Branching has taught your programs to choose; the next unit teaches them to repeat, which is exactly what Asha's form still cannot do on its own when it needs to ask again after a bad entry.
