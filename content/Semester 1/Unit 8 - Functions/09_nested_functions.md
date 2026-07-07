## Introduction

Naveen's receipt-printing function needs a small helper that formats a number as currency, padding it with a rupee symbol and two decimal places. That formatting logic is only ever useful inside the receipt function itself; no other part of his script has any business calling it directly, and he would rather not clutter the top level of his file with a tiny helper that only makes sense in one specific context.

Python lets you define a function inside another function, called a **nested function**, which exists only for as long as, and only inside, the function that contains it.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/09_nested_helper_function.png)

## Defining a Function Inside a Function

A nested function is written with `def`, exactly like any other function, simply indented one level inside another function's body.

```python
def print_receipt(item, price):
    def format_currency(amount):
        return f"Rs {amount:.2f}"

    print(f"{item}: {format_currency(price)}")

print_receipt("Mug", 150)
```

Output:

```
Mug: Rs 150.00
```

`format_currency` is defined and used entirely inside `print_receipt`. It does its one small job, formatting a number, and `print_receipt` calls it exactly the way it would call any other function.

## A Nested Function Is Invisible From Outside

Try to call the inner function from outside the outer one, and Python cannot find it at all.

```python
def print_receipt(item, price):
    def format_currency(amount):
        return f"Rs {amount:.2f}"
    print(f"{item}: {format_currency(price)}")

print_receipt("Mug", 150)

format_currency(150)    # NameError: not visible outside print_receipt
```

```text
Mug: Rs 150.00
NameError: name 'format_currency' is not defined
```

This raises a `NameError`, because `format_currency` only exists while `print_receipt` is running, and only inside `print_receipt`'s own scope. The moment `print_receipt` finishes, its nested function disappears with it, exactly as if it had never been named at all outside that one context.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/09_nested_function_visibility.png)


## Why Hide a Function Like This?

Nesting is a deliberate way of saying "this helper exists purely to support this one outer job, and nobody else needs to know it exists." It keeps the top level of your script focused on the pieces that genuinely matter to the rest of the program, while small, single-purpose helpers stay tucked away exactly where they are used.

```python
def calculate_final_total(items):
    def apply_discount(price):
        return price * 0.9 if price > 300 else price

    return sum(apply_discount(price) for price in items)

print(calculate_final_total([350, 150, 450]))    # 870.0
```

`apply_discount` is a genuinely useful idea, but only inside the context of calculating this particular total. Nesting it keeps that relationship explicit, rather than leaving a loosely related helper sitting at the top level of the script where it might be mistaken for something more broadly useful.

## A Nested Function Can See the Outer Function's Variables

A nested function can read variables from the function that contains it, without those variables being passed in as parameters at all.

```python
def print_invoice(buyer):
    tax_rate = 0.05

    def add_tax(amount):
        return amount * (1 + tax_rate)

    print(f"{buyer} owes {add_tax(1000):.2f}")

print_invoice("Naveen")
```

`add_tax` never received `tax_rate` as a parameter, yet it can see it directly, because it is defined inside the same function that holds it. This connection between a nested function and its surrounding function's variables is called a closure, a deeper idea you will meet properly in a later course; for now, it is enough to know that an inner function can quietly see its outer function's local variables.

## Nested Functions at a Glance

| Idea | Behaviour |
|---|---|
| Where it is defined | Inside another function's body, indented one level deeper |
| Where it can be called from | Only from inside the outer function |
| Visibility from outside | Invisible; calling it directly raises a `NameError` |
| Access to the outer function's variables | Yes, it can read them directly |

## Your Turn: A Helper for a Helper's Job

```python
def summarise_scores(scores):
    def grade_for(score):
        if score >= 75:
            return "Pass"
        return "Fail"

    for score in scores:
        print(f"{score}: {grade_for(score)}")

summarise_scores([88, 60, 95, 40])
```

`grade_for` exists only to support `summarise_scores`, and tucking it inside keeps that relationship clear to anyone reading the code from the top down.

## Conclusion

A nested function is defined inside another function's body and exists only while, and only inside, that outer function, invisible to the rest of the script and free to read the outer function's local variables directly. Nesting is a tool for keeping small, single-purpose helpers exactly where they belong, rather than scattering them across the top level of your file. Functions can call each other and contain each other; the next lesson explains precisely which variables a function can see at all, a set of rules called scope.
