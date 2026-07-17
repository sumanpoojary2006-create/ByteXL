import random
import openpyxl

random.seed(67)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])

INSERT_ADDING_ROWS = [
    (
        "Alia needs to add a new student, Diya Kulkarni, to the students table (student_id, full_name, email, city, phone, joined_on).\n\nWhich statement correctly follows the standard shape of INSERT: name the table, name the columns, then supply values in the same order?",
        "`INSERT INTO students (student_id, full_name, email, city, phone, joined_on) VALUES (9, 'Diya Kulkarni', 'diya.kulkarni@campusmail.edu', 'Pune', '9845066666', '2025-02-14');` follows the standard shape exactly.",
        "easy", "apply", "insert-adding-new-rows",
        "INSERT INTO students (student_id, full_name, email, city, phone, joined_on) VALUES (9, 'Diya Kulkarni', 'diya.kulkarni@campusmail.edu', 'Pune', '9845066666', '2025-02-14');",
        ["INSERT students VALUES ('Diya Kulkarni', 9, 'Pune');", "ADD ROW TO students (9, 'Diya Kulkarni', 'Pune');", "INSERT INTO students SET student_id = 9, full_name = 'Diya Kulkarni';"],
    ),
    (
        "In `INSERT INTO students (student_id, full_name, email, city, phone, joined_on) VALUES (...)`, what job does the column list right after the table name actually do?",
        "It tells the database exactly which column each value in VALUES belongs to, so the ninth value in a row never gets misread as something it isn't — it maps values positionally to the named columns, not the table's original creation order.",
        "medium", "understand", "insert-adding-new-rows",
        "It tells the database exactly which column each value corresponds to, based on the names listed, not the table's original creation order",
        ["It has no functional effect and exists purely for documentation", "It deletes any existing columns not mentioned in the list", "It creates new columns in the table matching the names listed"],
    ),
    (
        "Registration week brings in Kabir Sethi and Meera Das at once. Which statement correctly inserts both students in a single INSERT statement?",
        "`INSERT INTO students (student_id, full_name, email, city, phone, joined_on) VALUES (10, 'Kabir Sethi', 'kabir.sethi@campusmail.edu', 'Chennai', '9845077777', '2025-02-15'), (11, 'Meera Das', 'meera.das@gmail.com', NULL, '9845088888', '2025-02-15');` — INSERT accepts more than one row inside a single statement, each a parenthesized group separated by a comma.",
        "medium", "apply", "insert-adding-new-rows",
        "INSERT INTO students (...) VALUES (10, 'Kabir Sethi', ...), (11, 'Meera Das', ...); — one statement, two comma-separated row groups",
        ["Two separate INSERT statements are always required; batching rows in one is not valid SQL", "INSERT INTO students (...) VALUES (10, 'Kabir Sethi'); AND VALUES (11, 'Meera Das');", "INSERT INTO students (...) VALUES (10, 11), ('Kabir Sethi', 'Meera Das');"],
    ),
    (
        "Beyond being shorter to type, why does the lesson say batching multiple rows into a single INSERT statement matters?",
        "The database treats the whole batch as one unit of work, which matters once a table has rules like PRIMARY KEY that must hold for every row in the statement together, giving a kind of shared correctness guarantee across the batch.",
        "medium", "analyze", "insert-adding-new-rows",
        "The database treats the whole batch as one unit of work, which matters for table rules like PRIMARY KEY that must hold across every row together",
        ["It makes each individual row insert faster to type character by character", "It automatically assigns a shared foreign key to every row in the batch", "It has no real benefit beyond typing convenience; the effect is identical to separate statements"],
    ),
    (
        "`INSERT INTO courses VALUES (106, 'Operating Systems', 'Computer Science', 4);` omits the column list entirely and relies on the table's original column order (course_id, title, department, credits).\n\nWhat risk does this positional approach carry that naming columns explicitly avoids?",
        "If a future change to the table adds a column in the middle, or if two values are simply written in the wrong order by mistake, a positional INSERT places every later value into the wrong column with no error at all, since the database has no way to know a value was misplaced.",
        "hard", "analyze", "insert-adding-new-rows",
        "A table change or a simple ordering mistake can silently place values in the wrong columns, with no error raised at all",
        ["There is no real risk; positional inserts are always exactly as safe as named ones", "The statement will always fail with a syntax error if the order is wrong", "Positional inserts are actually faster to execute than named-column inserts"],
    ),
    (
        "A new student, Farhan Ali, registers from Hyderabad with no phone number on file yet, and needs student_id 12.\n\nWhich statement correctly adds him, leaving phone appropriately blank?",
        "`INSERT INTO students (student_id, full_name, email, city, phone, joined_on) VALUES (12, 'Farhan Ali', 'farhan.ali@campusmail.edu', 'Hyderabad', NULL, '2025-02-16');` uses NULL for the missing phone value, exactly as it should be for a value that genuinely hasn't been provided.",
        "medium", "apply", "insert-adding-new-rows",
        "INSERT INTO students (...) VALUES (12, 'Farhan Ali', 'farhan.ali@campusmail.edu', 'Hyderabad', NULL, '2025-02-16');",
        ["INSERT INTO students (...) VALUES (12, 'Farhan Ali', 'farhan.ali@campusmail.edu', 'Hyderabad', '', '2025-02-16');", "INSERT INTO students (...) VALUES (12, 'Farhan Ali', 'farhan.ali@campusmail.edu', 'Hyderabad', '2025-02-16');", "INSERT INTO students (...) VALUES (12, 'Farhan Ali', 'farhan.ali@campusmail.edu', 'Hyderabad', 0, '2025-02-16');"],
    ),
]

