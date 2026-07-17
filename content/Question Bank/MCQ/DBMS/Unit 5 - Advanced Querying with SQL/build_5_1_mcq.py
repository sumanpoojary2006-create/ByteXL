import random
import openpyxl

random.seed(89)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])

WHAT_IS_A_SUBQUERY = [
    (
        "Kabir wants to find \"who earns more than the company average?\" but cannot write `WHERE salary > AVG(salary)` directly.\n\nWhy does this fail?",
        "Aggregate functions cannot sit inside a WHERE clause, the same rule covered when HAVING was introduced — the average has to be computed first, then used as part of a larger query, which is exactly what a subquery does.",
        "easy", "understand", "what-is-a-subquery",
        "Aggregate functions like AVG cannot be used directly inside a WHERE clause",
        ["WHERE clauses can only compare against literal numbers, never calculated values", "AVG(salary) is invalid syntax outside of a SELECT list entirely", "salary and AVG(salary) are incompatible data types for comparison"],
    ),
    (
        "`SELECT employee_name, salary FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);`\n\nWhat does the database do with the parenthesized part, and how is it used?",
        "The parenthesized part is a subquery (inner query); the database runs it first, gets back a single number, and substitutes that number directly into the outer query's condition, as if Kabir had typed the average in by hand.",
        "easy", "understand", "what-is-a-subquery",
        "It's a subquery run first to get one number, which is then substituted into the outer query's WHERE condition",
        ["It's a comment explaining the query's intent, ignored during execution", "It's a second, unrelated query that runs independently after the first", "It's a table alias that renames the employees table for this query"],
    ),
    (
        "Instead of the subquery, Kabir could run the average once, read the number, and hardcode `WHERE salary > 73000.00;`. This returns the same three rows today.\n\nWhy does the lesson describe this hardcoded approach as \"fragile\"?",
        "The moment a new employee is hired or anyone's salary changes, the true average shifts, and the hardcoded 73000.00 silently becomes wrong, with nothing in the query itself signaling the problem — the subquery version recalculates fresh every time and can never drift out of sync.",
        "medium", "analyze", "what-is-a-subquery",
        "The hardcoded value silently goes stale whenever the underlying data changes, with no signal that it's now wrong",
        ["The hardcoded version is actually invalid SQL syntax and would fail to run", "The hardcoded version runs slower than the subquery version in every case", "There's no real difference; hardcoding is always exactly as reliable as a subquery"],
    ),
    (
        "The lesson insists \"a subquery is not a special SQL feature with its own grammar.\"\n\nWhat is a subquery actually, structurally?",
        "A completely ordinary SELECT statement, the same kind covered since the first lesson of the course, just placed inside parentheses in a position where the outer query expects a value — any valid SELECT can act as a subquery, including one with its own WHERE, GROUP BY, or JOIN clauses.",
        "medium", "understand", "what-is-a-subquery",
        "An ordinary SELECT statement placed inside parentheses where the outer query expects a value",
        ["A specialized keyword-based construct unrelated to the SELECT statement", "A stored procedure that must be defined separately before it can be used", "A feature exclusive to WHERE clauses that cannot appear anywhere else"],
    ),
    (
        "`WHERE salary > (SELECT AVG(salary) FROM employees WHERE department = 'Engineering');`\n\nWhat changes about the comparison once the inner query adds its own WHERE department = 'Engineering'?",
        "The inner query now computes the average salary within Engineering specifically, rather than across the whole company, and the outer query compares every employee's salary against that narrower, department-specific figure instead of the whole-company average.",
        "medium", "apply", "what-is-a-subquery",
        "The comparison now uses the Engineering-only average instead of the whole-company average",
        ["The outer query is restricted to only showing Engineering employees automatically", "The subquery now returns every Engineering employee's individual salary as a list", "Nothing changes; adding WHERE inside the subquery has no effect on the outer comparison"],
    ),
    (
        "The lesson previews three different positions a subquery can occupy throughout the rest of the chapter.\n\nWhat are they?",
        "Inside WHERE (comparing a column against a computed value), inside FROM (standing in for an entire table), and correlated to the outer query (its result depending on each outer row).",
        "medium", "remember", "what-is-a-subquery",
        "Inside WHERE, inside FROM, and correlated to the outer query's current row",
        ["Inside SELECT, inside ORDER BY, and inside GROUP BY", "Inside CREATE TABLE, inside INSERT, and inside DELETE", "Only inside WHERE; subqueries cannot appear anywhere else in SQL"],
    ),
]

