# Capstone Project: Employee Payroll System

## Background

Payroll processing is one of the most critical and error-prone operations in any organisation. A miscalculated salary or a missed deduction can have legal and financial consequences. PayRoll is a command-line payroll management system that computes monthly salaries, applies statutory deductions (PF, TDS, ESI), generates payslips, and maintains records across multiple months.

This project draws on everything from Units 1 through 13: input validation, loops, lists and dictionaries, functions, file handling, basic OOP, and exception handling. You will build it in six stages, starting with a single employee salary calculation and ending with a multi-employee, multi-month payroll system.

## Stages

### Stage 1: Compute a Single Salary

1. Ask the HR to enter details for one employee:
   - Employee name (text)
   - Employee ID (text)
   - Basic salary (float, in ₹)
   - House Rent Allowance — HRA (float, as a percentage of basic)
   - Dearness Allowance — DA (float, as a percentage of basic)

2. Apply the following deductions automatically:
   - Provident Fund (PF): 12% of basic salary
   - Employee State Insurance (ESI): 0.75% of gross salary (basic + HRA + DA)
   - Professional Tax: ₹200 flat per month

3. Display a formatted payslip:
   ```
   ============================================
   PAYSLIP — July 2025
   ============================================
   Employee    : Ramesh Kumar (EMP001)
   --------------------------------------------
   EARNINGS
   Basic       : ₹ 25,000.00
   HRA (40%)   : ₹ 10,000.00
   DA (20%)    : ₹  5,000.00
   Gross       : ₹ 40,000.00
   --------------------------------------------
   DEDUCTIONS
   PF (12%)    : ₹  3,000.00
   ESI (0.75%) : ₹    300.00
   Prof. Tax   : ₹    200.00
   Total Ded.  : ₹  3,500.00
   --------------------------------------------
   NET SALARY  : ₹ 36,500.00
   ============================================
   ```

4. Validate that basic salary is a positive number. Validate that HRA and DA percentages are between 0 and 100.

**Answer these questions after completing Stage 1:**
- ESI is applied on gross salary, not basic. If you computed ESI before computing gross, you would get a wrong answer. In what order did you compute the components, and does your order guarantee correctness?
- Professional Tax is ₹200 flat. In reality, it varies by state and income slab. What would you need to change in your program to support state-wise or slab-wise professional tax?

### Stage 2: Manage Multiple Employees with a Menu

1. Build a main menu:
   ```
   ========== PayRoll ==========
   1. Add Employee
   2. View All Employees
   3. Generate Payslip
   4. Search Employee
   5. Remove Employee
   6. Exit
   =============================
   ```

2. Store employees in a dictionary keyed by employee ID.

3. Add Employee: name, ID, designation, department, basic salary, HRA%, DA%.

4. Generate Payslip: takes employee ID and month/year (e.g. "July 2025"). Computes and displays the payslip for that month.

5. Search Employee: by name (partial, case-insensitive) or exact employee ID.

**Answer these questions after completing Stage 2:**
- Payslips are generated on demand and not stored. If the HR asks for July's payslip again next month, can they get it? What do you need to add?
- An employee's basic salary might change mid-year (due to an increment). Your current design uses a single stored basic salary. How would you handle a salary revision that applies from a specific month?

### Stage 3: TDS Calculation and Annual Summary

1. Add TDS (Tax Deducted at Source) calculation based on annual income:
   - Annual gross = monthly gross × 12
   - Tax slabs (new regime):
     - Up to ₹3,00,000: No tax
     - ₹3,00,001 – ₹6,00,000: 5%
     - ₹6,00,001 – ₹9,00,000: 10%
     - ₹9,00,001 – ₹12,00,000: 15%
     - Above ₹12,00,000: 20%
   - Monthly TDS = annual tax / 12

2. Add TDS to the payslip deductions.

3. Add an **Annual Summary** option: takes employee ID and year. Displays month-by-month gross, deductions, and net pay, plus total TDS paid for the year.

**Answer these questions after completing Stage 3:**
- Your TDS is computed as annual tax / 12, which assumes the same salary every month. If an employee gets a bonus in December, should TDS for that month be higher? How would a real payroll system handle this?
- Your tax slab is implemented as a series of if-elif conditions. What happens if the government changes the slab rates next year — how many lines of your code need to change?

