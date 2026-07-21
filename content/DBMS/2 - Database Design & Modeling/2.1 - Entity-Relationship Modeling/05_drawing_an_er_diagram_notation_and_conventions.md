## Introduction

Vivek has spent the last two weeks talking his hospital-management design through out loud: entities, attributes, cardinality, participation, all of it worked out carefully in sentences and small `tables`.

His manager stops him mid-explanation and asks a fair question: "This is solid work, but if I hand your notes to another developer who was not in the room with you, could they understand the design without you narrating it?" Vivek admits they probably could not.

Sentences are precise, but they are slow to scan, and a design with twelve entities and twenty relationships turns into a wall of paragraphs nobody wants to read twice.

What Vivek needs is a shared visual language, one where a rectangle always means the same thing no matter who drew it, and a diamond always means the same thing no matter which system it describes.

That shared language is the **ER diagram**, a standardised way of drawing entities, their attributes, and the relationships between them, using a small, fixed set of shapes and lines so that anyone trained in the notation can read the design at a glance, without needing the original designer in the room to explain it.

**Definition:** An ER diagram gives a design a shared visual vocabulary: rectangles for entities, ovals for attributes, diamonds for relationships, with underlines, dashes, and double outlines layered on to capture identifying, derived, and multivalued attributes, and with labelled or crow's-foot lines capturing cardinality and participation together.

<!--
IMAGE PROMPT  ->  generate as images/05_intro_drawing_an_er_diagram_notation_and_conventions.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: DBMS course introduction image based directly on the opening scene of this lesson. Use the named person, setting, and database problem from the Introduction.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue database forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A simple visual of the Introduction: Vivek has spent the last two weeks talking his hospital-management design through out loud: entities, attributes, cardinality, participation, all of it worked out carefully in sentences and small tables. His manager stops him mid-explanation and asks a fair.

ON-IMAGE TEXT: show a short bold title "Drawing An Er Diagram Notation And Conventions" plus only these few labels, large and legible: Drawing, Diagram, Notation. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing DBMS reading-material image standards.
-->

![Intro visual for drawing an er diagram notation and conventions](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_intro_drawing_an_er_diagram_notation_and_conventions.png)

## The Core Shapes and What Each One Means

An ER diagram leans on a small, disciplined set of shapes, and the discipline is the entire point: reusing the same shape for the same kind of idea every single time is what makes the diagram readable to a stranger.

Three shapes carry three different meanings:

- A rectangle labelled "Patient" represents an entity, a distinct real-world thing the system tracks.
- Small ovals hanging off that rectangle, connected by short lines, each labelled with one word, "Patient ID," "Name," "Date of Birth," "Blood Group," are attributes, each one describing one property of the entity they are attached to.
- A diamond shape sitting on the line between the Patient rectangle and a second rectangle labelled "Doctor," labelled "Admits," is the relationship, the meaningful `connection` between the two entities it touches.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Shape</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Represents</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example label</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rectangle</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Entity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Patient, Doctor, Appointment</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Oval</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Attribute</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Patient ID, Name, Date of Birth</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Diamond</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Relationship</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Admits, Prescribes, Schedules</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Line</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Connection between a shape and what it belongs to</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Connects Patient to its Patient ID oval, and to the Admits diamond</td>
    </tr>
  </tbody>
</table>

Every shape in the diagram is connected to something by a plain line, and the lines themselves carry no separate meaning beyond "this thing belongs to, or takes part in, that thing." An oval floating with no line to any rectangle would be meaningless, because an attribute detached from its entity is not describing anything.

![ER diagram notation using rectangles for entities, ovals for attributes, and diamonds for relationships](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_er_diagram_core_notation.png)

## Marking the Finer Details Within Each Shape

Plain rectangles and ovals capture the basic shapes, but Vivek's diagram also needs to show details covered already: which attribute is the identifying one, which attribute is composite, derived, or multivalued, and which entity has total participation in a relationship.

The identifying attribute, the one that plays the `role` of uniquely picking out one instance of the entity, gets its label underlined inside its oval, so "Patient ID" appears underlined while "Name" does not. A composite attribute, like Address, is drawn as an oval that itself has smaller ovals branching off it, Street, City, Pincode, visually showing that the whole is made of parts.

A derived attribute gets a dashed outline instead of a solid one, a quiet visual reminder that this value is calculated rather than stored. A multivalued attribute is drawn with a double-lined oval, signalling that a single entity instance can carry more than one value here.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Detail being shown</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">How the diagram marks it</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Identifying attribute</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Underlined label inside the oval</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Composite attribute</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Oval with smaller ovals branching off it</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Derived attribute</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dashed oval outline</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Multivalued attribute</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Double-lined oval outline</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Total participation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A double line connecting the entity to the relationship diamond</td>
    </tr>
  </tbody>
