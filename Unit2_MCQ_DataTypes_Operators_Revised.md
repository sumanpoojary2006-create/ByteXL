# Unit 2: Data Types and Operators

## SECTION A: COURSE MCQs (Set 1 — 10 Questions)

---

**Python - MCQ - 2.1.1**
**Difficulty:** Easy
**Tag:** Variables and Case Sensitivity
**Type:** Repair a failure

A warehouse program reads a product code correctly, but the label-printing step fails with a `NameError`:

```python
product_code = "BX-104"
print(Product_Code)
```

The value should remain unchanged. Which edit fixes the failure?

A) Convert the stored code using `product_code = str(product_code)`
B) Change the print statement to `print(product_code)`
C) Rename the stored value as `productCode` but leave `print(Product_Code)` unchanged
D) Replace the underscore in both names with a hyphen

**Answer:** B

**Explanation:** Python identifiers are case-sensitive. `product_code` exists, but `Product_Code` is a different, undefined name. Using the original identifier fixes the error without changing the stored value. `str()` cannot resolve an undefined name, and a hyphen is interpreted as subtraction rather than as part of an identifier.

---

**Python - MCQ - 2.1.2**
**Difficulty:** Easy
**Tag:** Dynamic Typing
**Type:** Trace a changing state

A delivery application first stores a parcel's weight as an estimated whole number. After a digital scale responds, the same variable is updated with a precise reading:

```python
weight = 12
weight = 12.75
```

Which statement is true immediately after the second assignment?

A) `weight` refers to a `float` value
B) `weight` remains an `int` with value `12`
C) Python stores both values together in a tuple
D) The reassignment fails because a variable's type is fixed

**Answer:** A

**Explanation:** Python is dynamically typed. A name can be rebound to a value of another type, so `weight` now refers to the float `12.75`. Python neither preserves the old value inside the variable nor combines the two assignments.

---

**Python - MCQ - 2.1.3**
**Difficulty:** Easy
**Tag:** Type Conversion
**Type:** Translate a requirement into code

A temperature sensor sends the text value `"27.5"`. The monitoring program must preserve the decimal reading and compare it numerically with the limit `30.0`.

Which conversion should be used?

A) `reading = int(float("27.5"))`
B) `reading = bool("27.5")`
C) `reading = str(27.5)`
D) `reading = float("27.5")`

**Answer:** D

**Explanation:** `float("27.5")` produces the numeric value `27.5`, which can be compared with `30.0`. `int("27.5")` raises a `ValueError` because the string contains a decimal point. The other conversions do not produce the required numeric reading.

---

**Python - MCQ - 2.1.4**
**Difficulty:** Easy
**Tag:** Floor Division and Modulo
**Type:** Translate a requirement into code

A bakery packs 95 muffins into boxes that hold 8 each. Its report must show the number of completely filled boxes first and the number of unpacked muffins second.

Which result pair is correct?

A) `11.875` complete boxes and `7` unpacked muffins
B) `7` complete boxes and `11` unpacked muffins
C) `11` complete boxes and `7` unpacked muffins
D) `11` complete boxes and `11.875` unpacked muffins

**Answer:** C

**Explanation:** `95 // 8` gives `11` complete boxes, while `95 % 8` gives `7` remaining muffins. Regular division gives `11.875`, which is not a count of completely filled boxes.

---

**Python - MCQ - 2.1.5**
**Difficulty:** Medium
**Tag:** Comparison Operators
**Type:** Select a boundary test

A streaming service enables a family plan when an account has **at least 4** profiles. The implementation is:

```python
family_plan = profile_count > 4
```

Which single test value most directly exposes the boundary bug?

A) `profile_count = 0`
B) `profile_count = 10`
C) `profile_count = 5`
D) `profile_count = 4`

**Answer:** D

**Explanation:** “At least 4” includes exactly `4`, but `4 > 4` is `False`. Testing the boundary value therefore exposes the error immediately. The condition should be `profile_count >= 4`. Values above 4 would not reveal the defect.

---

**Python - MCQ - 2.1.6**
**Difficulty:** Easy
**Tag:** Logical Operators
**Type:** Make the smallest correct change

A clinic releases a digital report only when the patient's identity is verified and the doctor has approved the report. The current expression releases a report when either condition is true:

```python
can_release = identity_verified or doctor_approved
```

Which minimal edit implements the stated rule?

