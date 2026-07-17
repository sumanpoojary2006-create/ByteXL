import random
import openpyxl

random.seed(17)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])
SET1 = [
    # 3.1.1 Easy — Truthiness in Conditions
    (
        "A college attendance portal checks whether a student has submitted their name before processing records. The developer avoids an explicit comparison and writes:\n\n```python\nname = \"\"\nif name:\n    print(\"Processing record for\", name)\nelse:\n    print(\"Name not provided.\")\n```\n\nA junior teammate says this will crash because `name` is not a boolean. What actually happens, and why?",
        "In Python, an empty string `\"\"` is falsy. The `if name:` check evaluates to `False`, so the `else` branch runs. The junior's concern is wrong — `if` accepts any value; Python's truthiness rules apply automatically.",
        "easy", "understand", "truthiness-in-conditions",
        "It prints `Name not provided.` — empty strings are falsy",
        ["It crashes — `if` requires an explicit `== True` or `== False`", "It prints `Processing record for` — empty strings are truthy in Python", "It prints nothing — the `else` branch is only reachable after a preceding `elif`"],
    ),
    # 3.1.2 Easy — Fill the condition, if-else
    (
        "A college hostel allocates AC rooms only to students who have paid a premium fee of more than ₹80,000. The warden's assistant is writing the allocation check. Which condition correctly implements this rule?\n\n```python\nfee_paid = 85000\nif ________:\n    print(\"AC room allocated\")\nelse:\n    print(\"Standard room allocated\")\n```",
        "The rule says \"more than ₹80,000\" — strict inequality. `>= 80000` would wrongly allocate an AC room to someone who paid exactly ₹80,000. `== 80000` only matches one specific value. `> 80000` is the only correct implementation.",
        "easy", "apply", "fill-the-condition",
        "`fee_paid > 80000`",
        ["`fee_paid == 80000`", "`fee_paid >= 80000`", "`fee_paid < 80000`"],
    ),
    # 3.1.3 Easy — Trace the output, if-elif-else
    (
        "A road transport office uses a Python script to categorise vehicles by engine capacity (in cc) for tax purposes: below 1000cc is \"Economy\", 1000–1999cc is \"Standard\", and 2000cc and above is \"Premium\". A vehicle with 1500cc is being processed.\n\n```python\ncc = 1500\nif cc < 1000:\n    print(\"Economy\")\nelif cc < 2000:\n    print(\"Standard\")\nelse:\n    print(\"Premium\")\n```\n\nWhat is printed?",
        "`cc < 1000` → `False`. `cc < 2000` → `True` (1500 < 2000). The `elif` branch fires and prints `Standard`. The `else` is never reached.",
        "easy", "apply", "trace-the-output",
        "`Standard`",
        ["`Economy`", "`Premium`", "Nothing — no condition matches 1500"],
    ),
    # 3.1.4 Medium — Spot the logic bug, boundary condition
    (
        "A ticketing system at a Chennai cinema gives a senior citizen discount to customers aged 60 and above. A developer writes the check below, but customers who are exactly 60 years old report they are not receiving the discount.\n\n```python\nage = 60\nif age > 60:\n    print(\"Senior citizen discount applied\")\nelse:\n    print(\"No discount\")\n```\n\nWhat is the bug and what does the code print for `age = 60`?",
        "`age > 60` is `False` when `age` is exactly 60, so the `else` branch runs. The rule says \"60 and above\", which requires `>=`. Changing `>` to `>=` fixes the boundary exclusion.",
        "medium", "analyze", "spot-the-logic-bug",
        "The bug is `>` should be `>=`; it prints `No discount`",
        ["The bug is `>` should be `!=`; it prints `No discount`", "There is no bug; it correctly prints `Senior citizen discount applied`", "The bug is `>` should be `==`; it prints `No discount`"],
    ),
    # 3.1.5 Medium — Trace the output, nested conditions
    (
        "A university library system blocks borrowing if a student has overdue books OR an unpaid fine above ₹200. The developer writes nested conditions to give a specific reason for the block:\n\n```python\noverdue = False\nfine = 350\n\nif overdue:\n    print(\"Blocked: overdue books\")\nelif fine > 200:\n    print(\"Blocked: unpaid fine\")\nelse:\n    print(\"Borrowing allowed\")\n```\n\nWhat is printed for these values?",
        "`overdue` is `False` — the first branch is skipped. `fine > 200` → `350 > 200` → `True` — the `elif` fires. Only one branch in an `if-elif-else` chain executes. Output is `Blocked: unpaid fine`.",
        "medium", "apply", "trace-the-output",
        "`Blocked: unpaid fine`",
        ["`Blocked: overdue books`", "`Borrowing allowed`", "`Blocked: overdue books` and `Blocked: unpaid fine`"],
    ),
    # 3.1.6 Medium — Which structure fits?
    (
        "A railway reservation system needs to categorise a passenger's ticket class based on their input: `\"SL\"` maps to Sleeper, `\"3A\"` to Third AC, `\"2A\"` to Second AC, and `\"1A\"` to First AC. Any other input should print \"Invalid class\". A developer is deciding which Python construct to use.\n\nWhich structure is most appropriate for this requirement?",
        "`match-case` is designed exactly for this pattern — matching a value against a fixed set of cases with a default fallback using `_`. Four separate `if` statements would not have a clean fallback and could print multiple outputs. A single `if` with `or` becomes unreadable. Nested `if` adds unnecessary complexity.",
        "medium", "analyze", "which-structure-fits",
        "A `match-case` block with a `_` wildcard for invalid input",
        ["A single `if` with `or` conditions combining all four ticket classes", "Four separate `if` statements, one per class, each with its own print", "A nested `if` inside an `if-else` for each ticket class"],
    ),
    # 3.1.7 Medium — Fill the condition, compound condition
    (
        "A job portal allows a candidate to apply for a senior engineer role only if they have at least 5 years of experience AND a degree in Computer Science OR Electronics. The HR team specifies: both conditions must hold — the experience threshold is mandatory, and the degree must be one of the two specified branches. Which condition correctly implements this?\n\n```python\nyears = 6\ndegree = \"Electronics\"\nif ________:\n    print(\"Eligible to apply\")\n```",
        "The rule requires experience (`years >= 5`) AND one of two degrees. Without parentheses, `and` binds tighter than `or`, so the unparenthesized options evaluate incorrectly — they would pass candidates with the right degree but insufficient experience. A degree cannot equal two values simultaneously, so an `or`-of-two-`and`s form is logically impossible here. Grouping the degree check with `or` inside parentheses is the correct form.",
        "medium", "analyze", "fill-the-condition",
        "`years >= 5 and (degree == \"Computer Science\" or degree == \"Electronics\")`",
        ["`years >= 5 and degree == \"Computer Science\" or degree == \"Electronics\"`", "`years >= 5 or (degree == \"Computer Science\" and degree == \"Electronics\")`", "`years > 5 and degree == \"Computer Science\" or degree == \"Electronics\"`"],
    ),
    # 3.1.8 Medium — Equivalent rewrite, if-else vs two ifs
    (
        "A student portal updates a grade label. A senior developer shows two versions to a junior and asks if they are equivalent:\n\n```python\n# Version A\nif marks >= 50:\n    grade = \"Pass\"\nelse:\n    grade = \"Fail\"\n\n# Version B\nif marks >= 50:\n    grade = \"Pass\"\nif marks < 50:\n    grade = \"Fail\"\n```\n\nAre these always equivalent? If not, for which value of `marks` do they differ?",
        "For any value of `marks`, exactly one of `marks >= 50` and `marks < 50` is `True`. Since the conditions are mutually exclusive and exhaustive, both versions assign the same value to `grade` for every possible input. They are logically equivalent here — though `if-else` is preferred for clarity and to avoid evaluating two conditions unnecessarily.",
        "medium", "analyze", "equivalent-rewrite",
        "They are always equivalent — both produce the same result for any value of `marks`",
        ["They differ when `marks == 50` — Version B sets `grade` to `\"Fail\"` for that value", "They differ when `marks == 49` — Version A skips assignment; Version B does not", "They are always equivalent — two `if` statements work identically to `if-else` here"],
    ),
    # 3.1.9 Hard — Predict unexpected behaviour, missing elif
    (
        "A grading system at a private college awards grades as follows: 90 and above → `\"O\"`, 75–89 → `\"A\"`, 60–74 → `\"B\"`. A developer writes the following code for a student who scored 92:\n\n```python\nmarks = 92\nif marks >= 60:\n    print(\"B\")\nif marks >= 75:\n    print(\"A\")\nif marks >= 90:\n    print(\"O\")\n```\n\nWhat is actually printed, and what is the structural problem?",
        "These are three independent `if` statements, not an `elif` chain. For `marks = 92`, all three conditions are `True`, so all three branches execute and print `B`, `A`, and `O`. The fix is to use `elif` so only the first matching branch fires.",
        "hard", "analyze", "predict-unexpected-behaviour",
        "`B`, `A`, and `O` — all three `if` conditions are true; all three print",
        ["`O` — only the last matching condition fires", "`B` — the first true condition fires and the remaining `if`s are skipped", "Nothing — the conditions overlap, causing a conflict error"],
    ),
    # 3.1.10 Hard — Guard clause, input validation
    (
        "A college exam portal accepts a student's percentage (0–100) and prints a grade. Before computing the grade, the developer wants to reject invalid input — anything below 0 or above 100 — immediately, without nesting the main logic inside an `if` block. Which approach correctly implements a guard clause?\n\n```python\npercentage = float(input(\"Enter percentage: \"))\n\n# Option A\nif percentage < 0 or percentage > 100:\n    print(\"Invalid input\")\nelse:\n    # grade logic here\n\n# Option B\nif not (0 <= percentage <= 100):\n    print(\"Invalid input\")\n# grade logic here (no else)\n```\n\nWhich of the following best describes the difference between Option A and Option B?",
        "Both conditions correctly reject values outside 0–100. Option A wraps the main logic in an `else`, which adds nesting. Option B exits early on invalid input (guard clause style) and lets the main logic continue at the same indentation level. Both are valid Python; Option B is the guard clause pattern the question describes.",
        "hard", "analyze", "guard-clause",
        "Both are logically correct; Option B is the guard clause style, avoids nesting",
        ["Option A is wrong — `or` cannot combine two separate comparisons in one `if`", "Option B is wrong — `not` cannot be applied to a chained comparison in Python", "Both are wrong — input validation always requires `try-except` instead of `if`"],
    ),
]

