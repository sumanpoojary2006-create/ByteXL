## Introduction

Tara built a genuinely useful attendee set and a tidy stall report in the last unit, sets and dictionaries that correctly deduplicated wristband scans and summarised an entire day of sales. Then she closed her laptop, opened it again the next morning, ran the exact same script, and found absolutely nothing left over: no attendee set, no stall report, nothing. Every value her program ever held existed only in the computer's memory while the script was running, and the moment that script finished, all of it vanished as if it had never been calculated at all.

Memory is fast, but it is also temporary. To make data outlive a single run of a program, you need to write it somewhere that survives after the program stops, a process called **persistence**, and the most fundamental tool for it is the **file**.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-11-file-handling/01_memory_vanishes_file_persists.png)

## Why Variables Alone Are Not Enough

```python
attendees = {"A101", "A102", "A103"}
print(len(attendees))    # 3
```

Run this script, see the answer, and close it. The next time you run it, `attendees` starts completely empty again, rebuilt from scratch by whatever lines created it, because a variable's lifetime is tied entirely to the program that is currently running. There is nothing wrong with the code; it is simply doing exactly what a variable was always going to do.

## Writing to a File: A First Look

This unit will cover the full, careful syntax over the next several lessons, but here is the shape of what persistence actually looks like, so the destination is clear from the start.

```python
file = open("attendees.txt", "w")
file.write("A101\n")
file.write("A102\n")
file.write("A103\n")
file.close()

print("attendees.txt now exists on disk. Reading it back:")
file = open("attendees.txt", "r")
print(file.read())
file.close()
```

After this script finishes and the program closes completely, a real file named `attendees.txt` now exists on disk, holding those three lines. Open the same folder tomorrow, next week, or on a different day entirely, and the file, and everything written into it, is still there.

## Reading It Back, Even After Restarting

```text file=attendees.txt
A101
A102
A103
```

```python with=attendees.txt
file = open("attendees.txt", "r")
saved_ids = file.read()
file.close()

print(saved_ids)
```

Run this in a brand new script, days later, and it reads exactly what was saved, because the data never depended on the original program still running. The file itself is now the thing that remembers, not the variable that briefly held the data in memory.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-11-file-handling/01_file_lifecycle_restart.png)


## Memory vs Files at a Glance

| | A Variable | A File |
|---|---|---|
| Where it lives | The computer's memory, while the program runs | The disk, as an actual saved file |
| Survives the program ending? | No | Yes |
| Survives the computer restarting? | No | Yes |
| Needs explicit code to create | Just an assignment | `open()`, written and saved |

## Why This Matters for Almost Every Real Program

Every app you use daily depends on this exact idea. A messaging app remembers your conversations after you close it. A game remembers your saved progress. A spreadsheet remembers your numbers the next time you open it. None of that is magic; it is the same `open()`-and-`write()` idea this lesson previewed, simply applied at a larger scale, often to far more carefully structured files than a single line of text.

## Your Turn: Watch Data Disappear, Then Persist

```python
score = 0
score += 10
print("Current score:", score)
# Close this script entirely, then run it again: score restarts at 0 every time.
```

```python
score = 10

file = open("score.txt", "w")
file.write(str(score))
file.close()

file = open("score.txt", "r")
print("Saved score, read back from disk:", file.read())
file.close()
```

Run the second block, then open `score.txt` in a text editor, or read it back with a separate small script, to confirm it really did survive.

## Conclusion

A variable's value disappears the instant a program finishes running, because memory is temporary, while a file written to disk survives long after, because it is real, persistent storage rather than a value held only while code is executing. Persisting data is the difference between a program that starts fresh every single time and one that genuinely remembers. The rest of this unit builds the full, careful toolkit for reading from and writing to files correctly, starting in the very next lesson with reading a file's contents properly.
