# Unit 8: Functions - 40 Higher-Order MCQs

## Assessment design

- Scope: all twelve Unit 8 topics
- Format: four options per question; exactly one best answer
- Difficulty mix: 10 foundational, 20 intermediate, 10 advanced
- Style: situation-led tracing, implementation comparison, failure diagnosis, repair selection, and design judgment
- Answer-quality controls: balanced positions, no consecutive repeated correct letter, and no uniquely longest correct option
- Opening coverage: Questions 1–10 collectively represent all eight Unit 8 taxonomy subtopics
- Metadata: every question identifies its taxonomy and primary assessment behaviour

---

## Questions

### 1. One discount rule, five checkout screens

**Difficulty:** Foundational

**Taxonomy:** `python` → `functions` → `defining-and-calling-functions`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a reusable function design

Five checkout screens contain copied versions of the same discount calculation. A policy change must take effect everywhere without creating five opportunities for inconsistent edits. Which redesign best supports that goal?

A. Add a comment above every copied calculation describing the new policy  
B. Place the calculation in one function and call it from each screen  
C. Rename the discount variable differently on every checkout screen  
D. Keep all five copies so that each screen remains independent

### 2. Binding keyword arguments independently of call order

**Difficulty:** Intermediate

**Taxonomy:** `python` → `functions` → `function-parameters-and-arguments`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing keyword binding; final value identification

A shipping function has one required parameter and one defaulted parameter:

```python
def shipping(weight, rate=20):
    return weight * rate

charge = shipping(rate=25, weight=4)
```

Which binding trace correctly identifies the value stored in `charge`?

A. `80`, because the default rate cannot be overridden by name  
B. `29`, because keyword arguments are added rather than bound  
C. The call fails because keyword arguments must follow parameter order  
D. `100`, because `weight` receives 4 and `rate` receives 25 by name

### 3. A local rate shadows but does not replace the global rate

**Difficulty:** Advanced

**Taxonomy:** `python` → `functions` → `variable-scope-and-legb`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing scope and shadowing; final values

A billing module contains two bindings with the same name:

```python
rate = 10

def quote():
    rate = 7
    return rate

inside = quote()
outside = rate
```

Which scope audit correctly records the two final values?

A. `inside == 7` and `outside == 10`  
B. Both are 7 because a local assignment replaces the global binding  
C. Both are 10 because functions cannot create local names matching global names  
D. The call raises `NameError` when Python sees two variables named `rate`

### 4. Completing a sorting key with a lambda

**Difficulty:** Foundational

**Taxonomy:** `python` → `functions` → `lambda-functions`  
**Is Curriculum Based:** No  
**Assessment type:** Completing missing lambda code

A product list contains `(name, stock)` tuples and must be sorted by stock count:

```python
products = [("Pen", 30), ("Book", 12), ("Bag", 20)]
ordered = sorted(products, key=__________________)
```

Which completion supplies a one-expression function that extracts the numeric stock field?

A. `lambda item: item[0]`  
B. `lambda item: len(item)`  
C. `lambda item: item[1]`  
D. `lambda item: item`

### 5. Comparing a mapped transformation with a comprehension

**Difficulty:** Intermediate

**Taxonomy:** `python` → `functions` → `higher-order-functions`  
**Is Curriculum Based:** No  
**Assessment type:** Comparing implementations; deciding equivalence

Two versions double every value in `numbers` and materialise a list.

Version A:

```python
result = list(map(lambda number: number * 2, numbers))
```

Version B:

```python
result = [number * 2 for number in numbers]
```

Assume each version receives a fresh equivalent finite iterable of numeric values. Which comparison is correct?

A. The versions produce the same list in the same order  
B. Version A retains only positive numbers, while Version B doubles all numbers  
C. Version B modifies every value inside the original iterable  
D. They differ whenever `numbers` is empty

### 6. Empty checks produce two different aggregate verdicts

**Difficulty:** Advanced

**Taxonomy:** `python` → `functions` → `built-in-functions`  
**Is Curriculum Based:** No  
**Assessment type:** Reasoning about truthiness and empty aggregate behaviour

A deployment has not registered any checks yet:

