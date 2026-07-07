## Introduction

Tara's script crashes partway through writing the day's sales report, somewhere between `open()` and the `close()` she dutifully wrote at the end, because of an unrelated bug a few lines in between. The crash means Python jumps straight to reporting the error and stops executing the rest of that block entirely, including her `close()` call, which never runs. The file is left open, possibly with only some of its intended content actually saved to disk, a quiet, easy-to-miss kind of bug that only shows up later, when something tries to read a report that turns out to be incomplete.

The problem is not that Tara forgot to write `close()`. It is that `close()` only runs if every single line before it succeeds, and real code occasionally does not. Python's `with` statement solves this by guaranteeing a file gets closed automatically, even when something goes wrong in between.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-11-file-handling/04_with_statement_guarantees_close.png)

## The Problem With Manual close()

```python
file = open("sales_report.txt", "w")
file.write("Day 1 Sales Report\n")
total = 100 / 0          # an unrelated bug, crashes right here
file.write("Total: " + str(total) + "\n")
file.close()              # never reached!
```

```
ZeroDivisionError: division by zero
```

The division by zero raises a `ZeroDivisionError` and stops the script immediately. `file.close()`, sitting two lines below, never gets a chance to run, because Python never reaches it. The file is left open, and the report is incomplete. Handling an error like this cleanly is the subject of a later unit; the point here is only that a crash between `open()` and `close()` leaves the file dangling.

## The with Statement: A Guaranteed Close

`with open(...) as file:` opens a file, runs an indented block using it, and guarantees the file is closed the moment that block ends, whether it finishes normally or is interrupted by an error partway through.

```python
with open("sales_report.txt", "w") as file:
    file.write("Day 1 Sales Report\n")
    file.write("Total: 4500\n")

# The block has ended, so with has already closed the file for us:
print("Is the file closed now?", file.closed)    # True

# Read it back to confirm the content was saved -- no close() was ever needed
with open("sales_report.txt", "r") as file:
    print(file.read())
```

There is no explicit `.close()` anywhere in this code, and none is needed. The instant the indented block under `with` finishes, Python closes the file automatically, which is why `file.closed` already reports `True` on the very next line.

## The Guarantee Holds Even When a Line Crashes

The real value of `with` shows up when something goes wrong inside the block. Here the same unrelated bug from the opening example crashes partway through, but this time the file is opened with `with`.

```python
with open("sales_report.txt", "w") as file:
    file.write("Day 1 Sales Report\n")
    total = 100 / 0          # crashes here, inside the with block
    file.write("Total: " + str(total) + "\n")
```

```
ZeroDivisionError: division by zero
```

This raises the exact same `ZeroDivisionError` as before, and the script still stops. The crucial difference is invisible in the output: as the block was interrupted on its way out, `with` still closed the file automatically, exactly as it did on the normal path above, because `with` releases the file however the block exits, cleanly or through an error. Everything written before the crash was flushed and saved; only the line after the crash is missing, which is precisely the behaviour you want.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-11-file-handling/04_with_context_manager_flow.png)


## Rewriting Earlier Lessons With with

Every `open()` and `close()` pair from the last two lessons can be rewritten this way, and from this point in the course onward, it is the way you should always open a file.

```text file=attendees.txt
A101
A102
A103
```

```python with=attendees.txt
with open("attendees.txt", "r") as file:
    for line in file:
        print(line.strip())
```

```python
with open("fest_log.txt", "w") as file:      # start the day's log
    file.write("Gate opened at 9 AM\n")

with open("fest_log.txt", "a") as file:      # append without erasing
    file.write("Stall closed at 6 PM\n")

with open("fest_log.txt", "r") as file:
    print(file.read())
```

The mode argument, `"r"`, `"w"`, or `"a"`, works exactly as before; `with` changes nothing about how a file behaves, only how reliably it gets closed afterward.

## Manual close() vs with at a Glance

| | Manual open() / close() | with open() as file: |
|---|---|---|
| Closes on normal completion | Yes, if `close()` is reached | Yes, automatically |
| Closes if an error occurs first | No, `close()` is skipped | Yes, guaranteed regardless |
| Extra line needed | `file.close()` | None |
| Recommended for new code | No | Yes |

## Your Turn: Convert to a with Block

```python
with open("attendees.txt", "a") as file:
    file.write("A108\n")

with open("attendees.txt", "r") as file:
    print(file.read())
```

Notice both operations, appending and then reading back, use the same `with` shape, each one opening, using, and automatically closing the file within its own clean, indented block.

## Conclusion

The `with` statement opens a file, runs an indented block, and guarantees that file is closed the moment the block ends, whether it finishes cleanly or is interrupted by an error partway through, solving exactly the kind of silently-incomplete-file bug a forgotten or skipped `close()` can cause. From here on, prefer `with open(...) as file:` over a manual `open()`/`close()` pair for every file you work with. With safe, reliable opening settled, the next lesson turns to a detail that matters increasingly as projects grow: working with file paths correctly, using `pathlib`.
