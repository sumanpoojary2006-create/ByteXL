"""5.1 - Subqueries and CTEs - Coding Questions (32: what a subquery is,
subqueries in WHERE, subqueries in FROM, correlated subqueries, CTEs, and
recursive CTEs).

Every displayed AVG is wrapped in ROUND(..., 2) for the same reason as
earlier chapters (PostgreSQL's unrounded AVG scale is not reliably
predictable without a live server) even though every department/company
average in this dataset happens to divide evenly to two decimal places.

Recursive-CTE questions are verified with small walk_up/walk_down BFS
helpers that replicate the recursive CTE's own round-by-round evaluation
(each round processes exactly the rows newly added by the previous round),
so level numbers and same-level row order are derived the same way
PostgreSQL would actually compute them, not asserted by hand.
"""
import decimal
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from dbms_cqlib import main, sql_insert

D = decimal.Decimal


def pg_round(value, places):
    quantum = D(1).scaleb(-places)
    return value.quantize(quantum, rounding=decimal.ROUND_HALF_UP)


TOPIC = "advanced-querying-with-sql"
WHAT_TOPIC = "what-is-a-subquery"
WHERE_TOPIC = "subqueries-in-where"
FROM_TOPIC = "subqueries-in-from"
CORRELATED_TOPIC = "correlated-subqueries"
CTE_TOPIC = "common-table-expressions"
RECURSIVE_TOPIC = "recursive-ctes-querying-hierarchies-and-graphs"

# ----------------------------- employees dataset (lessons 1-5) -----------------------------

EMPLOYEE_COLUMNS = ["employee_id", "employee_name", "department", "salary", "manager_id"]
EMPLOYEES = [
    dict(employee_id=1, employee_name="Ananya Sharma", department="Engineering", salary=D("95000.00"), manager_id=None),
    dict(employee_id=2, employee_name="Rajat Bhatia", department="Engineering", salary=D("78000.00"), manager_id=1),
    dict(employee_id=3, employee_name="Meghna Iyer", department="Engineering", salary=D("82000.00"), manager_id=1),
    dict(employee_id=4, employee_name="Sameer Khan", department="Sales", salary=D("65000.00"), manager_id=None),
    dict(employee_id=5, employee_name="Pooja Reddy", department="Sales", salary=D("58000.00"), manager_id=4),
    dict(employee_id=6, employee_name="Vikas Malhotra", department="Marketing", salary=D("60000.00"), manager_id=None),
]

EMPLOYEES_DDL = """
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    employee_name TEXT,
    department TEXT,
    salary NUMERIC(10, 2),
    manager_id INTEGER
);
"""
EMPLOYEES_SQL = EMPLOYEES_DDL.strip("\n") + "\n\n" + sql_insert("employees", EMPLOYEE_COLUMNS, EMPLOYEES)
EMPLOYEES_SCHEMA_LINES = [
    "employees(employee_id INTEGER PK, employee_name TEXT, department TEXT, salary NUMERIC(10,2), "
    "manager_id INTEGER) -- 6 rows; manager_id is NULL for the three department heads",
]


def dept_avg(department):
    salaries = [e["salary"] for e in EMPLOYEES if e["department"] == department]
    return sum(salaries, D("0")) / len(salaries)


COMPANY_AVG = sum((e["salary"] for e in EMPLOYEES), D("0")) / len(EMPLOYEES)

# ----------------------------- hierarchy dataset (lesson 6) -----------------------------

HIER_COLUMNS = ["employee_id", "employee_name", "manager_id"]
HIERARCHY = [
    dict(employee_id=1, employee_name="Ananya Sharma", manager_id=None),
    dict(employee_id=2, employee_name="Rajat Bhatia", manager_id=1),
    dict(employee_id=3, employee_name="Meghna Iyer", manager_id=1),
    dict(employee_id=4, employee_name="Karan Oberoi", manager_id=2),
    dict(employee_id=5, employee_name="Divya Nambiar", manager_id=2),
    dict(employee_id=6, employee_name="Farhan Sheikh", manager_id=4),
]

HIERARCHY_DDL = """
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    employee_name TEXT,
    manager_id INTEGER
);
"""
HIERARCHY_SQL = HIERARCHY_DDL.strip("\n") + "\n\n" + sql_insert("employees", HIER_COLUMNS, HIERARCHY)
HIERARCHY_SCHEMA_LINES = [
    "employees(employee_id INTEGER PK, employee_name TEXT, manager_id INTEGER) -- 6 rows; "
    "Ananya Sharma is at the top of the org chart with manager_id NULL",
]


def walk_up(start_id):
    """BFS mirroring the recursive CTE that walks from an employee up to the top."""
    result = []
    level = 1
    current = next(e for e in HIERARCHY if e["employee_id"] == start_id)
    while current is not None:
        result.append((current["employee_name"], level))
        mgr_id = current["manager_id"]
        current = next((e for e in HIERARCHY if e["employee_id"] == mgr_id), None) if mgr_id is not None else None
        level += 1
    return result


