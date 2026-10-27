## Introduction

Finding a defect and fixing it solves one problem. Understanding why it occurred, and why it was not found sooner, can prevent dozens. The first activity is defect management: recording, classifying, prioritising, and tracking defects so that none is lost and the team can see the pattern. The second is root-cause analysis: asking what allowed the defect to enter the product and to escape detection, and changing the process so it is less likely to happen again. Together they turn the stream of bugs from a nuisance into a source of improvement.

**Definition:** Defect management is the process of recording, classifying, prioritising, resolving, and tracking defects through their life cycle, and root-cause analysis is the structured investigation of why a defect occurred and escaped detection, in order to remove the underlying causes and prevent similar defects.

<!--
IMAGE PROMPT  ->  generate as images/06_intro_defect_management_and_root_cause_analysis.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A funnel catching defects from the left, a Pareto bar chart labelled 80 percent of defects from 20 percent of causes, and a fishbone diagram with branches Process, People, Tools, Requirements, Environment, Design leading to a head labelled Defect.

ON-IMAGE TEXT: show a short bold title "Defect Management and Root-Cause Analysis" plus only these few labels, large and legible: Track, Classify, Prevent. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Defect Life Cycle

Unit 9 and Unit 10 described the states a report passes through: new, confirmed, assigned, in progress, fixed, verified, and closed, with side exits such as duplicate, cannot reproduce, and will not fix, and the possibility of reopening. A defect management process makes the rules explicit: who may change a state, what evidence is needed, how severity and priority are set, and how quickly each class of defect must be addressed.

## Classifying Defects

Classification turns individual defects into data that can be analysed.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Attribute</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Question answered</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples of values</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Severity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How bad is the effect?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Critical, major, minor, trivial</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Priority</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How soon must it be fixed?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Immediate, high, medium, low</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Type (nature)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What kind of mistake?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Logic, interface, data handling, calculation, concurrency, configuration, documentation, performance, security</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Where found</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">In which component or feature?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ordering, payments, reporting</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Phase injected</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">At which stage was it introduced?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requirements, design, coding, build, deployment</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Phase detected</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">At which stage was it found?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Review, unit test, system test, acceptance, production</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Detection method</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How was it found?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inspection, automated test, exploratory testing, customer report, monitoring</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Root cause category</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Why did it happen?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unclear requirement, misunderstanding, missing test, rushed work, tool fault</td>
    </tr>
  </tbody>
</table>

IBM researchers led by Ram Chillarege developed **Orthogonal Defect Classification** in the early 1990s, a scheme that classifies defects by attributes such as the type of fix and the activity that found them, so that their distribution reveals which parts of the process are weak.

The pair **phase injected** and **phase detected** is especially valuable. A requirement mistake found in production, many phases after it was introduced, is expensive. The gap between injection and detection measures how well earlier checks work.

## Measuring Defects

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Measure</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Definition</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it shows</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defect density</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defects per unit of size</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Relative quality of components or releases</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defect removal efficiency (DRE)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defects found before release divided by total defects found before and after release</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How well the process filters defects</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Phase containment effectiveness</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The proportion of defects caught in the phase where they were introduced</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How early defects are caught</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defect arrival rate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">New defects found per period</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Whether testing is still finding problems or the product is stabilising</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defect fix rate and age</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How fast defects are closed; how long they stay open</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Responsiveness and backlog health</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Escape rate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defects found by users, as a proportion of all</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What reaches customers</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reopen rate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fixes that did not hold</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality of fixes and verification</td>
    </tr>
  </tbody>
</table>

A worked example: if testing and review find 90 defects before release and users report 10 more in the first months, the total is 100, and DRE is 90 divided by 100, which is 90 percent.

### Defect Clustering

Defects are not spread evenly. Studies repeatedly find that a small proportion of modules contain a large share of the defects, an application of the **Pareto principle**, popularly the 80/20 rule. Defect data identifies these modules so that extra attention, in review, testing, or redesign, goes where it is most useful.

## Why Root Cause Analysis

Fixing a defect repairs one instance. If the cause is a misunderstood rule, a missing check in the review process, or a confusing interface, the same cause will produce more defects. Root-cause analysis (RCA) looks for such causes. It is applied to:

