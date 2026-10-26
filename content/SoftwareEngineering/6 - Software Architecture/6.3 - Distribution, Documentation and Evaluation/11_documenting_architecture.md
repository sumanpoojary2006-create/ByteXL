## Introduction

An architecture that exists only in the heads of a few people is fragile. New team members cannot learn it, other teams cannot work with it, reviewers cannot challenge it, and the reasons for decisions are forgotten. Documentation solves these problems, but only when it is useful: a long document that nobody reads or updates is worse than none, because it misleads. Good architectural documentation is purposeful, focused on the needs of its readers, and kept close to the work.

**Definition:** Documenting architecture is the practice of recording the structure of a system, the significant decisions behind it, and their rationale, using views suited to different stakeholders, so that the architecture can be understood, communicated, reviewed, and evolved.

<!--
IMAGE PROMPT  ->  generate as images/11_intro_documenting_architecture.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A set of different transparent lenses placed over the same system sketch, each revealing a different view: structure, runtime flow, deployment, with a small decision record card beside them.

ON-IMAGE TEXT: show a short bold title "Documenting Architecture" plus only these few labels, large and legible: Views, Decisions, Readers. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Purposes of Architectural Documentation

- **Communication** to developers, testers, operators, managers, and customers
- **Learning and onboarding** of new team members
- **Analysis and review** of qualities such as performance and security
- **Coordination** among teams building different parts
- **Memory** of why decisions were made
- **Compliance** with regulation or contract where required

Start by asking who the readers are and what questions they need answered. Different readers need different documents.

## Views

A system is too rich for one diagram. Documentation therefore uses several **views**, each showing a particular aspect for a particular audience. This follows the ISO/IEC/IEEE 42010 standard, which relates **stakeholders**, their **concerns**, and **viewpoints** that define how to build a view addressing those concerns.

Philippe Kruchten proposed the influential **4+1 view model**.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">View</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Shows</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Audience</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Logical</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The main abstractions and their relationships; the functionality the system provides</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Designers and analysts</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Process</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Runtime behaviour: processes, concurrency, communication</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Integrators, performance engineers</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Development</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How the software is organised into modules and packages for building</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Developers, managers</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Physical</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How software is deployed to hardware and networks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operations and infrastructure engineers</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scenarios (the +1)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Key use cases that tie the four views together and validate them</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Everyone</td>
    </tr>
  </tbody>
</table>

Paul Clements and colleagues group views into three families.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Family</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Shows</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Module views</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How code is organised and what depends on what</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Layers, packages, dependency diagrams</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Component and connector views</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How the system works at run time: components and their interactions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Service diagrams, data flow</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Allocation views</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How software maps onto things in its environment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deployment, team assignments, build structure</td>
    </tr>
  </tbody>
</table>

## A Practical Set of Diagrams

Many teams find a small set sufficient: the **C4 model** from Unit 4 provides a context diagram, a container diagram, and, for complex parts, component diagrams. To these are added a **deployment view** and a few **dynamic views** showing how key scenarios flow through the system.

Good diagrams follow simple rules.

- Give each diagram a **title** and say what it shows.
- Use a **legend** that explains shapes, colours, and line styles.
- Label every element and every arrow, including **what the arrow means**.
- Keep **one level of abstraction** per diagram.
- Avoid overcrowding, and split large diagrams.

## Recording Decisions

Diagrams show what the architecture is, but not why. The most useful complementary record is the **architecture decision record (ADR)**, a short document for each significant decision, described by Michael Nygard in 2011.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Section</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Content</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Title</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A short name for the decision</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use a message queue between ordering and kitchen</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Status</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Proposed, accepted, superseded, or deprecated</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Accepted</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Context</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The forces at play: requirements, constraints, qualities</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Kitchen systems are slow and occasionally offline; ordering must stay available at lunch</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Decision</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What was decided, stated plainly</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Order events will be sent through a queue</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Consequences</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What becomes easier and harder, including costs and risks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ordering no longer waits for the kitchen; order status becomes eventually consistent; the queue must be monitored</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Alternatives considered</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Options rejected, with reasons</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Direct call (rejected: couples availability); shared database (rejected: coupling of data)</td>
    </tr>
  </tbody>
</table>

ADRs are short, stored with the code, numbered, and never edited to hide history. When a decision changes, a new record supersedes the old one, leaving a trail of reasoning.

## Keeping Documentation Alive

The main risk is that documents become out of date. Practices that help:

- **Keep it small and valuable.** Document what is hard to see from the code, not what is obvious.
- **Store it with the code,** in the same repository, so that it changes in the same review.
- **Generate** diagrams or reference material from code or configuration where possible.
- **Assign owners** and review documents when the architecture changes.
- **Make it easy to find,** with a clear structure and an index.
- **Treat it as a product:** ask readers whether it helps.

A structured template, such as the one provided by the arc42 approach, offers a checklist of sections: goals and constraints, context, solution strategy, building blocks, runtime, deployment, cross-cutting concepts, decisions, quality requirements, risks, and glossary. Teams adapt it to include only what they need.

## Documentation in Agile Teams

Agile values working software over comprehensive documentation, not over all documentation. Lightweight architecture documentation, a few clear diagrams, a short overview, and decision records, supports collaboration and is consistent with agile principles.

<!--
IMAGE PROMPT  ->  generate as images/02_four_plus_one_views_and_adr.png   (16:9 explanatory diagram, place here)

Left: the 4+1 model drawn as four views (Logical, Process, Development, Physical) around a central Scenarios circle. Right: an ADR card with the headings Title, Status, Context, Decision, Consequences, Alternatives, filled with a short example.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Which Document?

1. An operations engineer wants to know which servers each component runs on.
2. A new developer asks why the ordering and kitchen systems communicate through a queue.
3. A team lead wants to show non-technical stakeholders how the system fits with the outside world.

Question 1 is answered by the deployment (physical) view. Question 2 is answered by the architecture decision record for that choice. Question 3 is answered by a system context diagram.

## Conclusion

Documenting architecture is the practice of recording the structure of a system, the significant decisions behind it, and their rationale, using views suited to different stakeholders, so that the architecture can be understood, communicated, reviewed, and evolved. A few accurate, well-maintained artifacts beat a large, stale document.

Once an architecture is documented, it can be judged. The final topic of this unit describes how to evaluate architectural trade-offs.
