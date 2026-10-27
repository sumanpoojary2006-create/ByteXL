## Introduction

Earlier units each examined one part of software engineering: requirements, modelling, design, architecture, coding practice, version control and delivery, testing, quality, data, project management, security, and ethics. Real products are not built one unit at a time. The skill of an engineer shows in combining these into a single flow, from an idea to a working product in the hands of users, within a team, under constraints of time and resources. A capstone is a project in which a team does exactly that, and reflects on how it went. This topic guides such a project and, along the way, ties together the course.

It describes what a complete delivery involves, a recommended sequence of stages with the units that support each, the team's working agreements, what to produce at each stage, how to prepare the demonstration, how to run a retrospective, and how work is commonly assessed. It contains no code: it is a plan of the engineering work, to be carried out with the tools and language of your choice.

**Definition:** A capstone software project is an integrated, team-based exercise in which students carry a complete product from requirements through design, construction, verification, release, and reflection, applying the practices of the whole course, and demonstrating both the product and the engineering process that produced it.

<!--
IMAGE PROMPT  ->  generate as images/20_intro_capstone_delivering_a_complete_software_product.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A horizontal journey line from a lightbulb labelled Idea through stations Requirements, Design, Build, Test, Release to a small group of users labelled Value, with a loop arrow below labelled Retrospective.

ON-IMAGE TEXT: show a short bold title "Capstone: Delivering a Complete Software Product" plus only these few labels, large and legible: From Idea to Users. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## What "Complete" Means

A product is complete not when the code is written but when it is delivered usefully and responsibly. A complete delivery includes:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Dimension</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Evidence of completeness</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Purpose</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A clear problem statement, users, and goals; agreed scope and non-goals (Units 1, 3, 13)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prioritised, testable functional and non-functional requirements (Unit 3)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Models, architecture and design decisions with reasons (Units 4 to 7)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Implementation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Readable, reviewed, version-controlled code that follows team standards (Units 8, 9)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Verification</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automated and manual tests at several levels, with results (Units 10, 11)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A sensible approach to storing and exposing data and interfaces (Unit 12)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security and privacy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A threat model, safe handling of data and secrets, and privacy-aware choices (Unit 14)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Accessibility and inclusion</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Usable by people with a range of abilities (Unit 14)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Delivery and operation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A repeatable build and deployment, configuration, monitoring, and a recovery plan (Unit 9)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Documentation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">README, user guidance, and design documents (Unit 14)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Project management</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A plan, estimates, risk register, tracking, and stakeholder communication (Unit 13)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Professional practice</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Licence choices, ethical consideration, teamwork, and an honest reflection (Unit 14)</td>
    </tr>
  </tbody>
</table>

## Choosing a Project

A good capstone project is:

- **real enough** to have users and trade-offs, such as an ordering platform for a small restaurant, a booking tool for a community clinic, a learning tracker for a school, an inventory tool for a charity, or a tool used by your own department;
- **small enough** to finish in the available time with working software at each stage (a core of a few essential features, not dozens);
- **rich enough** to need several engineering concerns: some data, more than one user role, an interface, an integration with another service, and non-trivial rules;
- **free of unnecessary risk:** avoid domains where failure could hurt people (medical, safety-critical) unless the scope is a safe simulation;
- **owned by a real or realistic stakeholder** who can give feedback.

Write a one-page **project charter:** the problem, the users, the goals and measurable outcomes, the scope and non-goals, the team and roles, the constraints (time, resources, technology), the main risks, and how success will be judged.

## Organising the Team

- **Roles:** agree who plays product owner (priorities and acceptance), delivery lead or facilitator, technical lead, quality lead, and security and privacy champion. In a small team, people hold more than one role; every responsibility must have an owner (Unit 13).
- **Working agreements:** meeting times and channels, communication norms, decision rules, definition of done, code review rules, branching strategy, and how conflict will be handled (Units 2, 9, 11).
- **Tools:** a shared repository with protected main branch, an issue tracker with a board, a continuous integration pipeline, a place for documents, and a chat channel (Unit 9).
- **Process:** an agile framework with short iterations (for example, one or two weeks), planning, daily check-ins, reviews with the stakeholder, and retrospectives (Unit 2).

## The Journey: Stages and Deliverables