UPDATE_MODIFYING_ROWS = [
    (
        "Rohit needs to correct Varun Nair's city from Chennai to Bengaluru, one existing fact about one existing student that needs to change, not a new row and not a removal.\n\nWhich statement is the tool for this job?",
        "UPDATE — the statement that modifies values already sitting in a table, exactly the job of correcting one existing fact without creating a new row or removing an existing one.",
        "easy", "remember", "update-modifying-rows-safely",
        "UPDATE",
        ["INSERT", "DELETE", "REPLACE"],
    ),
    (
        "Before touching anything, Rohit runs `SELECT student_id, full_name, city FROM students WHERE student_id = 3;` and confirms exactly one row, Varun Nair in Chennai.\n\nWhat does the lesson call this step, and why does it matter?",
        "This is described as \"not an extra step, it is the actual safety check\" — running the exact same condition as a SELECT first lets Rohit know, with certainty, which row his UPDATE is about to touch, because he's already seen it with his own eyes before changing anything.",
        "medium", "understand", "update-modifying-rows-safely",
        "It's the actual safety check, confirming with certainty which row will be touched before the UPDATE runs",
        ["It's an optional courtesy step with no real bearing on safety", "It's required by SQL syntax before any UPDATE statement can run", "It automatically creates a backup of the row before it changes"],
    ),
    (
        "Which statement correctly changes only Varun Nair's (student_id 3) city to Bengaluru, leaving every other student and every other column untouched?",
        "`UPDATE students SET city = 'Bengaluru' WHERE student_id = 3;` — WHERE identifies the one row (student_id = 3), and SET says which column changes and to what; everything else about that row, and every other row, is left exactly as it was.",
        "easy", "apply", "update-modifying-rows-safely",
        "UPDATE students SET city = 'Bengaluru' WHERE student_id = 3;",
        ["UPDATE students SET city = 'Bengaluru';", "UPDATE students WHERE student_id = 3 SET city = 'Bengaluru';", "SET city = 'Bengaluru' IN students WHERE student_id = 3;"],
    ),
    (
        "Rohit accidentally runs `UPDATE students SET city = 'Bengaluru';` with no WHERE clause at all.\n\nWhat happens, and why is this described as especially dangerous?",
        "Every single student now shows Bengaluru as their city, not just Varun, since UPDATE with no WHERE clause treats every row in the table as the target. It's especially dangerous because there's no confirmation prompt, no warning about how many rows are about to change, and no undo button once the statement finishes.",
        "medium", "analyze", "update-modifying-rows-safely",
        "Every row in the table gets updated, not just the intended one, with no warning or undo once the statement finishes",
        ["Nothing happens; PostgreSQL requires a WHERE clause and rejects the statement", "Only the first row in the table gets updated by default", "The statement fails silently and no changes are made at all"],
    ),
    (
        "The lesson warns that \"a WHERE clause that is too broad causes the exact same damage as no WHERE clause at all.\" Which example illustrates this specific danger?",
        "Writing `WHERE city = 'Chennai'` when the intent was `WHERE student_id = 3` would update every student living in Chennai, not the one student Rohit actually meant — a WHERE clause that's present but not specific enough still causes broad, unintended damage.",
        "medium", "apply", "update-modifying-rows-safely",
        "Writing WHERE city = 'Chennai' when the intent was WHERE student_id = 3, accidentally updating every Chennai resident instead of one student",
        ["Writing WHERE student_id = 3 exactly as intended, which is always considered too broad", "Omitting the SET clause entirely while keeping a correct WHERE clause", "Using UPDATE instead of INSERT for a brand new student record"],
    ),
    (
        "`SET city = 'Mumbai', phone = '9845099999' WHERE student_id = 5;` updates both Yusuf Khan's city and phone in one statement.\n\nWhat does this demonstrate about SET?",
        "SET accepts more than one column, separated by commas, all applied together in a single statement, covered by the same single WHERE condition, so there's only one row to check rather than two separate statements to keep track of.",
        "medium", "understand", "update-modifying-rows-safely",
        "SET can update multiple columns at once, separated by commas, all under one shared WHERE condition",
        ["SET can only ever change one column per UPDATE statement", "Updating two columns always requires two separate UPDATE statements", "SET requires a separate WHERE clause for each column being changed"],
    ),
]

