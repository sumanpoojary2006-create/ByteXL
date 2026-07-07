## Introduction

The fest is over, and Tara is writing notes for next year's coordinator, the same way you might leave comments for your future self. Looking back at everything she built, the gate log, the price list, the stock counts, the combined stall report, she realises every single one of those choices came down to answering the same small set of questions about the data, not to memorising syntax. Now that you know lists, tuples, sets, and dictionaries, the real skill is choosing the right one before you write a single bracket.

This final lesson is a direct comparison across all four, so that choice becomes fast and confident rather than a guess.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-7-sets-and-dictionaries/08_four_structures_decision_board.png)

## The Four Structures, Side by Side

| Structure | Brackets | Ordered | Mutable | Duplicates | Looked Up By |
|---|---|---|---|---|---|
| List | `[ ]` | Yes | Yes | Allowed | Position |
| Tuple | `( )` | Yes | No | Allowed | Position |
| Set | `{ }` or `set()` | No | Yes | Removed automatically | Membership only |
| Dictionary | `{ }` with `key: value` | Insertion order kept | Yes | Keys must be unique | Key |

Every choice you have made across the last two units traces back to one row of this table.

## Question 1: Do I Need to Look Things Up by a Meaningful Name?

If you find yourself wanting to ask "what is the price of the mug" rather than "what is the third item", you need a dictionary, not a list.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2Nob29zaW5nX3RoZV9yaWdodF9kYXRhX3N0cnVjdHVyZSBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoicHJpY2VzID0ge1wiVC1zaGlydFwiOiAzNTAsIFwiTXVnXCI6IDE1MH0gICAgIyBsb29rdXAgYnkgbmFtZVxub3JkZXIgPSBbXCJULXNoaXJ0XCIsIFwiTXVnXCIsIFwiQmFkZ2VcIl0gICAgICAgIyBsb29rdXAgYnkgcG9zaXRpb24ifQ"
 width="100%"
></iframe>

## Question 2: Do I Only Care Whether Something Is Present?

If position and extra detail do not matter, and the only real question is "have I seen this before", a set is the right fit, especially once duplicates are a real risk.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2Nob29zaW5nX3RoZV9yaWdodF9kYXRhX3N0cnVjdHVyZSBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoic2Nhbm5lZF9pZHMgPSBzZXQoKSAgICAjIG9ubHkgY2FyZTogaXMgdGhpcyBJRCBhbHJlYWR5IGluPyJ9"
 width="100%"
></iframe>

## Question 3: Will This Collection of Values Change?

If yes, a list or a dictionary; if the values form a fixed, related group that should never change, a tuple.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2Nob29zaW5nX3RoZV9yaWdodF9kYXRhX3N0cnVjdHVyZSBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoic25hY2tfbGlzdCA9IFtcImNoaXBzXCIsIFwiYmlzY3VpdHNcIl0gICAgICAgICAgICAgICMgd2lsbCBjaGFuZ2UgLT4gbGlzdFxuZ3BzX2Nvb3JkaW5hdGVzID0gKDE1LjI5OTMsIDc0LjEyNDApICAgICAgICAgICAgIyBmaXhlZCBmb3JldmVyIC0-IHR1cGxlIn0"
 width="100%"
></iframe>

## Question 4: Am I Pairing Each Item With Extra Information?

A plain list holds standalone values. The moment each item needs an attached detail, a price, a count, a coordinate, you are really describing key-value data, which points to a dictionary, or a list of tuples if every record has the same fixed shape.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2Nob29zaW5nX3RoZV9yaWdodF9kYXRhX3N0cnVjdHVyZSBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoic3RvY2sgPSB7XCJULXNoaXJ0XCI6IDEyLCBcIk11Z1wiOiA4fSAgICAgICAgICAgICAgICAgICAgICAgIyBkaWN0aW9uYXJ5OiBuYW1lIC0-IGNvdW50XG5zdG9wcyA9IFsoXCJSZXNvcnRcIiwgMTUuMjksIDc0LjEyKSwgKFwiRmFsbHNcIiwgMTUuMzEsIDc0LjMxKV0gICMgbGlzdCBvZiB0dXBsZXM6IGZpeGVkIHJlY29yZHMifQ"
 width="100%"
></iframe>

## A Worked Decision

Suppose you are asked to track which students have submitted an assignment. There is no extra detail to attach, just presence or absence, and the list will only ever grow as more students submit, never need positional access. A set fits perfectly: `submitted = set()`, with `submitted.add(student_id)` each time someone turns work in, and `student_id in submitted` to check.

Now suppose instead you are asked to track each student's actual score. There is a meaningful value attached to each name, so a dictionary fits: `scores = {"Asha": 92, "Ravi": 78}`, looked up directly by name whenever needed.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-7-sets-and-dictionaries/08_structure_choice_question_flow.png)


## The Full Decision Table

| Need | Reach For |
|---|---|
| Ordered values that may change | List |
| A fixed, related group of values | Tuple |
| Only presence or absence, no duplicates | Set |
| A value looked up by a meaningful key | Dictionary |
| A growing collection of fixed records | List of tuples |
| Grouped key-value data, several layers deep | Nested dictionary |

## Your Turn: Pick the Right Container

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2Nob29zaW5nX3RoZV9yaWdodF9kYXRhX3N0cnVjdHVyZSBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoic3VibWl0dGVkX2lkcyA9IHNldCgpXG5zdWJtaXR0ZWRfaWRzLmFkZChcIlMxMDFcIilcbnN1Ym1pdHRlZF9pZHMuYWRkKFwiUzEwMlwiKVxucHJpbnQoXCJTMTAxIHN1Ym1pdHRlZD9cIiwgXCJTMTAxXCIgaW4gc3VibWl0dGVkX2lkcylcblxuc2NvcmVzID0ge1wiQXNoYVwiOiA5MiwgXCJSYXZpXCI6IDc4fVxuc2NvcmVzW1wiTWVlcmFcIl0gPSA4NVxucHJpbnQoXCJTY29yZXM6XCIsIHNjb3JlcylcblxudG9wX3N0b3AgPSAoXCJSZXNvcnRcIiwgMTUuMjk5MywgNzQuMTI0MClcbnByaW50KFwiRml4ZWQgc3RvcDpcIiwgdG9wX3N0b3ApXG5cbnNuYWNrX2xpc3QgPSBbXCJjaGlwc1wiLCBcImJpc2N1aXRzXCJdXG5zbmFja19saXN0LmFwcGVuZChcImp1aWNlXCIpXG5wcmludChcIkVkaXRhYmxlIGxpc3Q6XCIsIHNuYWNrX2xpc3QpIn0"
 width="100%"
></iframe>

Each of the four lines above answers a different one of the four questions from this lesson, with the structure chosen to match.

## Conclusion

Choosing a data structure is really just answering four questions in sequence: does it need a name-based lookup, does it only need presence checking, will it change, and does each item carry extra attached detail. Lists, tuples, sets, and dictionaries each answer a different combination of those questions, and a real program reaches for all four, often in the same few lines, exactly as Tara's gate log, price list, and stall report did throughout this fest. With these tools in hand, you are ready to organise, store, and transform almost any real-world data Python throws your way.