def walk_down(start_id):
    """BFS mirroring the recursive CTE that walks from a manager down through every report."""
    result = []
    frontier = [start_id]
    level = 1
    while frontier:
        for eid in frontier:
            result.append((next(e for e in HIERARCHY if e["employee_id"] == eid)["employee_name"], level))
        next_frontier = []
        for eid in frontier:
            next_frontier.extend(e["employee_id"] for e in HIERARCHY if e["manager_id"] == eid)
        frontier = next_frontier
        level += 1
    return result


Q = []

# ==================== what-is-a-subquery ====================

Q.append(dict(
    title="Employees Earning Above the Company Average", difficulty="Easy", topics=TOPIC, subTopics=WHAT_TOPIC,
    bloomTaxonomy="apply",
    prose="Kabir's manager wants to know who earns more than the company average. Find them, "
          "using a subquery to compute the average rather than a hardcoded number.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["employee_name", "salary"],
    solution_sql="SELECT employee_name, salary\nFROM employees\n"
                 "WHERE salary > (SELECT AVG(salary) FROM employees)\n"
                 "ORDER BY salary DESC;",
    data=dict(),
    oracle=lambda: sorted(
        [(e["employee_name"], e["salary"]) for e in EMPLOYEES if e["salary"] > COMPANY_AVG],
        key=lambda row: row[1], reverse=True,
    ),
    hints="The parentheses around SELECT AVG(salary) FROM employees mark it as a subquery; the "
          "database runs it first and substitutes the resulting number into the outer condition.",
))

Q.append(dict(
    title="Employees Earning Above the Engineering Average", difficulty="Easy", topics=TOPIC, subTopics=WHAT_TOPIC,
    bloomTaxonomy="apply",
    prose="Compare every employee's salary against the average salary within Engineering "
          "specifically, not the whole company.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["employee_name", "salary"],
    solution_sql="SELECT employee_name, salary\nFROM employees\n"
                 "WHERE salary > (SELECT AVG(salary) FROM employees WHERE department = 'Engineering')\n"
                 "ORDER BY salary DESC;",
    data=dict(),
    oracle=lambda: sorted(
        [(e["employee_name"], e["salary"]) for e in EMPLOYEES if e["salary"] > dept_avg("Engineering")],
        key=lambda row: row[1], reverse=True,
    ),
    hints="Adding WHERE department = 'Engineering' inside the subquery narrows what average is "
          "computed, without changing anything about the outer query's own structure.",
))

Q.append(dict(
    title="Employees Earning Less Than the Highest Paid", difficulty="Hard", topics=TOPIC, subTopics=WHAT_TOPIC,
    bloomTaxonomy="apply",
    prose="Find every employee earning less than Ananya Sharma, the highest-paid employee in the "
          "table.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["employee_name", "salary"],
    solution_sql="SELECT employee_name, salary\nFROM employees\n"
                 "WHERE salary < (SELECT salary FROM employees WHERE employee_name = 'Ananya Sharma')\n"
                 "ORDER BY salary DESC;",
    data=dict(),
    oracle=lambda: sorted(
        [(e["employee_name"], e["salary"]) for e in EMPLOYEES if e["employee_name"] != "Ananya Sharma"],
        key=lambda row: row[1], reverse=True,
    ),
    hints="A subquery that looks up one specific employee's salary by name works exactly like the "
          "AVG(salary) subquery, just returning a different single value.",
))

Q.append(dict(
    title="The Lowest-Paid Employee", difficulty="Medium", topics=TOPIC, subTopics=WHAT_TOPIC,
    bloomTaxonomy="apply",
    prose="Find whichever employee earns the single lowest salary in the table.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["employee_name", "salary"],
    solution_sql="SELECT employee_name, salary\nFROM employees\n"
                 "WHERE salary = (SELECT MIN(salary) FROM employees);",
    data=dict(),
    oracle=lambda: [
        (e["employee_name"], e["salary"]) for e in EMPLOYEES if e["salary"] == min(x["salary"] for x in EMPLOYEES)
    ],
    hints="MIN(salary) always returns exactly one number, so a plain = comparison works without "
          "any special handling.",
))

Q.append(dict(
    title="Employees Earning 1.5 Times Vikas Malhotra's Salary", difficulty="Hard", topics=TOPIC, subTopics=WHAT_TOPIC,
    bloomTaxonomy="analyze",
    prose="Find every employee earning more than one and a half times what Vikas Malhotra, the "
          "sole Marketing employee, earns.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["employee_name", "salary"],
    solution_sql="SELECT employee_name, salary\nFROM employees\n"
                 "WHERE salary > 1.5 * (SELECT salary FROM employees WHERE employee_name = 'Vikas Malhotra');",
    data=dict(),
    oracle=lambda: [
        (e["employee_name"], e["salary"]) for e in EMPLOYEES
        if e["salary"] > D("1.5") * next(x["salary"] for x in EMPLOYEES if x["employee_name"] == "Vikas Malhotra")
    ],
    hints="A subquery's single returned value can be used inside arithmetic too, not just a bare "
          "comparison; 1.5 * (subquery) computes the threshold before the outer WHERE checks it.",
))

# ==================== subqueries-in-where ====================

