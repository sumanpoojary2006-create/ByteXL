## Introduction

Asha is filling a college event signup form on her phone, and it keeps stopping her. She types "abc" in the age field and it flashes red. She tries "200" and it refuses again. She leaves a field blank and it will not submit. The form simply will not trust whatever she types until it makes sense. People leave fields blank, type letters where numbers belong, enter an age of 200, or paste in extra spaces, and a program that blindly trusts whatever it is given will sooner or later crash or, worse, produce a confidently wrong result.

The form on Asha's screen was not being difficult for its own sake; it was refusing to move forward with data it could not trust, exactly the discipline a well-written program needs. Input validation is the habit of checking input before you rely on it, and it brings together every idea in this unit: conditions, comparisons, truthiness, and clear branching.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t8hpwft/09_input_validation_gatekeeper.png)

## Never Trust Raw Input

Recall a trap from an earlier unit. The `input` function always returns text, so converting it to a number with `int` only works if the text actually looks like a number.

```python
age = int(input("Your age: "))    # crashes if the user types "abc"
print(age)
```

If someone types "abc", this line stops the whole program with an error. The fix is not to hope users behave, but to check first and respond gracefully.

## Check Before You Use

A useful tool here is the string method `.isdigit()`, which returns `True` only when the text is made entirely of digits. You can test the input before trusting it, then apply range checks once you know it is a number.

```python
entry = input("Your age: ")

if not entry.isdigit():
    print("Please enter digits only.")
else:
    age = int(entry)
    if age < 1 or age > 120:
        print("That age is out of range.")
    else:
        print(f"Thank you. Your age is {age}.")
```

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

```python
marks = input("Enter marks (0 to 100): ")

if not marks.isdigit():
    print("Invalid: marks must be a whole number.")
elif int(marks) > 100:
    print("Invalid: marks cannot exceed 100.")
else:
    print(f"Marks accepted: {marks}")
```

Test it with "abc", then "150", then "85". Each bad case is caught with its own clear message, and only sensible input is accepted. You have just made a program that defends itself.

## Conclusion

Input validation means checking data before you use it, because users will inevitably enter the unexpected. Combine the tools of this unit: test the shape of the input (for example with `.isdigit()`), apply range checks, and branch clearly to reject bad values with helpful messages. Conditions alone cannot re-ask or catch every error yet, and loops and exception handling will complete the picture in later units. But the mindset starts now: never trust raw input, always check it first. Branching has taught your programs to choose; the next unit teaches them to repeat, which is exactly what Asha's form still cannot do on its own when it needs to ask again after a bad entry.
