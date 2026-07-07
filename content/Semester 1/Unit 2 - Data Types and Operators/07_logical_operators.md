## Introduction

Real decisions are rarely about a single condition. A bank approves a withdrawal if the card is valid and the balance is sufficient. A shop offers a discount if you are a member or it is the festive season. A form rejects you if you are not old enough. The previous lesson taught you how to ask a single yes or no question with a comparison; real rules almost always stack several of those questions together before reaching one final verdict. These little words, and, or, and not, are how we combine yes or no answers into a final verdict, and Python uses them as **logical operators**.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t8334sg/07_and_gate_two_knobs.png)


## Combining Yes or No Answers

Logical operators take boolean values, the `True` and `False` results of comparisons, and combine them into a single boolean.

- `and` is true only when both sides are true.
- `or` is true when at least one side is true.
- `not` simply flips a value to its opposite.

```python
print(True and False)   # False, because not both are true
print(True or False)    # True, because one of them is true
print(not True)         # False, the opposite of true
```

Think of `and` as a strict gatekeeper that demands everything pass, and `or` as a generous one that is happy with any single pass. Picture a security guard at the entrance to the theme park ride checked against both a height marker and an age sign: the guard checking both conditions together is acting like `and`, while a guard who waves you through for satisfying either of two separate offers is acting like `or`. The words read almost exactly like ordinary English, which is precisely what makes logical operators easy to write and dangerously easy to get backwards if you are not careful.

## Logical Operators at a Glance

| A | B | A and B | A or B |
|---|---|---|---|
| True | True | True | True |
| True | False | False | True |
| False | True | False | True |
| False | False | False | False |

`not` simply flips a single value, so `not True` is `False` and `not False` is `True`.

## Putting Them to Work

Imagine a theme park ride that requires a rider to be at least 120 centimetres tall and at least 8 years old. Both must be true, so you join the two comparisons with `and`.

```python
height = 130
age = 10
can_ride = height >= 120 and age >= 8
print("Allowed on the ride?", can_ride)
```

Now picture a discount that applies if you are a member or it is your first visit. Here either condition is enough, so you use `or`. And `not` is perfect for rejecting: `not is_member` is true exactly when someone is not a member.

A natural question: in `age >= 8 and height >= 120`, what happens if the first part is already false? Python is efficient and stops checking as soon as the outcome is certain, since one false side makes the whole `and` false. This behaviour is called short-circuiting, and it quietly saves work.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t8334sg/07_short_circuit_logic.png)


## Your Turn: Two-Condition Gate

This program grants access only when both conditions hold.

```python
age = int(input("Your age: "))
has_ticket = input("Do you have a ticket? (yes/no): ") == "yes"

allowed = age >= 18 and has_ticket
print("Entry allowed?", allowed)
```

Try it as an 18 year old with a ticket, then again without one. Only when both parts are true does the gate open. Changing the `and` to an `or` would change the whole meaning, so the operator you choose is itself a decision about how strict the rule should be.

## Conclusion

Logical operators combine boolean values into a single decision: `and` needs every condition to be true, `or` needs only one, and `not` flips a value. Real rules are almost always combinations like these, so learning to translate a sentence such as "old enough and has a ticket" into `age >= 18 and has_ticket` is one of the most directly useful skills in programming. Once that translation becomes second nature, you can read almost any everyday eligibility rule, a loan approval, a competition entry, a login check, and immediately see the `and`, `or`, and `not` hiding inside the sentence.
