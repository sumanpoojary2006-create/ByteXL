## Introduction

Tara's script works perfectly on her own laptop, then crashes the instant a teammate runs it on theirs: a file that was supposed to be there simply is not, because they cloned the project folder but never received the data files Tara kept locally. Months later, a different crash appears, this time from a file that does exist, but contains a rupee symbol her script cannot quite read correctly, displaying as a strange, mangled character instead.

These are two of the most common real-world file problems: a **missing file**, and a **mismatched encoding**. Neither is exotic, and both are worth recognising on sight, because nearly every program that touches files eventually runs into one or the other.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-11-file-handling/09_missing_file_and_encoding_pitfalls.png)

## The Missing File Problem

Opening a file that does not exist, in read mode, raises a `FileNotFoundError` immediately.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-11-file-handling-09-common-file-pitfalls-encoding-and-missing-001-dae961ed0a.html"
 width="100%"
></iframe>

This is correct, expected behaviour, Python refusing to pretend a file exists when it does not, but a script that does not anticipate this possibility simply stops, with no graceful explanation offered to whoever is running it.

## Checking Before You Open

Without yet using the more powerful tool the very next unit introduces, you can guard against this with a simple existence check, exactly the `Path.exists()` method from earlier in this unit.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-11-file-handling-09-common-file-pitfalls-encoding-and-missing-002-349206489e.html"
 width="100%"
></iframe>

This is the same guard-clause instinct from the control flow unit, checking a condition before attempting something that could fail, rather than attempting it blindly and hoping. It is not the final word on handling this kind of failure, exception handling, the very next unit in this course, gives you a more general and more powerful tool for exactly this, but it is enough to keep a script from crashing outright on a file that simply has not been created yet.

## The Encoding Problem

Text files are not stored as the letters you see; they are stored as numbers, following an agreed-upon scheme called an **encoding**, that maps numbers back to characters. `UTF-8` is the overwhelmingly common, modern standard, and it correctly handles virtually every character from virtually every language, including symbols like the rupee sign, ₹. Older or different encodings do not always agree on what a given number means, and opening a file with the wrong assumption produces exactly the mangled, wrong-looking text Tara ran into.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-11-file-handling-09-common-file-pitfalls-encoding-and-missing-003-8e5be8837e.html"
 width="100%"
></iframe>

Specifying `encoding="utf-8"` explicitly, on both the write and the read, guarantees both sides agree on exactly how those characters are stored and interpreted. Leaving `encoding` out entirely lets Python fall back to a system-dependent default, which is not always UTF-8, and is exactly the gap that let a correctly written rupee sign turn into a mangled character on a different machine.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-11-file-handling/09_exists_encoding_defense.png)


## A Habit Worth Adopting Now

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-11-file-handling-09-common-file-pitfalls-encoding-and-missing-004-599cb105af.html"
 width="100%"
></iframe>

Make `encoding="utf-8"` part of how you open files by default, the same way you have made `with` part of how you open them at all. It costs nothing on the files that would have worked anyway, and it quietly prevents the exact mismatch that broke Tara's receipt.

## File Pitfalls at a Glance

| Pitfall | Symptom | Defence |
|---|---|---|
| Missing file | `FileNotFoundError` the moment you try to open it for reading | Check `Path.exists()` first, or handle it properly with tools from the next unit |
| Wrong or missing encoding | Mangled or incorrect characters, especially beyond plain English letters | Always specify `encoding="utf-8"` explicitly, on both reads and writes |

## Your Turn: Defend a Read

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-11-file-handling-09-common-file-pitfalls-encoding-and-missing-005-98b5edaf51.html"
 width="100%"
></iframe>

The same function handles both a real file and a missing one gracefully, returning a sensible message instead of letting the whole script crash, by checking first rather than assuming.

## Conclusion

A missing file raises `FileNotFoundError` the instant you try to open it for reading, and checking with `Path.exists()` first is a simple, immediate defence, though the next unit's exception handling gives you a more complete tool for the same problem. Mismatched encodings produce mangled or incorrect text, and explicitly specifying `encoding="utf-8"` on every file you open removes the ambiguity that causes it. Across this entire unit, you have learned to read, write, append, safely close, path correctly, pattern-match filenames, and structure your data as CSV or JSON; recognising these two pitfalls is what keeps all of that working reliably once your code leaves your own laptop and meets the real world's messier files.