Q.append(dict(
    title="The Single Highest-Paid Employee", difficulty="Easy", topics=TOPIC, subTopics=WHERE_TOPIC,
    bloomTaxonomy="apply",
    prose="Find whoever earns the single highest salary in the table.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["employee_name", "salary"],
    solution_sql="SELECT employee_name, salary\nFROM employees\n"
                 "WHERE salary = (SELECT MAX(salary) FROM employees);",
    data=dict(),
    oracle=lambda: [
        (e["employee_name"], e["salary"]) for e in EMPLOYEES if e["salary"] == max(x["salary"] for x in EMPLOYEES)
    ],
    hints="MAX(salary) always returns exactly one number, so this comparison works with a plain =.",
))

Q.append(dict(
    title="Same Department as Rajat or Vikas", difficulty="Medium", topics=TOPIC, subTopics=WHERE_TOPIC,
    bloomTaxonomy="analyze",
    prose="Find every employee who works in the same department as Rajat Bhatia or Vikas "
          "Malhotra, without needing to know in advance which departments those two belong to.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["employee_name", "department"],
    solution_sql="SELECT employee_name, department\nFROM employees\n"
                 "WHERE department IN (\n"
                 "    SELECT department FROM employees WHERE employee_name IN ('Rajat Bhatia', 'Vikas Malhotra')\n"
                 ")\n"
                 "ORDER BY employee_id;",
    data=dict(),
    oracle=lambda: [
        (e["employee_name"], e["department"]) for e in EMPLOYEES
        if e["department"] in {
            x["department"] for x in EMPLOYEES if x["employee_name"] in ("Rajat Bhatia", "Vikas Malhotra")
        }
    ],
    hints="IN checks whether the outer row's department matches any value the subquery returns, "
          "exactly like IN with a hand-typed list of literals.",
))

Q.append(dict(
    title="Beating At Least One Sales Salary", difficulty="Medium", topics=TOPIC, subTopics=WHERE_TOPIC,
    bloomTaxonomy="analyze",
    prose="Find every employee whose salary beats at least one Sales department salary.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["employee_name", "salary"],
    solution_sql="SELECT employee_name, salary\nFROM employees\n"
                 "WHERE salary > ANY (SELECT salary FROM employees WHERE department = 'Sales')\n"
                 "ORDER BY salary DESC;",
    data=dict(),
    oracle=lambda: sorted(
        [
            (e["employee_name"], e["salary"]) for e in EMPLOYEES
            if any(e["salary"] > s for s in (x["salary"] for x in EMPLOYEES if x["department"] == "Sales"))
        ],
        key=lambda row: row[1], reverse=True,
    ),
    hints="salary > ANY (subquery) is true if the outer row's salary beats at least one value the "
          "subquery returns; beating just the lower Sales salary is enough to qualify.",
))

Q.append(dict(
    title="Beating Every Sales Salary", difficulty="Medium", topics=TOPIC, subTopics=WHERE_TOPIC,
    bloomTaxonomy="analyze",
    prose="Find every employee whose salary beats every single Sales department salary, a "
          "stricter version of the previous question.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["employee_name", "salary"],
    solution_sql="SELECT employee_name, salary\nFROM employees\n"
                 "WHERE salary > ALL (SELECT salary FROM employees WHERE department = 'Sales')\n"
                 "ORDER BY salary DESC;",
    data=dict(),
    oracle=lambda: sorted(
        [
            (e["employee_name"], e["salary"]) for e in EMPLOYEES
            if all(e["salary"] > s for s in (x["salary"] for x in EMPLOYEES if x["department"] == "Sales"))
        ],
        key=lambda row: row[1], reverse=True,
    ),
    hints="salary > ALL (subquery) requires beating every value the subquery returns, not just "
          "one, producing a shorter list than the ANY version.",
))

Q.append(dict(
    title="Earning Less Than Every Engineering Salary", difficulty="Hard", topics=TOPIC, subTopics=WHERE_TOPIC,
    bloomTaxonomy="apply",
    prose="Find every employee who earns less than the lowest salary in Engineering.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["employee_name", "salary"],
    solution_sql="SELECT employee_name, salary\nFROM employees\n"
                 "WHERE salary < ALL (SELECT salary FROM employees WHERE department = 'Engineering')\n"
                 "ORDER BY salary DESC;",
    data=dict(),
    oracle=lambda: sorted(
        [
            (e["employee_name"], e["salary"]) for e in EMPLOYEES
            if all(e["salary"] < s for s in (x["salary"] for x in EMPLOYEES if x["department"] == "Engineering"))
        ],
        key=lambda row: row[1], reverse=True,
    ),
    hints="salary < ALL (subquery) requires being lower than every Engineering salary, including "
          "the lowest one, not just the average.",
))

