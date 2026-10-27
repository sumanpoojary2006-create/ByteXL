## Introduction

Scrum and XP organise work in fixed-length iterations. Many teams, such as those handling support requests, operations, or a steady stream of small changes, do not work well in that rhythm because work arrives unpredictably and cannot be planned for two weeks ahead. Kanban is a method that manages work as a continuous **flow** through stages, without fixed sprints.

**Definition:** Kanban is a method for managing knowledge work by visualising it on a board of workflow stages, limiting the amount of work in progress, and measuring and improving the flow of items from start to finish.

<!--
IMAGE PROMPT  ->  generate as images/15_intro_kanban_and_flow_based_work.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A Kanban board with five stage columns from left to right: Backlog, To Do, In Progress, Review, Done. Work cards sit in each column, the In Progress column shows a work-in-progress limit of three, and arrows show cards moving from left to right.

ON-IMAGE TEXT: show a short bold title "Kanban and Flow-Based Work" plus only these few labels, large and legible: Stages, WIP, Flow. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Origins

The word "kanban" is Japanese for "signboard" or "card". The idea comes from Toyota's production system, developed by Taiichi Ohno, where cards signalled when more parts were needed so that no stage produced more than the next could use. David J. Anderson adapted the approach for software and knowledge work in the 2000s.

## The Board: Making Work Visible

The central tool is a board with **columns that represent the stages of the team's real workflow**. Each work item is a card that moves from left to right as it progresses. The stages are defined by the team's own process. A common example is Backlog, To Do, In Progress, Review, and Done, and many teams add stages such as Testing, Blocked, or Ready for Release. Ticket tracking tools used by teams show the same idea as a board with status columns.

The board shows, at a glance:

- what work exists and what state each item is in
- who is working on what
- where work is piling up
- which items are blocked

## Limiting Work in Progress

The key rule that distinguishes Kanban is a **work-in-progress (WIP) limit**: a maximum number of items allowed in a stage at one time. If the "In Progress" column has a limit of three and already holds three cards, nobody may start a fourth. Instead, people help finish something or unblock it.

Why this helps:

- **Less multitasking.** Switching between many tasks wastes time and slows everything.
- **Faster completion.** Items finish sooner when fewer compete for attention.
- **Bottlenecks surface.** When a stage is full, the queue behind it is exposed, such as work waiting for review.
- **Pull, not push.** New work is pulled into a stage only when there is capacity, instead of being pushed in regardless.

<!--
IMAGE PROMPT  ->  generate as images/02_kanban_board_stages_wip.png   (16:9 explanatory diagram, place here)

A clean Kanban board with columns left to right: Backlog, To Do, In Progress (WIP limit 3), Review (WIP limit 2), Done. Cards in each column; the Review column is full and highlighted orange to show a bottleneck, with a note Finish before starting. Arrows show cards flowing left to right. No code or code review imagery.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Core Practices

1. **Visualise the workflow** on a board.
2. **Limit work in progress** at each stage.
3. **Manage flow**, watching how items move and removing delays.
4. **Make policies explicit**, such as what "ready for review" means.
5. **Implement feedback loops**, including regular reviews of the board and the process.
6. **Improve collaboratively**, evolving the system through small experiments.

## Measuring Flow

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Measure</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lead time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Total time from a request arriving until it is delivered, as the customer experiences it</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cycle time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Time from when work starts on an item until it is finished</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Throughput</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Number of items completed per unit of time</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Work in progress</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Number of items currently started but not finished</td>
    </tr>
  </tbody>
</table>

These are related by a simple rule known as Little's Law: on average, **cycle time equals work in progress divided by throughput**. If a team has twelve items in progress and finishes four per week, an item takes about three weeks on average. To shorten cycle time, reduce work in progress or increase throughput. This explains why limiting WIP makes work flow faster.

## Kanban and Scrum Compared

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Scrum</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Kanban</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cadence</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fixed-length sprints</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Continuous flow</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Roles</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Product Owner, Scrum Master, Developers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No prescribed roles</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Limit on work</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sprint scope</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">WIP limits per stage</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Change during the cycle</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Normally not added during a sprint</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can be added any time capacity allows</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Main measures</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Velocity, sprint burndown</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lead time, cycle time, throughput</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Best fit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Product development with plannable work</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Support, operations, mixed or unpredictable work</td>
    </tr>
  </tbody>
</table>

Many teams combine them, sometimes called Scrumban, using sprints for planning while visualising the flow and applying WIP limits.

## Your Turn: Read the Board

A team's board shows: To Do has 5 items, In Progress has 3 (limit 3), Review has 6 (limit 3), Done has 20.

1. Where is the bottleneck?
2. What should the developers do instead of starting new work?
3. A team has 15 items in progress and completes 5 per week. What is the average cycle time?

The bottleneck is Review, which is double its limit. Rather than start new work, developers should help review and clear items. The average cycle time is 15 divided by 5, which is 3 weeks.

## Conclusion

Kanban is a method for managing knowledge work by visualising it on a board of workflow stages, limiting the amount of work in progress, and measuring and improving the flow of items from start to finish. It reveals bottlenecks and encourages finishing over starting.

Kanban's focus on flow and waste connects to a wider body of thinking taken from manufacturing. The next topic presents lean software development.
