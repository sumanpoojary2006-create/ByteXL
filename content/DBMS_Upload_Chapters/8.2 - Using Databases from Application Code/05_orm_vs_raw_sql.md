## Introduction

Every query in this course has been written as raw SQL, typed directly. Much real application code, especially in frameworks built around languages like Python, Java, or Ruby, instead uses an **object-relational mapper**, or ORM, a library that lets a developer work with database rows as ordinary objects in their programming language, generating the actual SQL behind the scenes.

Neither approach is universally correct; each trades away something the other offers, and knowing what that trade-off actually is matters more than picking a side.

**Definition:** An ORM speeds up routine, everyday database operations by letting a developer work in objects rather than SQL text, at the cost of sometimes hiding real query costs, most notoriously the N+1 pattern, while raw SQL offers full visibility and control at the cost of more code to write directly, and most real applications end up using both, an ORM for the routine cases and raw SQL for anything complex or performance-critical enough to need precise control.

![Intro visual for orm vs raw sql](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_intro_orm_vs_raw_sql_matched_0b83a42b.png)

## What an ORM Actually Generates

An ORM's core promise is translating object-oriented code into SQL automatically, without the developer writing SQL text directly.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the starting data. The tables below show the rows loaded by the setup file.

### `shipments`

| shipment_id | driver_id | status | destination |
| --- | --- | --- | --- |
| 1 | 1 | in_transit | Mumbai |
| 2 | 2 | delivered | Pune |
| 3 | 1 | in_transit | Nagpur |

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    driver_id INTEGER,
    status TEXT,
    destination TEXT
);

INSERT INTO shipments (shipment_id, driver_id, status, destination) VALUES
(1, 1, 'in_transit', 'Mumbai'),
(2, 2, 'delivered', 'Pune'),
(3, 1, 'in_transit', 'Nagpur');
```

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkakgms" 
 width="100%"
></iframe>

Expected output:

| shipment_id | driver_id | status | destination |
| --- | --- | --- | --- |
| 1 | 1 | in_transit | Mumbai |
| 3 | 1 | in_transit | Nagpur |

The generated SQL here is clean and matches exactly what a developer would have written by hand, and this is the ORM's main selling point: for straightforward queries like this one:

- The developer never has to write or think about SQL text at all.
- Work happens entirely in terms of objects and method calls in their own programming language, with the library handling the translation.

![An ORM translates object-style application code into SQL behind the scenes](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_orm_translates_objects_to_sql.png)

## Where an ORM's Convenience Can Hide a Real Cost

The `N+1 query` problem, covered in the performance unit, is the single most common way ORM-generated code goes wrong, precisely because the object-oriented style makes looping over related objects look completely innocent.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkakgwx" 
 width="100%"
></iframe>

Expected output:

| shipment_id | driver_id | status | destination |
| --- | --- | --- | --- |
| 1 | 1 | in_transit | Mumbai |
| 2 | 2 | delivered | Pune |
| 3 | 1 | in_transit | Nagpur |

- Nothing about the object-oriented loop above looks like a database performance hazard; `shipment.driver.driver_name` reads like ordinary property access, not a database call.
- This is exactly the danger: an ORM's abstraction can hide the fact that a query is happening at all, making it easy to write code that is correct but silently slow, unless the developer specifically knows to ask the ORM to fetch related data eagerly, in one combined query, rather than one at a time as each object is touched.

![ORM convenience can hide N+1 queries, while raw SQL makes one-query control explicit](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_orm_n_plus_one_vs_raw_sql.png)

## Where Raw SQL Is the More Direct Choice

For a genuinely complex report, involving several joins, `window functions`, and careful aggregation, exactly the kind of query built up across earlier chapters of this course, writing raw SQL directly is often more straightforward than coaxing an ORM's object-oriented interface into generating that same precise query.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkakh9t" 
 width="100%"
></iframe>

Expected output:

| driver_id | active_shipments |
| --- | ---: |
| 1 | 2 |

A query shaped like this, with `GROUP BY`, `HAVING`, and `ORDER BY` working together, is something every SQL developer can write directly and reason about precisely, with full control over exactly what plan the database is likely to choose.

Most ORMs do offer an escape hatch for running raw SQL directly when their object-oriented interface becomes more awkward than helpful, which is often the pragmatic middle ground real applications settle into: ORM for routine, simple operations, raw SQL for anything genuinely complex or performance-sensitive.

## The Trade-off, Honestly Stated

An ORM trades some control and some query-level performance transparency for faster, more consistent everyday development, less boilerplate, automatic protection against SQL injection through built-in parameterization, and code that reads naturally in the application's own programming language.

Raw SQL trades that convenience for full visibility into exactly what query runs and full control over its exact shape, at the cost of more code to write and maintain by hand for routine operations.

## ORM vs. Raw SQL at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;"></th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">ORM</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Raw SQL</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Everyday CRUD operations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fast to write, consistent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">More boilerplate</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Complex reporting queries</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can be awkward or inefficient</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Direct, precise control</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Risk of hidden performance issues</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Higher, especially N+1</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lower, since every query is explicit</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">SQL injection protection</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Built in, by default</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requires deliberate use of prepared statements</td>
    </tr>
  </tbody>
</table>

## Your Turn

Using the `shipments` table above, write the raw SQL a developer might reach for directly instead of relying on an ORM's default behavior, to fetch every shipment along with a count of how many other shipments share the same `driver_id`, in one single query rather than one query per shipment.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkakhkg" 
 width="100%"
></iframe>

Expected result and verification:

One approach uses a `window function` from earlier in this course: `SELECT shipment_id, driver_id, COUNT(*) OVER (PARTITION BY driver_id) AS driver_shipment_count FROM shipments;`, answering the question in a single query, exactly the kind of precise, one-query-only control raw SQL offers over letting an ORM's default per-object access pattern generate one query per row instead.

## Conclusion

An ORM speeds up routine, everyday database operations by letting a developer work in objects rather than SQL text, at the cost of sometimes hiding real query costs, most notoriously the N+1 pattern, while raw SQL offers full visibility and control at the cost of more code to write directly, and most real applications end up using both, an ORM for the routine cases and raw SQL for anything complex or performance-critical enough to need precise control.

The final lesson in this chapter looks at a concern that touches both styles equally: how a database's structure itself is changed safely over time as an application evolves.
