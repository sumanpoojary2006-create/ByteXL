import random
import openpyxl

random.seed(29)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])

TABLES_ROWS_COLUMNS = [
    (
        "Meera used to have forty loose mark sheets, one per student, and answering \"which students scored above 80 in Maths?\" meant checking every sheet by hand. After she ruled a grid with Roll No, Name, Maths, Science, and English as column headings, the same question took ten seconds.\n\nWhy did the grid make the question so much faster to answer?",
        "Once every student's marks sit in the same row order with the same columns, Meera can scan a single column (Maths) mechanically instead of hunting through each separate sheet for the right line.",
        "easy", "understand", "tables-rows-and-columns",
        "Every row shares the same columns in the same order, so scanning one column works mechanically instead of searching sheet by sheet",
        ["The grid contains fewer facts than the forty loose sheets did", "Grids are automatically faster than paper regardless of how the data is arranged", "The vice-principal only asked about a single student, not the whole class"],
    ),
    (
        "Meera's ruled grid, with a name (\"Students\") and one row per student following the same columns, is described as the relational building block a database uses to hold this kind of data.\n\nWhat is this structure called?",
        "A named collection of rows that all describe the same kind of thing, with consistent columns, is exactly what a database calls a table.",
        "easy", "remember", "tables-rows-and-columns",
        "A table",
        ["A domain", "A constraint", "A schema diagram"],
    ),
    (
        "In Meera's grid, the row for roll number 103 holds Divya Nair's roll number, name, and marks, and nobody else's.\n\nWhat does this row represent in relational terms?",
        "A row is one specific instance of the kind of thing the table is about — here, one particular student, Divya Nair, and her data alone.",
        "easy", "understand", "tables-rows-and-columns",
        "One specific instance of the thing the table is about — this one student's own record",
        ["A named attribute shared by every student in the table", "The complete set of legal values for the Maths column", "A rule the database enforces on every student's data"],
    ),
    (
        "Someone scribbles a \"Sports Quota\" note only in the margin next to Rohit's row, with no matching entry for any other student.\n\nWhy does a relational table resist this kind of one-off addition?",
        "Every row in a table is expected to share exactly the same columns, meaning the same thing for each row. An ad hoc note only one row has breaks that uniformity, and if Sports Quota genuinely matters, it should become a proper column every row has, even if most rows leave it blank.",
        "medium", "analyze", "tables-rows-and-columns",
        "Every row must share exactly the same columns; an ad hoc field only one row has breaks the uniformity a table depends on",
        ["Because tables can only ever hold exactly five columns", "Because Rohit's row would otherwise be deleted automatically", "Tables don't actually resist this; extra one-off fields are the normal way to add detail"],
    ),
    (
        "Meera's forty-sheet system was manageable, but the same reasoning has to hold up for a relational database managing four hundred thousand student records instead of forty.\n\nWhy does the uniformity of rows and columns matter even more at that scale?",
        "If some rows quietly had \"Maths\" and others had \"Mathematics\" or \"Maths (retest)\", a column scan would stop being reliable. This same uniformity is precisely what lets a table be processed quickly and correctly by a computer at massive scale.",
        "hard", "analyze", "tables-rows-and-columns",
        "Uniform columns are what let a computer process and search the table mechanically and correctly, even as row count grows enormously",
        ["At larger scale, exact column uniformity stops mattering because computers can handle irregular data automatically", "Scale has no real effect; forty rows and four hundred thousand rows are equally easy to search without structure", "Larger tables need fewer columns to stay fast"],
    ),
]

