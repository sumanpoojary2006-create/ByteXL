## Introduction

Every plan depends on estimates: how big is this piece of software, how much effort will it take, how long will it take, and what will it cost? Software estimation is notoriously difficult, because the product is new each time, requirements change, and productivity varies from person to person. Yet decisions must be made before the work is done, so estimates cannot be avoided. The skill lies in producing estimates that are honest about their uncertainty, in using several methods, and in refining them as knowledge grows.

This topic explains what estimates are, the difference between size, effort, and duration, the main estimation techniques, how to express uncertainty, and the common causes of poor estimates.

**Definition:** Software estimation is the prediction of the size of a piece of software, the effort needed to build it, and the time and cost that will result, based on available information, with an explicit acknowledgement of uncertainty.

<!--
IMAGE PROMPT  ->  generate as images/03_intro_software_size_and_effort_estimation.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A cone widening to the left labelled Uncertainty narrowing to the right toward Delivery, with four milestone markers along it, and a small set of three linked blocks above: Size, Effort, Duration.

ON-IMAGE TEXT: show a short bold title "Software Size and Effort Estimation" plus only these few labels, large and legible: The Cone of Uncertainty. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Estimates, Targets, and Commitments

Three different things are often confused.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Term</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Who sets it</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Estimate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A prediction of what is likely, based on analysis. It should be honest, whether or not it is welcome</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The people who will do the work</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Target</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A desired outcome, such as a deadline someone wishes to achieve</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The business</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Commitment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A promise to deliver something by a time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Made after comparing estimates, targets, and the ability to adjust scope or resources</td>
    </tr>
  </tbody>
</table>

Trouble begins when a target is presented as an estimate, or when an estimate is bargained down until it equals the target. An estimate that changes because someone dislikes it was not an estimate. The proper response to a gap between estimate and target is to change the plan (scope, resources, or schedule), not to change the prediction.

## Size, Effort, and Duration

These are related but different quantities.

- **Size:** how much there is to build, measured in lines of code, function points, features, user stories, or story points.
- **Effort:** how much work, measured in person-hours, person-days, or person-months.
- **Duration (elapsed time):** calendar time, depending on how many people work and how much of their time is available.
- **Cost:** mostly effort times pay rates, plus equipment, licences, and services.

A task of 20 person-days is not 4 calendar days because five people were assigned; coordination, dependencies, and the indivisibility of some work intervene. Estimating size first, then effort, then duration, gives a chain in which assumptions can be examined at each step.

## Measuring Size

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Measure</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strengths</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Weaknesses</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lines of code (LOC or KLOC)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Count of source lines</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simple; easy to count afterwards</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Depends on the language and style; cannot be known early; rewards verbose code</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Function points (FP)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Developed by Allan Albrecht at IBM in the 1970s. Counts the functionality visible to users: external inputs, outputs, inquiries, internal files, and external interfaces, each weighted by complexity, then adjusted by general system factors</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Independent of language; can be measured from requirements; standardised by international bodies</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Counting needs training; less suited to non-business systems; time consuming</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use case points</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Count of actors and use cases weighted by complexity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Based on use cases</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Depends on how use cases are written</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Story points (agile)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Relative size of a user story, compared to other stories, on a scale such as 1, 2, 3, 5, 8, 13</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quick; reflects complexity and uncertainty, not only time; calibrated per team</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not comparable between teams; sometimes misused as hours</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Feature or story count</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Number of items, assuming similar sizes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Very simple; works well when items are small and fairly uniform</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs reasonable uniformity</td>
    </tr>
  </tbody>
</table>

### Story Points and Velocity

Teams assign story points by comparing a new story to reference stories they have already completed. The sum of points completed per iteration is the team s **velocity.** The remaining points divided by velocity gives the number of iterations still needed. This turns estimation into empirical forecasting, based on the team's actual past output, rather than prediction in the abstract. Points are a tool for the team's planning; comparing velocities between teams or using them as a performance target destroys their value, because people simply inflate estimates.

