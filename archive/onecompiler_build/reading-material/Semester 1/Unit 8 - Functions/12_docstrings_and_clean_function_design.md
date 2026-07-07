## Introduction

Naveen is finally handing his collection of scripts over to next year's committee, and he opens `split_cost` for the first time in months to check it still does what he remembers. The parameters are named `a`, `b`, and `c`. There is no note anywhere explaining what they mean, whether `c` is a percentage or a flat amount, or what the function actually hands back. He wrote this code, and even he has to guess.

This final lesson of the unit is not about a new piece of syntax. It is about the habits that turn a function from something that merely works into something a stranger, or you in six months, can trust and use without re-reading every line.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/12_docstring_explains_the_function.png)

## The Docstring: Documentation Built Into the Function

A **docstring** is a string, almost always triple-quoted, placed as the very first line inside a function's body, describing what the function does.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjEyX2RvY3N0cmluZ3NfYW5kX2NsZWFuX2Z1bmN0aW9uX2Rlc2lnbiBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoiZGVmIHNwbGl0X2Nvc3QodG90YWwsIHBlb3BsZSwgc2VydmljZV9jaGFyZ2U9MCk6XG4gICAgXCJcIlwiU3BsaXQgYSB0b3RhbCBjb3N0IGV2ZW5seSBhbW9uZyBwZW9wbGUsIHdpdGggYW4gb3B0aW9uYWwgc2VydmljZSBjaGFyZ2UuXCJcIlwiXG4gICAgcmV0dXJuICh0b3RhbCArIHNlcnZpY2VfY2hhcmdlKSAvIHBlb3BsZSJ9"
 width="100%"
></iframe>

Unlike an ordinary comment, a docstring is a real, accessible part of the function. Python attaches it to the function itself, retrievable with the built-in `help()`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjEyX2RvY3N0cmluZ3NfYW5kX2NsZWFuX2Z1bmN0aW9uX2Rlc2lnbiBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoiaGVscChzcGxpdF9jb3N0KSJ9"
 width="100%"
></iframe>

This prints the function's signature alongside the docstring, the exact information Naveen needed and did not have. A good editor or IDE will also show this docstring automatically the moment someone starts typing a call to the function, which is precisely why it is worth writing well.

## What a Good Docstring Covers

For a simple function, one clear sentence describing what it does and what it returns is often enough, exactly like the `split_cost` example above. For anything less obvious, a slightly longer docstring naming each parameter helps far more than a clever one-liner.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjEyX2RvY3N0cmluZ3NfYW5kX2NsZWFuX2Z1bmN0aW9uX2Rlc2lnbiBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoiZGVmIHRpY2tldF9wcmljZShiYXNlX3ByaWNlLCBkaXNjb3VudD0wKTpcbiAgICBcIlwiXCJDYWxjdWxhdGUgYSB0aWNrZXQncyBmaW5hbCBwcmljZS5cblxuICAgIGJhc2VfcHJpY2U6IHRoZSBwcmljZSBiZWZvcmUgYW55IGRpc2NvdW50LlxuICAgIGRpc2NvdW50OiBhbiBhbW91bnQgdG8gc3VidHJhY3QsIGRlZmF1bHRpbmcgdG8gMC5cbiAgICBSZXR1cm5zIHRoZSBmaW5hbCBwcmljZSBhZnRlciB0aGUgZGlzY291bnQgaXMgYXBwbGllZC5cbiAgICBcIlwiXCJcbiAgICByZXR1cm4gYmFzZV9wcmljZSAtIGRpc2NvdW50In0"
 width="100%"
></iframe>

The goal is always the same question, answered without making the reader trace through the function's body: what does this need, and what do I get back?

## Naming: The Cheapest Documentation There Is

Before a docstring is even read, a function's own name and parameter names are already documenting it, for free. Compare these two identical functions.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjEyX2RvY3N0cmluZ3NfYW5kX2NsZWFuX2Z1bmN0aW9uX2Rlc2lnbiBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoiZGVmIGYoYSwgYiwgYyk6XG4gICAgcmV0dXJuIChhICsgYykgLyBiXG5cbmRlZiBzcGxpdF9jb3N0KHRvdGFsLCBwZW9wbGUsIHNlcnZpY2VfY2hhcmdlPTApOlxuICAgIHJldHVybiAodG90YWwgKyBzZXJ2aWNlX2NoYXJnZSkgLyBwZW9wbGUifQ"
 width="100%"
></iframe>

Both compute exactly the same thing. Only one of them tells you what it computes without a single extra word of explanation. Naveen's `a`, `b`, `c` function from the introduction is exactly this trap: working code that nobody, including its own author, can trust on sight.

## One Function, One Job

