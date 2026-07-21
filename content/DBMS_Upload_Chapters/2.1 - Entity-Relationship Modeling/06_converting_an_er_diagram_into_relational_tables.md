## Introduction

Naina has finally finished the ER diagram for the college's course-registration system: rectangles for Student, Course, and Instructor, ovals hanging off each one for their attributes, and diamonds capturing how a student enrols in a course and how an instructor teaches a course. Her manager looks over the finished diagram, nods approvingly, and then asks the question Naina has been quietly dreading: "Good. Now how does this become an actual database?"

Naina realises that everything so far has been a picture of the world, not yet a database:

- A diagram cannot store a single row of real data; it can only describe the shape that the data will eventually take.
- What she needs now is a disciplined, repeatable procedure for turning every rectangle, oval, and diamond into something a relational database actually understands: tables, columns, and keys. That procedure is called **mapping an ER diagram to relational tables**, and once Naina learns its handful of rules, the translation stops feeling like guesswork and starts feeling almost mechanical.

**Definition:** Converting an ER diagram into relational tables follows a small, dependable set of rules: every entity becomes a table with its simple attributes as columns and its identifying attribute as the `primary key`, every one-to-many relationship is implemented by placing a `foreign key` on the table representing the "many" side, every one-to-one relationship places a unique `foreign key` on one side or merges the two tables outright, and every many-to-many relationship requires a new junction table holding a `foreign key` pointing to each of the two entities it connects.

![Intro visual for converting an er diagram into relational tables](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_intro_converting_an_er_diagram_into_relational_tables_matched_2ba9af3b.png)

## Rule One: Every Entity Becomes a Table

The first rule is the most intuitive. Every rectangle in the diagram, every entity, becomes its own table, and every simple attribute hanging off that entity becomes a column in that table. The attribute that was underlined in the diagram, the identifying one, becomes the table's `primary key`, the column guaranteed to hold a different value in every row.

Naina's Student entity, with attributes Roll Number (underlined), Name, and Date of Birth, becomes a Students table shaped like this.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Roll Number</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Name</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Date of Birth</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">20456</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rohan Mehta</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2005-03-14</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">20789</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Aisha Fernandes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2004-11-02</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">21103</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Devika Rao</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2005-07-30</td>
    </tr>
  </tbody>
</table>

Roll Number, the underlined attribute in the diagram, sits as the `primary key` here, exactly the same guarantee already familiar from working with `primary keys` directly: no two rows will ever share the same value in that column.

A composite attribute, like an address split into Street, City, and Pincode, simply becomes three separate columns rather than one, and a derived attribute like age is typically left out of the table entirely, since it can always be recalculated from date of birth whenever it is actually needed.

![Student entity and attributes mapped into a Students table with a primary key](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_entities_to_tables_mapping.png)

## Rule Two: One-to-Many Becomes a Foreign Key on the "Many" Side

The Instructor-teaches-Course relationship in Naina's diagram is one-to-many: one instructor can teach several courses, but each course, in this college, is taught by exactly one instructor. For a relationship shaped like this, no new table is needed at all. Instead, the "many" side simply gains a new column that points back to the "one" side, a column holding the `primary key` value of the related row.

That pointing column is a **`foreign key`**.

Naina's Courses table gains an Instructor ID column, holding the Instructor's identifying value for whichever instructor teaches that course.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Course Code</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Title</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Instructor ID</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">CS301</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Database Systems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">INS-14</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">CS302</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operating Systems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">INS-14</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">CS303</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Computer Networks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">INS-22</td>
    </tr>
  </tbody>
</table>

Reading this table confirms the one-to-many shape directly: INS-14 appears twice, meaning that one instructor teaches two courses, while each individual course row points to only one instructor. The rule is always the same regardless of the domain: the entity on the "many" side of a one-to-many relationship carries a `foreign key` column pointing at the entity on the "one" side, never the other way round.

Placing the `foreign key` on the "one" side instead would be unable to represent an instructor teaching more than a single course, since a single column can only ever hold one value per row.

## Rule Three: One-to-One Puts a Unique Foreign Key on Either Side

A one-to-one relationship, the kind already seen with an employee and their assigned desk, is the one shape Naina's own registration diagram does not happen to use, but it comes up often enough elsewhere to deserve its own rule. Unlike a one-to-many relationship, there is no automatic "many" side to host the `foreign key`, either entity's table could reasonably hold a reference to the other.

The usual choice is to place the `foreign key` on whichever side has total participation, the side guaranteed to always have a matching row, and to mark that column unique, so the database itself refuses to let the same desk end up assigned to two different employees.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Employee ID</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Name</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Desk ID</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">EMP-01</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rohan Mehta</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">DSK-14A</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">EMP-02</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sanjay Iyer</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">DSK-14B</td>
    </tr>
  </tbody>
</table>

Desk ID here is doing double duty, a `foreign key` pointing at the Desks table and a uniquely constrained column at the same time, and that uniqueness is exactly what stops one desk from quietly being handed to two employees.

