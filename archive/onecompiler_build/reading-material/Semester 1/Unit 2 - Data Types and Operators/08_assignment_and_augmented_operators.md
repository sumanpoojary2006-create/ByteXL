## Introduction

You already know that a single equals sign stores a value in a variable. Very often, though, you do not want a brand new value, you want to update the one you already have. A shopping cart total grows as you add items. A game score climbs as you win points. A countdown shrinks each second. None of those examples replace the old value with something unrelated; each one nudges the existing value a little further in some direction. This pattern, taking a variable and adjusting it, is so common that Python gives it a neat shorthand called augmented assignment.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t8348fj/08_running_total_jar.png)


## Updating a Variable Using Itself

The plain way to update a variable is to mention it on both sides of the equals sign.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2Fzc2lnbm1lbnRfYW5kX2F1Z21lbnRlZF9vcGVyYXRvcnMgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6InRvdGFsID0gMTAwXG50b3RhbCA9IHRvdGFsICsgNTBcbnByaW50KHRvdGFsKSAgICMgMTUwIn0"
 width="100%"
></iframe>

Read the middle line as an instruction: "work out total plus 50, then store the answer back in total". This works perfectly, and it is worth understanding fully, because the shorthand you are about to meet does exactly the same thing.

## The Shorthand: Augmented Assignment

Writing `total = total + 50` repeats the variable name, so Python offers a shorter form that combines an operator with the equals sign.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2Fzc2lnbm1lbnRfYW5kX2F1Z21lbnRlZF9vcGVyYXRvcnMgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6InRvdGFsID0gMTAwXG50b3RhbCArPSA1MCAgICAjIHRoZSBzYW1lIGFzIHRvdGFsID0gdG90YWwgKyA1MFxucHJpbnQodG90YWwpICAgIyAxNTAifQ"
 width="100%"
></iframe>

Every arithmetic operator has a matching augmented version:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2Fzc2lnbm1lbnRfYW5kX2F1Z21lbnRlZF9vcGVyYXRvcnMgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6InNjb3JlID0gMTBcbnNjb3JlICs9IDUgICAgICMgYWRkIGFuZCBzdG9yZSAgICAgICAtPiAxNVxuc2NvcmUgLT0gMyAgICAgIyBzdWJ0cmFjdCBhbmQgc3RvcmUgIC0-IDEyXG5zY29yZSAqPSAyICAgICAjIG11bHRpcGx5IGFuZCBzdG9yZSAgLT4gMjRcbnNjb3JlIC8vPSA1ICAgICMgZmxvb3ItZGl2aWRlICAgICAgICAtPiA0In0"
 width="100%"
></iframe>

They are not just shorter to type. They make your intent clearer, because `count += 1` says "increase the count" more directly than `count = count + 1` does, and a reader skimming your code recognises the shape of "update in place" instantly without re-deriving it from a longer line. You will see `+= 1` constantly once you reach loops, where a counter steps forward one at a time, ticking upward exactly the way the running total jar fills a little more with each addition.

## Augmented Operators at a Glance

| Operator | Equivalent To | Example |
|---|---|---|
| `+=` | `x = x + value` | `score += 5` |
| `-=` | `x = x - value` | `score -= 3` |
| `*=` | `x = x * value` | `score *= 2` |
| `/=` | `x = x / value` | `total /= 2` |
| `//=` | `x = x // value` | `score //= 5` |
| `%=` | `x = x % value` | `count %= 10` |
| `**=` | `x = x ** value` | `power **= 2` |

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t8348fj/08_augmented_operator_cards.png)


## Your Turn: A Running Total

This program keeps adding prices to a cart total, updating the same variable each time.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2Fzc2lnbm1lbnRfYW5kX2F1Z21lbnRlZF9vcGVyYXRvcnMgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6InRvdGFsID0gMFxudG90YWwgKz0gaW50KGlucHV0KFwiUHJpY2Ugb2YgaXRlbSAxOiBcIikpXG50b3RhbCArPSBpbnQoaW5wdXQoXCJQcmljZSBvZiBpdGVtIDI6IFwiKSlcbnRvdGFsICs9IGludChpbnB1dChcIlByaWNlIG9mIGl0ZW0gMzogXCIpKVxucHJpbnQoXCJDYXJ0IHRvdGFsOlwiLCB0b3RhbCkifQ"
 width="100%"
></iframe>

Start `total` at 0, then let each entry add to it. After three items you have the full amount, built up one step at a time. This add-as-you-go pattern is the heartbeat of totals, scores, and counters everywhere in programming.

## Conclusion

Augmented assignment operators like `+=`, `-=`, `*=`, and `//=` update a variable using its own current value, so `total += 50` is a tidy way of writing `total = total + 50`. They keep code short and, more importantly, make your intention obvious. Keep this pattern close, because the moment you start writing loops, a counter that climbs with `+= 1` will be everywhere, and you will be glad the habit is already comfortable by then.
