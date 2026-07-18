# Mini Project 2: Student Club Database CRUD

## Background

Every college club, whether it is a coding club, a robotics team, or a dance crew, ends up needing the same thing: a members list that people can search, filter, and safely update without one person's typo wiping out someone else's row. This project uses raw SQL statements against a single table to build every fundamental operation this unit covers: reading, filtering, sorting, and safely modifying data.

## What You Will Build

A PostgreSQL `club_members` table for a college coding club, queried and modified purely through SQL statements you run yourself, in `psql`, pgAdmin, or any SQL client.

## Dataset

Create the table and load it with this data:

Before writing project queries, inspect the starting data so every task has a visible source to reason from.

### Starting `club_members` rows

| full_name | branch | year_of_study | email | membership_status | joined_on |
| --- | --- | --- | --- | --- | --- |
| Ananya Rao | CSE | 2 | ananya.rao@college.edu | active | 2025-08-14 |
| Rahul Nair | ECE | 3 | rahul.nair@college.edu | active | 2025-08-15 |
| Priya Menon | CSE | 1 | NULL | active | 2026-01-10 |
| Karan Shah | MECH | 4 | karan.shah@college.edu | inactive | 2024-08-20 |
| Divya Iyer | IT | 2 | divya.iyer@college.edu | active | 2025-08-14 |
| Arjun Verma | CSE | 3 | arjun.verma@college.edu | active | 2025-08-18 |
Use two files in OneCompiler. Keep all `CREATE TABLE` and `INSERT` statements in `init.sql`; keep only the current task query in the active SQL file. The `with=init.sql` attribute connects the two files.

```postgresql file=init.sql
CREATE TABLE club_members (
    member_id         INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name         TEXT NOT NULL,
    branch            TEXT NOT NULL,
    year_of_study     INTEGER NOT NULL,
    email             TEXT UNIQUE,
    membership_status TEXT NOT NULL DEFAULT 'active',
    joined_on         DATE NOT NULL DEFAULT CURRENT_DATE
);

INSERT INTO club_members (full_name, branch, year_of_study, email, membership_status, joined_on) VALUES
('Ananya Rao', 'CSE', 2, 'ananya.rao@college.edu', 'active', '2025-08-14'),
('Rahul Nair', 'ECE', 3, 'rahul.nair@college.edu', 'active', '2025-08-15'),
('Priya Menon', 'CSE', 1, NULL, 'active', '2026-01-10'),
('Karan Shah', 'MECH', 4, 'karan.shah@college.edu', 'inactive', '2024-08-20'),
('Divya Iyer', 'IT', 2, 'divya.iyer@college.edu', 'active', '2025-08-14'),
('Arjun Verma', 'CSE', 3, 'arjun.verma@college.edu', 'active', '2025-08-18');
```

### Confirm the Setup

Run this in the active SQL file before starting the tasks. It confirms that `init.sql` loaded the expected number of rows.

```postgresql with=init.sql
SELECT COUNT(*) AS loaded_rows FROM club_members;
```

Expected output:

| loaded_rows |
| --- |
| 6 |

## Tasks

### Task 1: Reading and Sorting

1. Select every member's name and branch, aliasing the columns as `Name` and `Department`.
2. List every distinct branch present in the club, with no duplicates.
3. List members sorted by `year_of_study` descending, then `full_name` ascending, showing only the first 3 rows.
4. Select every member's name alongside an expression column showing `2027 - year_of_study` as their (rough) graduation year.

### Task 2: Filtering

1. Find every active member in CSE.
2. Find members who either joined in 2025 or are in their final year (`year_of_study = 4`).
3. Find members whose name starts with "A", using pattern matching.
4. Find every member who has not provided an email address.
5. Find every member whose email is not missing, ordered alphabetically by name.

### Task 3: Modifying Data Safely

1. Insert a new member and use `RETURNING` to get back the auto-generated `member_id` in the same statement.
2. Priya Menon has just added her email address. Update her row using her `member_id`, never her name, as the condition, and confirm exactly one row was affected.
3. Karan Shah has left the club. Instead of deleting his row, update his `membership_status` to `'inactive'`. Add a SQL comment explaining why a soft status change is usually safer than a hard `DELETE` for membership data.
4. Use `INSERT ... ON CONFLICT` so that re-inserting a member with an email that already exists updates their `membership_status` to `'active'` instead of failing or creating a duplicate row.

   ```postgresql with=init.sql
   INSERT INTO club_members (full_name, branch, year_of_study, email, membership_status)
   VALUES ('Ananya Rao', 'CSE', 2, 'ananya.rao@college.edu', 'active')
   ON CONFLICT (email)
   DO UPDATE SET membership_status = EXCLUDED.membership_status;
   ```

Expected result: Ananya's existing row remains unique and its `membership_status` is `active`; no duplicate email row is created.

**Answer these questions after completing all tasks:**
- Task 2.5 asked you to filter for emails that are not missing. Did you write `email != NULL` or `email IS NOT NULL`? Try the first version in your SQL client: what actually happens, and why do the usual comparison operators break down around `NULL`?
- Your `UPDATE` in Task 3.2 used `member_id` in the `WHERE` clause instead of `full_name`. What could go wrong if two members happened to share the same name and you had filtered by name instead?
- The `ON CONFLICT` clause in Task 3.4 needs a unique column to detect a conflict. Which column made this possible here, and what happens if you try the same `ON CONFLICT` target on a column that has no uniqueness constraint?