ATTRIBUTES_AND_DOMAINS = [
    (
        "A new gym member fills in Kabir's signup form and, in a hurry, writes \"twenty-five\" under \"Age\" instead of a number.\n\nWhat has this entry violated?",
        "The Age column's domain is the set of legal values it may hold — whole numbers in a sensible range. \"Twenty-five\" written as words falls outside that domain, even though it describes a valid age conceptually.",
        "easy", "understand", "attributes-and-domains",
        "The domain of the Age column, which only permits whole numbers, not words",
        ["The primary key of the Members table", "A foreign key pointing to another table", "Nothing; any text is acceptable in any column by default"],
    ),
    (
        "Kabir prints a note next to \"Age\" on his redrawn form: \"whole number, 10 to 90.\"\n\nIn database terms, what is Kabir defining by writing that note?",
        "A domain is the complete set of values a given attribute is permitted to hold — Kabir's note is an informal, early version of exactly that definition for the Age column.",
        "medium", "apply", "attributes-and-domains",
        "The domain of the Age attribute — the complete set of legal values it may hold",
        ["A primary key for the Members table", "A foreign key referencing another table", "A relational algebra operation"],
    ),
    (
        "Both -5 and 25 are whole numbers, yet only 25 makes sense as a value for a gym member's Age column.\n\nWhat does this show about what a domain actually restricts?",
        "A domain isn't just about the type of value (whole number vs. text) — it's also about which values within that type genuinely make sense. -5 is a valid whole number but not a sensible age.",
        "medium", "analyze", "attributes-and-domains",
        "A domain restricts both the type of value and which values within that type actually make sense",
        ["A domain only restricts the type of value, never which specific values within that type are sensible", "A domain has nothing to do with negative numbers specifically", "Domains apply only to text columns, never to numeric ones"],
    ),
    (
        "If a handful of rows in a million-row Members table have \"Age\" values like \"young,\" \"N/A,\" or \"25 years\" instead of clean whole numbers, what happens when someone tries to calculate the average age or list members between 20 and 30?",
        "Any calculation relying on Age either breaks outright or quietly produces a wrong answer, which is exactly why defining a strict domain before data starts arriving is what keeps a table trustworthy as it grows.",
        "hard", "analyze", "attributes-and-domains",
        "The calculation either breaks or silently produces a wrong result, because it assumes every Age value is a clean whole number",
        ["Nothing changes; databases automatically ignore malformed values in calculations", "The database converts \"young\" and \"N/A\" into valid numbers automatically", "Only the rows with bad values are calculated; the rest of the table is unaffected"],
    ),
    (
        "Kabir's Email column is meant to hold values like \"farah.sheikh@example.com,\" never a bare number or a random sentence.\n\nWhich statement best describes the Email column's domain?",
        "The Email column's domain is text shaped like a valid email address, containing an \"@\" and a domain part — a completely different promise than the Age column makes.",
        "easy", "remember", "attributes-and-domains",
        "Text shaped like a valid email address, containing an \"@\" and a domain part",
        ["Any text of any shape or length", "Whole numbers between 10 and 90", "A value that must match a primary key in another table"],
    ),
]

