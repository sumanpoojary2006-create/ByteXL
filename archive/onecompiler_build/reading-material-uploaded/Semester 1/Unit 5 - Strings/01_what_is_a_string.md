## Introduction

Meera is setting up a username for her new handmade-craft page, typing it into the box on her phone one letter at a time while a little character counter ticks upward beside it. A friend watching asks what the app is actually storing as she types. Meera explains that every letter, every space, even a dot or an underscore, is just one piece of a single ordered string of text, the same kind of thing a computer stores for names, messages, captions, and passwords. You have already met strings in passing, storing a name or printing a greeting, but now it is time to understand what a string really is. So much of real programming, from web pages to chat apps to the posts on your phone, is really just the careful handling of text. That little character counter ticking beside Meera's username box is not doing anything mysterious; it is simply watching the string grow, one character at a time, and reporting its length back to her.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-5-strings/01_string_beads.png)

## Text Lives Between Quotes

A string is any sequence of characters wrapped in quotation marks. Python accepts single or double quotes, and the two are interchangeable as long as you are consistent.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-5-strings-01-what-is-a-string-001-2c78cc85d6.html"
 width="100%"
></iframe>

So when would you choose one over the other? The handy trick is to use whichever quote your text does not contain. If your string has an apostrophe, wrap it in double quotes; if it contains double quotes, wrap it in single quotes:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-5-strings-01-what-is-a-string-002-4ba9a3660b.html"
 width="100%"
></iframe>

This way the quote inside the text does not get confused with the quotes that mark where the string begins and ends.

## A String Is an Ordered Sequence

The most important idea in this whole unit is that a string is not one solid blob. It is an ordered sequence of individual characters, each sitting in its own position, one after another. The word "Python" is really P, then y, then t, then h, then o, then n, lined up in order.

Because of that order, you can do sequence-like things with strings, as you saw in the looping unit when you walked through a word letter by letter. You can also ask how long a string is using `len()`:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-5-strings-01-what-is-a-string-003-bcf9f1fd73.html"
 width="100%"
></iframe>

That ordered structure is what makes everything in the coming lessons possible: reaching a single character, slicing out a piece, searching, and transforming. Without that order, there would be no sensible way to talk about the "first letter" of Meera's username at all, because the characters would just be a loose pile rather than a sequence with a definite beginning and end.

## The Empty String

One special case is worth meeting now: a string with nothing in it, written as two quotes with nothing between them. Its length is zero.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-5-strings-01-what-is-a-string-004-dd87f9dfdf.html"
 width="100%"
></iframe>

You saw earlier that an empty string is falsy, which is exactly why `if name:` is a neat way to check whether the user actually typed something. The empty string is the natural "nothing here yet" starting point for text.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-5-strings/01_quotes_empty_string.png)


## Strings at a Glance

| Idea | What It Means | Example |
|---|---|---|
| Quotes | Either `'single'` or `"double"`, as long as you are consistent | `name = "Asha"` |
| Ordered sequence | Each character sits in its own fixed position | `"Python"` is P, y, t, h, o, n in order |
| Length | `len()` counts every character, including spaces | `len("Python")` is 6 |
| Empty string | Two quotes with nothing between them, length zero, and falsy | `blank = ""` |

## Your Turn: Measure a Name

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-5-strings-01-what-is-a-string-005-c6a7628770.html"
 width="100%"
></iframe>

Type your name and see its length. Notice that spaces count as characters too, because to a string a space is just another character in the sequence, sitting in its own position like all the rest.

## Conclusion

A string is Python's type for text: an ordered sequence of characters wrapped in single or double quotes. Choose the quote style that avoids clashing with quotes inside your text, remember that every character including spaces has its own position, and use `len()` to measure the length. Seeing a string as an ordered sequence, rather than one solid lump, is the key that unlocks indexing, slicing, searching, and all the text-handling power that follows. The very next lesson puts that order to direct use, reaching into a string to pull out exactly the character or piece you want.
