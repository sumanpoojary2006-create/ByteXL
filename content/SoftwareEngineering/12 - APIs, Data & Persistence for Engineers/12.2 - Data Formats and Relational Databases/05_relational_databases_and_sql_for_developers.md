## Introduction

A relational database stores data in tables made of rows and columns, relates tables to each other through shared values, and is queried with a declarative language, SQL. Since Edgar Codd proposed the relational model at IBM in 1970, it has been the most widely used way of storing the structured data of business applications. Its strength is a rigorous model that separates what data means from how it is stored, together with guarantees about correctness, discussed in the next topic.

This topic gives developers the working concepts of relational databases and SQL: how data is organised, how it is queried and changed, why indexes matter, and the habits that keep applications correct and fast. The platform's separate database course treats the subject in depth; here the aim is to understand how it fits into application development.

**Definition:** A relational database is a database that organises data into tables of rows and columns connected by keys, managed by a relational database management system and accessed with the declarative language SQL, which lets programs state what data they want and leaves the system to decide how to retrieve it.

<!--
IMAGE PROMPT  ->  generate as images/05_intro_relational_databases_and_sql_for_developers.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Three linked tables Customers, Orders, Order Lines with key columns highlighted and connecting lines, a query request arrow entering, an optimiser block choosing an access plan, and an index card beside a table.

ON-IMAGE TEXT: show a short bold title "Relational Databases and SQL for Developers" plus only these few labels, large and legible: Tables, Keys, Queries. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Relational Model

- A **table** (relation) holds data about one kind of thing, such as customers or orders.
- A **row** (record, tuple) is one instance, such as one order.
- A **column** (attribute) is one property, with a defined **data type**.
- A **primary key** is a column, or set of columns, whose value uniquely identifies each row.
- A **foreign key** is a column that holds the primary key of a row in another table, creating a relationship, for example each order refers to its customer.
- A **schema** defines the tables, columns, types, and constraints.

This is the implementation of the entity-relationship models of Unit 4. Entities become tables, attributes become columns, relationships become foreign keys, and many-to-many relationships are resolved by a table that sits between the two, such as order lines linking orders and dishes.

## Constraints

The database can enforce rules itself.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Constraint</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Rule enforced</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Primary key</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Each row is uniquely identifiable and has an identifier</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Foreign key (referential integrity)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A reference must point to an existing row; an order cannot refer to a missing customer</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unique</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No two rows may share a value, such as an email address</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not null</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A value must be supplied</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Check</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A value must satisfy a condition, such as a quantity greater than zero</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Default</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A value is supplied automatically if none is given</td>
    </tr>
  </tbody>
</table>

Enforcing rules in the database is a defence in depth: every application and every tool that touches the data is bound by the same rules.

## Normalisation

**Normalisation** is the discipline of organising tables to avoid storing the same fact in more than one place, which causes inconsistency when copies diverge. In brief:

- Each column holds a single, indivisible value (first normal form).
- Every column depends on the whole key and not on part of it (second normal form).
- Columns depend on the key and on nothing else (third normal form).

The guiding rule is that **each fact is stored once.** Deliberate **denormalisation**, copying data to avoid costly joins, is sometimes used for performance, at the price of keeping the copies consistent.

## SQL: A Declarative Language

SQL, developed at IBM in the 1970s and standardised internationally in the 1980s, is **declarative**: the developer states the **result wanted**, and the database engine determines the steps. It has several families of statements.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Family</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Main statements (names only)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data definition (DDL)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Define and change structure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Create, alter, and drop tables, indexes, and views</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data manipulation (DML)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Read and change data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Select, insert, update, delete</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data control (DCL)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Manage permissions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Grant, revoke</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Transaction control</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Group and finish units of work</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Begin, commit, rollback</td>
    </tr>
  </tbody>
</table>

## The Ideas Behind Queries

Rather than syntax, developers should understand the operations a query combines.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Operation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it does</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example idea</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Selection (filtering rows)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keeps only rows meeting a condition</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Orders placed today</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Projection (choosing columns)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keeps only the named columns</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Customer name and order total</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Join</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Combines rows from two tables where they match on keys</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Each order with the name of its customer</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Outer join</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A join that keeps rows with no match on one side</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">All customers, including those with no orders</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Aggregation and grouping</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Summarises many rows into one per group, with counts, sums, averages, minimums, and maximums</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Total sales per dish</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sorting</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Orders the result</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Newest orders first</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Limiting</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Returns only some rows</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The top ten</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Subqueries</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A query inside another</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Customers whose total exceeds the average</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Set operations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Combine results of queries</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Union of two lists</td>
    </tr>
  </tbody>
