## Introduction

Naveen keeps almost reinventing things Python already ships with, simply because he has not yet been formally introduced to where they live. He once wrote his own little loop to guess a random number between 1 and 6 for a hostel dice game, never realising a ready-made tool already existed. He needed today's date stamped onto a report and typed it in by hand instead. Python's **standard library** is the large collection of modules that ships with every Python installation, with no separate install step at all, and a handful of them are worth knowing on sight.

This lesson is a guided tour of four of the most useful ones: `math`, `random`, `datetime`, and `os`.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-10-modules-and-packages/03_standard_library_toolboxes.png)

## math: Numbers Beyond the Basic Operators

The `math` module covers mathematical operations beyond the plain arithmetic operators you already know.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-10-modules-and-packages-03-touring-the-standard-library-001-7fae953d70.html"
 width="100%"
></iframe>

`math.ceil` and `math.floor` are exactly the rounding-up and rounding-down tools that floor division alone could not give you for arbitrary decimal values, and `math.pi` saves you from ever mistyping the constant by hand.

## random: Unpredictability, on Purpose

The `random` module generates values that are deliberately unpredictable, exactly what Naveen's dice game needed.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-10-modules-and-packages-03-touring-the-standard-library-002-6379c3ab80.html"
 width="100%"
></iframe>

`random.randint(a, b)` includes both endpoints, unlike `range()`, which is worth double-checking whenever the exact boundary matters. `random.choice` picks one item from any sequence, perfect for a raffle draw or randomly assigning room pairs.

## datetime: Working With Dates and Times

The `datetime` module represents calendar dates and times as proper, structured values, instead of error-prone strings you would have to parse by hand.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-10-modules-and-packages-03-touring-the-standard-library-003-82d243d045.html"
 width="100%"
></iframe>

Subtracting one `date` from another hands back a `timedelta` object, and its `.days` attribute gives you the plain number of days between them, exactly the "how many days until the trip" calculation Naveen used to do by counting on his fingers.

## os: Talking to the Operating System

The `os` module lets your script interact with the file system itself: where it is running, and what files surround it.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-10-modules-and-packages-03-touring-the-standard-library-004-c675d4b155.html"
 width="100%"
></iframe>

`os.getcwd()` answers "where is this script actually running from," and `os.listdir(".")` answers "what files are sitting right here," both genuinely useful the moment your scripts start reading or writing files of their own, a skill you will build properly in the file handling unit.

## Four Modules at a Glance

| Module | Solves | Example |
|---|---|---|
| `math` | Mathematical operations beyond `+ - * /` | `math.sqrt(64)` |
| `random` | Deliberate unpredictability | `random.choice(names)` |
| `datetime` | Dates, time spans, and calendar math | `trip_date - today` |
| `os` | Talking to the file system | `os.listdir(".")` |

These four barely scratch the surface of the standard library, which contains dozens of modules, but they are common enough that recognising them on sight, and knowing roughly what each is for, will serve you in almost every real script you write.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-10-modules-and-packages/03_stdlib_import_without_install.png)


## Your Turn: A Quick Tour in One Script

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-10-modules-and-packages-03-touring-the-standard-library-005-316fb7d5ef.html"
 width="100%"
></iframe>

Run this a few times and notice `math.sqrt` always answers the same way, while `random.choice` genuinely changes, and `datetime.date.today()` reflects whatever day it actually is when you run it.

## Conclusion

`math` covers calculations beyond plain arithmetic, `random` generates deliberate unpredictability for games and sampling, `datetime` represents dates and time spans as structured, calculable values, and `os` lets a script see and navigate the file system it is running in. All four ship with Python itself, ready to import with no separate installation. The next lesson turns this around: instead of touring modules someone else wrote, you will properly build and import one of your own.