```python
checks = []
release_ready = all(checks)
alert_needed = any(checks)
```

Which result pair follows Python's empty-collection rules?

A. Both values are `False` because the list has no truthy items  
B. Both values are `True` because no check failed  
C. `release_ready` is `False` and `alert_needed` is `True`  
D. `release_ready` is `True` and `alert_needed` is `False`

### 7. Completing the stopping condition of a recursive countdown

**Difficulty:** Foundational

**Taxonomy:** `python` → `functions` → `recursion`  
**Is Curriculum Based:** No  
**Assessment type:** Completing a missing recursive base condition

A recursive helper must return `[3, 2, 1]` for `countdown(3)` and stop before adding zero:

```python
def countdown(n):
    if __________________:
        return []
    return [n] + countdown(n - 1)
```

Which base condition completes the function for non-negative starting values?

A. `n < 0`  
B. `n == 0`  
C. `n > 0`  
D. `n == 1`

### 8. Comparing a real docstring with an ordinary comment

**Difficulty:** Intermediate

**Taxonomy:** `python` → `functions` → `docstrings-and-clean-code`  
**Is Curriculum Based:** No  
**Assessment type:** Comparing documentation implementations

A team submits two documentation versions.

Version A:

```python
def total(values):
    """Return the sum of the supplied values."""
    return sum(values)
```

Version B:

```python
def total(values):
    # Return the sum of the supplied values.
    return sum(values)
```

Which review finding correctly distinguishes what `help(total)` can retrieve as the function's docstring?

A. Both versions create identical function docstrings because comments and strings are interchangeable  
B. Neither version creates documentation visible to `help()`  
C. Version A creates a docstring because the string is the first body statement; Version B provides only a source comment  
D. Version B creates a docstring, while Version A returns its explanatory string at runtime

### 9. A display helper is mistaken for a calculation helper

**Difficulty:** Intermediate

**Taxonomy:** `python` → `functions` → `function-parameters-and-arguments`  
**Is Curriculum Based:** No  
**Assessment type:** Spotting a print-versus-return bug; final value tracing

```python
def calculate_fee(amount):
    print(amount * 0.10)

fee = calculate_fee(500)
```

The screen shows `50.0`, but a later expression using `fee + 20` fails. Which value stored in `fee` explains the failure?

A. `50.0`, stored as text  
B. `500`, because the input is retained  
C. `20`, because the later addition assigns its operand to `fee` before calculating  
D. `None`, because the function prints but does not return a value

### 10. A validator has an early exit

**Difficulty:** Advanced

**Taxonomy:** `python` → `functions` → `defining-and-calling-functions`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing multiple conditions and early return

```python
def status(score):
    if score < 0:
        return "invalid"
    if score >= 50:
        return "pass"
    return "retry"

label = status(-4)
```

Which trace correctly accounts for the value assigned to `label`?

A. The first return ends the call, so `label` becomes `"invalid"`  
B. Every return runs in sequence, so `label` finally becomes `"retry"`  
C. The second condition replaces the first result with `"pass"`  
D. No branch completes because negative values cannot be compared

### 11. A booking helper receives incomplete trip data

**Difficulty:** Intermediate

**Taxonomy:** `python` → `functions` → `function-parameters-and-arguments`  
**Is Curriculum Based:** No  
**Assessment type:** Diagnosing a missing-argument failure

```python
def fare(distance, rate):
    return distance * rate

amount = fare(12)
```

Which incident report best matches this call?

A. It returns `12` because an omitted argument defaults to `1`  
B. It returns `0` because the second parameter has no value  
C. It raises `TypeError` because the required `rate` argument is missing  
D. It raises `NameError` because parameters cannot be used in expressions

### 12. A standard delivery fee can be overridden

**Difficulty:** Foundational

**Taxonomy:** `python` → `functions` → `function-parameters-and-arguments`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a call that uses a default value

```python
def total(price, delivery=40):
    return price + delivery
```

A local order uses the standard delivery fee. Which call expresses that intention most directly?

A. `total(delivery=500)`  
B. `total(500)`  
C. `total()`  
D. `total(40, 500)`

