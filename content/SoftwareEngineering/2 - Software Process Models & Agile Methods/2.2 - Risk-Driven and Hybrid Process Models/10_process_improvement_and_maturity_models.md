## Introduction

Choosing a process is only a first step. Organisations that deliver software repeatedly want to know whether their way of working is getting better: fewer defects, more predictable schedules, less rework. Process improvement is the discipline of measuring how work is done, finding weaknesses, changing the process, and checking whether the change helped.

**Definition:** Process improvement is the continuing practice of measuring how an organisation develops software, identifying weaknesses, changing its process, and verifying the result, and maturity models describe stages of capability that help organisations judge where they stand and what to improve next.

<!--
IMAGE PROMPT  ->  generate as images/10_intro_process_improvement_and_maturity_models.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A five-step staircase from Initial at the bottom to Optimizing at the top, with a measuring gauge beside it and a circular improvement arrow.

ON-IMAGE TEXT: show a short bold title "Process Improvement and Maturity Models" plus only these few labels, large and legible: Measure, Improve, Mature. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Improvement Cycle

Most improvement approaches follow the same loop, often described as **Plan, Do, Check, Act**.

1. **Plan.** Identify a problem or goal, such as too many defects found after release, and decide on a change to the process.
2. **Do.** Try the change, usually on a small scale first.
3. **Check.** Measure the result and compare it with expectations.
4. **Act.** If it worked, standardise it. If not, learn why and try again.

The loop only works when there is **measurement**. Without data, an improvement is only an opinion.

## What to Measure

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example measures</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defects found per size of software, defects found by users after release, rework effort</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Predictability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Difference between estimated and actual effort and dates</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Speed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Time from an idea to delivery, time to fix defects</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Efficiency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Effort spent per feature, share of time lost to rework</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Satisfaction</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Customer feedback, team morale</td>
    </tr>
  </tbody>
</table>

Measures should be chosen carefully. Counting lines of code per day, for example, rewards verbosity and ignores quality. Good measures link to outcomes that matter.

## Maturity Models

A maturity model describes levels of increasing capability. The best known in software is the **Capability Maturity Model Integration (CMMI)**, developed at the Software Engineering Institute at Carnegie Mellon University from earlier work on software process maturity. Its staged form describes five levels.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Level</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Name</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Characteristic</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Initial</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Work is unpredictable and ad hoc; success depends on individuals</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Managed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Projects plan and track work, manage requirements, and keep records</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">3</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defined</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The organisation has standard, documented processes that projects tailor</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">4</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quantitatively managed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Process performance is measured and controlled with statistics</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">5</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Optimizing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The organisation continually improves its processes using measurement and innovation</td>
    </tr>
  </tbody>
</table>

The principle is that an organisation should **stabilise basics before optimising**: it is pointless to apply sophisticated statistical control to a process that is not even repeatable.

## Other Frameworks and Standards

- **ISO/IEC 12207** defines a standard set of life cycle processes for software.
- **ISO 9001** is a general quality management standard often used by software suppliers.
- **ISO/IEC 33000 family** (which replaced the earlier SPICE work) provides process assessment methods.
- **Agile retrospectives** are lightweight improvement loops, held at the end of each iteration.

## Criticism and Good Use

Maturity models have been criticised: pursuing a certificate can become the goal, producing paperwork instead of better software, and heavy models can be a poor fit for small or fast-moving teams. Used well, they provide a shared vocabulary and a sensible order of improvement. The healthy attitude is to improve in response to real problems, using models as guidance and not as a checklist.

<!--
IMAGE PROMPT  ->  generate as images/02_maturity_levels_staircase.png   (16:9 explanatory diagram, place here)

A five-step staircase with labels Initial, Managed, Defined, Quantitatively managed, Optimizing. Beside each step, a short plain-language caption: Ad hoc, Planned, Standard, Measured, Improving. A small figure climbs the stairs.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Place the Organisation

1. Success depends entirely on a few heroic individuals, and each project is run differently.
2. Each project plans and tracks its work, but practices differ from project to project.
3. The organisation has a documented standard process that every project tailors.

Organisation 1 is at level 1, Initial. Organisation 2 is at level 2, Managed. Organisation 3 is at level 3, Defined.

## Conclusion

Process improvement is the continuing practice of measuring how an organisation develops software, identifying weaknesses, changing its process, and verifying the result, and maturity models describe stages of capability that help organisations judge where they stand and what to improve next. Measurement and honest reflection matter more than any certificate.

This closes the study of process models as a family. The remaining chapters turn to agile methods, beginning with the values and principles that defined the movement.
