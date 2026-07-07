## Introduction

Asha opens the canteen ordering app on her phone and sees a short menu: press 1 for the thali, 2 for a sandwich, 3 for a coffee, and a catch-all option for anything else. She taps 2 and the sandwich option lights up instantly, no long staircase of checks needed, just a direct match against a known option. Which menu item did the user pick, 1, 2, or 3? Which command did they type, "start", "stop", or "help"? You can already handle this with an `if`/`elif` chain, but when every branch compares the same variable to a different fixed value, something cleaner fits the menu's shape better.

An `elif` chain would work here too, but it would mean repeating "choice equals" on every single line just to compare the same variable against one fixed option after another. Python offers exactly that: the `match`/`case` statement, available in Python 3.10 and newer.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t8hm2bs/06_match_case_menu.png)

## Choosing From a Menu of Options

First, here is the familiar `elif` way, comparing one variable against several values:

```python
command = "start"
if command == "start":
    print("Starting...")
elif command == "stop":
    print("Stopping...")
elif command == "help":
    print("Showing help")
else:
    print("Unknown command")
```

It works, but notice how `command ==` is repeated on every line. The `match` statement removes that repetition and makes the intent obvious.

## The match and case Syntax

You state the value to match once, then list each possibility as a `case`.

```python
command = "start"
match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "help":
        print("Showing help")
    case _:
        print("Unknown command")
```

Python compares `command` against each `case` from top to bottom and runs the first one that matches. The structure reads like a clean table of options, which is much easier to scan than a wall of `elif` lines.

## The Underscore Is the Catch-All

The last case, `case _:`, uses an underscore as a wildcard that matches anything. It plays the role that `else` plays in an `if` chain: if none of the specific values matched, the underscore case runs. It is good practice to include it, so your program always has a sensible response to an unexpected value, the same net that quietly caught any stray tap outside Asha's three known menu options.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t8hm2bs/06_match_catch_all_case.png)


## match vs elif at a Glance

So which should you reach for?

| Situation | Better Tool |
|---|---|
| Comparing one value against several fixed, known options | `match`/`case` |
| Testing ranges, such as `marks >= 75` | `if`/`elif` |
| Combining conditions, such as `age >= 18 and has_id` | `if`/`elif` |

Choosing the right tool makes your intent obvious to anyone reading the code. It is also worth knowing that `match` can do more than this lesson shows, including matching the shape of a list or pulling values out of it directly in the `case` line, a feature called structural pattern matching that you will meet if you go further with Python.

## Your Turn: A Simple Menu

```python
print("1. Check balance")
print("2. Deposit")
print("3. Exit")
choice = input("Choose an option: ")

match choice:
    case "1":
        print("Your balance is 5000")
    case "2":
        print("Deposit selected")
    case "3":
        print("Goodbye")
    case _:
        print("Invalid choice")
```

Run it and pick 1, 2, 3, and then something random like 9. The matching option responds, and the underscore case politely handles anything unexpected. Remember that `input` returns text, which is why each case compares against a string like "1", not the number 1.

## Conclusion

The `match`/`case` statement is Python's clean way to compare one value against several fixed options, stating the value once and listing each possibility as a `case`, with `case _` acting as the catch-all. Prefer it for menu-style choices and known commands, and keep `if`/`elif` for ranges and combined conditions. Same decision-making power, expressed in whichever form reads most clearly. Every condition seen so far has compared a clear value, but Python is also willing to judge values that are not booleans at all, which is exactly the surprising idea the next lesson opens with.