SUBQUERIES_IN_WHERE = [
    (
        "`SELECT employee_name, salary FROM employees WHERE salary = (SELECT MAX(salary) FROM employees);` uses a plain = comparison against a subquery.\n\nWhy is a plain = safe to use here specifically?",
        "MAX(salary) always returns exactly one number (a scalar value), so comparing it with = works without any special handling, unlike a subquery that might return multiple rows.",
        "easy", "understand", "subqueries-in-where",
        "MAX(salary) always returns exactly one value, so a plain equality comparison works safely",
        ["= always works with any subquery regardless of how many rows it returns", "MAX automatically converts its result into a list before comparison", "The employees table only has one row, making the comparison trivial"],
    ),
    (
        "Kabir needs \"employees in the same department as Rajat or Vikas,\" and the inner query finding their departments could return more than one department.\n\nWhich operator correctly handles a subquery that may return multiple values for an equality-style match?",
        "IN — it checks whether the outer row's value matches any value in the list the subquery returns, exactly the same way IN works with a hand-typed list of literal values.",
        "easy", "remember", "subqueries-in-where",
        "IN",
        ["=", "ANY only, never IN", "BETWEEN"],
    ),
    (
        "The Sales department's salaries are 65000.00 and 58000.00. `WHERE salary > ANY (SELECT salary FROM employees WHERE department = 'Sales')` returns everyone earning more than 58000.00, while `WHERE salary > ALL (...)` returns only those earning more than 65000.00.\n\nWhy does ANY use the easier bar (58000) and ALL use the harder bar (65000)?",
        "ANY is true if the outer row's salary beats at least one value returned by the subquery, so beating just the lower figure is enough; ALL is stricter, requiring the salary to beat every single value returned, so it must clear even the highest figure.",
        "medium", "analyze", "subqueries-in-where",
        "ANY only needs to beat one returned value (the easiest one to clear); ALL must beat every returned value, including the hardest one",
        ["ANY and ALL always produce identical results regardless of the data", "ANY requires beating every value; ALL requires beating only one, the reverse of the correct behavior", "The bar depends on which Sales employee is listed first in the table, not on ANY or ALL"],
    ),
    (
        "`NOT IN` carries a hidden risk that the lesson warns about specifically.\n\nWhat happens if the subquery behind a NOT IN can return a NULL, and what's the safer alternative?",
        "If the subquery can return a NULL, NOT IN silently returns no rows at all for every outer row, with no error to signal the problem — NOT EXISTS avoids this trap entirely and is generally the safer choice whenever the compared column might contain NULL.",
        "medium", "analyze", "subqueries-in-where",
        "NOT IN silently returns zero rows for every outer row if the subquery contains even one NULL; NOT EXISTS avoids this trap",
        ["NOT IN raises a clear, explicit error whenever a NULL appears in its subquery", "NOT IN simply ignores NULL values in its subquery, with no other effect", "NOT IN and NOT EXISTS always behave identically regardless of NULLs"],
    ),
    (
        "`WHERE employee_id NOT IN (SELECT manager_id FROM employees WHERE manager_id IS NOT NULL)` includes a `WHERE manager_id IS NOT NULL` filter inside the subquery.\n\nWhy is this filter not optional?",
        "Without it, the subquery's result would include a NULL for every employee who has no manager, and that single NULL in the list would silently break the entire NOT IN comparison for every row in the outer query.",
        "medium", "apply", "subqueries-in-where",
        "Without it, the subquery would return a NULL (from employees with no manager), silently breaking the entire NOT IN comparison for every row",
        ["It's purely a performance optimization with no effect on correctness", "It's required only because manager_id is the primary key of the table", "Without it, the query would fail with a syntax error rather than a silent wrong answer"],
    ),
    (
        "Kabir wants every employee who earns less than the lowest salary in Engineering.\n\nWhich operator correctly expresses \"less than every value in the Engineering salary list\"?",
        "ALL — `WHERE salary < ALL (SELECT salary FROM employees WHERE department = 'Engineering')` is true only if the outer row's salary is less than every single value the subquery returns, meaning less than even the highest Engineering salary, which guarantees it's below the lowest one too.",
        "medium", "apply", "subqueries-in-where",
        "ALL, since the salary must be lower than every value the subquery returns to guarantee it's below the lowest one",
        ["ANY, since beating just one Engineering salary is sufficient", "IN, since it only needs to match one specific salary value", "EXISTS, since it only checks whether Engineering has any employees at all"],
    ),
]