Q.append(dict(
    title="Employees Who Do Not Manage Anyone", difficulty="Hard", topics=TOPIC, subTopics=WHERE_TOPIC,
    bloomTaxonomy="analyze",
    prose="Find every employee whose employee_id never appears as anyone else's manager_id, "
          "guarding the subquery against NULL the way NOT IN requires.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["employee_name"],
    solution_sql="SELECT employee_name\nFROM employees\n"
                 "WHERE employee_id NOT IN (\n"
                 "    SELECT manager_id FROM employees WHERE manager_id IS NOT NULL\n"
                 ")\n"
                 "ORDER BY employee_id;",
    data=dict(),
    oracle=lambda: [
        (e["employee_name"],) for e in sorted(EMPLOYEES, key=lambda e: e["employee_id"])
        if e["employee_id"] not in {x["manager_id"] for x in EMPLOYEES if x["manager_id"] is not None}
    ],
    hints="Without WHERE manager_id IS NOT NULL inside the subquery, a NULL would slip into the "
          "list NOT IN compares against and silently break the entire condition for every row.",
))

# ==================== subqueries-in-from ====================

Q.append(dict(
    title="Average Salary per Department", difficulty="Easy", topics=TOPIC, subTopics=FROM_TOPIC,
    bloomTaxonomy="apply",
    prose="Compute the average salary within each department, as the standalone first step of a "
          "larger report.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["department", "department_avg"],
    solution_sql="SELECT department, ROUND(AVG(salary), 2) AS department_avg\n"
                 "FROM employees\nGROUP BY department\nORDER BY department;",
    data=dict(),
    oracle=lambda: [
        (dept, pg_round(dept_avg(dept), 2)) for dept in sorted({e["department"] for e in EMPLOYEES})
    ],
    hints="This grouped query is exactly what will become the FROM subquery in the next step of "
          "the report.",
))

Q.append(dict(
    title="Departments Paying Above the Company Average", difficulty="Medium", topics=TOPIC, subTopics=FROM_TOPIC,
    bloomTaxonomy="analyze",
    prose="Treat the department-average query as a derived table, then keep only the departments "
          "whose average clears the overall company average.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["department", "department_avg"],
    solution_sql="SELECT department, department_avg\n"
                 "FROM (\n"
                 "    SELECT department, ROUND(AVG(salary), 2) AS department_avg\n"
                 "    FROM employees\n"
                 "    GROUP BY department\n"
                 ") AS dept_averages\n"
                 "WHERE department_avg > (SELECT AVG(salary) FROM employees);",
    data=dict(),
    oracle=lambda: [
        (dept, pg_round(dept_avg(dept), 2)) for dept in sorted({e["department"] for e in EMPLOYEES})
        if dept_avg(dept) > COMPANY_AVG
    ],
    hints="The FROM subquery, aliased dept_averages, runs first and produces a small result the "
          "outer query then filters like any real table.",
))

Q.append(dict(
    title="Each Employee's Salary Versus Their Department Average", difficulty="Medium", topics=TOPIC, subTopics=FROM_TOPIC,
    bloomTaxonomy="analyze",
    prose="Join every employee to a derived table of department averages, showing each person's "
          "own salary next to their department's average and how far above or below it they "
          "fall.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["employee_name", "salary", "department_avg", "diff_from_dept_avg"],
    solution_sql="SELECT e.employee_name, e.salary, dept_averages.department_avg,\n"
                 "       e.salary - dept_averages.department_avg AS diff_from_dept_avg\n"
                 "FROM employees e\n"
                 "JOIN (\n"
                 "    SELECT department, ROUND(AVG(salary), 2) AS department_avg\n"
                 "    FROM employees\n"
                 "    GROUP BY department\n"
                 ") AS dept_averages ON e.department = dept_averages.department\n"
                 "ORDER BY e.employee_id;",
    data=dict(),
    oracle=lambda: [
        (e["employee_name"], e["salary"], pg_round(dept_avg(e["department"]), 2),
         e["salary"] - pg_round(dept_avg(e["department"]), 2))
        for e in sorted(EMPLOYEES, key=lambda e: e["employee_id"])
    ],
    hints="A derived table can be joined to a real table exactly like any other table, letting "
          "every individual row see the pre-computed summary sitting right next to it.",
))

Q.append(dict(
    title="The Single Top-Paying Department", difficulty="Hard", topics=TOPIC, subTopics=FROM_TOPIC,
    bloomTaxonomy="apply",
    prose="Find the single department with the highest average salary, showing just its name and "
          "that average.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["department", "department_avg"],
    solution_sql="SELECT department, department_avg\n"
                 "FROM (\n"
                 "    SELECT department, ROUND(AVG(salary), 2) AS department_avg\n"
                 "    FROM employees\n"
                 "    GROUP BY department\n"
                 ") AS dept_averages\n"
                 "ORDER BY department_avg DESC LIMIT 1;",
    data=dict(),
    oracle=lambda: sorted(
        [(dept, pg_round(dept_avg(dept), 2)) for dept in {e["department"] for e in EMPLOYEES}],
        key=lambda row: row[1], reverse=True,
    )[:1],
    hints="Ordering the derived table's results and limiting to one row on the outer query gives "
          "the single top-paying department.",
))