DELETE_REMOVING_ROWS = [
    (
        "Rahul Verma drops Linear Algebra, and his enrollment row needs to be removed from the table entirely, not marked, not changed, simply gone.\n\nWhich statement is the tool for this job?",
        "DELETE — the statement Priyanka uses, applying the exact same caution Rohit learned with UPDATE, since a statement that removes rows deserves the same care as one that changes them.",
        "easy", "remember", "delete-removing-rows",
        "DELETE",
        ["REMOVE", "DROP", "TRUNCATE"],
    ),
    (
        "Before deleting anything, Priyanka runs `SELECT enrollment_id, student_id, course_id, enrolled_on FROM enrollments WHERE enrollment_id = 9;` and confirms exactly one row.\n\nWhat is this step doing, and how does it compare to Rohit's habit before an UPDATE?",
        "It's the same safety habit applied to deletion: know precisely what is about to disappear before running anything that removes it, using the exact condition the DELETE is about to use.",
        "medium", "apply", "delete-removing-rows",
        "It's the same check-before-acting safety habit used for UPDATE, now applied before a DELETE",
        ["It's a completely different habit unique to DELETE, unrelated to UPDATE's safety check", "It's unnecessary, since DELETE cannot remove more than one row at a time", "It's required by SQL syntax; DELETE cannot run without a preceding SELECT"],
    ),
    (
        "Which statement correctly removes only Rahul Verma's Linear Algebra enrollment (enrollment_id 9), leaving the other nine enrollments untouched?",
        "`DELETE FROM enrollments WHERE enrollment_id = 9;` — DELETE FROM names the table, WHERE narrows which rows are removed, and unlike UPDATE, DELETE has no SET clause since there's nothing to set; a deleted row simply stops existing.",
        "easy", "apply", "delete-removing-rows",
        "DELETE FROM enrollments WHERE enrollment_id = 9;",
        ["DELETE enrollments SET enrollment_id = 9;", "REMOVE FROM enrollments WHERE enrollment_id = 9;", "DELETE FROM enrollments SET removed = TRUE WHERE enrollment_id = 9;"],
    ),
    (
        "`DELETE FROM enrollments;` is run with no WHERE clause at all.\n\nWhat happens, and why does the lesson call this \"one of the most dangerous single lines a person can type into a database\"?",
        "Every single enrollment row, all ten of them, is removed, not just Rahul's. It's dangerous because there was no warning, no count of rows about to disappear, and once the statement finishes there is no ordinary way to bring those rows back.",
        "medium", "analyze", "delete-removing-rows",
        "Every row in the table is removed, with no warning and no ordinary way to undo it once the statement finishes",
        ["Nothing happens; DELETE always requires a WHERE clause to run at all", "Only the most recently inserted row is removed by default", "The table itself is deleted entirely, not just its rows"],
    ),
    (
        "The lesson describes two \"failure modes\" for DELETE that look nearly identical in effect. What are they?",
        "No WHERE clause at all, which removes every row with no warning; and a WHERE clause that is merely too broad, like `WHERE course_id = 103` when the intent was `WHERE enrollment_id = 9`, which removes every enrollment in that course across every student rather than the one row intended.",
        "medium", "understand", "delete-removing-rows",
        "No WHERE clause at all, and a WHERE clause that's present but too broad, matching far more rows than intended",
        ["Using DELETE instead of UPDATE, and using UPDATE instead of DELETE", "Deleting from the wrong table, and deleting from the right table", "Running DELETE twice in a row, and running it only once"],
    ),
    (
        "Priyanka's safe DELETE reuses `WHERE student_id = 5 AND course_id = 101` from an earlier SELECT check. The lesson notes that `student_id = 5` alone \"might one day match more than one row.\"\n\nWhy does combining two conditions with AND make this DELETE safer?",
        "If Yusuf ever enrolls in a second course, student_id = 5 alone would match more than one enrollment row; combining it with course_id = 101 using AND narrows the match down to exactly the one enrollment intended, even as the data grows over time.",
        "hard", "analyze", "delete-removing-rows",
        "Combining conditions with AND keeps the match narrowed to exactly one row, even as the student enrolls in more courses over time",
        ["AND makes the query run faster, which is the only reason it's used here", "A single condition can never match more than one row, so AND is purely stylistic here", "AND is required by SQL syntax whenever DELETE is used with WHERE"],
    ),
]

