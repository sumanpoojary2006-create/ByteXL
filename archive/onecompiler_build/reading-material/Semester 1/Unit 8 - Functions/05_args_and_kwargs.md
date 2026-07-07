## Introduction

The trip fund split used to involve four people, reliably, every time, until one trip had five contributors and another had only three. Naveen cannot write a parameter for every possible headcount in advance, and he does not want a separate function for three people, a separate one for four, and another for five. What he actually needs is a function that accepts any number of contributions at all, decided fresh at each call, with no upper limit fixed in the definition.

Python provides exactly this with `*args`, which gathers any number of extra positional arguments into a single tuple, and its cousin `**kwargs`, which gathers any number of extra named arguments into a dictionary.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/05_variable_args_gathering.png)

## *args: Any Number of Positional Arguments

A parameter written with a single star gathers every extra positional argument into a tuple.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2FyZ3NfYW5kX2t3YXJncyBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoiZGVmIHRvdGFsX2NvbnRyaWJ1dGlvbnMoKmFtb3VudHMpOlxuICAgIHJldHVybiBzdW0oYW1vdW50cylcblxucHJpbnQodG90YWxfY29udHJpYnV0aW9ucygzMDAsIDMwMCwgMzAwLCAzMDApKSAgICAgICAgICMgMTIwMFxucHJpbnQodG90YWxfY29udHJpYnV0aW9ucyg1MDAsIDQwMCwgNjAwKSkgICAgICAgICAgICAgICAgIyAxNTAwXG5wcmludCh0b3RhbF9jb250cmlidXRpb25zKDEwMDApKSAgICAgICAgICAgICAgICAgICAgICAgICAgIyAxMDAwIn0"
 width="100%"
></iframe>

The name `amounts` is ordinary; the single star in front of it is what tells Python "collect everything here, however many there are." Inside the function, `amounts` behaves exactly like the tuples you already know from the lists and tuples unit, so `sum(amounts)` works immediately, and so would looping over it with a `for`.

## You Can Still Mix in Ordinary Parameters

`*args` does not have to be the only parameter; it simply has to come after any required, ordinary ones.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2FyZ3NfYW5kX2t3YXJncyBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoiZGVmIGRlc2NyaWJlX3RyaXAoZGVzdGluYXRpb24sICpjb250cmlidXRvcnMpOlxuICAgIHByaW50KGZcIlRyaXAgdG8ge2Rlc3RpbmF0aW9ufSB3aXRoIHtsZW4oY29udHJpYnV0b3JzKX0gY29udHJpYnV0b3JzOlwiKVxuICAgIGZvciBuYW1lIGluIGNvbnRyaWJ1dG9yczpcbiAgICAgICAgcHJpbnQoZlwiICB7bmFtZX1cIilcblxuZGVzY3JpYmVfdHJpcChcIkdvYVwiLCBcIkFzaGFcIiwgXCJSYXZpXCIsIFwiTWVlcmFcIikifQ"
 width="100%"
></iframe>

`destination` takes the first argument as always, and every argument after it, however many there are, gets swept into the `contributors` tuple.

## **kwargs: Any Number of Named Arguments

Two stars in front of a parameter name gather any number of extra keyword arguments into a dictionary instead of a tuple.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2FyZ3NfYW5kX2t3YXJncyBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoiZGVmIGJ1aWxkX3Byb2ZpbGUoKipkZXRhaWxzKTpcbiAgICByZXR1cm4gZGV0YWlsc1xuXG5wcm9maWxlID0gYnVpbGRfcHJvZmlsZShuYW1lPVwiTmF2ZWVuXCIsIHJvbGU9XCJ0cmVhc3VyZXJcIiwgeWVhcj0yKVxucHJpbnQocHJvZmlsZSkgICAgIyB7J25hbWUnOiAnTmF2ZWVuJywgJ3JvbGUnOiAndHJlYXN1cmVyJywgJ3llYXInOiAyfSJ9"
 width="100%"
></iframe>

Each keyword used in the call, `name`, `role`, `year`, becomes a key in the resulting dictionary, with whatever value was supplied. This is exactly the dictionary-from-pairs idea from the sets and dictionaries unit, just built automatically from a function call instead of typed out by hand.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/05_args_kwargs_unpacking.png)


