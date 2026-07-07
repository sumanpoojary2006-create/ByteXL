## Introduction

Everything in this unit comes together the moment a program holds a conversation with the person using it. It asks a question, the user answers, and it responds with a clear, well-formatted message. Variables gave you a place to keep that answer, types told Python what kind of thing it was, and operators let you calculate with it. Output is the final, visible step, where all of that quiet internal work finally becomes a message a real person can read and trust. You have already used the two tools for this, `input()` to receive and `print()` to display. This lesson sharpens them, and introduces f-strings, the modern and far tidier way to build the text your program shows.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t836kc7/10_order_window_conversation.png)


## Talking to the User

A quick recap of the pair you have been using. `input()` pauses the program, shows a prompt, and returns whatever the user types, always as a string. `print()` displays one or more values on the screen.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjEwX2lucHV0X291dHB1dF9hbmRfZnN0cmluZ3MgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6Im5hbWUgPSBpbnB1dChcIldoYXQgaXMgeW91ciBuYW1lPyBcIilcbnByaW50KFwiSGVsbG8sXCIsIG5hbWUpIn0"
 width="100%"
></iframe>

When you pass several items to `print` separated by commas, it shows them in order with a single space between each. That automatic space is convenient, but it is not always exactly what you want, which is where the next idea helps.

## The Messy Way and the Clean Way

Suppose you want to print a sentence that weaves a name and an age together. Using plus signs to join strings quickly becomes awkward, and it fails outright if you forget to convert numbers to text.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjEwX2lucHV0X291dHB1dF9hbmRfZnN0cmluZ3MgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6Im5hbWUgPSBcIkFzaGFcIlxuYWdlID0gMjBcbnByaW50KFwiTXkgbmFtZSBpcyBcIiArIG5hbWUgKyBcIiBhbmQgSSBhbSBcIiArIHN0cihhZ2UpICsgXCIgeWVhcnMgb2xkLlwiKSJ9"
 width="100%"
></iframe>

That works, but it is hard to read and easy to break. Add one more variable to that sentence, or forget a single `str()` around a number, and the whole line stops working or reads awkwardly. Counting plus signs and quotation marks by eye is not a skill any programmer should need. So is there a cleaner way? Yes, and it is one of the nicest features in Python.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t836kc7/10_concat_vs_fstring.png)


## f-strings: the Clean Way to Build Text

An f-string is a normal string with the letter `f` in front of the opening quote. Inside it, anything you place in curly braces is replaced by its value. No plus signs, no manual conversion.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjEwX2lucHV0X291dHB1dF9hbmRfZnN0cmluZ3MgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6Im5hbWUgPSBcIkFzaGFcIlxuYWdlID0gMjBcbnByaW50KGZcIk15IG5hbWUgaXMge25hbWV9IGFuZCBJIGFtIHthZ2V9IHllYXJzIG9sZC5cIikifQ"
 width="100%"
></iframe>

Output:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjEwX2lucHV0X291dHB1dF9hbmRfZnN0cmluZ3MgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6Ik15IG5hbWUgaXMgQXNoYSBhbmQgSSBhbSAyMCB5ZWFycyBvbGQuIn0"
 width="100%"
></iframe>

The text reads almost exactly as the final sentence will look, with the variables sitting neatly in their slots. f-strings can even hold small calculations, so `f"Next year you will be {age + 1}."` works directly.

They also format numbers cleanly. To show a price with exactly two decimal places, add a small instruction after a colon:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjEwX2lucHV0X291dHB1dF9hbmRfZnN0cmluZ3MgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6InByaWNlID0gNDkuNVxucHJpbnQoZlwiVG90YWw6IHtwcmljZTouMmZ9XCIpICAgIyBUb3RhbDogNDkuNTAifQ"
 width="100%"
></iframe>

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t836kc7/10_mini_receipt_fstrings.png)


## Format Specifiers at a Glance

| Specifier | Effect | Example | Output |
|---|---|---|---|
| `:.2f` | Round to 2 decimal places | `f"{49.5:.2f}"` | `49.50` |
| `:,` | Group thousands with commas | `f"{1500000:,}"` | `1,500,000` |
| `:.1%` | Show as a percentage | `f"{0.873:.1%}"` | `87.3%` |

These are enough to make most output look clean. You will meet column alignment and more formatting tricks when you reach the Strings unit.

## Your Turn: A Mini Receipt

This program reads a couple of values and prints a tidy receipt using f-strings.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjEwX2lucHV0X291dHB1dF9hbmRfZnN0cmluZ3MgY29kZSA2IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA2LnB5IiwiY29kZSI6Iml0ZW0gPSBpbnB1dChcIkl0ZW0gbmFtZTogXCIpXG5xdHkgPSBpbnQoaW5wdXQoXCJRdWFudGl0eTogXCIpKVxucHJpY2UgPSBmbG9hdChpbnB1dChcIlByaWNlIHBlciBpdGVtOiBcIikpXG5cbnByaW50KGZcIntxdHl9IHgge2l0ZW19IGF0IHtwcmljZTouMmZ9IGVhY2hcIilcbnByaW50KGZcIlRvdGFsIHBheWFibGU6IHtxdHkgKiBwcmljZTouMmZ9XCIpIn0"
 width="100%"
></iframe>

Enter a few items of your own. Notice how the output lines read like a real receipt, with the quantity, name, and neatly rounded amounts all in place. The calculation `qty * price` even happens right inside the f-string.

## Conclusion

`input()` collects text from the user and `print()` displays results, while f-strings, written as `f"...{value}..."`, are the clean, readable way to weave variables and calculations into your output. Prefer them over joining strings with plus signs, lean on the `:.2f` style for money and measurements, and your programs will not only work correctly but also speak to their users clearly. Look back over this unit and you will see a single thread running through it: a value arrives, gets a type, gets stored in a well-named variable, gets transformed by an operator, and finally gets shown to someone in a sentence that makes sense. With variables, types, operators, and input and output in hand, you are fully ready for the decisions of the next unit.
