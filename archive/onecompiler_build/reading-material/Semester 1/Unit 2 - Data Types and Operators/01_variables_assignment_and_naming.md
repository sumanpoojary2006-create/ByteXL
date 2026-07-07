## Introduction

Think about a kitchen shelf lined with jars. One is labelled "sugar", another "salt", another "tea". The label is not the contents; it is how you find the contents. When a recipe says "add two spoons of sugar", you do not care which exact grains you use. You just reach for the jar named "sugar".

A **variable** in Python is exactly that: a label attached to a piece of data. You already met one in the last unit, when a program asked for your name and remembered it. That remembered value lived in a variable. Without that labelled drawer, the computer would have nowhere to keep what you typed, and the very next line of the program would have no idea what you meant by "your name". Variables are the reason a program can hold a thought from one line to the next instead of forgetting everything the instant it moves on. In this lesson we look at how to create variables, how to give them values, and how to name them well.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t7vzund/01_variables_assignment_naming.png)


## Giving a Name to a Value

Creating a variable takes one symbol: the equals sign. It does not mean "equal" in the maths sense. It means "put the value on the right into the label on the left".

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3ZhcmlhYmxlc19hc3NpZ25tZW50X2FuZF9uYW1pbmcgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6ImNpdHkgPSBcIlB1bmVcIlxudGVtcGVyYXR1cmUgPSAzMiJ9"
 width="100%"
></iframe>

Read those as instructions: "let city hold the text Pune" and "let temperature hold the number 32". From now on, wherever you write `city`, Python hands you "Pune". You can prove it:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3ZhcmlhYmxlc19hc3NpZ25tZW50X2FuZF9uYW1pbmcgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6ImNpdHkgPSBcIlB1bmVcIlxucHJpbnQoXCJJIGxpdmUgaW5cIiwgY2l0eSkifQ"
 width="100%"
></iframe>

Output:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3ZhcmlhYmxlc19hc3NpZ25tZW50X2FuZF9uYW1pbmcgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6IkkgbGl2ZSBpbiBQdW5lIn0"
 width="100%"
></iframe>

The variable did its job: it stored a value once, and you reused it by name. Notice what you did not have to do. You did not retype "Pune" the second time, and you did not need to remember where in the computer's memory the text was actually sitting. The name `city` is the only address you ever need, and Python quietly handles the rest behind the scenes, the same way a jar's label spares you from peeking inside every container on the shelf just to find the sugar.

## The Name on the Box Matters

A computer will happily accept a variable called `x`, but six months later, will you remember what `x` meant? Picture two kitchen jars with no labels at all, just plain glass containers of white powder. You would have to taste one to know whether you grabbed sugar or salt, and by then the damage is done. Unnamed or carelessly named variables cause exactly that kind of confusion in code, except the mistake usually surfaces as a bug that someone has to track down later, often you. Good names are a gift to your future self and to anyone who reads your code. Python has a few firm rules and a widely followed style guide called PEP 8.

The firm rules:

- A name may use letters, digits, and the underscore, but it cannot start with a digit.
- No spaces are allowed, and names are case sensitive, so `score` and `Score` are two different variables.
- You cannot use a word Python has reserved for itself, such as `if`, `for`, or `class`.

The style conventions from PEP 8:

- Use lower case words joined by underscores, such as `first_name` or `total_marks`. This is called snake_case.
- Choose descriptive names. `student_age` tells a story; `a` does not.

## Naming Rules at a Glance

| Aspect | Requirement | Example |
|---|---|---|
| Allowed characters | Letters, digits, underscore; cannot start with a digit | `score_1` is valid, `1_score` is not |
| Case sensitivity | `score` and `Score` are treated as different variables | Pick one style and stay consistent |
| Reserved words | Cannot reuse a word Python keeps for itself | Avoid `if`, `for`, `class`, `print` |
| Style (PEP 8) | snake_case, descriptive, lower case | `total_marks`, not `TotalMarks` or `tm` |

So here is a quick question: would `2nd_score` be a valid variable name?

No. A name cannot begin with a digit, so Python rejects it before the program even runs. A small rename to `second_score` fixes it and reads better too.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t7vzund/01_naming_rules_checkpoint.png)


## A Label Can Be Re-attached

A variable is not carved in stone. You can point the same name at a new value whenever you like, and the old value is simply forgotten.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3ZhcmlhYmxlc19hc3NpZ25tZW50X2FuZF9uYW1pbmcgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6ImJhbGFuY2UgPSAxMDAwXG5iYWxhbmNlID0gYmFsYW5jZSAtIDI1MFxucHJpbnQoXCJSZW1haW5pbmcgYmFsYW5jZTpcIiwgYmFsYW5jZSkifQ"
 width="100%"
></iframe>

Output:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3ZhcmlhYmxlc19hc3NpZ25tZW50X2FuZF9uYW1pbmcgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6IlJlbWFpbmluZyBiYWxhbmNlOiA3NTAifQ"
 width="100%"
></iframe>

The line in the middle looks strange if you read the equals sign as "equal", because nothing equals itself minus 250. But read it as an instruction and it is clear: "work out balance minus 250, then store the result back in balance". This is exactly what happens at a real bank counter: the same account does not get a new number after a withdrawal, the balance recorded against it simply changes. The label `balance` stays fixed throughout the program; only the value sitting behind that label is swapped out. Python also lets a name hold different kinds of data at different times, which makes it flexible, though you should avoid reusing one name for unrelated things, since a jar labelled "sugar" that quietly starts holding salt will mislead the very next person who reaches for it.

## Your Turn: Build a Profile

Try this small interactive program. It asks for your details and stores each one in a well-named variable.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3ZhcmlhYmxlc19hc3NpZ25tZW50X2FuZF9uYW1pbmcgY29kZSA2IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA2LnB5IiwiY29kZSI6Im5hbWUgPSBpbnB1dChcIllvdXIgbmFtZTogXCIpXG5hZ2UgPSBpbnB1dChcIllvdXIgYWdlOiBcIilcbmNpdHkgPSBpbnB1dChcIllvdXIgY2l0eTogXCIpXG5cbnByaW50KG5hbWUsIFwiaXNcIiwgYWdlLCBcInllYXJzIG9sZCBhbmQgbGl2ZXMgaW5cIiwgY2l0eSkifQ"
 width="100%"
></iframe>

Run it, type your own answers, and watch the output change to match. You have just used three variables to hold three different pieces of information, exactly as a real registration form does behind the scenes.

## Conclusion

A variable is a named label for a value, created with the equals sign, which means "store this", not "is equal to". Choose clear, lower case, descriptive names in snake_case, avoid starting with a digit or using Python's reserved words, and remember that a variable can be updated at any time. Good naming is not decoration. It is what turns a wall of symbols into code that reads like a sentence.