### 13. Repairing an invalid parameter list

**Difficulty:** Intermediate

**Taxonomy:** `python` → `functions` → `function-parameters-and-arguments`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the smallest parameter-order repair

A developer writes `def reserve(seats=1, customer):` and Python rejects the definition. Which smallest repair retains `seats` as optional and `customer` as required?

A. `def reserve(seats, customer=1):`  
B. `def reserve(seats=1, customer=None):`  
C. `def reserve(customer=1, seats):`  
D. `def reserve(customer, seats=1):`

### 14. Named arguments protect a call from order confusion

**Difficulty:** Intermediate

**Taxonomy:** `python` → `functions` → `function-parameters-and-arguments`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing keyword arguments and defaults

```python
def badge(name, role, colour="blue"):
    return f"{name}:{role}:{colour}"

result = badge(role="Mentor", name="Ira")
```

Which badge text is produced?

A. `Mentor:Ira:blue`  
B. `Ira:blue:Mentor`  
C. `Ira:Mentor:blue`  
D. The call fails because keyword arguments must follow parameter order

### 15. A mixed call places one argument in an illegal position

**Difficulty:** Advanced

**Taxonomy:** `python` → `functions` → `function-parameters-and-arguments`  
**Is Curriculum Based:** No  
**Assessment type:** Diagnosing call syntax; smallest correct repair

For `def quote(customer, rate=5): ...`, a developer writes `quote(rate=7, "Riya")`. Which minimal edit makes the call valid while preserving the intended customer and rate?

A. `quote("Riya", rate=7)`  
B. `quote(rate=7, customer)`  
C. `quote(customer="Riya", 7)`  
D. `quote("Riya" rate=7)`

### 16. Extra positional readings arrive from a sensor

**Difficulty:** Foundational

**Taxonomy:** `python` → `functions` → `function-parameters-and-arguments`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing `*args` collection

```python
def capture(device, *readings):
    return readings

data = capture("S1", 18, 21, 19)
```

Which object is stored in `data`?

A. `{"18": 21, "19": None}`  
B. `[18, 21, 19]`  
C. `"18,21,19"`  
D. `(18, 21, 19)`

### 17. Optional named settings vary by deployment

**Difficulty:** Intermediate

**Taxonomy:** `python` → `functions` → `function-parameters-and-arguments`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing `**kwargs` collection

```python
def configure(app, **settings):
    return settings

chosen = configure("portal", theme="dark", retries=2)
```

Which value is assigned to `chosen`?

A. `{"theme": "dark", "retries": 2}`  
B. `("theme", "dark", "retries", 2)`  
C. `["dark", 2]`  
D. `{"portal": {"theme": "dark", "retries": 2}}`

### 18. One call routes three kinds of input

**Difficulty:** Advanced

**Taxonomy:** `python` → `functions` → `function-parameters-and-arguments`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing ordinary, variadic positional, and keyword inputs

```python
def record(owner, *tags, **details):
    return owner, tags, details

entry = record("Asha", "urgent", "new", floor=2, active=True)
```

Which decomposition matches the values returned in `entry`?

A. Owner is `"Asha"`; tags and details are combined into one list  
B. Owner is `"Asha"`; tags is a dictionary; details is a tuple  
C. Owner is `"Asha"`; tags is a tuple; details is a dictionary  
D. Owner contains all strings; details contains only `True`

### 19. A short conversion is needed inside another expression

**Difficulty:** Foundational

**Taxonomy:** `python` → `functions` → `lambda-functions`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a correct lambda implementation

A report needs a compact function that converts rupees to paise by multiplying one value by 100. Which expression creates that function?

A. `lambda amount: amount + 100`  
B. `lambda amount: amount * 100`  
C. `lambda: amount * 100`  
D. `lambda amount: 100`

### 20. Sorting products by stock instead of by name

**Difficulty:** Intermediate

**Taxonomy:** `python` → `functions` → `lambda-functions`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing a lambda sorting key

```python
products = [("Pen", 30), ("Book", 12), ("Bag", 20)]
ordered = sorted(products, key=lambda item: item[1])
```

Which ordering reaches `ordered`?