PRIMARY_KEYS = [
    (
        "Two students named Ravi Kumar live in Tara's hostel, one in Block A and one in Block C. When the college office calls about \"Ravi Kumar,\" Tara cannot tell which student they mean.\n\nWhat does this reveal about using a name as a table's identifying column?",
        "A name is just another attribute, and nothing stops two different people from sharing one. Without a column guaranteed to be unique, a table cannot promise that a question about \"this one row\" has a single, correct answer.",
        "easy", "understand", "primary-keys",
        "A name is not guaranteed to be unique, so it cannot reliably identify one specific row",
        ["Names should never be stored in a database table at all", "This only happens when a table has fewer than three rows", "Tara's register was missing a Block column, which was the real problem"],
    ),
    (
        "A primary key is described as making two firm promises that every other column in a table is free to ignore.\n\nWhat are those two promises?",
        "A primary key must be unique — no two rows ever share the same value — and it must never be left empty, since a row with no identifying value is one nothing else can reliably refer back to.",
        "medium", "remember", "primary-keys",
        "It must be unique across all rows, and it must never be left empty",
        ["It must be a number, and it must never be longer than ten characters", "It must be readable by humans, and it must match a foreign key somewhere", "It must be the first column in the table, and it must never repeat a name"],
    ),
    (
        "Tara considers using a student's email address as the Students table's primary key, since it happens to be unique today. She decides against it and uses Roll Number instead.\n\nWhy is Roll Number the better choice?",
        "A primary key that can change underneath a table is fragile. Students occasionally change their email addresses, but Roll Number is assigned once and never changes for the life of that student's enrolment — stability matters as much as uniqueness.",
        "medium", "apply", "primary-keys",
        "Roll Number is stable and never changes, while an email address can change over time even though it's unique today",
        ["Email addresses are never actually unique among students", "Roll Number is shorter to type than an email address", "Primary keys must always be purely numeric, and email addresses contain letters"],
    ),
    (
        "A quick test is suggested for judging whether a column deserves to be a table's primary key: imagine the table growing to a hundred thousand rows, and ask a specific question.\n\nWhat is that question?",
        "The test asks: could two rows ever, even by rare coincidence, end up with the same value in this column? If the honest answer is yes, the column cannot be trusted alone as the primary key.",
        "hard", "analyze", "primary-keys",
        "Could two rows, even by rare coincidence, ever end up sharing the same value in this column?",
        ["Is this column the first one listed in the table?", "Does this column contain only numbers rather than text?", "Would removing this column make the table simpler to read?"],
    ),
    (
        "Without any column guaranteed to be unique, what is the strongest kind of answer a table can offer to a question like \"give me Ravi Kumar's details\"?",
        "A table with no primary key can only offer probable answers, since more than one row might satisfy the same description — and a database that only deals in probabilities is not one anyone can fully trust.",
        "medium", "understand", "primary-keys",
        "Only a probable answer, since more than one row could match the same description",
        ["A guaranteed, certain answer, since databases always resolve ambiguity automatically", "No answer at all — the query would always fail outright", "The most recently added matching row, chosen automatically"],
    ),
]

FOREIGN_KEYS = [
    (
        "An order sheet reaches Ravi with the note \"Deliver to Customer, urgent\" and nothing else identifying who placed it.\n\nWhat problem does adding a Customer ID column to the Orders table, referencing the Customers table, solve?",
        "The Customer ID column lets every order be traced back to the exact customer who placed it — this is exactly what a foreign key does: a column in one table pointing to the primary key of another, preventing orders that point at nobody.",
        "easy", "understand", "foreign-keys",
        "It lets every order be traced back with certainty to the exact customer who placed it, instead of pointing at nobody",
        ["It removes the need for the Orders table to have its own primary key", "It automatically renames every customer to match their most recent order", "It merges the Customers and Orders tables into a single table"],
    ),
    (
        "What is a foreign key, precisely?",
        "A foreign key is a column, or set of columns, in one table whose values are meant to match the primary key values of another (referenced, or \"parent\") table.",
        "easy", "remember", "foreign-keys",
        "A column in one table whose values are meant to match the primary key values of another table",
        ["A column that is never allowed to repeat a value across rows", "A column whose values must always be text rather than numbers", "The very first column listed in any table"],
    ),
    (
        "Orders 5001 and 5003 both carry Customer ID 1042 in Ravi's Orders table.\n\nWhat does this tell us?",
        "Both orders belong to the same customer, Meera Pillai, even though they are two separate rows in a completely separate table — the foreign key connects each order back to exactly one customer.",
        "medium", "apply", "foreign-keys",
        "Both orders belong to the same customer, even though they are separate rows in a separate table",
        ["Order 5001 and Order 5003 are actually the same order duplicated by mistake", "Customer ID 1042 must be the primary key of the Orders table itself", "The two orders were placed on exactly the same date"],
    ),
    (
        "Suppose someone tries to insert an order with Customer ID 9999, but no customer with that ID exists anywhere in the Customers table.\n\nWhat promise would this violate, and what does a foreign key exist to prevent?",
        "A foreign key carries the promise that every value appearing in the child table corresponds to a value that genuinely exists in the parent table. An order for Customer ID 9999 would be a dangling, meaningless reference — exactly what a foreign key is built to stop.",
        "medium", "analyze", "foreign-keys",
        "It would violate the promise that every foreign key value matches a genuinely existing value in the parent table, creating a dangling reference",
        ["It would violate the rule that every table must have exactly one foreign key", "It would violate the Orders table's own primary key, since 9999 is too large a number", "Nothing would be violated; foreign keys only check that a value is a number"],
    ),
    (
        "The word \"relational,\" as in \"relational database,\" is explained to refer to something more specific than tables simply being related the way relatives are related in a family.\n\nWhat does \"relational\" actually refer to?",
        "It refers to how each table represents a mathematical relation, and foreign keys are the threads that stitch those separate relations, those separate tables, into one coherent, connected system.",
        "hard", "analyze", "foreign-keys",
        "Each table represents a mathematical relation, and foreign keys stitch those separate relations into one connected system",
        ["It refers to tables being physically stored next to each other on disk", "It refers to every table needing at least one relative table with an identical structure", "It refers to the relationship between a database and its DBMS software"],
    ),
]

