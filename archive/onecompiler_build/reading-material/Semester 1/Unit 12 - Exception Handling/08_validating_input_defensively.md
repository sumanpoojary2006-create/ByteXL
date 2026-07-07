## Introduction

Asha's signup form, all the way back in the control flow unit, could check input with conditions, but it could not re-ask after a bad entry; that lesson explicitly said loops would be needed to complete the picture. The looping unit then gave her exactly that, a way to keep asking until an entry passed. What was still missing was a clean way to handle the kind of failure conditions alone could never anticipate, like text where a number was expected, which is exactly what this entire unit has now supplied.

This lesson combines all three: a loop to keep asking, conditions to check the rules that matter, and `try`/`except` to survive the conversions that conditions alone cannot protect against. Together, they form **defensive input validation**, the complete pattern real, user-facing programs depend on.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-12-exception-handling/08_defensive_validation_loop.png)

## The Gap Conditions Alone Could Not Close

Recall the limitation from the control flow unit directly.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X3ZhbGlkYXRpbmdfaW5wdXRfZGVmZW5zaXZlbHkgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6ImFnZSA9IGlucHV0KFwiRW50ZXIgeW91ciBhZ2U6IFwiKVxuaWYgbm90IGFnZS5pc2RpZ2l0KCk6XG4gICAgcHJpbnQoXCJQbGVhc2UgZW50ZXIgZGlnaXRzIG9ubHkuXCIpXG5lbHNlOlxuICAgIGFnZSA9IGludChhZ2UpXG4gICAgaWYgYWdlIDwgMSBvciBhZ2UgPiAxMjA6XG4gICAgICAgIHByaW50KFwiVGhhdCBhZ2UgaXMgb3V0IG9mIHJhbmdlLlwiKVxuICAgIGVsc2U6XG4gICAgICAgIHByaW50KGZcIlRoYW5rIHlvdS4gWW91ciBhZ2UgaXMge2FnZX0uXCIpIn0"
 width="100%"
></iframe>

This rejects bad input with a clear message, but it never asks again. A user who mistypes once is simply done, forced to rerun the entire script from the top. The loop is the piece that was always missing.

## Adding the Loop: Keep Asking Until Valid

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X3ZhbGlkYXRpbmdfaW5wdXRfZGVmZW5zaXZlbHkgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6IndoaWxlIFRydWU6XG4gICAgYWdlX3RleHQgPSBpbnB1dChcIkVudGVyIHlvdXIgYWdlOiBcIilcbiAgICBpZiBub3QgYWdlX3RleHQuaXNkaWdpdCgpOlxuICAgICAgICBwcmludChcIlBsZWFzZSBlbnRlciBkaWdpdHMgb25seS5cIilcbiAgICAgICAgY29udGludWVcbiAgICBhZ2UgPSBpbnQoYWdlX3RleHQpXG4gICAgaWYgYWdlIDwgMSBvciBhZ2UgPiAxMjA6XG4gICAgICAgIHByaW50KFwiVGhhdCBhZ2UgaXMgb3V0IG9mIHJhbmdlLlwiKVxuICAgICAgICBjb250aW51ZVxuICAgIGJyZWFrXG5cbnByaW50KGZcIlRoYW5rIHlvdS4gWW91ciBhZ2UgaXMge2FnZX0uXCIpIn0"
 width="100%"
></iframe>

Now a bad entry simply loops back and asks again, exactly the `while True` with `continue` and `break` pattern from the looping unit, finally closing the gap that lesson left open.

## Adding try/except: Defending Against What Conditions Cannot Predict

The `.isdigit()` check above quietly assumes a very specific kind of bad input, text instead of digits. It does not protect against every possible failure a more complex conversion might hit, and in genuinely complex validation, a `try`/`except` around the risky conversion itself is often more general and more robust than chaining condition after condition trying to anticipate every bad shape in advance.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X3ZhbGlkYXRpbmdfaW5wdXRfZGVmZW5zaXZlbHkgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6IndoaWxlIFRydWU6XG4gICAgYWdlX3RleHQgPSBpbnB1dChcIkVudGVyIHlvdXIgYWdlOiBcIilcbiAgICB0cnk6XG4gICAgICAgIGFnZSA9IGludChhZ2VfdGV4dClcbiAgICBleGNlcHQgVmFsdWVFcnJvcjpcbiAgICAgICAgcHJpbnQoXCJQbGVhc2UgZW50ZXIgYSB2YWxpZCB3aG9sZSBudW1iZXIuXCIpXG4gICAgICAgIGNvbnRpbnVlXG5cbiAgICBpZiBhZ2UgPCAxIG9yIGFnZSA-IDEyMDpcbiAgICAgICAgcHJpbnQoXCJUaGF0IGFnZSBpcyBvdXQgb2YgcmFuZ2UuXCIpXG4gICAgICAgIGNvbnRpbnVlXG5cbiAgICBicmVha1xuXG5wcmludChmXCJUaGFuayB5b3UuIFlvdXIgYWdlIGlzIHthZ2V9LlwiKSJ9"
 width="100%"
