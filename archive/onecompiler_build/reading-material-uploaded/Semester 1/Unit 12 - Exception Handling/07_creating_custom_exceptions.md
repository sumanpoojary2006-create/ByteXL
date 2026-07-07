## Introduction

Asha's signup form now raises a plain `ValueError` for several genuinely different problems: an age that is negative, an age that is unreasonably large, and a name field left completely blank. Every one of these currently looks identical to whoever is catching it, just a generic `ValueError`, with the actual difference buried inside the message text, which means catching "specifically the age problem, not the name problem" is not really possible without fragile, manual checks on the message itself.

Python lets you define your own exception types, just like the classes from the OOP unit, giving each distinct kind of problem its own clearly named identity that calling code can catch specifically, instead of every custom failure looking like generic, indistinguishable noise.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-12-exception-handling/07_custom_exception_types.png)

## Defining a Custom Exception

A custom exception is a class, defined exactly like the classes from the object-oriented programming unit, except it inherits from Python's built-in `Exception` class, which is what makes it usable with `raise` and `except` at all.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-12-exception-handling-07-creating-custom-exceptions-001-52a81dda74.html"
 width="100%"
></iframe>

That `pass` is enough for a complete, usable exception type. Inheriting from `Exception` (a detail you will explore properly in a later, deeper OOP course) gives `InvalidAgeError` everything it needs to behave exactly like `ValueError` or `ZeroDivisionError` do, simply under a name Asha chose herself.

## Raising and Catching a Custom Exception

A custom exception is raised and caught exactly like any built-in one, since `raise` and `except` do not distinguish between Python's own exceptions and ones you define yourself.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-12-exception-handling-07-creating-custom-exceptions-002-84f0c9692a.html"
 width="100%"
></iframe>

The output reads `Registration failed: Age must be between 0 and 120.`, and crucially, this `except` will only ever catch an `InvalidAgeError`, never accidentally swallowing some unrelated `ValueError` that happened to occur somewhere else in a larger `try` block.

## Several Custom Exceptions, Each Clearly Named

The real benefit appears once a program has several genuinely different problems worth telling apart.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-12-exception-handling-07-creating-custom-exceptions-003-8981f2cca8.html"
 width="100%"
></iframe>

Each `except` now catches exactly the problem its name promises, and the calling code can respond completely differently to a missing name versus an invalid age, something a single, generic `ValueError` for both could never have allowed this cleanly.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-12-exception-handling/07_custom_exception_hierarchy.png)


## A Custom Exception Can Still Be Caught Broadly

Because every custom exception still inherits from `Exception`, a broad `except Exception:` continues to catch it too, exactly the inheritance relationship the lesson on multiple exceptions warned you to order carefully.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-12-exception-handling-07-creating-custom-exceptions-004-141e3d5592.html"
 width="100%"
></iframe>

This still works, catching the `EmptyNameError` along with anything else, but it loses the specific, separate handling the earlier example demonstrated. Reach for specific custom exceptions when you actually want to respond differently; reach for a broad catch only when any failure here truly deserves the exact same response.

## Custom Exceptions at a Glance

| Step | Code |
|---|---|
| Define one | `class InvalidAgeError(Exception): pass` |
| Raise it | `raise InvalidAgeError("message")` |
| Catch it specifically | `except InvalidAgeError as error:` |
| Still caught by a broad handler | `except Exception:` also matches it |

## Your Turn: Name Your Own Problem

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-12-exception-handling-07-creating-custom-exceptions-005-deeffa80a5.html"
 width="100%"
></iframe>

Notice how much more this name communicates on its own than a generic `ValueError` ever could, both to whoever reads the `raise` line and to whoever writes the matching `except`.

## Conclusion

A custom exception is a class inheriting from `Exception`, giving a specific kind of problem its own clearly named identity that can be raised and caught exactly like any built-in exception type, letting calling code respond differently to genuinely different problems instead of treating every custom failure as indistinguishable, generic noise. A custom exception is still caught by a broad `except Exception:`, so specificity is a choice you make deliberately, not a guarantee enforced automatically. With the ability to name and catch your own problems precisely, the next lesson combines everything from this unit into a complete, defensive input-validation pattern.
