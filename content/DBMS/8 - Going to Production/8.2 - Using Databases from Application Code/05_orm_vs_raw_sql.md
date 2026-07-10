## Introduction

Every query in this course has been written as raw SQL, typed directly. Much real application code, especially in frameworks built around languages like Python, Java, or Ruby, instead uses an **object-relational mapper**, or ORM, a library that lets a developer work with database rows as ordinary objects in their programming language, generating the actual SQL behind the scenes. Neither approach is universally correct; each trades away something the other offers, and knowing what that trade-off actually is matters more than picking a side.

## What an ORM Actually Generates

An ORM's core promise is translating object-oriented code into SQL automatically, without the developer writing SQL text directly.

```postgresql file=orm_demo.sql
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

```postgresql with=orm_demo.sql
-- ORM-style code, in pseudocode, might read like:
-- shipments = Shipment.objects.filter(status='in_transit')
-- Behind the scenes, this generates and runs SQL equivalent to:
SELECT shipment_id, driver_id, status, destination
FROM shipments
WHERE status = 'in_transit';
```

The generated SQL here is clean and matches exactly what a developer would have written by hand, and this is the ORM's main selling point: for straightforward queries like this one:

- The developer never has to write or think about SQL text at all.
- Work happens entirely in terms of objects and method calls in their own programming language, with the library handling the translation.

## Where an ORM's Convenience Can Hide a Real Cost

The `N+1 query` problem, covered in the performance unit, is the single most common way ORM-generated code goes wrong, precisely because the object-oriented style makes looping over related objects look completely innocent.

```postgresql with=orm_demo.sql
-- ORM-style code that looks perfectly reasonable:
-- shipments = Shipment.objects.all()
-- for shipment in shipments:
--     print(shipment.driver.driver_name)
-- Depending on the ORM's configuration, accessing `.driver` inside this loop
-- can silently trigger one additional query PER shipment, exactly the
-- N+1 pattern covered earlier in this course:
SELECT shipment_id, driver_id, status, destination FROM shipments;
-- followed by one of these per row:
-- SELECT * FROM drivers WHERE driver_id = 1;
-- SELECT * FROM drivers WHERE driver_id = 2;
-- SELECT * FROM drivers WHERE driver_id = 1;
```

Nothing about the object-oriented loop above looks like a database performance hazard; `shipment.driver.driver_name` reads like ordinary property access, not a database call. This is exactly the danger: an ORM's abstraction can hide the fact that a query is happening at all, making it easy to write code that is correct but silently slow, unless the developer specifically knows to ask the ORM to fetch related data eagerly, in one combined query, rather than one at a time as each object is touched.

## Where Raw SQL Is the More Direct Choice

For a genuinely complex report, involving several `join`s, `window functions`, and careful aggregation, exactly the kind of query built up across earlier chapters of this course, writing raw SQL directly is often more straightforward than coaxing an ORM's object-oriented interface into generating that same precise query.

```postgresql with=orm_demo.sql
SELECT driver_id, COUNT(*) AS active_shipments
FROM shipments
WHERE status = 'in_transit'
GROUP BY driver_id
HAVING COUNT(*) > 0
ORDER BY active_shipments DESC;
```

A query shaped like this, with `GROUP BY`, `HAVING`, and `ORDER BY` working together, is something every SQL developer can write directly and reason about precisely, with full control over exactly what plan the database is likely to choose. Most ORMs do offer an escape hatch for running raw SQL directly when their object-oriented interface becomes more awkward than helpful, which is often the pragmatic middle ground real applications settle into: ORM for routine, simple operations, raw SQL for anything genuinely complex or performance-sensitive.

## The Trade-off, Honestly Stated

An ORM trades some control and some query-level performance transparency for faster, more consistent everyday development, less boilerplate, automatic protection against SQL injection through built-in parameterization, and code that reads naturally in the application's own programming language. Raw SQL trades that convenience for full visibility into exactly what query runs and full control over its exact shape, at the cost of more code to write and maintain by hand for routine operations.

## ORM vs. Raw SQL at a Glance

| | ORM | Raw SQL |
|---|---|---|
| Everyday CRUD operations | Fast to write, consistent | More boilerplate |
| Complex reporting queries | Can be awkward or inefficient | Direct, precise control |
| Risk of hidden performance issues | Higher, especially N+1 | Lower, since every query is explicit |
| SQL injection protection | Built in, by default | Requires deliberate use of prepared statements |

## Your Turn

Using the `shipments` table above, write the raw SQL a developer might reach for directly instead of relying on an ORM's default behavior, to fetch every shipment along with a count of how many other shipments share the same `driver_id`, in one single query rather than one query per shipment.

```postgresql with=orm_demo.sql
-- Write your query below
```

One approach uses a `window function` from earlier in this course: `SELECT shipment_id, driver_id, COUNT(*) OVER (PARTITION BY driver_id) AS driver_shipment_count FROM shipments;`, answering the question in a single query, exactly the kind of precise, one-query-only control raw SQL offers over letting an ORM's default per-object access pattern generate one query per row instead.

## Conclusion

An ORM speeds up routine, everyday database operations by letting a developer work in objects rather than SQL text, at the cost of sometimes hiding real query costs, most notoriously the N+1 pattern, while raw SQL offers full visibility and control at the cost of more code to write directly, and most real applications end up using both, an ORM for the routine cases and raw SQL for anything complex or performance-critical enough to need precise control. The final lesson in this chapter looks at a concern that touches both styles equally: how a database's structure itself is changed safely over time as an application evolves.