RETURNING_CLAUSE = [
    (
        "Zara has been running INSERT, UPDATE, and DELETE statements, then typing a separate SELECT afterward just to see what happened.\n\nWhat clause does a senior developer point her toward that hands back confirmation immediately, as part of the very same statement?",
        "RETURNING — a clause that hands back the affected row as part of the very same INSERT, UPDATE, or DELETE statement, with no separate SELECT needed afterward.",
        "easy", "remember", "returning-clause",
        "RETURNING",
        ["CONFIRM", "OUTPUT", "ECHO"],
    ),
    (
        "`INSERT INTO enrollments (...) VALUES (6, 5, 101, '2025-02-09', NULL) RETURNING enrollment_id, student_id, course_id, enrolled_on;` hands back the new row's values in one pass.\n\nWhen does RETURNING matter most, according to the lesson?",
        "It matters most when a column's value is generated by the database itself, such as a sequence-based identifier the caller never typed in — RETURNING is how the caller learns what value the database actually chose, at the exact moment the row is created.",
        "medium", "understand", "returning-clause",
        "When a column's value is generated by the database itself, letting the caller learn that value at the moment of creation",
        ["It only matters for DELETE statements, never for INSERT or UPDATE", "It matters only when no columns were named in the original statement", "RETURNING only works when the table has no primary key defined"],
    ),
    (
        "`UPDATE students SET city = 'Chennai' WHERE student_id = 2 RETURNING student_id, full_name, city;` is run.\n\nWhat does the result show, and what would RETURNING show if the WHERE condition had matched no rows at all?",
        "The result shows Neha Sharma with city already reading Chennai, confirming both which row changed and its new value. If the WHERE condition matched no rows, RETURNING would come back empty, itself a useful signal that nothing was touched.",
        "medium", "apply", "returning-clause",
        "It shows the updated row with its new value; if no rows matched, RETURNING would come back empty, signaling nothing was touched",
        ["It shows the row's old value before the change, not the new one", "It always shows every row in the table, regardless of the WHERE condition", "An empty RETURNING result means the UPDATE statement itself failed with an error"],
    ),
    (
        "`DELETE FROM enrollments WHERE enrollment_id = 5 RETURNING enrollment_id, student_id, course_id, grade;` is run.\n\nWhat does the returned row represent, and why is this described as \"often more useful than it first sounds\"?",
        "It hands back the row exactly as it looked the instant before it was removed, the last view anyone gets of it. This is useful for something like a support workflow logging exactly what was removed, using this single result, without needing to have queried the row moments earlier and hoped nothing changed in between.",
        "medium", "analyze", "returning-clause",
        "It shows the row exactly as it looked right before deletion, useful for logging what was removed without a separate earlier query",
        ["It shows a blank row, since the data no longer exists after deletion", "It shows every row that was NOT deleted, as a confirmation of what remains", "It shows the row as it will look after being restored from a backup"],
    ),
    (
        "Why does the lesson say RETURNING \"beats a separate SELECT,\" specifically in a busy system with many things happening at once?",
        "A modification and a follow-up SELECT are two statements sent one after another, and the row a second SELECT sees isn't guaranteed to be in the exact state the first statement just left it in, since something else could have touched it in between. RETURNING sidesteps that gap entirely by reporting on the very same rows the modification just touched, as part of the very same statement.",
        "hard", "analyze", "returning-clause",
        "A separate SELECT could see a row changed by something else in between; RETURNING reports on exactly the rows the modification just touched, with no gap",
        ["RETURNING is simply shorter to type, with no real correctness advantage", "A separate SELECT is always faster to run than RETURNING", "RETURNING and a separate SELECT are functionally identical in every situation"],
    ),
    (
        "Which statement correctly inserts a new student, Kabir Sethi, and confirms the row in the same statement, with no separate SELECT afterward?",
        "`INSERT INTO students (student_id, full_name, email, city, phone, joined_on) VALUES (6, 'Kabir Sethi', 'kabir.sethi@campusmail.edu', 'Chennai', '9845077777', '2025-02-16') RETURNING student_id, full_name, city;` confirms the row within the INSERT itself.",
        "medium", "apply", "returning-clause",
        "INSERT INTO students (...) VALUES (6, 'Kabir Sethi', ...) RETURNING student_id, full_name, city;",
        ["INSERT INTO students (...) VALUES (6, 'Kabir Sethi', ...); SELECT * FROM students WHERE student_id = 6;", "INSERT INTO students (...) VALUES (6, 'Kabir Sethi', ...) CONFIRM student_id, full_name, city;", "INSERT INTO students (...) VALUES (6, 'Kabir Sethi', ...) OUTPUT student_id, full_name, city;"],
    ),
]