A) Replace `or` with `not`
B) Replace `or` with `and`
C) Compare both values with `False`
D) Remove the `identity_verified` check

**Answer:** B

**Explanation:** The word “and” in the requirement means both conditions must be true. Replacing `or` with `and` prevents release when only one approval is present. The other changes either invert or remove a required check.

---

**Python - MCQ - 2.1.7**
**Difficulty:** Medium
**Tag:** Arithmetic Operator Precedence
**Type:** Compare competing implementations

A repair shop calculates a bill as a ₹500 service charge plus three parts costing ₹120 each. A 10% tax must then apply to the entire subtotal.

Which expression implements that policy?

A) `500 + 3 * 120 * 1.10`
B) `500 + (3 * 120) + (500 * 0.10)`
C) `(500 + 3 * 120) * 1.10`
D) `500 + (3 * 120 * 0.10)`

**Answer:** C

**Explanation:** `3 * 120` calculates the parts cost, and parentheses combine it with the service charge before multiplying the complete subtotal by `1.10`. Option A taxes only the parts component. Options B and D model different calculations.

---

**Python - MCQ - 2.1.8**
**Difficulty:** Easy
**Tag:** Augmented Assignment
**Type:** Trace a changing state

A game starts a player with 250 coins. The player buys an item for 80 coins, earns a 45-coin reward, and pays a 20-coin entry fee:

```python
coins = 250
coins -= 80
coins += 45
coins -= 20
```

What value is stored in `coins` at the end?

A) `115 coins`
B) `195 coins`
C) `205 coins`
D) `215.0 coins`

**Answer:** B

**Explanation:** The operations update the same value in sequence: `250 - 80 = 170`, `170 + 45 = 215`, and `215 - 20 = 195`. Augmented assignments do not reset the variable between lines.

---

**Python - MCQ - 2.1.9**
**Difficulty:** Medium
**Tag:** input() and Type Conversion
**Type:** Repair a failure

A ticket kiosk asks for the number of adult and child tickets. When the operator enters `2` and `3`, the screen displays `Tickets reserved: 23` instead of `5`.

```python
adults = input("Adult tickets: ")
children = input("Child tickets: ")
total = adults + children
print("Tickets reserved:", total)
```

Which repair correctly handles whole-number ticket counts?

A) `total = str(adults) + str(children)`
B) `total = float(adults + children)`
C) `total = bool(adults) + bool(children)`
D) `total = int(adults) + int(children)`

**Answer:** D

**Explanation:** `input()` returns strings, so `+` concatenates `"2"` and `"3"`. Converting each input separately with `int()` makes `+` perform numeric addition. Converting the already-concatenated text would produce `23`, not `5`.

---

**Python - MCQ - 2.1.10**
**Difficulty:** Hard
**Tag:** Logical Operator Precedence
**Type:** Design a test that exposes a bug

A secure download should be permitted only when a user is signed in **and** is either the file owner or an administrator. A developer omits the parentheses:

```python
allowed = signed_in and is_owner or is_admin
```

Which test case demonstrates that an unsigned administrator is incorrectly allowed?

A) `signed_in=False, is_owner=False, is_admin=True; expected=False`
B) `signed_in=True, is_owner=True, is_admin=False; expected=True`
C) `signed_in=True, is_owner=False, is_admin=True; expected=True`
D) `signed_in=False, is_owner=False, is_admin=False; expected=False`

**Answer:** A

**Explanation:** `and` is evaluated before `or`, so the expression is `(signed_in and is_owner) or is_admin`. With `False, False, True`, it becomes `False or True`, incorrectly allowing the download. The intended expression is `signed_in and (is_owner or is_admin)`.

---

## SECTION B: ASSESSMENT MCQs (Set 2 — 30 Questions)

---

**Python - MCQ - 2.2.1**
**Difficulty:** Easy
**Tag:** Numeric Types
**Type:** Trace a changing state

A fuel monitor stores litres as `18`, then adds a measured delivery of `2.5` litres:

```python
fuel = 18
fuel += 2.5
```

Which description of `fuel` is correct afterward?

A) It is the float `20.5`
B) It is the integer `20`
C) It remains the integer `18`
D) It becomes the string `"20.5"`

**Answer:** A

**Explanation:** Adding an `int` and a `float` produces a `float`. Augmented assignment stores the resulting `20.5` back in `fuel`.

