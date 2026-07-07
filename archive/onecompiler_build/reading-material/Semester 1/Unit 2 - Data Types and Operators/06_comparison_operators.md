## Introduction

A program becomes genuinely useful the moment it can make a decision: pass or fail, in stock or sold out, old enough or not. Every one of those decisions starts with a comparison between two values. Up to now your programs have simply calculated and reported; from here, they start to judge. Comparison operators are how you ask Python a yes or no question, and the answer always comes back as a boolean, `True` or `False`, the type you met a few lessons ago, which is no coincidence: comparisons are the single biggest source of boolean values in any real program.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t82zdka/06_comparison_balance_scale.png)


## Asking Questions That Return True or False

There are six comparison operators, and each one asks a precise question.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2NvbXBhcmlzb25fb3BlcmF0b3JzIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJwcmludCg1ID09IDUpICAgICMgVHJ1ZSAgIGFyZSB0aGV5IGVxdWFsP1xucHJpbnQoNSAhPSAzKSAgICAjIFRydWUgICBhcmUgdGhleSBkaWZmZXJlbnQ_XG5wcmludCg1ID4gMykgICAgICMgVHJ1ZSAgIGlzIHRoZSBsZWZ0IGdyZWF0ZXI_XG5wcmludCg1IDwgMykgICAgICMgRmFsc2UgIGlzIHRoZSBsZWZ0IHNtYWxsZXI_XG5wcmludCg1ID49IDUpICAgICMgVHJ1ZSAgIGdyZWF0ZXIgdGhhbiBvciBlcXVhbD9cbnByaW50KDMgPD0gMikgICAgIyBGYWxzZSAgbGVzcyB0aGFuIG9yIGVxdWFsPyJ9"
 width="100%"
></iframe>

Read each result as the answer to the question in the comment. The program is not calculating a number here, it is reaching a verdict, and that verdict is exactly what a decision later in your code will act upon.

## Comparison Operators at a Glance

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater than or equal to | `5 >= 5` | `True` |
| `<=` | Less than or equal to | `3 <= 2` | `False` |

## One Equals Sign Versus Two

Here is a mistake so common it deserves its own warning. A single equals sign assigns a value, while a double equals sign compares two values. They look almost the same and mean completely different things.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2NvbXBhcmlzb25fb3BlcmF0b3JzIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJzY29yZSA9IDkwICAgICAgIyBhc3NpZ25tZW50OiBzdG9yZSA5MCBpbiBzY29yZVxuc2NvcmUgPT0gOTAgICAgICMgY29tcGFyaXNvbjogaXMgc2NvcmUgZXF1YWwgdG8gOTA_IChUcnVlKSJ9"
 width="100%"
></iframe>

So what happens if you accidentally write `if score = 90` when you meant to compare? Python stops with an error, which is actually a kindness, because it points you straight at the slip. In some other languages this exact mistake is allowed to run, quietly turning a comparison into an assignment and producing a bug that can take hours to track down. Python refuses to let that happen by design. Whenever you are testing whether two things are equal, you want two equals signs.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t82zdka/06_assignment_vs_equality.png)


## Comparisons Can Chain

Python allows something many languages do not: comparisons can be chained to read just like mathematics.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2NvbXBhcmlzb25fb3BlcmF0b3JzIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJtYXJrcyA9IDcyXG5wcmludCgwIDw9IG1hcmtzIDw9IDEwMCkgICAjIFRydWU6IG1hcmtzIGlzIGJldHdlZW4gMCBhbmQgMTAwIn0"
 width="100%"
></iframe>

That single line checks two things at once, that marks is at least 0 and at most 100. It reads naturally and saves you from writing a longer, clumsier condition. You can compare numbers, strings (which compare alphabetically), and more.

## Your Turn: Eligibility Check

This program compares an entered age against a threshold and reports the boolean result.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2NvbXBhcmlzb25fb3BlcmF0b3JzIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJhZ2UgPSBpbnQoaW5wdXQoXCJZb3VyIGFnZTogXCIpKVxucHJpbnQoXCJFbGlnaWJsZSB0byB2b3RlP1wiLCBhZ2UgPj0gMTgpIn0"
 width="100%"
></iframe>

Try 16 and then 18. The exact boundary matters here: because the operator is "greater than or equal to", an age of exactly 18 returns `True`. Choosing between `>` and `>=` is a real decision, and getting the boundary right is the kind of detail that separates a correct program from a buggy one. A voting rule that quietly used `>` instead of `>=` would wrongly turn away every single person on the day they turn eighteen, which is precisely the kind of off-by-one mistake that boundary cases are designed to catch before real users ever feel its effect.

## Conclusion

Comparison operators ask questions and return booleans: `==` and `!=` for equality, and `<`, `>`, `<=`, `>=` for ordering. Keep the single equals sign for storing values and the double equals sign for comparing them, and remember that Python lets you chain comparisons to express a range cleanly. These small questions are the seeds of every decision your programs will ever make.
