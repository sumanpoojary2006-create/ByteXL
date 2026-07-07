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

```python
prices = {"T-shirt": 350, "Mug": 150}    # lookup by name
order = ["T-shirt", "Mug", "Badge"]       # lookup by position
print(order)
```

## Question 2: Do I Only Care Whether Something Is Present?

If position and extra detail do not matter, and the only real question is "have I seen this before", a set is the right fit, especially once duplicates are a real risk.

```python
scanned_ids = set()    # only care: is this ID already in?
print(scanned_ids)
```

## Question 3: Will This Collection of Values Change?

If yes, a list or a dictionary; if the values form a fixed, related group that should never change, a tuple.

```python
snack_list = ["chips", "biscuits"]              # will change -> list
gps_coordinates = (15.2993, 74.1240)            # fixed forever -> tuple
print(gps_coordinates)
```

## Question 4: Am I Pairing Each Item With Extra Information?

A plain list holds standalone values. The moment each item needs an attached detail, a price, a count, a coordinate, you are really describing key-value data, which points to a dictionary, or a list of tuples if every record has the same fixed shape.

```python
stock = {"T-shirt": 12, "Mug": 8}                       # dictionary: name -> count
stops = [("Resort", 15.29, 74.12), ("Falls", 15.31, 74.31)]  # list of tuples: fixed records
print(stops)
```

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

```python
submitted_ids = set()
submitted_ids.add("S101")
submitted_ids.add("S102")
print("S101 submitted?", "S101" in submitted_ids)

scores = {"Asha": 92, "Ravi": 78}
scores["Meera"] = 85
print("Scores:", scores)

top_stop = ("Resort", 15.2993, 74.1240)
print("Fixed stop:", top_stop)

snack_list = ["chips", "biscuits"]
snack_list.append("juice")
print("Editable list:", snack_list)
```

Each of the four lines above answers a different one of the four questions from this lesson, with the structure chosen to match.

## Conclusion

Choosing a data structure is really just answering four questions in sequence: does it need a name-based lookup, does it only need presence checking, will it change, and does each item carry extra attached detail. Lists, tuples, sets, and dictionaries each answer a different combination of those questions, and a real program reaches for all four, often in the same few lines, exactly as Tara's gate log, price list, and stall report did throughout this fest. With these tools in hand, you are ready to organise, store, and transform almost any real-world data Python throws your way.
