# Database Management Systems - Curriculum Table of Contents

**Draft for finalization.** Mirrors the Python Fundamentals structure: clean Unit -> Topic layout (no chapters), in teaching order, over a 15-week term. Each unit has a one-line goal, followed by its topics in the exact order they should be taught. Reading materials will follow the same house style as the Python course: professional, beginner-friendly, no emojis, no em dashes, standardized Introduction heading, narrative flow.

The arc matches the Python course philosophy: think in data before writing SQL (Units 1-2), learn the language hands-on (Units 3-9), then design and operate real databases (Units 10-13).

---

## Unit 1: Introduction to Databases

Think in data before writing SQL: why organized, shared, reliable data storage matters.

1. What is Data? Data vs. Information
2. The Problem with Files: Redundancy, Inconsistency, and Lost Updates
3. What is a Database? What is a DBMS?
4. Where Databases Live: Real Apps You Already Use (Banking, Food Delivery, College Portals)
5. Types of Databases: Relational, Key-Value, Document, and When Each Fits
6. How a DBMS is Organized: Storage, Query Processor, and the Catalog
7. Who Uses a Database: End Users, Developers, and Administrators
8. Why Relational Databases First: Tables, SQL, and the Industry Standard

## Unit 2: The Relational Model

See all data as tables, and learn the rules that keep those tables trustworthy.

1. Tables, Rows, and Columns: The Shape of Relational Data
2. Domains and Data Types: What a Column is Allowed to Hold
3. Keys: Candidate, Primary, and Composite
4. Foreign Keys: How Tables Point to Each Other
5. Relationships: One-to-One, One-to-Many, Many-to-Many
6. Integrity Rules: Entity Integrity and Referential Integrity
7. Constraints: NOT NULL, UNIQUE, DEFAULT, CHECK
8. Reading a Schema: From a Diagram to Real Tables

## Unit 3: SQL Setup and First Queries

Set up a working database and run your first real SQL, hands-on from day one.

1. What is SQL? Declarative Thinking: Say What, Not How
2. Setting Up Your Environment (MySQL/SQLite and a Client)
3. Creating a Database and Your First Table (CREATE TABLE)
4. SQL Data Types in Practice: Numbers, Text, Dates, Booleans
5. Inserting Your First Rows (INSERT INTO)
6. Your First SELECT: Reading Data Back
7. Changing a Table's Structure (ALTER TABLE, DROP TABLE)
8. SQL Habits: Statements, Semicolons, Comments, and Readable Formatting

## Unit 4: Retrieving Data with SELECT

Ask precise questions of a table and get exactly the rows you want.

1. SELECT and FROM: Choosing Columns
2. Filtering Rows with WHERE
3. Comparison and Logical Operators in Conditions (AND, OR, NOT)
4. Pattern Matching with LIKE and Wildcards
5. Ranges and Lists: BETWEEN and IN
6. Working with Missing Data: NULL, IS NULL, and Three-Valued Logic
7. Removing Duplicates with DISTINCT
8. Sorting Results with ORDER BY
9. Limiting Results: LIMIT and OFFSET
10. Column Aliases and Computed Columns

## Unit 5: Built-in Functions and Conditional Logic

Transform values inside a query using SQL's built-in toolkit.

1. String Functions: CONCAT, UPPER, LOWER, LENGTH, TRIM, SUBSTRING
2. Numeric Functions: ROUND, CEIL, FLOOR, ABS, MOD
3. Date and Time Functions: NOW, DATE Arithmetic, Extracting Parts
4. Type Conversion in SQL: CAST and Implicit Conversion
5. Conditional Logic with CASE
6. Handling NULLs Gracefully: COALESCE and NULLIF
7. Combining Functions: Cleaning Messy Real-World Data in One Query

## Unit 6: Aggregation and Grouping

Turn thousands of rows into totals, averages, and summaries.

1. Why Aggregate: From Rows to Answers
2. COUNT, SUM, AVG, MIN, MAX
3. Grouping Rows with GROUP BY
4. Filtering Groups with HAVING (and How It Differs from WHERE)
5. Grouping by Multiple Columns
6. Aggregates and NULLs: What Gets Counted
7. Logical Order of a Query: FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY
8. Common Reporting Patterns: Top-N, Per-Category Totals, Daily Summaries

## Unit 7: Joins: Combining Tables

Answer questions that span multiple tables, the heart of relational SQL.

1. Why Joins: Data Lives in Many Tables
2. INNER JOIN: Matching Rows Across Tables
3. Join Conditions and Table Aliases
4. LEFT and RIGHT Outer Joins: Keeping the Unmatched
5. FULL Outer Join and Emulating It
6. Self Joins: A Table Meets Itself
7. CROSS JOIN and When It Is Actually Useful
8. Joining Three or More Tables
9. Choosing the Right Join: Common Mistakes and How to Spot Them

## Unit 8: Subqueries, Set Operations, and CTEs

Build bigger questions out of smaller queries.