Q.append(dict(
    title="Departments With More Than One Employee", difficulty="Hard", topics=TOPIC, subTopics=FROM_TOPIC,
    bloomTaxonomy="analyze",
    prose="Show every department alongside its employee count, keeping only departments with "
          "more than one employee.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["department", "emp_count"],
    solution_sql="SELECT department, emp_count\n"
                 "FROM (\n"
                 "    SELECT department, COUNT(*) AS emp_count\n"
                 "    FROM employees\n"
                 "    GROUP BY department\n"
                 ") AS dept_counts\n"
                 "WHERE emp_count > 1\n"
                 "ORDER BY department;",
    data=dict(),
    oracle=lambda: [
        (dept, len([e for e in EMPLOYEES if e["department"] == dept]))
        for dept in sorted({e["department"] for e in EMPLOYEES})
        if len([e for e in EMPLOYEES if e["department"] == dept]) > 1
    ],
    hints="A derived table is not limited to averages; any grouped, aggregated result can be "
          "treated as a table and filtered further by the outer query.",
))

# ==================== correlated-subqueries ====================

Q.append(dict(
    title="Above Your Own Department's Average", difficulty="Easy", topics=TOPIC, subTopics=CORRELATED_TOPIC,
    bloomTaxonomy="analyze",
    prose="For each employee, check whether their salary is above the average of their own "
          "department, recomputed fresh for every employee rather than once overall.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["employee_name", "department", "salary"],
    solution_sql="SELECT e1.employee_name, e1.department, e1.salary\n"
                 "FROM employees e1\n"
                 "WHERE e1.salary > (\n"
                 "    SELECT AVG(e2.salary) FROM employees e2 WHERE e2.department = e1.department\n"
                 ")\n"
                 "ORDER BY e1.employee_id;",
    data=dict(),
    oracle=lambda: [
        (e["employee_name"], e["department"], e["salary"])
        for e in sorted(EMPLOYEES, key=lambda e: e["employee_id"])
        if e["salary"] > dept_avg(e["department"])
    ],
    hints="e2.department = e1.department reaches into the outer query's current row, so the "
          "average recomputes for each employee's own department rather than using one fixed "
          "number.",
))

Q.append(dict(
    title="Each Employee's Own Department Average as a Column", difficulty="Medium", topics=TOPIC, subTopics=CORRELATED_TOPIC,
    bloomTaxonomy="analyze",
    prose="Show every employee's name alongside their own department's average salary as a "
          "computed column, confirming it genuinely differs between Engineering, Sales, and "
          "Marketing rows.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["employee_name", "dept_avg"],
    solution_sql="SELECT e1.employee_name,\n"
                 "       (SELECT ROUND(AVG(e2.salary), 2) FROM employees e2 WHERE e2.department = e1.department) AS dept_avg\n"
                 "FROM employees e1\n"
                 "ORDER BY e1.employee_id;",
    data=dict(),
    oracle=lambda: [
        (e["employee_name"], pg_round(dept_avg(e["department"]), 2))
        for e in sorted(EMPLOYEES, key=lambda e: e["employee_id"])
    ],
    hints="Placed in the SELECT list instead of WHERE, the same correlated subquery becomes a "
          "computed column that visibly changes value from row to row.",
))

Q.append(dict(
    title="Employees Who Manage At Least One Other Employee", difficulty="Medium", topics=TOPIC, subTopics=CORRELATED_TOPIC,
    bloomTaxonomy="analyze",
    prose="Find every employee who manages at least one other employee, using a correlated "
          "EXISTS check rather than a self join or GROUP BY.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["employee_name"],
    solution_sql="SELECT e1.employee_name\n"
                 "FROM employees e1\n"
                 "WHERE EXISTS (\n"
                 "    SELECT 1 FROM employees e2 WHERE e2.manager_id = e1.employee_id\n"
                 ")\n"
                 "ORDER BY e1.employee_id;",
    data=dict(),
    oracle=lambda: [
        (e["employee_name"],) for e in sorted(EMPLOYEES, key=lambda e: e["employee_id"])
        if any(x["manager_id"] == e["employee_id"] for x in EMPLOYEES)
    ],
    hints="The inner query checks, for each candidate row, whether any other employee lists that "
          "row's employee_id as their manager_id, a yes-or-no question per row.",
))

Q.append(dict(
    title="Employees Who Out-Earn Their Own Manager", difficulty="Hard", topics=TOPIC, subTopics=CORRELATED_TOPIC,
    bloomTaxonomy="analyze",
    prose="Find every employee who earns more than their own direct manager, using a correlated "
          "subquery that compares each employee's salary to their manager's salary.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["employee_name"],
    solution_sql="SELECT e1.employee_name\n"
                 "FROM employees e1\n"
                 "WHERE e1.salary > (\n"
                 "    SELECT e2.salary FROM employees e2 WHERE e2.employee_id = e1.manager_id\n"
                 ");",
    data=dict(),
    oracle=lambda: [
        (e["employee_name"],) for e in EMPLOYEES
        if e["manager_id"] is not None
        and e["salary"] > next(x["salary"] for x in EMPLOYEES if x["employee_id"] == e["manager_id"])
    ],
    allow_empty_result=True,
    hints="An empty result is still a correct one here: every manager in this data out-earns "
          "their own direct reports, so nobody qualifies.",
))