UPSERT_ON_CONFLICT = [
    (
        "Aditya is processing enrollment submissions where some student-course pairings are brand new and others already exist with a grade that just needs correcting, and he can't tell which is which until he checks.\n\nWhat single clause does PostgreSQL provide for inserting a row if it's new and updating it if it already exists?",
        "ON CONFLICT — the clause behind what's commonly called an upsert, letting a single statement insert a new row or update an existing one, decided by the database itself rather than a separate check-then-decide step.",
        "easy", "remember", "upsert-and-on-conflict",
        "ON CONFLICT",
        ["IF EXISTS", "MERGE INTO", "ON DUPLICATE"],
    ),
    (
        "Aditya's enrollments table needs a `UNIQUE (student_id, course_id)` constraint before ON CONFLICT can do anything useful.\n\nWhy is this constraint a prerequisite for an upsert?",
        "An upsert only makes sense once the database has a rule to check a new row against; without the UNIQUE constraint, PostgreSQL would have no rule saying two rows with the same student_id and course_id are a problem, and there would be nothing for ON CONFLICT to \"conflict\" against at all.",
        "medium", "understand", "upsert-and-on-conflict",
        "Without a UNIQUE constraint, there is no rule defining what counts as a conflict, so ON CONFLICT has nothing to react to",
        ["The constraint is not actually required; ON CONFLICT works without it", "The constraint is only needed for the DO NOTHING variant, not DO UPDATE", "The constraint automatically deletes any duplicate rows before the INSERT runs"],
    ),
    (
        "Neha Sharma's Database Systems enrollment already exists with no grade recorded. Aditya runs `INSERT INTO enrollments (...) VALUES (4, 2, 101, '2025-02-02', 'B+') ON CONFLICT (student_id, course_id) DO UPDATE SET grade = EXCLUDED.grade RETURNING enrollment_id, ...;`\n\nWhat does PostgreSQL actually do, step by step?",
        "It tries the INSERT exactly as written, detects that student_id 2 and course_id 101 already match the UNIQUE constraint, and instead of raising an error, runs the DO UPDATE SET instead, targeting the row that was already there — the result shows the existing enrollment_id 2, not a new row.",
        "medium", "apply", "upsert-and-on-conflict",
        "It tries the INSERT, detects the conflict against the UNIQUE constraint, and runs DO UPDATE SET on the existing row instead of inserting a new one",
        ["It always inserts a brand new row alongside the existing one, creating a duplicate", "It raises an error and stops, since a conflict was detected", "It silently ignores the entire statement and does nothing at all"],
    ),
    (
        "In `DO UPDATE SET grade = EXCLUDED.grade`, what does EXCLUDED.grade specifically refer to?",
        "EXCLUDED.grade refers to the grade value from the row that was proposed for insertion, the B+ that never actually got inserted, letting the UPDATE branch reuse that proposed value without retyping it.",
        "medium", "understand", "upsert-and-on-conflict",
        "The grade value from the row that was proposed for insertion but didn't actually get inserted due to the conflict",
        ["The grade value currently stored in the existing, conflicting row", "The grade value from a completely unrelated row in the table", "A placeholder that always evaluates to NULL regardless of the insert"],
    ),
    (
        "Aditya runs the exact same ON CONFLICT statement for Varun Nair registering for Data Structures (course_id 102), a pairing that has never been submitted before, and enrollment_id 5 appears as a genuinely new row.\n\nWhy does the identical statement behave differently this time?",
        "ON CONFLICT only changes behavior when a conflict is actually detected; since student_id 3 and course_id 102 had never been paired before, there was no conflict to react to, so the INSERT proceeds exactly as it would have without the clause at all.",
        "medium", "analyze", "upsert-and-on-conflict",
        "ON CONFLICT only changes behavior when a conflict is actually detected; with no matching existing row, the INSERT proceeds normally",
        ["The statement actually failed silently and enrollment_id 5 is a database error artifact", "ON CONFLICT always creates a new row regardless of whether a conflict exists", "The UNIQUE constraint was automatically disabled for this particular insert"],
    ),
    (
        "Aditya's original instinct, a SELECT to check for the row followed by an INSERT or UPDATE depending on the answer, is described as risky if two submissions for the same pairing are processed at nearly the same moment.\n\nWhat specifically goes wrong with the check-then-decide approach that ON CONFLICT avoids?",
        "Both submissions could run their SELECT, both could see no existing row yet, and both could then attempt an INSERT, one of which fails or, worse, both of which succeed and violate the very constraint meant to prevent duplicates — ON CONFLICT avoids this because the check and the action happen as one atomic statement with no gap for another process to interfere.",
        "hard", "analyze", "upsert-and-on-conflict",
        "Two near-simultaneous submissions could both see no existing row and both attempt an insert, risking a duplicate or a failure — ON CONFLICT closes that gap atomically",
        ["Nothing actually goes wrong; the check-then-decide approach is exactly as safe as ON CONFLICT", "The SELECT step would always run slower than ON CONFLICT, with no correctness difference", "The risk only applies to DELETE statements, not to INSERT or UPDATE"],
    ),
]