SUBQUERIES_IN_FROM = [
    (
        "`SELECT department, department_avg FROM (SELECT department, AVG(salary) AS department_avg FROM employees GROUP BY department) AS dept_averages WHERE department_avg > (SELECT AVG(salary) FROM employees);`\n\nWhat does the outer query treat dept_averages as?",
        "A real table (a derived table) — the outer query filters its rows with WHERE just like any actual table, using department_avg, a column that only exists because the inner query computed it.",
        "easy", "understand", "subqueries-in-from",
        "A real table (a derived table) that can be filtered with WHERE, even though its columns only exist because the inner query computed them",
        ["A single scalar value to compare against, exactly like a WHERE subquery", "A temporary variable that must be declared before the query runs", "An error, since subqueries cannot appear inside FROM in standard SQL"],
    ),
    (
        "Why must every subquery used in FROM be given an alias, unlike a WHERE subquery which never needs one?",
        "The outer query needs some way to refer to the derived table, the same way any real table needs a name to be selected from; leaving off the alias causes an error in most databases, since a WHERE subquery is only ever compared against, never selected from.",
        "medium", "understand", "subqueries-in-from",
        "The outer query needs a name to select from it, unlike a WHERE subquery, which is only ever compared against and never selected from",
        ["Aliases are only required for readability, and the query works fine without one", "FROM subqueries never actually need an alias; this is a common misconception", "The alias is required only when the subquery contains a GROUP BY clause"],
    ),
    (
        "A FROM subquery, dept_averages, is JOINed to the real employees table `ON e.department = dept_averages.department`.\n\nWhat does this let the report show that neither the raw employees table nor the aggregated subquery alone could show by itself?",
        "Both raw, row-level detail (an individual employee's own salary) and pre-computed summary (their department's average) side by side on the same row, plus a computed column showing exactly how far each person's salary sits above or below their department's average.",
        "medium", "apply", "subqueries-in-from",
        "Individual employee detail and their department's average summary together on the same row, including how far each person deviates from that average",
        ["Only the department averages, with individual employee rows discarded entirely", "Only the individual employee rows, with department averages discarded entirely", "A list of every possible department, regardless of whether any employees belong to it"],
    ),
    (
        "According to the \"Subqueries in FROM at a glance\" summary, when does the database compute a FROM subquery relative to the outer query?",
        "It runs before the outer query — the database computes the FROM subquery first, then treats its result as fixed, like a real table, for the rest of the outer query.",
        "medium", "understand", "subqueries-in-from",
        "The FROM subquery runs first, and the database treats its result as a fixed table for the outer query to use",
        ["It runs simultaneously with the outer query, with no fixed order between them", "It runs only after the outer query's WHERE clause has already been evaluated", "It runs last, after the outer query has already produced its final result"],
    ),
    (
        "Kabir wants the single department with the highest average salary, showing just its name and that average.\n\nWhich two techniques does he combine with a FROM subquery to isolate just that top row?",
        "ORDER BY department_avg DESC and LIMIT 1, applied on the outer query wrapping the derived table — sorting the department averages highest first and keeping only the very top row.",
        "medium", "apply", "subqueries-in-from",
        "ORDER BY department_avg DESC and LIMIT 1, applied to the outer query around the derived table",
        ["GROUP BY department_avg and HAVING COUNT(*) = 1", "WHERE department_avg = MAX(department_avg), applied inside the same subquery", "DISTINCT department_avg combined with TOP 1"],
    ),
    (
        "According to the \"at a glance\" summary, what is the most common use case for a FROM subquery?",
        "Pre-aggregating data before filtering or joining on the aggregate — exactly the pattern Kabir used to compute department averages first, then filter or join against that pre-computed result.",
        "medium", "remember", "subqueries-in-from",
        "Pre-aggregating data before filtering or joining on the aggregate",
        ["Storing permanent backup copies of frequently queried tables", "Replacing the need for a primary key on the underlying table", "Converting text columns into numeric columns automatically"],
    ),
]