Q.append(dict(
    title="The Top Earner in Each Department", difficulty="Hard", topics=TOPIC, subTopics=CORRELATED_TOPIC,
    bloomTaxonomy="analyze",
    prose="Find the single highest-paid employee within each department, using a correlated "
          "subquery to compare each employee against their own department's maximum.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["employee_name", "department", "salary"],
    solution_sql="SELECT e1.employee_name, e1.department, e1.salary\n"
                 "FROM employees e1\n"
                 "WHERE e1.salary = (\n"
                 "    SELECT MAX(e2.salary) FROM employees e2 WHERE e2.department = e1.department\n"
                 ")\n"
                 "ORDER BY e1.department;",
    data=dict(),
    oracle=lambda: sorted(
        [
            (e["employee_name"], e["department"], e["salary"])
            for e in EMPLOYEES
            if e["salary"] == max(x["salary"] for x in EMPLOYEES if x["department"] == e["department"])
        ],
        key=lambda row: row[1],
    ),
    hints="The correlated subquery recomputes MAX(salary) separately for each employee's own "
          "department, so the comparison target changes row by row.",
))

# ==================== common-table-expressions ====================

Q.append(dict(
    title="Departments Above Company Average, via CTE", difficulty="Easy", topics=TOPIC, subTopics=CTE_TOPIC,
    bloomTaxonomy="apply",
    prose="Rewrite the departments-above-company-average report using a CTE instead of a nested "
          "FROM subquery, so the query reads top to bottom.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["department", "department_avg"],
    solution_sql="WITH dept_averages AS (\n"
                 "    SELECT department, ROUND(AVG(salary), 2) AS department_avg\n"
                 "    FROM employees\n"
                 "    GROUP BY department\n"
                 ")\n"
                 "SELECT department, department_avg\n"
                 "FROM dept_averages\n"
                 "WHERE department_avg > (SELECT AVG(salary) FROM employees);",
    data=dict(),
    oracle=lambda: [
        (dept, pg_round(dept_avg(dept), 2)) for dept in sorted({e["department"] for e in EMPLOYEES})
        if dept_avg(dept) > COMPANY_AVG
    ],
    hints="WITH dept_averages AS (...) names the inner query before the main query begins, and "
          "the main query then reads FROM dept_averages exactly as if it were a real table.",
))

Q.append(dict(
    title="Department and Company Averages Side by Side", difficulty="Medium", topics=TOPIC, subTopics=CTE_TOPIC,
    bloomTaxonomy="analyze",
    prose="Chain two CTEs together: one computing department averages, one computing the company "
          "average, then show only the departments beating the company figure alongside both "
          "numbers.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["department", "department_avg", "company_avg"],
    solution_sql="WITH dept_averages AS (\n"
                 "    SELECT department, ROUND(AVG(salary), 2) AS department_avg\n"
                 "    FROM employees\n"
                 "    GROUP BY department\n"
                 "),\n"
                 "company_average AS (\n"
                 "    SELECT ROUND(AVG(salary), 2) AS company_avg FROM employees\n"
                 ")\n"
                 "SELECT dept_averages.department, dept_averages.department_avg, company_average.company_avg\n"
                 "FROM dept_averages, company_average\n"
                 "WHERE dept_averages.department_avg > company_average.company_avg;",
    data=dict(),
    oracle=lambda: [
        (dept, pg_round(dept_avg(dept), 2), pg_round(COMPANY_AVG, 2))
        for dept in sorted({e["department"] for e in EMPLOYEES})
        if dept_avg(dept) > COMPANY_AVG
    ],
    hints="Two CTEs, separated by a comma, are each defined once and then referenced together in "
          "the final SELECT, which compares their columns directly.",
))

Q.append(dict(
    title="High Earners, via a Named CTE", difficulty="Medium", topics=TOPIC, subTopics=CTE_TOPIC,
    bloomTaxonomy="apply",
    prose="Pull the above-average-salary WHERE subquery out into a named CTE, then select from "
          "it ordered by salary descending.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["employee_name", "salary"],
    solution_sql="WITH high_earners AS (\n"
                 "    SELECT employee_id, employee_name, salary\n"
                 "    FROM employees\n"
                 "    WHERE salary > (SELECT AVG(salary) FROM employees)\n"
                 ")\n"
                 "SELECT employee_name, salary\n"
                 "FROM high_earners\n"
                 "ORDER BY salary DESC;",
    data=dict(),
    oracle=lambda: sorted(
        [(e["employee_name"], e["salary"]) for e in EMPLOYEES if e["salary"] > COMPANY_AVG],
        key=lambda row: row[1], reverse=True,
    ),
    hints="A WHERE subquery can be wrapped in a CTE too, not just a FROM subquery; the pattern "
          "keeps the final query focused on what happens with the result.",
))