A. `[('Pen', 30), ('Book', 12), ('Bag', 20)]`  
B. `[('Bag', 20), ('Book', 12), ('Pen', 30)]`  
C. `[('Pen', 30), ('Bag', 20), ('Book', 12)]`  
D. `[('Book', 12), ('Bag', 20), ('Pen', 30)]`

### 21. Choosing between a lambda and a named function

**Difficulty:** Advanced

**Taxonomy:** `python` → `functions` → `lambda-functions`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a maintainable function structure

A pricing rule must validate a category, apply one of three discounts, log rejected inputs, and be reused by several modules. Which implementation choice is most appropriate?

A. Put all steps into one lambda separated by semicolons  
B. Use a named function with clear branches and a documented return value  
C. Create and maintain a separate lambda independently inside every module that needs the pricing rule  
D. Store the steps as strings and evaluate them when a price arrives

### 22. Converting every temperature reading

**Difficulty:** Foundational

**Taxonomy:** `python` → `functions` → `higher-order-functions`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a correct mapping pipeline

Given `celsius = [0, 10, 20]`, which use of `map` applies the conversion `c * 9 / 5 + 32` to every reading and produces a list?

A. `list(map(lambda c: c * 9 / 5 + 32, celsius))`  
B. `list(map(lambda c: c * 9 / 5, celsius))`  
C. `list(filter(lambda c: c * 9 / 5 + 32, celsius))`  
D. `[c * 9 / 5 + 32 for c in celsius if c > 0]`

### 23. Keeping only orders that qualify for free delivery

**Difficulty:** Intermediate

**Taxonomy:** `python` → `functions` → `higher-order-functions`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing a filtering predicate

```python
totals = [320, 800, 499, 1200]
eligible = list(filter(lambda amount: amount >= 500, totals))
```

Which list is assigned to `eligible`?

A. `[False, True, False, True]`  
B. `[320, 499]`  
C. `[800, 1200]`  
D. `[320, 800, 499, 1200]`

### 24. A reduction works, but the standard tool is clearer

**Difficulty:** Advanced

**Taxonomy:** `python` → `functions` → `higher-order-functions`  
**Is Curriculum Based:** No  
**Assessment type:** Comparing aggregation implementations

A developer uses `reduce(lambda a, b: a + b, amounts)` only to add ordinary numeric amounts. Which review recommendation best improves clarity without changing the goal?

A. Replace it with `filter(amounts)` because filtering also combines values  
B. Replace it with `sum(amounts)` because summation is the direct built-in operation  
C. Replace it with `map(amounts)` because mapping automatically returns one accumulated numeric total  
D. Keep `reduce`; built-ins cannot add a collection of numeric values

### 25. Releasing a batch only when every check passes

**Difficulty:** Foundational

**Taxonomy:** `python` → `functions` → `built-in-functions`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting an all-values aggregate condition

A deployment stores check results as `[True, True, False, True]`. The release must proceed only if every check passed. Which condition enforces that policy?

A. `if len(checks):`  
B. `if sum(checks):`  
C. `if any(checks):`  
D. `if all(checks):`

### 26. Alerting when at least one account is overdue

**Difficulty:** Intermediate

**Taxonomy:** `python` → `functions` → `built-in-functions`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting an any-value aggregate condition

The flags `[False, False, True, False]` represent overdue accounts. Which expression answers whether the alert service has at least one case to process?

A. `all(overdue)`  
B. `any(overdue)`  
C. `max(len(overdue))`  
D. `sorted(overdue)`

### 27. Selecting the shortest support ticket by message length

**Difficulty:** Intermediate

**Taxonomy:** `python` → `functions` → `built-in-functions`  
**Is Curriculum Based:** No  
**Assessment type:** Applying a built-in with a key function

```python
tickets = ["Cannot log in", "Refund", "Address update"]
```

Which expression returns `"Refund"` without manually tracking a current shortest value?

A. `min(tickets, key=len)`  
B. `min(len(tickets))`  
C. `sorted(tickets)[0]`  
D. `max(tickets, key=len)`

### 28. A formatting helper belongs only to one report