1. Subqueries in WHERE: Scalar and List Results
2. IN, ANY, ALL with Subqueries
3. EXISTS and NOT EXISTS
4. Correlated Subqueries: The Inner Query That Looks Outside
5. Subqueries in FROM: Derived Tables
6. Set Operations: UNION, UNION ALL, INTERSECT, EXCEPT
7. Common Table Expressions: WITH for Readable Queries
8. Rewriting a Messy Query: Subquery vs. Join vs. CTE

## Unit 9: Modifying Data Safely

Change data with confidence, and never lose rows you meant to keep.

1. INSERT Revisited: Multiple Rows, Column Lists, and Defaults
2. Inserting from a Query: INSERT ... SELECT
3. UPDATE: Changing Existing Rows
4. The WHERE Clause is Not Optional: Avoiding Accidental Mass Updates
5. DELETE vs. TRUNCATE: Removing Rows the Right Way
6. Upserts: Handling "Insert or Update" Situations
7. Constraint Violations: Reading and Fixing the Errors
8. A Safe-Change Routine: SELECT First, Then Modify

## Unit 10: Database Design and ER Modeling

Turn a real-world requirement into a clean, correct database design.

1. From Requirements to Data: What to Store and Why
2. Entities and Attributes: Finding the Nouns
3. Relationships and Cardinality: Finding the Verbs
4. Drawing ER Diagrams
5. Strong and Weak Entities, Composite and Derived Attributes
6. Resolving Many-to-Many: Junction Tables
7. From ER Diagram to Tables: The Mapping Rules
8. Design Walkthrough: Modeling a College Course-Registration System

## Unit 11: Normalization

Remove redundancy and anomalies so data stays consistent as it grows.

1. Why Normalize: Update, Insert, and Delete Anomalies
2. Functional Dependencies: What Determines What
3. First Normal Form: Atomic Values, No Repeating Groups
4. Second Normal Form: Removing Partial Dependencies
5. Third Normal Form: Removing Transitive Dependencies
6. BCNF: A Stricter Third Normal Form (introduction)
7. Normalizing a Real Table: A Step-by-Step Worked Example
8. When to Stop: Practical Denormalization and Its Trade-offs

## Unit 12: Transactions and Concurrency

Keep data correct when many things happen at once, or when things go wrong.

1. What is a Transaction: All or Nothing
2. ACID Properties, Explained with a Bank Transfer
3. COMMIT and ROLLBACK in Practice
4. Auto-commit and Explicit Transactions
5. Concurrency Problems: Dirty Reads, Non-Repeatable Reads, Phantoms
6. Isolation Levels (introduction)
7. Locks and Deadlocks: What They Are and How Databases Cope
8. Designing for Safety: Transactions in Everyday Application Code

## Unit 13: Indexes, Views, and Query Performance

Make queries fast, find out why they are slow, and package them for reuse - the most practical real-world skill.

1. Why Some Queries are Slow: Full Table Scans
2. What is an Index: The Phone-Book Analogy
3. Creating and Dropping Indexes; What Gets Indexed Automatically
4. When Indexes Help and When They Hurt
5. Reading a Query Plan with EXPLAIN (introduction)
6. Views: Saved Queries as Virtual Tables
7. Users, Privileges, and GRANT/REVOKE Basics
8. A Performance-Debugging Routine: Measure, Explain, Index, Re-measure
9. Course Capstone: Design, Build, Load, and Query a Complete Database

---

## Summary

| # | Unit | Topics |
|---|------|--------|
| 1 | Introduction to Databases | 8 |
| 2 | The Relational Model | 8 |
| 3 | SQL Setup and First Queries | 8 |
| 4 | Retrieving Data with SELECT | 10 |
| 5 | Built-in Functions and Conditional Logic | 7 |
| 6 | Aggregation and Grouping | 8 |
| 7 | Joins: Combining Tables | 9 |
| 8 | Subqueries, Set Operations, and CTEs | 8 |
| 9 | Modifying Data Safely | 8 |
| 10 | Database Design and ER Modeling | 8 |
| 11 | Normalization | 8 |
| 12 | Transactions and Concurrency | 8 |
| 13 | Indexes, Views, and Query Performance | 9 |
| | **Total** | **107** |

**Notes for finalization**

- 13 units matches the Semester 1 Python folder structure; topic count (107) is in the same band as Python Semester 1 (99).
- SQL flavour is written to be MySQL-first with SQLite acceptable for local practice; wording stays engine-neutral wherever possible.
- Design theory (ER modeling, normalization) is placed after hands-on SQL, mirroring how the Python course teaches syntax before architecture, so students design tables only after they have queried them for weeks.
- Python-DBMS integration (connecting from `sqlite3`/drivers) is intentionally excluded here because Python Semester 2, Unit 13 (Database Interaction) already covers it.
- Once this TOC is approved, unit folders and READMEs can be scaffolded the same way as the Python course, and reading materials authored unit by unit in the existing house style.