Q.append(dict(
    title="Above Department Average, via CTE and JOIN", difficulty="Hard", topics=TOPIC, subTopics=CTE_TOPIC,
    bloomTaxonomy="analyze",
    prose="Rewrite the correlated-subquery version of 'employees earning more than their own "
          "department average' as a CTE joined back to employees instead.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["employee_name", "department", "salary"],
    solution_sql="WITH dept_averages AS (\n"
                 "    SELECT department, ROUND(AVG(salary), 2) AS department_avg\n"
                 "    FROM employees\n"
                 "    GROUP BY department\n"
                 ")\n"
                 "SELECT employees.employee_name, employees.department, employees.salary\n"
                 "FROM employees\n"
                 "JOIN dept_averages ON employees.department = dept_averages.department\n"
                 "WHERE employees.salary > dept_averages.department_avg\n"
                 "ORDER BY employees.employee_id;",
    data=dict(),
    oracle=lambda: [
        (e["employee_name"], e["department"], e["salary"])
        for e in sorted(EMPLOYEES, key=lambda e: e["employee_id"])
        if e["salary"] > dept_avg(e["department"])
    ],
    hints="This produces the same two employees, Ananya Sharma and Sameer Khan, as the correlated "
          "subquery version, just computed once as a small table and joined rather than "
          "recomputed per row.",
))

Q.append(dict(
    title="Top Earner per Department, via CTE and JOIN", difficulty="Hard", topics=TOPIC, subTopics=CTE_TOPIC,
    bloomTaxonomy="analyze",
    prose="Find the top earner in each department a second way: a CTE computing each "
          "department's maximum salary, joined back to employees to find who actually earns it.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["employee_name", "department", "salary"],
    solution_sql="WITH dept_max AS (\n"
                 "    SELECT department, MAX(salary) AS max_salary\n"
                 "    FROM employees\n"
                 "    GROUP BY department\n"
                 ")\n"
                 "SELECT e.employee_name, e.department, e.salary\n"
                 "FROM employees e\n"
                 "JOIN dept_max d ON e.department = d.department AND e.salary = d.max_salary\n"
                 "ORDER BY e.department;",
    data=dict(),
    oracle=lambda: sorted(
        [
            (e["employee_name"], e["department"], e["salary"])
            for e in EMPLOYEES
            if e["salary"] == max(x["salary"] for x in EMPLOYEES if x["department"] == e["department"])
        ],
        key=lambda row: row[1],
    ),
    hints="Joining on both department and the matching max_salary pinpoints exactly the row that "
          "achieved that maximum, the same result the correlated MAX subquery produced earlier.",
))

# ==================== recursive-ctes-querying-hierarchies-and-graphs ====================

Q.append(dict(
    title="Every Manager Above Farhan Sheikh", difficulty="Easy", topics=TOPIC, subTopics=RECURSIVE_TOPIC,
    bloomTaxonomy="apply",
    prose="List every manager above Farhan Sheikh, all the way to the top of the org chart, with "
          "a level showing how many steps up from him each one sits.",
    schema_sql=HIERARCHY_SQL, schema_lines=HIERARCHY_SCHEMA_LINES,
    header=["employee_name", "level"],
    solution_sql="WITH RECURSIVE reporting_chain AS (\n"
                 "    SELECT employee_id, employee_name, manager_id, 1 AS level\n"
                 "    FROM employees\n"
                 "    WHERE employee_id = 6\n\n"
                 "    UNION ALL\n\n"
                 "    SELECT e.employee_id, e.employee_name, e.manager_id, reporting_chain.level + 1\n"
                 "    FROM employees e\n"
                 "    JOIN reporting_chain ON e.employee_id = reporting_chain.manager_id\n"
                 ")\n"
                 "SELECT employee_name, level\n"
                 "FROM reporting_chain\n"
                 "ORDER BY level;",
    data=dict(),
    oracle=lambda: walk_up(6),
    hints="The base case starts with just Farhan at level 1; the recursive case repeatedly finds "
          "whoever manages the person just added, stopping once it finds no manager for Ananya.",
))

Q.append(dict(
    title="Every Employee Under Ananya Sharma", difficulty="Medium", topics=TOPIC, subTopics=RECURSIVE_TOPIC,
    bloomTaxonomy="analyze",
    prose="List every employee who reports, directly or indirectly, to Ananya Sharma, with a "
          "level showing how many steps down from her each one sits.",
    schema_sql=HIERARCHY_SQL, schema_lines=HIERARCHY_SCHEMA_LINES,
    header=["employee_name", "level"],
    solution_sql="WITH RECURSIVE team_below AS (\n"
                 "    SELECT employee_id, employee_name, manager_id, 1 AS level\n"
                 "    FROM employees\n"
                 "    WHERE employee_id = 1\n\n"
                 "    UNION ALL\n\n"
                 "    SELECT e.employee_id, e.employee_name, e.manager_id, team_below.level + 1\n"
                 "    FROM employees e\n"
                 "    JOIN team_below ON e.manager_id = team_below.employee_id\n"
                 ")\n"
                 "SELECT employee_name, level\n"
                 "FROM team_below\n"
                 "ORDER BY level;",
    data=dict(),
    oracle=lambda: walk_down(1),
    hints="Flipping the join condition to e.manager_id = team_below.employee_id walks down the "
          "org chart instead of up it, starting from Ananya at level 1.",
))