CORRELATED_SUBQUERIES = [
    (
        "\"For each employee, is their salary above the average of their own department?\" breaks the independence of a normal subquery.\n\nWhy does this specific question require a correlated subquery rather than a regular one?",
        "It needs the inner query to recompute for every single outer row, using that row's own department each time, rather than computing one fixed number that gets reused for every row the outer query checks.",
        "easy", "understand", "correlated-subqueries",
        "The inner query must recompute per outer row, using that specific row's department, rather than reusing one fixed result",
        ["It's actually impossible to answer this question using any kind of subquery", "This question can be answered with a regular, uncorrelated subquery just as easily", "It requires a window function instead of any kind of subquery"],
    ),
    (
        "`SELECT e1.employee_name, e1.department, e1.salary FROM employees e1 WHERE e1.salary > (SELECT AVG(e2.salary) FROM employees e2 WHERE e2.department = e1.department);`\n\nWhat do the aliases e1 and e2 each represent?",
        "e1 stands for \"the row currently being checked\" (the outer query), and e2 stands for \"every row used to compute an average\" (the inner query) — both alias the same physical employees table.",
        "easy", "remember", "correlated-subqueries",
        "e1 represents the outer row being checked; e2 represents the rows used to compute the department average",
        ["e1 represents the Engineering department; e2 represents the Sales department", "e1 and e2 are two different tables holding entirely different data", "e1 represents managers; e2 represents their direct reports"],
    ),
    (
        "What's the structural difference between an uncorrelated subquery and a correlated subquery, in terms of how many times each conceptually runs?",
        "An uncorrelated subquery runs exactly once, and its single result is reused for every row the outer query checks. A correlated subquery conceptually reruns once per outer row, because its result depends on a value, like e1.department, that changes from row to row.",
        "medium", "analyze", "correlated-subqueries",
        "An uncorrelated subquery runs once and reuses its result; a correlated subquery conceptually reruns once per outer row",
        ["Both run exactly once, with no difference in behavior between them", "An uncorrelated subquery reruns per row; a correlated subquery runs only once, the reverse of the correct behavior", "A correlated subquery only ever runs zero times, since it depends on the outer query"],
    ),
    (
        "`WHERE EXISTS (SELECT 1 FROM employees e2 WHERE e2.manager_id = e1.employee_id)` finds everyone who manages at least one other employee.\n\nWhy doesn't this correlated EXISTS need a self join or a GROUP BY?",
        "It only asks a yes-or-no question per row (does at least one match exist) rather than pulling in matching columns or needing to count and collapse duplicate rows, which is exactly what a self join or GROUP BY would otherwise be needed for.",
        "medium", "apply", "correlated-subqueries",
        "EXISTS only asks a yes-or-no question per row, without needing to pull in matching columns or collapse duplicates the way a self join or GROUP BY would",
        ["It actually does need a self join internally; EXISTS is just shorthand for one", "GROUP BY and self joins are never valid for finding managers, regardless of approach", "EXISTS cannot be used with correlated conditions at all, only uncorrelated ones"],
    ),
    (
        "Why can correlated subqueries be noticeably slower than an equivalent join, especially on a large table?",
        "Because a correlated subquery's result depends on the outer row, the database often has to evaluate it once per outer row rather than once overall, which can make it noticeably slower than an equivalent join or FROM subquery on a large table.",
        "medium", "understand", "correlated-subqueries",
        "The database often evaluates it once per outer row rather than once overall, unlike an equivalent join",
        ["Correlated subqueries are always slower than joins by a fixed, predictable amount", "Correlated subqueries only run slowly on tables with fewer than ten rows", "There's no real performance difference; the claim in the lesson is a common myth"],
    ),
    (
        "Kabir runs `SELECT e1.employee_name FROM employees e1 WHERE e1.salary > (SELECT e2.salary FROM employees e2 WHERE e2.employee_id = e1.manager_id);` and gets zero rows back.\n\nWhat does this empty result mean?",
        "It's still a correct result — it confirms that nobody in the table currently out-earns their manager, since every manager in this data (Ananya at 95000.00, Sameer at 65000.00) out-earns their own direct reports.",
        "medium", "analyze", "correlated-subqueries",
        "It's a correct, meaningful result confirming that nobody currently out-earns their manager, not a sign of a broken query",
        ["It means the query has a syntax error and needs to be rewritten", "It means the employees table is empty and contains no data at all", "It means every employee is tied exactly with their manager's salary"],
    ),
]

