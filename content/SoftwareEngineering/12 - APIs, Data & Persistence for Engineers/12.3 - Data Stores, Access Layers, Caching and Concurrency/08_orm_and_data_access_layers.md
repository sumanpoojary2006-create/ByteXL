## Introduction

Application code is written in terms of objects with behaviour, while relational databases store rows in tables. The two models differ in how they represent relationships, identity, inheritance, and collections, and the gap between them is known as the object-relational impedance mismatch. Every application that stores objects in a relational database must bridge it somehow. A data access layer isolates the rest of the program from the details of storage, and an object-relational mapper automates much of the translation.

This topic explains the mismatch, the main patterns for data access, what mappers do, their typical pitfalls, and how to decide how much to rely on them.

**Definition:** A data access layer is the part of an application that is responsible for reading and writing persistent data, hiding the details of the storage technology from the rest of the code, and an object-relational mapper (ORM) is a tool that automatically translates between objects in a program and rows in relational tables.

<!--
IMAGE PROMPT  ->  generate as images/08_intro_orm_and_data_access_layers.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Three horizontal bands: top band Business logic with object shapes, middle band Data access layer with a translator icon between objects and rows, bottom band Database with tables; arrows pass only between adjacent bands.

ON-IMAGE TEXT: show a short bold title "Object-Relational Mapping and Data Access Layers" plus only these few labels, large and legible: Objects, Mapping, Rows. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Impedance Mismatch

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Concern</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">In objects</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">In relational tables</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Structure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Objects contain other objects and collections, forming graphs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Flat rows, with relationships by foreign keys</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Identity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two references are the same if they point to the same object in memory</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rows are the same if their primary keys match</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inheritance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Classes extend other classes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No direct equivalent; must be simulated</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Relationships</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Navigate by following references</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Combine tables with joins</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Types</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Language-specific types</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Database types, with different rules for text, numbers, dates, and nulls</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Access</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One object at a time, by navigation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sets of rows, by queries</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Encapsulation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data hidden behind behaviour</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data exposed in columns</td>
    </tr>
  </tbody>
</table>

### Representing Inheritance

There are three common ways to store a hierarchy of classes in tables.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strategy</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Trade-off</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Single table</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">All classes in one table with a column that says which class each row is</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fast and simple; many empty columns; weaker constraints</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Table per class (joined)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A table for each class, joined by key</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clean structure; joins on every read</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Table per concrete class</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A complete table for each concrete class</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No joins; duplicated columns; difficult to query across classes</td>
    </tr>
  </tbody>
</table>

## Data Access Patterns

Several patterns, many described by Martin Fowler in his book on enterprise application architecture, organise access to storage.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Pattern</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data Access Object (DAO)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An object that wraps all access to a particular kind of data, offering methods to find, save, and remove</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Isolates database specifics from business code</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Repository</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A collection-like interface for the objects of a domain concept, which hides how and where they are stored; part of domain-driven design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Speaks the language of the domain, not of tables</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Active Record</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Each object represents a row and knows how to save and load itself</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simple; mixes business and persistence concerns; suits simple domains</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data Mapper</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A separate mapper moves data between objects and the database, so the objects know nothing about storage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keeps the domain clean; more machinery</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unit of Work</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tracks all the objects changed during a business operation, and writes the changes together in one transaction</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ensures consistency and reduces round trips</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Identity Map</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ensures each row is loaded into only one object during a unit of work</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Avoids conflicting copies</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lazy Loading</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Related data is fetched only when first needed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Saves work; can cause many hidden queries</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Query Object / Specification</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Queries described as objects that can be combined</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reusable and testable</td>
    </tr>
  </tbody>
</table>

These connect to the design principles of earlier units. A repository applies separation of concerns and dependency inversion: business logic depends on an abstract interface, so storage can be replaced and testing can use an in-memory substitute.

## What an ORM Does

An ORM provides:

- **Mapping** declared between classes and tables, and fields and columns.
- **Generated queries** for common operations, so the developer rarely writes routine statements.
- **Change tracking,** which notices which objects were modified and writes only those.
- **Relationship handling,** including loading related objects.
- **Caching** within an operation or across operations.
- **Schema tools,** such as generating migrations from model changes.
- **Portability** across database products to some degree.
- A **query language** at the level of objects.

Widely used ORMs include Hibernate and JPA in the Java ecosystem, Entity Framework for .NET, Django ORM and SQLAlchemy for Python, ActiveRecord for Ruby, and Prisma and TypeORM in the JavaScript world.

### Benefits

