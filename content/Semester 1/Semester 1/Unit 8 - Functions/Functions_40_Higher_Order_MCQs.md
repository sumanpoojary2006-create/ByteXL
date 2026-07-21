# Unit 8: Functions - 40 Higher-Order MCQs

## Assessment design

- Scope: all twelve Unit 8 topics
- Format: four options per question; exactly one best answer
- Difficulty mix: 10 foundational, 20 intermediate, 10 advanced
- Style: situation-led tracing, implementation comparison, failure diagnosis, repair selection, and design judgment
- Answer-quality controls: balanced positions, no consecutive repeated correct letter, and no uniquely longest correct option

---

## Questions

### 1. One discount rule, five checkout screens

**Difficulty:** Foundational

Five checkout screens contain copied versions of the same discount calculation. A policy change must take effect everywhere without creating five opportunities for inconsistent edits. Which redesign best supports that goal?

A. Add a comment above every copied calculation describing the new policy  
B. Place the calculation in one function and call it from each screen  
C. Rename the discount variable differently on every checkout screen  
D. Keep all five copies so that each screen remains independent

### 2. Turning a long registration workflow into reviewable parts

**Difficulty:** Intermediate

A registration script validates contact details, calculates a fee, saves a record, and sends a confirmation inside one large block. The team wants each responsibility to be testable on its own. Which organisation is the strongest fit?

A. Repeat the full workflow for testing and production, then compare both copies manually after every change  
B. Replace every intermediate variable with a longer expression  
C. Put the whole workflow inside one loop controlled by a flag  
D. Create focused functions for validation, fee calculation, saving, and notification

### 3. Comparing two maintenance strategies

**Difficulty:** Advanced

Version A copies a tax formula into three reports. Version B calls one `calculate_tax(amount)` function from all three reports. The formula changes, and one report also needs to display the untaxed amount. Which assessment is most accurate?

A. Version B centralises the tax rule, while each report can still handle its own display needs  
B. Version A is safer because copied formulas automatically detect policy changes and synchronise every report without edits  
C. Version B prevents the reports from using any values except the returned tax  
D. Both versions always require exactly the same number of policy edits

### 4. A definition is loaded during application startup

**Difficulty:** Foundational

During startup, Python reaches this code but no later line calls the function:

```python
def announce():
    print("Workshop open")
```

Which startup observation is consistent with Python's function model?

A. The message appears twice because the name and body are processed  
B. Python reports an error because the function has no parameters  
C. The function becomes available, but the message does not appear  
D. The message appears once as soon as the definition is reached

### 5. A reminder must be sent once per pending account

**Difficulty:** Intermediate

The function below is already defined correctly:

```python
def remind():
    print("Payment pending")
```

A batch contains three pending accounts. Which addition produces one reminder for each account without copying the function body?

A. `for _ in range(3): remind()`  
B. `remind`  
C. `def remind(3)`  
D. `for _ in range(3): print(remind)`

### 6. A startup sequence calls a helper too early

**Difficulty:** Advanced

An engineer arranges a file like this:

```python
prepare()

def prepare():
    print("Ready")
```

The smallest repair must preserve the function body and still call it once. Which change meets that requirement?

A. Add `return prepare` inside the existing function body  
B. Change the first line to `print(prepare())` and leave its position unchanged  
C. Indent the function definition beneath the original call  
D. Move `prepare()` to a line after the function definition

### 7. Separating the placeholder from the supplied data

**Difficulty:** Foundational

Consider `def greet(name): ...` followed later by `greet("Meera")`. A reviewer is documenting the two roles. Which description is accurate?

A. Both `name` and `"Meera"` are return values  
B. `name` is a parameter; `"Meera"` is an argument  
C. `name` is an argument; `"Meera"` is a parameter  
D. Both are function names with different scopes

### 8. A cost-sharing service feeds another calculation

**Difficulty:** Intermediate

```python
def share(total, people):
    return total / people

per_person = share(900, 3)
final_charge = per_person + 25
```

Which amount reaches `final_charge`?

A. `275.0`  
B. `300.0`  
C. `325.0`  
D. `925.0`

### 9. A display helper is mistaken for a calculation helper

**Difficulty:** Intermediate

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

A developer writes `def reserve(seats=1, customer):` and Python rejects the definition. Which smallest repair retains `seats` as optional and `customer` as required?

A. `def reserve(seats, customer=1):`  
B. `def reserve(seats=1, customer=None):`  
C. `def reserve(customer=1, seats):`  
D. `def reserve(customer, seats=1):`

### 14. Named arguments protect a call from order confusion

**Difficulty:** Intermediate

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

For `def quote(customer, rate=5): ...`, a developer writes `quote(rate=7, "Riya")`. Which minimal edit makes the call valid while preserving the intended customer and rate?

A. `quote("Riya", rate=7)`  
B. `quote(rate=7, customer)`  
C. `quote(customer="Riya", 7)`  
D. `quote("Riya" rate=7)`

### 16. Extra positional readings arrive from a sensor

**Difficulty:** Foundational

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

A report needs a compact function that converts rupees to paise by multiplying one value by 100. Which expression creates that function?

A. `lambda amount: return amount * 100`  
B. `lambda amount: amount * 100`  
C. `def(amount): amount * 100`  
D. `lambda = amount * 100`

### 20. Sorting products by stock instead of by name

**Difficulty:** Intermediate

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

A pricing rule must validate a category, apply one of three discounts, log rejected inputs, and be reused by several modules. Which implementation choice is most appropriate?

