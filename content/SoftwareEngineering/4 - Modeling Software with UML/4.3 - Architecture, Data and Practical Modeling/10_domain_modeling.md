## Introduction

Before deciding how software will be structured, a team must understand the world it serves. What are the important concepts, what do the words mean, and how do the concepts relate? A domain model captures this understanding. It is not a design for software but a description of the problem area, written so that developers and domain experts share one picture. Errors at this stage are among the most expensive, because a design built on the wrong concepts cannot be repaired by clever coding.

**Definition:** A domain model is a description of the concepts of a problem area, their attributes, and their relationships, expressed in the vocabulary of the people who work in that area, and it serves as the foundation for the design of the software.

<!--
IMAGE PROMPT  ->  generate as images/10_intro_domain_modeling.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A glossary-like cloud of business terms on the left being organised into a simple diagram of labelled boxes and lines on the right, with a domain expert and a developer figure pointing at it together.

ON-IMAGE TEXT: show a short bold title "Domain Modeling" plus only these few labels, large and legible: Concepts, Words, Shared. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## What a Domain Model Contains

- **Conceptual classes (concepts)** that matter in the domain: Customer, Order, Dish, Menu, Payment.
- **Attributes**: the important facts about each concept, such as the date of an order.
- **Associations**: how concepts relate, such as a Customer places Orders.
- **Business rules and constraints**: an order needs at least one item, and a dish has one price at a time.

A domain model is usually drawn as a simplified UML class diagram with no operations and few attributes. Its purpose is understanding, so it uses business words.

## Domain Model and Software Design

The classes in a domain model are **conceptual**, not necessarily software classes. A model of a library might include Member, Book, and Loan, because those matter to librarians. The software design will add technical classes with no counterpart in the domain, such as database connections or screens. But the domain model strongly influences the main classes of the design, which keeps the software aligned with how the business thinks. This alignment reduces the gap between the language of experts and the structure of the code.

## Ubiquitous Language

Eric Evans, in the approach known as domain-driven design, stresses a **ubiquitous language**: a shared vocabulary used by everyone, in conversation, documents, and code. If experts say "booking" but developers say "reservation," confusion follows. Settling on the same terms, defining them precisely in a glossary, and using them in names across code and diagrams, removes a common source of misunderstanding. Domain modeling is the main tool for building that language.

## Building a Domain Model

A practical sequence is:

1. **Gather material**: requirements, use cases, user stories, documents, conversations with experts.
2. **Identify candidate concepts** by looking for the important nouns and noun phrases.
3. **Filter them.** Discard duplicates, vague terms, things outside scope, and items that are really attributes or actions.
4. **Define each concept** in the glossary in the experts' words.
5. **Identify relationships** and record multiplicities.
6. **Add key attributes**, only those that matter to understanding.
7. **Identify rules** and record them as notes or constraints.
8. **Review with domain experts**, correcting misunderstandings, and iterate.

## Common Traps

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Trap</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Remedy</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Modeling the software, not the domain</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Including screens, tables, and technical classes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep to real-world concepts</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Too much detail</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every attribute of every concept</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Include only what aids understanding</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Attributes as classes, or the reverse</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Treating a simple value as a class, or a real concept as a field</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ask whether the system must track it as a thing with its own identity</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Action classes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Classes named for actions, such as Process Payment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Make them operations, or find the underlying concept, such as Payment</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Different words for the same thing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Several terms in use</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fix a single term in the glossary</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No expert review</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Developers guess the domain</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Review with those who know it</td>
    </tr>
  </tbody>
</table>

## Domain Models Evolve

Understanding of a domain deepens as a project proceeds, so the model changes. A team that models in short iterations, tests the model against real scenarios, and revises it, ends with a model that reflects reality better than one drawn once at the start.

<!--
IMAGE PROMPT  ->  generate as images/02_domain_model_meal_ordering.png   (16:9 explanatory diagram, place here)

A simple domain model with boxes Customer, Order, Order Line, Dish, Menu, Payment connected by labelled associations with multiplicities, next to a small glossary card defining Order as a customer request for one or more dishes. No operations are listed.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Filter the Candidates

From the sentence "A customer places an order for dishes and pays by card; the kitchen prepares the order," a student lists: customer, order, dish, card, pays, kitchen, prepares.

1. Which are likely concepts?
2. Which are actions that should not be classes?
3. Which might be attributes or deserve a closer look?

Customer, order, and dish are clear concepts. "Pays" and "prepares" are actions, which become operations or are captured by concepts such as Payment. "Card" might be a type of payment method, an attribute of Payment, or a concept of its own, depending on whether the system must track cards. "Kitchen" could be an actor or a department concept, depending on scope.

## Conclusion

A domain model is a description of the concepts of a problem area, their attributes, and their relationships, expressed in the vocabulary of the people who work in that area, and it serves as the foundation for the design of the software. A shared language and a validated model prevent errors that no later technique can fully repair.

Teams need models that are useful but light. The final topic of the unit describes how to model just enough, using lightweight sketching and the C4 model.