## Why the Names args and kwargs?

The single and double stars are what actually matter to Python; the names `args` and `kwargs` are simply the overwhelmingly common convention, short for "arguments" and "keyword arguments." You could legally write `*numbers` or `**details` instead, and both lessons above already did exactly that, but recognising `*args` and `**kwargs` by sight matters, because you will see this exact convention in almost every Python codebase and library you read from here on.

## Using Both Together

A function can accept ordinary parameters, `*args`, and `**kwargs` all at once, provided they appear in that order: ordinary parameters, then `*args`, then `**kwargs`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2FyZ3NfYW5kX2t3YXJncyBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoiZGVmIHJlZ2lzdGVyKGV2ZW50LCAqYXR0ZW5kZWVzLCAqKmRldGFpbHMpOlxuICAgIHByaW50KGZcIkV2ZW50OiB7ZXZlbnR9XCIpXG4gICAgcHJpbnQoZlwiQXR0ZW5kZWVzOiB7YXR0ZW5kZWVzfVwiKVxuICAgIHByaW50KGZcIkV4dHJhIGRldGFpbHM6IHtkZXRhaWxzfVwiKVxuXG5yZWdpc3RlcihcIkZlc3RcIiwgXCJBc2hhXCIsIFwiUmF2aVwiLCB2ZW51ZT1cIkF1ZGl0b3JpdW1cIiwgZW50cnlfZmVlPTApIn0"
 width="100%"
></iframe>

Output:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2FyZ3NfYW5kX2t3YXJncyBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoiRXZlbnQ6IEZlc3RcbkF0dGVuZGVlczogKCdBc2hhJywgJ1JhdmknKVxuRXh0cmEgZGV0YWlsczogeyd2ZW51ZSc6ICdBdWRpdG9yaXVtJywgJ2VudHJ5X2ZlZSc6IDB9In0"
 width="100%"
></iframe>

Every plain positional argument after `event` falls into `attendees`, and every keyword argument falls into `details`, sorted automatically by how each one was supplied.

## *args and **kwargs at a Glance

| Syntax | Gathers | Type Inside the Function |
|---|---|---|
| `*args` | Any number of extra positional arguments | Tuple |
| `**kwargs` | Any number of extra keyword arguments | Dictionary |
| Order in a definition | Ordinary parameters, then `*args`, then `**kwargs` | n/a |

## Your Turn: A Flexible Total

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2FyZ3NfYW5kX2t3YXJncyBjb2RlIDYiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDYucHkiLCJjb2RlIjoiZGVmIHRyaXBfc3VtbWFyeShkZXN0aW5hdGlvbiwgKmNvbnRyaWJ1dGlvbnMsICoqZXh0cmFfaW5mbyk6XG4gICAgcHJpbnQoZlwiRGVzdGluYXRpb246IHtkZXN0aW5hdGlvbn1cIilcbiAgICBwcmludChmXCJUb3RhbCBjb2xsZWN0ZWQ6IHtzdW0oY29udHJpYnV0aW9ucyl9XCIpXG4gICAgZm9yIGtleSwgdmFsdWUgaW4gZXh0cmFfaW5mby5pdGVtcygpOlxuICAgICAgICBwcmludChmXCJ7a2V5fToge3ZhbHVlfVwiKVxuXG50cmlwX3N1bW1hcnkoXCJHb2FcIiwgNTAwLCA0MDAsIDYwMCwgb3JnYW5pc2VyPVwiTmF2ZWVuXCIsIGRheXM9MykifQ"
 width="100%"
></iframe>

Call this with a different number of contributions and a different set of extra details each time, and notice the same function definition handles every shape of call without complaint.

## Conclusion

`*args` gathers any number of extra positional arguments into a tuple, and `**kwargs` gathers any number of extra keyword arguments into a dictionary, freeing a function from needing to know in advance exactly how many inputs a call will bring. The two can be combined with ordinary parameters, always in the order ordinary parameters, then `*args`, then `**kwargs`. With functions now this flexible, the next lesson turns to a much shorter way to write a small, throwaway function: the lambda.
