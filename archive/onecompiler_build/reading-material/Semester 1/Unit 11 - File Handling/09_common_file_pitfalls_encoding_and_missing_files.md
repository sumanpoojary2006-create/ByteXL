## Introduction

Tara's script works perfectly on her own laptop, then crashes the instant a teammate runs it on theirs: a file that was supposed to be there simply is not, because they cloned the project folder but never received the data files Tara kept locally. Months later, a different crash appears, this time from a file that does exist, but contains a rupee symbol her script cannot quite read correctly, displaying as a strange, mangled character instead.

These are two of the most common real-world file problems: a **missing file**, and a **mismatched encoding**. Neither is exotic, and both are worth recognising on sight, because nearly every program that touches files eventually runs into one or the other.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-11-file-handling/09_missing_file_and_encoding_pitfalls.png)

## The Missing File Problem

Opening a file that does not exist, in read mode, raises a `FileNotFoundError` immediately.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X2NvbW1vbl9maWxlX3BpdGZhbGxzX2VuY29kaW5nX2FuZF9taXNzaW5nX2ZpbGVzIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJ3aXRoIG9wZW4oXCJhdHRlbmRlZXNfZGF5NC50eHRcIiwgXCJyXCIpIGFzIGZpbGU6XG4gICAgcHJpbnQoZmlsZS5yZWFkKCkpICAgICMgZXJyb3IhIHRoaXMgZmlsZSB3YXMgbmV2ZXIgY3JlYXRlZCJ9"
 width="100%"
></iframe>

This is correct, expected behaviour, Python refusing to pretend a file exists when it does not, but a script that does not anticipate this possibility simply stops, with no graceful explanation offered to whoever is running it.

## Checking Before You Open

Without yet using the more powerful tool the very next unit introduces, you can guard against this with a simple existence check, exactly the `Path.exists()` method from earlier in this unit.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X2NvbW1vbl9maWxlX3BpdGZhbGxzX2VuY29kaW5nX2FuZF9taXNzaW5nX2ZpbGVzIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGhcblxubG9nX2ZpbGUgPSBQYXRoKFwiYXR0ZW5kZWVzX2RheTQudHh0XCIpXG5cbmlmIGxvZ19maWxlLmV4aXN0cygpOlxuICAgIHByaW50KGxvZ19maWxlLnJlYWRfdGV4dCgpKVxuZWxzZTpcbiAgICBwcmludChcIk5vIGxvZyBmb3VuZCBmb3IgZGF5IDQgeWV0LlwiKSJ9"
 width="100%"
></iframe>

This is the same guard-clause instinct from the control flow unit, checking a condition before attempting something that could fail, rather than attempting it blindly and hoping. It is not the final word on handling this kind of failure, exception handling, the very next unit in this course, gives you a more general and more powerful tool for exactly this, but it is enough to keep a script from crashing outright on a file that simply has not been created yet.

## The Encoding Problem

Text files are not stored as the letters you see; they are stored as numbers, following an agreed-upon scheme called an **encoding**, that maps numbers back to characters. `UTF-8` is the overwhelmingly common, modern standard, and it correctly handles virtually every character from virtually every language, including symbols like the rupee sign, ₹. Older or different encodings do not always agree on what a given number means, and opening a file with the wrong assumption produces exactly the mangled, wrong-looking text Tara ran into.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X2NvbW1vbl9maWxlX3BpdGZhbGxzX2VuY29kaW5nX2FuZF9taXNzaW5nX2ZpbGVzIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJ3aXRoIG9wZW4oXCJyZWNlaXB0LnR4dFwiLCBcIndcIiwgZW5jb2Rpbmc9XCJ1dGYtOFwiKSBhcyBmaWxlOlxuICAgIGZpbGUud3JpdGUoXCJUb3RhbDog4oK5MTUwMFxcblwiKVxuXG53aXRoIG9wZW4oXCJyZWNlaXB0LnR4dFwiLCBcInJcIiwgZW5jb2Rpbmc9XCJ1dGYtOFwiKSBhcyBmaWxlOlxuICAgIHByaW50KGZpbGUucmVhZCgpKSAgICAjIFRvdGFsOiDigrkxNTAwIn0"
 width="100%"
></iframe>

Specifying `encoding="utf-8"` explicitly, on both the write and the read, guarantees both sides agree on exactly how those characters are stored and interpreted. Leaving `encoding` out entirely lets Python fall back to a system-dependent default, which is not always UTF-8, and is exactly the gap that let a correctly written rupee sign turn into a mangled character on a different machine.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-11-file-handling/09_exists_encoding_defense.png)


## A Habit Worth Adopting Now

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X2NvbW1vbl9maWxlX3BpdGZhbGxzX2VuY29kaW5nX2FuZF9taXNzaW5nX2ZpbGVzIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJ3aXRoIG9wZW4oXCJyZWNlaXB0LnR4dFwiLCBcIndcIiwgZW5jb2Rpbmc9XCJ1dGYtOFwiKSBhcyBmaWxlOlxuICAgIGZpbGUud3JpdGUoXCJUb3RhbDog4oK5MTUwMFxcblwiKSJ9"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X2NvbW1vbl9maWxlX3BpdGZhbGxzX2VuY29kaW5nX2FuZF9taXNzaW5nX2ZpbGVzIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGhcblxuZGVmIHJlYWRfbG9nX3NhZmVseShmaWxlbmFtZSk6XG4gICAgcGF0aCA9IFBhdGgoZmlsZW5hbWUpXG4gICAgaWYgbm90IHBhdGguZXhpc3RzKCk6XG4gICAgICAgIHJldHVybiBcIk5vIGRhdGEgZm91bmQuXCJcbiAgICByZXR1cm4gcGF0aC5yZWFkX3RleHQoZW5jb2Rpbmc9XCJ1dGYtOFwiKVxuXG5wcmludChyZWFkX2xvZ19zYWZlbHkoXCJmZXN0X2xvZy50eHRcIikpXG5wcmludChyZWFkX2xvZ19zYWZlbHkoXCJub25leGlzdGVudF9maWxlLnR4dFwiKSkifQ"
 width="100%"
></iframe>

The same function handles both a real file and a missing one gracefully, returning a sensible message instead of letting the whole script crash, by checking first rather than assuming.

## Conclusion

A missing file raises `FileNotFoundError` the instant you try to open it for reading, and checking with `Path.exists()` first is a simple, immediate defence, though the next unit's exception handling gives you a more complete tool for the same problem. Mismatched encodings produce mangled or incorrect text, and explicitly specifying `encoding="utf-8"` on every file you open removes the ambiguity that causes it. Across this entire unit, you have learned to read, write, append, safely close, path correctly, pattern-match filenames, and structure your data as CSV or JSON; recognising these two pitfalls is what keeps all of that working reliably once your code leaves your own laptop and meets the real world's messier files.
