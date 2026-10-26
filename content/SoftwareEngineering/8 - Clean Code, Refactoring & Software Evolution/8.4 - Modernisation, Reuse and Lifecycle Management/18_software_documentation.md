## Introduction

Software is delivered with more than code. People need to know how to install it, how to use it, how it is built, why it was built that way, and how to run and repair it. The knowledge held in the heads of the original team disappears when they move on. Documentation is the means of making that knowledge durable. Yet it is also a common source of waste: documents that are never read, never updated, and misleading. Good documentation is deliberate, aimed at a reader, and kept in step with the software.

**Definition:** Software documentation is the collection of written and visual material that explains a software system to the people who use, build, operate, and maintain it, and good documentation is accurate, current, findable, and written for a specific reader with a specific purpose.

<!--
IMAGE PROMPT  ->  generate as images/18_intro_software_documentation.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A library shelf with four coloured sections labelled Tutorials, How-to guides, Reference, Explanation, and readers of different kinds, a user, a developer, an operator, each pulling the right book from the right section.

ON-IMAGE TEXT: show a short bold title "Software Documentation" plus only these few labels, large and legible: Reader, Purpose, Current. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Kinds of Documentation

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Kind</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Audience</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Content</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">User documentation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">End users</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How to use the product</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Getting started guides, tutorials, help pages, frequently asked questions</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requirements and specifications</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stakeholders, testers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What the system must do</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requirements specification, user stories, acceptance criteria</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Architecture and design documentation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Developers, architects</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Structure, decisions, and rationale</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Architecture overview, diagrams, decision records</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">API (interface) reference</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Developers using the interface</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operations, inputs, outputs, errors, examples</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reference pages, interface specifications</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Code documentation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Developers maintaining the code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Intent, constraints, reasons for decisions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Comments, README files in each part</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operations documentation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operators, support</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How to install, configure, monitor, and recover</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Runbooks, deployment guides, incident procedures</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Developer onboarding</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">New team members</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How to set up, build, test, and contribute</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">README, contributing guide, setup guide</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Release documentation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Users, operators</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What changed in each version</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Release notes, changelog, upgrade guides</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test documentation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Testers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Strategy, plans, results</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test plans and reports</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Process and policy documents</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The team</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How the team works</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Coding standards, review rules, security policy</td>
    </tr>
  </tbody>
</table>

## A Framework for Technical Documentation

Daniele Procida proposed a model, known as Diátaxis, which observes that documentation serves four different needs, and that mixing them makes documents confusing.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Type</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Reader need</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Style</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tutorial</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">I am learning</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Take a beginner through a guided experience to a first success</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A lesson: step by step, safe, with a clear result</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How-to guide</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">I want to achieve a particular goal</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Show how to solve a specific problem</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A recipe: steps for a competent user</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reference</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">I need precise facts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Describe the system accurately and completely</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A dictionary: structured, neutral, accurate</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Explanation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">I want to understand</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Discuss concepts, background, and reasons</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An essay: context and trade-offs</td>
    </tr>
  </tbody>
</table>

Writing each type with its purpose in mind makes documentation easier to write and to use.

## The Essential README

Every project should have a short document at its top level that answers basic questions:

- What is this, and what problem does it solve?
- How do I install or run it?
- How do I use it, with a short example?
- How do I run the tests and contribute?
- Where is more documentation, and who owns it?
- What is the licence?

For many projects, a good README is the single most valuable piece of documentation.

## Principles of Good Documentation

1. **Know the reader** and what they need to do.
2. **Be accurate.** Wrong documentation is worse than none.
3. **Keep it current.** Make updating it part of the work.
4. **Be concise.** Say what is needed; omit what can be seen in the code.
5. **Explain why,** since the reasons are what the code cannot show.
6. **Use examples,** which often communicate better than description.
7. **Organise it** so it can be found: clear structure, headings, search, and links.
8. **Keep one source of truth,** and link instead of copying.
9. **Use plain language,** consistent terms, and a glossary.
10. **Use visuals** where they clarify, such as diagrams with labels and a legend.

## Keeping Documentation Alive

The greatest threat is staleness. Practices that help:

- **Docs as code:** store documentation in the same repository as the software, in simple text formats, review it with the same process, and change it in the same commit as the code.
- **Include documentation in the Definition of Done:** a change is not complete until the affected documents are updated.
- **Generate** reference material from code and annotations, and diagrams from the system, where possible.
- **Test documentation:** check that examples run, and that links work, automatically.
- **Assign owners** and review on a schedule.
- **Remove or archive** what is obsolete.
- **Collect feedback** from readers, and track which pages are used.
- **Make contribution easy,** so anyone who finds an error can fix it.

## Living Documentation and Self-Documentation

The best documentation is often the system itself: readable code, descriptive names, automated tests that serve as examples, and clear error messages. Living documentation is produced or checked automatically from the system, so it cannot drift. Written documents are then reserved for what the system cannot say: purpose, context, decisions, and how to operate it.

## Documentation Debt

Missing and outdated documentation is a form of technical debt with a clear cost: time wasted rediscovering things, errors from misunderstanding, slow onboarding, and dependence on individuals. It should be recorded and repaid like other debt, concentrating on the documents that are most used and most costly to lack.

## In Agile Settings

The Agile Manifesto values working software over comprehensive documentation, which does not mean no documentation. Agile teams document what is needed, close to when it is needed, and keep it light, while regulated or safety-related domains still require formal documents.

<!--
IMAGE PROMPT  ->  generate as images/02_diataxis_four_quadrants.png   (16:9 explanatory diagram, place here)

A two-by-two grid with axes Learning versus Working and Practical versus Theoretical. Quadrants: Tutorials (learning, practical), How-to guides (working, practical), Reference (working, theoretical), Explanation (learning, theoretical). Each has a short descriptor and a small icon.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Which Type of Document?

1. A page that walks a new user through building their first order, step by step.
2. A page listing every operation of an interface with its inputs, outputs, and errors.
3. A page that explains why the system uses a message queue between ordering and kitchen.
4. A page describing exactly how to restore the database from a backup.

Document 1 is a tutorial. Document 2 is reference. Document 3 is explanation, and may be an architecture decision record. Document 4 is a how-to guide, in an operations runbook.

## Conclusion

Software documentation is the collection of written and visual material that explains a software system to the people who use, build, operate, and maintain it, and good documentation is accurate, current, findable, and written for a specific reader with a specific purpose. Keeping it close to the code and part of the normal workflow is the best way to keep it true.

Documentation is one part of keeping a changing system under control. The next topic covers the broader disciplines of configuration management and release management.