CANDIDATE_COMPOSITE_SURROGATE = [
    (
        "In Aisha's Books table, both ISBN and Accession No are unique for every single book, and neither is ever blank. She chooses ISBN as the primary key.\n\nWhat does Accession No become, in relational terms?",
        "Any column, or minimal combination of columns, that satisfies every requirement a primary key demands is a candidate key — a genuine candidate for the job whether or not it's chosen. Once ISBN is picked, Accession No remains a candidate key (specifically, an alternate key).",
        "medium", "understand", "candidate-composite-surrogate-keys",
        "A candidate key — it met every requirement to be the primary key but wasn't the one chosen",
        ["A foreign key pointing back to the Books table", "A surrogate key invented purely for convenience", "A constraint restricting which values Title may hold"],
    ),
    (
        "In Aisha's Book Loans table, neither Roll No alone nor ISBN alone is unique, and even the pair (Roll No, ISBN) isn't quite safe. Adding Loan Date to the combination finally makes it unique.\n\nWhat kind of key is (Roll No, ISBN, Loan Date) together?",
        "A primary key formed by combining two or more columns, where the full combination is unique even though no individual column or smaller subset is, is called a composite key.",
        "medium", "apply", "candidate-composite-surrogate-keys",
        "A composite key — unique only when all three columns are considered together",
        ["A candidate key, since each column individually could serve as the primary key", "A surrogate key, since it was invented rather than found naturally in the data", "A foreign key, since it references another table's primary key"],
    ),
    (
        "In Aisha's anonymous Feedback Forms table, nothing about a submitted form is naturally unique, not the comments, not the date. The table invents a Feedback ID, a plain ever-increasing number, purely to give each row a reliable identity.\n\nWhat is Feedback ID an example of?",
        "An artificial identifier created solely to serve as a primary key, when nothing genuinely unique exists in the real-world data, is called a surrogate key.",
        "easy", "remember", "candidate-composite-surrogate-keys",
        "A surrogate key",
        ["A candidate key", "A composite key", "A foreign key"],
    ),
    (
        "Why isn't the pair (Roll No, ISBN) alone, without Loan Date, safe as a key for the Book Loans table?",
        "Nothing stops the same student from borrowing the exact same book again on a later date, once it has been returned, which would repeat that same (Roll No, ISBN) pair. Adding Loan Date makes the combination genuinely unique, since a student isn't expected to borrow the same book twice on the same day.",
        "hard", "analyze", "candidate-composite-surrogate-keys",
        "A student could borrow the same book again on a later date, repeating the same (Roll No, ISBN) pair",
        ["Roll No and ISBN are stored as different data types, so they cannot be combined at all", "Composite keys are never allowed to include exactly two columns", "The Book Loans table does not have a Loan Date column at all"],
    ),
    (
        "Aisha develops a practical habit for choosing a key for any new table: first ask if a single column is naturally unique; if several are, they're all candidate keys and one becomes primary; if none alone but some combination is, that combination becomes what; and if nothing in the real-world data is reliably unique at all, what should be done?",
        "If no single column is unique but some combination is, that combination becomes a composite key. If truly nothing in the real-world data can be trusted to stay unique, inventing a surrogate key is often the simplest, safest way forward.",
        "medium", "understand", "candidate-composite-surrogate-keys",
        "The combination becomes a composite key; if nothing is naturally unique at all, a surrogate key should be invented",
        ["The combination becomes a foreign key; if nothing is unique, the table should be deleted", "The combination becomes a candidate key; if nothing is unique, the table needs no primary key", "The combination becomes a domain; if nothing is unique, use a composite key instead"],
    ),
]