A. Put all steps into one lambda separated by semicolons  
B. Use a named function with clear branches and a documented return value  
C. Create and maintain a separate lambda independently inside every module that needs the pricing rule  
D. Store the steps as strings and evaluate them when a price arrives

### 22. Converting every temperature reading

**Difficulty:** Foundational

Given `celsius = [0, 10, 20]`, which use of `map` applies the conversion `c * 9 / 5 + 32` to every reading and produces a list?

A. `list(map(lambda c: c * 9 / 5 + 32, celsius))`  
B. `map(celsius, lambda c: c * 9 / 5 + 32)`  
C. `list(filter(lambda c: c * 9 / 5 + 32, celsius))`  
D. `reduce(lambda c: c * 9 / 5 + 32, celsius)`

### 23. Keeping only orders that qualify for free delivery

**Difficulty:** Intermediate

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

A developer uses `reduce(lambda a, b: a + b, amounts)` only to add ordinary numeric amounts. Which review recommendation best improves clarity without changing the goal?

A. Replace it with `filter(amounts)` because filtering also combines values  
B. Replace it with `sum(amounts)` because summation is the direct built-in operation  
C. Replace it with `map(amounts)` because mapping automatically returns one accumulated numeric total  
D. Keep `reduce`; built-ins cannot add a collection of numeric values

### 25. Releasing a batch only when every check passes

**Difficulty:** Foundational

A deployment stores check results as `[True, True, False, True]`. The release must proceed only if every check passed. Which condition enforces that policy?

A. `if len(checks):`  
B. `if sum(checks):`  
C. `if any(checks):`  
D. `if all(checks):`

### 26. Alerting when at least one account is overdue

**Difficulty:** Intermediate

The flags `[False, False, True, False]` represent overdue accounts. Which expression answers whether the alert service has at least one case to process?

A. `all(overdue)`  
B. `any(overdue)`  
C. `max(len(overdue))`  
D. `sorted(overdue)`

### 27. Selecting the shortest support ticket by message length

**Difficulty:** Intermediate

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

An outer function defines `format_row()` inside itself and uses it successfully. Later, unrelated code tries to call `format_row()` directly. Which result follows from that placement?

A. The helper runs because every nested definition is automatically copied into global scope when the outer function returns  
B. Python silently creates another helper outside the report  
C. The direct outside call raises `NameError` because the helper is local to the outer function  
D. The helper returns `None` only when called from outside

### 29. An inner helper uses its enclosing function's value

**Difficulty:** Intermediate

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

A sanitising helper is used only while building one confidential report and should not become part of the module's public collection of utilities. Which placement best communicates that design?

A. Define the sanitising helper inside the report-building function  
B. Duplicate the sanitising expression at every point of use  
C. Define it globally and rely on a comment asking others not to call it  
D. Store the helper name in a list instead of defining a function

### 31. A local calculation is requested after the call ends

**Difficulty:** Intermediate

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

### 36. Tracing the return journey of a recursive call

**Difficulty:** Intermediate

Using the `factorial` function from the previous scenario, which value is delivered by `factorial(4)` after the calls unwind?

A. `16`  
B. `24`  
C. `10`  
D. `120`

### 37. A recursive retry never approaches a stopping case

**Difficulty:** Advanced

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

A team wants `help(calculate_total)` to show a concise explanation of the function. Where should the explanatory string be placed?

A. As the first statement inside the function body  
B. After every call to the function  
C. Before `def`, assigned to a module variable that happens to use the same function name  
D. Inside the return expression after the result

### 39. Interpreting type hints during execution

**Difficulty:** Intermediate

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
| 2 | D | Intermediate | Separating the workflow by responsibility makes each part independently understandable and testable. |
| 3 | A | Advanced | Centralising the calculation removes duplicated policy logic without preventing a caller from managing its own presentation. |
| 4 | C | Foundational | A `def` statement creates the function object; its body runs only when the function is called. |
| 5 | A | Intermediate | The loop performs three calls, while the reusable body remains defined in one place. |
| 6 | D | Advanced | Python must execute the definition before it can resolve and call `prepare` at module level. |
| 7 | B | Foundational | A parameter is the placeholder in the definition, and an argument is the value supplied during a call. |
| 8 | C | Intermediate | `900 / 3` returns `300.0`; adding 25 produces `325.0`. |
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
| 36 | B | Intermediate | The calls unwind as `4 * 3 * 2 * 1`, which equals 24. |
| 37 | D | Advanced | Starting at 3 and adding 1 never reaches 0, so calls accumulate until Python's recursion limit is exceeded. |
| 38 | A | Intermediate | A string literal placed first in the function body becomes its docstring and is surfaced by `help`. |
| 39 | B | Intermediate | Annotations do not enforce runtime types by themselves; string multiplication therefore returns `haha`. |
| 40 | C | Intermediate | Focused functions isolate responsibilities, while a small coordinator can preserve the overall order workflow. |

---

## Topic coverage

| Unit 8 topic | Questions |
|---|---|
| Why Functions: Reuse and Decomposition | 1-3 |
| Defining and Calling Functions | 4-6 |
| Parameters, Arguments, and Return Values | 7-11 |
| Default, Keyword, and Positional Arguments | 12-15 |
| `*args` and `**kwargs` | 16-18 |
| Lambda | 19-21 |
| `map`, `filter`, and `reduce` | 22-24 |
| Useful Built-ins | 25-27 |
| Nested Functions | 28-30 |
| Scope and LEGB | 31-34 |
| Recursion | 35-37 |
| Docstrings and Clean Function Design | 38-40 |
