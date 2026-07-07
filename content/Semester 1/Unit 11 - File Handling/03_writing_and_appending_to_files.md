## Introduction

Reading `attendees.txt` solved half of Tara's problem; the other half is that her own script needs to create that file in the first place, and keep adding to it as new wristbands get scanned throughout the day, without erasing everyone who was already logged. Writing turns out to come in two distinct flavours, and mixing them up by accident is one of the easiest ways to lose data you actually meant to keep.

This lesson covers `"w"` mode, which creates a file fresh or completely overwrites an existing one, and `"a"` mode, which adds new content onto the end of whatever is already there.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-11-file-handling/03_write_mode_vs_append_mode.png)

## Write Mode: Create or Overwrite

Opening a file with `"w"` creates it if it does not exist, and, critically, completely empties it first if it does already exist, before anything new is written.

```python
file = open("attendees.txt", "w")
file.write("A101\n")
file.write("A102\n")
file.close()

# Read it back to confirm what got saved
file = open("attendees.txt", "r")
print(file.read())
file.close()
```

After this runs, `attendees.txt` contains exactly two lines, A101 and A102, regardless of whatever it might have held a moment before this script ran. `.write()` does not add a line break for you automatically, which is exactly why each call above ends with an explicit `\n`; without it, every write would simply run into the next on the same line.

## The Danger of Write Mode

```python
# Start with A101 and A102 already saved, like the previous example left them
file = open("attendees.txt", "w")
file.write("A101\nA102\n")
file.close()

file = open("attendees.txt", "w")    # wipes the file immediately, just by opening it!
file.write("A103\n")
file.close()

file = open("attendees.txt", "r")
print(file.read())    # only A103 -- A101 and A102 are gone
file.close()
```

Run this, and the A101 and A102 from the previous example are gone, replaced entirely by a file containing only A103. This is not a bug; it is exactly what `"w"` mode promises to do, and it is precisely why choosing the right mode matters before you write a single line. If Tara's goal was to add A103 to the existing list, `"w"` mode was the wrong tool entirely.

## Append Mode: Add Without Erasing

Opening a file with `"a"` also creates it if it does not exist, but if it does exist, new writes are added onto the end, with everything already there left completely untouched.

```python
# Start with A101 and A102 already saved
file = open("attendees.txt", "w")
file.write("A101\nA102\n")
file.close()

file = open("attendees.txt", "a")    # append: keeps what is already there
file.write("A104\n")
file.close()

file = open("attendees.txt", "r")
print(file.read())    # A101, A102, and A104
file.close()
```

Now `attendees.txt` holds A101, A102, and A104, because append mode preserved what was already saved and simply added one more line after it. This is exactly the behaviour Tara needs for a wristband log that keeps growing throughout the day, one scan at a time, across however many times the script runs.

## write() vs writelines()

`.write()` takes one string at a time. `.writelines()` takes a list of strings and writes them all in sequence, though, like `.write()`, it adds no line breaks of its own.

```python
new_scans = ["A105\n", "A106\n", "A107\n"]

file = open("scans.txt", "w")
file.writelines(new_scans)
file.close()

file = open("scans.txt", "r")
print(file.read())
file.close()
```

Each string in the list needed its own `\n` already built in, exactly as shown, or the three IDs would land on a single, run-together line.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-11-file-handling/03_file_modes_switchboard.png)


## Write Modes at a Glance

| Mode | If the File Does Not Exist | If the File Already Exists |
|---|---|---|
| `"w"` | Creates a new, empty file | Erases everything, then writes fresh |
| `"a"` | Creates a new, empty file | Keeps existing content, adds new content after it |
| `"r"` | Raises `FileNotFoundError` | Opens for reading only, no writing allowed |

## Your Turn: Build a Growing Log Safely

```python
file = open("fest_log.txt", "w")
file.write("Gate opened at 9 AM\n")
file.close()

file = open("fest_log.txt", "a")
file.write("First wristband scanned at 9:02 AM\n")
file.close()

file = open("fest_log.txt", "a")
file.write("Stall opened at 9:15 AM\n")
file.close()

file = open("fest_log.txt", "r")
print(file.read())
file.close()
```

Notice the very first open uses `"w"`, deliberately, to start the log fresh for a new day, while every entry after it uses `"a"`, deliberately, to add without disturbing what the day has already recorded.

## Conclusion

`"w"` mode creates a file or completely overwrites one that already exists, while `"a"` mode creates a file or safely appends to one that already exists, leaving its prior content untouched; choosing the wrong one is a quiet, common way to lose data you meant to keep. `.write()` writes one string, and `.writelines()` writes a list of them, with neither adding line breaks automatically. Every `open()` for writing still needs a matching `.close()`, exactly as it did for reading, a pairing easy to forget and the entire subject of the very next lesson.
