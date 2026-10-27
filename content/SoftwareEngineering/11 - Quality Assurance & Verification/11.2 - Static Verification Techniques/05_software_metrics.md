## Introduction

Managers want to know whether a project is on track, engineers want to know whether the code is improving, and customers want assurance of quality. Measurement is how such questions are answered with evidence instead of opinion. The physicist Lord Kelvin is quoted as saying that what cannot be measured cannot be improved. Software, however, is hard to measure, and many measures have been misused to judge individuals, to set targets that were then gamed, or to give an illusion of control. Good use of metrics requires knowing what each one means, what it cannot show, and what question it is meant to answer.

**Definition:** A software metric is a quantitative measure of some property of a software product, process, or project, used to understand, control, and improve the work, and it is meaningful only when tied to a goal and interpreted in context.

<!--
IMAGE PROMPT  ->  generate as images/05_intro_software_metrics.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A dashboard with several different gauges and trend lines: size, complexity, defects, delivery speed, each with a caution label Context needed, and a goal-question-metric tree beside it.

ON-IMAGE TEXT: show a short bold title "Software Metrics" plus only these few labels, large and legible: Goal, Question, Metric. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Start With the Question: Goal-Question-Metric

Victor Basili and colleagues proposed the **Goal-Question-Metric (GQM)** approach, which prevents measuring for its own sake.

1. Define a **goal**: for example, "improve the reliability of the order service."
2. Ask the **questions** that would tell whether the goal is met: "How many defects reach production? How quickly do we recover from failures?"
3. Choose the **metrics** that answer the questions: defect escape rate, mean time to restore.

A metric with no question and no goal behind it is a vanity measure.

## Kinds of Metrics

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Category</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it measures</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Product (code) metrics</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Properties of the software itself</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Size, complexity, coupling, cohesion, duplication, test coverage, maintainability</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Process metrics</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How the work is done</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lead time, cycle time, review turnaround, defect detection by phase</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Project metrics</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Progress against plan</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Effort, cost and schedule variance, velocity, burn-down</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality metrics</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Outcomes for users</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defect density, escape rate, availability, customer-reported problems</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Delivery metrics</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Software delivery performance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deployment frequency, lead time for changes, change failure rate, time to restore service (Unit 9)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">People and team metrics</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Experience of the team</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Satisfaction, workload, onboarding time</td>
    </tr>
  </tbody>
</table>

## Size Metrics

- **Lines of code (LOC)** is the simplest measure of size. It is easy to count and widely available but varies enormously between languages and styles, and is a poor measure of productivity or value. A saying often attributed to Bill Gates compares measuring programming progress by lines of code with measuring aircraft building progress by weight.
- **Function points,** proposed by Allan Albrecht at IBM in 1979, measure the functionality delivered from the user's viewpoint, counting inputs, outputs, queries, files, and interfaces. They are independent of language and used for estimation, although they take effort to calculate.
- **Story points** are relative sizes assigned by a team, as Unit 2 described, valid within one team only.

## Complexity Metrics

- **Cyclomatic complexity** (McCabe, 1976) counts independent paths through a function. Higher values mean harder to understand and more tests needed. Common guidance regards values above about 10 as a warning.
- **Cognitive complexity** adjusts for how hard code is for people to read, penalising nesting and breaks in flow.
- **Halstead metrics** (1977) derive measures of effort and difficulty from counts of operators and operands in code. They are seldom used directly now.
- **Nesting depth, function length, and parameter count** are simple indicators.

## Object-Oriented Design Metrics

Shyam Chidamber and Chris Kemerer proposed a widely studied suite in 1994.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Metric</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">High values suggest</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Weighted methods per class</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Total complexity of a class methods</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A class doing too much</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Depth of inheritance tree</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How far down a hierarchy a class sits</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fragile, hard-to-understand hierarchies</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Number of children</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How many classes inherit from it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Wide impact of change</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Coupling between objects</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How many other classes it is tied to</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tight coupling, as in Unit 5</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Response for a class</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How many operations can be triggered by a message</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Complexity, hard testing</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lack of cohesion of methods</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How little the methods share attributes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low cohesion; probably two responsibilities</td>
    </tr>
  </tbody>
</table>

Other design-level measures include **afferent and efferent coupling** (how many things depend on a module, and how many it depends on) and **instability** derived from them, which indicate how risky a module is to change.

## Maintainability and Technical Debt Measures