## Estimation Techniques

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Technique</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strengths</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Weaknesses</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Expert judgement</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Experienced people estimate from their knowledge</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fast; uses tacit knowledge</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Biased and hard to defend; depends on the individual</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Analogy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Compare with similar past projects whose actual effort is known and adjust for differences</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Grounded in reality</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs good history and a truly similar project</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Decomposition (bottom-up)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Estimate each work package from the breakdown, then add them</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Detailed; exposes forgotten work; errors may cancel</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Time consuming; omits integration and overhead work; needs the breakdown to be complete</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Top-down</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Estimate the whole and divide it among parts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quick at early stage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">May hide detail</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Three-point estimation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">For each item give optimistic, most likely, and pessimistic values; combine them (a common weighting gives the expected value as the optimistic plus four times the most likely plus the pessimistic, divided by six)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Captures uncertainty</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs thought about extremes</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Wideband Delphi</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A facilitated group technique: members estimate independently, discuss the differences anonymously or openly, and re-estimate until they converge</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reduces bias and domination by one voice</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Takes time</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Planning poker</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An agile form of Delphi: each member selects a card with an estimate at the same time; differences are discussed and a new round follows</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quick; everyone contributes; reveals disagreements and hidden assumptions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs well-understood stories</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Parametric models</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Equations calibrated on historical data (the next topic)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Repeatable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Depend on calibration</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reference class forecasting</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Look at the distribution of outcomes for a class of similar projects and place this one within it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Counters optimism</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs a good data set</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Throughput-based forecasting</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Using the number of items a team finishes per week to project the delivery of the remainder, often with simulation of ranges</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Uses real data; no estimation of each item</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs a stable team and similar-sized items</td>
    </tr>
  </tbody>
</table>

No single technique is best. A recommended practice is to use **at least two different methods** and investigate the difference when they disagree.

## Expressing Uncertainty

A single number conveys false precision. An honest estimate comes with its uncertainty.

- **Ranges:** "between 8 and 14 weeks" tells more than "11 weeks."
- **Confidence levels:** say how likely it is to be met; a commitment at 50 per cent confidence will fail half the time.
- **Assumptions:** list what the estimate relies on, such as staff, scope, and external dependencies.
- **The cone of uncertainty,** described by Barry Boehm and refined by others, shows that early in a project estimates can be wrong by a factor of several in each direction, narrowing as the requirements, design, and construction become clearer. It also warns that the cone narrows only if decisions are made to reduce uncertainty; it does not narrow by itself with time.
- **Re-estimate** at milestones, as facts arrive.

## Why Estimates Go Wrong

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Cause</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Explanation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Counter-measure</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Optimism and the planning fallacy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">People imagine the best-case path and forget interruptions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use history and reference classes</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pressure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Estimates are reduced to please the sponsor</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Separate estimate from commitment; protect honesty</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Anchoring</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The first number mentioned dominates later thinking</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Estimate independently before sharing</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Forgotten work</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Testing, review, integration, deployment, meetings, rework</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use a checklist and a complete breakdown</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unclear requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The thing being estimated is not yet understood</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Estimate ranges; clarify scope; do discovery work first</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ignoring variation between people</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Experts may be several times faster than novices</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Estimate for the people who will really do the work</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Non-linear growth</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Larger systems need disproportionately more coordination</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Take account of size and team scale</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hidden assumptions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dependence on others, on environments, on decisions yet to be made</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Record and monitor assumptions</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No feedback</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Actual results never compared with the estimate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Track actuals and calibrate</td>
    </tr>
  </tbody>
</table>

## Good Practice

- **Estimate in a team,** so that different knowledge and viewpoints are included.
- **Estimate size by relative comparison** where possible; people compare better than they predict.
- **Break large items down;** small items are estimated more accurately and errors tend to offset.
- **Keep records** of estimates and actuals, and learn from the differences.
- **Include everything:** all the roles, all the activities, and the time lost to meetings and support.
- **Avoid false precision:** a figure to the nearest hour for a task months away is meaningless.
- **Estimate again when information changes,** and communicate the changes early.
- **Use "no estimates" thinking selectively:** some teams reduce the need to estimate by making work items small and uniform and forecasting from throughput. This works only when the work lends itself to it and when stakeholders accept forecasts.

<!--
IMAGE PROMPT  ->  generate as images/03_cone_of_uncertainty.png   (16:9 explanatory diagram, place here)

A funnel on its side: wide at Initial concept, narrowing through Requirements, Design, Construction to Delivered, with upper and lower bounds labelled 4x and 0.25x at the wide end narrowing to 1x. Below it, a row of three planning poker cards with different numbers and a discussion arrow.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Estimate Honestly

1. A manager asks for a single date for a project whose requirements are still vague. What do you give?
2. Three developers show planning-poker cards of 2, 3, and 13 for one story. What should happen next?
3. A task has optimistic, most likely, and pessimistic estimates of 4, 6, and 14 days. What is the three-point expected value?

For case 1, a range with assumptions and confidence, and a plan for narrowing it. For case 2, the person with 13 and the person with 2 explain their reasoning, which usually reveals a hidden assumption or risk, and the team votes again. For case 3, four plus four times six plus fourteen is 42, divided by six gives 7 days.

## Conclusion

Software estimation is the prediction of the size of a piece of software, the effort needed to build it, and the time and cost that will result, based on available information, with an explicit acknowledgement of uncertainty. Using several techniques, stating ranges and assumptions, and learning from actual results produce estimates that people can trust.

Some estimation methods package that learning into mathematical models. The next topic examines algorithmic cost models such as COCOMO.
