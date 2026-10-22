## Introduction

During her first week, Ananya noticed that CampusConnect had rules that felt almost ceremonial. Every change needed a second person to read it before it could be merged. Every release followed a checklist. Nobody was allowed to deploy on a Friday afternoon. She asked Vikram whether all this was really necessary for a mess-menu app.

Vikram smiled and told her a story that begins in October 1968, in a hotel in the Bavarian town of Garmisch, Germany. Around fifty of the world's leading computer scientists and engineers had been invited by NATO to talk about a problem that embarrassed them: large software projects kept arriving late, over budget, and full of faults. The conference title was deliberately provocative. It was called "Software Engineering," a phrase meant to suggest that building software ought to be as dependable as building bridges, and that it clearly was not yet.

"Every rule you find annoying," Vikram said, "is a scar from a failure someone paid for."

**Definition:** The history of software engineering is the story of people repeatedly hitting the limits of how they built software, and inventing new practices, such as structured design, process models, version control, and agile methods, to push those limits back.

<!--
IMAGE PROMPT  ->  generate as images/02_intro_a_brief_history_of_software_engineering.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Use the named person, setting, and engineering problem from the Introduction.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Vikram points at a glowing timeline stretching from a 1968 conference hall with delegates at long tables to a modern open-plan office, while Ananya studies the milestones along it.

ON-IMAGE TEXT: show a short bold title "A Brief History of Software Engineering" plus only these few labels, large and legible: 1968, Crisis, Today. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The 1960s: Hardware Gets Cheap, Software Gets Hard

In the 1950s, programs were small and written by the same people who built or operated the machine. During the 1960s, computers became far more powerful, and organisations asked them to do far more. Programs grew from hundreds of lines to hundreds of thousands, and the old craft habits stopped working.

IBM's OS/360 operating system became the famous example. It was one of the largest software projects of its time, it arrived late and over budget, and the manager who led it, Fred Brooks, later wrote one of the most influential books in the field about what went wrong (more on that below).

This widespread pattern of late, expensive, unreliable software became known as the **software crisis**. The 1968 NATO conference in Garmisch, and a follow-up in Rome in 1969, are the moments where the term "software engineering" entered common use. Margaret Hamilton, who led the flight software team for the Apollo missions at MIT, has said she began using the phrase herself in the early 1960s to give software work the seriousness it deserved.

## The 1970s and 1980s: Structure and Process

The first response was to impose **structure**. In 1968 Edsger Dijkstra published a short letter titled "Go To Statement Considered Harmful," arguing that code built from tangled jumps was impossible to reason about, and that programs should use clear sequence, choice, and loops. This led to **structured programming**.

Process followed structure. In 1970, Winston Royce described a staged approach in which requirements, design, coding, and testing happen in order. Later readers named this the **waterfall model**, though Royce himself warned that a strict version was risky.

In 1975 Fred Brooks published *The Mythical Man-Month*. Its best-known idea, now called **Brooks's Law**, states that adding more people to a late software project tends to make it later, because new people must be taught and the number of communication paths grows rapidly. In 1986 his essay "No Silver Bullet" argued that no single tool or technique would make software development ten times easier, because much of the difficulty is essential to the problem and not an accident of tools.

## The 1990s: Objects, Patterns, and Heavy Processes

As systems kept growing, engineers organised code around **objects** that bundle data with the operations on that data. In 1994, four authors known as the "Gang of Four" published a catalogue of reusable object-oriented design solutions, launching the **design patterns** movement. The Unified Modeling Language (UML) standardised how designs were drawn, and detailed processes such as the Rational Unified Process tried to make large projects predictable.

Many of these processes were heavy. Teams could spend months producing documents while the customer's needs quietly changed.

## 2001 Onward: Agile, Open Source, and DevOps

In February 2001, seventeen practitioners met at a ski resort in Utah and wrote the **Agile Manifesto**. It valued working software, customer collaboration, and responding to change over rigid plans and heavy documentation. Scrum, Extreme Programming, and Kanban spread quickly afterwards.

Tools matured alongside methods. Linus Torvalds created **Git** in 2005, giving teams a fast way to track and merge changes. Open-source platforms made collaboration across companies routine. Around 2009 the **DevOps** movement joined development and operations, with automation that builds, tests, and deploys software many times a day. The 2020s add cloud platforms, machine learning components, and AI coding assistants, each of which brings new benefits and new ways to fail.

## Timeline at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Period</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem faced</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Response that emerged</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1960s</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Large programs late, over budget, unreliable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The term "software engineering," the NATO conferences</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Late 1960s to 1970s</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tangled code nobody can reason about</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Structured programming, staged processes such as waterfall</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1975 to 1986</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Adding people does not speed up late projects</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Brooks's Law, recognition that there is no silver bullet</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1990s</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Growing systems hard to organise and reuse</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Object-oriented design, design patterns, UML, heavy processes</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2001 onward</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Plans and documents outpace changing needs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Agile methods, Git, open-source collaboration</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2009 onward</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Slow, risky releases</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">DevOps, continuous integration and delivery, cloud</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2020s</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">New kinds of components and tools</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Machine learning engineering, AI-assisted development</td>
    </tr>
  </tbody>
</table>

<!--
IMAGE PROMPT  ->  generate as images/03_software_engineering_timeline.png   (16:9 explanatory diagram, place here)

A horizontal timeline from 1960s to 2020s with seven milestone markers: NATO 1968, Structured Programming, Mythical Man-Month 1975, Design Patterns 1994, Agile Manifesto 2001, Git 2005, DevOps 2009. Each marker has a tiny icon.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## The Pattern Behind the Dates

Look at the right-hand column of that table. Every item is a **response** to something that had hurt people. This is the single most useful idea in the history of the field: practices are not fashions, they are accumulated lessons. When a team abandons a practice without understanding the failure it was created to prevent, the failure usually returns.

## Your Turn: Match the Practice to the Pain

Match each practice (A to C) to the problem it was invented to reduce (1 to 3).

- A. Version control with Git
- B. Structured programming
- C. Agile iterations with frequent customer feedback

1. Customers received software months later that no longer matched what they needed.
2. Code full of tangled jumps that nobody could follow or safely change.
3. Several developers overwriting each other's work and losing track of who changed what.

A matches 3: version control exists so that many people can change the same code and every change is recorded and mergeable. B matches 2: structured programming gave code a clear shape that people can reason about. C matches 1: short iterations with customer feedback reduce the gap between what is built and what is needed.

## Conclusion

The history of software engineering is the story of people repeatedly hitting the limits of how they built software, and inventing new practices, such as structured design, process models, version control, and agile methods, to push those limits back. The rules at CampusConnect that seemed excessive to Ananya are each connected to a real class of failure.

The obvious next question is a practical one: what exactly goes wrong on real projects, and how often is the cause something other than a bug in the code?
