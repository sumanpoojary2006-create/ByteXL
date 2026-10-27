## Introduction

Building software requires more than writing code. In a typical product team, only part of the people mainly write code; others decide what to build, design how it should feel, check its quality, and keep it running. Each role carries distinct responsibilities, and the way these roles communicate often limits the pace of a team more than individual technical skill.

This topic describes the common roles in a software team, the stakeholders outside the team, and why communication, more than typing speed, usually limits how fast a team can move.

**Definition:** A software team is a group of people with complementary responsibilities, such as deciding what to build, designing it, writing and checking it, and running it, who must coordinate closely because no single person holds all the knowledge the product requires.

<!--
IMAGE PROMPT  ->  generate as images/06_intro_roles_in_a_software_team.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A round table with eight avatars, each holding a symbol: a compass, a pencil, a laptop, a magnifier, a gear, a map, a megaphone, and a clipboard.

ON-IMAGE TEXT: show a short bold title "Roles in a Software Team" plus only these few labels, large and legible: Team, Roles, Ownership. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Common Roles

Titles vary between companies, but these responsibilities appear almost everywhere.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Role</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Main responsibility</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical question they ask</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Product owner / product manager</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Decides what is worth building and in what order</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What problem do users have, and is this the most valuable thing to do next?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Business analyst</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Turns business needs into precise requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What exactly must the system do, and what are the rules?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">UX / UI designer</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Designs how the product feels and flows</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can a first-time user complete this task without help?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Software engineer</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Designs and builds features, and writes tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How should this be built so it is correct and easy to change?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tech lead / architect</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Guides technical direction and key decisions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Will this design still work with ten times the users?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">QA / test engineer</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Plans and runs checks to find problems before users do</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How could this break, and how do we show it does not?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">DevOps / site reliability engineer</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Builds the delivery pipeline and keeps the system running</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How do we release safely, and how do we know the system is healthy?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Engineering manager</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Supports the team: people, hiring, delivery, growth</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does the team have what it needs to do good work?</td>
    </tr>
  </tbody>
</table>

## Stakeholders: People Who Care About the Outcome

A **stakeholder** is anyone with an interest in the system or its outcome, whether or not they sit on the team. Typical groups are:

- **Users:** the people who use the product directly
- **Customers:** the organisations or individuals who pay for it
- **Operators:** staff who configure it and read its reports
- **Regulators and partners:** bodies and suppliers whose rules or services the product must respect

These groups want different, sometimes conflicting, things. Users want convenience, customers want low cost, and partners want strict security. Recognising whose needs a decision serves is a core engineering skill.

## Small Teams Wear Many Hats

In a small startup one person may act as both product owner and business analyst, and every engineer may handle some testing and deployment. Large companies split roles finely. Either way, **each responsibility still needs an owner**. A frequent cause of failure is an important responsibility, such as security review, that everyone assumed someone else was handling.

Engineers are encouraged to be **T-shaped**: deep in one specialty, with enough breadth to understand and talk to neighbouring roles.

## Why Communication Becomes the Bottleneck

As a team grows, the number of pairs of people who might need to talk grows much faster than the number of people. For a team of n people, the number of possible one-to-one communication paths is n times (n minus 1), divided by 2.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Team size (n)</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Possible communication paths</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">3</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">3</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">5</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">10</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">28</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">12</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">66</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">20</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">190</td>
    </tr>
  </tbody>
</table>

This is the arithmetic behind Brooks's Law from the history topic: adding people to a late project adds communication overhead before it adds output. It is also why teams rely on clear roles, written decisions, and short regular meetings instead of expecting everyone to talk to everyone.

## Your Turn: Who Owns It?

Name the role most responsible for each task.

1. Deciding whether the next quarter should go to a rating feature or a faster ordering flow.
2. Noticing that the checkout button is hard to find on a small phone screen.
3. Arranging for tests to run automatically whenever code is changed.
4. Checking how the system behaves when a user submits an empty rating.

Task 1 belongs to the product owner or product manager. Task 2 belongs to the UX designer. Task 3 belongs to the DevOps engineer, although developers benefit every day. Task 4 belongs to QA, with developers also writing automated checks for the same case.

## Conclusion

A software team is a group of people with complementary responsibilities, such as deciding what to build, designing it, writing and checking it, and running it, who must coordinate closely because no single person holds all the knowledge the product requires. Clear ownership and light but regular communication keep a growing team effective.

All these roles share a goal: software that is genuinely good. The next topic makes that goal precise by naming the qualities that separate good software from merely working software.