DATABASE_CONSTRAINTS = [
    (
        "At Kiran's clinic, a receptionist once left the phone number field empty for a day's worth of patients, another patient got registered twice under slightly different spellings, and a third patient's age was entered as -3.\n\nWhat do all three incidents reveal about the old spreadsheet system?",
        "None of these were failures of the receptionists' intelligence — they were failures of the spreadsheet, which never enforced a single rule about what counted as an acceptable entry. It simply accepted whatever was typed and moved on.",
        "easy", "understand", "database-constraints",
        "The spreadsheet never enforced any rules about acceptable entries, so it accepted whatever was typed without question",
        ["The receptionists were simply careless and needed better training", "Spreadsheets are incapable of storing patient information reliably at all", "The clinic had too few staff members to catch every mistake"],
    ),
    (
        "What is a constraint, in database terms?",
        "A constraint is a rule attached to a column, or sometimes a whole table, that every row must satisfy before the database will accept it — enforced automatically by the database software itself, regardless of who is entering the data.",
        "easy", "remember", "database-constraints",
        "A rule attached to a column or table that every row must satisfy, enforced automatically by the database itself",
        ["A suggestion written in a manual that staff are expected to remember", "A backup copy of a table kept in case data is lost", "A password required to log into the database software"],
    ),
    (
        "\"A membership status might only ever be 'Active,' 'Inactive,' or 'Suspended,' nothing else.\"\n\nWhich kind of constraint rule does this describe?",
        "This restricts a value to a fixed, allowed set — exactly like requiring a patient's blood group to be a genuine blood group rather than a typo or invented label.",
        "medium", "apply", "database-constraints",
        "Must come from a fixed, allowed set",
        ["Must never be missing", "Must be unique", "Must always point at something real"],
    ),
    (
        "Larger systems often have several doors into a database: a website, a mobile app, a batch import script, and a direct connection used by another internal system.\n\nWhy does it matter that constraints are enforced by the database itself rather than only by one application's form?",
        "If a rule like \"phone number cannot be missing\" is only checked by the website's form, a batch import script that never passes through that form can quietly slip bad data straight past it. A constraint enforced by the database guards every entry route at once, since no data can reach the table without passing the database's own checks first.",
        "hard", "analyze", "database-constraints",
        "A database-level constraint guards every entry route at once, while an application-only check only protects the one door it's built into",
        ["It doesn't matter; every application always checks data the same way", "Database-level constraints are slower, so application-only checks are always preferred", "Batch import scripts are not capable of writing data to a database at all"],
    ),
    (
        "How does a constraint relate to the earlier idea of a domain?",
        "A domain describes, in the abstract, what values belong in a column. A constraint is the database actually standing guard at that boundary and turning away anything that doesn't belong — the domain is the definition, the constraint is the enforcement.",
        "medium", "understand", "database-constraints",
        "A domain defines what values belong in a column in the abstract; a constraint is the database actively enforcing that boundary",
        ["A domain and a constraint are two unrelated ideas with nothing in common", "A constraint defines the domain, and the domain enforces the constraint", "A domain only applies to numeric columns, while constraints only apply to text columns"],
    ),
]