---

**Python - MCQ - 2.2.2**
**Difficulty:** Medium
**Tag:** Type Conversion
**Type:** Repair a failure

An API supplies the rating `"4.8"`. The application must store only its whole-number portion as `4`, but this line fails:

```python
rating = int("4.8")
```

Which replacement works?

A) `rating = int(str(float("4.8")))`
B) `rating = bool("4.8")`
C) `rating = int(float("4.8"))`
D) `rating = float(int("4.8"))`

**Answer:** C

**Explanation:** `float("4.8")` first produces `4.8`; applying `int()` then truncates it to `4`. Directly passing a decimal string to `int()` raises `ValueError`.

---

**Python - MCQ - 2.2.3**
**Difficulty:** Easy
**Tag:** input()
**Type:** Translate a requirement into code

A stock counter reads a quantity from `input()`. It must add that quantity to the integer `stock`.

Which statement performs numeric addition?

A) `stock = stock + input("Quantity: ")`
B) `stock = str(stock) + input("Quantity: ")`
C) `stock = bool(stock) + input("Quantity: ")`
D) `stock = stock + int(input("Quantity: "))`

**Answer:** D

**Explanation:** `input()` returns text. Converting that text to `int` before addition makes both operands numeric.

---

**Python - MCQ - 2.2.4**
**Difficulty:** Easy
**Tag:** Modulo
**Type:** Translate a requirement into code

A rotating support schedule has 7 positions numbered `0` through `6`. After position `6`, the next position must be `0`.

Which expression advances `position` correctly?

A) `position = position // 7 + 1`
B) `position = (position + 1) % 7`
C) `position = position + 1 / 7`
D) `position = ((position % 7) + 1) % 8`

**Answer:** B

**Explanation:** Adding first and then taking modulo 7 maps `6` to `0` while advancing every other valid position normally.

---

**Python - MCQ - 2.2.5**
**Difficulty:** Medium
**Tag:** Negative Floor Division
**Type:** Compare competing implementations

A migration must reproduce Python's bucketing of offsets into groups of 4. Which result must a replacement system produce for `-9 // 4`?

A) `-3`, because Python floors toward negative infinity
B) `-2`, matching systems that discard the fractional part toward zero
C) `-2.25`, because `//` preserves the fraction
D) `3`, because a bucket index cannot be negative

**Answer:** A

**Explanation:** `-9 / 4` is `-2.25`; floor division moves down to the next integer, `-3`. It does not truncate toward zero.

---

**Python - MCQ - 2.2.6**
**Difficulty:** Medium
**Tag:** Chained Comparisons
**Type:** Make the smallest correct change

A pressure reading is safe only from 30 through 70, inclusive:

```python
safe = 30 < pressure < 70
```

Which minimal edit includes both permitted endpoints?

A) `30 == pressure == 70`
B) `30 != pressure != 70`
C) `30 <= pressure <= 70`
D) `30 >= pressure or pressure >= 70`

**Answer:** C

**Explanation:** Inclusive boundaries require `<=` on both sides. Python supports chained comparisons directly.

---

**Python - MCQ - 2.2.7**
**Difficulty:** Hard
**Tag:** Logical Precedence
**Type:** Repair a failure

A refund requires a receipt and either a damaged item or manager approval. This expression permits manager-approved refunds without a receipt:

```python
refund = has_receipt and is_damaged or manager_approved
```

Which repair matches the policy?

A) `has_receipt and is_damaged or (manager_approved and not has_receipt)`
B) `has_receipt or (is_damaged and manager_approved)`
C) `(has_receipt or is_damaged) and manager_approved`
D) `has_receipt and (is_damaged or manager_approved)`

**Answer:** D

**Explanation:** The receipt requirement applies to both permitted alternatives, so the alternatives must be grouped inside parentheses.

---

**Python - MCQ - 2.2.8**
**Difficulty:** Hard
**Tag:** Short-Circuit Evaluation
**Type:** Design a test that exposes a bug

A ratio is calculated only when `count` is nonzero:

```python
valid = count != 0 and total / count > 10
```

Which test best confirms that short-circuiting prevents division by zero?

A) `count=1, total=0`
B) `count=0, total=50`
C) `count=5, total=50`
D) `count=10, total=0`, which exercises an ordinary division path

**Answer:** B

