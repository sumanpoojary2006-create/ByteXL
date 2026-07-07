## Introduction

Once a program holds numbers, the next thing it does is calculate with them. Totalling a bill, working out an average, splitting a cost among friends, checking whether a number is even: all of these are arithmetic, and all of them were once tasks you did slowly by hand, with a pen, a calculator, or a careful bit of mental maths. A program just does the same arithmetic at a speed and scale a person never could, which is one of the simplest reasons computers were built in the first place. Python uses the familiar symbols you already know from school, and adds a couple of genuinely useful ones that you may not have seen before.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t82yggj/05_basic_arithmetic_prep.png)


## The Familiar Five and Two Extras

Most arithmetic operators look exactly as you expect:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2FyaXRobWV0aWNfb3BlcmF0b3JzIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJwcmludCgxMCArIDMpICAgICMgMTMgICBhZGRpdGlvblxucHJpbnQoMTAgLSAzKSAgICAjIDcgICAgc3VidHJhY3Rpb25cbnByaW50KDEwICogMykgICAgIyAzMCAgIG11bHRpcGxpY2F0aW9uXG5wcmludCgxMCAvIDMpICAgICMgMy4zMzMuLi4gIGRpdmlzaW9uXG5wcmludCgxMCAqKiAzKSAgICMgMTAwMCAgcG93ZXIgKDEwIHRvIHRoZSBwb3dlciAzKSJ9"
 width="100%"
></iframe>

The first four are old friends. The double star, `**`, means "raise to the power of", so `2 ** 10` is 1024. That leaves two more operators that are quietly some of the most useful in all of programming.

## Arithmetic Operators at a Glance

| Operator | Name | Example | Result |
|---|---|---|---|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `/` | Division | `10 / 3` | `3.333...` |
| `**` | Power | `10 ** 3` | `1000` |
| `//` | Floor division | `17 // 5` | `3` |
| `%` | Modulo (remainder) | `17 % 5` | `2` |

## Two Operators Worth Meeting: // and %

The double slash, `//`, is floor division. It divides and then throws away the fractional part, giving you the whole number of times one value fits into another. The percent sign, `%`, is the modulo operator, and it gives the remainder left over.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2FyaXRobWV0aWNfb3BlcmF0b3JzIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJwcmludCgxNyAvLyA1KSAgICMgMyAgICBmaXZlIGZpdHMgaW50byBzZXZlbnRlZW4gdGhyZWUgd2hvbGUgdGltZXNcbnByaW50KDE3ICUgNSkgICAgIyAyICAgIHdpdGggdHdvIGxlZnQgb3ZlciJ9"
 width="100%"
></iframe>

Why care about a remainder? Because it answers questions that come up constantly. How do you tell if a number is even? Check whether `number % 2` equals 0. How do you find the last digit of a number? Take `number % 10`. How do you turn 250 minutes into hours and minutes? Hours are `250 // 60` and the leftover minutes are `250 % 60`. Without these two operators you would have to write several clumsy lines of logic to answer each of those questions; with them, the answer fits on one line. These two operators turn fiddly problems into a single line, and once you start looking for them, you will notice the "how many whole groups, and what is left over" shape hiding inside an enormous number of everyday problems.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t82yggj/05_floor_division_and_remainder_pie.png)


## A Small but Important Detail

Notice that plain division with a single slash always produces a float, even when the numbers divide evenly:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2FyaXRobWV0aWNfb3BlcmF0b3JzIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJwcmludCg4IC8gMikgICAgIyA0LjAsIG5vdCA0In0"
 width="100%"
></iframe>

If you specifically want a whole number answer, use floor division instead. Mixing these up is a common source of surprise, so when a result has an unexpected decimal point, the single slash is usually the reason. It is a small inconsistency worth memorising once and never being confused by again, since the rule never changes: `/` always promises a float, no matter how evenly the numbers divide.

## Operators Are Not Just for Numbers

Strings borrow two of these very symbols, with a different meaning. `+` joins two strings together, and `*` repeats one a chosen number of times.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2FyaXRobWV0aWNfb3BlcmF0b3JzIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJwcmludChcImhhXCIgKiAzKSAgICAgICAgIyBoYWhhaGFcbnByaW50KFwiUHlcIiArIFwidGhvblwiKSAgICMgUHl0aG9uIn0"
 width="100%"
></iframe>

Same symbol, a different meaning depending on the type it is used with, which is exactly why checking `type()` is worth doing whenever a result surprises you.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t82yggj/05_string_operator_meanings.png)


## Your Turn: Split the Bill

This program shares a bill among friends and reports both the fair share and the awkward remainder.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2FyaXRobWV0aWNfb3BlcmF0b3JzIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJ0b3RhbCA9IGludChpbnB1dChcIlRvdGFsIGJpbGw6IFwiKSlcbnBlb3BsZSA9IGludChpbnB1dChcIk51bWJlciBvZiBwZW9wbGU6IFwiKSlcblxucHJpbnQoXCJFYWNoIHBheXM6XCIsIHRvdGFsIC8vIHBlb3BsZSlcbnByaW50KFwiTGVmdCBvdmVyOlwiLCB0b3RhbCAlIHBlb3BsZSkifQ"
 width="100%"
></iframe>

Try a bill of 1000 split among 3 people. Each pays 333, with 1 rupee left over that someone has to cover. Floor division found the equal share, and modulo found exactly what could not be divided evenly.

## Conclusion

Python's arithmetic operators cover the usual addition, subtraction, multiplication, division, and powers with `**`, and add two quiet workhorses: floor division `//` for the whole part and modulo `%` for the remainder. Reach for modulo whenever you need to test divisibility, extract digits, or split things into groups. They look small, but they solve a remarkable number of real problems in a single stroke.