The stages overlap and repeat; the order below is the logical flow. Each stage draws on units of the course.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Stage</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Activities</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Deliverables</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Supporting units</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1. Discover and define</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Interview stakeholders; identify users and their needs; study similar products; define scope, goals, and measures of success; write the project charter</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Charter; stakeholder list; initial problem statement</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1, 3, 13</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2. Specify</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Write user stories with acceptance criteria and use cases; capture non-functional requirements (performance, security, accessibility, privacy); prioritise with a method such as MoSCoW; build the first backlog</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prioritised backlog; requirements document or equivalent; definition of done</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2, 3, 14</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">3. Plan</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Break down the work; estimate with ranges; plan the first iterations and a rough release plan; identify risks and responses; agree on communication with stakeholders</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Release plan; estimates; risk register; communication plan</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">13</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">4. Design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Model the domain, data, and key behaviours; choose an architecture with reasons against the main quality attributes; define interfaces; threat-model the system; plan accessibility and privacy; record decisions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Models; architecture description; decision records; threat model; API outline</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">4, 5, 6, 7, 12, 14</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">5. Set up the delivery system</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Create the repository, branching rules, automated build and test pipeline, environments, and configuration and secrets management</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Working pipeline running from day one; environment descriptions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9, 14</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">6. Build in iterations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deliver thin vertical slices of value each iteration; write tests alongside code; review each change; refactor continuously; manage technical debt; integrate daily</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Working increments; reviewed code; test results</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2, 7, 8, 9, 10, 11</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">7. Verify</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test at unit, integration, and system levels; test non-functional qualities; exploratory and accessibility testing; security scanning and review; track and fix defects; run acceptance with the stakeholder</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test report; defect log; security findings and fixes; accessibility check</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">10, 11, 14</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8. Release</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prepare a release candidate; tag a version; write release notes; deploy using a safe strategy with a rollback plan; set up monitoring and alerts; prepare operating instructions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deployed product; release notes; runbook; monitoring</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9. Operate and learn</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Observe use; gather feedback and metrics; fix issues; decide what comes next based on evidence</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Feedback summary; metrics; updated backlog</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9, 13</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">10. Reflect and present</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Demonstrate the product; present design decisions and trade-offs; run a retrospective; assess your own contribution; archive the project</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Demo; presentation; retrospective report; final documentation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2, 14</td>
    </tr>
  </tbody>
</table>

### Advice for Each Stage

**Discover and specify.** Spend real time with stakeholders, not guessing. Write acceptance criteria that can be tested. Make non-goals explicit; scope will grow unless you protect it. Ask what outcome matters, not only what features are wanted (Unit 13, product thinking).

**Plan.** Estimate honestly and in ranges. Do the riskiest and most uncertain work first (Unit 13). Keep a buffer, because something will go wrong.

**Design.** Keep it as simple as will work: a well-structured single deployable unit is usually right for a capstone (Unit 6). Draw a few useful diagrams, not many. Write down the three or four decisions that matter most, with the alternatives. Do a short threat model: what are the assets, the trust boundaries, and the top threats (Unit 14)?

**Set up delivery first.** A pipeline that builds, tests, and deploys a trivial "hello" version in the first week removes most late surprises about environments. Protect the main branch; require review and passing checks.

**Build in slices.** Deliver something users could use at the end of each iteration, however small. Do not build all of one layer before another. Keep the main line always working.

**Verify throughout.** Test as you build; do not leave testing for a final phase. Include tests for the non-functional requirements you promised and for the security behaviours you designed.

**Release deliberately.** Treat release as a first-class activity with a checklist: tests green, security issues triaged, configuration and secrets checked, documentation updated, rollback tried.

**Reflect honestly.** The aim is learning, including from what did not work.

## Quality Gates and Evidence

At the end of each iteration and before release, the team should be able to show:

- stories meet the definition of done and the acceptance criteria;
- automated tests pass; known defects are triaged with owners;
- code is reviewed and meets standards; technical debt is recorded;
- security and privacy requirements are met, dependencies are checked, and no secrets are in the repository;
- accessibility checks were performed;
- documentation is current;
- the product can be built and deployed from scratch by someone else, using the instructions;
- risks and issues are tracked with decisions.

Keep this evidence (reports, pull requests, test output, decision records). It is the basis for assessment and for your portfolio (previous topic).

## Managing Common Problems

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical response</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scope growth</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Return to the charter and backlog priorities; trade new items for old; talk to the stakeholder</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A team member is unavailable or not contributing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Raise early and kindly; clarify expectations; redistribute work; involve the supervisor if needed</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Technical dead end</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Time-box exploration; ask for help; consider an alternative or a simpler design; record the lesson</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Behind schedule</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reduce scope to the most valuable features; do not cut testing or security; communicate early (Unit 13)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Integration surprises late</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Integrate daily; deploy early; test the whole system each iteration</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Disagreement about design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Write down options and criteria; test with a spike; decide and record; disagree and commit</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defects accumulating</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stop adding features; fix and strengthen tests; refactor (Unit 8)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Over-reliance on AI tools</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Understand and review everything committed; keep authorship honest; follow course rules (previous topics)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stress and burnout</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Plan realistic workloads; share load; protect rest</td>
    </tr>
  </tbody>
</table>

## The Demonstration

The demo shows value to the stakeholder; it is not a tour of the code.

1. **Open with the problem and the users,** briefly.
2. **Show the product doing real tasks** end to end, as a user would, with realistic data. Rehearse the path and prepare for failure with a recorded fallback.
3. **Highlight key quality attributes:** how it handles errors, how it protects data, how it works for users with different needs.
4. **Explain the engineering behind it briefly:** the architecture, key decisions and trade-offs, how it is tested and delivered, the security and privacy approach.
5. **Be honest about limitations,** known issues, and what you would do next.
6. **Invite feedback and questions;** take notes.