- Less repetitive code, so faster development.
- Consistent handling of connections, transactions, and parameters, with protection against injection by default.
- A domain model expressed in objects.
- Easier changes of database and easier testing.

### Costs and Risks

- **Leaky abstraction.** Developers must still understand SQL and the database, because the ORM's behaviour shows through in performance and errors.
- **Hidden queries** and difficult-to-predict cost.
- **Complexity** of configuration and of the ORM's own rules.
- **Weaker use of database-specific features** and bulk operations.
- **A temptation to ignore the data model,** leading to poor schemas.

The well-known critique, sometimes called "the Vietnam of computer science" in an essay by Ted Neward, holds that the mismatch is deep and that trying to hide it entirely fails. A balanced view is that ORMs are very useful for ordinary operations and need to be supplemented by direct queries for demanding ones.

## Common Pitfalls

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Pitfall</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What happens</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Remedy</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">N+1 queries</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Loading a list of N items and then the related data of each item causes one query for the list plus N more, which is slow at scale</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fetch related data in the same query or in one batched query (eager loading); check the number of queries issued</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Over-fetching</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Loading entire objects and relations when a few fields are needed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Select only needed columns; use projections</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lazy loading outside its scope</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Related data requested after the connection or session has closed fails</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Load what is needed within the unit of work</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Long-lived sessions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Objects held across user interactions become stale and hold resources</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep units of work short</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unbounded results</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Loading a whole large table into memory</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Page results; stream large sets</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Row-by-row updates</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Thousands of single changes where one set-based statement would do</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use bulk operations</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ignoring transactions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Changes committed piecemeal</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Define the unit of work explicitly</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Generated schemas used blindly</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Missing indexes and poor types</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Review and tune the schema and migrations</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Leaking entities into APIs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Persistence objects are sent to clients, exposing internals and tying the API to the schema</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use separate data transfer objects</td>
    </tr>
  </tbody>
</table>

## Designing a Data Access Layer

- **Hide storage behind an interface** that expresses what the application needs, such as "find the open orders for this customer", not how.
- **Keep business rules out of the data layer,** and persistence details out of business rules.
- **Put transaction boundaries** at the level of a business operation.
- **Return domain objects or purpose-built data transfer objects,** not raw rows.
- **Handle errors** at the boundary: translate database-specific failures into meaningful conditions.
- **Test it against a real database** in integration tests, since mocks cannot show whether queries are correct, and test business logic with in-memory substitutes.
- **Measure** the queries a feature actually runs.

## Reads and Writes Differ

Many systems separate the model for **changing** data from the model for **reading** it, a pattern called **CQRS** (command query responsibility segregation). Reads can use simple queries tailored to screens, while writes go through the domain model with its rules. This is helpful where read and write needs diverge sharply, and is unnecessary for simple applications.

## How Much Mapping?

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Situation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Approach</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ordinary create, read, update, delete operations on business entities</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An ORM is productive</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Complex reports and heavy queries</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hand-written queries, perhaps through the same access layer</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Bulk loads and data pipelines</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Direct database facilities</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Very simple scripts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A thin library may suffice</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Non-relational stores</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mappers and client libraries suited to that store</td>
    </tr>
  </tbody>
</table>

Most mature systems mix: the ORM for routine work and carefully written queries where performance or clarity demands.

<!--
IMAGE PROMPT  ->  generate as images/02_the_n_plus_one_problem.png   (16:9 explanatory diagram, place here)

Two panels. Left (red): one query fetches a list of orders, then arrows fan out to ten separate queries for each order's lines, with a stopwatch showing a long time. Right (green): a single combined query returning orders with their lines, one arrow, short stopwatch.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Mind the Gap

1. A page showing 50 orders with their items takes seconds to load, and logs show 51 database queries. What is the problem and the fix?
2. Why might a team put a repository interface between business logic and the ORM?
3. A developer sends persistence entity objects straight to clients through the API. Give two problems.

For case 1, N+1 queries; fetch the items along with the orders in a single combined or batched query. For case 2, to decouple business code from storage, allowing replacement and testing with in-memory substitutes. For case 3, internal fields are exposed and the API becomes tied to the database schema, so schema changes break clients; use separate transfer objects.

## Conclusion

A data access layer is the part of an application that is responsible for reading and writing persistent data, hiding the details of the storage technology from the rest of the code, and an object-relational mapper (ORM) is a tool that automatically translates between objects in a program and rows in relational tables. Used with an understanding of the mismatch and of the underlying database, they remove drudgery without hiding what matters.

Even a well-designed access layer is limited by the speed of the store. The next topic introduces caching, the most common way of making data access faster.
