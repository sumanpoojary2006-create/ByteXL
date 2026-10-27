## Introduction

Software is built by teams, maintained by people who were not there at the start, and paid for by people who do not read code. In all three cases, the ideas must travel through language. A design that exists only in one engineer's head cannot be reviewed, criticised, extended, or handed over; a decision whose reasons were never written down is repeatedly reopened; and a proposal that the reader cannot understand quickly will not be approved. Technical writing is the skill of explaining complex material clearly, concisely, and for a particular reader, and it is among the most valued and least taught skills in the profession.

This topic explains the principles of clear technical writing, the main kinds of engineering document, how to write and review a design document or request for comments, how to present trade-offs, and how to give effective presentations and written communication in everyday work.

**Definition:** Technical writing is the practice of communicating technical information, such as designs, decisions, instructions, and reports, in a form that a specific audience can understand and act on accurately, with the least effort necessary on their part.

<!--
IMAGE PROMPT  ->  generate as images/18_intro_technical_writing_and_communicating_designs.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A document page on the left with annotated blocks labelled Context, Goals, Options, Decision; a reader silhouette on the right with a thought bubble; a pen drawing an arrow between them labelled Clear.

ON-IMAGE TEXT: show a short bold title "Technical Writing and Communicating Designs" plus only these few labels, large and legible: Write for the Reader. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Start With the Reader

Every effective document begins with two questions.

1. **Who is the reader?** A new team member, a reviewing architect, an executive deciding on funding, a customer, an operations engineer at night: each needs different content, depth, and vocabulary.
2. **What should the reader do or understand afterwards?** Approve, build, operate, decide, learn. If you cannot state this in one sentence, you are not ready to write.

Readers are busy, read selectively, and are unfamiliar with what you know well. This gives a few guidelines.

- **Put the conclusion first.** State what you want or recommend at the top, then give support (the "inverted pyramid", used by journalists).
- **Assume intelligence but not context.** Explain what the reader could not know; do not explain what they surely know.
- **Define terms** on first use, and use each term consistently (do not alternate between "user", "customer", and "client" for the same thing).
- **Make it scannable:** headings, short paragraphs, lists where items are parallel, tables for comparisons, diagrams for structure.

## Principles of Clear Writing

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Principle</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Guidance</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Weak</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Better</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Be concise</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Remove words that do no work</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"It is the case that the system has the ability to process orders"</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"The system processes orders"</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Be precise</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use exact words and numbers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"The service is pretty slow"</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"The service takes 3 seconds at the 95th percentile; the target is 1 second"</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prefer active voice</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Say who does what</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"The request is sent by the client"</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"The client sends the request"</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use short sentences and plain words</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One idea per sentence</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"Utilise" for "use"; "in order to" for "to"</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"Use"; "to"</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Be concrete</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Give examples</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"Handle errors appropriately"</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"Return a message that names the invalid field"</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Be consistent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Same term, same format, same structure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mixing styles</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A template used throughout</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Be honest about uncertainty</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mark assumptions, unknowns, and risks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hiding gaps</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"We have not measured load above 1,000 users"</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Avoid ambiguity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Check each sentence for two readings</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"The module that calls the service that fails"</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Split into two sentences</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Avoid unexplained abbreviations and jargon</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Spell out and define</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"We use CQRS with ES"</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Define on first use, or link to a glossary</td>
    </tr>
  </tbody>
</table>

### A Writing Process

1. **Plan:** reader, purpose, and key message; an outline of headings.
2. **Draft** quickly without polishing.
3. **Revise for structure:** is the order logical? Is anything missing or irrelevant?
4. **Edit for language:** cut, simplify, and fix.
5. **Check facts and links.**
6. **Test with a reader:** ask someone from the target audience to read it and tell you what they understood. Their confusion is a defect in the document.
7. **Maintain:** documents rot (Unit 8). Keep them near the code, dated, owned, and updated, or delete them.

