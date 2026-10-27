## Introduction

Software is not built in a single act. Whatever the team, tools, or product, the work passes through recognisable activities: understanding what is needed, deciding how to build it, building it, checking it, releasing it, and keeping it useful afterwards.

This topic names those activities, shows what each one produces, and explains why the order is a loop and not a straight line. Later units on process models and agile methods are variations on how this life cycle is organised.

**Definition:** The software development life cycle (SDLC) is the sequence of activities, from understanding what is needed through building, checking, releasing, and maintaining software, that turns an idea into a working system and keeps it useful.

<!--
IMAGE PROMPT  ->  generate as images/05_intro_the_software_development_life_cycle.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A circular loop with six stops labelled Requirements, Design, Implementation, Verification, Deployment, Maintenance, with a return arrow from Maintenance to Requirements.

ON-IMAGE TEXT: show a short bold title "The Software Development Life Cycle" plus only these few labels, large and legible: Plan, Build, Release. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Six Core Activities

Teams name and order these differently, but the same six appear in nearly every project.

1. **Requirements.** Find out what users and the business need. Output: a clear description of the required features and qualities.
2. **Design.** Decide how the system will be structured to meet those needs. Output: architecture and design descriptions.
3. **Implementation.** Write the code. Output: working source code.
4. **Verification.** Check that the software does what was required and meets the expected quality. Output: test results and a list of defects.
5. **Deployment.** Release the software so real users can use it. Output: a running system.
6. **Maintenance.** Fix problems, adapt to new environments, and add improvements for as long as the software lives. Output: new versions.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Activity</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Question it answers</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical output</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example: a meal-rating feature</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What should it do, and for whom?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">User stories, requirement specification</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A user can rate a meal from 1 to 5 once, after it has been served</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How will it be built?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Diagrams, data model, interface sketches</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A ratings store linked to meals and users, and a screen to submit a rating</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Implementation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can we make it real?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Code and unit tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Code that stores ratings and calculates averages</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Verification</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does it work as required?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test reports, defect list</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Checks for duplicate ratings and out-of-range values</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deployment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How do users get it?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A released version</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The feature is switched on for real users</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maintenance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How do we keep it useful?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fixes and updates</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Allow editing a rating after user feedback</td>
    </tr>
  </tbody>
</table>

## It Is a Loop, Not a Straight Line

Reading the table top to bottom suggests a one-way journey. In practice, work moves backwards constantly. A tester finds that a requirement was ambiguous, a designer discovers that an idea cannot be built within budget, and maintenance reveals needs that begin the cycle again. Each pass through the activities is an **iteration**.

Different **process models**, studied in Unit 2, answer one question: how long should each loop be, and how much should be planned before the first loop begins?

## Activities Versus Phases

An **activity** is a kind of work, such as testing. A **phase** is a period of time in a plan. In a strictly sequential plan, each activity gets its own phase. In an iterative or agile plan, every iteration contains a little of every activity. Keeping the two ideas apart avoids the common mistake of believing that "testing happens at the end" is a law instead of a choice.

## Why Early Mistakes Cost More

A defect is cheaper to fix the earlier it is found. A misunderstanding caught during requirements costs a conversation. The same misunderstanding caught after deployment costs rework in design, code, tests, and every user already affected. Barry Boehm's classic studies reported cost growing sharply the later a fault is found. The exact multipliers vary between projects, and modern practices have flattened part of the curve, but the direction holds: **find mistakes early**.

## Writing Requirements Before Building

The cheapest control in the whole life cycle is a short, precise statement of what a feature must do and how anyone will know it works. A good one names who benefits and why, and lists acceptance conditions that can be checked. For a rating feature, the conditions might state that a rating must be a whole number from 1 to 5, that each user may rate each meal at most once, and that a meal cannot be rated before it has been served. Those three conditions drive every later activity: design decides where ratings are stored, implementation enforces the rules, and verification checks each one.

## Your Turn: Which Activity Is This?

Name the life cycle activity for each situation.

1. The team discusses whether ratings belong in the existing database or in a separate service.
2. A tester tries to submit a rating of 7 to see how the system reacts.
3. Three months after launch, staff ask for a weekly report of the lowest rated dishes.
4. A developer writes the logic that calculates an average rating.

Situation 1 is design. Situation 2 is verification. Situation 3 is maintenance, since it extends software already in use, and it also triggers new requirements work. Situation 4 is implementation.

## Conclusion

The software development life cycle is the sequence of activities, from understanding what is needed through building, checking, releasing, and maintaining software, that turns an idea into a working system and keeps it useful. It is a loop, and the earlier a mistake is caught, the cheaper it is to fix.

Each activity needs people with different skills. The next topic looks at the roles those people play and how they work together.