**Difficulty:** Foundational

**Taxonomy:** `python` → `functions` → `variable-scope-and-legb`  
**Is Curriculum Based:** No  
**Assessment type:** Identifying nested-function visibility

An outer function defines `format_row()` inside itself and uses it successfully. Later, unrelated code tries to call `format_row()` directly. Which result follows from that placement?

A. The helper runs because every nested definition is automatically copied into global scope when the outer function returns  
B. Python silently creates another helper outside the report  
C. The direct outside call raises `NameError` because the helper is local to the outer function  
D. The helper returns `None` only when called from outside

### 29. An inner helper uses its enclosing function's value

**Difficulty:** Intermediate

**Taxonomy:** `python` → `functions` → `variable-scope-and-legb`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing enclosing-scope lookup

```python
def make_label(prefix):
    def attach(name):
        return prefix + name
    return attach("42")

result = make_label("ORD-")
```

Which value reaches `result`?

A. `"42ORD-"`  
B. `"prefix42"`  
C. The call fails because `attach` has no access to `prefix`  
D. `"ORD-42"`

### 30. Deciding whether a helper should be nested

**Difficulty:** Advanced

**Taxonomy:** `python` → `functions` → `docstrings-and-clean-code`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting an appropriately scoped helper design

A sanitising helper is used only while building one confidential report and should not become part of the module's public collection of utilities. Which placement best communicates that design?

A. Define the sanitising helper inside the report-building function  
B. Duplicate the sanitising expression at every point of use  
C. Define it globally and rely on a comment asking others not to call it  
D. Store the helper name in a list instead of defining a function

### 31. A local calculation is requested after the call ends

**Difficulty:** Intermediate

**Taxonomy:** `python` → `functions` → `variable-scope-and-legb`  
**Is Curriculum Based:** No  
**Assessment type:** Diagnosing a local-scope failure

```python
def invoice(subtotal):
    tax = subtotal * 0.18
    return subtotal + tax

total = invoice(1000)
print(tax)
```

Which diagnosis belongs in the test report?

A. `tax` becomes `0` after the call and is printed normally  
B. The final line raises `NameError` because `tax` exists only in the function's local scope  
C. `tax` is automatically copied into global scope when the function returns any expression that uses it  
D. The function raises `TypeError` before calculating a value

### 32. A function reads a module-level rate

**Difficulty:** Intermediate

**Taxonomy:** `python` → `functions` → `variable-scope-and-legb`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing global lookup under LEGB

```python
rate = 8

def charge(units):
    return units * rate

bill = charge(5)
```

Which value is assigned to `bill`?

A. `5`  
B. `8`  
C. The call fails because functions cannot read global variables  
D. `40`

### 33. The nearest matching name wins

**Difficulty:** Intermediate

**Taxonomy:** `python` → `functions` → `variable-scope-and-legb`  
**Is Curriculum Based:** No  
**Assessment type:** Tracing local shadowing under LEGB

```python
label = "global"

def choose():
    label = "local"
    return label

result = choose()
```

Under LEGB lookup, which value is assigned to `result`?

A. Both strings joined together  
B. `"global"`  
C. `"local"`  
D. An undefined-name error

### 34. A counter update is mistaken for a global read

**Difficulty:** Advanced

**Taxonomy:** `python` → `functions` → `variable-scope-and-legb`  
**Is Curriculum Based:** No  
**Assessment type:** Spotting an assignment-scope bug; smallest repair

```python
counter = 0

def increment():
    counter = counter + 1
    return counter

increment()
```

The existing global counter must be modified. Which smallest repair makes that intention explicit?

A. Add `global counter` as the first statement inside `increment`  
B. Add `return counter` before the assignment  
C. Rename the global variable but leave the function unchanged  
D. Move the assignment into another nested function

### 35. Giving factorial a stopping point

**Difficulty:** Foundational

**Taxonomy:** `python` → `functions` → `recursion`  
**Is Curriculum Based:** No  
**Assessment type:** Identifying the role of a recursive base case

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

Which role does the `n == 0` branch play?

