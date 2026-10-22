## Introduction

CampusConnect's users had been asking for the same thing for weeks: a way to rate each meal. Ananya assumed her first real feature would begin the way her student projects always had, by opening the editor and typing. She had already created a file called `ratings.py`.

Vikram stopped her kindly. "Before we write a line," he said, "tell me who rates meals, what happens to a rating, and how we will know the feature works." She realised she could not answer any of those. In ten minutes of conversation they discovered that students wanted to rate a meal only after eating it, that the mess manager wanted weekly averages, and that nobody had decided whether ratings could be edited.

Had Ananya started coding, she would have built something plausible and wrong. What Vikram was guiding her through is the shape that nearly all software work follows: the **software development life cycle**.

**Definition:** The software development life cycle (SDLC) is the sequence of activities, from understanding what is needed through building, checking, releasing, and maintaining software, that turns an idea into a working system and keeps it useful.

<!--
IMAGE PROMPT  ->  generate as images/05_intro_the_software_development_life_cycle.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Use the named person, setting, and engineering problem from the Introduction.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Ananya sits at a laptop with a half-written ratings file while Vikram draws a circular route on a glass board with six labelled stops, from a lightbulb idea to a deployed app with star ratings.

ON-IMAGE TEXT: show a short bold title "The Software Development Life Cycle" plus only these few labels, large and legible: Plan, Build, Release. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Six Core Activities

Different teams name and order them differently, but the same six activities appear in nearly every project.

1. **Requirements.** Find out what the users and the business need. Output: a clear description of the features and qualities required.
2. **Design.** Decide how the system will be structured to meet those needs. Output: architecture and design descriptions.
3. **Implementation.** Write the code. Output: working source code.
4. **Verification (testing).** Check that the software does what was required and that it is of acceptable quality. Output: test results and a list of defects.
5. **Deployment.** Release the software so real users can use it. Output: a running system.
6. **Maintenance.** Fix problems, adapt to new environments, and add improvements for as long as the software lives. Output: new versions.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Activity</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Question it answers</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical output</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Ratings feature example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What should it do, and for whom?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">User stories, requirement specification</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A student can rate a meal 1 to 5 once after the meal time ends</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How will it be built?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Diagrams, data model, interface sketches</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A Ratings table linked to meals and users, a new API endpoint</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Implementation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can we make it real?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Code and unit tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Code that stores and averages ratings</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Verification</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does it work as required?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test reports, bug list</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tests for duplicate ratings and out-of-range values</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deployment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How do users get it?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A released version</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ratings go live on the production server</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maintenance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How do we keep it useful?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fixes and updates</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Allow editing a rating after feedback from students</td>
    </tr>
  </tbody>
</table>

<!--
IMAGE PROMPT  ->  generate as images/02_sdlc_six_activities_loop.png   (16:9 explanatory diagram, place here)

A circular loop with six numbered stops: Requirements, Design, Implementation, Verification, Deployment, Maintenance. A thin return arrow from Maintenance back to Requirements, and small back-arrows between neighbouring stops to show feedback.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## It Is a Loop, Not a Straight Line

Reading the table top to bottom suggests a one-way journey. In practice, work moves backwards constantly. A tester finds that a requirement was ambiguous, a designer discovers that an idea cannot be built within budget, and maintenance reveals needs that start the cycle again. Each pass through the loop is called an **iteration**.

Different **process models**, which Unit 2 studies in detail, answer a single question: how long should each loop be, and how much should be planned before the first one begins?

## Why Early Mistakes Cost More

A defect is cheaper to fix when it is found early. A misunderstanding caught during requirements costs a conversation. The same misunderstanding caught after deployment costs rework in design, code, tests, and every user already affected. Barry Boehm's classic studies reported cost growing sharply the later a fault is found. The exact multipliers vary widely between projects, and modern practices have flattened some of the curve, but the direction of the effect still holds: **find mistakes early**.

## Working Through One Feature

Back to the ratings feature. After her conversation with Vikram, Ananya wrote this short requirement before touching code:

```text
As a student, I want to rate a meal from 1 to 5 stars after
meal time ends, so that the mess manager knows which dishes to improve.

Acceptance:
- A rating must be an integer from 1 to 5.
- A student can rate each meal at most once.
- A student cannot rate a meal that has not been served yet.
```

Those three acceptance lines drive every later activity: design chooses where to store ratings, implementation enforces the rules, and testing checks each rule. Notice that this little text took five minutes, and it saved days.

## Your Turn: Which Activity Is This?

Name the life cycle activity each situation belongs to.

1. The team discusses whether to store ratings in the existing database or a separate service.
2. A tester tries to submit a rating of 7 to see what the app does.
3. Mess staff ask for a weekly report of the lowest rated dishes, three months after launch.
4. A developer writes the function that calculates the average rating.

Situation 1 is design. Situation 2 is verification. Situation 3 is maintenance, since it extends software that is already in use, and it will also trigger new requirements work. Situation 4 is implementation.

## Conclusion

The software development life cycle is the sequence of activities, from understanding what is needed through building, checking, releasing, and maintaining software, that turns an idea into a working system and keeps it useful. It is a loop, and the earlier a mistake is caught, the cheaper it is to fix.

Each activity needs people with different skills. In the same ratings conversation, Ananya spoke to the mess manager, Vikram, and a designer within an hour. The next lesson looks at who these people are and how they work together.
