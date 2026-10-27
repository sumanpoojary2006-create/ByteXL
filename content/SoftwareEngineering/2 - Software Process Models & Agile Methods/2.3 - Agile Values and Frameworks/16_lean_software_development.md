## Introduction

Many of the ideas behind agile, including pull systems, continuous improvement, and eliminating wasted effort, come from lean manufacturing, especially the Toyota Production System. Mary and Tom Poppendieck applied these ideas to software, giving a set of principles that explain why agile practices work and that help evaluate any practice by its contribution to value.

**Definition:** Lean software development is an approach that applies lean manufacturing thinking to software by focusing on delivering value to the customer, eliminating waste, amplifying learning, and optimising the flow of work across the whole system.

<!--
IMAGE PROMPT  ->  generate as images/16_intro_lean_software_development.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A value stream flowing left to right through stages from Idea to Customer, with grey blocks labelled Waste being removed from the stream and a green arrow showing a shorter, faster path.

ON-IMAGE TEXT: show a short bold title "Lean Software Development" plus only these few labels, large and legible: Value, Waste, Flow. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Central Idea: Value and Waste

In lean thinking, every activity is judged by whether it adds **value** from the customer's point of view. Anything that consumes effort without adding value is **waste** (in Japanese, *muda*) and should be reduced or removed. Waste is not always obvious: a day spent waiting for an approval looks like inactivity, and a feature nobody uses looks like an achievement.

## The Seven Principles

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Principle</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning in software</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Eliminate waste</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Do not build, document, or process anything that does not serve the customer</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Amplify learning</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Software development is a learning process; use short cycles, experiments, and feedback to learn faster</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Decide as late as possible</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Delay irreversible decisions until you have the most information, while keeping options open</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deliver as fast as possible</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Short cycles speed feedback and reduce the cost of delay</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Empower the team</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Let the people doing the work make decisions; trust expertise</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Build integrity in</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Make quality part of the work from the start through testing, good design, and clear communication, rather than inspecting it in later</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">See the whole</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Optimise the entire value stream, not individual stages in isolation</td>
    </tr>
  </tbody>
</table>

## The Seven Wastes of Software

The Poppendiecks translated manufacturing's categories of waste into software terms.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Waste</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Partially done work</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Features started but not finished, code waiting to be tested or released</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Extra features</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Functionality nobody asked for or uses</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Relearning</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rediscovering what was already known because knowledge was not shared</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Handoffs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Passing work between people, losing context each time</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Task switching</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Moving between many tasks, losing focus each time</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Delays</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Waiting for approvals, environments, or decisions</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defects</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Faults that must be found and fixed, and the work that depends on them</td>
    </tr>
  </tbody>
</table>

## Value Stream Mapping

A practical lean technique is to draw a **value stream map**: lay out every step an idea passes through from request to delivery, record how long each step takes of actual work versus waiting, and look at where time is lost. In many organisations, the time an item spends waiting between steps is far greater than the time anyone spends working on it, so removing delays gives bigger gains than working faster.

<!--
IMAGE PROMPT  ->  generate as images/02_value_stream_map.png   (16:9 explanatory diagram, place here)

A value stream map: a row of stage boxes from Idea to Released (Analysis, Design, Build, Test, Release) with a timeline beneath. Under each box a green bar for Work time and a longer orange bar for Wait time between boxes. A summary shows total work time much smaller than total elapsed time. No code or code review imagery.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Lean and Other Agile Methods

Lean supplies the reasoning. Scrum's short sprints amplify learning and deliver quickly. XP's test-first practice builds integrity in. Kanban's WIP limits reduce partially done work and task switching. Seeing the common principles helps a team judge new practices and abandon ones that add only ceremony.

## Cautions

Lean language can be misused. "Eliminate waste" must not become an excuse to cut testing, reflection, or learning time, which are investments, not waste. Likewise, "decide as late as possible" does not mean avoiding decisions: it means not committing early to costly choices without evidence, while not delaying so long that the cost of delay exceeds the benefit.

## Your Turn: Name the Waste

1. A team builds an elaborate administration screen that no customer ever opens.
2. A change waits two weeks for approval from a committee that meets monthly.
3. A developer works on six tasks at once and progresses on none.
4. A team writes and tests code that is never merged because priorities changed.

Situation 1 is extra features. Situation 2 is delay. Situation 3 is task switching. Situation 4 is partially done work.

## Conclusion

Lean software development is an approach that applies lean manufacturing thinking to software by focusing on delivering value to the customer, eliminating waste, amplifying learning, and optimising the flow of work across the whole system. It explains why many agile practices work, and gives a test for any practice: does it add value for the customer?

The frameworks are now complete. The final chapter turns to the daily craft of agile work, beginning with how requirements are expressed as user stories and managed in a backlog.
