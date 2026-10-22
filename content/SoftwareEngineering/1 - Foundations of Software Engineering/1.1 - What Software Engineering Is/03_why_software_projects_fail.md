## Introduction

CampusConnect's first big release was due on the first of July, when new students arrive. It shipped on the twenty-sixth. By then, two of the twelve colleges had asked to postpone, the payment integration still double-charged some students, and the team was exhausted.

Vikram did not hold a meeting to find someone to blame. He held a **postmortem**, a structured review in which the team writes down what happened, why, and what will change. He opened it with a warning: "If our answer is 'someone wrote a bug,' we have not understood anything yet. Bugs are the last link in the chain."

To prove his point, he walked the team through four famous failures where a single line of code was blamed in the headlines, but the real causes were far broader.

**Definition:** A software project fails when it is delivered late, over budget, with serious faults, or not at all, and the root cause is almost never a single bug but a chain of weak decisions about requirements, design, testing, communication, and risk.

<!--
IMAGE PROMPT  ->  generate as images/03_intro_why_software_projects_fail.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Use the named person, setting, and engineering problem from the Introduction.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Vikram stands at a whiteboard titled Postmortem with a long chain of connected links, one of them cracked, while the CampusConnect team sits around a table looking at a calendar with the first of July circled.

ON-IMAGE TEXT: show a short bold title "Why Software Projects Fail" plus only these few labels, large and legible: Chain, Postmortem, Late. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Case 1: Ariane 5, 1996

On 4 June 1996 the first Ariane 5 rocket left its launch pad in French Guiana. About 37 seconds later it veered off course and destroyed itself, along with its satellite cargo, a loss commonly estimated at around 370 million US dollars.

The immediate cause was a number conversion. The guidance software, reused from the older Ariane 4 rocket, tried to convert a 64-bit floating point value (a measure of horizontal velocity) into a 16-bit integer. Ariane 5 was faster, so the value was too large for 16 bits, the conversion overflowed, and the guidance computers shut down.

The root causes were larger: software was **reused without being re-validated** against the new rocket's different flight conditions, and a calculation that was no longer needed after liftoff kept running anyway.

## Case 2: Mars Climate Orbiter, 1999

NASA's Mars Climate Orbiter was lost in September 1999 as it approached Mars. One team's software produced thruster data in pound-force seconds (an imperial unit), while the team receiving the data expected newton seconds (a metric unit). The spacecraft's course was wrong by enough to bring it too close to the planet.

The root cause was an **interface mismatch between teams**: the unit of the data was not stated and checked at the boundary between two systems.

## Case 3: Knight Capital, 2012

On 1 August 2012 a trading firm called Knight Capital deployed new software to its servers. A deployment step missed one of eight servers, leaving old code that had been repurposed running there. In roughly 45 minutes the firm made a flood of unintended trades and lost about 440 million US dollars, close to the company's entire value.

The root causes were a **manual, unchecked deployment process**, old code left in the system, and no quick way to stop the damage once it started.

## Case 4: Therac-25, 1985 to 1987

Therac-25 was a radiation therapy machine. In at least six accidents, patients received massive overdoses, and some died. Investigators found software errors, including a **race condition** that could occur when an operator edited treatment settings quickly. They also found that hardware safety interlocks from earlier models had been removed on the assumption that the software was reliable enough to replace them.

The root causes were an **overconfident trust in software**, weak testing, and a failure to take early accident reports seriously.

<!--
IMAGE PROMPT  ->  generate as images/04_four_famous_failures.png   (16:9 explanatory diagram, place here)

Four panels side by side: a rocket labelled Ariane 5, a spacecraft labelled Mars Orbiter, a trading screen labelled Knight Capital, and a medical machine labelled Therac-25. Under each panel a short root cause label: Reuse, Units, Deployment, Race.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Common Root Causes

Setting these cases beside everyday project failures, the same causes keep appearing.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Root cause</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it looks like</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example from the cases</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unclear or changing requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Team builds the wrong thing, or the target keeps moving</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Everyday projects, and Ariane 5 conditions not re-checked</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Poor communication between teams</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Assumptions differ across a boundary</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mars Climate Orbiter units</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inadequate testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Failures only meet real users</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ariane 5, Therac-25</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unrealistic estimates and schedules</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deadline set before the work is understood</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">CampusConnect missing 1 July</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unmanaged risk</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nobody asks "what if this goes wrong?"</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Knight Capital had no emergency stop</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Weak process and automation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Manual steps that humans eventually miss</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Knight Capital deployment</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Overconfidence in software</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Removing other safeguards</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Therac-25 interlocks</td>
    </tr>
  </tbody>
</table>

## Failure Is a Chain, Not a Single Event

Safety engineers use the image of slices of Swiss cheese. Each safeguard (a review, a test, a monitor, a manual check) has holes. A disaster happens only when the holes in several slices line up. This is good news: strengthening any one layer can break the chain, so teams improve by adding independent defences, not by hoping to write perfect code.

## Your Turn: Find the Root Cause

For each statement, name the category of root cause from the table above.

1. CampusConnect's payment feature double-charged students because the payment partner counted amounts in paise and the app sent rupees.
2. The team promised the July release date in March, before any design work had started.
3. A developer manually copied files to the production server and forgot one folder.

Statement 1 is poor communication across a boundary: the unit was never agreed and checked, the same family as Mars Climate Orbiter. Statement 2 is an unrealistic estimate, because the date was committed to before the work was understood. Statement 3 is weak process and automation: a manual step relied on human memory, which is exactly what failed at Knight Capital.

## Conclusion

A software project fails when it is delivered late, over budget, with serious faults, or not at all, and the root cause is almost never a single bug but a chain of weak decisions about requirements, design, testing, communication, and risk. Postmortems exist to find the chain, not the culprit.

With a realistic picture of what can go wrong, Ananya can now ask a better question about her own work: what kind of system is she building, and how much rigour does it deserve? A mess-menu app and a radiation machine are both "software," but they are not the same kind of problem.
