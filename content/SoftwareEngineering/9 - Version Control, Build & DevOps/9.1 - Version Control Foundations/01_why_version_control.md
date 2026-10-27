## Introduction

Version control is the practice of recording every change made to a set of files, who made it, when, and why, so that any earlier state can be recovered, compared, and understood. For software, whose source is a large and constantly changing set of files edited by many people at once, this record is essential: it allows work to proceed in parallel, changes to be reviewed and reversed, and a team to know exactly which version of the system is in use at any time. It underlies almost every other practice in this unit.

**Definition:** Version control is a system that records every change made to a set of files over time, who made it and why, so that any earlier state can be recovered, different lines of work can be developed in parallel and combined, and a team can collaborate on the same material without overwriting one another.

<!--
IMAGE PROMPT  ->  generate as images/01_intro_why_version_control.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A timeline of file snapshots labelled with versions, a rewind arrow going back to an earlier snapshot, and two parallel branches of work joining together, with several collaborators around it.

ON-IMAGE TEXT: show a short bold title "Why Version Control" plus only these few labels, large and legible: History, Branch, Merge. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Problems It Solves

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem without version control</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What version control provides</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Files overwritten by colleagues, work lost</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every change is recorded and merged; nothing is silently lost</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No way to return to a working state after a bad change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Any earlier version can be restored</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unknown reason for a change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Each change carries an author, time, and message explaining why</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Folders of copies with confusing names</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One organised history</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cannot work on two things at once without interference</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Branches allow parallel lines of work</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cannot reproduce the exact version released last year</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Releases are marked and can be rebuilt precisely</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No accountability or audit trail</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A complete record of who changed what and when</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fear of experimenting</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Experiments are cheap and can be discarded</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hard to find which change introduced a bug</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">History can be searched and bisected</td>
    </tr>
  </tbody>
</table>

## What Is Tracked

Version control manages a **repository**: a project's files together with their complete history. It tracks source code and anything else that is needed to build and run the system and that is mostly text: configuration, build scripts, documentation, tests, and infrastructure definitions. It is poorly suited to very large binary files such as videos and compiled outputs, which are usually stored elsewhere.

## A Short History

The tools evolved through generations.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Generation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Characteristics</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Local, single file</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">SCCS (1970s), RCS (1980s)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Track versions of individual files on one machine</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Centralised</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">CVS (1990s), Subversion (2000), Perforce</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A single central server holds the history; users check out and commit to it</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Distributed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Git and Mercurial (both 2005), Bazaar</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every user holds a full copy of the history; no single point of failure</td>
    </tr>
  </tbody>
</table>

Linus Torvalds created **Git** in 2005 to manage development of the Linux kernel, after a proprietary tool the project had been using could no longer be used. He wanted speed, strong support for non-linear development with thousands of branches, and protection of the integrity of history. Git is now by far the most widely used version control system, and the rest of this unit uses it as the main example.

## Centralised and Distributed

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Centralised</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Distributed</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Where history lives</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">On a central server</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">In every clone, as well as on any shared server</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Working offline</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Limited: most operations need the server</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Almost everything works offline</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Speed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operations often involve a network round trip</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Most operations are local and fast</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Backup and resilience</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The server is a single point of failure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every clone is a full backup</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Branching</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Often heavy and discouraged</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cheap and routine</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Access control</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fine-grained at the server</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mainly managed through the hosting platform</td>
    </tr>
  </tbody>
</table>

A shared server is still used in practice, for collaboration, but it is a convenience and not a technical necessity.

## Two Models of Editing

- **Lock-modify-unlock:** a person locks a file, edits it, and releases it, so no one else can change it meanwhile. It prevents conflicts but blocks parallel work.
- **Copy-modify-merge:** everyone edits freely and the system combines the changes, asking humans only where changes truly collide. It is the model of modern tools, and it works well for text.

## Core Benefits for Software Teams

1. **Collaboration:** many people work at once.
2. **History and traceability:** a record that serves as documentation of how and why the system changed.
3. **Safety:** work is backed up, and mistakes can be undone.
4. **Parallel development:** features, fixes, and experiments proceed independently on branches.
5. **Reproducibility:** any version, such as a released one, can be rebuilt.
6. **Foundation for automation:** build, test, and deployment pipelines are triggered by changes in the repository.
7. **Code review and quality control:** changes are proposed and examined before acceptance.

## Good Habits from the Start

- Put **everything needed to build and run** the project in version control.
- Keep **generated files, secrets, and personal settings** out of it.
- **Commit often** in small logical steps.
- Write **meaningful messages**.
- **Never store passwords or keys** in a repository, since history preserves them forever.
- Use a **consistent workflow** agreed by the team.

<!--
IMAGE PROMPT  ->  generate as images/02_centralised_vs_distributed_vcs.png   (16:9 explanatory diagram, place here)

Left: a Centralised system, one server in the middle and three users with only working copies connected by arrows. Right: a Distributed system, three users each holding a full repository copy, connected to each other and to a shared server, with history icons in every copy.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Which Benefit?

1. A developer discovers that last week change broke the login, and wants to see exactly what changed since the last working version.
2. Two developers have been editing different parts of the same file and want to combine their work.
3. A customer reports a bug in version 3.2 that was released a year ago, and the team needs to rebuild it.

Situation 1 uses the recorded history to compare versions. Situation 2 uses merging, which combines parallel changes. Situation 3 uses reproducibility: a marked release can be rebuilt exactly.

## Conclusion

Version control is a system that records every change made to a set of files over time, who made it and why, so that any earlier state can be recovered, different lines of work can be developed in parallel and combined, and a team can collaborate on the same material without overwriting one another. It is the base on which the rest of modern software practice is built.

Having seen why it matters, the next topic explains how Git, the dominant tool, actually works.
