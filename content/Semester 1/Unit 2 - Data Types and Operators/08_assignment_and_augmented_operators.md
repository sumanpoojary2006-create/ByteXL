## Introduction

You already know that a single equals sign stores a value in a variable. Very often, though, you do not want a brand new value, you want to update the one you already have. A shopping cart total grows as you add items. A game score climbs as you win points. A countdown shrinks each second. None of those examples replace the old value with something unrelated; each one nudges the existing value a little further in some direction. This pattern, taking a variable and adjusting it, is so common that Python gives it a neat shorthand called augmented assignment.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t8348fj/08_running_total_jar.png)


## Updating a Variable Using Itself

The plain way to update a variable is to mention it on both sides of the equals sign.

```python
total = 100
total = total + 50
print(total)   # 150
```

Read the middle line as an instruction: "work out total plus 50, then store the answer back in total". This works perfectly, and it is worth understanding fully, because the shorthand you are about to meet does exactly the same thing.

## The Shorthand: Augmented Assignment

Writing `total = total + 50` repeats the variable name, so Python offers a shorter form that combines an operator with the equals sign.

```python
total = 100
total += 50    # the same as total = total + 50
print(total)   # 150
```

Every arithmetic operator has a matching augmented version:

```python
score = 10
score += 5     # add and store       -> 15
score -= 3     # subtract and store  -> 12
score *= 2     # multiply and store  -> 24
score //= 5    # floor-divide        -> 4
print(score)
```

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

```python
total = 0
total += int(input("Price of item 1: "))
total += int(input("Price of item 2: "))
total += int(input("Price of item 3: "))
print("Cart total:", total)
```

Start `total` at 0, then let each entry add to it. After three items you have the full amount, built up one step at a time. This add-as-you-go pattern is the heartbeat of totals, scores, and counters everywhere in programming.

## Conclusion

Augmented assignment operators like `+=`, `-=`, `*=`, and `//=` update a variable using its own current value, so `total += 50` is a tidy way of writing `total = total + 50`. They keep code short and, more importantly, make your intention obvious. Keep this pattern close, because the moment you start writing loops, a counter that climbs with `+= 1` will be everywhere, and you will be glad the habit is already comfortable by then.
