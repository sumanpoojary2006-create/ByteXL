## Introduction

Meera is collecting email addresses from customers who want order updates, and one of them just typed "asha gmail.com" with no at sign anywhere in it. She scans down her list checking each one for the at sign, noting where it sits when it is there, and while she is at it she searches a caption for a particular word and counts how many times a hashtag shows up. Working with text constantly means asking questions like this. Does this email contain an at sign? Where does the area code end in this phone number? How many times does a word appear in a caption? Does this filename end in ".jpg"? Python gives you a small, friendly set of tools for searching inside strings, and they turn these everyday questions into single, readable lines. Splitting and joining, from the last lesson, would be a clumsy way to answer "is the at sign in here somewhere"; searching directly is the far more natural fit.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-5-strings/06_searching_magnifier.png)

## Does It Contain? The in Operator

The simplest search asks only yes or no: is this piece of text somewhere inside that one? The `in` operator answers with a boolean.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3NlYXJjaGluZ193aXRoaW5fc3RyaW5ncyBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoiZW1haWwgPSBcImFzaGFAZW1haWwuY29tXCJcbnByaW50KFwiQFwiIGluIGVtYWlsKSAgICAgICAgIyBUcnVlXG5wcmludChcInh5elwiIGluIGVtYWlsKSAgICAgICMgRmFsc2UifQ"
 width="100%"
></iframe>

This is perfect inside an `if`, for example to do a rough check that an email at least contains an at sign before accepting it.

## Where Is It? The find Method

When you need the exact position rather than just yes or no, `find` returns the index where a piece of text first appears, or -1 if it is not there at all.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3NlYXJjaGluZ193aXRoaW5fc3RyaW5ncyBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoiZW1haWwgPSBcImFzaGFAZW1haWwuY29tXCJcbnByaW50KGVtYWlsLmZpbmQoXCJAXCIpKSAgICAgIyA0XG5wcmludChlbWFpbC5maW5kKFwielwiKSkgICAgICMgLTEifQ"
 width="100%"
></iframe>

There is a close cousin called `index` that does the same thing, with one difference worth knowing: if the text is missing, `index` raises an error instead of returning -1. So when the thing you are searching for might genuinely be absent, prefer `find`, because checking for -1 is gentler than handling a crash. This is precisely the kind of check Meera was running by eye on "asha gmail.com", scanning for an at sign that simply was not there.

## How Many Times? The count Method

The `count` method tells you how many times a piece of text appears.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3NlYXJjaGluZ193aXRoaW5fc3RyaW5ncyBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoic2VudGVuY2UgPSBcInNoZSBzZWxscyBzZWEgc2hlbGxzXCJcbnByaW50KHNlbnRlbmNlLmNvdW50KFwic1wiKSkgICAgIyA2In0"
 width="100%"
></iframe>

## Starts and Ends With

Two more methods check the edges of a string, returning a boolean. They are ideal for prefixes and file extensions.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3NlYXJjaGluZ193aXRoaW5fc3RyaW5ncyBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoiZmlsZW5hbWUgPSBcInJlcG9ydC5wZGZcIlxucHJpbnQoZmlsZW5hbWUuZW5kc3dpdGgoXCIucGRmXCIpKSAgICAjIFRydWVcbnByaW50KGZpbGVuYW1lLnN0YXJ0c3dpdGgoXCJyZXBcIikpICAgIyBUcnVlIn0"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3NlYXJjaGluZ193aXRoaW5fc3RyaW5ncyBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoiZW1haWwgPSBpbnB1dChcIkVudGVyIGFuIGVtYWlsOiBcIilcbmlmIFwiQFwiIGluIGVtYWlsIGFuZCBlbWFpbC5lbmRzd2l0aChcIi5jb21cIik6XG4gICAgcHJpbnQoXCJMb29rcyBsaWtlIGEgdmFsaWQgZW1haWwuXCIpXG5lbHNlOlxuICAgIHByaW50KFwiVGhhdCBkb2VzIG5vdCBsb29rIHJpZ2h0LlwiKSJ9"
 width="100%"
></iframe>

Try a proper address and then something missing the at sign. Combining `in` with `endswith` gives a simple sanity check. It is not a perfect validator (you will meet proper pattern matching with regular expressions in a later semester), but it catches the obvious mistakes.

## Conclusion

To search inside strings, use `in` for a quick yes or no, `find` to get a position (or -1 when absent), `count` to tally occurrences, and `startswith` and `endswith` to test the edges. Remember that searches are case-sensitive, so lower-case the text first when you want to ignore case. These small tools answer the everyday "does it contain, where, and how many" questions that fill real text-processing work. You have now read, transformed, split, joined, and searched text; the next lesson turns to presenting it neatly, the way Meera wants her price list to actually look once it is posted.
