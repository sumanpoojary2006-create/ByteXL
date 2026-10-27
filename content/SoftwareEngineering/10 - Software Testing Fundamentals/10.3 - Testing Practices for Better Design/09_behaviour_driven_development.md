## Introduction

Many failures in software come not from coding mistakes but from misunderstandings: the business meant one thing, the developers built another, and the testers checked a third. Behaviour-driven development, or BDD, targets this gap. It extends the ideas of test-driven development to the conversation between business people, developers, and testers, by describing the expected behaviour of the system in concrete examples written in plain language that everyone can read, and that can also be run as automated tests.

**Definition:** Behaviour-driven development (BDD) is a collaborative approach in which a team specifies the expected behaviour of a system through concrete examples written in a shared, structured natural language, typically Given-When-Then, which serve at once as requirements, acceptance tests, and living documentation.

<!--
IMAGE PROMPT  ->  generate as images/09_intro_behaviour_driven_development.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Three figures labelled Business, Developer, Tester around a table discussing a card with Given, When, Then lines, an arrow from the card to an automated check turning green, and a document labelled Living documentation.

ON-IMAGE TEXT: show a short bold title "Behaviour-Driven Development" plus only these few labels, large and legible: Talk, Examples, Automate. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Origins

Dan North developed BDD between about 2003 and 2006 while teaching test-driven development and finding that the word "test" confused people. He proposed focusing on **behaviour**: what the system should do, described in the language of the business. His article "Introducing BDD" set out the ideas. The related practice of **specification by example**, described by Gojko Adzic, and **acceptance test-driven development** share the same core: use concrete examples to build shared understanding.

## The Core Ideas

1. **Discover through conversation.** The team talks through each story using real examples before building it, to expose misunderstandings and missing cases.
2. **Formulate examples** in a structured, readable form.
3. **Automate** the examples as executable checks.
4. **Keep them as living documentation** of what the system does, always accurate because they run against the code.

## The Three Amigos

A key practice is a short meeting, often called the **three amigos**, before work begins on a story. It brings together three perspectives:

- **Business** (product owner or analyst): what is needed and why.
- **Development:** how it might be built and what is feasible.
- **Testing:** what could go wrong and what cases are missing.

Together they walk through the story, ask questions, and write examples. Many misunderstandings are discovered here, where correcting them costs a few minutes, instead of after the code is built.

## Given-When-Then

The standard format for an example is a **scenario** with three kinds of step.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Keyword</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Given</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The starting context</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Given a customer has a basket with ten items</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">When</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The event or action</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">When the customer places the order</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Then</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The expected outcome</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Then a ten percent discount is applied to the total</td>
    </tr>
  </tbody>
</table>

"And" and "But" extend a section. A complete scenario in words reads:

- Given a registered customer with ten dishes in the basket,
- when they place the order,
- then the total shows a ten percent discount, and a confirmation is displayed.

This is the same arrange-act-assert shape as a unit test, at the level of business behaviour. A group of scenarios for one capability is a **feature**, headed by a short statement of its purpose, often using the user story form.

## Gherkin and Tools

The structured language used in many tools is **Gherkin**, which has simple keywords, and plain-text feature files that anyone can read. Tools such as **Cucumber** and its relatives in many languages, including Behave and SpecFlow, read the feature files and connect each step to code, called a **step definition**, that performs the action or check against the system. The examples then run in the pipeline like any other test. This is optional: the value of BDD lies mostly in the conversation and the examples, and they can be used without automation tools.

## Declarative and Imperative Scenarios

A frequent mistake is to write scenarios as lists of user interface actions: click here, type this, press that. These are **imperative**, brittle, and unreadable to the business. Better scenarios are **declarative**: they state **what** is true or what the user wants to achieve, and leave the detail to the step definitions.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Style</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem or benefit</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Imperative (poor)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Given I open the login page, and I type a name into the first box, and I type a password into the second box, and I click the button</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Breaks when the interface changes; hides the intent</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Declarative (good)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Given a registered customer who is logged in</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Short, stable, and says what matters</td>
    </tr>
  </tbody>
</table>

## Benefits

- **Shared understanding** between roles, reducing rework from misunderstanding.
- **Requirements that are testable** by construction.
- **Living documentation** that cannot drift away from the system, since failing examples signal change.
- **A clear definition of done** for a story.
- **A common language** based on the domain, in the spirit of the ubiquitous language of Unit 4.
- **Focus on value:** scenarios start with the behaviour users want.
- **Early discovery** of gaps, edge cases, and conflicting rules.

## Pitfalls

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Pitfall</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Explanation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Remedy</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Treating BDD as a test tool only</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Teams adopt the tool but skip the conversations, so the benefit is lost</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hold the three amigos discussions; write examples collaboratively</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Developers write all the scenarios alone</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The business does not own or understand them</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Involve business people throughout</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scenarios too detailed or interface-driven</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Brittle and unreadable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Write declarative scenarios about behaviour</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Too many scenarios</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Slow and costly to maintain</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep the key examples; cover detail with unit tests</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Duplicating the lower levels of the pyramid</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Slow suite</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use BDD for business rules and key journeys; keep detailed logic in unit tests</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Poorly maintained feature files</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Documentation decays</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Treat them as code: review and refactor</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ambiguous language</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Different people read different meanings</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Agree a glossary and reuse standard phrases</td>
    </tr>
  </tbody>
</table>

## BDD and the Test Pyramid

BDD scenarios usually run at the **service or system level** and so occupy the middle and upper layers of the pyramid. They should therefore express **important business behaviours** and not every case. Detailed edge cases belong in unit tests. A common good division is: a few BDD scenarios for each business rule and the main journeys, with many fast unit tests beneath them.

## Relation to Requirements

BDD scenarios are closely related to the acceptance criteria of Unit 3. In many teams, the Given-When-Then examples **are** the acceptance criteria for each user story, written during refinement, then automated, and then kept as documentation. The user story gives the purpose, the scenarios give the precise conditions of acceptance.

<!--
IMAGE PROMPT  ->  generate as images/02_three_amigos_and_gherkin_scenario.png   (16:9 explanatory diagram, place here)

Left: three amigos (Business, Developer, Tester) discussing a story. Right: a feature card with the heading Feature: Bulk discount and a scenario with Given, When, Then lines in plain language, an arrow to step definitions and then an automated pipeline check marked green. A contrast panel shows a poor imperative scenario crossed out.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Improve the Scenario

1. A scenario reads: click the menu, click the third item, type 2 in the box, click add, click the basket icon. What is wrong, and how would you rewrite it?
2. When in the process should the three amigos meet?
3. A team uses a BDD tool but business people never read the scenarios. What has been lost?

The scenario is imperative and tied to the interface; a declarative version would say: given a customer with two portions of a dish in the basket, when they view the basket, then the basket shows two portions and the correct total. The three amigos should meet **before** development of a story begins. In case 3, the team has lost the shared understanding and living documentation that are the main benefits; the tool is only a test runner.

## Conclusion

Behaviour-driven development (BDD) is a collaborative approach in which a team specifies the expected behaviour of a system through concrete examples written in a shared, structured natural language, typically Given-When-Then, which serve at once as requirements, acceptance tests, and living documentation. Its value is in the conversation that precedes the code.

With unit-level practices covered, the next chapter turns to testing at higher levels, starting with how parts of a system are checked together: integration and system testing.