COMMON_TABLE_EXPRESSIONS = [
    (
        "Kabir found himself \"squinting at nested parentheses\" re-reading his FROM-subquery department-average report a week later.\n\nWhat does a CTE (a WITH clause) solve about this?",
        "It names an intermediate result up front, before the main query even begins, letting the rest of the statement read top to bottom in the order the logic actually happens, rather than reading inside-out through deeply nested parentheses.",
        "easy", "understand", "common-table-expressions",
        "It names an intermediate result up front, letting the query read top to bottom instead of inside-out through nested parentheses",
        ["It makes the query run measurably faster than an equivalent nested subquery", "It allows a query to bypass the WHERE clause's aggregate function restriction entirely", "It converts the subquery into a permanent table stored on disk"],
    ),
    (
        "`WITH dept_averages AS (SELECT department, AVG(salary) AS department_avg FROM employees GROUP BY department) SELECT department, department_avg FROM dept_averages WHERE department_avg > (SELECT AVG(salary) FROM employees);`\n\nCompared to the equivalent FROM-subquery version, what's actually different about the CTE version?",
        "The two versions produce an identical result (Engineering as the only department above the company average); the CTE version simply reads in the order a person would naturally explain it out loud, a readability difference, not a functional one.",
        "medium", "apply", "common-table-expressions",
        "Nothing functionally different — the results are identical; the CTE version is simply easier to read top to bottom",
        ["The CTE version returns additional departments the FROM-subquery version misses", "The CTE version can only be used with a single department, unlike the FROM subquery", "The CTE version requires an explicit alias, while the FROM subquery does not"],
    ),
    (
        "A single WITH clause can define more than one CTE, separated by commas.\n\nWhat's the rule about later CTEs referencing earlier ones within the same WITH clause?",
        "Later CTEs are allowed to reference earlier ones, letting a multi-step calculation build up one readable, named piece at a time, such as dept_averages and company_average both being defined and then both referenced together in the final SELECT.",
        "medium", "remember", "common-table-expressions",
        "Later CTEs are allowed to reference earlier ones defined in the same WITH clause",
        ["CTEs can never reference each other under any circumstances", "Only the very first CTE defined can be referenced by the final query", "Every CTE must be entirely self-contained, referencing only real tables"],
    ),
    (
        "The lesson states that neither derived tables nor CTEs are \"inherently faster\" than the other in most modern databases.\n\nWhat is the real, practical difference between them, then?",
        "Readability and maintainability — a CTE gives an intermediate result a name that documents what it represents, and it keeps deeply nested queries from turning into a wall of parentheses that has to be read from the inside out.",
        "medium", "understand", "common-table-expressions",
        "Readability and maintainability, since a CTE names and documents each intermediate step instead of nesting parentheses",
        ["CTEs always execute in parallel, while FROM subqueries always execute sequentially", "CTEs can hold more rows than a FROM subquery is capable of holding", "There is no real difference of any kind between the two approaches"],
    ),
    (
        "What is the scope of a CTE — where is it visible once defined?",
        "Only within the single statement that defines it — a CTE is not a permanent, reusable object like a real table or a view; it exists only for the duration of the one query that names it in its WITH clause.",
        "medium", "remember", "common-table-expressions",
        "Only within the single statement that defines it",
        ["Across every query run in the same database session", "Permanently, until the database server is restarted", "Across every user connected to the same database"],
    ),
    (
        "Can a WHERE subquery, not just a FROM subquery, be pulled out into a named CTE if it makes the query easier to follow?",
        "Yes — any subquery, including the correlated and list-based ones from earlier lessons, can be pulled into a named CTE, such as `WITH high_earners AS (SELECT ... WHERE salary > (SELECT AVG(salary)...)) SELECT ... FROM high_earners`, keeping the final query focused on what happens with the result rather than how it was derived.",
        "medium", "apply", "common-table-expressions",
        "Yes, any subquery, including WHERE-based ones, can be pulled into a named CTE for readability",
        ["No, CTEs can only ever replace FROM subqueries, never WHERE subqueries", "No, only correlated subqueries can be rewritten as CTEs", "Yes, but only if the WHERE subquery uses an aggregate function"],
    ),
]

