## Introduction

Maintainers spend a large share of their time not changing code but understanding it. The original authors may have left, documentation may be missing or wrong, and the system may be large. Program comprehension is the process by which people build an understanding of software, and reverse engineering is the broader activity of analysing a system to recover its design and purpose. Unit 1 introduced basic habits for reading code. This topic considers the process at the scale of whole systems and the strategies that experienced engineers use.

**Definition:** Reverse engineering is the analysis of an existing system to identify its components and their relationships and to create representations of it at a higher level of abstraction, and program comprehension is the cognitive process of building a mental model of what software does and how, which maintainers rely on before making any change.

<!--
IMAGE PROMPT  ->  generate as images/15_intro_reverse_engineering_and_program_comprehension.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A person standing in front of an unknown machine with its casing removed, drawing a simplified diagram of its parts on a clipboard, with arrows showing the move from detailed code up to a higher-level design sketch.

ON-IMAGE TEXT: show a short bold title "Reverse Engineering and Program Comprehension" plus only these few labels, large and legible: Observe, Abstract, Understand. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Terms

In a widely cited 1990 taxonomy, Elliot Chikofsky and James Cross defined related ideas.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Term</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Forward engineering</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The normal move from requirements and design down to implementation</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reverse engineering</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Analysing a system to recover design-level or requirement-level information, moving up in abstraction</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Redocumentation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Creating or revising documentation of the same level of abstraction, for example producing diagrams from code</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Design recovery</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Using domain knowledge and analysis to reconstruct design abstractions, beyond what the code shows directly</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Restructuring</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Transforming a representation into another of the same level, such as improving the structure of code without changing behaviour</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reengineering</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Examining and altering a system to reconstitute it in a new form, combining reverse engineering with forward engineering</td>
    </tr>
  </tbody>
</table>

Reverse engineering itself **does not change** the system. It aims to understand it.

## How People Understand Programs

Research on how developers read code identified several typical strategies.

- **Top-down comprehension:** the reader starts with a hypothesis about what the program does, based on its domain, and refines it by looking for supporting evidence in the code. Ruven Brooks described it in 1983. It works when the reader knows the domain well.
- **Bottom-up comprehension:** the reader reads code and groups statements into larger meaningful chunks, building up an understanding of the whole, as described by Nancy Pennington. It is common when the code or domain is unfamiliar.
- **Opportunistic or integrated comprehension:** real readers switch between both as needed, as von Mayrhauser and Vans described.
- **As-needed strategy:** for large systems, understand only what is necessary for the task at hand, instead of the whole.

Readers use **beacons**, features that signal what code does, such as a meaningful name or a familiar structure, and form **chunks**, grouped units they can hold as one idea. Good naming and structure assist both.

## Practical Techniques

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Technique</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Start from the user view</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use the system as a user does; list its features and screens; find where each begins in the code</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Run and observe</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Execute the program with different inputs and watch the results; use a debugger to follow the flow</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Read the tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tests show intended behaviour, and examples of use</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Trace a feature end to end</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Follow one request or event from entry to output, noting each step</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Find the entry points and boundaries</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Identify where the program starts, where data enters and leaves, and the main modules</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use search and navigation tools</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Find definitions and uses; follow callers and callees</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Generate diagrams from code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dependency graphs, call graphs, class and package diagrams from tools, to see structure at a glance</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Study data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Examine database tables, formats, and sample records, which often reveal the real model of the domain</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use logs and tracing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Instrument a safe environment to see real behaviour</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Read version history</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Commit messages, linked tickets, and who changed what explain intent</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Talk to people</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Users, support, and previous developers know what documents omit</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Write down findings</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sketches, glossaries, and notes, and update documentation as you learn</td>
    </tr>
  </tbody>
</table>

## Tools

- **Static analysis and visualisation tools** that extract structure and dependencies from code.
- **Debuggers and profilers** that show behaviour at run time.
- **Code search and indexing,** often across many repositories.
- **Version control browsing and blame views.**
- **Decompilers and disassemblers,** when source code is not available, which reconstruct approximate code from compiled programs.
- **Network and system tracing tools** that show how a system talks to others.

## Recovering Higher-Level Views

A goal of reverse engineering is to produce the views that were never written: the **architecture** (components and dependencies), the **data model**, the **main behaviours** (as sequences or flows), the **business rules** embedded in code, and a **glossary** of domain terms used. These recovered views can then support maintenance, modernisation, and onboarding. Their accuracy should be checked against users and experts, since code shows what the system does and not always what it was meant to do.

## Challenges

- **Scale:** too much code to read.
- **Missing context:** the reasons for decisions are not in the code.
- **Misleading names and stale comments.**
- **Dead and duplicated code,** which obscures what matters.
- **Dynamic behaviour,** such as reflection and configuration, which static reading does not reveal.
- **Obsolete technology** that few understand.
- **Time pressure,** which pushes people into making changes without understanding.

## Legal and Ethical Aspects

Reverse engineering of software you do not own may be restricted by licence terms and by law, which varies between countries and contexts. Certain purposes, such as interoperability, security research, and recovering your own lost source, are often treated differently. Engineers should check the licence and legal position before reverse engineering third-party software, and respect confidentiality.

<!--
IMAGE PROMPT  ->  generate as images/02_abstraction_ladder_reverse_vs_forward.png   (16:9 explanatory diagram, place here)

A vertical ladder of abstraction levels from top to bottom: Requirements, Architecture and design, Code, Running system. A downward arrow on the left labelled Forward engineering and a thick upward arrow on the right labelled Reverse engineering, with a small note that restructuring moves sideways at the same level.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Pick the Technique

1. A maintainer wants to see which modules depend on which in a large unfamiliar system.
2. A maintainer needs to know why an unusual workaround was added to a function two years ago.
3. A maintainer wants to understand the structure of the data a legacy system stores.

Case 1 calls for dependency visualisation generated by tools. Case 2 calls for version history and linked tickets, and possibly asking former developers. Case 3 calls for examining the database structure and sample records.

## Conclusion

Reverse engineering is the analysis of an existing system to identify its components and their relationships and to create representations of it at a higher level of abstraction, and program comprehension is the cognitive process of building a mental model of what software does and how, which maintainers rely on before making any change. Combining observation, tools, history, and people is the way to recover understanding efficiently.

Understanding a system may lead to a decision about its future. The next chapter describes the choices for modernising and renewing software, beginning with reengineering.
