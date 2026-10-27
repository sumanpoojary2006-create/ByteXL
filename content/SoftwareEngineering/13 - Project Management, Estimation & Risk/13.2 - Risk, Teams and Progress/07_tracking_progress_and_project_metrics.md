## Introduction

A plan is a prediction; progress is evidence. Because software is invisible, it is easy to believe the project is on track when it is not, and a team that cannot see its position cannot correct its course. Tracking is the practice of measuring what has been achieved, comparing it with the plan, forecasting where the project will end up, and communicating the picture honestly. Good tracking measures real, finished outcomes, and bad tracking measures activity that merely looks like progress.

This topic describes what to track, the main charts and measures used in agile and traditional settings, earned value management, how to report status, and the dangers of measuring the wrong things.

**Definition:** Project tracking is the continuous measurement of progress, cost, quality, and risk against the plan, together with the forecasting and reporting needed to support timely decisions and corrective action.

<!--
IMAGE PROMPT  ->  generate as images/07_intro_tracking_progress_and_project_metrics.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Three small chart panels side by side: a burn-down line sloping down against a dashed ideal line, a bar chart of velocity per iteration, and an earned value chart with three curves labelled Planned, Earned, Actual.

ON-IMAGE TEXT: show a short bold title "Tracking Progress and Project Metrics" plus only these few labels, large and legible: Measure, Compare, Act. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Principles of Good Tracking

- **Measure outcomes, not effort.** Hours spent are not progress; working, tested functionality is.
- **Count only what is done.** An item is complete only when it meets the definition of done. Half-finished items count as zero, which prevents the familiar "ninety per cent done" illusion.
- **Make progress visible** to everyone, using boards and charts in shared spaces.
- **Use leading and lagging indicators.** Lagging measures show what happened; leading ones warn of what will happen.
- **Few, meaningful measures** are better than many.
- **Trends matter more than single values.**
- **Use measures to learn, not to punish,** or they will be falsified.
- **Decide actions in advance:** what will we do if the measure crosses a threshold?

## Measuring Work Done

### Done Means Done

A shared **definition of done** states what must be true before work counts: for example, built, reviewed, tested, integrated, documented, and deployable. Without it, teams carry hidden unfinished work that appears at the end.

### Task Boards

A board with columns for the stages of work (such as backlog, in progress, in review, in test, done) shows the state of every item. Boards reveal **bottlenecks,** which show up as columns where cards accumulate, and **blocked** items, which are flagged. Limits on work in progress, as Kanban prescribes, keep flow smooth.

## Agile Measures and Charts

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Measure</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it shows</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">How to read it</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Burn-down chart</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Remaining work (points or tasks) plotted over the iteration or release against an ideal line</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Above the ideal line means behind; flat segments show no completed work; upward jumps show added scope</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Burn-up chart</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Work completed rising over time, with a separate line for total scope</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clearer than burn-down when scope changes; the gap between lines shows work remaining</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Velocity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Amount of work (usually story points) completed per iteration</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Used for planning and forecasting; stable velocity makes forecasts reliable</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cumulative flow diagram</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stacked areas showing the number of items in each stage over time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Bands that widen reveal bottlenecks; parallel bands mean steady flow</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lead time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Time from request to delivery of an item</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shows how long customers wait</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cycle time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Time from start of work to completion</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shows how fast the team works on items; can be forecast statistically</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Throughput</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Number of items completed per unit time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Basis for forecasting without estimating each item</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Work in progress (WIP)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Number of items being worked on at once</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High WIP slows everything (Little law: average lead time equals WIP divided by throughput)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Escaped defects</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defects found after release</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality signal</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sprint goal achievement</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Whether the goal of the iteration was met</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Focus on outcomes</td>
    </tr>
  </tbody>
</table>

### Forecasting

Teams use velocity or throughput history to answer: "When will we have this much finished?" With a backlog of 120 points and a velocity of 20 points per iteration, six iterations remain. Because velocity varies, a range is better: using the best and worst recent velocities gives optimistic and pessimistic dates. Simulation methods apply the same idea statistically.

## Traditional Measures: Earned Value Management

Earned value management (EVM) integrates scope, schedule, and cost in a single framework, developed for large government projects in the 1960s. It uses three values at a given date.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Term</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Name</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">PV</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Planned value</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Budgeted cost of the work scheduled to be done by now</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">EV</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Earned value</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Budgeted cost of the work actually completed by now</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">AC</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Actual cost</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What has actually been spent so far</td>
    </tr>
  </tbody>
</table>