RECURSIVE_CTES = [
    (
        "A self join can only reach exactly one level up per join written.\n\nWhy does this make a self join insufficient for \"list every person above this employee, all the way to the top\"?",
        "The depth of the hierarchy is not known in advance, and a self join would need a separate join for every possible level, which cannot be written without knowing in advance how many levels the org chart actually has.",
        "easy", "understand", "recursive-ctes",
        "The hierarchy's depth isn't known in advance, and a self join would need one more join per level, which can't be written without knowing how deep it goes",
        ["Self joins can only ever be used on tables with fewer than ten rows", "Self joins cannot reference a column like manager_id under any circumstances", "A self join always returns every employee regardless of the join condition"],
    ),
    (
        "What two parts does a recursive CTE have, joined by UNION ALL?",
        "A base case that starts the recursion, and a recursive case that repeats, each time building on the previous round's result.",
        "easy", "remember", "recursive-ctes",
        "A base case that starts the recursion, and a recursive case that repeats and builds on the previous result",
        ["A WHERE clause and a HAVING clause, joined together", "An INSERT statement and a DELETE statement, run in sequence", "A primary key definition and a foreign key definition"],
    ),
    (
        "In `WITH RECURSIVE reporting_chain AS (SELECT ... WHERE employee_id = 6 UNION ALL SELECT ... FROM employees e JOIN reporting_chain ON e.employee_id = reporting_chain.manager_id) ...`, what does the recursive case's join condition do each round?",
        "It finds whoever manages the person just added in the previous round (matching e.employee_id to the manager_id of the row just found), and that newly found manager becomes part of reporting_chain for the next round, walking one level further up the hierarchy each time.",
        "medium", "analyze", "recursive-ctes",
        "It finds the manager of whoever was just added in the previous round, adding that manager to the result for the next round",
        ["It finds every direct report of whoever was just added, walking down instead of up", "It re-runs the entire base case again from scratch on every round", "It filters out any employee already present in the reporting_chain result"],
    ),
    (
        "Why are both WITH RECURSIVE and UNION ALL specifically required in a recursive CTE, rather than substitutable with other keywords?",
        "WITH RECURSIVE is the keyword that tells the database this CTE is allowed to reference itself (a plain WITH would reject a query that tries to select from its own name inside its own definition); UNION ALL is required rather than a plain JOIN because the recursive case needs to combine the base case's row with every additional row the recursive step produces, round after round, the exact stacking behavior UNION ALL provides.",
        "medium", "understand", "recursive-ctes",
        "WITH RECURSIVE permits the CTE to reference itself; UNION ALL is needed to stack the base case's row with every round's new rows",
        ["Both keywords are purely stylistic and could be swapped for WITH and JOIN with no effect", "WITH RECURSIVE controls stacking; UNION ALL permits self-reference, the reverse of their actual roles", "Neither keyword is actually required; a plain WITH and JOIN would work identically"],
    ),
    (
        "How does the recursive CTE example reverse direction to find everyone BELOW a manager instead of everyone above an employee?",
        "By flipping which side of the join condition matches which column: using `e.manager_id = team_below.employee_id` instead of `e.employee_id = reporting_chain.manager_id`, which walks down the org chart (finding reports) instead of up it (finding managers).",
        "medium", "apply", "recursive-ctes",
        "By flipping the join condition's sides, matching e.manager_id to the CTE's employee_id instead of the other way around",
        ["By changing WITH RECURSIVE to WITH DESCENDING, a separate keyword for downward recursion", "By reversing the order of the base case and the recursive case in the query", "By replacing UNION ALL with INTERSECT to invert the direction of the search"],
    ),
    (
        "When does a recursive CTE stop repeating its recursive case?",
        "The database repeats the recursive case automatically and stops on its own the moment a round produces zero new rows — for example, once it tries to find a manager for the person at the top (like the CEO) and finds none.",
        "medium", "understand", "recursive-ctes",
        "It stops automatically once a round produces zero new rows",
        ["It stops after exactly four rounds, regardless of the data", "It never stops on its own; a LIMIT clause must always be added manually", "It stops as soon as the base case's first row is found"],
    ),
]