**Explanation:** When `count != 0` is false, Python does not evaluate the division on the right side of `and`, preventing `ZeroDivisionError`.

---

**Python - MCQ - 2.2.9**
**Difficulty:** Medium
**Tag:** f-Strings
**Type:** Translate a requirement into code

A dashboard must display `completion = 0.876` as `87.6%` without changing the stored value.

Which f-string does this?

A) `f"{completion:.1%}"`
B) `f"{completion:.1f}%"`
C) `f"{completion * 100:%}"`
D) `f"{completion}%"` followed by rounding

**Answer:** A

**Explanation:** The `%` format specifier multiplies by 100 and adds the percent sign; `.1` keeps one decimal place.

---

**Python - MCQ - 2.2.10**
**Difficulty:** Medium
**Tag:** Boolean Conversion
**Type:** Make the smallest correct change

A configuration file contains Boolean settings as text. The current conversion unexpectedly enables the feature when the file contains `"False"`:

```python
raw = "False"
enabled = bool(raw)
```

Which replacement treats `"true"` in any letter case as enabled and every other value as disabled?

A) `enabled = bool(raw.lower())`
B) `enabled = raw == bool(True)`
C) `enabled = raw.lower() in ("true", "false")`
D) `enabled = raw.strip().lower() == "true"`

**Answer:** D

**Explanation:** Normalising whitespace and case before comparing with `"true"` implements the stated rule. `bool(raw)` only checks whether the string is empty, and membership in both words would incorrectly enable `"false"`.

---

**Python - MCQ - 2.2.11**
**Difficulty:** Medium
**Tag:** Exponentiation Precedence
**Type:** Compare competing implementations

A model must square the negative value `-3`, producing `9`. Which expression reliably represents that requirement?

A) `-3 ** 2`
B) `-(abs(3) ** 2)`
C) `(-3) ** 2`
D) `-3 * 2`

**Answer:** C

**Explanation:** Parentheses make `-3` the base. Without them, exponentiation occurs before unary minus and `-3 ** 2` produces `-9`.

---

**Python - MCQ - 2.2.12**
**Difficulty:** Medium
**Tag:** Augmented Assignment with Strings
**Type:** Trace a changing state

A tracking code is built in stages:

```python
code = "PK"
code += "-"
code += "204"
```

What is stored in `code`?

A) `"204-PK"`
B) `"PK-204"`
C) `"PK204"`
D) An integer conversion error

**Answer:** B

**Explanation:** For strings, `+=` concatenates the new text on the right in execution order.

---

**Python - MCQ - 2.2.13**
**Difficulty:** Medium
**Tag:** Type Conversion
**Type:** Make the smallest correct change

A device sends `"18"`, but the program fails at `reading + 2` because `reading` is text. Which smallest change fixes the arithmetic while retaining a whole-number result?

A) `result = int(reading) + 2`
B) `result = reading + "2"`
C) `result = str(reading) + str(2)`
D) `result = (type(reading) == int) + 2`

**Answer:** A

**Explanation:** `int(reading) + 2` converts the numeric text at the point where numeric addition is required.

---

**Python - MCQ - 2.2.14**
**Difficulty:** Medium
**Tag:** Error Classification
**Type:** Repair a failure

A login check contains:

```python
if entered_pin = saved_pin:
    print("Access granted")
```

How should the defect be classified?

A) `ValueError`, caused by converting an invalid PIN
B) `TypeError`, caused by comparing two strings
C) Logic error, because the condition is always false
D) `SyntaxError`, because comparison requires `==`

**Answer:** D

**Explanation:** Assignment with `=` is not valid in this condition. Equality comparison uses `==`.

---

**Python - MCQ - 2.2.15**
**Difficulty:** Medium
**Tag:** Numeric Conversion
**Type:** Design a test that exposes a bug

A billing import must preserve decimal prices, but a developer writes:

```python
price = int(float(raw_price))
```

Which test value exposes the unintended loss of the fractional part?

A) `raw_price = "10"`
B) `raw_price = "0"`
C) `raw_price = "12.75"`
D) `raw_price = "-300.00"`

**Answer:** C

**Explanation:** `float("12.75")` produces `12.75`, but the outer `int()` changes it to `12`. Whole-number test values would not reveal the data loss.

---

**Python - MCQ - 2.2.16**
**Difficulty:** Hard
**Tag:** Arithmetic Requirements
**Type:** Compare competing implementations