- **Maintainability index,** a composite of complexity, size, and other factors, proposed by Oman and Hagemeister in the early 1990s and variants since.
- **Code duplication:** the proportion of repeated code.
- **Test coverage** (with the cautions of Unit 10).
- **Estimated remediation time,** reported by some platforms as a measure of technical debt, as Unit 8 discussed.
- **Code churn:** how often files change; files that change often and have high complexity are hot spots.

## Quality and Defect Metrics

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Metric</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Definition</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Use</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defect density</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defects found per unit of size, such as per thousand lines or per function point</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Compare modules or releases; spot problem areas</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defect removal efficiency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The proportion of all defects that were found before release</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How good the process is at catching defects</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defect escape rate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The proportion of defects found after release</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The reverse view: what reached users</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defect arrival and fix rates over time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How many are found and fixed per period</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Whether the product is stabilising</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mean time to detect and to restore</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Speed of noticing and recovering from failures</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operational responsiveness</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Customer-reported problems and satisfaction</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What users experience</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ultimate outcomes</td>
    </tr>
  </tbody>
</table>

## Process and Productivity Measures

Measuring developer productivity is notoriously difficult. Counting output such as lines or commits per person invites distortion. More useful are measures of **flow** and **outcomes** at the level of the team and system, such as cycle time, lead time, and the delivery measures of Unit 9. A framework proposed in 2021 by Nicole Forsgren and colleagues, **SPACE**, argues that productivity has several dimensions that should be looked at together: **s**atisfaction and well-being, **p**erformance, **a**ctivity, **c**ommunication and collaboration, and **e**fficiency and flow.

## Properties of Good Metrics

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Property</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Relevant</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Linked to a goal and a decision</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Valid</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Measures what it claims to measure</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reliable and repeatable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Gives the same result when the same thing is measured again</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simple to understand</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">So that people trust and use it</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cheap to collect</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ideally automatic</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Actionable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Suggests what to do when it moves</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hard to game</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not easily improved without real improvement</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Timely</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Available when the decision is made</td>
    </tr>
  </tbody>
</table>

## How Metrics Go Wrong

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Pitfall</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Explanation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Remedy</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Goodhart law</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">When a measure becomes a target, it ceases to be a good measure; people optimise the number, not the goal</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use metrics to inform, not to reward; use several metrics together</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Measuring individuals</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ranking people by output creates fear, gaming, and neglect of teamwork</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Measure teams and systems; use data for learning</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Vanity metrics</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Impressive numbers that do not link to outcomes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tie each metric to a decision</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ignoring context</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Comparing teams or products with different circumstances</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Compare a team with its own history; supply context</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Absolute thresholds</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Treating a number as a verdict</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use thresholds as prompts to look, and look at trends</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Too many metrics</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dashboards nobody reads</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Choose a few that matter</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Measurement distorting the work</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Effort spent on reporting</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automate; keep it light</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Metrics used to blame</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Teams hide problems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep a blameless culture, as in Unit 9</td>
    </tr>
  </tbody>
</table>

## Using Metrics Well

1. **Begin with goals and questions.**
2. **Prefer trends to snapshots:** direction and change tell more than a single value.
3. **Use a small, balanced set,** covering speed, quality, and wellbeing, so that improving one at the expense of another is visible.
4. **Automate collection** from the repository, the pipeline, and the tracker.
5. **Review regularly with the team,** and let the team own them.
6. **Combine numbers with judgement** and conversation.
7. **Retire metrics** that no longer inform decisions.

<!--
IMAGE PROMPT  ->  generate as images/02_gqm_tree_and_metric_categories.png   (16:9 explanatory diagram, place here)

Left: a GQM tree with a goal Improve reliability at the top, two questions beneath it, and three metrics at the leaves. Right: six category tiles Product, Process, Project, Quality, Delivery, People, and a warning panel Goodhart's law: a measure used as a target stops being a good measure.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Choose or Criticise

1. A manager proposes to rank developers by the number of lines they write each week. What is wrong?
2. A team wants to know whether its testing is catching defects before release. Which metric helps?
3. A function has a cyclomatic complexity of 35. What does that suggest?

The proposal in case 1 rewards verbosity, ignores quality and teamwork, and will be gamed. In case 2, defect removal efficiency or the defect escape rate answers the question. In case 3, the function is very complex, hard to understand, and needs many tests; it is a candidate for splitting into smaller functions.

## Conclusion

A software metric is a quantitative measure of some property of a software product, process, or project, used to understand, control, and improve the work, and it is meaningful only when tied to a goal and interpreted in context. Metrics are useful servants for a team seeking to learn, and dangerous masters when turned into targets.

Metrics point to where defects are. The next chapter turns to the defects themselves: how to manage them, find their causes, and judge how reliable a system is.