From these come indicators.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Indicator</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Formula</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Interpretation</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Schedule variance (SV)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">EV minus PV</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Negative means behind schedule</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost variance (CV)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">EV minus AC</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Negative means over budget</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Schedule performance index (SPI)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">EV divided by PV</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Below 1 means behind</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost performance index (CPI)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">EV divided by AC</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Below 1 means paying more than planned for work done</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Estimate at completion (EAC)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Budget at completion divided by CPI (one common form)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Forecast of the final cost</td>
    </tr>
  </tbody>
</table>

For example, a project planned to have completed work worth 100 units by now, has completed work worth 80, and has spent 90. SPI is 0.8 (behind) and CPI is about 0.89 (over cost). If the trend continues, the final cost will exceed the budget by about 12 per cent, a warning that arrives long before the end.

EVM depends on a good plan and on honest measurement of completion. In software, where completion is hard to judge for partly done work, it works best with small work packages credited only when done.

## Other Project Metrics

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Area</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Schedule</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Milestones met; slippage of key dates; percentage of scope delivered</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Spend against budget; cost per feature</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scope</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rate of change in requirements; backlog growth</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defect density and trends; defect age; test coverage and pass rates; escaped defects; reliability measures; customer-reported issues</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Delivery performance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deployment frequency; lead time for changes; change failure rate; time to restore service</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Technical health</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Build duration; flaky test rate; static analysis findings; dependency age; technical debt indicators</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Risk</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Number and exposure of open risks; risks closing; triggers hit</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">People</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Team satisfaction; turnover; overtime; onboarding time</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Customer and business</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Usage, adoption, satisfaction, revenue, and other outcomes (see topic 10)</td>
    </tr>
  </tbody>
</table>

## Reporting Status

Reports exist to support decisions, so they should be short, clear, and honest.

- **Audience:** executives want the headline, the risks, and the decisions needed; teams want detail.
- **A simple status** (green, amber, red) with a one-line reason, trend since last time, and **what will be done** about it. Amber and red should prompt action and support, not blame.
- **Content:** progress against milestones, key metrics, top risks and issues, changes in scope, upcoming decisions, and what is planned next.
- **Rhythm:** regular and predictable, such as weekly, with significant changes reported immediately.
- **Transparency:** bad news early is cheaper than bad news late. The **watermelon problem,** a report green on the outside and red inside, is a sign that people fear reporting reality.
- **Show the working product.** A demonstration at the end of each iteration is the best status report.

## Dangers of Metrics

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Danger</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Explanation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Goodhart law</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">When a measure becomes a target, it ceases to be a good measure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Targeting test coverage produces tests that assert nothing</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Vanity metrics</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Impressive numbers that do not guide decisions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Total lines of code written</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Measuring activity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hours, commits, and tickets closed measure busyness, not value</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rewarding the most commits</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Gaming</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">People adjust behaviour or data to look good</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inflating story points to raise velocity</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Comparing teams</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Contexts differ; comparison creates competition</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ranking teams by velocity</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Individual surveillance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Destroys trust and encourages short-term thinking</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tracking keystrokes</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ignoring context</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Numbers without explanation mislead</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A drop in velocity during a holiday week</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Too many measures</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Overload; nobody acts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A dashboard with fifty charts</td>
    </tr>
  </tbody>
</table>

## Taking Action

Tracking has value only if it leads to action. When the data show a problem:

- **Understand the cause** before reacting; discuss with the team.
- **Options** include re-planning, reducing scope, adding or reallocating resources (with the cautions of Brooks), removing blockers, improving process, and renegotiating the date.
- **Re-forecast** and share the updated expectation.
- **Record lessons** for the retrospective.

<!--
IMAGE PROMPT  ->  generate as images/07_burn_down_and_earned_value.png   (16:9 explanatory diagram, place here)

Left: burn-down chart with an ideal dashed line and an actual line above it, annotated with a scope increase step. Right: earned value chart with Planned, Earned, and Actual curves over time, with arrows marking schedule variance and cost variance.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Read the Signals

1. A burn-down chart rises in the middle of an iteration. What does it indicate?
2. EV is 60, PV is 75, and AC is 66. What are SPI and CPI, and what do they mean?
3. A manager wants to rank developers by the number of commits per week. Why is this a poor measure?

For case 1, work was added or re-estimated upward, a scope change. For case 2, SPI is 60 divided by 75, which is 0.8 (behind schedule), and CPI is 60 divided by 66, about 0.91 (over cost). For case 3, commits measure activity, not value or quality; it encourages many small meaningless commits and discourages collaboration and hard work.

## Conclusion

Project tracking is the continuous measurement of progress, cost, quality, and risk against the plan, together with the forecasting and reporting needed to support timely decisions and corrective action. Measuring finished work, reading trends, reporting honestly, and acting on what the numbers show keep a project steerable.

Tracking depends on honest conversation with the people who care about the outcome. The next chapter turns to those relationships, beginning with managing stakeholders and expectations.
