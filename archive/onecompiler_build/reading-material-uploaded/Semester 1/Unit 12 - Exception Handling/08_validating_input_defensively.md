## Introduction

Asha's signup form, all the way back in the control flow unit, could check input with conditions, but it could not re-ask after a bad entry; that lesson explicitly said loops would be needed to complete the picture. The looping unit then gave her exactly that, a way to keep asking until an entry passed. What was still missing was a clean way to handle the kind of failure conditions alone could never anticipate, like text where a number was expected, which is exactly what this entire unit has now supplied.

This lesson combines all three: a loop to keep asking, conditions to check the rules that matter, and `try`/`except` to survive the conversions that conditions alone cannot protect against. Together, they form **defensive input validation**, the complete pattern real, user-facing programs depend on.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-12-exception-handling/08_defensive_validation_loop.png)

## The Gap Conditions Alone Could Not Close

Recall the limitation from the control flow unit directly.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-12-exception-handling-08-validating-input-defensively-001-02c5475e13.html"
 width="100%"
></iframe>

This rejects bad input with a clear message, but it never asks again. A user who mistypes once is simply done, forced to rerun the entire script from the top. The loop is the piece that was always missing.

## Adding the Loop: Keep Asking Until Valid

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-12-exception-handling-08-validating-input-defensively-002-fc1f97b257.html"
 width="100%"
></iframe>

Now a bad entry simply loops back and asks again, exactly the `while True` with `continue` and `break` pattern from the looping unit, finally closing the gap that lesson left open.

## Adding try/except: Defending Against What Conditions Cannot Predict

The `.isdigit()` check above quietly assumes a very specific kind of bad input, text instead of digits. It does not protect against every possible failure a more complex conversion might hit, and in genuinely complex validation, a `try`/`except` around the risky conversion itself is often more general and more robust than chaining condition after condition trying to anticipate every bad shape in advance.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-12-exception-handling-08-validating-input-defensively-003-a2f14d005f.html"
 width="100%"
></iframe>

Notice the division of labour here, the heart of defensive validation: `try`/`except` guards the conversion itself, the operation that can fail in ways hard to fully predict with conditions, while a plain `if` still checks the business rule, the range 1 to 120, which is not really about failure at all, just a rule about what counts as a sensible age.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-12-exception-handling/08_validation_loop_until_valid.png)


## A Complete, Reusable Validation Function

Wrapping this pattern in a function makes it reusable anywhere your program needs a validated number within a range.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-12-exception-handling-08-validating-input-defensively-004-4be7525cd2.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-12-exception-handling-08-validating-input-defensively-005-f11045bb20.html"
 width="100%"
></iframe>

Try entering "abc", then "0", then "3", and confirm only the third attempt is ever accepted, with the first two re-asking instead of crashing or silently continuing.

## Conclusion

Defensive input validation combines a loop to keep asking after a rejected attempt, `try`/`except` to survive conversions that cannot be fully anticipated with conditions alone, and plain `if` checks to enforce the business rules that matter once a value has successfully converted. This is the complete picture the control flow unit promised was coming, finally assembled from loops and exception handling together. The final lesson of this unit steps back from any one pattern to ask the broader question: what does it actually mean to design a program that treats errors as a normal, expected part of its design, rather than a failure to be merely survived?
