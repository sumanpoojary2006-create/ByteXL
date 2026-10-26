## Introduction

A requirement exists because someone needs it. If the wrong people are consulted, or an important group is forgotten, the resulting requirements will be incomplete however carefully they are written. Identifying stakeholders is therefore the first act of requirements work, and it is easy to do poorly: projects often discover a critical group, such as the people who will operate or regulate the system, only after the design is fixed.

**Definition:** A stakeholder is any person, group, or organisation that affects, or is affected by, a system, and stakeholder analysis is the practice of identifying those parties, understanding their interests and influence, and deciding how to involve each of them.

<!--
IMAGE PROMPT  ->  generate as images/02_intro_stakeholder_identification_and_analysis.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A central system icon surrounded by concentric rings of people icons: users close in, customers and operators next, regulators and partners at the outer ring, connected by lines of different thickness.

ON-IMAGE TEXT: show a short bold title "Stakeholder Identification and Analysis" plus only these few labels, large and legible: Who, Interest, Influence. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Types of Stakeholders

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Group</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Who they are</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What they typically care about</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">End users</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">People who use the system directly</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ease of use, speed, features that help their work</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Customers and sponsors</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Those who pay for or approve the project</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Value for money, schedule, business results</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operators and support staff</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">People who run, configure, and support the system</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reliability, monitoring, ease of maintenance</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Developers and testers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Those who build and check it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clear requirements, feasible scope, quality</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Managers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Those responsible for the organisation or project</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost, risk, alignment with strategy</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Regulators and legal bodies</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Authorities setting rules</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Compliance, safety, privacy</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Partners and suppliers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Organisations whose systems or services connect to yours</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stable interfaces, clear agreements</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Indirectly affected people</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Those affected without using the system</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Impact on their work, data, or lives</td>
    </tr>
  </tbody>
</table>

An important point is that users are not the only stakeholders, and the people who pay are often not the people who use. A system can satisfy its sponsor and fail its users, or the reverse.

## Finding Stakeholders

Several techniques help produce a complete list.

- **Use a checklist** of the groups above and ask who fits each.
- **Follow the data and the process.** Who creates, reads, changes, or depends on each piece of information?
- **Ask existing stakeholders** who else should be consulted, a method called snowballing.
- **Review the organisation chart and existing systems** for connected departments and users.
- **Think about the whole life cycle**: who installs, trains, operates, maintains, and eventually retires the system?

## Analysing Stakeholders

Not all stakeholders can be treated equally. A common tool is the **power and interest grid**, which classifies stakeholders by how much influence they have and how interested they are.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Group</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Power</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Interest</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical approach</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Key players</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Involve closely; agree decisions with them</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep satisfied</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Consult at important points; avoid surprises</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep informed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Update regularly; seek their feedback</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Monitor</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Minimal effort; watch for change</td>
    </tr>
  </tbody>
</table>

For each stakeholder, an analyst records goals, concerns, level of influence, expected involvement, and any known conflicts with other groups.

## Conflicting Interests

Stakeholders frequently want things that cannot all be had.

- Users want convenience; security staff want extra verification steps.
- Sponsors want an early release; testers want more time to check quality.
- One department wants data shared widely; another has privacy obligations.

Part of the analyst's job is to **surface these conflicts early** and bring them to a decision made with the right people, rather than silently choosing one side. A later topic on negotiation returns to this.

<!--
IMAGE PROMPT  ->  generate as images/02_power_interest_grid.png   (16:9 explanatory diagram, place here)

A two-by-two grid with Interest on the horizontal axis and Power on the vertical axis. Quadrants labelled Keep satisfied (top left), Key players (top right), Monitor (bottom left), Keep informed (bottom right), each with a few small people icons.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Representing Users

Often the real users cannot all be present. Analysts use **user representatives** and **personas**, which are fictional but research-based profiles of typical user types, with goals, skills, and frustrations. Personas help keep real people in mind, but they are summaries, and they should be checked against real users whenever possible.

## Your Turn: Place the Stakeholder

For a hospital appointment system, place each party on the power and interest grid.

1. The hospital director, who approves the budget and is closely following the project.
2. A national health regulator, who sets rules for patient data but is not following the project.
3. Reception staff, who will use the system daily but have no say in decisions.

The director is a key player (high power, high interest). The regulator belongs in keep satisfied (high power, low interest): they must be consulted on compliance and not surprised. Reception staff belong in keep informed (low power, high interest): their daily experience is vital input even though they do not decide.

## Conclusion

A stakeholder is any person, group, or organisation that affects, or is affected by, a system, and stakeholder analysis is the practice of identifying those parties, understanding their interests and influence, and deciding how to involve each of them. A requirement set is only as complete as the set of stakeholders consulted.

With the right people identified, the next question is how to draw out what they know. The next topic covers elicitation techniques.