SYNTHESIS = [
    (
        "Kabir's WHERE subquery compares against one fixed computed value, his FROM subquery treats an aggregated result as a table to filter or join further, and his correlated subquery recomputes per outer row using that row's own context.\n\nWhich scenario correctly matches each position to its example?",
        "\"Salary greater than the company average\" is a WHERE subquery (one fixed value); \"department averages filtered against the company average\" is a FROM subquery (a derived table); \"salary greater than one's own department's average\" is a correlated subquery (recomputed per row).",
        "medium", "analyze", "subqueries-in-from",
        "Company-average comparison = WHERE subquery; department-averages-as-a-table = FROM subquery; own-department comparison per employee = correlated subquery",
        ["All three examples are actually the same kind of subquery, just written differently", "The FROM subquery example is really a correlated subquery in disguise", "Company-average comparison is a correlated subquery, since it involves salary"],
    ),
    (
        "The recursive CTE lesson builds on both the plain CTE lesson (WITH) and the self-join concept from the joins chapter.\n\nWhy do neither a self join alone nor a plain (non-recursive) CTE alone solve the \"find every manager above this employee, however many levels deep\" problem?",
        "A self join can only reach exactly one level up per join written, requiring a separate join for every possible depth, which is unknown in advance; a plain CTE computes its result once from existing tables and cannot repeat an unknown number of times against its own growing result — only a recursive CTE's base-case-plus-repeating-recursive-case structure can walk an unknown number of levels.",
        "hard", "analyze", "recursive-ctes",
        "A self join needs one join per level (depth unknown in advance); a plain CTE computes once and can't repeat against its own growing result — only a recursive CTE can walk an unknown depth",
        ["A self join alone actually solves this problem perfectly well without any CTE at all", "A plain CTE can already reference itself repeatedly, making WITH RECURSIVE unnecessary", "Both a self join and a plain CTE solve this equally well; RECURSIVE is only a performance optimization"],
    ),
    (
        "NOT IN's NULL trap (from subqueries in WHERE) and the anti-join NULL trap covered earlier in the joins chapter both point to the same safer alternative.\n\nWhat's the throughline connecting these two lessons?",
        "Whenever a comparison is checking for absence (no match, not in a list) against a column or subquery that might contain NULL, NOT IN and its anti-join equivalent both silently produce wrong or empty results, and NOT EXISTS is the consistently safer tool across both contexts, since it tests for the presence of a matching row directly rather than comparing against a list that could include an unknown value.",
        "hard", "analyze", "subqueries-in-where",
        "NOT IN and its anti-join equivalent both break silently on NULLs; NOT EXISTS is the consistently safer alternative in both contexts, since it tests for a matching row directly",
        ["The two lessons are unrelated; NOT IN and anti joins share no common risk", "NOT EXISTS is actually riskier than NOT IN in both of these contexts", "The safer alternative differs between the two lessons: IN for joins, EXISTS for subqueries"],
    ),
    (
        "Kabir's uncorrelated WHERE subquery (filtering employees above the company average) and his FROM subquery (pre-aggregating department averages) are both eventually shown wrapped in a CTE in the CTE lesson.\n\nWhat single benefit does wrapping either kind of subquery in a CTE provide, regardless of which position (WHERE or FROM) the original subquery occupied?",
        "A CTE gives the intermediate result a clear, documented name and lets the query read top to bottom in the order the logic happens, regardless of whether the underlying subquery originally sat inside WHERE or FROM — the readability benefit is the same either way, since CTEs generalize across subquery positions.",
        "medium", "understand", "common-table-expressions",
        "A CTE names and documents the intermediate result and improves top-to-bottom readability, regardless of whether the original subquery was in WHERE or FROM",
        ["Wrapping a WHERE subquery in a CTE makes it run faster, but wrapping a FROM subquery does not", "Only FROM subqueries can actually be wrapped in a CTE; WHERE subqueries cannot", "CTEs only benefit correlated subqueries, not the WHERE or FROM subqueries described here"],
    ),
]