A. It repeats the recursive step with a smaller argument until multiplication reaches zero  
B. It converts every argument into a Boolean value  
C. It is the base case that stops further recursive calls  
D. It causes the function to skip all multiplication

### 36. Selecting the input that exposes a missing zero base case

**Difficulty:** Intermediate

**Taxonomy:** `python` → `functions` → `recursion`  
**Is Curriculum Based:** No  
**Assessment type:** Choosing an input that exposes a recursion defect

A developer writes a factorial function whose only base case is `n == 1`:

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
```

The required domain includes zero. Which input most directly exposes the missing `0! = 1` base case by driving the recursion away from termination?

A. `factorial(1)`  
B. `factorial(0)`  
C. `factorial(2)`  
D. `factorial(4)`

### 37. A recursive retry never approaches a stopping case

**Difficulty:** Advanced

**Taxonomy:** `python` → `functions` → `recursion`  
**Is Curriculum Based:** No  
**Assessment type:** Diagnosing unexpected recursive nontermination

```python
def retry(attempt):
    if attempt == 0:
        return "done"
    return retry(attempt + 1)

retry(3)
```

Which operational outcome should the developer expect?

A. It returns `"done"` after three calls because the input is positive  
B. It returns `4` because the recursive argument increases once  
C. It loops forever without Python imposing a recursion limit or interrupting the accumulating calls  
D. It eventually raises `RecursionError` because the argument moves away from the base case

### 38. Making built-in help useful for a new function

**Difficulty:** Intermediate

**Taxonomy:** `python` → `functions` → `docstrings-and-clean-code`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting correct docstring placement

A team wants `help(calculate_total)` to show a concise explanation of the function. Where should the explanatory string be placed?

A. As the first statement inside the function body  
B. After every call to the function  
C. Before `def`, assigned to a module variable that happens to use the same function name  
D. Inside the return expression after the result

### 39. Interpreting type hints during execution

**Difficulty:** Intermediate

**Taxonomy:** `python` → `functions` → `docstrings-and-clean-code`  
**Is Curriculum Based:** No  
**Assessment type:** Identifying unexpected annotation behaviour

```python
def double(value: int) -> int:
    return value * 2