A courier charges ₹40 per complete 5 kg block, including a partially filled final block. Which expression computes the number of chargeable blocks for a positive integer `weight`?

A) `(weight + 4) // 5`
B) `weight // 5`
C) `weight % 5`
D) `weight / 5` rounded down afterward

**Answer:** A

**Explanation:** Adding `4` before floor division implements ceiling division for positive integers. For example, 6 kg becomes `10 // 5`, or 2 blocks.

---

**Python - MCQ - 2.2.17**
**Difficulty:** Easy
**Tag:** Division Result Type
**Type:** Trace a changing state

```python
items = 8
items = items / 2
```

Which assertion passes after the second line?

A) `type(items) == int`
B) `type(items) == float`
C) `items == "4.0"`
D) `isinstance(items, str) and items == "4.0"`

**Answer:** B

**Explanation:** In Python 3, `/` returns a float even when the mathematical result is a whole number, so `items` becomes `4.0`.

---

**Python - MCQ - 2.2.18**
**Difficulty:** Medium
**Tag:** f-String Expressions
**Type:** Translate a requirement into code

`price` stores `249.5`. A label must show the price after adding 18% tax, rounded to two decimal places, without assigning another variable.

Which placeholder is correct?

A) `{price + 18:.2f}`
B) `{price:.2f * 1.18}`
C) `{price * 1.18:.2f}`
D) `{str(price * 1.18):.2f}`

**Answer:** C

**Explanation:** Expressions are allowed inside braces, and `:.2f` formats their numeric result to two decimal places.

---

**Python - MCQ - 2.2.19**
**Difficulty:** Medium
**Tag:** Truthiness
**Type:** Make the smallest correct change

A form uses this check to reject an empty note:

```python
if note:
    save(note)
```

Whitespace-only input is still saved. Which smallest change rejects both empty and whitespace-only strings?

A) `if bool(note):`
B) `if note != "":`
C) `if len(note) > 0:`
D) `if note.strip():`

**Answer:** D

**Explanation:** `strip()` removes surrounding whitespace. The resulting empty string is falsy, while the other three checks still accept a string containing only spaces.

---

**Python - MCQ - 2.2.20**
**Difficulty:** Medium
**Tag:** Boundary Comparisons
**Type:** Select a boundary test

A discount applies to totals from ₹1,000 through ₹5,000 inclusive. The code uses `1000 < total < 5000`.

Which compact test set exposes both boundary defects?

A) `total=1000` and `total=5000`
B) `total=999` and `total=5001`
C) `total=2000` and `total=4000`
D) `total=-10000` and `total=50000`

**Answer:** A

**Explanation:** The two exact endpoints should qualify but are rejected by strict `<` comparisons.

---

**Python - MCQ - 2.2.21**
**Difficulty:** Medium
**Tag:** Compound Logical Expressions
**Type:** Translate a requirement into code

A shipment may leave only if payment is confirmed and either customs is cleared or the shipment is domestic.

Which expression represents the rule?

A) `(paid and customs_cleared) or (domestic and not customs_cleared)`
B) `paid and (customs_cleared or domestic)`
C) `(paid or customs_cleared) and domestic`
D) `paid or (customs_cleared and domestic)`

**Answer:** B

**Explanation:** Payment is mandatory in both cases; the other two conditions are alternatives and must be grouped.

---

**Python - MCQ - 2.2.22**
**Difficulty:** Medium
**Tag:** Modulo
**Type:** Make the smallest correct change

A 24-hour clock advances an hour with `hour += 1`, but becomes `24` after `23`. Which replacement keeps the value in `0`–`23`?

A) `hour = hour // 24 + 1`
B) `hour = (hour % 23) + (1 if hour < 23 else 0)`
C) `hour = (hour + 1) % 24`
D) `hour = (hour + 24) // 24`

**Answer:** C

**Explanation:** Modulo 24 wraps the incremented value from 24 back to 0.

---

**Python - MCQ - 2.2.23**
**Difficulty:** Hard
**Tag:** Operator Precedence
**Type:** Design a test that exposes a bug

A rule should approve only active premium users or active staff members:

```python
approved = active and premium or staff
```

Which test exposes that `active` is not being required for staff?

