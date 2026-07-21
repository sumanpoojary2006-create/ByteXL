## Background

College libraries track thousands of books, hundreds of members, and constant borrowing activity. Before a single query gets written, someone has to decide what tables exist, what belongs in each one, and how they connect. Get this wrong and every query downstream becomes an awkward workaround. This project walks the full design path: model the real world as an ER diagram, catch the anomalies hiding in a badly flattened spreadsheet, normalize it properly, then translate the result into a real schema.

## What You Will Build

An ER diagram and a normalized PostgreSQL schema for a college library system tracking books, authors, members, and loans, plus the `CREATE TABLE` statements that bring it to life.

## Project Workspace

Use two files when you move from the design work to your SQL environment. Keep the completed schema in `init.sql`, including every `CREATE TABLE` statement and constraint. Use a separate SQL file for one verification query at a time, such as checking the tables in `information_schema` or inserting a sample author, book, member, and loan. This separation lets you rebuild the schema from a clean state without mixing setup statements into every test.

The spreadsheet in Task 2 is the source data to inspect before writing any schema. The SQL shown in Task 3 is only a starting example; extend it with `members` and `loans`, then run your verification queries against the completed `init.sql` file.

## Tasks

### Task 1: Model the Entities

1. Identify the core entities: Author, Book, Member, Loan.
2. For each entity, list its attributes and mark the primary key.
3. Work out the relationships and their cardinality:
   - One author can write many books; a book has exactly one primary author for this project.
   - One member can borrow many books over time; one loan record belongs to exactly one member and one book.
4. Draw the ER diagram (on paper or any tool) showing entities, attributes, primary keys, and relationship cardinalities (1:1, 1:N, or M:N) with the correct notation.

### Task 2: Normalize a Broken Spreadsheet

You are handed this flat spreadsheet the librarian has been maintaining manually:

| loan_id | member_name | member_phone | book_title | book_author | author_country | borrow_date | due_date |
|---|---|---|---|---|---|---|---|
| 1 | Ananya Rao | 98765xxxxx | Clean Code | Robert Martin | USA | 2026-01-05 | 2026-01-19 |
| 2 | Ananya Rao | 98765xxxxx | The Pragmatic Programmer | Andrew Hunt | USA | 2026-01-10 | 2026-01-24 |
| 3 | Rahul Nair | 91234xxxxx | Clean Code | Robert Martin | USA | 2026-01-12 | 2026-01-26 |

1. Identify at least three update, insert, or delete anomalies in this table. For example: what happens if Ananya's phone number changes but only one of her two rows gets updated?
2. Identify the functional dependencies at work here (for example, `book_title → book_author`, `book_author → author_country`, `member_name → member_phone`).
3. Normalize step by step: take the table to 1NF, then 2NF, then 3NF, showing the resulting tables at each step and stating which anomaly each split removes.

### Task 3: Build the Real Schema

1. Translate your normalized design into `CREATE TABLE` statements for `authors`, `books`, `members`, and `loans`.
2. Use appropriate data types for each column (`TEXT`, `NUMERIC`, `DATE`, `BOOLEAN`), a surrogate integer primary key (`GENERATED ALWAYS AS IDENTITY`) for each table, and foreign keys with an explicit `ON DELETE` behaviour. Decide whether deleting an author should delete their books, and justify your choice in a comment.
3. Add audit columns (`created_at`, `updated_at`) to every table, and a `returned_at` column on `loans` that stays `NULL` until the book comes back.
4. Follow consistent naming conventions throughout: `snake_case`, one decision on singular vs. plural table names applied everywhere, and foreign key columns named `<entity>_id`.

   ```text
   CREATE TABLE authors (
       author_id   INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
       full_name   TEXT NOT NULL,
       country     TEXT,
       created_at  TIMESTAMP NOT NULL DEFAULT now(),
       updated_at  TIMESTAMP NOT NULL DEFAULT now()
   );

   CREATE TABLE books (
       book_id     INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
       title       TEXT NOT NULL,
       author_id   INTEGER NOT NULL REFERENCES authors(author_id) ON DELETE CASCADE,
       created_at  TIMESTAMP NOT NULL DEFAULT now(),
       updated_at  TIMESTAMP NOT NULL DEFAULT now()
   );
   ```

**Answer these questions after completing all tasks:**
- Your `loans` table has a `returned_at` column that is `NULL` for books still checked out. What is the difference between `NULL` and an empty string here, and why would using an empty string instead have been the wrong choice?
- The flat spreadsheet repeated `author_country` on every row for the same author. After normalization, where does `author_country` live, and how many times does "USA" now physically appear in your database for Robert Martin's two books?
- Suppose two members share the exact same name. Does your schema still tell them apart correctly? Which column makes this possible, and what would have gone wrong if you had used `member_name` as a key instead?

## Where to Build This Project

1. Go to [bytexl.app/nimbus](https://bytexl.app/nimbus).
2. Click **Create new workspace**.

![The Nimbus dashboard with the Create new workspace button highlighted](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_create_new_workspace.png)

3. Select the **PostgreSQL** template, then click **Next**.

![Select the PostgreSQL template and click Next](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_select_postgresql_template.png)

4. Enter a workspace name and click **Launch Workspace**.

![Enter a workspace name and launch the PostgreSQL workspace](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_name_and_launch_workspace.png)
