## Introduction

Naveen's receipt-printing function needs a small helper that formats a number as currency, padding it with a rupee symbol and two decimal places. That formatting logic is only ever useful inside the receipt function itself; no other part of his script has any business calling it directly, and he would rather not clutter the top level of his file with a tiny helper that only makes sense in one specific context.

Python lets you define a function inside another function, called a **nested function**, which exists only for as long as, and only inside, the function that contains it.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/09_nested_helper_function.png)

## Defining a Function Inside a Function

A nested function is written with `def`, exactly like any other function, simply indented one level inside another function's body.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X25lc3RlZF9mdW5jdGlvbnMgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6ImRlZiBwcmludF9yZWNlaXB0KGl0ZW0sIHByaWNlKTpcbiAgICBkZWYgZm9ybWF0X2N1cnJlbmN5KGFtb3VudCk6XG4gICAgICAgIHJldHVybiBmXCJScyB7YW1vdW50Oi4yZn1cIlxuXG4gICAgcHJpbnQoZlwie2l0ZW19OiB7Zm9ybWF0X2N1cnJlbmN5KHByaWNlKX1cIilcblxucHJpbnRfcmVjZWlwdChcIk11Z1wiLCAxNTApIn0"
 width="100%"
></iframe>

Output:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X25lc3RlZF9mdW5jdGlvbnMgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6Ik11ZzogUnMgMTUwLjAwIn0"
 width="100%"
></iframe>

`format_currency` is defined and used entirely inside `print_receipt`. It does its one small job, formatting a number, and `print_receipt` calls it exactly the way it would call any other function.

## A Nested Function Is Invisible From Outside

Try to call the inner function from outside the outer one, and Python cannot find it at all.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X25lc3RlZF9mdW5jdGlvbnMgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6InByaW50X3JlY2VpcHQoXCJNdWdcIiwgMTUwKVxuZm9ybWF0X2N1cnJlbmN5KDE1MCkgICAgIyBlcnJvciEifQ"
 width="100%"
></iframe>

This raises a `NameError`, because `format_currency` only exists while `print_receipt` is running, and only inside `print_receipt`'s own scope. The moment `print_receipt` finishes, its nested function disappears with it, exactly as if it had never been named at all outside that one context.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/09_nested_function_visibility.png)


## Why Hide a Function Like This?

Nesting is a deliberate way of saying "this helper exists purely to support this one outer job, and nobody else needs to know it exists." It keeps the top level of your script focused on the pieces that genuinely matter to the rest of the program, while small, single-purpose helpers stay tucked away exactly where they are used.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X25lc3RlZF9mdW5jdGlvbnMgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6ImRlZiBjYWxjdWxhdGVfZmluYWxfdG90YWwoaXRlbXMpOlxuICAgIGRlZiBhcHBseV9kaXNjb3VudChwcmljZSk6XG4gICAgICAgIHJldHVybiBwcmljZSAqIDAuOSBpZiBwcmljZSA-IDMwMCBlbHNlIHByaWNlXG5cbiAgICByZXR1cm4gc3VtKGFwcGx5X2Rpc2NvdW50KHByaWNlKSBmb3IgcHJpY2UgaW4gaXRlbXMpXG5cbnByaW50KGNhbGN1bGF0ZV9maW5hbF90b3RhbChbMzUwLCAxNTAsIDQ1MF0pKSAgICAjIDg3MC4wIn0"
 width="100%"
></iframe>

`apply_discount` is a genuinely useful idea, but only inside the context of calculating this particular total. Nesting it keeps that relationship explicit, rather than leaving a loosely related helper sitting at the top level of the script where it might be mistaken for something more broadly useful.

## A Nested Function Can See the Outer Function's Variables

A nested function can read variables from the function that contains it, without those variables being passed in as parameters at all.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X25lc3RlZF9mdW5jdGlvbnMgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6ImRlZiBwcmludF9pbnZvaWNlKGJ1eWVyKTpcbiAgICB0YXhfcmF0ZSA9IDAuMDVcblxuICAgIGRlZiBhZGRfdGF4KGFtb3VudCk6XG4gICAgICAgIHJldHVybiBhbW91bnQgKiAoMSArIHRheF9yYXRlKVxuXG4gICAgcHJpbnQoZlwie2J1eWVyfSBvd2VzIHthZGRfdGF4KDEwMDApOi4yZn1cIilcblxucHJpbnRfaW52b2ljZShcIk5hdmVlblwiKSJ9"
 width="100%"
></iframe>

`add_tax` never received `tax_rate` as a parameter, yet it can see it directly, because it is defined inside the same function that holds it. This connection between a nested function and its surrounding function's variables is called a closure, a deeper idea you will meet properly in a later course; for now, it is enough to know that an inner function can quietly see its outer function's local variables.

## Nested Functions at a Glance

| Idea | Behaviour |
|---|---|
| Where it is defined | Inside another function's body, indented one level deeper |
| Where it can be called from | Only from inside the outer function |
| Visibility from outside | Invisible; calling it directly raises a `NameError` |
| Access to the outer function's variables | Yes, it can read them directly |

## Your Turn: A Helper for a Helper's Job

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA5X25lc3RlZF9mdW5jdGlvbnMgY29kZSA2IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA2LnB5IiwiY29kZSI6ImRlZiBzdW1tYXJpc2Vfc2NvcmVzKHNjb3Jlcyk6XG4gICAgZGVmIGdyYWRlX2ZvcihzY29yZSk6XG4gICAgICAgIGlmIHNjb3JlID49IDc1OlxuICAgICAgICAgICAgcmV0dXJuIFwiUGFzc1wiXG4gICAgICAgIHJldHVybiBcIkZhaWxcIlxuXG4gICAgZm9yIHNjb3JlIGluIHNjb3JlczpcbiAgICAgICAgcHJpbnQoZlwie3Njb3JlfToge2dyYWRlX2ZvcihzY29yZSl9XCIpXG5cbnN1bW1hcmlzZV9zY29yZXMoWzg4LCA2MCwgOTUsIDQwXSkifQ"
 width="100%"
></iframe>

`grade_for` exists only to support `summarise_scores`, and tucking it inside keeps that relationship clear to anyone reading the code from the top down.

## Conclusion

A nested function is defined inside another function's body and exists only while, and only inside, that outer function, invisible to the rest of the script and free to read the outer function's local variables directly. Nesting is a tool for keeping small, single-purpose helpers exactly where they belong, rather than scattering them across the top level of your file. Functions can call each other and contain each other; the next lesson explains precisely which variables a function can see at all, a set of rules called scope.