## Common Kinds of Engineering Document

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Document</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Reader</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Key content</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">README</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Entry point to a project</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">New contributor or user</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What it is, how to install and run, how to contribute, where to find more</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Design document / technical specification</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Propose and record a solution before building</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reviewers, implementers, future maintainers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Context, goals and non-goals, design, alternatives, risks, plan</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Request for Comments (RFC)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Invite feedback on a significant proposal before adopting it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Peers and stakeholders</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Problem, proposal, alternatives, impact, open questions</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Architecture decision record (ADR)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Capture one decision and its reasons (Unit 6)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Future engineers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Context, decision, consequences, status</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">API documentation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Explain how to use an interface (Unit 12)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Developers who consume it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Purpose, operations, examples, errors, limits, versions</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">User guide / tutorial / how-to</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Help people use the product</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">End users</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Task-based steps, screenshots, troubleshooting</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Runbook / operations guide</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Help respond to events</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">On-call engineers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Symptoms, diagnosis steps, actions, escalation (Unit 9)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Incident report / postmortem</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Learn from failure (Unit 9)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Whole organisation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Timeline, impact, causes, actions</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Release notes / changelog</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tell users what changed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Users and integrators</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">New features, fixes, breaking changes, upgrade steps</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Status report</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inform stakeholders (Unit 13)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sponsors and managers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Progress, risks, decisions needed</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Proposal / business case</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Argue for funding or direction</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Decision-makers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Problem, benefit, cost, risk, recommendation</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pull request description and commit message</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Explain a change (Unit 9)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reviewers and future maintainers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What changed and, above all, why</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Bug report</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Describe a defect (Unit 10)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Developers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Steps, expected and actual results, environment</td>
    </tr>
  </tbody>
</table>

### Types of Documentation: Four Needs

A useful framework, associated with Daniele Procida and called Diataxis, distinguishes four kinds of documentation, because mixing them confuses readers.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Kind</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Reader is</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Answers</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Style</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tutorial</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Learning, new</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"Can you teach me?"</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A guided lesson with a successful outcome</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How-to guide</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Working, with a goal</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"How do I do X?"</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Steps to a specific end</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reference</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Working, needing facts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"What exactly is Y?"</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Complete, accurate, dry, consistent</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Explanation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Studying, seeking understanding</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"Why is it like this?"</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Discussion of concepts, context, and reasons</td>
    </tr>
  </tbody>
</table>

## Writing a Design Document

A design document is the standard way for engineers to think through a significant change before committing effort, and to gather review. Writing it forces clarity; many flaws are found while writing.

### A Typical Structure

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Section</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Content</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Title, authors, reviewers, status, date</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Who owns it and its state: draft, in review, approved, superseded</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Summary</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two or three sentences: the problem and the proposal. A reader should be able to stop here</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Context and problem</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Background and why this matters now; the pain being addressed; links to requirements</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Goals</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What success looks like, ideally measurable</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Non-goals</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What is deliberately out of scope (an important and often forgotten section)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Proposed design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The solution at a level that lets reviewers judge it: components and their responsibilities, data flow, interfaces, data model, key algorithms described in prose, with diagrams (Unit 4)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Alternatives considered</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Other options and why they were not chosen. This shows that the choice was reasoned, and saves the next reader from re-asking</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Trade-offs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What the design gives up and what it gains, against quality attributes (Unit 6)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cross-cutting concerns</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security and privacy, performance and scalability, reliability, observability, accessibility, cost, operations (Unit 14 and Unit 9)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Risks and open questions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unknowns, assumptions, and how they will be resolved</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Migration and rollout plan</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How to get from here to there safely, including compatibility and rollback</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Testing plan</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How it will be verified (Unit 10)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Milestones and effort</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rough plan and estimate with ranges (Unit 13)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Appendices</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Supporting detail, references, glossary</td>
    </tr>
  </tbody>
</table>

### Qualities of a Good Design Document

- **Short as possible, as long as necessary.** A few pages for most changes; reviewers' time is limited.
- **Focus on decisions** and their reasons, not on listing everything.
- **Written for readers who are not experts** in your corner of the system.
- **Honest about trade-offs** and uncertainty, not a sales pitch.
- **Reviewed early** while change is still cheap; circulate drafts before decisions are final.
- **Kept after approval** as a record, with a status that makes clear whether it describes current reality.

### Request-for-Comments Culture

Many organisations and open-source communities use RFCs: public, written proposals open to comments for a set time. The practice, which began with the Internet's Request for Comments series in 1969, spreads context, improves quality, creates a durable record, and gives everyone, including juniors, a voice. As an author, welcome criticism as a gift, answer each comment, and record changes; as a reviewer, be specific, kind, and constructive, separating blocking concerns from preferences.

## Presenting Trade-offs

Engineering is the art of choosing among imperfect options. Communicating a decision means showing the options and the reasons.