</table>

A single query may combine several of these. The result is itself a table, which can be used by the next stage.

## Changing Data

- **Insert** adds new rows.
- **Update** changes columns of existing rows that match a condition.
- **Delete** removes rows that match a condition.

A condition is vital: a change with no condition affects **every row**, a classic and costly mistake. Good practice is to test conditions with a read first, to run changes within transactions, and to prefer marking rows as inactive (a "soft delete") when the history matters.

## How the Database Executes a Query

The developer does not say how to get the result. The **query optimiser** examines the possible strategies, using statistics about the data, and chooses an **execution plan**: which indexes to use, in what order to join tables, and which algorithms to apply. Two queries that give the same answer can differ in cost by orders of magnitude. Databases can show the plan they chose, and reading it is the standard way to understand why a query is slow.

## Indexes

An **index** is a separate structure, commonly a balanced tree, that lets the database find rows by the values of certain columns without examining the whole table, like the index of a book.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Detail</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Benefit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reads that filter, join, or sort on the indexed columns become much faster</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every insert, update, and delete must also update the index; indexes use storage</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Primary and unique keys</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Normally indexed automatically</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Foreign keys</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Often worth indexing, since joins and lookups use them</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Composite indexes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cover several columns; the order of columns matters</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Selectivity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Indexes help most when they narrow the rows greatly; an index on a column with few distinct values helps little</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Over-indexing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Too many indexes slow writes and waste space</td>
    </tr>
  </tbody>
</table>

The practice is to **design indexes for the real queries,** verify with execution plans, and remove those that are unused.

## SQL Injection

The most notorious security flaw in database applications arises when a program builds a query by pasting user-supplied text into the text of the query. A malicious user can supply text that changes the meaning of the query, reading or destroying data. The defence is simple and absolute: **never construct queries by joining strings with user input.** Use **parameterised queries** (prepared statements), in which the structure of the query is fixed and the user values are passed separately as data that can never be interpreted as commands. Also apply least privilege to the database account, so that the application can do only what it needs.

## Managing Schema Change

The schema evolves with the application. **Migrations** are versioned, ordered scripts that change the structure, kept in version control and applied automatically through the pipeline, so every environment has the same schema, as Unit 9 described for infrastructure. Changes must be compatible with both the old and new versions of the application during a rollout, following the **expand and contract** pattern: add new structures first, migrate, and remove old ones later.

## Working Habits

- **Let the database enforce integrity** with constraints.
- **Select only the columns and rows needed;** avoid retrieving whole tables.
- **Think in sets,** not in loops that handle one row at a time.
- **Keep transactions short.**
- **Look at execution plans** for slow queries and add indexes thoughtfully.
- **Use parameterised queries** everywhere.
- **Back up and test restores.**
- **Do not put business logic in obscure database code** without good reason, since it is harder to test and version.
- **Treat the database as a shared, long-lived asset,** not as part of one application.

## Popular Systems

Widely used relational systems include PostgreSQL, MySQL and MariaDB, SQLite (an embedded database in a single file), Microsoft SQL Server, and Oracle Database, with cloud-managed versions. They share the core model and SQL but differ in features and dialects.

<!--
IMAGE PROMPT  ->  generate as images/02_tables_keys_joins_and_indexes.png   (16:9 explanatory diagram, place here)

Left: Customers, Orders, and Order Lines tables with primary key and foreign key arrows and a join highlighted. Right: a book-style index structure (tree) pointing to table rows, and a split showing a query with an index (fast, short path) versus without (scans all rows).

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Relational Reasoning

1. How is the relationship between an order and the customer who placed it represented?
2. A query to find orders by customer is slow on a large table. What is the usual remedy, and how do you check it works?
3. Why must user input never be pasted into the text of a query?

For case 1, the order table has a foreign key column holding the customer's primary key. For case 2, add an index on the customer column of the orders table, and confirm with the execution plan that the query now uses it. For case 3, doing so allows an attacker to alter the query; parameterised queries keep user input as data.

## Conclusion

A relational database is a database that organises data into tables of rows and columns connected by keys, managed by a relational database management system and accessed with the declarative language SQL, which lets programs state what data they want and leaves the system to decide how to retrieve it. Constraints, normalisation, sensible indexes, parameterised queries, and managed schema changes are the habits that make it reliable.

Rows are rarely changed in isolation. The next topic describes how the database keeps data correct when many changes happen together: transactions and data integrity.
