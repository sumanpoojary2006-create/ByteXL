## Introduction

The moment an expression contains more than one operator, a question arises: which part runs first? You already know the answer from school maths, where multiplication happens before addition. Python follows the same kind of rulebook, called operator precedence, and getting it wrong is one of the sneakiest sources of bugs, because the program does not crash. It simply gives you the wrong number with complete confidence, and confident wrong numbers are far more dangerous than a loud error, because nothing on screen tells you to go back and check.

## Which Operator Goes First?

Consider a simple expression:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-2-data-types-and-operators-09-operator-precedence-and-associat-001-93bcfa48aa.html"
 width="100%"
></iframe>

If Python worked strictly left to right, the answer would be 20. Instead it prints 14, because multiplication has higher precedence than addition, so `3 * 4` happens first and then 2 is added. This matches ordinary arithmetic, which is reassuring, but it means you cannot assume operations run in reading order.

## Operator Precedence at a Glance

| Level | Operators | Example |
|---|---|---|
| 1 (highest) | `**` | `2 ** 3` |
| 2 | `*`, `/`, `//`, `%` | `3 * 4` |
| 3 | `+`, `-` | `2 + 3` |
| 4 | `==`, `!=`, `<`, `>`, `<=`, `>=` | `5 > 3` |
| 5 (lowest) | `not`, `and`, `or` | `True and False` |

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t8356mw/09_recipe_card_step_order.png)


## The Bug Hiding in a Formula

Here is a classic. Suppose you want the average of two numbers and write this:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-2-data-types-and-operators-09-operator-precedence-and-associat-002-e628b20342.html"
 width="100%"
></iframe>

Why is the answer wrong? Because division runs before addition, so Python computes `b / 2` first, getting 10, and then adds `a`, giving 20. The program is behaving exactly as the rules require. It is the formula that is at fault. This is the trap precedence sets for anyone who skims a formula left to right instead of asking which operator actually has priority, and notice that nothing here looked suspicious; the line ran cleanly and printed a perfectly reasonable looking number, just the wrong one.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t8356mw/09_parentheses_average_fix.png)


## Parentheses Are Your Safety Net

The fix is simple and worth making a habit: use parentheses to force the order you actually want. Anything inside parentheses is worked out first.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-2-data-types-and-operators-09-operator-precedence-and-associat-003-c23e87eece.html"
 width="100%"
></iframe>

Even when parentheses are not strictly necessary, adding them often makes an expression far easier to read. Clear beats clever, and a reader should never have to recall the full precedence table to understand your intent.

## When Operators Are Equal: Associativity

What if two operators have the same precedence, as in `100 - 30 - 20`? Python resolves these from left to right, so it computes `100 - 30` first, then subtracts 20, giving 50. This left-to-right rule is called associativity, and it applies to most operators. The main exception is the power operator, which works right to left, so `2 ** 3 ** 2` is `2 ** 9`, not `8 ** 2`.

## Your Turn: Spot the Silent Bug

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-2-data-types-and-operators-09-operator-precedence-and-associat-004-aeda1fa4dc.html"
 width="100%"
></iframe>

Before running this, work out by hand what you expect, then run it and compare. Now add parentheses around `discount / 100 * price * quantity` to make the intended order explicit, and confirm the answer does not change, only the formula's readability does.

## Conclusion

When an expression mixes operators, Python follows a fixed precedence: powers first, then multiplication and division, then addition and subtraction, then comparisons, then logic. Operators of equal rank usually run left to right. You do not need to memorise every detail, because one habit covers you: when in doubt, add parentheses. They make the order explicit, prevent silent arithmetic bugs, and make your formulas readable at a glance. The average-of-two formula you just saw fail is a mistake every beginner makes at least once, so let this lesson be the time you make it on paper instead of in a program someone else is depending on. The next lesson turns to input, output, and f-strings, where precedence quietly matters again the moment you start building formatted strings out of calculated values.