- **Serious defects** and failures in production.
- **Recurring types** of defect, identified from the data.
- **Escapes:** defects that should have been caught earlier.
- **Near misses** that did not do harm but could have.

The postmortems of Unit 9 are RCA at the scale of an incident.

## Techniques

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Technique</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">How it works</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Good for</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Five whys</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ask "why?" repeatedly, usually about five times, each answer becoming the subject of the next question, until a cause is found that can be acted on</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simple, quick analysis</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fishbone (Ishikawa) diagram</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A diagram with the problem at the head and branches for categories of cause, such as people, process, tools, requirements, design, and environment, to be filled in through brainstorming</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Structuring many possible causes</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pareto analysis</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rank causes or types by frequency to find the few that account for most defects</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Choosing where to act</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fault tree analysis</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Work backward from the failure through combinations of events that could cause it, using logical and/or links</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Complex failures, safety analysis</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Timeline analysis</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reconstruct what happened and when</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Incidents</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Change analysis</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Compare what changed between working and failing states</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Regressions</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Barrier analysis</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ask which defences should have caught the defect, and why they failed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Escapes</td>
    </tr>
  </tbody>
</table>

### An Example: The Five Whys

Defect: customers with exactly ten items receive no discount.

1. **Why?** The code applies the discount only when the quantity is greater than ten, not when it is exactly ten.
2. **Why was the wrong comparison written?** The requirement said "ten or more," but the developer read it as "more than ten."
3. **Why was it not noticed in review?** The reviewer saw no tests of the boundary and did not check the requirement.
4. **Why was there no boundary test?** The team has no habit of designing tests for boundaries.
5. **Why not?** Test design techniques are not part of the team's guidance.

The fix of the code is a single line. The **root-cause actions** are to add boundary tests for the discount rule, to add boundary checks to the review checklist, and to teach the boundary value technique, which prevents a whole class of similar defects.

The method has limits: it can follow one chain of reasoning and miss others, and can end at a person, which is the wrong place to stop. Good analysis considers **several contributing factors** and looks for causes in process and system, not blame.

## From Analysis to Prevention

RCA is useful only if it leads to **action**.

- **Corrective action** fixes the existing defect.
- **Preventive action** changes the process, tools, or training so that similar defects are less likely: a new checklist item, a static analysis rule, an extra test, a clearer template, a changed design, or training.
- Actions need **owners, deadlines, and follow-up**, and their effect should be checked in later data.
- Share **lessons learned** across teams.

## Making It Work

- **Blameless culture.** People report defects and discuss causes frankly only if they will not be punished.
- **Record data consistently,** with lightweight forms and tool support.
- **Analyse regularly,** such as at the end of each release or iteration, in retrospectives.
- **Focus on the vital few,** applying RCA to the defects and categories with the biggest impact.
- **Keep it proportionate.** Not every bug needs a full analysis.
- **Close the loop:** check that defect rates fall after preventive action.

<!--
IMAGE PROMPT  ->  generate as images/02_phase_injected_vs_detected_and_five_whys.png   (16:9 explanatory diagram, place here)

Left: a matrix with phases injected on rows and phases detected on columns, diagonal cells in green (caught in the same phase) and far off-diagonal cells in red (late detection). Right: a five whys chain of boxes from Defect to Root cause to Preventive action.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Analyse the Defects

1. Testing and review find 72 defects before release, and customers report 8 more. What is the defect removal efficiency?
2. Most of the defects in a release come from two of twenty modules. What principle is this, and what should the team do?
3. After fixing a defect, a team does nothing to change its process. What has been missed?

For case 1 the total is 80 and DRE is 72 divided by 80, which is 90 percent. Case 2 is defect clustering, an example of the Pareto principle; extra review, testing, or redesign should focus on those modules. In case 3, the team has missed the preventive action that root-cause analysis would identify.

## Conclusion

Defect management is the process of recording, classifying, prioritising, resolving, and tracking defects through their life cycle, and root-cause analysis is the structured investigation of why a defect occurred and escaped detection, in order to remove the underlying causes and prevent similar defects. Good data and honest analysis turn defects into the most reliable teacher a team has.

Defects matter because they cause failures, and users care about how often those occur and how long they last. The next topic introduces the ideas of reliability and availability.