SET2 = [
    # 3.2.1 Easy — Truthiness, zero and None
    (
        "An inventory system at a medical store checks whether any units of a medicine are in stock before allowing a sale. The stock count is stored as an integer. For a medicine with `stock = 0`, what does the following print?\n\n```python\nstock = 0\nif stock:\n    print(\"Available\")\nelse:\n    print(\"Out of stock\")\n```",
        "In Python, `0` is falsy. `if stock:` with `stock = 0` evaluates to `False`, so the `else` branch runs. `None`, `0`, `\"\"`, and empty collections are all falsy — not just `None` and `False`.",
        "easy", "understand", "truthiness-in-conditions",
        "`Out of stock` — `0` is falsy in Python",
        ["`Available` — `0` is a valid integer value, so it is truthy", "`Available` — only `None` and `False` are falsy in Python", "A `TypeError` — integers cannot be used directly in `if` conditions"],
    ),
    # 3.2.2 Easy — Fill the condition, if-elif-else
    (
        "A Bengaluru food delivery app classifies delivery distance into three tiers for dynamic pricing: below 3 km is \"Near\", 3–8 km is \"Mid\", and above 8 km is \"Far\". A developer needs to fill in the `elif` condition. Which correctly completes the chain?\n\n```python\ndistance = 5.2\nif distance < 3:\n    print(\"Near\")\nelif ________:\n    print(\"Mid\")\nelse:\n    print(\"Far\")\n```",
        "By the time the `elif` is reached, `distance < 3` has already been ruled out — so `distance` is guaranteed to be 3 or above. The only remaining condition needed is `distance <= 8` to separate Mid from Far; the lower bound is already handled by the preceding `if`, so repeating it is redundant. `distance <= 8` is the cleanest, idiomatic form given the chain context.",
        "easy", "apply", "fill-the-condition",
        "`distance <= 8`",
        ["`distance > 3 and distance < 8`", "`distance >= 3 and distance <= 8`", "`distance < 8`"],
    ),
    # 3.2.3 Easy — Which structure fits?, match-case
    (
        "A bank's IVR system maps a customer's numeric keypress to an action: `1` for balance enquiry, `2` for mini statement, `3` for fund transfer, and anything else for \"invalid option\". A developer is choosing a construct to implement this.\n\nWhich is the most appropriate?",
        "`match-case` maps cleanly to fixed value-to-action patterns. The `_` wildcard arm handles any unmatched keypress. Four independent `if` statements have no clean default and could print multiple responses. A single `if` with `or` can't direct to different actions per value.",
        "easy", "understand", "which-structure-fits",
        "A `match-case` block with a `_` wildcard for invalid input",
        ["Nested `if` statements — one per keypress value, placed inside each other", "A single `if` with all four options joined by `or`", "Four independent `if` statements, one per keypress"],
    ),
    # 3.2.4 Easy — Trace the output, if-else
    (
        "A ride-sharing app applies surge pricing when demand is high. Demand is considered high if more than 80 ride requests are pending. For `requests = 80`, what does the following print?\n\n```python\nrequests = 80\nif requests > 80:\n    print(\"Surge pricing active\")\nelse:\n    print(\"Normal pricing\")\n```",
        "`80 > 80` is `False`. The condition requires strictly more than 80 requests. The `else` branch runs and prints `Normal pricing`. This is a boundary condition — if the rule were \"80 or more\", `>=` would be needed.",
        "easy", "apply", "trace-the-output",
        "`Normal pricing`",
        ["`Surge pricing active` — 80 meets the high-demand threshold", "Both lines are printed — the boundary triggers both branches", "Nothing — the condition is ambiguous at exactly 80"],
    ),
    # 3.2.5 Medium — Spot the logic bug, wrong logical operator
    (
        "A college exam system invalidates a paper if a student's score is below 0 or above 100. A developer writes the validation check. During testing, a score of 110 passes through without being flagged as invalid.\n\n```python\nscore = 110\nif score < 0 and score > 100:\n    print(\"Invalid score\")\nelse:\n    print(\"Score accepted\")\n```\n\nWhat is the bug?",
        "A single number cannot be both below 0 AND above 100 at the same time — so `and` makes the condition always `False`. The correct operator is `or`: flag the score if it is below 0 OR above 100. With `and`, every score passes through as accepted.",
        "medium", "analyze", "spot-the-logic-bug",
        "`and` should be `or` — no score can be below 0 and above 100 at the same time",
        ["The comparisons are reversed — it should be `score > 0 and score < 100` to validate", "The `else` branch is missing a condition to accept scores properly", "`<` and `>` should both be `<=` and `>=` respectively"],
    ),
    # 3.2.6 Medium — Fill the condition, ternary expression
    (
        "A result portal at a Pune university displays a student's status in a single line. The rule is simple: if marks are 40 or above, status is `\"Pass\"`, otherwise `\"Fail\"`. A developer wants to use a ternary expression. Which correctly implements this?\n\n```python\nmarks = 55\nstatus = ________\nprint(status)\n```",
        "The rule is \"40 or above\" — so `>=` is correct. Using `>` instead wrongly fails a student with exactly 40 marks. A colon-based `if: ... else:` form is not valid ternary syntax in Python. Swapping the pass and fail labels would also be incorrect.",
        "medium", "apply", "fill-the-condition",
        "`\"Pass\" if marks >= 40 else \"Fail\"`",
        ["`\"Pass\" if marks > 40 else \"Fail\"`", "`if marks >= 40: \"Pass\" else: \"Fail\"`", "`\"Fail\" if marks >= 40 else \"Pass\"`"],
    ),
    # 3.2.7 Medium — Trace the output, elif chain with boundary
    (
        "A state electricity board uses a slab-based billing system. Units consumed determine the rate per unit: up to 100 units → ₹2/unit, 101–300 units → ₹4/unit, above 300 units → ₹6/unit. A household consumed exactly 300 units.\n\n```python\nunits = 300\nif units <= 100:\n    rate = 2\nelif units <= 300:\n    rate = 4\nelse:\n    rate = 6\nprint(rate)\n```\n\nWhat is printed?",
        "`units <= 100` → `300 <= 100` → `False`. `units <= 300` → `300 <= 300` → `True`. The `elif` fires and `rate = 4`. The `else` is not reached. Boundary values like 300 are correctly handled by `<=`.",
        "medium", "apply", "trace-the-output",
        "`4`",
        ["`2`", "`6`", "Nothing — 300 falls on a boundary and no condition matches"],
    ),
    # 3.2.8 Medium — Which structure fits?, if vs if-else vs elif
    (
        "A student's dashboard needs to show a message based on their CGPA: below 5.0 shows a warning, 5.0–7.4 shows \"Good standing\", and 7.5 and above shows \"Dean's List\". Exactly one message should appear. Which construct is most appropriate?",
        "Exactly one message must appear for any CGPA value. An `if-elif-else` chain guarantees only one branch executes and covers all cases including boundaries. Three independent `if` statements could fire multiple branches. An `if` with `or` cannot direct to different outputs per range. An `if` with two `elif`s and no `else` leaves values above 7.5 unhandled if the conditions aren't written carefully.",
        "medium", "analyze", "which-structure-fits",
        "An `if-elif-else` chain",
        ["Three independent `if` statements", "An `if` with two `elif` branches and no `else`", "A single `if` with all conditions joined by `or`"],
    ),
    # 3.2.9 Medium — Spot the logic bug, unreachable branch
    (
        "A developer writes a ticket pricing system for a theme park. Children below 12 get a ₹100 ticket, seniors above 60 get ₹150, and everyone else pays ₹300. A colleague notices one branch is never reachable regardless of the input.\n\n```python\nage = 45\nif age < 12:\n    print(\"₹100\")\nelif age < 12:\n    print(\"₹150\")\nelse:\n    print(\"₹300\")\n```\n\nWhat is the bug, and what does this print for `age = 8`?",
        "The `elif` condition is identical to the `if` condition (`age < 12`). If the `if` is `True`, the `elif` is never evaluated. If the `if` is `False`, the `elif` is also `False` for the same reason. The `elif` branch (`₹150`) is permanently unreachable. For `age = 8`, `if age < 12` is `True` and `₹100` is printed. The senior pricing logic is simply missing.",
        "medium", "analyze", "spot-the-logic-bug",
        "The second `elif` is unreachable — it duplicates the `if` condition; prints `₹100`",
        ["The `else` is unreachable; prints `₹100` for age 8", "Both `if` and `elif` are unreachable; only `₹300` ever prints for any input", "No bug — Python evaluates all branches independently; prints `₹100` and `₹150` for age 8"],
    ),
    # 3.2.10 Medium — Truthiness, non-empty string
    (
        "A feedback form at an engineering college checks whether a student has entered a comment before saving it to the database. The field is stored as a string. For `comment = \"  \"` (a string containing only spaces), what does the following print?\n\n```python\ncomment = \"  \"\nif comment:\n    print(\"Comment saved\")\nelse:\n    print(\"No comment entered\")\n```",
        "Python's truthiness check for strings is based solely on length — an empty string `\"\"` is falsy, but any string with at least one character (including spaces) is truthy. `\"  \"` has two characters, so `if comment:` is `True`. To properly catch whitespace-only input, the developer should use `if comment.strip():`.",
        "medium", "understand", "truthiness-in-conditions",
        "`Comment saved` — any non-empty string, including spaces, is truthy",
        ["`No comment entered` — strings with only spaces are falsy", "A `ValueError` — whitespace-only strings cannot be used in conditions", "`No comment entered` — Python strips spaces before evaluating truthiness"],
    ),
    # 3.2.11 Medium — Trace the output, nested if
    (
        "A smart home app controls an air conditioner. It turns on cooling only if the room temperature is above 28°C AND the AC mode is set to \"auto\". If the temperature is above 28 but mode is not \"auto\", it logs a warning instead.\n\n```python\ntemp = 31\nmode = \"manual\"\n\nif temp > 28:\n    if mode == \"auto\":\n        print(\"Cooling started\")\n    else:\n        print(\"Warning: manual mode active\")\nelse:\n    print(\"Temperature normal\")\n```\n\nWhat is printed?",
        "`temp > 28` → `31 > 28` → `True`. The outer `if` is entered. `mode == \"auto\"` → `\"manual\" == \"auto\"` → `False`. The inner `else` fires: `Warning: manual mode active`. The outer `else` is never reached.",
        "medium", "apply", "trace-the-output",
        "`Warning: manual mode active`",
        ["`Cooling started`", "`Temperature normal`", "`Cooling started` and `Warning: manual mode active`"],
    ),
    # 3.2.12 Medium — Fill the condition, compound with not
    (
        "A hostel mess system serves special diet meals only to students who have registered for the diet programme AND have not already collected their meal token for the day. Which condition correctly implements this check?\n\n```python\nis_registered = True\ntoken_collected = True\n\nif ________:\n    print(\"Special meal issued\")\nelse:\n    print(\"Not eligible\")\n```",
        "Both conditions must hold: the student must be registered (`is_registered` is `True`) AND must not have collected a token (`not token_collected` must be `True`). For the given values, `True and not True` → `True and False` → `False`, so \"Not eligible\" is printed — correct, since the token was already collected.",
        "medium", "apply", "fill-the-condition",
        "`is_registered and not token_collected`",
        ["`is_registered or not token_collected`", "`is_registered and token_collected`", "`not is_registered and not token_collected`"],
    ),
    # 3.2.13 Hard — Equivalent rewrite, if-else vs ternary
    (
        "A developer refactors a grade display into a ternary expression. A colleague reviews both versions and claims they are not equivalent.\n\n```python\n# Version A\nif percentage >= 35:\n    result = \"Pass\"\nelse:\n    result = \"Fail\"\n\n# Version B\nresult = \"Fail\" if percentage >= 35 else \"Pass\"\n```\n\nFor `percentage = 40`, what does each version assign to `result`?",
        "In Version A, `percentage >= 35` is `True` → `result = \"Pass\"`. In Version B, the ternary reads `\"Fail\" if percentage >= 35 else \"Pass\"` — the labels are swapped. When the condition is `True`, it returns `\"Fail\"`. The colleague is correct — the versions are not equivalent. The correct ternary should be `\"Pass\" if percentage >= 35 else \"Fail\"`.",
        "hard", "analyze", "equivalent-rewrite",
        "Version A assigns `\"Pass\"`, Version B assigns `\"Fail\"` — not equivalent",
        ["Both assign `\"Pass\"` — the two versions are logically equivalent", "Both assign `\"Fail\"` — `>=` evaluates to `False` for a value of 40", "Version A assigns `\"Fail\"` and Version B assigns `\"Pass\"` for `percentage = 40`"],
    ),
    # 3.2.14 Hard — Spot the logic bug, condition order in elif chain
    (
        "A cab aggregator charges fares based on distance: up to 5 km → ₹50, up to 15 km → ₹100, above 15 km → ₹150. A developer writes the chain below. For a trip of 8 km, the system is incorrectly charging ₹50.\n\n```python\ndistance = 8\nif distance <= 15:\n    fare = 50\nelif distance <= 5:\n    fare = 100\nelse:\n    fare = 150\nprint(fare)\n```\n\nWhat is the bug?",
        "`distance <= 15` is `True` for any trip up to 15 km, including 8 km. So the first `if` fires immediately and assigns `fare = 50`. The `elif distance <= 5` is never reached for any value ≤ 15. The fix is to order conditions from most specific to most general: check `<= 5` first, then `<= 15`, then `else`.",
        "hard", "analyze", "spot-the-logic-bug",
        "The conditions are in wrong order — `distance <= 15` swallows the short-trip slab",
        ["The `else` should use `distance > 15` explicitly so it only triggers for long trips", "`<=` should be `<` throughout to prevent boundary overlap between the two slabs", "The mid and far slabs need explicit `and` conditions to define a lower bound too"],
    ),
    # 3.2.15 Hard — Predict unexpected behaviour, indentation
    (
        "A student builds a login system. The intended behaviour is: if the username and password are both correct, print \"Login successful\", otherwise print \"Login failed\". They write:\n\n```python\nusername = \"admin\"\npassword = \"1234\"\n\nif username == \"admin\":\n    if password == \"1234\":\n        print(\"Login successful\")\nelse:\n    print(\"Login failed\")\n```\n\nA user enters username `\"admin\"` and password `\"wrong\"`. What is printed?",
        "The `else` is aligned with the outer `if` (`username == \"admin\"`). For username `\"admin\"`, the outer `if` is `True` — so the `else` is skipped entirely. Inside, `password == \"1234\"` is `False` — the inner `if` does not execute. No print statement is reached. The intended behaviour requires an `else` under the inner `if`, not the outer one.",
        "hard", "analyze", "predict-unexpected-behaviour",
        "Nothing is printed",
        ["`Login failed`", "`Login successful`", "Both `Login successful` and `Login failed`"],
    ),
    # 3.2.16 Hard — Equivalent rewrite, nested if vs and
    (
        "Two developers debate whether these two blocks always produce the same output:\n\n```python\n# Version A\nif temperature > 35:\n    if humidity > 80:\n        print(\"Heat alert issued\")\n\n# Version B\nif temperature > 35 and humidity > 80:\n    print(\"Heat alert issued\")\n```\n\nAre they equivalent, and does it matter which is used?",
        "Both versions require `temperature > 35` AND `humidity > 80` to print the alert. A nested `if` where the inner `if` has no `else` is logically identical to a single `if` with `and`. They produce the same output for all inputs. Version B is preferred for readability.",
        "hard", "analyze", "equivalent-rewrite",
        "Equivalent — both require both conditions to be true before printing",
        ["Not equivalent — Version A prints the alert even when humidity is below 80", "Not equivalent — Version B short-circuits and skips the temperature check", "Not equivalent — nested `if` in Version A evaluates humidity unconditionally"],
    ),
    # 3.2.17 Hard — Ternary expression, predict value
    (
        "A logistics company's Python dashboard shows delivery priority as a single label. Priority is `\"High\"` if the order value exceeds ₹5,000 and the customer is a premium member; otherwise `\"Standard\"`. A developer writes:\n\n```python\norder_value = 6000\nis_premium = False\npriority = \"High\" if order_value > 5000 and is_premium else \"Standard\"\nprint(priority)\n```\n\nWhat is printed, and why?",
        "The ternary condition is `order_value > 5000 and is_premium`. `6000 > 5000` → `True`, but `is_premium` → `False`. `True and False` → `False`. The ternary returns the `else` value: `\"Standard\"`. Both conditions must be met for High priority.",
        "hard", "apply", "ternary-expression",
        "`Standard` — `is_premium` is `False`, so the `and` condition fails",
        ["`High` — `order_value > 5000` is `True`, which is sufficient", "A `SyntaxError` — `and` cannot be used inside a ternary expression", "`High` — ternary expressions ignore the second condition after `and`"],
    ),
    # 3.2.18 Hard — Guard clause, multi-condition validation
    (
        "A banking app accepts a PIN change request. The new PIN must be exactly 4 digits long and must not be the same as the old PIN. The developer wants to reject invalid requests early using guard clauses. Which implementation is correct?\n\n```python\nold_pin = \"1234\"\nnew_pin = input(\"Enter new PIN: \")\n\n# Option A\nif len(new_pin) != 4:\n    print(\"PIN must be 4 digits\")\nelif new_pin == old_pin:\n    print(\"New PIN cannot be same as old PIN\")\nelse:\n    print(\"PIN changed successfully\")\n\n# Option B\nif len(new_pin) != 4 and new_pin == old_pin:\n    print(\"Invalid PIN\")\nelse:\n    print(\"PIN changed successfully\")\n```\n\nWhich option correctly handles all cases, and what is wrong with the other?",
        "Option A checks the two rules independently in sequence and gives a specific message for each failure. Option B uses `and` — a PIN would only be flagged if it is both the wrong length AND the same as the old PIN simultaneously. A 3-digit PIN that is also different from the old PIN would pass through incorrectly. Option A correctly handles each failure case on its own.",
        "hard", "analyze", "guard-clause",
        "Option A is correct; Option B uses `and` where only one condition needs to be true",
        ["Option A is correct; Option B fails — it requires both checks to be true at once", "Both are correct — `and` inside `if` and `elif` chaining behave identically here", "Option B is correct; Option A introduces unnecessary branching for a simple check"],
    ),
    # 3.2.19 Hard — match-case, wildcard and fall-through
    (
        "A student support chatbot at a college maps a student's typed command to an action. The developer writes:\n\n```python\ncommand = \"help\"\n\nmatch command:\n    case \"status\":\n        print(\"Showing status\")\n    case \"fees\":\n        print(\"Showing fees\")\n    case \"schedule\":\n        print(\"Showing schedule\")\n    case _:\n        print(\"Unknown command\")\n```\n\nA student types `\"HELP\"` (uppercase). What is printed, and why?",
        "Python's `match-case` performs exact equality matching by default and is case-sensitive. `\"HELP\"` does not match `\"help\"`, so none of the first three cases fire. The `_` wildcard matches any value that hasn't matched above — it is not restricted to `None`. `Unknown command` is printed. The fix would be `command.lower()` before matching.",
        "hard", "analyze", "match-case-behaviour",
        "`Unknown command` — Python's `match-case` is case-sensitive; no match found",
        ["`Showing status` — `match-case` tries each case until one partially matches", "Nothing — `match-case` raises a `MatchError` when no case clause is satisfied", "`Unknown command` — but only because `_` explicitly matches the `None` type here"],
    ),
    # 3.2.20 Hard — Combined, multi-condition trace with truthiness
    (
        "A college gate management system logs entry only if a visitor has a valid pass AND has been pre-approved by a department. If either condition fails, it logs the specific reason. A security guard tests it with a visitor who has a pass but no pre-approval.\n\n```python\nhas_pass = True\npre_approved = False\ndepartment = \"\"\n\nif has_pass and pre_approved:\n    print(\"Entry logged\")\nelif has_pass and not pre_approved:\n    print(\"Pass valid — awaiting department approval\")\nelif not has_pass and department:\n    print(\"No pass — department override active\")\nelse:\n    print(\"Entry denied\")\n```\n\nWhat is printed?",
        "First `elif`: `has_pass and pre_approved` → `True and False` → `False`. Second `elif`: `has_pass and not pre_approved` → `True and True` → `True`. This branch fires and prints `Pass valid — awaiting department approval`. The third `elif` and `else` are not evaluated. `department = \"\"` is falsy but never tested here.",
        "hard", "analyze", "truthiness-and-trace",
        "`Pass valid — awaiting department approval` — pass present but pre-approval missing",
        ["`Entry denied` — neither condition in the chain is satisfied", "`Entry logged` — both `has_pass` and `pre_approved` are `True`", "`No pass — department override active` — `has_pass` is `False` but `department` is set"],
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
            "topics": "control-flow",
            "subTopics": subtopic,
            "companies": None,
            "option1": options[0],
            "option2": options[1],
            "option3": options[2],
            "option4": options[3],
            "answer": pos,
        })
    return rows


rows1 = build_rows(SET1, "Set 1", "Python - MCQ - 3.1")
rows2 = build_rows(SET2, "Set 2", "Python - MCQ - 3.2")
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
ws.title = "Python - MCQ - Unit 3"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/Unit 3 - Control Flow/Unit 3 - Control Flow - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
