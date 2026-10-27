## Introduction

A requirement such as "the system should be fast" sounds reasonable and is almost useless. Fast compared to what, on which screen, for how many users? Without answers, nobody can say when the requirement has been met, so people disagree about it only after the software is built.

This topic distinguishes **what a system does** from **how well it does it**, and shows how to turn vague quality wishes into requirements that can be verified.

**Definition:** A functional property describes what a system does, its features and behaviours, while a non-functional property describes how well it does them, such as how fast, how secure, how available, or how easy to use, and good requirements state both in a form that can be verified.

<!--
IMAGE PROMPT  ->  generate as images/08_intro_functional_and_non_functional_properties.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A split illustration: a green checklist of features on the left labelled What the system does, and a gauge, shield, and clock on the right labelled How well it does it.

ON-IMAGE TEXT: show a short bold title "Functional and Non-Functional Properties" plus only these few labels, large and legible: What, How well, Measure. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Functional Requirements: What the System Does

Functional requirements describe features and behaviours: inputs, outputs, and business rules. They are phrased as things the system can do.

- A user can view the menu for any day in the current week.
- A user can rate a meal from 1 to 5 once after it has been served.
- A manager can download a weekly report of average ratings per dish.

If a functional requirement is not met, a user can say, "It does not do X."

## Non-Functional Requirements: How Well It Does It

Non-functional requirements describe qualities and constraints. If one is not met, the user says, "It does X, but badly." They are also called **quality attributes**, and they often shape a system's architecture more than any single feature does.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Category</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Vague version</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Measurable version</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Performance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The system should be fast</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">95% of menu requests complete within 300 ms with 2,000 simultaneous users</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Availability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The system should always work</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Available 99.9% of the time during meal hours, measured monthly</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The system should be secure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Passwords stored using a salted hash, accounts locked for 15 minutes after 5 failed logins</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Usability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The system should be easy to use</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A first-time user completes an order in under 60 seconds without help, in testing with 10 users</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scalability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">It should handle growth</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The system supports 20,000 daily users by adding servers, without redesign</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maintainability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The code should be clean</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A new developer can set up the project and run all tests within 30 minutes</td>
    </tr>
  </tbody>
</table>

The measurable column has numbers, conditions, and a way to check. Those three things turn an opinion into a requirement.

## Same Function, Different Quality

Imagine two ways to build the feature that reports a dish's average rating. Both produce exactly the same correct number, so both satisfy the same functional requirement.

In the first, the system fetches every stored rating for the dish across the network and computes the average itself. In the second, it asks the data store to compute the average and sends back a single number. With a few dozen ratings, nobody can tell them apart. With hundreds of thousands, the first moves a vast amount of data and slows down badly, while the second stays quick.

The two designs are identical in **what** they do and very different in **how well** they do it. Only a non-functional requirement, such as "the report must load within one second with 200,000 ratings," exposes the difference before users do.

## Trade-offs and Conflicts

Non-functional requirements often conflict, and the team must decide which wins. Very strong security (long passwords, frequent re-authentication) can harm usability. The fastest possible response may increase cost. Writing each non-functional requirement with a number lets stakeholders argue about the number instead of about adjectives.

## Constraints

Some non-functional requirements are **constraints** imposed from outside: the system must run on a particular platform, comply with a data-protection law, integrate with an existing system, or be delivered within a fixed budget. Constraints are not negotiable in the way preferences are, and they narrow the design options early.

## Your Turn: Classify and Sharpen

1. "Users can cancel an order up to 10 minutes before pickup." Functional or non-functional?
2. "Report generation must be quick." Rewrite it as a measurable requirement.
3. "Order data must survive a server crash." Which attribute does this concern?

Statement 1 is functional: it describes a behaviour and a rule. For statement 2, a good rewrite is: "The weekly ratings report is generated within 2 seconds for up to 100,000 ratings, measured on the production system." For statement 3, the attribute is dependability, specifically reliability and durability of data. A sound version might read: "No confirmed order is lost if a single server fails."

## Conclusion

A functional property describes what a system does, its features and behaviours, while a non-functional property describes how well it does them, such as how fast, how secure, how available, or how easy to use, and good requirements state both in a form that can be verified. Vague adjectives are not requirements until they carry a number and a method of checking.

This completes the chapter on how software work is shaped. The final chapter turns to the engineer's own habits of mind, tools, and skills, starting with how engineers think.