DISCIPLINE = [
    (
        "Naveen notices that Alia, Rohit, Priyanka, Zara, and Aditya all pause and check before committing to an UPDATE or DELETE, never typing one the moment they think of it.\n\nWhat single underlying idea does the lesson say all of INSERT, UPDATE, DELETE, RETURNING, and ON CONFLICT really come down to?",
        "That changing data is a fundamentally different act from reading it, and it calls for discipline, a habit of checking before acting that a SELECT never demanded in the first place.",
        "easy", "understand", "why-modification-needs-discipline",
        "Changing data is fundamentally different from reading it, and requires a habit of checking before acting",
        ["All five statements are really just different names for the same SQL keyword", "Modification statements should always be avoided in favor of SELECT wherever possible", "Discipline only matters for DELETE; the other four statements are inherently safe"],
    ),
    (
        "A SELECT with a wrong WHERE clause returns the wrong rows on screen, and Naveen can simply notice, fix the condition, and run it again with nothing lost.\n\nHow is a mistaken UPDATE or DELETE fundamentally different?",
        "An UPDATE or DELETE with a wrong or missing WHERE clause changes or removes rows permanently, and by the time the mistake is noticed, the correct data may no longer exist anywhere to compare against — reading forgives mistakes, writing does not.",
        "easy", "understand", "why-modification-needs-discipline",
        "UPDATE and DELETE mistakes are permanent, and the correct data may no longer exist anywhere to recover once the mistake is noticed",
        ["There is no real difference; both kinds of mistakes are equally easy to reverse", "UPDATE mistakes are permanent but DELETE mistakes are always automatically reversible", "SELECT mistakes are actually more dangerous, since they run more frequently"],
    ),
    (
        "In `SELECT ... WHERE student_id = 2 AND course_id = 101; UPDATE enrollments SET grade = 'B' WHERE student_id = 2 AND course_id = 101 RETURNING ...;`, the lesson stacks three separate habits.\n\nWhat are they?",
        "Checking first (the SELECT), matching the condition exactly (reusing the identical WHERE rather than a rewritten or loosened version), and confirming immediately (RETURNING) — none individually difficult, but they must be done on purpose rather than skipped.",
        "medium", "remember", "why-modification-needs-discipline",
        "Checking first, matching the condition exactly, and confirming immediately",
        ["Writing fast, testing rarely, and confirming never", "Checking first, ignoring the result, and running the UPDATE anyway", "Matching the condition loosely, confirming twice, and skipping the check"],
    ),
    (
        "Naveen has started reading his own WHERE clause out loud before running anything that changes a row.\n\nWhat does the lesson say this small ritual is meant to catch?",
        "It's a short pause built into the process itself, asking: what table, what condition, how many rows should this match, and does the statement in front of me actually say that — a habit that catches a surprising number of mistakes before they become permanent.",
        "medium", "understand", "why-modification-needs-discipline",
        "It catches mistakes in the table, condition, or expected row count before they become permanent by forcing a deliberate pause",
        ["It's purely a personal quirk with no described benefit in the lesson", "It's required because PostgreSQL cannot parse silent, unspoken queries", "It only catches syntax errors, not logical mistakes in the condition"],
    ),
    (
        "`DELETE FROM enrollments WHERE student_id = 4 AND course_id = 102 RETURNING enrollment_id, student_id, course_id;` shows exactly one row leaving the table.\n\nWhat does the lesson say this visible confirmation turns \"I think that worked\" into?",
        "\"I can see that it worked\" — RETURNING is not just a convenience for skipping a second query, it's a built-in confirmation step that happens whether or not anyone remembers to ask for it separately, arriving in the same breath as the DELETE itself.",
        "medium", "apply", "why-modification-needs-discipline",
        "\"I can see that it worked,\" turning an assumption into a visible, confirmed fact",
        ["\"I hope that worked,\" adding more uncertainty rather than less", "\"That definitely failed,\" since RETURNING only shows errors, not successes", "Nothing changes; RETURNING adds no new information beyond a plain DELETE"],
    ),
    (
        "The chapter's conclusion says real systems go further still, offering a way to group several changes together so that if something goes wrong partway through, every part of the group can be undone at once.\n\nWhat idea is the lesson gesturing toward as \"worth carrying forward\" beyond individual statements?",
        "The idea of treating several related modifications as a single unit that either all succeed or all fail together, rather than leaving data half-changed if something goes wrong midway, an idea that extends the same checking discipline from a single statement to a group of them.",
        "hard", "analyze", "why-modification-needs-discipline",
        "Treating several related modifications as one unit that succeeds or fails together, rather than leaving data half-changed partway through",
        ["The idea that RETURNING should always be paired with ON CONFLICT in every statement", "The idea that DELETE should never be used without first running an UPDATE", "The idea that every table should be backed up manually before any modification"],
    ),
]