When both sides of a one-to-one relationship have total participation, some designs skip a `foreign key` altogether and merge the two entities into a single table instead, since neither one can ever exist without the other anyway.

## Rule Four: Many-to-Many Needs a Table of Its Own

The Student-enrols-in-Course relationship is where the mechanical simplicity of rule two breaks down. This relationship is many-to-many: one student takes several courses, and one course has several students. Neither the Students table nor the Courses table can hold a single `foreign key` column for this relationship, because a single column in a single row cannot represent "several" values at once.

The fix is to introduce an entirely new table, often called a junction table or associative table, whose entire purpose is to hold the connection between the two sides. Each row in this new table represents one specific student-course pairing, and it does so by holding a `foreign key` pointing to the student and another `foreign key` pointing to the course.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Roll Number</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Course Code</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">20456</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">CS301</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">20456</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">CS303</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">20789</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">CS301</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">21103</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">CS302</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">21103</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">CS303</td>
    </tr>
  </tbody>
</table>

Look closely at what this table allows. Roll Number 20456 appears twice, once for each course that student is enrolled in, and Course Code CS301 appears twice, once for each student enrolled in it. Both sides can repeat freely, which is exactly the flexibility a many-to-many relationship requires and a single `foreign key` column never could have provided.

If the relationship itself carried its own attribute, say an enrolment date recording exactly when the student joined that course, that attribute would live directly inside this same junction table, since the date describes the enrolment, not the student or the course individually.

![One-to-many relationships becoming foreign keys and many-to-many relationships becoming junction tables](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/12_relationships_to_foreign_keys_and_junctions.png)

## Mapping Rules at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">ER diagram element</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Becomes in the relational design</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Entity (rectangle)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A table</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simple attribute (oval)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A column in that entity&#x27;s table</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Identifying attribute (underlined oval)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The table&#x27;s primary key</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Composite attribute</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Several separate columns, one per component part</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Derived attribute</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Usually no column at all; recalculated when needed</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One-to-many relationship</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A foreign key column on the table for the &quot;many&quot; side</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One-to-one relationship</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A unique foreign key on one side (often the side with total participation), or a merged table</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Many-to-many relationship</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A brand new junction table holding a foreign key to each side</td>
    </tr>
  </tbody>
</table>

## Walking the Full Diagram, Table by Table

Naina applies the three rules to her entire registration diagram in one pass and ends up with four tables where she once had three rectangles and two diamonds: a Students table, a Courses table, an Instructors table, and a new Enrolments table born entirely out of the many-to-many relationship.

The Courses table quietly grew an extra Instructor ID column that never appeared as its own rectangle in the diagram, and the Enrolments table did not correspond to any rectangle at all, it exists purely because a many-to-many diamond needed somewhere to live.

This is the moment Naina's earlier objection, that a diagram is only a picture and not a database, gets fully resolved. Every shape she drew has a precise, repeatable destination: entities become tables, simple attributes become columns, identifying attributes become `primary keys`, one-to-many relationships become a single `foreign key`, and many-to-many relationships become a table of their own.

None of it is arbitrary, and none of it required guessing, because each rule follows directly from what the diagram was already saying about cardinality and participation.

## Your Turn: Map the Diagram

A gym's ER diagram has a Trainer entity and a Member entity, connected by a many-to-many "Trains" relationship that itself carries a session date attribute. Trainer also has a one-to-one relationship with a Locker entity, with total participation on the Locker side. Describe the tables this diagram produces, including any table that does not correspond to a rectangle at all.

A working answer: Trainer becomes a Trainers table and Member becomes a Members table, each with their own simple attributes as columns. Trains, being many-to-many, needs a brand new junction table, say TrainingSessions, holding a foreign key to Trainer, a foreign key to Member, and the session date attribute that belongs to the relationship itself, not to either entity alone. Trainer-Locker, being one-to-one with total participation on the Locker side, places a unique foreign key pointing to Trainer on the Lockers table, guaranteeing no trainer is ever assigned two lockers.

## Conclusion

Converting an ER diagram into relational tables follows a small, dependable set of rules: every entity becomes a table with its simple attributes as columns and its identifying attribute as the `primary key`, every one-to-many relationship is implemented by placing a `foreign key` on the table representing the "many" side, every one-to-one relationship places a unique `foreign key` on one side or merges the two tables outright, and every many-to-many relationship requires a new junction table holding a `foreign key` pointing to each of the two entities it connects.

What began as rectangles, ovals, and diamonds ends as a concrete set of tables, ready to hold real rows of real data. Naina can now answer her manager's original question directly: her Student, Course, and Instructor rectangles become three tables, the Instructor-teaches-Course diamond becomes an Instructor ID column on Courses, and the Student-enrols-in-Course diamond becomes a brand new Enrolments table.

This conversion is only the first pass, though, and a freshly mapped set of tables is not automatically free of the kinds of redundancy and inconsistency that make a database hard to trust. Checking whether a table's columns truly belong together, and tightening the design where they do not, is the natural next concern once the raw translation from diagram to tables is complete.
