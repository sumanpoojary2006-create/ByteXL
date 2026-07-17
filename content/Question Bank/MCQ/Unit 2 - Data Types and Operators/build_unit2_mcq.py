import random
import openpyxl

random.seed(17)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])
SET1 = [
    # 2.1.1 Easy — Variables and Case Sensitivity
    (
        "A college admin portal stores student names for two different database tables — one for internal records and one for a public-facing leaderboard. A developer on the team writes:\n\n```python\nstudent_name = \"Riya Sharma\"\nStudent_Name = \"Ananya Verma\"\n```\n\nA junior teammate insists both variables point to the same memory location and will conflict. The senior developer disagrees. What does `print(student_name)` produce?",
        "Python is case-sensitive. `student_name` and `Student_Name` are entirely different variables. `print(student_name)` prints `Riya Sharma`. The junior's assumption is a misconception carried over from case-insensitive languages.",
        "easy", "understand", "variables-and-case-sensitivity",
        "`Riya Sharma` — Python is case-sensitive; these are two distinct variables",
        ["`Ananya Verma` — Python treats similarly spelled names as the same variable", "A `NameError` — two variables with similar names cannot coexist", "`Riya SharmaAnanya Verma` — Python merges values of similar names"],
    ),
    # 2.1.2 Easy — int and float, dynamic typing
    (
        "A canteen billing system initially sets the price of a meal as a whole number. Mid-semester, a partial subsidy changes it to a decimal. A student reviewing the code is confused about whether reassigning a variable to a different type is legal in Python.\n\n```python\nprice = 40\nprice = 36.5\n```\n\nWhat is `type(price)` after the second line, and does Python allow this?",
        "Python is dynamically typed. A variable's type is determined by its current value, not declared upfront. When `price = 36.5` runs, Python reassigns `price` to a `float`. The earlier `int` binding is simply discarded. This is legal and fundamental to Python.",
        "easy", "understand", "dynamic-typing",
        "`float` — Python allows reassignment to a new type; this is valid",
        ["`int` — Python keeps the original type and truncates `36.5` to `36`", "`str` — Python converts decimals to strings to avoid type conflict", "Python raises a `TypeError` — variables cannot change type after declaration"],
    ),
    # 2.1.3 Easy — Type Conversion
    (
        "A government scholarship portal collects a student's family income through a web form. All inputs arrive as strings. An intern writes the following to check if the family qualifies for the highest aid tier:\n\n```python\nincome = \"180000\"\nif income < 200000:\n    print(\"Eligible for full scholarship\")\n```\n\nThe intern is surprised by an error. What went wrong?",
        "Web form inputs always arrive as strings. `\"180000\" < 200000` attempts to compare a `str` with an `int`, which Python 3 does not allow — it raises a `TypeError`. The fix is `int(income) < 200000`.",
        "easy", "analyze", "type-conversion",
        "`income` is a string; comparing `str` to `int` raises a `TypeError`",
        ["The `if` syntax is wrong — `== True` must be added at the end", "The `<` operator does not work with numbers above 100,000", "String variables must be declared with `str()` before use in conditions"],
    ),
    # 2.1.4 Medium — Arithmetic, floor division and modulo
    (
        "A logistics startup assigns delivery orders to riders. At the end of each shift, the operations manager needs two numbers: how many complete batches of 6 orders each rider handled, and how many orders are left over. For a shift with 85 total orders, which pair of expressions gives both values correctly?",
        "`85 // 6 = 14` gives the number of complete batches (floor division). `85 % 6 = 1` gives the leftover orders. `/` returns `14.166...` — a float, not a usable batch count. One of the distractors lists the two values in the wrong order relative to the question asked.",
        "medium", "apply", "arithmetic-operators",
        "`85 // 6` and `85 % 6`",
        ["`85 / 6` and `85 - 6`", "`85 % 6` and `85 // 6`", "`85 / 6` and `85 % 6`"],
    ),
    # 2.1.5 Medium — Comparison Operators, boundary conditions
    (
        "An online exam platform lets students reattempt a paper only if their previous score was strictly below 40. A student who scored exactly 40 finds they cannot reattempt. The coordinator then updates the rule: reattempt is now allowed for scores of 40 and below. Which single change to the condition implements this correctly?\n\n```python\nscore = 40\nif score < 40:   # original\n```",
        "`score < 40` excludes exactly 40. The updated rule includes 40, so `<=` is correct. `!=` would wrongly allow reattempt for any score that is not 40, including those above it. `==` only matches exactly 40, excluding lower failing scores.",
        "medium", "apply", "comparison-operators",
        "Change `<` to `<=`",
        ["Change `<` to `!=`", "Change `<` to `==`", "Change `<` to `>`"],
    ),
    # 2.1.6 Medium — Logical Operators
    (
        "A hostel Wi-Fi system grants access only if a student's fee payment is complete AND they have not received a disciplinary warning this semester. A developer tests it with a student who has paid but has a warning:\n\n```python\nfee_paid = True\nwarning_received = True\naccess = fee_paid and not warning_received\n```\n\nThe developer expects `access` to be `True` since the fee is paid. What is `access` actually, and why?",
        "`not warning_received` → `not True` → `False`. Then `True and False` → `False`. `and` requires both sides to be `True`. The developer's expectation is wrong — access is correctly denied because of the outstanding warning.",
        "medium", "apply", "logical-operators",
        "`False` — `not warning_received` evaluates to `False`, so access is denied",
        ["`True` — `fee_paid` being `True` is sufficient; the second condition is ignored", "`True` — `not` applies to the entire expression, not just `warning_received`", "`False` — `and` always returns `False` when either operand involves `not`"],
    ),
    # 2.1.7 Medium — Operator Precedence
    (
        "A teacher writes the following expression on the board during a Python class to calculate a weighted score:\n\n```python\nresult = 10 + 4 * 3 ** 2 - 6 / 2\n```\n\nTwo students debate the answer. Kiran says `43.0`. Meena says `34.0` because she reads left to right. Who is correct?",
        "Precedence order: `3**2 = 9`, then `4*9 = 36`, then `6/2 = 3.0`, then `10 + 36 - 3.0 = 43.0`. Meena's left-to-right reading would give a different incorrect result. Kiran is right.",
        "medium", "apply", "operator-precedence",
        "Kiran — Python follows precedence: `**` → `*` → `/` → `+/-`",
        ["Meena — Python evaluates expressions strictly left to right", "Both are wrong — mixing `int` and `float` raises an error in Python", "Meena — division is always resolved before multiplication"],
    ),
    # 2.1.8 Medium — Augmented Assignment
    (
        "A freelance developer builds a task tracker for a design agency. Each completed task adds ₹1,200 to the client's invoice. A new intern claims `+=` doesn't actually update the variable and insists on writing `total = total + 1200` explicitly each time. After 5 tasks starting from ₹0, what is the final value of `total` using `+=`, and is the intern correct?\n\n```python\ntotal = 0\ntotal += 1200  # repeated 5 times\n```",
        "`+=` is augmented assignment — `total += 1200` is exactly `total = total + 1200`. After 5 operations from `0`, total reaches `6000`. The intern's concern is unfounded.",
        "medium", "apply", "augmented-assignment",
        "`total` is `6000` — `+=` is valid shorthand and the intern is wrong",
        ["`total` is `0` — the intern is right, `+=` doesn't modify the variable", "`total` is `1200` — `+=` resets the value each time rather than accumulating", "`total` is `5` — `+=` counts the number of times it was applied"],
    ),
    # 2.1.9 Hard — f-strings, format specifiers
    (
        "A placement cell generates offer letter summaries. CTC is stored in lakhs. The coordinator wants the value displayed with exactly 2 decimal places, and also asks whether arithmetic can be done inside the f-string to avoid creating a new variable. The developer writes:\n\n```python\nname = \"Sneha Reddy\"\nctc = 8\nprint(f\"{name} has been offered ₹{ctc:.2f} LPA\")\n```\n\n`ctc` is now an integer, not a float. What is printed?",
        "`:.2f` works on both `int` and `float`. Python converts the integer to its float representation and applies the 2-decimal format. `8` becomes `8.00`. No error is raised.",
        "hard", "analyze", "fstrings-format-specifiers",
        "`Sneha Reddy has been offered ₹8.00 LPA`",
        ["`Sneha Reddy has been offered ₹8 LPA` — `:.2f` is ignored for integers", "A `ValueError` — `:.2f` only works with float variables", "`Sneha Reddy has been offered ₹8.0 LPA`"],
    ),
    # 2.1.10 Hard — input(), type and concatenation trap
    (
        "A student demonstrates a fee calculator to the class. The program collects the number of students and the fee per student, then prints the total. The admin enters `120` and `5000` during the demo. The student is shocked by the output:\n\n```python\nstudents = input(\"Number of students: \")\nfee = input(\"Fee per student: \")\ntotal = students + fee\nprint(\"Total fee collected: ₹\", total)\n```\n\nWhat is actually printed, and what is the root cause?",
        "`input()` always returns a string. `\"120\" + \"5000\"` is string concatenation, producing `\"1205000\"`. The fix is to wrap both with `int()` before adding.",
        "hard", "analyze", "input-type-trap",
        "`Total fee collected: ₹ 1205000` — `+` on two strings concatenates them",
        ["`Total fee collected: ₹ 600000` — `input()` auto-converts numeric entries to `int`", "`Total fee collected: ₹ 120` — Python uses only the first `input()` value", "A `TypeError` — the `+` operator does not work between two `input()` results"],
    ),
]

