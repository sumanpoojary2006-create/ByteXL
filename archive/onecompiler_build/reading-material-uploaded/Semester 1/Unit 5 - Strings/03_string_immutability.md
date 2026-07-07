## Introduction

Meera spots a typo in the username she just locked in for her page: the first letter should be an "M", not an "N". She taps right on that one wrong letter to fix it, but the field will not let her change a single character in place. In the end she clears the whole thing and types a fresh, corrected username from scratch, leaving the original untouched until she replaces it. That little surprise is a fact about strings that catches almost every beginner, and explains a whole family of confusing errors: a string cannot be changed once it is created. You can read any part of it, slice it, and inspect it freely, but you cannot reach in and alter a character in place. Programmers call this property immutability, and understanding it now will save you real frustration later. Indexing and slicing from the last lesson only ever let you look, never touch, and that one-way nature was a quiet hint of what this lesson now makes explicit.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-5-strings/03_immutability_locked.png)

## You Cannot Edit a Character in Place

It feels natural to think you could fix a typo by replacing a single character directly. Let us try.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-5-strings-03-string-immutability-001-dafa7373a6.html"
 width="100%"
></iframe>

Python refuses with a `TypeError`, saying that strings do not support item assignment. The string "Python" is fixed; there is no way to poke a new letter into position 0. So if strings cannot be changed, how do we ever transform text? The answer reframes the whole idea.

## Changing Means Building Something New

You do not change a string. You build a new string from the old one and, usually, point your variable at the new result. Slicing and joining make this easy.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-5-strings-03-string-immutability-002-be37d0baa3.html"
 width="100%"
></iframe>

Here `word[1:]` slices out "ython", and joining "J" in front creates a brand new string "Jython", which we then store back in `word`. The original "Python" was never edited; it was replaced. Every string method you will meet works this way: it returns a new string and leaves the original untouched.

## Why Would a Language Do This?

It might sound like a limitation, but immutability is a deliberate, helpful choice. Because a string can never change underneath you, it is safe to share and reason about. If you pass a string to one part of your program, you can trust that no other part will silently alter it. This same property is what allows strings to be used as dictionary keys, which you will appreciate in a later unit. Safety and predictability are worth the small change in how you think. Meera's original username was never silently altered either; it simply stayed exactly as typed until she chose to replace it with something new.

## A Variable Is Not the Same as the String It Holds

It helps to separate two ideas that look identical but are not: the variable `word`, and the actual string object it currently points to. Reassigning `word` does not edit anything; it simply makes the variable point somewhere new, leaving the old string exactly as it was, unreachable but unharmed.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-5-strings-03-string-immutability-003-c1b0316cf1.html"
 width="100%"
></iframe>

`id()` reveals the object's identity in memory, and the two printed numbers are different, confirming that `word` was never edited in place. It was pointed at a completely new string, while the original "Python" simply faded out of reach, exactly as Meera's original username sat untouched until she replaced it with a corrected one.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-5-strings/03_reassign_new_string.png)


## Immutability at a Glance

| What You Might Expect | What Actually Happens |
|---|---|
| `word[0] = "J"` edits the string | Raises `TypeError`, strings cannot be edited in place |
| Fixing a typo changes the original | A brand new string is built and the variable is repointed |
| The original disappears immediately | It stays unchanged in memory until nothing refers to it |
| Immutability is a limitation | It is what makes strings safe to share and use as dictionary keys |

## Your Turn: Capitalise the First Letter

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-5-strings-03-string-immutability-004-aa016d8d2e.html"
 width="100%"
></iframe>

Type "asha" and watch it become "Asha". You did not edit the original string; you built a new one from an upper-cased first letter joined to the rest. That build-a-new-one habit is the heart of working with immutable text.

## Conclusion

Strings are immutable, meaning you cannot change a character in place; attempting `word[0] = "J"` raises an error. To transform text, you build a new string using slicing and joining, or string methods, and store the result, leaving the original untouched. Far from being a nuisance, immutability makes strings safe to share and reason about. Once you expect to create rather than edit, working with text becomes natural. You just built a new string by hand with slicing; the next lesson hands you a whole toolbox of ready-made methods that do this same kind of transformation in a single call.