A) `active=True, premium=True, staff=False; expected=True` — positive control
B) `active=True, premium=False, staff=False; expected=False` — ordinary denial control
C) `active=False, premium=True, staff=False; expected=False` — inactive premium control
D) `active=False, premium=False, staff=True; expected=False` — inactive staff test

**Answer:** D

**Explanation:** The expression is evaluated as `(active and premium) or staff`, so a true `staff` value bypasses the active check.

---

**Python - MCQ - 2.2.24**
**Difficulty:** Easy
**Tag:** Numeric Conversion
**Type:** Compare competing implementations

A measurement string may contain surrounding spaces, such as `" 42 "`. Which implementation safely converts this example to an integer?

A) `int(" 42 ")`
B) `bool(" 42 ")`
C) `str(int) + " 42 "`
D) `int(" 42 ".replace("4", ""))`

**Answer:** A

**Explanation:** `int()` accepts leading and trailing whitespace around a valid integer literal and returns `42`.

---

**Python - MCQ - 2.2.25**
**Difficulty:** Medium
**Tag:** Augmented Assignment
**Type:** Trace a changing state

```python
value = 10
value *= 3
value //= 4
value **= 2
```

What is the final value?

A) `49.0`
B) `49`
C) `56`
D) `64`

**Answer:** B

**Explanation:** The successive values are `30`, `7`, and `49`. Floor division of two integers produces an integer here.

---

**Python - MCQ - 2.2.26**
**Difficulty:** Medium
**Tag:** Conversion and Arithmetic
**Type:** Repair a failure

A checkout receives `quantity="3"` and `price="19.5"`. Which calculation produces the numeric total `58.5`?

A) `int(quantity) * int(price)`
B) `quantity * float(price)`
C) `int(quantity) * float(price)`
D) `float(quantity + price) * 1.0`

**Answer:** C

**Explanation:** Quantity is valid integer text and price is decimal text, so each must be converted to its appropriate numeric type before multiplication.

---

**Python - MCQ - 2.2.27**
**Difficulty:** Hard
**Tag:** Logical Negation
**Type:** Make the smallest correct change

A warning should appear when a device is not online and not in maintenance. The current expression is:

```python
warning = not (online and maintenance)
```

Which replacement matches the requirement exactly?

A) `not online or (maintenance is False)`
B) `online and not maintenance`
C) `not online and maintenance`
D) `not online and not maintenance`

**Answer:** D

**Explanation:** Both negative conditions are required simultaneously. The original expression is also true when only one of them is false.

---

**Python - MCQ - 2.2.28**
**Difficulty:** Medium
**Tag:** Numeric Operators
**Type:** Translate a requirement into code

A report must split `seconds` into complete minutes and remaining seconds. Which assignment produces both values in that order?

A) `minutes, remaining = seconds // 60, seconds % 60`
B) `minutes, remaining = seconds / 60, seconds % 60`
C) `minutes, remaining = seconds % 60, seconds // 60`
D) `minutes, remaining = seconds // 60, (seconds / 60) % 60`

**Answer:** A

**Explanation:** Floor division counts complete minutes, while modulo returns the seconds left after those minutes.

---

**Python - MCQ - 2.2.29**
**Difficulty:** Hard
**Tag:** Type and Value Reasoning
**Type:** Compare competing implementations

Two implementations calculate half of an integer count:

```python
a = count / 2
b = count // 2
```

For which input do they have equal numeric values but different types?

A) `count = 1`
B) `count = -1`
C) `count = 8`
D) No integer input can do this

**Answer:** C

**Explanation:** With `8`, `a` is `4.0` and `b` is `4`. They compare equal numerically, but their types are `float` and `int`.

---

**Python - MCQ - 2.2.30**
**Difficulty:** Medium
**Tag:** Combined Operators
**Type:** Design a test that exposes a bug

A booking is valid when `seats` is from 1 to 6 inclusive and `balance` is at least `seats * 250`. The code mistakenly uses `seats < 6`:

```python
valid = 1 <= seats < 6 and balance >= seats * 250
```

Which test isolates the upper-bound defect while satisfying the payment rule?

A) `seats=0, balance=0; expected=False`
B) `seats=6, balance=1500; expected=True`
C) `seats=7, balance=1750; expected=False`
D) `seats=6, balance=1000; expected=False`

**Answer:** B

**Explanation:** Six seats should be permitted and ₹1,500 exactly satisfies the payment requirement. The test fails only because the upper comparison incorrectly excludes 6.

---
