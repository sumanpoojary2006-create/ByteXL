## Introduction

Devika's college IT office finally sends over a proper diagram of what her library's new database will look like, three boxes connected by lines, with small labels she has never had to read carefully before. Every idea from this unit, tables, keys, foreign keys, relationship shapes, and constraints, is sitting inside that one diagram at once. This lesson is about reading it, calmly and completely, before Unit 3 turns it into a real, running database.

## What a Schema Actually Is

A **schema** is the complete design of a database: every table it contains, every column in each table, every key, and every relationship connecting them, all stated together as one coherent structure. It is the blueprint, not the data itself; two colleges could use the exact same schema for their libraries while holding completely different books and members inside it, the same way two houses can be built from one identical architectural plan.

## The Diagram, Read as Three Boxes

Picture three boxes on Devika's page, one for `books`, one for `members`, one for `loans`. Each box lists its table's columns, with the primary key marked at the top.

```
books                    members                  loans
-----                    -------                  -----
book_id (PK)             member_id (PK)            loan_id (PK)
title                    name                       member_id (FK -> members)
author                   email_address (UNIQUE)     book_id (FK -> books)
shelf_location           phone_number               date_borrowed
is_available (DEFAULT)                              date_returned
```

Nothing here is new information; it is every earlier lesson's vocabulary, arranged in one place. `book_id` and `member_id` are marked PK because they are each table's primary key, from the lesson on keys. `email_address` carries UNIQUE, from the lesson on constraints. `is_available` carries DEFAULT, from the same lesson. And `loans.member_id` and `loans.book_id` are marked FK, foreign keys, each pointing back to the primary key of the table named beside it.

## Reading the Relationships Between the Boxes

A schema diagram usually draws a line between related tables, often with a symbol at each end showing the relationship's shape. A line from `members` to `loans` reads as one-to-many: one member can have many loan rows, but each loan row belongs to exactly one member, exactly the shape named two lessons ago. The same reading applies to the line from `books` to `loans`. Neither line needs a third table in between, because neither relationship is many-to-many; if the diagram later needed to show, say, books belonging to several categories at once, that line would look different, and a third table would appear alongside it, the exact case the relationships lesson set aside for later in the course.

## Tracing One Real Question Through the Diagram

Ask the diagram a genuine question: "which member currently has 'Wings of Fire' on loan, and is it overdue?" Start at `books`, find the row where `title` is "Wings of Fire," and read off its `book_id`. Follow the foreign key line into `loans`, and find the row where `book_id` matches, reading off its `date_borrowed` and its `member_id`. Follow that second foreign key line into `members`, and find the row where `member_id` matches, reading off the member's name and phone number.

Notice that this entire trace was possible without a single stray copy-pasted detail anywhere: no book title stored inside `loans`, no member name stored inside `loans`, only identifiers, connected by foreign keys, exactly as Unit 2 designed them to be.

## Schema Elements at a Glance

| Symbol or Label | What It Means | Where It Appears Above |
|---|---|---|
| PK | This column is the table's primary key | `book_id`, `member_id`, `loan_id` |
| FK -> table | This column is a foreign key referencing that table's primary key | `loans.member_id`, `loans.book_id` |
| UNIQUE | No two rows may repeat this value | `members.email_address` |
| DEFAULT | An automatic value fills in when none is given | `books.is_available` |
| A line between two boxes | A relationship, whose shape is read from both ends | `members` to `loans`, `books` to `loans` |

## From Paper to a Real Database

Everything in this diagram is still just paper, exactly like every lesson in this unit so far. What changes in Unit 3 is not the design; it is the fact that this same schema will finally be typed, in SQL, as a set of real `CREATE TABLE` statements that a running DBMS actually enforces. Reading this diagram correctly now is what makes that next step almost mechanical: every PK becomes a primary key declaration, every FK becomes a foreign key declaration, every UNIQUE and DEFAULT becomes exactly the constraint it already is on paper.

## Conclusion

A schema is a database's complete design, stated as tables, their columns, their keys, and the relationships connecting them, and reading one is simply reading the vocabulary this entire unit built, one lesson at a time, all appearing together in a single diagram. Devika's three boxes, `books`, `members`, and `loans`, hold every idea from tables and domains to keys, foreign keys, relationship shapes, integrity rules, and constraints, and tracing one real question through them shows those ideas working together, not just sitting side by side. With a complete, correctly read schema in hand, the next unit finally sets up a real database environment and turns this exact diagram into working SQL.
