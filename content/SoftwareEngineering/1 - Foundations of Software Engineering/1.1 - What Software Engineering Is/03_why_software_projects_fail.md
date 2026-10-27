## Introduction

Software projects fail more often than most people expect, and rarely for the reason that headlines suggest. A failed launch is usually attributed to a bug, but a bug is the last link in a longer chain of decisions about requirements, design, testing, communication, and risk.

This topic examines what "failure" means for a software project, studies four well-documented cases, and identifies the recurring root causes that professional teams try to design out of their process.

**Definition:** A software project fails when it is delivered late, over budget, with serious faults, or not at all, and the root cause is almost never a single bug but a chain of weak decisions about requirements, design, testing, communication, and risk.

<!--
IMAGE PROMPT  ->  generate as images/03_intro_why_software_projects_fail.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A chain of connected links labelled Requirements, Design, Testing, Communication, Risk, with one cracked link at the end labelled Bug.

ON-IMAGE TEXT: show a short bold title "Why Software Projects Fail" plus only these few labels, large and legible: Chain, Cause, Failure. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## What Counts as Failure?

Failure is not only a crash. A project can fail by:

- **missing its schedule or budget** by a wide margin
- **delivering the wrong product**, one that works but does not meet the real need
- **shipping with serious defects** that harm users or the business
- **becoming unmaintainable**, so that every change is slow, risky, and expensive
- **being cancelled** before it delivers anything of value

## Four Case Studies

**Ariane 5, 1996.** About 37 seconds after launch, the first Ariane 5 rocket veered off course and destroyed itself, a loss commonly estimated at around 370 million US dollars. The guidance software, reused from the older Ariane 4, converted a large 64-bit floating point value into a 16-bit integer, causing an overflow that shut down the guidance computers. Root causes: software **reused without re-validation** for a faster rocket, and a calculation no longer needed after liftoff that kept running.

**Mars Climate Orbiter, 1999.** The spacecraft was lost on approach to Mars because one team's software produced thruster data in imperial units (pound-force seconds) while the receiving team expected metric units (newton seconds). Root cause: an **interface assumption that was never stated and checked** between two teams.

**Knight Capital, 2012.** A deployment step missed one of eight servers, leaving old code running that sent a flood of unintended trades. In roughly 45 minutes the firm lost about 440 million US dollars. Root causes: a **manual, unchecked deployment process**, obsolete code left in the system, and no quick way to stop the damage.

**Therac-25, 1985 to 1987.** A radiation therapy machine delivered massive overdoses in at least six accidents. Investigators found software errors, including a race condition triggered by fast operator input, and noted that hardware safety interlocks from earlier models had been removed on the assumption that software was reliable enough. Root causes: **overconfidence in software**, weak testing, and failure to act on early accident reports.

## Common Root Causes

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Root cause</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it looks like</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example from the cases</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unclear or changing requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The team builds the wrong thing, or the target keeps moving</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ariane 5 conditions not re-examined for the new rocket</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Poor communication between teams</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Assumptions differ across a boundary</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mars Climate Orbiter units</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inadequate testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Failures first meet real users</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ariane 5, Therac-25</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unrealistic estimates and schedules</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A deadline is fixed before the work is understood</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Common on everyday projects</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unmanaged risk</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nobody asks "what if this goes wrong?"</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Knight Capital had no emergency stop</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Weak process and automation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Manual steps that humans eventually miss</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Knight Capital deployment</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Overconfidence in software</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Other safeguards are removed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Therac-25 interlocks</td>
    </tr>
  </tbody>
</table>

## Failure Is a Chain, Not a Single Event

Safety engineers use the image of slices of Swiss cheese. Each safeguard, such as a review, a test, a monitor, or a manual check, has holes. A disaster happens only when the holes in several slices line up. This is encouraging: strengthening any one layer can break the chain, so teams improve by adding independent defences instead of hoping to write perfect code.

## Learning From Failure: The Postmortem

A **postmortem** (or retrospective review) is a structured analysis written after a failure. Good ones are **blameless**: they ask what conditions allowed the failure instead of who is at fault, because blame discourages people from reporting problems early. A postmortem records the timeline, the root causes, and concrete changes to prevent recurrence.

## Your Turn: Find the Root Cause

Name the category of root cause from the table for each statement.

1. A payment feature double-charged users because one system counted amounts in the smallest currency unit while another sent whole units.
2. A release date was promised before any design work had started.
3. A developer copied files to a production server by hand and forgot one folder.

Statement 1 is poor communication across a boundary: the unit was never agreed and checked, the same family as Mars Climate Orbiter. Statement 2 is an unrealistic estimate, because the date was committed before the work was understood. Statement 3 is weak process and automation: a manual step relied on human memory, which is exactly what failed at Knight Capital.

## Conclusion

A software project fails when it is delivered late, over budget, with serious faults, or not at all, and the root cause is almost never a single bug but a chain of weak decisions about requirements, design, testing, communication, and risk. Postmortems exist to find the chain, not the culprit.

Knowing what can go wrong helps decide how much care a project needs, and that depends on the kind of system being built. The next topic classifies software systems and shows how the type shapes the engineering effort.
