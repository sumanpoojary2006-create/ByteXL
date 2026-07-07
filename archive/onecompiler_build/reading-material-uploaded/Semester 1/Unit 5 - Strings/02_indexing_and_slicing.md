## Introduction

Meera is filling in some details on her phone and needs only small pieces of text, not whole values. For a friend's initial she wants just the first letter of their name, and to confirm a payment she needs only the last four digits of a long phone number, not the entire thing. She taps to grab the single character she wants, then selects a short run of characters near the end, without retyping anything. That is exactly what a string lets you do once you know that it is an ordered sequence, where every character sits at a known position. Two powerful abilities open up: reaching in to grab a single character, called indexing, and pulling out a whole run of characters, called slicing, and they follow rules you have already half-met with `range()`. Without that known position for every character, there would be no way to say "give me the first letter" or "give me the last four digits" at all; you would be stuck describing pieces of text in words instead of grabbing them directly.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-5-strings/02_indexing_slicing_beads.png)

## Indexing: Reaching One Character

Each character has a position number called its index, and counting starts at 0, not 1. So in "Python", P is at index 0, y is at index 1, and so on. You reach a character with square brackets.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-5-strings-02-indexing-and-slicing-001-bce2899d90.html"
 width="100%"
></iframe>

Python also allows negative indices, which count from the end. The last character is at index -1, the second to last at -2, and so on. This is wonderfully handy when you want the end of a string without first measuring its length.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-5-strings-02-indexing-and-slicing-002-463a2fb1a6.html"
 width="100%"
></iframe>

A natural question: what happens if you ask for a position that does not exist, like `word[10]` on a six-letter word? Python stops with an `IndexError`, telling you the index is out of range. The valid indices run from 0 up to the length minus one. Negative indexing is exactly the shortcut Meera reaches for when she wants the last four digits of a phone number without first working out how long the whole string is.

## Slicing: Grabbing a Range

Indexing gives one character; slicing gives a piece. You write a start and a stop position separated by a colon, and Python returns the characters from start up to, but not including, stop. If that "not including the stop" rule feels familiar, it is the very same rule as `range()`.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-5-strings-02-indexing-and-slicing-003-3e1318bb27.html"
 width="100%"
></iframe>

You can leave out the start to mean "from the beginning", or the stop to mean "to the end".

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-5-strings-02-indexing-and-slicing-004-ec4a612084.html"
 width="100%"
></iframe>

There is even a third number, the step, just like `range()`. A step of 2 takes every second character, and a clever step of -1 reverses the whole string.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-5-strings-02-indexing-and-slicing-005-725f895d4f.html"
 width="100%"
></iframe>

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-5-strings/02_negative_index_slice_bounds.png)


## Back to Meera's Phone Number

That negative-index trick from earlier is exactly how Meera grabs the last four digits of a payment confirmation, without ever measuring how long the full number is first.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-5-strings-02-indexing-and-slicing-006-c4dfcdd444.html"
 width="100%"
></iframe>

`[-4:]` reads as "start four characters from the end, and go all the way to the end", which works no matter how long the number actually is, ten digits or twelve, because it always counts backward from the last character rather than from a fixed position.

## Indexing and Slicing at a Glance

| Operation | Syntax | Result |
|---|---|---|
| Single character | `word[0]` | The character at index 0 |
| From the end | `word[-1]` | The last character |
| A range | `word[2:5]` | Characters at index 2, 3, 4 (stop excluded) |
| From the start | `word[:3]` | Everything before index 3 |
| To the end | `word[3:]` | Everything from index 3 onward |
| With a step | `word[::2]` | Every second character |
| Reversed | `word[::-1]` | The whole string, back to front |

## Your Turn: First, Last, and Reversed

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-5-strings-02-indexing-and-slicing-007-339cb1a244.html"
 width="100%"
></iframe>

Type your name and watch it pick out the first and last letters and spell the whole thing backwards. The reverse trick, `[::-1]`, is a small piece of Python magic worth remembering.

## Conclusion

Indexing reaches a single character by its position using square brackets, counting from 0 at the front or from -1 at the back, and asking for a position that does not exist raises an `IndexError`. Slicing pulls out a range with `start:stop`, excluding the stop just as `range()` does, and an optional step lets you skip characters or reverse the string with `[::-1]`. Together, indexing and slicing let you reach into any part of a string with precision. So far you have only ever read from a string this way; the next lesson explains why trying to write back into one of these positions does not work the way you might expect.
