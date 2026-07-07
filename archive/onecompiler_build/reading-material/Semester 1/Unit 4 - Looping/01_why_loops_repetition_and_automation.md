## Introduction

Kabir, the class representative, needs to send the same fest reminder to everyone in his class. He starts thumb-typing it out and sending it one person at a time: first classmate, second, third. Then he remembers there are sixty of them, and his thumb already aches just thinking about it. Sending it by hand worked fine for three friends, but sixty identical messages, one after another, is a different problem entirely.

Computers face this same moment constantly, except they never get bored or tired, which makes them extraordinary at one particular thing: doing the same task over and over, quickly and without mistakes. That ability is called repetition, and the tool that unlocks it is the **loop**. Loops are what turn a program from something that does one thing once into something that can process a thousand students, send a hundred messages, or keep a game running until you decide to quit. Where the previous unit taught your programs to choose a path, this one teaches them to walk that path as many times as the job actually needs.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44tb5j2kk/01_why_loops_by_hand_vs_loop.png)

## The Copy-Paste Problem

Suppose you want to print the numbers 1 to 5. Without loops, you might write:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3doeV9sb29wc19yZXBldGl0aW9uX2FuZF9hdXRvbWF0aW9uIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJwcmludCgxKVxucHJpbnQoMilcbnByaW50KDMpXG5wcmludCg0KVxucHJpbnQoNSkifQ"
 width="100%"
></iframe>

Five lines, tedious but manageable. Now here is the question that reveals why loops exist: what if you needed 1 to 1000? Copying that line a thousand times is absurd, and a single typo would hide among the rest, the exact problem with Kabir's thumb-typed reminders, except his copies are messages, not lines of code. There has to be a better way, and there is.

## A Loop Does the Repeating for You

A loop lets you write the repeated action once and tell Python how often to do it.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3doeV9sb29wc19yZXBldGl0aW9uX2FuZF9hdXRvbWF0aW9uIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJmb3IgbnVtYmVyIGluIHJhbmdlKDEsIDYpOlxuICAgIHByaW50KG51bWJlcikifQ"
 width="100%"
></iframe>

Those two lines print 1, 2, 3, 4, 5, and changing the 6 to 1001 would print all thousand numbers without a single extra line. The loop carries the burden of repetition so you do not have to. You will learn exactly how this works in the next lessons; for now, simply feel the leap in power.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44tb5j2kk/01_loop_body_repeats.png)


## Two Kinds of Repetition

Almost every loop falls into one of two situations, and Python has a tool for each.

Sometimes you know in advance how many times to repeat, or you want to go through every item in a collection: print each of 30 students, or step through the numbers 1 to 100. This is the job of the `for` loop.

Other times you do not know the count ahead of time, and you simply want to keep going until something changes: keep asking for a password until it is correct, or keep playing until the user quits. This is the job of the `while` loop.

## for vs while at a Glance

| Situation | Tool | Example |
|---|---|---|
| You know the count in advance, or want every item in a group | `for` loop | Print each of 30 students |
| You do not know the count, and must repeat until something changes | `while` loop | Keep asking for a password until correct |

Knowing which situation you are in tells you which loop to reach for, a choice you will make comfortably by the end of this unit.

## Your Turn: Spot the Right Tool

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3doeV9sb29wc19yZXBldGl0aW9uX2FuZF9hdXRvbWF0aW9uIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiIjIFNpdHVhdGlvbiBBOiBwcmludCBhIFwiSGFwcHkgQmlydGhkYXlcIiBtZXNzYWdlIGZvciBlYWNoIG9mIDI1IGNsYXNzbWF0ZXMuXG4jIFNpdHVhdGlvbiBCOiBrZWVwIHJvbGxpbmcgYSBkaWNlIHVudGlsIGl0IGxhbmRzIG9uIDYuXG4jIFNpdHVhdGlvbiBDOiBwcmludCBldmVyeSBudW1iZXIgZnJvbSAxIHRvIDUwLlxuIyBTaXR1YXRpb24gRDoga2VlcCBhc2tpbmcgYSB1c2VyIHRvIGNob29zZSBhbiBvcHRpb24gdW50aWwgdGhleSBwaWNrIGEgdmFsaWQgb25lLiJ9"
 width="100%"
></iframe>

For each situation, decide out loud whether it is a `for` loop or a `while` loop, using the table above as your guide, before any of these are actually written in code over the next few lessons. (A) and (C) know their count in advance, so both are `for` loops; (B) and (D) repeat until something changes with no fixed count, so both are `while` loops.

## Conclusion

Loops exist because computers are brilliant at repetition and humans are not. Instead of copying an instruction many times, you write it once and let the loop repeat it, whether five times or five million. Repetition comes in two flavours: repeating a known number of times or for every item, which suits a `for` loop, and repeating until a condition changes, which suits a `while` loop. With loops, your programs stop doing one thing once and start automating real work. Kabir's first real loop, fittingly, is the one with no known count at all: retrying a wifi password until it finally connects.
