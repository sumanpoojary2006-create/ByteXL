## Introduction

Most systems exist to create, store, and use data: orders, customers, products, payments. Decisions about what data is held and how it is related shape both the design of the software and the correctness of what it records. Data modeling is the activity of describing this data independently of the program that manipulates it. The entity-relationship (ER) diagram is the standard notation for it.

**Definition:** Data modeling is the practice of identifying the entities about which a system must store information, their attributes, and the relationships among them, and an entity-relationship diagram is the graphical notation used to show this structure.

<!--
IMAGE PROMPT  ->  generate as images/09_intro_data_modeling_and_entity_relationship_diagrams.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Three rectangles labelled Customer, Order, Dish with attribute lists, joined by diamond or crow-foot relationship lines labelled places and contains, with a one-to-many mark on each.

ON-IMAGE TEXT: show a short bold title "Data Modeling and Entity-Relationship Diagrams" plus only these few labels, large and legible: Entity, Attribute, Relationship. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Building Blocks

Peter Chen introduced the entity-relationship model in 1976. Its core elements are:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Element</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Entity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A thing of interest about which data is stored</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Customer, Order, Dish</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Attribute</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A property of an entity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Customer name, Order date, Dish price</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Key (identifier)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An attribute, or set of attributes, that uniquely identifies each instance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Order number</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Relationship</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An association between entities</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A Customer places an Order</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cardinality</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How many instances can participate on each side of a relationship</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One customer, many orders</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Participation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Whether taking part is mandatory or optional</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every order must have a customer</td>
    </tr>
  </tbody>
</table>

## Cardinality

Cardinality is the heart of a data model, because it records business rules.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Type</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One-to-one</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Each instance of A relates to at most one of B, and the other way round</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Employee and parking space</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One-to-many</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One A relates to many Bs, but each B relates to one A</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One customer places many orders</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Many-to-many</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Many As relate to many Bs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Orders and dishes: an order contains many dishes, and a dish appears in many orders</td>
    </tr>
  </tbody>
</table>

## Resolving Many-to-Many Relationships

A many-to-many relationship cannot be stored directly in a relational database. It is resolved by introducing an **associative entity** that sits between the two. For orders and dishes, the associative entity is Order Line, which records one dish on one order along with details that belong to the pairing, such as quantity and the price at the time. Order Line has a many-to-one relationship with Order and a many-to-one relationship with Dish. The associative entity is often a hidden business concept worth naming.

## Notations

Several notations draw the same ideas.

- **Chen notation** uses rectangles for entities, ovals for attributes, and diamonds for relationships.
- **Crow's foot notation** uses rectangles listing attributes, with line endings that resemble a bird's foot to show "many." It is the most common in practice.
- **UML class diagrams** can also model data, using classes for entities and multiplicities for cardinality.

The notation matters less than the thinking: what are the entities, and how are they related?

## Three Levels of Data Model

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Level</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Describes</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Audience</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Detail</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Conceptual</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The main entities and relationships in business terms</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stakeholders and analysts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Few attributes, no technology</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Logical</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Entities, attributes, keys, and relationships in full, independent of a specific database product</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Designers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Complete, normalised structure</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Physical</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tables, columns, types, indexes for a specific database</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Database engineers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Technology-specific</td>
    </tr>
  </tbody>
</table>

Teams usually progress from conceptual to logical to physical as understanding and decisions firm up.

## Data Modeling and Class Modeling

Class diagrams and ER diagrams look alike but have different focus. A class diagram describes **objects with behaviour**, and includes operations. An ER diagram describes **stored data** and has no operations. In many systems, a domain model leads to both: persistent classes are mapped to entities and tables. Differences, such as how inheritance is stored, are handled in the design of the data layer.

## Quality of a Data Model

A good model has entities that match real business concepts, a key for each entity, relationships whose cardinality matches the rules, and no repeated facts stored in several places. Avoiding redundancy is the purpose of **normalisation**, a technique for organising data to prevent inconsistencies. A database course treats it in depth. Here it is enough to know that each fact should be stored once.

<!--
IMAGE PROMPT  ->  generate as images/02_er_order_dish_order_line.png   (16:9 explanatory diagram, place here)

An ER diagram in crow's foot notation. Customer one-to-many Order, Order one-to-many Order Line, Dish one-to-many Order Line, showing how the many-to-many between Order and Dish is resolved by the associative entity Order Line with attributes quantity and unit price.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Model the Data

For a library, consider entities Member, Book, and Loan.

1. What is the cardinality between Member and Loan?
2. What problem arises if Member and Book are linked directly many-to-many to record borrowing, and how is it solved?

A member can make many loans, and each loan belongs to one member, so the relationship is one-to-many. A direct many-to-many link between Member and Book cannot record details of each borrowing, such as the date borrowed and the due date. The solution is the associative entity Loan, which carries those details and relates one member to one book copy for one period.

## Conclusion

Data modeling is the practice of identifying the entities about which a system must store information, their attributes, and the relationships among them, and an entity-relationship diagram is the graphical notation used to show this structure. Getting cardinality and keys right at this stage prevents inconsistencies that are costly to repair once data exists.

Both class and data models depend on a clear understanding of the problem area. The next topic describes how to build that understanding as a domain model.
