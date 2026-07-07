## Introduction

Meera is collecting email addresses from customers who want order updates, and one of them just typed "asha gmail.com" with no at sign anywhere in it. She scans down her list checking each one for the at sign, noting where it sits when it is there, and while she is at it she searches a caption for a particular word and counts how many times a hashtag shows up. Working with text constantly means asking questions like this. Does this email contain an at sign? Where does the area code end in this phone number? How many times does a word appear in a caption? Does this filename end in ".jpg"? Python gives you a small, friendly set of tools for searching inside strings, and they turn these everyday questions into single, readable lines. Splitting and joining, from the last lesson, would be a clumsy way to answer "is the at sign in here somewhere"; searching directly is the far more natural fit.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-5-strings/06_searching_magnifier.png)

## Does It Contain? The in Operator

The simplest search asks only yes or no: is this piece of text somewhere inside that one? The `in` operator answers with a boolean.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-5-strings-06-searching-within-strings-001-a91140a4bb.html"
 width="100%"
></iframe>

This is perfect inside an `if`, for example to do a rough check that an email at least contains an at sign before accepting it.

## Where Is It? The find Method

When you need the exact position rather than just yes or no, `find` returns the index where a piece of text first appears, or -1 if it is not there at all.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-5-strings-06-searching-within-strings-002-fd35c26d05.html"
 width="100%"
></iframe>

There is a close cousin called `index` that does the same thing, with one difference worth knowing: if the text is missing, `index` raises an error instead of returning -1. So when the thing you are searching for might genuinely be absent, prefer `find`, because checking for -1 is gentler than handling a crash. This is precisely the kind of check Meera was running by eye on "asha gmail.com", scanning for an at sign that simply was not there.

## How Many Times? The count Method

The `count` method tells you how many times a piece of text appears.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-5-strings-06-searching-within-strings-003-32122a10db.html"
 width="100%"
></iframe>

## Starts and Ends With

Two more methods check the edges of a string, returning a boolean. They are ideal for prefixes and file extensions.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-5-strings-06-searching-within-strings-004-6278bb4e80.html"
 width="100%"
></iframe>

## A Word on Capital Letters

One thing to remember: searching is case-sensitive, so "S" and "s" are treated as different. If you want a search to ignore case, lower-case the text first, for example `sentence.lower().count("s")`. That small step makes your searches forgiving of how the user typed things.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-5-strings/06_case_sensitive_search.png)


## Searching Methods at a Glance

| Tool | Answers | Returns |
|---|---|---|
| `"x" in text` | Is "x" anywhere in text? | `True` or `False` |
| `text.find("x")` | Where does "x" first appear? | An index, or -1 if absent |
| `text.count("x")` | How many times does "x" appear? | A count |
| `text.startswith("x")` | Does text begin with "x"? | `True` or `False` |
| `text.endswith("x")` | Does text end with "x"? | `True` or `False` |

## Your Turn: A Rough Email Check

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-5-strings-06-searching-within-strings-005-8a311c4bd6.html"
 width="100%"
></iframe>

Try a proper address and then something missing the at sign. Combining `in` with `endswith` gives a simple sanity check. It is not a perfect validator (you will meet proper pattern matching with regular expressions in a later semester), but it catches the obvious mistakes.

## Conclusion

To search inside strings, use `in` for a quick yes or no, `find` to get a position (or -1 when absent), `count` to tally occurrences, and `startswith` and `endswith` to test the edges. Remember that searches are case-sensitive, so lower-case the text first when you want to ignore case. These small tools answer the everyday "does it contain, where, and how many" questions that fill real text-processing work. You have now read, transformed, split, joined, and searched text; the next lesson turns to presenting it neatly, the way Meera wants her price list to actually look once it is posted.
