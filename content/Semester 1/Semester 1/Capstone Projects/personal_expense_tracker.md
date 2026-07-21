## Background

Managing daily expenses is something every college student struggles with — UPI payments, mess bills, travel, stationery, and late-night food orders add up quickly without any visibility. SpendSmart is a command-line expense tracking application that helps users log, categorise, view, and analyse their spending.

This project draws on everything from Units 1 through 13: input validation, loops, lists and dictionaries, functions, file handling, basic OOP, and exception handling. You will build it in six stages, each one adding a meaningful layer of functionality.

By the end, SpendSmart will be a fully working CLI tool that persists data between sessions, handles bad input gracefully, and generates a monthly summary report.

## Stages

### Stage 1: Record Your First Expense

Build the foundation — accept expense details from the user and display them back.

1. Ask the user to enter the following details for one expense:
   - Description (text)
   - Amount (float)
   - Category (text — e.g. Food, Travel, Study, Entertainment, Other)
   - Date (text in DD-MM-YYYY format)

2. After entry, display a formatted receipt:
   ```
   ----------------------------------------
   EXPENSE RECORDED
   ----------------------------------------
   Description : Mess bill
   Category    : Food
   Amount      : ₹ 850.00
   Date        : 15-07-2025
   ----------------------------------------
   ```

3. Validate the amount — if the user enters a non-numeric or negative value, display an error message and ask again. Keep asking until a valid amount is entered.

4. Validate the category — if the user enters something not in your predefined list, prompt them to choose from the available options.

**Answer these questions after completing Stage 1:**
- If a user enters ₹0 as an expense amount, your validation accepts it. Should it? What edge cases did your validation not account for?
- Your category list is hardcoded. What breaks if someone wants to add "Gym" as a new category, and how would you fix that without changing the source code?

### Stage 2: Build the Main Menu

Extend the program to handle multiple expenses in a session using a menu-driven loop.

1. Build a main menu that repeats until the user chooses to exit:
   ```
   ========== SpendSmart ==========
   1. Add Expense
   2. View All Expenses
   3. View by Category
   4. Exit
   ================================
   ```

2. Store all expenses entered in the session as a list of dictionaries. Each dictionary should have keys: `description`, `amount`, `category`, `date`.

3. The "View All Expenses" option should display all recorded expenses in a numbered list with a session total at the bottom. If no expenses exist, display a meaningful message.

4. The "View by Category" option should filter and display only expenses matching a category the user specifies.

**Answer these questions after completing Stage 2:**
- Your "View by Category" filter — is it case-sensitive? Try entering "food" when expenses are stored as "Food". If it breaks, fix it. If it works, explain why.
- What happens to all expenses when the user exits the program? Is this acceptable for a tool meant to track spending?

### Stage 3: Organise with Functions and Add Reports

Refactor the program so every operation is a function, and add a summary report.

1. Refactor your code so each menu action calls a dedicated function:
   - `add_expense(expenses)` — handles input and appends to the list
   - `view_all(expenses)` — displays all expenses with a total
   - `view_by_category(expenses, category)` — filters by category
   - `get_total(expenses)` — returns the total amount as a float
   - `get_category_summary(expenses)` — returns a dictionary of category → total spent

2. Add a **Summary Report** menu option that calls `get_category_summary()` and displays spending per category, sorted from highest to lowest, with a percentage of total spend for each:
   ```
   ======= SPENDING SUMMARY =======
   Food          ₹ 1,250.00   52.1%
   Travel        ₹   800.00   33.3%
   Study         ₹   350.00   14.6%
   ---------------------------------
   Total         ₹ 2,400.00
   =================================
   ```

3. Add a `find_highest_expense(expenses)` function that returns the single most expensive item recorded.

**Answer these questions after completing Stage 3:**
- What does `get_total()` return when the expenses list is empty? Run it and check. Does it crash, return 0, or something else? Is that the right behaviour for a user who opens the app for the first time?
- After refactoring, did the main menu loop get shorter or longer? What moved out of it, and what does that tell you about why functions exist?

### Stage 4: Save Expenses Between Sessions

Make expenses persist between sessions by saving to and loading from a CSV file.

1. On program startup, load existing expenses from `expenses.csv` if it exists. If the file does not exist, start with an empty list.

2. Every time an expense is added, append it immediately to `expenses.csv`.

3. Use Python's `csv` module with `DictWriter` and `DictReader` so the file has a header row and is human-readable.