SYNTHESIS = [
    (
        "Rohit's safe UPDATE habit and Priyanka's safe DELETE habit both follow the exact same three-step pattern: SELECT with the target condition, run the modification with the identical condition, then confirm.\n\nWhat does this shared pattern reveal about how the lesson treats UPDATE and DELETE, compared to how it treats SELECT?",
        "UPDATE and DELETE are treated as fundamentally riskier than SELECT because their mistakes are permanent, so both are wrapped in the same deliberate check-then-act discipline, while SELECT, whose mistakes cost nothing more than a glance and a retry, never needs that same ritual.",
        "medium", "analyze", "why-modification-needs-discipline",
        "UPDATE and DELETE are treated as riskier than SELECT because their mistakes are permanent, so both get wrapped in the same check-then-act discipline",
        ["UPDATE, DELETE, and SELECT are all treated as equally risky and require identical rituals", "SELECT actually requires more caution than UPDATE or DELETE, according to the lesson", "The shared pattern is coincidental and has no real explanation in the lesson"],
    ),
    (
        "Zara's RETURNING clause and Aditya's ON CONFLICT clause both let a single SQL statement do more than one previously separate step used to require.\n\nWhat separate, two-step process does each one collapse into a single atomic statement?",
        "RETURNING collapses \"modify, then run a separate SELECT to see the result\" into one statement. ON CONFLICT collapses \"SELECT to check if a row exists, then decide whether to INSERT or UPDATE\" into one statement — both remove a risky gap between checking and acting.",
        "medium", "analyze", "upsert-and-on-conflict",
        "RETURNING collapses \"modify then re-query\" into one step; ON CONFLICT collapses \"check then decide insert-or-update\" into one step",
        ["Both clauses collapse exactly the same two-step process: INSERT followed by DELETE", "RETURNING collapses ON CONFLICT's job, and ON CONFLICT collapses RETURNING's job, the reverse of the correct pairing", "Neither clause actually collapses any previously separate steps"],
    ),
    (
        "Rohit's UPDATE-without-WHERE mistake changes every row in the table, and Priyanka's DELETE-without-WHERE mistake removes every row in the table.\n\nWhat single structural fact about WHERE explains why both mistakes produce such similarly catastrophic results?",
        "WHERE narrows a statement's target down from \"every row in the table\" to a specific subset; without it, both UPDATE and DELETE default to treating the entire table as their target, since there's no narrowing condition to limit their scope at all.",
        "hard", "analyze", "update-modifying-rows-safely",
        "Without WHERE, both statements default to treating every row in the table as their target, since nothing narrows their scope",
        ["UPDATE and DELETE only affect the first row by default, and WHERE has no real bearing on scope", "WHERE only matters for DELETE; UPDATE is always automatically limited to one row", "The two mistakes are unrelated coincidences with no shared structural explanation"],
    ),
    (
        "Across INSERT (naming columns explicitly), UPDATE and DELETE (checking with SELECT first), and ON CONFLICT (avoiding a check-then-decide race), the chapter's conclusion says the common thread is \"knowing, before a statement runs, exactly what it is about to do.\"\n\nHow does naming columns explicitly in INSERT fit this same theme, even though INSERT doesn't risk touching existing rows the way UPDATE and DELETE do?",
        "Naming columns explicitly removes the same kind of blind trust in assumed structure that a missing WHERE clause represents for UPDATE or DELETE: relying on column position (rather than names) risks silently misplacing values if the table's structure changes or the order is misremembered, exactly the same \"know what you're doing before it runs\" discipline applied to a different kind of risk.",
        "hard", "analyze", "insert-adding-new-rows",
        "Naming columns removes reliance on assumed table structure, the same \"know what will happen before running it\" discipline applied to INSERT's own kind of risk",
        ["Naming columns has nothing to do with discipline; it's purely a stylistic preference", "INSERT carries no real risk at all, so this comparison doesn't actually apply", "Naming columns only matters for performance, not for correctness or safety"],
    ),
]