</table>

## Showing Cardinality on the Connecting Lines

The line between an entity and a relationship diamond is also where cardinality gets written down. Two common conventions exist, and Vivek's team uses the first because it reads cleanly in a text-heavy specification document.

The first convention simply labels the line with "1" or "N" (sometimes "M") right where it touches each shape: a line from Department to the Admits-like "Has Employees" diamond is labelled "1" on the Department side and "N" on the Employees side, spelling out one-to-many directly on the diagram.

The second convention, popular in more polished diagramming tools, uses small fork-shaped marks called a crow's foot at the end of a line to mean "many," and a single short tick mark to mean "one," so a many-to-many relationship shows a crow's foot at both ends of its connecting line.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Cardinality</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">1/N label convention</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Crow&#x27;s foot convention</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One-to-one</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">&quot;1&quot; at both ends</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A single tick mark at both ends</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One-to-many</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">&quot;1&quot; at one end, &quot;N&quot; at the other</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A tick mark at one end, a crow&#x27;s foot at the other</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Many-to-many</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">&quot;N&quot; at both ends (or &quot;M&quot; and &quot;N&quot;)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A crow&#x27;s foot at both ends</td>
    </tr>
  </tbody>
</table>

Total participation is layered onto the same line using a double line instead of a single line between the entity and the diamond, while partial participation stays a plain single line.

In Vivek's hospital diagram, the line between Patient and the Admits diamond is doubled, because every admitted patient must have an admitting doctor, while the line between Doctor and the same diamond stays single, because a doctor can currently have zero admitted patients.

![ER notation details for identifying, composite, derived, multivalued, cardinality, and total participation](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_er_diagram_detail_notation.png)

## Notation Legend

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Symbol</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rectangle</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An entity</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Oval (solid, single line)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A simple attribute</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Oval (dashed line)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A derived attribute</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Oval (double line)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A multivalued attribute</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ovals nested off a larger oval</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A composite attribute and its parts</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Diamond</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A relationship connecting two or more entities</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Underlined text inside an oval</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The identifying attribute of an entity</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Single line from entity to diamond</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Partial participation in that relationship</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Double line from entity to diamond</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Total participation in that relationship</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">&quot;1&quot; / &quot;N&quot; labels or crow&#x27;s foot marks on a line</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The cardinality of that side of the relationship</td>
    </tr>
  </tbody>
</table>

## Reading a Finished Diagram Like a Sentence

Once the shapes and lines are all in place, Vivek's manager teaches him to read the diagram out loud the way a sentence reads: start at one rectangle, follow the line to the diamond, note whether that line is single or double, read the "1" or "N" label, then follow the line onward to the next rectangle.

"Patient, connected by a double line labelled N, to Admits, connected by a single line labelled 1, to Doctor" translates directly into the sentence "many patients are admitted, and every admitted patient must have exactly one admitting doctor, though a doctor may have zero admitted patients right now." Every fact that took Vivek a full paragraph to explain earlier now sits compactly inside a handful of connected shapes, readable by anyone who knows the legend, without a single word of narration needed.

## Your Turn: Read the Notation

A diagram shows a rectangle labelled "Author" connected by a single line to a diamond labelled "Writes," which connects by a double line labelled "N" to a rectangle labelled "Book." The Book rectangle also has an oval attached with a dashed outline, labelled "Years in Print." Describe, in a sentence, what this diagram is telling you, including what the dashed oval means.

A working answer: the single line on the Author side means partial participation, an author can exist in the system without having written a book yet, while the double line on the Book side means total participation, every book must have been written by some author. The "N" label means one author can write many books. The dashed "Years in Print" oval is a derived attribute, a value the system calculates from a book's publication date rather than storing directly, exactly the way Vivek's notation marks a computed fact with a dashed outline instead of a solid one.

## Conclusion

An ER diagram gives a design a shared visual vocabulary: rectangles for entities, ovals for attributes, diamonds for relationships, with underlines, dashes, and double outlines layered on to capture identifying, derived, and multivalued attributes, and with labelled or crow's-foot lines capturing cardinality and participation together.

Learning this small, fixed set of shapes is what turns a design that only its author can explain into one that any trained reader can pick up and understand unaided. Vivek's hospital-management diagram, with Patient, Doctor, and Admits drawn out in the standard notation, can now finally answer his manager's original challenge: another developer can pick it up and read it correctly without Vivek in the room to narrate it.

Everything built up so far, the entities, their attributes, the relationships between them, their cardinality, and their participation, exists for one final purpose: to be translated faithfully into the `rows` and `columns` a relational `database` actually stores, which is the last, very practical step still ahead.