Q.append(dict(
    title="Every Employee Under Rajat Bhatia", difficulty="Hard", topics=TOPIC, subTopics=RECURSIVE_TOPIC,
    bloomTaxonomy="analyze",
    prose="Find every employee who reports, directly or indirectly, to Rajat Bhatia, including "
          "how many levels below him each one sits.",
    schema_sql=HIERARCHY_SQL, schema_lines=HIERARCHY_SCHEMA_LINES,
    header=["employee_name", "level"],
    solution_sql="WITH RECURSIVE team_below AS (\n"
                 "    SELECT employee_id, employee_name, manager_id, 1 AS level\n"
                 "    FROM employees\n"
                 "    WHERE employee_id = 2\n\n"
                 "    UNION ALL\n\n"
                 "    SELECT e.employee_id, e.employee_name, e.manager_id, team_below.level + 1\n"
                 "    FROM employees e\n"
                 "    JOIN team_below ON e.manager_id = team_below.employee_id\n"
                 ")\n"
                 "SELECT employee_name, level\n"
                 "FROM team_below\n"
                 "ORDER BY level;",
    data=dict(),
    oracle=lambda: walk_down(2),
    hints="Basing the recursion on WHERE employee_id = 2 starts the walk from Rajat instead of "
          "Ananya, correctly walking down every branch beneath him regardless of depth.",
))

Q.append(dict(
    title="Every Manager Above Divya Nambiar", difficulty="Hard", topics=TOPIC, subTopics=RECURSIVE_TOPIC,
    bloomTaxonomy="analyze",
    prose="List every manager above Divya Nambiar, all the way to the top, with a level showing "
          "how many steps up from her each one sits.",
    schema_sql=HIERARCHY_SQL, schema_lines=HIERARCHY_SCHEMA_LINES,
    header=["employee_name", "level"],
    solution_sql="WITH RECURSIVE reporting_chain AS (\n"
                 "    SELECT employee_id, employee_name, manager_id, 1 AS level\n"
                 "    FROM employees\n"
                 "    WHERE employee_id = 5\n\n"
                 "    UNION ALL\n\n"
                 "    SELECT e.employee_id, e.employee_name, e.manager_id, reporting_chain.level + 1\n"
                 "    FROM employees e\n"
                 "    JOIN reporting_chain ON e.employee_id = reporting_chain.manager_id\n"
                 ")\n"
                 "SELECT employee_name, level\n"
                 "FROM reporting_chain\n"
                 "ORDER BY level;",
    data=dict(),
    oracle=lambda: walk_up(5),
    hints="Divya's chain is shorter than Farhan's, since she sits one level higher in the org "
          "chart to begin with.",
))

Q.append(dict(
    title="Every Employee Under Karan Oberoi", difficulty="Hard", topics=TOPIC, subTopics=RECURSIVE_TOPIC,
    bloomTaxonomy="analyze",
    prose="Find every employee who reports, directly or indirectly, to Karan Oberoi.",
    schema_sql=HIERARCHY_SQL, schema_lines=HIERARCHY_SCHEMA_LINES,
    header=["employee_name", "level"],
    solution_sql="WITH RECURSIVE team_below AS (\n"
                 "    SELECT employee_id, employee_name, manager_id, 1 AS level\n"
                 "    FROM employees\n"
                 "    WHERE employee_id = 4\n\n"
                 "    UNION ALL\n\n"
                 "    SELECT e.employee_id, e.employee_name, e.manager_id, team_below.level + 1\n"
                 "    FROM employees e\n"
                 "    JOIN team_below ON e.manager_id = team_below.employee_id\n"
                 ")\n"
                 "SELECT employee_name, level\n"
                 "FROM team_below\n"
                 "ORDER BY level;",
    data=dict(),
    oracle=lambda: walk_down(4),
    hints="Karan's team is small: just himself and Farhan Sheikh, who reports directly to him.",
))

Q.append(dict(
    title="Total Team Size Under Ananya, Excluding Herself", difficulty="Hard", topics=TOPIC, subTopics=RECURSIVE_TOPIC,
    bloomTaxonomy="analyze",
    prose="Using the same recursive walk down from Ananya Sharma, count how many people report "
          "to her directly or indirectly, not including Ananya herself.",
    schema_sql=HIERARCHY_SQL, schema_lines=HIERARCHY_SCHEMA_LINES,
    header=["team_size"],
    solution_sql="WITH RECURSIVE team_below AS (\n"
                 "    SELECT employee_id, employee_name, manager_id, 1 AS level\n"
                 "    FROM employees\n"
                 "    WHERE employee_id = 1\n\n"
                 "    UNION ALL\n\n"
                 "    SELECT e.employee_id, e.employee_name, e.manager_id, team_below.level + 1\n"
                 "    FROM employees e\n"
                 "    JOIN team_below ON e.manager_id = team_below.employee_id\n"
                 ")\n"
                 "SELECT COUNT(*) AS team_size\n"
                 "FROM team_below\n"
                 "WHERE employee_id != 1;",
    data=dict(),
    oracle=lambda: [(len(walk_down(1)) - 1,)],
    hints="The recursive CTE's result can be filtered and aggregated afterward exactly like any "
          "other named result; excluding employee_id 1 removes Ananya's own row before counting.",
))

assert len(Q) == 32, len(Q)

for q in Q:
    q["tags"] = f"dbms - {q['subTopics']}"

OUT = "content/Question Bank/Coding Questions/DBMS/5.1 - Subqueries and CTEs - Coding Questions.xlsx"

if __name__ == "__main__":
    main(Q, OUT)