### Stage 4: Payroll Processing and Reports

1. Add a **Run Monthly Payroll** option: processes payslips for all employees for a given month, stores all payslips, and displays a payroll summary.

2. Add a **Payroll Summary Report** for a given month:
   - Total gross payroll (sum of all gross salaries)
   - Total deductions
   - Total net payroll
   - Highest and lowest paid employees

3. Add a **Department Report**: groups employees by department and shows average salary, total headcount, and total payroll cost per department.

4. Track payroll history: store each processed payroll month so it cannot be processed twice.

**Answer these questions after completing Stage 4:**
- Your payroll history prevents processing the same month twice. What if an employee was added after payroll was already run for that month — how do you handle their first payslip?
- Total payroll cost is the sum of net salaries. But the true cost to the employer also includes the employer's PF contribution (12% of basic). Add this to the department report and explain why it was missing from your earlier calculations.

### Stage 5: Redesign with Classes

1. Create an `Employee` class with attributes `employee_id`, `name`, `designation`, `department`, `basic`, `hra_pct`, `da_pct` and methods `compute_gross()`, `compute_deductions(month, year)`, `generate_payslip(month, year)`.

2. Create a `Payslip` class with attributes `employee_id`, `month`, `year`, `gross`, `deductions` (dict), `net` and a `display()` method.

3. Create a `PayrollSystem` class that holds a dictionary of employees and a history of payslips. Move payroll processing, search, and reporting into `PayrollSystem` methods.

**Answer these questions after completing Stage 5:**
- `Employee.generate_payslip()` creates a `Payslip` object. Should the `Employee` know about the `Payslip` class, or should the `PayrollSystem` be responsible for creating `Payslip` objects from `Employee` data? Argue for one design.
- After the refactor, where does the TDS calculation live — in the `Employee` class or the `PayrollSystem` class? Does TDS depend only on employee data, or does it require system-level information?

### Stage 6: Make It Persistent and Robust

1. Save employees and payslip history to `employees.json` and `payslips.json`. Load on startup.

2. Handle file errors, missing files, and corrupted JSON.

3. Add a custom exception `PayrollError` with subclasses `EmployeeNotFoundError` and `PayrollAlreadyProcessedError`. Raise and catch these appropriately.

4. Find and fix the following three bugs:

**Bug 1:**
```python
def compute_tds(self, annual_gross):
    if annual_gross <= 300000:
        return 0
    elif annual_gross <= 600000:
        return annual_gross * 0.05
    elif annual_gross <= 900000:
        return annual_gross * 0.10
    # applies the full rate to the entire income
    # instead of only to the income within each slab
```

**Bug 2:**
```python
def run_monthly_payroll(self, month, year):
    for emp in self.employees.values():
        payslip = emp.generate_payslip(month, year)
        self.payslips.append(payslip)
    # does not check if payroll for this month already exists
    # running it twice doubles all payslips
```

**Bug 3:**
```python
def department_report(self):
    departments = {}
    for emp in self.employees.values():
        dept = emp.department
        if dept not in departments:
            departments[dept] = []
        departments[dept].append(emp.compute_gross())
    for dept, salaries in departments.items():
        print(f"{dept}: avg ₹{sum(salaries)/len(salaries):.2f}, headcount {len(salaries)}")
    # compute_gross() is called without arguments
    # but it requires month and year to compute HRA and DA
```

**Answer these questions after completing Stage 6:**
- Bug 1 computes tax on the full income rather than on each slab incrementally. For an annual gross of ₹7,00,000, what wrong TDS does the buggy version compute, and what is the correct answer?
- Bug 2 runs silently — it does not crash, it just creates duplicate payslips. What would the HR notice first: the wrong payslip count or the wrong total payroll figure?

## The Complete Picture

When all six stages are complete, PayRoll:

- Computes monthly salaries with HRA, DA, PF, ESI, and TDS deductions
- Generates formatted payslips for individual employees
- Runs monthly payroll for all employees and prevents duplicate processing
- Generates department reports and annual summaries
- Persists all employee and payslip data across sessions
- Uses a clean three-class OOP design
- Handles bad input and file errors without crashing
- Has three realistic bugs identified and fixed
