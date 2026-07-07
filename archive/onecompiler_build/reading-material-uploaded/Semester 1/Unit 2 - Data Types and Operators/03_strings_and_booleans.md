## Introduction

Numbers are only half the story. Programs also handle words and decisions. The message "Welcome, Asha", a city name, a password: all of these are text. And every time a program asks a yes or no question, like "is this user old enough?", the answer is a special value that is either true or false.

Python calls text a **string** and calls a true-or-false value a **boolean**. The two might look unrelated at first, but they share a job: numbers measure the world, while strings and booleans describe and judge it. A string carries what something is called; a boolean carries whether something holds true. Almost every program you will ever write ends up combining all three kinds of value in the same handful of lines. You will give strings a full unit of their own later. For now, this lesson introduces both so you can use them comfortably alongside numbers.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t82w7y6/03_string_concatenation_icing.png)


## Text Lives in Strings

A string is any sequence of characters wrapped in quotation marks. You may use single or double quotes, as long as you are consistent.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-2-data-types-and-operators-03-strings-and-booleans-001-a7753d5316.html"
 width="100%"
></iframe>

The quotes are the signal that says "this is text, not a command and not a number". Leave them off and Python will think `Asha` is a variable name and complain that it does not exist. This is one of the most common early slips: writing `name = Asha` instead of `name = "Asha"` looks almost identical on screen, yet the first asks Python to go find something called Asha that was never created, while the second simply hands over four letters to store. A pair of quotes is a small mark, but it changes the entire meaning of the line.

Strings can be joined together with the plus sign, an action called concatenation.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-2-data-types-and-operators-03-strings-and-booleans-002-584b381f06.html"
 width="100%"
></iframe>

Output:

```
Sachin Tendulkar
```

Notice the small `" "` in the middle. Without that deliberate space, the names would run together as `SachinTendulkar`, because Python adds exactly what you tell it and nothing more.

## True or False: the Boolean

A boolean, written `bool`, can hold only two values: `True` or `False`. They must be capitalised, and they are not strings, so they take no quotes. Booleans usually appear as the answer to a comparison.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-2-data-types-and-operators-03-strings-and-booleans-003-38658e9909.html"
 width="100%"
></iframe>

Output:

```
True
```

The program compared 20 with 18, found the statement true, and stored that truth in `is_adult`. Notice that `is_adult` is not holding the number 20, and it is not holding the text "yes". It is holding a verdict, a single bit of judgment that the rest of the program can act on without redoing the comparison. Booleans are the foundation of every decision a program makes, which you will use heavily when you reach control flow.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t82w7y6/03_boolean_scorecard.png)


Here is a question worth previewing: is the number 0 considered true or false? In Python, 0 counts as false and any other number counts as true, an idea called truthiness that you will explore properly in the control-flow unit. For now, just notice that truth and numbers are quietly connected.

## Truthy and Falsy at a Glance

| Value | Treated As |
|---|---|
| `0` | False |
| Any non-zero number | True |
| `""` (empty string) | False |
| Any non-empty string | True |
| `False` | False |
| `True` | True |

You will use this constantly once you reach control flow, where a line like `if some_value:` is quietly checking exactly this.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t82w7y6/03_truthy_falsy_switchboard.png)


## Your Turn: Adult or Not

This program reads an age and reports a boolean decision.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-2-data-types-and-operators-03-strings-and-booleans-004-f5cd12cb47.html"
 width="100%"
></iframe>

Try it with 15 and then with 21. The same line of logic prints `False` for one and `True` for the other, without you changing a single character of the program. That is the power of letting a boolean carry the answer.

## Conclusion

Strings hold text and always sit inside quotes, while booleans hold one of two truth values, `True` or `False`, usually produced by a comparison. Together with numbers, these are the everyday materials your programs are built from: numbers to count and measure, strings to label and communicate, and booleans to decide. You will return to each in greater depth, but you can already mix all three with confidence. The next lesson tackles a problem these three types create the moment they meet each other: what happens when a number needs to become text, or text needs to become a number.
