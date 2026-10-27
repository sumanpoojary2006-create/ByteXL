## Introduction

Software is rarely finished. The first release marks the beginning of a long phase in which users ask for improvements, defects appear, and the surrounding world, including laws, platforms, and other systems, keeps moving. Software that stops changing is usually software that has stopped being used. Understanding why software changes, and what kinds of change occur, is the foundation for planning and costing the phase of its life that follows delivery.

**Definition:** Software evolution is the continuing process of changing software after its first release to correct faults, adapt it to new environments, improve it, and extend it, and software maintenance is the set of activities that carry out those changes and keep the software useful.

<!--
IMAGE PROMPT  ->  generate as images/12_intro_why_software_changes.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A timeline of a software product from release through five years, with a stream of arrows of different colours entering from the sides labelled Bugs, New environment, New features, Regulation, Cleanup, and the product box growing and changing shape.

ON-IMAGE TEXT: show a short bold title "Why Software Changes" plus only these few labels, large and legible: Fix, Adapt, Improve, Prevent. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Reasons for Change

- **Faults are found.** Testing is never complete, and real use finds problems.
- **The environment changes.** Operating systems, browsers, devices, libraries, and partner systems are updated or retired.
- **Users and business needs change.** Requests for new features, new markets, and new ways of working.
- **Laws and standards change.** New regulation requires new behaviour.
- **Competition and technology advance,** creating pressure to add capabilities.
- **Understanding improves,** exposing design weaknesses that need correction.
- **Success brings growth,** with more users and data than expected.
- **Security threats evolve,** requiring continual updates.

## Lehman's Laws of Software Evolution

From studies of large systems beginning in the 1970s, Meir Lehman and colleagues formulated observations, called laws, about how software that is used in the real world behaves over time. The most widely cited can be summarised:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Law</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Continuing change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A system in use must be continually adapted, or it becomes progressively less useful</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Increasing complexity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">As a system changes, its complexity increases unless work is done to reduce it</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Self-regulation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The evolution of a large system follows regular, statistically predictable patterns</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Conservation of organisational stability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The average rate of work on a system tends to stay roughly constant over its life</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Conservation of familiarity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The amount of change in each release stays roughly constant, because teams must stay familiar with it</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Continuing growth</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Functional content must keep growing to maintain user satisfaction</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Declining quality</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality appears to decline unless the system is rigorously maintained and adapted</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Feedback system</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Evolution is a multi-level feedback process, which must be recognised to be improved</td>
    </tr>
  </tbody>
</table>

The practical lessons are that **change is the normal state**, that **structure decays unless effort is spent on it**, and that **growth is limited by the ability of the team to understand the system**.

## Types of Maintenance

E. Burton Swanson classified maintenance in 1976, and international standards for software maintenance, such as ISO/IEC/IEEE 14764, use a four-way division.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Type</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Corrective</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Repair faults found in operation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fix a calculation that gives the wrong total in a rare case</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Adaptive</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep the software working in a changed environment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Support a new operating system version or a changed interface of a partner service</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Perfective</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Improve performance or maintainability, or add features requested by users</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Add a new report; make a screen faster</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Preventive</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Improve the structure to prevent future problems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Refactor a fragile module; upgrade a library before it becomes unsupported</td>
    </tr>
  </tbody>
</table>

Early surveys found that the largest share of maintenance effort went to perfective work, meaning enhancements, and that corrective work, bug fixing, was a smaller share than many people assumed. The **common belief that maintenance is mainly fixing defects is therefore mistaken**: most maintenance is about continuing to extend and adapt.

## Maintenance Is Not a Lesser Activity

In many organisations maintenance is seen as less valuable than building new systems. This is a misconception. Maintenance includes substantial design and development, and often requires more skill than new development because of the need to understand an existing system and not to break it. A system that is maintained well delivers value for years, whereas one that is neglected loses value quickly.

## The Software Life Cycle After Release

A typical life has stages:

1. **Initial development:** the first version is built.
2. **Evolution:** rapid growth and change in response to users.
3. **Servicing (maintenance):** changes become limited to fixes and small adaptations as the architecture ages and knowledge fades.
4. **Phase-out:** the software is supported with no further changes, and users migrate.
5. **Close-down:** it is withdrawn.

This staged view, proposed by Rajlich and Bennett, shows that the type of work changes over time, and that decisions about modernisation and retirement belong in the plan from early on.

## Implications for Design and Process

- **Design for change** from the start, as Unit 5 argued.
- **Invest in tests,** documentation, and clean structure, which pay back in every later change.
- **Plan for maintenance** in budgets, since it is a large and continuing cost.
- **Keep knowledge alive** by sharing it, to survive staff turnover.
- **Decide deliberately** between continued evolution, modernisation, and retirement.

<!--
IMAGE PROMPT  ->  generate as images/02_maintenance_types_and_life_stages.png   (16:9 explanatory diagram, place here)

Left: a two-by-two of maintenance types, Corrective (fix faults), Adaptive (new environment), Perfective (new features and improvements), Preventive (restructure), with perfective drawn as the largest block. Right: a horizontal life line with stages Initial development, Evolution, Servicing, Phase-out, Close-down.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Classify the Maintenance

1. A bug that gives wrong totals for orders with exactly three items is repaired.
2. The system is changed to work with a new version of the payment provider interface.
3. A new report requested by managers is added.
4. A fragile module is restructured, with no change in what it does, to make future changes easier.

Change 1 is corrective. Change 2 is adaptive. Change 3 is perfective, as it adds a user-requested enhancement. Change 4 is preventive.

## Conclusion

Software evolution is the continuing process of changing software after its first release to correct faults, adapt it to new environments, improve it, and extend it, and software maintenance is the set of activities that carry out those changes and keep the software useful. Change is normal, mostly about improvement, and demands deliberate effort to keep the structure healthy.

Because maintenance continues for years, it accounts for much of the total cost of software. The next topic examines that cost.
