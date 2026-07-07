## Introduction

Zara has isolated her bug down to five lines, but she still cannot see why it is happening, and it is now well past midnight. She is tempted to message a friend with "my code is broken, please help," but some part of her suspects that message will not actually get her very far. Before reaching out to anyone, there is a strange but genuinely effective technique worth trying first: explaining the problem out loud, in complete sentences, to something that cannot answer back, like a rubber duck sitting on the desk.

This is called **rubber-duck debugging**, and it works far more often than its silly name suggests, for a specific and explainable reason.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-13-debugging/08_rubber_duck_debugging.png)

## Why Explaining Out Loud Actually Works

Reading code silently lets your eyes skip over a line you already believe is correct, even when it is not, because skimming relies on assumptions you already hold. Explaining the same code out loud, in full sentences, forces you to state each assumption explicitly, and a wrong assumption sounds noticeably wrong the moment it leaves your mouth in a way it never did sitting quietly in your head.

```python
import traceback

class Attendee:
    def __init__(self, rsvp_count):
        self.rsvp_count = rsvp_count

def total_rsvps(attendees):
    return sum(attendee.rsvp_count for attendee in attendees)

# All numbers: works fine
print("Clean data:", total_rsvps([Attendee(2), Attendee(3)]))    # 5

# "wait, is rsvp_count always a number?" -- here one is a string:
try:
    print(total_rsvps([Attendee(2), Attendee("3")]))
except TypeError:
    print(traceback.format_exc())
```

Said out loud: "this goes through every attendee, and adds up their `rsvp_count`... and `rsvp_count` is always a number, because... wait, is it always a number? Where does this list actually come from?" That pause, "wait, is it always a number," is the entire technique working exactly as intended.

## A Concrete Rubber-Duck Script

The technique is more effective with a small amount of structure than with a vague "let me think about this," since structure forces you through the assumptions you are most likely to skip.

```python
# Walk through the rubber-duck debugging steps as print statements

steps = {
    "1. Expected behaviour": "Add up every attendee's rsvp_count and return the total.",
    "2. Actual behaviour":   "Crashes with TypeError on the sum() line.",
    "3. Error message":      "unsupported operand type(s) for +: 'int' and 'str'",
    "4. Root cause theory":  "rsvp_count must be a string somewhere -- likely the CSV loader.",
}

for step, explanation in steps.items():
    print(f"{step}:")
    print(f"  {explanation}")
    print()

print("Saying step 4 out loud often reveals the bug without any tool at all.")
```

Saying step four out loud is often the exact moment the bug becomes obvious, not because the duck answered, but because narrating the data's origin honestly, rather than assuming it was always fine, surfaces the gap.

## Asking a Human the Right Way, When the Duck Is Not Enough

Sometimes rubber-duck debugging alone does not surface the answer, and asking another person genuinely is the right next step. The difference between a question that gets fast, useful help and one that gets only "have you tried turning it off and on again" is almost entirely about how much of the rubber-duck script you include before asking.

```python
weak_question = "my code doesn't work, can someone help?"

strong_question = (
    "total_rsvps() raises TypeError: unsupported operand type(s) for +: 'int' and 'str'.\n"
    "Minimal case: counts = [2, '3']; sum(counts) -> TypeError.\n"
    "I expected every rsvp_count to be an int.\n"
    "I suspect the CSV loader never calls int() on that column.\n"
    "Does anyone see where the conversion is missing?"
)

print("Weak question:")
print(" ", weak_question)
print()
print("Strong question (includes error, minimal case, expectation, theory):")
for line in strong_question.split("\n"):
    print(" ", line)
```

The strong version includes the exact error, a minimal reproduction from the previous lesson, what was expected, and a specific, testable theory, everything anyone helping would otherwise have to ask for first, one slow message at a time.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-13-debugging/08_good_debug_question_card.png)

*A strong debugging question gives the helper the four things they need first: expected result, actual result, steps, and small code.*

## Good Questions at a Glance

| Weak Question | Strong Question |
|---|---|
| "It doesn't work" | The exact error message, copied in full |
| No code, or the entire project | A minimal failing case, from the previous lesson |
| No stated expectation | What you expected to happen, and why |
| No theory at all | A specific, testable guess about the cause |

## Your Turn: Write the Strong Version

```python
import traceback

def average_price(cart):
    return sum(cart.prices) / len(cart.prices)

class Cart:
    def __init__(self, prices):
        self.prices = prices

empty_cart = Cart([])
try:
    print(average_price(empty_cart))    # error! empty list -> divide by zero
except ZeroDivisionError:
    print(traceback.format_exc())
```

Write out, in full sentences, the four-step rubber-duck script for this bug: what you expected, what actually happens, what the error says read bottom-up, and your specific theory for why. Then write the strong version of a question you would ask someone else about it.

## Conclusion

Rubber-duck debugging works by forcing you to state your assumptions out loud, in complete sentences, which surfaces wrong assumptions that silent skimming lets slide past unnoticed, and the same structure, what you expected, what happened, the exact error, and a specific theory, turns a weak question into a strong one when you do need to ask another person for help. The final lesson of this unit, and this entire semester, turns that same structure toward one more collaborator worth asking carefully: an AI assistant, and what using one responsibly while debugging actually looks like.