ON_DELETE_ON_UPDATE = [
    (
        "Naina Kapoor asks to have her account permanently deleted. She has eleven past orders in the Orders table, each pointing back at her Customer ID through a foreign key.\n\nWhat is the core dilemma Sanjay faces?",
        "Deciding what should happen to those eleven dependent order rows once the customer row they depend on disappears — should they vanish too, stay behind pointing at a customer who no longer exists, or should the deletion simply be blocked until someone deals with them?",
        "easy", "understand", "on-delete-and-on-update",
        "Deciding what should happen to the eleven dependent orders once the customer row they point to is deleted",
        ["Deciding which employee is allowed to process the deletion request", "Deciding whether Naina's request is legally valid", "Deciding how to encrypt Naina's remaining personal data"],
    ),
    (
        "A relational database lets a designer configure, in advance, what happens to dependent rows when a referenced parent row is deleted or its identifying value changes.\n\nWhat are the three broad choices available?",
        "The three choices are: block the change entirely, cascade the change so dependent rows are automatically deleted or updated too, or set the link empty so dependent rows survive but lose their reference to the parent.",
        "medium", "remember", "on-delete-and-on-update",
        "Block the change, cascade the change, or set the link empty",
        ["Delete the change, ignore the change, or duplicate the change", "Archive the change, encrypt the change, or export the change", "Approve the change, reject the change, or postpone the change"],
    ),
    (
        "A blog post is deleted, and its own comments should disappear along with it, since a comment has no meaning once its post is gone.\n\nWhich on-delete choice fits this relationship best?",
        "Cascade suits relationships where the child row's entire reason for existing is tied to the parent — comments belonging to a post are a textbook case, since a comment truly has no life of its own once the post is gone.",
        "medium", "apply", "on-delete-and-on-update",
        "Cascade — deleting the post automatically deletes its comments too",
        ["Block — the post should never be allowed to be deleted", "Set the link empty — comments should be kept but detached from any post", "None of these; comments and posts should never be linked by a foreign key"],
    ),
    (
        "A bookstore wants to keep a customer's order history intact for sales figures and inventory records, even after the customer's account is closed.\n\nWhich on-delete choice fits this situation best, and why?",
        "Blocking, or setting the link empty, suits relationships where the dependent rows represent something valuable in their own right — an order history the business genuinely wants to keep, rather than lose the moment an account closes.",
        "medium", "apply", "on-delete-and-on-update",
        "Block, or set the link empty — the order history is valuable and shouldn't vanish silently",
        ["Cascade — deleting the customer should also delete every one of their orders", "None of these; customer deletion should never be allowed under any circumstances", "Set the link empty on the Orders table's primary key rather than the foreign key"],
    ),
    (
        "The lesson insists that none of the three choices, block, cascade, or set the link empty, is \"universally correct.\"\n\nWhat actually determines which choice is right for a given foreign key relationship?",
        "The right choice depends entirely on what the relationship between the two tables actually means in the real world — whether the child row's purpose is entirely tied to the parent, or whether it represents something worth preserving on its own.",
        "hard", "analyze", "on-delete-and-on-update",
        "What the relationship between the two tables actually means in the real world",
        ["Whichever choice is fastest for the database to execute", "Whichever choice was used the last time a similar table was designed", "The alphabetical order of the two table names"],
    ),
]

