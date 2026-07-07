## Introduction

Last year's fest coordinator left behind a text file, `attendees.txt`, one wristband ID per line, and Tara needs to actually read it into her current script: as one long block of text for a quick look, as a list of separate lines for processing one ID at a time, or one line at a time if the file turns out to be enormous. Each of those is a genuinely different need, and Python gives her three closely related tools, all starting from the same `open()` call.

This lesson covers reading: `open()` to access a file, and `read()`, `readlines()`, and a `for` loop directly over the file, the three ways to actually pull its contents into your program.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-11-file-handling/02_three_ways_to_read_a_file.png)

## The File This Lesson Reads

Before any of this works, `attendees.txt` has to actually exist. Last year's coordinator left it behind, one wristband ID per line, and it sits alongside the script in the editor's file explorer for every example below to open.

```text file=attendees.txt
A101
A102
A103
```

## Opening a File

`open()` takes a filename and a mode, and returns a file object you can then read from.

```python with=attendees.txt
file = open("attendees.txt", "r")
print(file)    # a file object, ready to read from
file.close()
```

The `"r"` means **read mode**, and it is actually the default if you leave the mode out entirely, but writing it explicitly states your intent clearly to anyone reading the code. Opening a file in read mode requires that file to already exist; if `attendees.txt` is not actually present in the same folder as your script, this line raises a `FileNotFoundError`, a pitfall the final lesson of this unit covers properly.

## read(): The Whole File as One String

`.read()` pulls the entire contents of the file into a single string, exactly as it is stored, including the line breaks.

```python with=attendees.txt
file = open("attendees.txt", "r")
contents = file.read()
file.close()

print(contents)
```

`contents` now holds the string `"A101\nA102\nA103\n"`, with `\n` marking each line break, exactly the escape sequence from the strings unit, simply appearing now because it was really there in the saved file all along.

## Always Close What You Open

Notice the `file.close()` line above. Every file you open with `open()` should eventually be closed, which releases the file back to the operating system. Forgetting to close a file, especially one you have written to, can leave changes not fully saved, or leave the file locked against other programs trying to use it. The next lesson in this unit introduces a cleaner way to guarantee this happens automatically, but for now, treat `close()` as a required, paired partner to every `open()`.

## readlines(): A List of Lines

`.readlines()` returns the file's contents as a list, one string per line, with each line's `\n` still attached at the end.

```python with=attendees.txt
file = open("attendees.txt", "r")
lines = file.readlines()
file.close()

print(lines)    # ['A101\n', 'A102\n', 'A103\n']
```

This is exactly the list you met throughout the lists and tuples unit, simply built from a file instead of typed by hand, and every list method and loop pattern you already know works on it directly.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-11-file-handling/02_file_cursor_after_read.png)


## Looping Over a File Directly

You rarely need `.readlines()` just to loop over every line; Python lets you loop straight over an open file object, one line at a time, which is both simpler to write and far more memory-efficient on large files.

```python with=attendees.txt
file = open("attendees.txt", "r")
for line in file:
    print(line.strip())
file.close()
```

Notice `.strip()` on each line, removing that trailing `\n` before printing, the exact whitespace-trimming method from the strings unit, used here for precisely the job it was always good at.

## Reading Tools at a Glance

| Tool | Returns | Best For |
|---|---|---|
| `file.read()` | One single string, the whole file | A quick look at the entire contents |
| `file.readlines()` | A list of strings, one per line | Needing every line available as a list, all at once |
| `for line in file:` | One line at a time, inside a loop | Processing line by line, especially on large files |

## Your Turn: Read and Clean a Saved List

Assume `attendees.txt` exists in the same folder as your script, holding the three lines shown earlier.

```python with=attendees.txt
file = open("attendees.txt", "r")
ids = [line.strip() for line in file]
file.close()

print(ids)               # ['A101', 'A102', 'A103']
print(len(ids))           # 3
```

This combines a list comprehension from the lists and tuples unit directly with a file loop, building a clean list of IDs with no trailing line breaks, in a single readable line.

## Conclusion

`open(filename, "r")` opens a file for reading, and you can pull its contents with `.read()` for one whole string, `.readlines()` for a list of lines, or by looping directly over the open file object for one line at a time, the most memory-efficient option. Every file you open should be paired with a `.close()` once you are done with it. The next lesson turns this around, covering how to create and write new content into a file in the first place.
