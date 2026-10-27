## Introduction

The practices of modern software engineering, such as code review, version control, and iterative delivery, developed in stages, each in response to a recurring kind of failure.

This topic outlines those stages, so that later topics on process, design, testing, and operations can be read as responses to specific problems.

**Definition:** The history of software engineering is the record of how practitioners repeatedly hit the limits of how they built software, and introduced new practices, such as structured design, process models, version control, and agile methods, to push those limits back.

<!--
IMAGE PROMPT  ->  generate as images/02_intro_a_brief_history_of_software_engineering.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A horizontal timeline from the 1960s to the 2020s with milestone markers for each era, rising from a single mainframe to a cloud of connected services.

ON-IMAGE TEXT: show a short bold title "A Brief History of Software Engineering" plus only these few labels, large and legible: 1960s, Today, Practices. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The 1960s: Hardware Gets Cheap, Software Gets Hard

In the 1950s programs were small and usually written by the people who operated the machine. During the 1960s computers became far more powerful, and organisations asked them to do far more. Programs grew from hundreds to hundreds of thousands of lines, and craft habits that worked for small programs stopped working.

Large projects such as IBM's OS/360 operating system were famously late and over budget. This widespread pattern of late, expensive, unreliable software became known as the **software crisis**. The term "software engineering" came into common use at two NATO conferences, in Garmisch in 1968 and Rome in 1969, whose organisers deliberately chose a provocative name to suggest that software should become as dependable as other engineering products.

## The 1970s and 1980s: Structure and Process

The first response was to impose **structure**. Edsger Dijkstra's 1968 letter "Go To Statement Considered Harmful" argued that programs built from tangled jumps were impossible to reason about, which led to **structured programming** built from sequence, choice, and repetition.

Process followed structure. In 1970 Winston Royce described a staged approach in which requirements, design, coding, and testing happen in order, later called the **waterfall model**. Royce himself warned that a strict single pass was risky.

In 1975 Fred Brooks published *The Mythical Man-Month*, introducing the idea now called **Brooks's Law**: adding people to a late software project tends to make it later, because newcomers must be taught and communication paths multiply. His 1986 essay "No Silver Bullet" argued that no single tool or technique would make software development ten times easier, because much of the difficulty is essential to the problem.

## The 1990s: Objects, Patterns, and Heavy Processes

Engineers organised systems around **objects**, which bundle data with the operations on it. In 1994 four authors known as the "Gang of Four" published a catalogue of reusable object-oriented design solutions, launching the **design patterns** movement. The Unified Modeling Language standardised how designs were drawn, and detailed processes such as the Rational Unified Process tried to make large projects predictable.

Many of these processes were heavy. Teams could spend months producing documents while the customer's needs quietly changed.

## 2001 Onward: Agile, Open Source, and DevOps

In February 2001, seventeen practitioners wrote the **Agile Manifesto**, valuing working software, customer collaboration, and responding to change over rigid plans and heavy documentation. Scrum, Extreme Programming, and Kanban spread quickly afterwards.

Tools matured alongside methods. Git, created in 2005, gave teams a fast, reliable way to track and merge changes, and open-source platforms made collaboration across organisations routine. Around 2009 the **DevOps** movement joined development and operations through automation of building, testing, and deployment. The 2020s add cloud platforms, machine learning components, and AI coding assistants, each bringing new benefits and new ways to fail.

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

## The Pattern Behind the Dates

Every row in the right-hand column is a **response** to something that had hurt people. This is the most useful idea in the history of the field: practices are not fashions, they are accumulated lessons. A team that drops a practice without understanding the failure it was created to prevent usually meets that failure again.

## Your Turn: Match the Practice to the Pain

Match each practice (A to C) to the problem it was created to reduce (1 to 3).

- A. Version control
- B. Structured programming
- C. Agile iterations with frequent customer feedback

1. Customers received software months later that no longer matched what they needed.
2. Code full of tangled jumps that nobody could follow or safely change.
3. Several developers overwriting each other's work and losing track of who changed what.

A matches 3: version control lets many people change the same material while every change is recorded and mergeable. B matches 2: structured programming gave code a clear shape that people can reason about. C matches 1: short iterations with customer feedback reduce the gap between what is built and what is needed.

## Conclusion

The history of software engineering is the record of how practitioners repeatedly hit the limits of how they built software, and introduced new practices, such as structured design, process models, version control, and agile methods, to push those limits back. Knowing which problem a practice answers is the best protection against both blind ritual and careless abandonment.

The next topic looks at the problems themselves: what actually goes wrong on real projects.