1. **State the decision to be made and the criteria,** weighted by what the organisation values (cost, time to deliver, risk, maintainability, performance).
2. **Describe each realistic option fairly,** including the one you do not favour.
3. **Compare against the criteria,** often in a table with brief justifications.
4. **Make a recommendation** and explain why.
5. **State the consequences and risks** of the recommendation and how they will be managed.
6. **Say what would change your mind:** the conditions in which another option would be better.

For example, a table comparing three ways of adding search to an application can list the effort, running cost, relevance quality, operational burden, and risks of each, followed by a recommendation. Avoid presenting only the preferred option; it invites distrust and misses better ideas.

## Visual Communication

Diagrams are valuable when they show structure or flow that prose describes poorly (Unit 4 on modelling).

- **One idea per diagram,** with a title.
- **Consistent notation,** with a legend if not standard.
- **Label arrows** to say what they mean (calls, sends event, reads).
- **Show the right level of detail** for the reader: context first, then zoom in (the C4 model is one approach).
- **Do not rely on colour alone;** consider accessibility (previous topic).
- Keep diagrams in editable, version-controlled text where possible so they stay current.

## Presenting Orally

- **Know the audience and the one message** you want them to remember.
- **Structure:** tell them what you will say, say it, and summarise. Lead with the problem and the ask.
- **Slides support, not replace:** few words, one point each, readable visuals; the detail belongs in the document.
- **Rehearse,** and keep to time.
- **Explain, do not read.** Use examples and stories from real cases.
- **Invite questions;** say "I do not know, and I will find out" when that is true.
- **For demonstrations,** prepare, test the environment, have a fallback, and focus on value to the user, not on features (Unit 2 on reviews).
- **Adapt to the room:** executives want outcomes, risks, and decisions needed; engineers want depth.

## Everyday Written Communication

Most writing in engineering is small, and its quality shapes team effectiveness.

- **Messages in chat and email:** a clear subject; the point and the request first; context after; one topic per message; specific deadlines.
- **Asking for help well:** say what you are trying to achieve, what you have tried, what happened, and what you expected, with enough detail to reproduce the problem. This is the skill behind good bug reports (Unit 10), and it shows respect for the helper's time.
- **Code review comments:** specific, explain the reason, suggest alternatives, and are polite; distinguish required changes from suggestions (Unit 11).
- **Meeting notes:** decisions, actions, owners, and dates.
- **Tone:** written words lack voice and face; assume good intent; avoid sarcasm; be careful with strong words. For sensitive matters, speak instead.
- **Cross-cultural and non-native readers:** avoid idioms and slang; prefer simple constructions; be patient.
- **Documentation as a habit:** record decisions when they are made; update docs in the same change as the code; treat a missing explanation as a defect.

## Common Failures

- Writing for yourself, not the reader.
- Burying the conclusion.
- Describing what the system does, without why.
- Documents that never get updated and mislead.
- Long documents with no summary.
- Presenting a single option as the only one.
- Using jargon to sound expert.
- Not asking anyone to read it before sending it.

<!--
IMAGE PROMPT  ->  generate as images/18_design_document_structure.png   (16:9 explanatory diagram, place here)

A vertical document with labelled sections stacked top to bottom (Summary, Context, Goals and non-goals, Proposed design, Alternatives, Risks, Rollout), with an arrow on the side labelled Most readers stop here at the top and a bracket around Alternatives and Trade-offs highlighted in green.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Rewrite and Plan

1. Rewrite this sentence to be clearer: "It is possible that the performance of the system might potentially be negatively impacted by the utilisation of the new caching approach."
2. A design document runs to thirty pages and begins with the history of the project. What is the likely problem, and what is the remedy?
3. Why is a section on alternatives considered valuable?

For case 1, for example: "The new cache may slow the system." (Better still: say how, by how much, and under what conditions.) For case 2, readers cannot find the point; add a short summary and the decision at the top, cut or move the history to an appendix, and organise for the reader. For case 3, it shows that the choice was reasoned, helps reviewers suggest better options, and saves later engineers from reopening the same question.

## Conclusion

Technical writing is the practice of communicating technical information, such as designs, decisions, instructions, and reports, in a form that a specific audience can understand and act on accurately, with the least effort necessary on their part. Starting with the reader, leading with the conclusion, recording alternatives and trade-offs, and keeping documents alive make engineering work understandable, reviewable, and durable.

Skill in writing and in building is developed over a career, in teams, and through continued learning. The next topic covers careers, teamwork, and continuous learning.