A function that does one clearly nameable thing is easier to test, easier to reuse, and easier to trust than a function that quietly does three things at once. If you find yourself struggling to summarise a function in one short sentence for its docstring, that struggle is often a sign the function is trying to do too much, and would read more clearly split into two.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjEyX2RvY3N0cmluZ3NfYW5kX2NsZWFuX2Z1bmN0aW9uX2Rlc2lnbiBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoiZGVmIHByb2Nlc3NfbWVtYmVyKG5hbWUsIGR1ZXMpOlxuICAgIHByaW50KGZcIlByb2Nlc3Npbmcge25hbWV9XCIpXG4gICAgdG90YWwgPSBkdWVzICogMS4wNVxuICAgIHByaW50KGZcIntuYW1lfSBvd2VzIHt0b3RhbH1cIilcbiAgICByZXR1cm4gdG90YWwifQ"
 width="100%"
></iframe>

This function prints a status message, computes a late fee, prints another message, and returns a result, all at once. Splitting it makes each piece nameable and testable on its own.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/12_one_job_function_design.png)


<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjEyX2RvY3N0cmluZ3NfYW5kX2NsZWFuX2Z1bmN0aW9uX2Rlc2lnbiBjb2RlIDYiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDYucHkiLCJjb2RlIjoiZGVmIGFwcGx5X2xhdGVfZmVlKGR1ZXMpOlxuICAgIFwiXCJcIkFwcGx5IGEgZmxhdCA1IHBlcmNlbnQgbGF0ZSBmZWUgdG8gYSBkdWUgYW1vdW50LlwiXCJcIlxuICAgIHJldHVybiBkdWVzICogMS4wNVxuXG5kZWYgcmVwb3J0X2R1ZShuYW1lLCBhbW91bnQpOlxuICAgIFwiXCJcIlByaW50IGEgb25lLWxpbmUgc3RhdHVzIHJlcG9ydCBmb3IgYSBtZW1iZXIncyBkdWUgYW1vdW50LlwiXCJcIlxuICAgIHByaW50KGZcIntuYW1lfSBvd2VzIHthbW91bnR9XCIpIn0"
 width="100%"
></iframe>

## Clean Function Design at a Glance

| Habit | Why It Matters |
|---|---|
| A clear docstring as the first line | Lets `help()` and editors explain the function instantly |
| Descriptive parameter and function names | Documents intent before anyone reads the body |
| One function, one clearly nameable job | Easier to test, trust, reuse, and explain in one sentence |
| Defaults for the genuinely optional details | Keeps the common call simple, the rare call still possible |

## Your Turn: Document Your Own Function

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjEyX2RvY3N0cmluZ3NfYW5kX2NsZWFuX2Z1bmN0aW9uX2Rlc2lnbiBjb2RlIDciLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDcucHkiLCJjb2RlIjoiZGVmIGNhbGN1bGF0ZV9zaGFyZSh0b3RhbCwgcGVvcGxlLCBzZXJ2aWNlX2NoYXJnZT0wKTpcbiAgICBcIlwiXCJDYWxjdWxhdGUgZWFjaCBwZXJzb24ncyBzaGFyZSBvZiBhIHRvdGFsIGNvc3QuXG5cbiAgICB0b3RhbDogdGhlIGFtb3VudCB0byBiZSBzcGxpdC5cbiAgICBwZW9wbGU6IGhvdyBtYW55IHBlb3BsZSBhcmUgc3BsaXR0aW5nIGl0LlxuICAgIHNlcnZpY2VfY2hhcmdlOiBhbiBvcHRpb25hbCBmbGF0IGFtb3VudCBhZGRlZCBiZWZvcmUgc3BsaXR0aW5nLlxuICAgIFJldHVybnMgZWFjaCBwZXJzb24ncyBzaGFyZSBhcyBhIGZsb2F0LlxuICAgIFwiXCJcIlxuICAgIHJldHVybiAodG90YWwgKyBzZXJ2aWNlX2NoYXJnZSkgLyBwZW9wbGVcblxucHJpbnQoY2FsY3VsYXRlX3NoYXJlKDEyMDAsIDQpKVxuaGVscChjYWxjdWxhdGVfc2hhcmUpIn0"
 width="100%"
></iframe>

Run both lines and compare what `help()` shows you against the docstring you wrote, confirming they say exactly the same thing, because they are, in fact, the same text.

## Conclusion

A docstring, written as the first line inside a function's body, documents what a function does in a way `help()` and editors can surface automatically, and clear names for the function and its parameters document intent before anyone even reads that docstring. A function that does one clearly nameable job is easier to trust, reuse, and explain than one that quietly does several things at once. Across this entire unit, you have learned to define, call, parameterise, default, gather, shorten, transform, scope, and recurse with functions; writing them clearly, the way this final lesson asked, is what makes every one of those tools actually pay off in code other people, including future you, can rely on.