SYNTHESIS = [
    (
        "Match each term to its role in Ravi's stationery shop: Customer ID is chosen to uniquely identify each customer; Accession No in a library system could have been chosen instead of ISBN but wasn't; and Customer ID reappears inside the Orders table pointing back at Customers.\n\nWhich matching is correct?",
        "Customer ID in Customers is the primary key (the one chosen to identify rows). Accession No, unchosen but equally capable, is a candidate key. Customer ID inside Orders, pointing back at Customers, is a foreign key.",
        "medium", "analyze", "foreign-keys",
        "Customer ID in Customers = primary key; Accession No = candidate key; Customer ID in Orders = foreign key",
        ["Customer ID in Customers = foreign key; Accession No = primary key; Customer ID in Orders = candidate key", "Customer ID in Customers = candidate key; Accession No = foreign key; Customer ID in Orders = primary key", "All three examples describe the exact same kind of key"],
    ),
    (
        "A patient's Age column receives the value -3, and the value is saved without any error.\n\nWhich two ideas from this chapter, working together, should have caught this before it was ever saved?",
        "The domain of Age (whole, non-negative numbers in a sensible range) defines what's legal, and a constraint is the database mechanism that actually enforces that boundary and rejects an out-of-range value like -3.",
        "medium", "analyze", "database-constraints",
        "The domain of the Age column, enforced by a range constraint that rejects values outside it",
        ["The primary key of the Patients table, since primary keys reject negative numbers", "A foreign key pointing from Age to another table", "The system catalog, which only concerns itself with table names"],
    ),
    (
        "Aisha's anonymous Feedback Forms table needed an invented Feedback ID because nothing in the real data was unique, while her Book Loans table needed Roll No plus ISBN plus Loan Date combined because no single column was unique alone.\n\nWhich pairing of table to key type is correct?",
        "Feedback Forms needed a surrogate key (invented from nothing) because no real attribute was unique at all. Book Loans needed a composite key because uniqueness only emerged once several real columns were combined.",
        "medium", "apply", "candidate-composite-surrogate-keys",
        "Feedback Forms → surrogate key; Book Loans → composite key",
        ["Feedback Forms → composite key; Book Loans → surrogate key", "Feedback Forms → candidate key; Book Loans → primary key", "Both tables need exactly the same kind of key"],
    ),
    (
        "A college wants a rule enforced: if a department still has employees belonging to it, deleting that department should fail outright until the employees are reassigned.\n\nWhich foreign-key mechanism enforces this?",
        "This is a foreign key from Employees to Departments, configured with an on-delete policy of \"block,\" which stops the department deletion while dependent employee rows still exist.",
        "hard", "apply", "on-delete-and-on-update",
        "A foreign key from Employees to Departments with an on-delete policy set to block",
        ["A domain restricting the Department column to a fixed list of names", "A primary key on the Departments table alone, with no foreign key involved", "A surrogate key added to the Employees table"],
    ),
    (
        "Consider five ideas from this chapter: tables/columns, primary keys, foreign keys, constraints, and on-delete/on-update policies.\n\nIn what order would a database designer typically settle these while building a brand-new schema?",
        "Tables and their columns come first, since nothing can be identified before it exists. A primary key is chosen next to identify rows, followed by foreign keys linking tables together. Constraints then refine which values are allowed, and on-delete/on-update policies decide what happens to dependent rows through those foreign keys.",
        "hard", "analyze", "tables-rows-and-columns",
        "Tables and columns, then primary keys, then foreign keys, then constraints, then on-delete/on-update policies",
        ["On-delete/on-update policies first, then constraints, then foreign keys, then primary keys, then tables", "Constraints first, then tables, then primary keys, then on-delete policies, then foreign keys", "The order never matters; all five are always defined simultaneously"],
    ),
]

SET1_SOURCES = [
    (TABLES_ROWS_COLUMNS, 0),
    (ATTRIBUTES_AND_DOMAINS, 0),
    (PRIMARY_KEYS, 0),
    (FOREIGN_KEYS, 0),
    (CANDIDATE_COMPOSITE_SURROGATE, 0),
    (DATABASE_CONSTRAINTS, 0),
    (ON_DELETE_ON_UPDATE, 0),
]

SET1 = [src[idx] for src, idx in SET1_SOURCES]
SET1.extend(SYNTHESIS[:3])

SET2 = (
    TABLES_ROWS_COLUMNS[1:]
    + ATTRIBUTES_AND_DOMAINS[1:]
    + PRIMARY_KEYS[1:]
    + FOREIGN_KEYS[1:]
    + CANDIDATE_COMPOSITE_SURROGATE[1:]
    + DATABASE_CONSTRAINTS[1:]
    + ON_DELETE_ON_UPDATE[1:]
    + SYNTHESIS[3:]
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
            "topics": "database-foundations",
            "subTopics": subtopic,
            "companies": None,
            "option1": options[0],
            "option2": options[1],
            "option3": options[2],
            "option4": options[3],
            "answer": pos,
        })
    return rows


rows1 = build_rows(SET1, "Set 1", "DBMS - MCQ - 1.2.1")
rows2 = build_rows(SET2, "Set 2", "DBMS - MCQ - 1.2.2")
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
ws.title = "DBMS - MCQ - Unit 1.2"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/DBMS/Unit 1 - Database Foundations/1.2 - The Relational Model - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
