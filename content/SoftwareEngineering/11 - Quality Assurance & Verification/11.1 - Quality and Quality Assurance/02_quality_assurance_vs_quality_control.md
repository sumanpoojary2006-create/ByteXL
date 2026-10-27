## Introduction

The terms quality assurance and quality control are used loosely, and even job advertisements confuse them: a "QA engineer" is often a tester. The distinction is nevertheless important, because it separates two different ways of pursuing quality. One aims to **prevent** defects by improving how software is made. The other aims to **detect** defects in what has been made. A team that practises only the second spends its life finding and fixing mistakes that a better process would never have produced.

**Definition:** Quality assurance (QA) is the set of planned, systematic activities that give confidence that the development process will produce software meeting its quality requirements, by preventing defects, while quality control (QC) is the set of activities that examine the actual product to detect defects, such as testing and inspection, and quality management coordinates both.

<!--
IMAGE PROMPT  ->  generate as images/02_intro_quality_assurance_vs_quality_control.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A factory line: above the line a team improving the process with blueprints and checklists labelled Quality assurance (prevent), and at the end of the line an inspector examining finished products labelled Quality control (detect).

ON-IMAGE TEXT: show a short bold title "Quality Assurance versus Quality Control" plus only these few labels, large and legible: Prevent, Detect, Improve. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Distinction

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Quality assurance</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Quality control</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Focus</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The process of making the product</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The product itself</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Aim</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prevent defects; build confidence in the process</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Find and correct defects</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Timing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Throughout, proactive</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">After something is made, reactive</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Question asked</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Are we doing the right things, in the right way?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does this work product meet the requirements?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Typical activities</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defining standards and methods; process audits; training; reviews of process compliance; defect prevention; metrics for improvement</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Testing; inspections of work products; static analysis; acceptance checks</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Responsibility</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Everyone, with coordination by a quality function</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Developers, testers, reviewers</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Orientation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Verification of the process</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Verification of the product</td>
    </tr>
  </tbody>
</table>

In the vocabulary of the previous unit, **testing is a quality control activity.** Quality assurance is the larger discipline of which good testing practice is only one outcome.

## Quality Management

The two sit under **quality management**, which in standards such as ISO 9000 and ISO 9001 comprises four elements.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Element</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality planning</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Setting quality objectives and the processes and resources needed to meet them</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality assurance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Providing confidence that requirements will be fulfilled</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality control</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Examining outputs to confirm that requirements are fulfilled</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality improvement</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Increasing the ability to fulfil requirements, continually</td>
    </tr>
  </tbody>
</table>

## Quality Assurance Activities

- **Define standards and procedures:** coding standards, review procedures, templates, and the development process itself.
- **Plan quality:** a quality plan or test strategy stating the quality goals, the activities, and the responsibilities.
- **Train and support** people in the methods.
- **Review and audit processes:** checking whether the agreed process is actually followed and whether it works. Audits compare practice with the documented process and with standards.
- **Collect and analyse measures:** defect rates, review effectiveness, delivery measures, to learn and improve.
- **Manage defects and root causes:** analysing defects to remove the causes, not only the symptoms, as a later topic describes.
- **Control change and configuration,** as in Unit 8.
- **Select and qualify tools.**
- **Prevent defects** by technical means: clear requirements, design reviews, automation, and static analysis in the pipeline.
- **Run retrospectives and process improvement.**

## Quality Control Activities

- **Testing** at all levels, as Unit 10 described.
- **Inspections and reviews** of work products, covered in the next topic.
- **Static analysis** of code.
- **Acceptance checks** against criteria.
- **Quality gates:** checks in a pipeline that a change must pass before progressing.
- **Production monitoring** that detects failures in operation.

## Standards for Software Quality