SET1_SOURCES = [
    (WHAT_IS_A_SUBQUERY, 0),
    (SUBQUERIES_IN_WHERE, 0),
    (SUBQUERIES_IN_FROM, 0),
    (CORRELATED_SUBQUERIES, 0),
    (COMMON_TABLE_EXPRESSIONS, 0),
    (RECURSIVE_CTES, 0),
]

SET1 = [src[idx] for src, idx in SET1_SOURCES]
SET1.extend(SYNTHESIS)

SET2 = (
    WHAT_IS_A_SUBQUERY[1:]
    + SUBQUERIES_IN_WHERE[1:]
    + SUBQUERIES_IN_FROM[1:]
    + CORRELATED_SUBQUERIES[1:]
    + COMMON_TABLE_EXPRESSIONS[1:]
    + RECURSIVE_CTES[1:]
)

assert len(SET1) == 10, len(SET1)
assert len(SET2) == 30, len(SET2)


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
            "tags": f"dbms - {set_label}",
            "subjects": "dbms",
            "topics": "advanced-querying-with-sql",
            "subTopics": subtopic,
            "companies": None,
            "option1": options[0],
            "option2": options[1],
            "option3": options[2],
            "option4": options[3],
            "answer": pos,
        })
    return rows


rows1 = build_rows(SET1, "Set 1", "DBMS - MCQ - 5.1.1")
rows2 = build_rows(SET2, "Set 2", "DBMS - MCQ - 5.1.2")
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
ws.title = "DBMS - MCQ - Unit 5.1"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/DBMS/Unit 5 - Advanced Querying with SQL/5.1 - Subqueries and CTEs - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