4. Add an **Export Summary** menu option that writes the category summary to a file called `summary_report.txt`.

5. Handle the case where `expenses.csv` exists but is empty or corrupted — the program should not crash, it should display a warning and start fresh.

**Answer these questions after completing Stage 4:**
- Open `expenses.csv` in a text editor after adding a few expenses. Does the amount column look exactly as you stored it, or has Python formatted it differently? What does this mean when you read it back?
- You save on every add. What is the tradeoff of saving after every entry versus saving only on exit? Which would you choose for a real application and why?

### Stage 5: Redesign with Classes

Redesign the application using classes.

1. Create an `Expense` class:
   - Attributes: `description`, `amount`, `category`, `date`
   - A `__str__` method that returns a formatted single-line summary
   - A `to_dict()` method that returns the expense as a dictionary
   - A `build_from_dict(data)` method that creates an `Expense` object from a dictionary (you can write this as a plain function outside the class, or as a method — Stage 5's questions ask you to compare both)

2. Create an `ExpenseTracker` class:
   - Attribute: `expenses` — a list of `Expense` objects
   - Methods: `add(expense)`, `get_all()`, `get_by_category(category)`, `get_total()`, `get_summary()`, `find_highest()`, `load_from_csv(filepath)`, `save_to_csv(filepath)`

3. Rewrite the main menu to use an `ExpenseTracker` instance. The menu loop should only call tracker methods — no business logic inside it.

**Answer these questions after completing Stage 5:**
- Count the lines in your main menu loop now versus after Stage 3. What moved out of it? If business logic is still in the menu loop, move it into the appropriate method.
- You built `build_from_dict()` as either a plain function or a method. Try it the other way. Which reads more naturally at the call site — `Expense.build_from_dict(row)` or `build_from_dict(row)`? What does it cost to keep dict-to-object conversion outside the class entirely?

### Stage 6: Make It Robust and Bug-Free

Make the application robust and fix three planted bugs.

**Exception Handling:**

1. Wrap all file operations in `try-except` blocks. Handle `FileNotFoundError`, `PermissionError`, and `csv.Error` separately with a distinct message for each.

2. Add a custom exception `InvalidExpenseError` that is raised when an expense has a negative amount or an empty description. Raise it inside `Expense.__init__` and catch it in the menu.

3. Rewrite the amount validation from Stage 1 using `try-except ValueError` instead of a conditional loop. Run both versions and decide which you keep — document your reasoning in a comment.

**Debugging:**

The following three bugs are planted. Find and fix each one. For each, write two sentences: what the bug was and what a real user would have experienced because of it.

**Bug 1:**
```text
def get_total(expenses):
    total = 0
    for expense in expenses:
        total += expense.amount
    return total / len(expenses)
```

**Bug 2:**
```text
def get_by_category(self, category):
    return [e for e in self.expenses if e.category == category]
    # categories were saved to CSV in lowercase
    # but user input comes in as title case
```

**Bug 3:**
```text
def load_from_csv(self, filepath):
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            self.expenses.append(Expense.from_dict(row))
    # this method is called on startup
    # and also offered as a "Reload from file" menu option
```

**Answer these questions after completing Stage 6:**
- Bug 3 is silent — it does not crash, it just doubles the data. How would a user eventually notice this? What kind of bug is harder to catch: one that crashes immediately or one that silently corrupts data?
- You now have both a validation loop (Stage 1) and a `try-except` approach (Stage 6) for handling bad amount input. Which did you keep and why? Is there a situation where the other approach would be better?

## The Complete Picture

When all six stages are complete, SpendSmart:

- Runs a persistent CLI menu that survives across sessions
- Stores expenses in a CSV file readable outside the program
- Validates all user input and handles errors without crashing
- Generates a formatted category summary with percentages
- Exports a summary report to a text file
- Is built with a clean OOP design separating data, logic, and interface
- Has been debugged with three realistic issues identified and fixed

## Where to Build This Project

1. Go to [bytexl.app/nimbus](https://bytexl.app/nimbus).
2. Click **Create new workspace**.

![The Nimbus dashboard with the Create new workspace button highlighted](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/nimbus-python/01_create_new_workspace.png)

3. Select the **Python** template, then click **Next**.

![Select the Python template and click Next](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/nimbus-python/02_select_python_template.png)

4. Enter a workspace name and click **Launch Workspace**.

![Enter a workspace name and launch the Python workspace](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/nimbus-python/03_name_and_launch_workspace.png)
