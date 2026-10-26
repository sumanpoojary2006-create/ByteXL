## Introduction

Classes are rarely useful alone. A design is mostly a statement about how classes relate: which ones know about each other, which are built from others, and which are special cases of others. UML provides distinct kinds of line for these relationships, and choosing the right one communicates design intent clearly.

**Definition:** The relationships in a class diagram, association, aggregation, composition, generalisation, realisation, and dependency, describe respectively how objects are linked, how a whole is made of parts with or without shared lifetime, how one class specialises another, how a class fulfils an interface, and how one class relies on another.

<!--
IMAGE PROMPT  ->  generate as images/04_intro_associations_aggregation_composition_and_inheritance.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Six small diagrams in a grid, each showing two boxes joined by a different line style: plain line, hollow diamond, filled diamond, hollow triangle, dashed triangle, dashed arrow.

ON-IMAGE TEXT: show a short bold title "Relationships in Class Diagrams" plus only these few labels, large and legible: Link, Part, Kind. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Association

An **association** is a structural link between classes: objects of one know about, or hold, objects of the other. It is drawn as a solid line, often with a name, a multiplicity at each end, and optionally an arrow showing direction of navigation. For example, a Customer places Orders. Associations can have **roles**, names describing the part each class plays, such as "buyer" at the Customer end.

## Aggregation and Composition

Both describe a **whole and its parts**, drawn with a diamond at the whole's end.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aggregation (hollow diamond)</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Composition (filled diamond)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Meaning</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A weak "has-a": the whole contains parts, but they can exist independently</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A strong "owns-a": the parts belong to exactly one whole</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lifetime of the part</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Independent of the whole</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ends when the whole is destroyed</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sharing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A part may belong to several wholes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A part belongs to only one whole</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Example</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A Menu has Dishes; a dish remains if the menu is retired</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An Order has Order Items; the items cease to exist if the order is deleted</td>
    </tr>
  </tbody>
</table>

The distinction is subtle, and many designers use plain association instead of aggregation because it adds little. Composition is worth using when ownership and lifetime really matter: if the whole is deleted, so are its parts.

## Generalisation (Inheritance)

**Generalisation** shows that one class is a more specific kind of another: the child inherits the attributes and operations of the parent and may add or change some. It is drawn as a solid line with a hollow triangle pointing at the parent. For example, Card Payment and Cash Payment are kinds of Payment. This is an **is-a** relationship.

Use generalisation when the child truly **is a** special case that can be used anywhere the parent is expected. It is often overused: a class that only shares some behaviour with another is better modelled by composition, where it **has a** component that does the work. Many designers advise preferring composition to inheritance because inheritance couples the child tightly to the parent.

## Realisation

A **realisation** relationship, drawn as a dashed line with a hollow triangle, connects a class to an interface it implements. It means the class promises to provide the operations the interface defines. For example, a Card Payment class realises a Payment Method interface. This allows other classes to depend on the interface without knowing which class provides it.

## Dependency

A **dependency**, drawn as a dashed arrow, is the weakest relationship. It means one class uses another temporarily, for example as a parameter or local variable, so a change to the used class might affect the user. Fewer and simpler dependencies make software easier to change.

## Summary of Relationships

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Relationship</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Line</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Reading</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Association</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Solid line (optional arrow)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"knows about" or "is linked to"</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Customer places Order</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Aggregation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Solid line with hollow diamond at the whole</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"has parts" (weak)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Menu has Dishes</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Composition</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Solid line with filled diamond at the whole</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"is made of" (strong ownership)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Order is made of Order Items</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Generalisation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Solid line with hollow triangle at the parent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"is a kind of"</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Card Payment is a kind of Payment</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Realisation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dashed line with hollow triangle at the interface</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"implements"</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Card Payment implements Payment Method</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dependency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dashed arrow toward the used class</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"uses temporarily"</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Receipt Printer uses Order</td>
    </tr>
  </tbody>
</table>

## Choosing the Right One

1. Start with **association** if objects simply need to refer to each other.
2. Use **composition** if the part cannot exist without the whole and is not shared.
3. Use **generalisation** only for a genuine is-a relationship, and prefer composition otherwise.
4. Use **realisation** to separate what a class promises from how it does it.
5. Show **dependencies** only when they illustrate an important point, since they are numerous.

<!--
IMAGE PROMPT  ->  generate as images/02_relationship_notations.png   (16:9 explanatory diagram, place here)

A reference sheet with six rows. Each row shows two small boxes joined by one relationship line style with its name and a one-line meaning: Association, Aggregation, Composition, Generalisation, Realisation, Dependency. Examples use Customer, Order, Order Item, Payment.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Pick the Relationship

1. A Customer places Orders.
2. If a Playlist is deleted, its Entries disappear too.
3. A Square is a kind of Shape.
4. A Report Generator receives an Order as a parameter to a method and does not keep it.

Item 1 is an association. Item 2 is composition, since the entries belong to the playlist and share its lifetime. Item 3 is generalisation. Item 4 is a dependency.

## Conclusion

The relationships in a class diagram, association, aggregation, composition, generalisation, realisation, and dependency, describe respectively how objects are linked, how a whole is made of parts with or without shared lifetime, how one class specialises another, how a class fulfils an interface, and how one class relies on another. Choosing precisely expresses design intent and exposes coupling.

Structure shows what exists, but not how objects work together over time. The next chapter turns to behaviour, beginning with sequence diagrams.