></iframe>

Notice the division of labour here, the heart of defensive validation: `try`/`except` guards the conversion itself, the operation that can fail in ways hard to fully predict with conditions, while a plain `if` still checks the business rule, the range 1 to 120, which is not really about failure at all, just a rule about what counts as a sensible age.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-12-exception-handling/08_validation_loop_until_valid.png)


## A Complete, Reusable Validation Function

Wrapping this pattern in a function makes it reusable anywhere your program needs a validated number within a range.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X3ZhbGlkYXRpbmdfaW5wdXRfZGVmZW5zaXZlbHkgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6ImRlZiBhc2tfZm9yX2FnZSgpOlxuICAgIHdoaWxlIFRydWU6XG4gICAgICAgIGFnZV90ZXh0ID0gaW5wdXQoXCJFbnRlciB5b3VyIGFnZTogXCIpXG4gICAgICAgIHRyeTpcbiAgICAgICAgICAgIGFnZSA9IGludChhZ2VfdGV4dClcbiAgICAgICAgZXhjZXB0IFZhbHVlRXJyb3I6XG4gICAgICAgICAgICBwcmludChcIlBsZWFzZSBlbnRlciBhIHZhbGlkIHdob2xlIG51bWJlci5cIilcbiAgICAgICAgICAgIGNvbnRpbnVlXG4gICAgICAgIGlmIGFnZSA8IDEgb3IgYWdlID4gMTIwOlxuICAgICAgICAgICAgcHJpbnQoXCJUaGF0IGFnZSBpcyBvdXQgb2YgcmFuZ2UuXCIpXG4gICAgICAgICAgICBjb250aW51ZVxuICAgICAgICByZXR1cm4gYWdlXG5cbmFnZSA9IGFza19mb3JfYWdlKClcbnByaW50KGZcIlJlZ2lzdGVyZWQgd2l0aCBhZ2Uge2FnZX0uXCIpIn0"
 width="100%"
></iframe>

`return age` inside the loop both hands back the valid value and ends the function in one step, exactly the way `break` ended the loop in the earlier, non-function version, simply expressed through a function's own natural exit point.

## Defensive Validation at a Glance

| Layer | Tool | Catches |
|---|---|---|
| Keep asking | `while True:` with `continue` and `break` | A single rejected attempt should not end the program |
| Guard against conversion failure | `try`/`except ValueError` | Input that simply cannot become the type you need |
| Enforce a business rule | A plain `if`, after the conversion succeeds | A value that converted fine but is still not acceptable |

## Your Turn: Validate a Ticket Quantity

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X3ZhbGlkYXRpbmdfaW5wdXRfZGVmZW5zaXZlbHkgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6ImRlZiBhc2tfZm9yX3F1YW50aXR5KCk6XG4gICAgd2hpbGUgVHJ1ZTpcbiAgICAgICAgdGV4dCA9IGlucHV0KFwiSG93IG1hbnkgdGlja2V0cz8gXCIpXG4gICAgICAgIHRyeTpcbiAgICAgICAgICAgIHF1YW50aXR5ID0gaW50KHRleHQpXG4gICAgICAgIGV4Y2VwdCBWYWx1ZUVycm9yOlxuICAgICAgICAgICAgcHJpbnQoXCJQbGVhc2UgZW50ZXIgYSB3aG9sZSBudW1iZXIuXCIpXG4gICAgICAgICAgICBjb250aW51ZVxuICAgICAgICBpZiBxdWFudGl0eSA8PSAwOlxuICAgICAgICAgICAgcHJpbnQoXCJRdWFudGl0eSBtdXN0IGJlIGF0IGxlYXN0IDEuXCIpXG4gICAgICAgICAgICBjb250aW51ZVxuICAgICAgICByZXR1cm4gcXVhbnRpdHlcblxucXVhbnRpdHkgPSBhc2tfZm9yX3F1YW50aXR5KClcbnByaW50KGZcIkJvb2tpbmcge3F1YW50aXR5fSB0aWNrZXQocykuXCIpIn0"
 width="100%"
></iframe>

Try entering "abc", then "0", then "3", and confirm only the third attempt is ever accepted, with the first two re-asking instead of crashing or silently continuing.

## Conclusion

Defensive input validation combines a loop to keep asking after a rejected attempt, `try`/`except` to survive conversions that cannot be fully anticipated with conditions alone, and plain `if` checks to enforce the business rules that matter once a value has successfully converted. This is the complete picture the control flow unit promised was coming, finally assembled from loops and exception handling together. The final lesson of this unit steps back from any one pattern to ask the broader question: what does it actually mean to design a program that treats errors as a normal, expected part of its design, rather than a failure to be merely survived?