Several international standards provide frameworks.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Standard or model</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Concern</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">ISO 9001</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">General requirements for a quality management system, used across industries and by many software suppliers</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">ISO/IEC/IEEE 12207</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Life cycle processes for software</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">ISO/IEC/IEEE 29119</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Software testing processes, documentation, and techniques</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">IEEE 730</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Software quality assurance processes</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">ISO/IEC 25000 family (SQuaRE)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality requirements and evaluation</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">CMMI</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Process maturity, described in Unit 2</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Domain standards</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Safety-critical, medical, automotive, and similar standards, covered later in this unit</td>
    </tr>
  </tbody>
</table>

Standards give a common vocabulary and can be required by customers and regulators, but they must be applied with judgement: following a process on paper does not guarantee a good product.

## Quality in Agile and DevOps Teams

In traditional organisations, a separate QA group sat between development and release and acted as a gatekeeper. Modern teams spread quality across everyone.

- **Whole-team responsibility:** developers write tests and review each other's work; testers contribute to requirements and design as well as to testing.
- **Shift left:** quality activities move earlier, to requirements, design, and coding, where defects are cheapest to prevent.
- **Automation of quality gates** in the pipeline, giving every change the same checks.
- **Definition of Done** that includes quality criteria, as Unit 2 described.
- **Quality coaching:** specialists help teams improve their practices instead of inspecting their output.
- **Shift right:** monitoring and learning from production, covered in Unit 9.

Specialist roles remain valuable. **Quality engineers** and **software development engineers in test (SDETs)** design test strategy and automation, and bring a questioning mindset and expertise in risk, but quality remains **the team's responsibility.**

## A Quality Plan in Outline

A short quality plan for a project might state:

1. The **quality goals**, drawn from the quality requirements.
2. The **standards and practices** to be followed.
3. The **review and test activities** at each stage and their entry and exit criteria.
4. The **tools and automation** in the pipeline and the quality gates.
5. The **measures** to be collected and reviewed.
6. **Roles and responsibilities.**
7. **Risks** to quality and the responses.
8. How **defects** will be tracked and analysed.

## Common Problems

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Explanation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Remedy</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality as a final phase</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defects found late, costing most</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Build quality in: reviews, tests, and automation throughout</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">QA as gatekeeper</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Developers hand quality over to a separate group</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Share responsibility; use the quality function for coaching and strategy</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Process for its own sake</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Documents and audits that satisfy a standard but change nothing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tie process to outcomes; remove what does not help</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Measuring the wrong things</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Counting activity, not quality</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Choose measures that reflect results</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Neglecting prevention</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">All effort goes to finding defects</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Invest in root-cause analysis and defect prevention</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No management support</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality sacrificed to schedule</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Make quality goals explicit and visible; agree trade-offs openly</td>
    </tr>
  </tbody>
</table>

<!--
IMAGE PROMPT  ->  generate as images/02_qa_prevents_qc_detects.png   (16:9 explanatory diagram, place here)

A left-to-right development flow Requirements, Design, Code, Build, Release. Above the flow, green shield icons labelled QA: standards, reviews, training, process audits, prevention. Below the flow, magnifier icons labelled QC: testing, inspection, static analysis, quality gates, detection. A feedback loop labelled Improve the process joins them.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: QA or QC?

1. A team defines and trains everyone in a new review procedure for designs.
2. A tester runs the regression suite on a release candidate.
3. An audit checks whether projects actually follow the agreed development process.
4. A pipeline step blocks any change whose static analysis reports a serious problem.

Activity 1 is quality assurance, since it improves the process and aims at prevention. Activity 2 is quality control, detecting defects in the product. Activity 3 is quality assurance, a process audit. Activity 4 is a quality control gate in the pipeline, although it is part of a prevention-minded process.

## Conclusion

Quality assurance (QA) is the set of planned, systematic activities that give confidence that the development process will produce software meeting its quality requirements, by preventing defects, while quality control (QC) is the set of activities that examine the actual product to detect defects, such as testing and inspection, and quality management coordinates both. Both are needed, and the greatest returns come from prevention.

One of the most effective ways to detect defects early, before any code runs, is for people to read the work. The next chapter begins with code reviews and inspections.