SET2 = [
    # 2.2.1 Easy — Naming Conventions, PEP 8
    (
        "During a code review at a college analytics startup, a tech lead flags one variable name as violating PEP 8 conventions, even though it runs without error. Which of these, used as a plain variable (not a class), would be flagged?",
        "PEP 8 specifies that regular variable names should use `snake_case`. `StudentGrade` uses `CamelCase`, which PEP 8 reserves for class names. The other three correctly follow snake_case.",
        "easy", "understand", "naming-conventions-pep8",
        "`StudentGrade`",
        ["`total_marks`", "`pass_count`", "`average_score`"],
    ),
    # 2.2.2 Easy — int and float, type promotion
    (
        "A hospital pharmacy system calculates a patient's bill. Tablet count is stored as an integer and price per tablet as a float. A billing clerk asks why the total always shows a decimal even when it seems like a whole number.\n\n```python\ntablets = 10\nprice_per_tablet = 2.5\ntotal = tablets * price_per_tablet\n```\n\nWhat is `total`, and what explains the decimal?",
        "When `int` and `float` are used in arithmetic, Python promotes the result to `float`. `10 * 2.5 = 25.0`, not `25`. The clerk's observation is correct — it is intentional Python behaviour.",
        "easy", "understand", "type-promotion",
        "`25.0` — mixing `int` and `float` produces a `float`",
        ["`25` — result is `int` since `tablets` is an `int`", "`25` — Python rounds to a whole number when one operand divides evenly", "`\"25.0\"` — Python converts to string when mixing types"],
    ),
    # 2.2.3 Easy — Strings and Booleans
    (
        "A startup's employee onboarding tool stores each employee's display name and their active status. A new developer asks what types these variables are:\n\n```python\nemp_name = \"Kavitha Nair\"\nis_active = False\n```\n\n`emp_name` is of type ______ and `is_active` is of type ______.",
        "Any value enclosed in quotes is a `str`. `False` is a boolean literal of type `bool`. Although `bool` is a subclass of `int` internally, `type(False)` returns `<class 'bool'>`.",
        "easy", "understand", "strings-and-booleans",
        "`str`, `bool`",
        ["`str`, `int`", "`str`, `str`", "`int`, `bool`"],
    ),
    # 2.2.4 Easy — Type Conversion, division always returns float
    (
        "A school's attendance system reads total working days from a config file as the string `\"60\"`. A developer converts it and computes the attendance percentage:\n\n```python\nworking_days = int(\"60\")\npresent = 45\npercentage = present / working_days * 100\n```\n\nA teacher asks: \"Is `percentage` a whole number or a decimal?\" What is the correct answer?",
        "In Python 3, `/` always returns a `float` regardless of whether the operands are integers. `45 / 60 * 100 = 75.0`, not `75`. Use `//` if an integer result is needed.",
        "easy", "understand", "type-conversion",
        "A decimal — `/` in Python 3 always returns a `float`",
        ["A whole number — both `present` and `working_days` are integers after conversion", "A whole number — `* 100` converts the result back to integer", "A decimal — the original `\"60\"` was a string, so the result inherits that"],
    ),
    # 2.2.5 Easy — Arithmetic, modulo for cycling
    (
        "A hostel warden assigns room numbers in a repeating cycle of 1 through 8. The room position for a student is determined by their serial number using modulo. Student serial number 25 is being processed. Which expression and result are correct?",
        "`25 % 8 = 1` — 8 goes into 25 three times with remainder 1. Modulo gives the remainder, which is what a cycling room assignment needs. `25 // 8 = 3` gives the cycle count, not the room position.",
        "easy", "apply", "arithmetic-operators",
        "`25 % 8` → `1`",
        ["`25 // 8` → `3`", "`25 / 8` → `3.125`", "`25 % 8` → `3`"],
    ),
    # 2.2.6 Medium — Comparison, equality vs boundary
    (
        "A competitive coding platform awards a Gold Badge for more than 100 problems solved and a Silver Badge for exactly 100. A user has solved exactly 100 problems. What are the values of `gold` and `silver`?\n\n```python\nproblems_solved = 100\ngold = problems_solved > 100\nsilver = problems_solved == 100\n```",
        "`100 > 100` is `False` — the user does not qualify for Gold. `100 == 100` is `True` — they qualify for Silver. The boundary between `>` and `==` is exactly what this question tests.",
        "medium", "apply", "comparison-operators",
        "`gold = False`, `silver = True`",
        ["`gold = True`, `silver = True`", "`gold = True`, `silver = False`", "`gold = False`, `silver = False`"],
    ),
    # 2.2.7 Medium — Logical Operators, and/or combination
    (
        "A Bengaluru EdTech platform offers a free trial to users who are either students OR referred by an existing member — but in both cases, they must not have a previously banned account. A developer writes:\n\n```python\nis_student = False\nis_referred = True\nis_banned = False\n\ntrial_eligible = (is_student or is_referred) and not is_banned\n```\n\nA QA tester claims the condition is wrong and will incorrectly block this user. Is the tester right?",
        "`is_student or is_referred` → `False or True` → `True`. `not is_banned` → `not False` → `True`. `True and True` → `True`. The user is a referred, non-banned user — trial access is correctly granted. The tester is wrong.",
        "medium", "analyze", "logical-operators",
        "No — the logic evaluates correctly to `True`; the tester is wrong",
        ["Yes — `or` must be replaced with `and` for the rule to work correctly", "Yes — `not is_banned` should be written as `is_banned == False` to work", "No — but the result is `False`, so access is actually denied"],
    ),
    # 2.2.8 Medium — Augmented Assignment, tracing
    (
        "A mobile recharge app tracks a user's wallet. The user starts with ₹500, recharges ₹200, buys a data pack for ₹149, then receives a ₹30 cashback. The developer traces the wallet:\n\n```python\nbalance = 500\nbalance += 200\nbalance -= 149\nbalance += 30\n```\n\nThe developer claims the final balance is ₹611. What is it actually, and is the developer right?",
        "`500 + 200 = 700`, `700 - 149 = 551`, `551 + 30 = 581`. The augmented operators work correctly and chain. The developer's code logic is right, but their stated answer of ₹611 is a manual arithmetic mistake.",
        "medium", "apply", "augmented-assignment",
        "₹581 — the code is correct but the developer made an arithmetic error",
        ["₹581 — the developer's code is wrong; augmented operators don't chain", "₹611 — the developer is correct", "₹500 — augmented operators don't persist across lines"],
    ),
    # 2.2.9 Medium — Operator Precedence, mixed arithmetic
    (
        "A data science intern at a Pune analytics firm computes a normalised placement score:\n\n```python\nscore = 5 + 2 ** 3 * 4 / 8 - 1\n```\n\nHer manager says the result is `8.0`. The intern says it's `9.0`. Who is right?",
        "`2**3 = 8`, `8 * 4 = 32`, `32 / 8 = 4.0`, `5 + 4.0 - 1 = 8.0`. The manager is correct. The intern likely misapplied the precedence order.",
        "medium", "apply", "operator-precedence",
        "The manager — the result is `8.0`",
        ["The intern — the result is `9.0`", "Neither — Python raises a `ZeroDivisionError`", "Neither — the result is `12.0`"],
    ),
    # 2.2.10 Medium — type() and Conversion
    (
        "A health-tech startup processes blood pressure readings that arrive from a medical device as strings. Before running calculations, a developer confirms the type after conversion:\n\n```python\nreading = \"120\"\nconverted = float(reading)\nprint(type(converted) == float)\n```\n\nWhat does this print?",
        "`float(\"120\")` converts `\"120\"` to `120.0`. `type(120.0) == float` compares type objects directly — this is valid Python. The result is `True`. `type()` returns a type object, and `==` works correctly with type comparisons.",
        "medium", "apply", "type-conversion",
        "`True` — `float()` converts the string and the type check passes",
        ["`False` — `float(\"120\")` produces an `int` since `\"120\"` has no decimal point", "`False` — `type()` returns a string like `\"float\"`, not a type object", "An error — `type()` output cannot be compared using `==`"],
    ),
    # 2.2.11 Medium — input(), division on strings
    (
        "Two students test a Python script to split a restaurant bill. They enter `1200` and `4` when prompted. The output surprises them:\n\n```python\ntotal = input(\"Total bill: \")\npeople = input(\"Number of people: \")\nprint(\"Each person pays: ₹\", total / people)\n```\n\nWhat actually happens when this runs?",
        "`input()` returns strings. `total = \"1200\"` and `people = \"4\"`. The `/` operator cannot divide two strings — it raises a `TypeError`. The fix is `int(input(...))` for both.",
        "medium", "analyze", "input-type-trap",
        "It raises a `TypeError` — you cannot divide two strings",
        ["It prints `Each person pays: ₹ 300.0`", "It raises a `ValueError` — `input()` cannot accept numbers", "It prints `Each person pays: ₹ 12004`"],
    ),
    # 2.2.12 Medium — f-strings, expressions and format specifiers
    (
        "A placement coordinator wants to display a student's CTC in rupees without creating a separate variable for the conversion. CTC is stored in lakhs as a float. The coordinator asks the developer: \"Can we do the multiplication inside the f-string itself?\"\n\n```python\nname = \"Rohit Verma\"\nctc_lakhs = 12.5\nprint(f\"{name}'s CTC is ₹{ctc_lakhs * 100000:.0f}\")\n```\n\nWhat is printed?",
        "f-strings allow full Python expressions inside `{}`. `12.5 * 100000 = 1250000.0`, and `:.0f` formats it with zero decimal places, giving `1250000`. The output is `Rohit Verma's CTC is ₹1250000`.",
        "medium", "apply", "fstrings-format-specifiers",
        "`Rohit Verma's CTC is ₹1250000`",
        ["`Rohit Verma's CTC is ₹12.5`", "`Rohit Verma's CTC is ₹12500000.0`", "An error — arithmetic is not allowed inside f-string `{}`"],
    ),
    # 2.2.13 Medium — Boolean, truthiness of zero
    (
        "A quiz app tracks whether a student has attempted a question using an integer score: `0` if unattempted, any positive value if attempted. A developer writes:\n\n```python\nscore = 0\nif score:\n    print(\"Attempted\")\nelse:\n    print(\"Not attempted\")\n```\n\nA teammate argues this is wrong because `score` is an integer, not a boolean, and `if` only works with `True` or `False`. What is printed, and is the teammate right?",
        "In Python, `0` is falsy. `if score:` with `score = 0` evaluates to `False`, so the `else` branch runs. The teammate is wrong — `if` accepts any value and Python defines clear truthiness rules for all built-in types.",
        "medium", "understand", "truthiness",
        "`Not attempted` — `0` is falsy in Python; the teammate is wrong",
        ["`Attempted` — `0` is truthy since it is a defined, non-`None` value", "Nothing — the condition is skipped when the value is an integer", "A `TypeError` — `if` requires a boolean expression"],
    ),
    # 2.2.14 Medium — Arithmetic, exponentiation and parentheses
    (
        "A finance team computes the maturity value of a fixed deposit using `P × (1 + r)^n`. Two versions of the code are on the screen:\n\n```python\n# Version A\nmaturity_a = 50000 * 1 + 0.07 ** 5\n\n# Version B\nmaturity_b = 50000 * (1 + 0.07) ** 5\n```\n\nP = ₹50,000, r = 0.07, n = 5. Which version is correct, and why?",
        "In Version A, precedence applies `0.07 ** 5` first (≈ 0.0000000168), then `50000 * 1 = 50000`, then adds the tiny value — giving roughly ₹50,000. Wrong formula. Version B uses parentheses to compute `1.07 ** 5 ≈ 1.4026`, then `50000 * 1.4026 ≈ ₹70,128`. Version B is correct.",
        "medium", "analyze", "operator-precedence",
        "Version B — parentheses force `(1 + 0.07)` before exponentiation",
        ["Version A — `*` is evaluated before `**`, so the formula order is correct", "Both are equivalent — parentheses don't change the result here", "Version A — result is approximately ₹50,001 and matches the FD formula"],
    ),
    # 2.2.15 Hard — Comparison, assignment in condition
    (
        "During a code review at a fintech company, a reviewer flags the following snippet from a PIN verification module:\n\n```python\nentered_pin = \"1234\"\nif entered_pin = \"1234\":\n    print(\"Access granted\")\n```\n\nThe developer insists it should work. What actually happens?",
        "Using `=` inside an `if` condition is a `SyntaxError` in Python. `=` is the assignment operator; Python does not permit it where an expression is expected. The developer must use `==`. This is one of the most common bugs beginners carry from mathematical notation.",
        "hard", "analyze", "comparison-operators",
        "It raises a `SyntaxError` — `=` is not valid in a condition; use `==`",
        ["It prints `Access granted` — `=` and `==` are interchangeable inside `if` conditions", "It prints nothing — `=` returns `None`, which is falsy", "It raises a `TypeError` — strings cannot be compared using `=`"],
    ),
    # 2.2.16 Hard — Type Conversion, int() on a decimal string
    (
        "A data pipeline at an ed-tech company receives student ratings like `\"4.8\"` as strings from an API. A developer writes:\n\n```python\nrating = int(\"4.8\")\n```\n\nA senior developer immediately says it will fail. The junior disagrees, saying `4.8` is clearly a number. Who is right?",
        "`int()` cannot directly parse a string containing a decimal point — it raises a `ValueError`. The correct approach is `int(float(\"4.8\"))`, which gives `4`. Note that `int(\"4\")` (no decimal point) works fine; the issue is specifically the decimal point in the string.",
        "hard", "analyze", "type-conversion",
        "The senior — `int()` cannot parse a decimal string; raises `ValueError`",
        ["The junior — `int()` handles decimal strings by truncating to `4`", "The junior — `int(\"4.8\")` silently drops the decimal and returns `4`", "The senior — `int()` cannot handle any string containing a numeric value"],
    ),
    # 2.2.17 Hard — Operator Precedence, logical operators
    (
        "A smart gate at a corporate office opens only if the employee badge is valid AND the person either has a scheduled meeting OR is an authorised visitor. A developer writes:\n\n```python\nbadge_valid = False\nhas_meeting = False\nis_authorised = True\n\ngate_open = badge_valid and has_meeting or is_authorised\n```\n\nThe security team notices the gate opens even when `badge_valid` is `False`. Is this a bug?",
        "`and` has higher precedence than `or`. The expression evaluates as `(False and False) or True` → `False or True` → `True`. The badge is never checked against `is_authorised`. The correct expression is `badge_valid and (has_meeting or is_authorised)`.",
        "hard", "analyze", "operator-precedence",
        "Yes — `and` binds tighter than `or`, bypassing the badge check entirely",
        ["No — authorised visitors should always be admitted regardless of badge status", "No — `or` binds tighter than `and`, so the full intended logic is preserved", "Yes — the expression always evaluates to `True` regardless of any input"],
    ),
    # 2.2.18 Hard — Floor division with negatives
    (
        "A scheduling system tracks days relative to the start of an academic year. A data migration from a legacy C-based system introduces a negative value: `days = -7`. A developer familiar with C expects `-7 // 2` to return `-3`. A Python developer says the result is different. Who is right?",
        "Python's `//` floors toward negative infinity. `-7 / 2 = -3.5`, and `floor(-3.5) = -4`. C truncates toward zero, giving `-3`. This difference causes subtle bugs when migrating numeric logic between languages.",
        "hard", "analyze", "arithmetic-operators",
        "The Python developer — Python floors toward negative infinity; result is `-4`",
        ["The C developer — Python and C agree on this; `-7 // 2` returns `-3`", "Neither — Python returns `-3.5` for floor division on negative numbers", "The Python developer — Python returns `0` for floor division of any negative number"],
    ),
    # 2.2.19 Hard — Augmented assignment, chained operations and tracing
    (
        "A student fee reconciliation system processes three adjustments to a base fee in sequence: a ₹500 penalty for a late payment, a ₹200 rebate for an early clearance, and a further ₹150 penalty for a missed deadline. Starting from a base fee of ₹10,000, what is the final value?\n\n```python\nfee = 10000\nfee += 500\nfee -= 200\nfee += 150\n```",
        "`10000 + 500 = 10500`, `10500 - 200 = 10300`, `10300 + 150 = 10450`. Augmented operators apply sequentially and do accumulate. The final fee is ₹10,450.",
        "hard", "apply", "augmented-assignment",
        "₹10,450",
        ["₹10,150", "₹10,500", "₹10,000 — augmented operators don't accumulate across multiple lines"],
    ),
    # 2.2.20 Hard — Combined operators, multi-condition tracing
    (
        "A rural microfinance app in Tamil Nadu auto-approves small loans if all three conditions hold: applicant is between 21 and 55 years old (inclusive), monthly income is at least ₹8,000, and no existing default on record. An applicant is 34 years old, earns ₹9,500/month, and has a recorded default.\n\n```python\nage = 34\nincome = 9500\nhas_default = True\n\napproved = 21 <= age <= 55 and income >= 8000 and not has_default\n```\n\nWhat is `approved`, and which condition causes the rejection?",
        "`21 <= 34 <= 55` → `True`. `9500 >= 8000` → `True`. `not has_default` → `not True` → `False`. `True and True and False` → `False`. The rejection is caused solely by the existing default record. Chained comparisons like `21 <= age <= 55` are valid Python and work as expected.",
        "hard", "analyze", "logical-operators",
        "`False` — `not has_default` is `False`, blocking approval",
        ["`True` — all three conditions are satisfied for this applicant", "`False` — monthly income does not meet the minimum ₹8,000 threshold", "`False` — the chained comparison `21 <= age <= 55` fails for age values above 30"],
    ),
]