SET1_SOURCES = [
    (INSERT_ADDING_ROWS, 0),
    (UPDATE_MODIFYING_ROWS, 0),
    (DELETE_REMOVING_ROWS, 0),
    (RETURNING_CLAUSE, 0),
    (UPSERT_ON_CONFLICT, 0),
    (DISCIPLINE, 0),
]

SET1 = [src[idx] for src, idx in SET1_SOURCES]
SET1.extend(SYNTHESIS)

SET2 = (
    INSERT_ADDING_ROWS[1:]
    + UPDATE_MODIFYING_ROWS[1:]
    + DELETE_REMOVING_ROWS[1:]
    + RETURNING_CLAUSE[1:]
    + UPSERT_ON_CONFLICT[1:]
    + DISCIPLINE[1:]
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
            "topics": "sql-essentials",
            "subTopics": subtopic,
            "companies": None,
            "option1": options[0],
            "option2": options[1],
            "option3": options[2],
            "option4": options[3],
            "answer": pos,
        })
    return rows


rows1 = build_rows(SET1, "Set 1", "DBMS - MCQ - 3.4.1")
rows2 = build_rows(SET2, "Set 2", "DBMS - MCQ - 3.4.2")
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
ws.title = "DBMS - MCQ - Unit 3.4"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/DBMS/Unit 3 - SQL Essentials/3.4 - Modifying Data - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