Prepare a short **presentation** (a few slides), a **live deployed instance,** and a **final report** or repository documentation that others can follow.

## The Retrospective

At the end (and at the end of each iteration), the team examines its own process (Unit 2).

1. **Set the stage:** purpose, safety, and ground rules (blameless).
2. **Gather data:** a timeline of the project; metrics such as planned versus delivered scope, defects, lead times, and the estimates against actuals (Unit 13).
3. **Generate insight:** What went well? What did not? Why? Use simple formats such as start, stop, continue, or "what to keep, drop, and try".
4. **Decide actions:** a few specific changes, with owners.
5. **Close:** appreciation of the team.

Individually, write a short **reflection:** your contribution, what you learned technically and professionally, what you would do differently, and how you will continue to grow (previous topic). Link each claim to evidence.

## How Capstones Are Commonly Assessed

Criteria vary by institution, but typically include:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Area</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What is looked for</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Product</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Meets the agreed goals; works reliably; is usable and accessible</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requirements and design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sensible, traceable, with reasoned decisions and trade-offs</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Code and process</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clean, reviewed, version-controlled work; effective use of branches and a pipeline</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Testing and quality</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sound strategy, meaningful tests, evidence of fixes</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security, privacy, and ethics</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A threat model, secure handling of data, awareness of impacts</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Project management</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Plan, tracking, risk management, and adaptation</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Teamwork</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fair contribution, communication, and handling of difficulties (often from peer and supervisor input)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Documentation and communication</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clear writing, a good demo, and honest reflection</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Learning</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Evidence of growth and insight</td>
    </tr>
  </tbody>
</table>

Individual contribution is usually assessed through repository history, review records, task ownership, and viewpoints of teammates, so keep a record of your work and credit others fairly.

## After the Capstone

Treat the project as the first item of your portfolio: tidy the repository, write a clear README with screenshots, the goals and architecture summary, setup instructions, and licence (Unit 14), and add a short write-up of design decisions and lessons. Preserve secrets-free configuration, and consider continuing the project or contributing what you built to open source. Most importantly, keep applying the habits you practised: understand the problem before building, work in small steps, test, review, deliver continuously, communicate clearly, protect the people who use your software, and learn from every outcome.

## Course Summary: The Threads That Run Through Everything

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Thread</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Idea</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Where it appears</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Software engineering is about change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Software must be understandable and affordable to change throughout a long life</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Units 1, 5, 7, 8, 9</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Think before you build</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Understand the problem, the users, and the constraints</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Units 1, 3, 4, 13</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Manage complexity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Abstraction, modularity, cohesion, coupling, and architecture</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Units 5, 6, 7</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality is built in and verified</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reviews, tests, analysis, and metrics at every stage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Units 8, 10, 11</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deliver continuously and safely</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Version control, automation, and learning from operations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unit 9</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Manage uncertainty</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Estimates as ranges, risks, feedback, and iteration</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Units 2, 13</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Protect people</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security, privacy, safety, accessibility, and fairness</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Units 11, 14</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Work as a profession</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Communication, teamwork, ethics, and lifelong learning</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Units 13, 14</td>
    </tr>
  </tbody>
</table>

<!--
IMAGE PROMPT  ->  generate as images/20_capstone_journey_and_threads.png   (16:9 explanatory diagram, place here)

A winding road drawn in ten numbered stages from Discover to Reflect, with a loop arrow from Operate and learn back to Specify; beneath the road eight coloured threads (Change, Understand, Complexity, Quality, Delivery, Uncertainty, People, Profession) run in parallel under the whole length.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Plan Your Capstone

1. Write a one-sentence problem statement, the main user, and two measurable goals for a capstone project of your choice.
2. List three risks your team is likely to face and a response for each.
3. Decide what belongs in the first iteration so that it delivers a usable slice, however small.

There is no single correct answer. A good response to case 1 names a real user and a real problem, and goals that can be measured (for example, a customer places an order in under two minutes; ninety per cent of test users complete it without help). For case 2, typical risks are unclear requirements, uneven contribution, and an unfamiliar technology; responses include early stakeholder feedback, explicit roles and tracking, and an early technical spike. For case 3, a thin end-to-end path through every layer that a user can run, such as sign in, choose an item, and place an order, with the pipeline already deploying it.

## Conclusion

A capstone software project is an integrated, team-based exercise in which students carry a complete product from requirements through design, construction, verification, release, and reflection, applying the practices of the whole course, and demonstrating both the product and the engineering process that produced it. Delivering something real, in small steps, with the discipline of testing, review, security, and honest communication, is the clearest demonstration of what software engineering means.

This completes the course. The skills you have met here, from understanding people's needs to protecting them, are the foundations of a long career in building software that is worth trusting.