assert len(SET1) == 10, len(SET1)
assert len(SET2) == 20, len(SET2)


def build_rows(items, set_label, title_prefix):
    positions = [(i % 4) + 1 for i in range(len(items))]
    random.shuffle(positions)

    rows = []
    for idx, (desc, expl, diff, bloom, subtopic, correct, distractors) in enumerate(items, start=1):
        pos = positions[idx - 1]
        options = distractors[:]
        options.insert(pos - 1, correct)
        rows.append({
            "title": f"{title_prefix}.{idx}",
            "description": desc,
            "explanation": expl,
            "score": 1,
            "status": "published",
            "difficulty": diff,
            "bloomTaxonomy": bloom,
            "tags": f"python - {set_label}",
            "subjects": "python",
            "topics": "data-types-and-operators",
            "subTopics": subtopic,
            "companies": None,
            "option1": options[0],
            "option2": options[1],
            "option3": options[2],
            "option4": options[3],
            "answer": pos,
        })
    return rows


rows1 = build_rows(SET1, "Set 1", "Python - MCQ - 2.1")
rows2 = build_rows(SET2, "Set 2", "Python - MCQ - 2.2")
all_rows = rows1 + rows2


def summarize(name, rs):
    diff, bloom, sub, ans = {}, {}, {}, {1: 0, 2: 0, 3: 0, 4: 0}
    for r in rs:
        diff[r["difficulty"]] = diff.get(r["difficulty"], 0) + 1
        bloom[r["bloomTaxonomy"]] = bloom.get(r["bloomTaxonomy"], 0) + 1
        sub[r["subTopics"]] = sub.get(r["subTopics"], 0) + 1
        ans[r["answer"]] += 1
    print(name, "diff:", diff)
    print(name, "bloom:", bloom)
    print(name, "subtopics:", sub)
    print(name, "answers:", ans)


summarize("SET1", rows1)
summarize("SET2", rows2)

descs = [r["description"] for r in all_rows]
assert len(descs) == len(set(descs)), "duplicate description found"
for r in all_rows:
    opts = [r["option1"], r["option2"], r["option3"], r["option4"]]
    assert len(set(opts)) == 4, f"duplicate option in {r['title']}: {opts}"

headers = ["title", "description", "explanation", "score", "status", "difficulty", "bloomTaxonomy",
           "tags", "subjects", "topics", "subTopics", "companies",
           "option1", "option2", "option3", "option4", "answer"]

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Python - MCQ - Unit 2"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/Unit 2 - Data Types and Operators/Unit 2 - Data Types and Operators - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