result = double("ha")
```

In standard Python without an external type checker, which assessment is accurate?

A. Python rejects the call before entering the function because `value` is not an integer  
B. The hint documents intent but is not enforced here, so `result` becomes `"haha"`  
C. Python converts `"ha"` to an integer and returns `0`  
D. The annotation changes string multiplication into numeric addition

### 40. A function has accumulated unrelated responsibilities

**Difficulty:** Intermediate

**Taxonomy:** `python` → `functions` → `docstrings-and-clean-code`  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a clean decomposition repair

`process_order()` validates an address, calculates tax, updates inventory, sends email, and formats an analytics report. Failures are difficult to isolate. Which redesign most closely follows clean function design?

A. Rename it `process_order_and_everything_else()` while keeping the body unchanged  
B. Add Boolean flags for every responsibility and require each caller to choose the exact combination before every order  
C. Extract focused functions for each responsibility and coordinate them from a small workflow  
D. Copy the entire function for each kind of order

---

## Instructor answer key and rationales

| Q | Answer | Difficulty | Rationale |
|---:|:---:|---|---|
| 1 | B | Foundational | One shared function provides a single place to update the discount rule while allowing every screen to reuse it. |
| 2 | D | Intermediate | Keyword arguments bind by parameter name rather than call order, so `4 * 25` produces 100. |
| 3 | A | Advanced | The assignment inside `quote` creates a local binding of 7; it shadows but does not replace the global binding of 10. |
| 4 | C | Foundational | The lambda receives one tuple and returns its stock field at index 1 for use as the sorting key. |
| 5 | A | Intermediate | Both implementations iterate once, double every encountered numeric value, preserve order, and materialise the results as a list. |
| 6 | D | Advanced | `all([])` is vacuously true because no element fails, while `any([])` is false because no element succeeds. |
| 7 | B | Foundational | At zero the function returns an empty list without another call; earlier calls then prepend 1, 2, and 3 while unwinding. |
| 8 | C | Intermediate | Only a string literal used as the first function-body statement becomes `__doc__` and is displayed by `help`; a comment does not. |
| 9 | D | Intermediate | Printing displays a value but does not return it; a function with no explicit return supplies `None`. |
| 10 | A | Advanced | A return immediately ends that call, so neither later condition nor the final return is evaluated. |
| 11 | C | Intermediate | Both parameters are required, but the call supplies only `distance`, producing a missing-argument `TypeError`. |
| 12 | B | Foundational | Supplying only `price` allows the declared delivery default of 40 to be used. |
| 13 | D | Intermediate | Required parameters must precede parameters with default values. |
| 14 | C | Intermediate | Keyword arguments bind by parameter name, and the omitted colour uses its default. |
| 15 | A | Advanced | Positional arguments must precede keyword arguments; this repair supplies the customer first and names the rate. |
| 16 | D | Foundational | `*readings` collects the extra positional arguments into a tuple. |
| 17 | A | Intermediate | `**settings` collects extra keyword arguments into a dictionary using their names as keys. |
| 18 | C | Advanced | The ordinary parameter receives the first value, `*tags` forms a tuple, and `**details` forms a dictionary. |
| 19 | B | Foundational | A lambda contains parameters, a colon, and one automatically returned expression, without the `return` keyword. |
| 20 | D | Intermediate | The key extracts each stock count, so ascending order is 12, 20, then 30. |
| 21 | B | Advanced | Multi-step validation, branching, logging, reuse, and documentation are clearer in a named function. |
| 22 | A | Foundational | `map` applies the conversion to every element, and `list` materialises the mapped results. |
| 23 | C | Intermediate | `filter` retains the original amounts whose predicate is true: 800 and 1200. |
| 24 | B | Advanced | `sum` states the ordinary numeric aggregation directly and avoids an unnecessary custom reducer. |
| 25 | D | Foundational | `all` is true only when every item is truthy, matching an every-check-must-pass policy. |
| 26 | B | Intermediate | `any` answers whether at least one item is truthy. |
| 27 | A | Intermediate | `min` compares the strings through the `len` key and returns the shortest original string. |
| 28 | C | Foundational | A nested function name belongs to the enclosing function's local scope and is not directly available outside it. |
| 29 | D | Intermediate | The inner function can read `prefix` from the enclosing scope, producing `ORD-42`. |
| 30 | A | Advanced | Nesting keeps a single-purpose implementation detail close to its only caller and out of module scope. |
| 31 | B | Intermediate | `tax` is local to `invoice` and no longer exists by that name after the call finishes. |
| 32 | D | Intermediate | Since no nearer `rate` exists, LEGB lookup finds the global value 8, giving 40. |
| 33 | C | Intermediate | The local assignment is the nearest binding, so it shadows the global `label` during the call. |
| 34 | A | Advanced | Declaring `global counter` tells Python that the assignment targets the existing global binding. |
| 35 | C | Foundational | The base case supplies a result without making another recursive call, allowing recursion to stop. |
| 36 | B | Intermediate | Starting at zero misses the `n == 1` base case and recurses through negative values, directly exposing the missing zero case. |
| 37 | D | Advanced | Starting at 3 and adding 1 never reaches 0, so calls accumulate until Python's recursion limit is exceeded. |
| 38 | A | Intermediate | A string literal placed first in the function body becomes its docstring and is surfaced by `help`. |
| 39 | B | Intermediate | Annotations do not enforce runtime types by themselves; string multiplication therefore returns `haha`. |
| 40 | C | Intermediate | Focused functions isolate responsibilities, while a small coordinator can preserve the overall order workflow. |

---

## Taxonomy coverage

| Unit 8 taxonomy subtopic | Questions |
|---|---|
| `defining-and-calling-functions` | 1, 10 |
| `function-parameters-and-arguments` | 2, 9, 11–18 |
| `variable-scope-and-legb` | 3, 28–29, 31–34 |
| `lambda-functions` | 4, 19–21 |
| `higher-order-functions` | 5, 22–24 |
| `built-in-functions` | 6, 25–27 |
| `recursion` | 7, 35–37 |
| `docstrings-and-clean-code` | 8, 30, 38–40 |
