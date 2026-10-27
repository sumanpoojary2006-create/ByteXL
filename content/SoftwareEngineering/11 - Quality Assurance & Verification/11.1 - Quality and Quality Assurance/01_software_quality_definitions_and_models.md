## Introduction

Everyone wants quality software, and almost nobody means exactly the same thing by it. To a user it means that the product does what they need and does not get in their way. To a developer it may mean clean, maintainable code. To a manager it may mean few complaints and low support costs. To a regulator it means compliance and safety. Unit 1 introduced the essential attributes of good software and Unit 3 showed how quality requirements are stated. This unit treats quality as a discipline of its own, beginning with the question that must come first: what do we mean by quality, and how can it be described and compared?

**Definition:** Software quality is the degree to which a software product or process satisfies stated and implied needs, which is expressed through a set of measurable characteristics, such as functionality, reliability, security, usability, and maintainability, organised by quality models so that quality can be specified, assessed, and improved.

<!--
IMAGE PROMPT  ->  generate as images/01_intro_software_quality_definitions_and_models.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A gem with several facets, each facet labelled with a quality characteristic, Functionality, Reliability, Security, Usability, Maintainability, Performance, viewed by different observers: a user, a developer, a manager.

ON-IMAGE TEXT: show a short bold title "Software Quality Definitions and Models" plus only these few labels, large and legible: Many views, One product. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Definitions of Quality

Writers on quality have offered different definitions, each emphasising a different aspect.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Source</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Definition</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Emphasis</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Philip Crosby</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Conformance to requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Meeting the specification; zero defects against it</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Joseph Juran</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fitness for use</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Whether the product serves the actual purpose of the user</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Gerald Weinberg</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality is value to some person</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality is relative: it depends on who is asked</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">W. Edwards Deming</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality is defined by the customer; quality must be built into the process</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Process improvement and prevention</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">ISO/IEC 25010</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The degree to which a product satisfies stated and implied needs when used under specified conditions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Measurable characteristics</td>
    </tr>
  </tbody>
</table>

The definitions are complementary. Conformance to the specification is necessary but not sufficient: a product can match a specification and still be unfit for use if the specification was wrong, the distinction between verification and validation drawn in Unit 2. Weinberg's remark that quality is **value to some person** is a reminder that stakeholders will judge differently, and that deciding whose view counts is a project decision.

## David Garvin's Five Views

Garvin, writing on product quality in general, identified five views that apply well to software.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">View</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning for software</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Transcendent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality is recognised by experience but hard to define: "you know it when you see it"</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Product-based</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality is a measurable set of attributes of the product: speed, reliability, features</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">User-based</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality is fitness for the purposes of particular users</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Manufacturing-based</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality is conformance to specification and low defect rates; the process view</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Value-based</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality is the best performance for the price and effort; the economic view</td>
    </tr>
  </tbody>
</table>

A balanced quality effort attends to all five.

## Internal, External, and In-Use Quality

Quality can be examined from several positions.

- **Internal quality** concerns properties of the code and design visible to developers: structure, readability, test coverage, and complexity. It affects the cost of change.
- **External quality** concerns the behaviour of the running system as seen by testers: defects, performance, and reliability.
- **Quality in use** concerns the experience of users in context: whether they can reach their goals effectively and efficiently, and are satisfied and safe.

Good internal quality supports good external quality, and external quality supports quality in use, but the chain is not automatic.

## Quality Models

A **quality model** breaks the vague idea of quality into named characteristics so that they can be specified and measured. Several have been proposed.

- **McCall's model (1977)** grouped factors by the product's operation, revision, and transition: correctness, reliability, efficiency, integrity, usability; maintainability, testability, flexibility; portability, reusability, interoperability.
- **Boehm's model (1978)** arranged characteristics in a hierarchy from general utility down to measurable metrics.
- **ISO/IEC 9126**, and its successor **ISO/IEC 25010**, the international standard on which most current practice is based.

### ISO/IEC 25010

The product quality model in the 2011 edition has eight characteristics, each divided into sub-characteristics.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Characteristic</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Concerned with</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples of sub-characteristics</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Functional suitability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Whether it provides the functions needed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Completeness, correctness, appropriateness</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Performance efficiency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Speed and use of resources</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Time behaviour, resource utilisation, capacity</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Compatibility</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Coexistence and exchange with other products</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Co-existence, interoperability</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Usability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ease of learning and use</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Learnability, operability, user error protection, accessibility</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reliability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Performing correctly over time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maturity, availability, fault tolerance, recoverability</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Protection of information and access</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Confidentiality, integrity, authenticity, accountability</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maintainability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ease of change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Modularity, reusability, analysability, modifiability, testability</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Portability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Moving to other environments</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Adaptability, installability, replaceability</td>
    </tr>
  </tbody>
</table>

The standard also defines a **quality-in-use model**, with effectiveness, efficiency, satisfaction, freedom from risk, and context coverage. A 2023 revision updated the product model, for example renaming usability as interaction capability and portability as flexibility, and adding safety as a characteristic. The exact lists matter less than the use of such a model as a **checklist of qualities that might matter**, from which a project chooses the important ones.

## Choosing and Weighing Qualities

No product maximises every characteristic. A quality effort therefore:

1. **Identifies** the characteristics that matter for this product and its users, using a model as a prompt.
2. **Defines** each as a measurable target, as Unit 3 explained.
3. **Prioritises** them, accepting trade-offs: strong security may reduce convenience; high performance may increase cost.
4. **Plans** how each will be built in, checked, and monitored.

## The Cost of Quality

The economics of quality are often described using four kinds of cost, a model associated with Armand Feigenbaum and Joseph Juran.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Cost</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Software examples</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prevention</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Spending to stop defects arising</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Training, standards, design reviews, good tooling</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Appraisal</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Spending to find defects</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Testing, inspections, audits, static analysis</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Internal failure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The cost of defects found before release</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rework, retesting, delays</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">External failure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The cost of defects found after release</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Support, fixes, refunds, reputation, liability</td>
    </tr>
  </tbody>
</table>

The central insight is that **prevention and appraisal are cheaper than failure**, particularly external failure, and that investment in prevention reduces the total. This is the economic argument behind the early testing and early reviews of the previous units.

## Quality Is Built In

Deming and the lean movement argued that quality cannot be inspected into a product at the end; it must be **built in** by the process. In software this means clear requirements, sound design, disciplined coding, continuous testing, and rapid feedback, rather than a testing phase at the end to find what earlier phases got wrong. The remainder of this unit presents the practices that carry this principle out.

<!--
IMAGE PROMPT  ->  generate as images/02_quality_characteristics_and_cost_of_quality.png   (16:9 explanatory diagram, place here)

Left: a wheel with eight spokes labelled with the ISO 25010 characteristics around a centre labelled Quality. Right: a stacked bar showing cost of quality split into Prevention, Appraisal, Internal failure, External failure, with External failure drawn as the tallest red block.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Which View or Model?

1. A product meets every item in its specification, but its users cannot complete their main task. Which definitions of quality conflict?
2. A team wants a checklist of qualities to consider for a new product. What can it use?
3. A company spends heavily on support and refunds after release. Which cost category is this?

In case 1, quality as conformance to requirements is satisfied while quality as fitness for use is not, which shows a validation failure. In case 2, a quality model such as ISO/IEC 25010 serves as the checklist. In case 3 these are external failure costs, which could be reduced by investing in prevention and appraisal.

## Conclusion

Software quality is the degree to which a software product or process satisfies stated and implied needs, which is expressed through a set of measurable characteristics, such as functionality, reliability, security, usability, and maintainability, organised by quality models so that quality can be specified, assessed, and improved. It is multidimensional, relative to stakeholders, and cheaper to build in than to inspect in.

Defining quality is one task. Organising the effort to achieve it is another. The next topic distinguishes the two main strands of that effort: quality assurance and quality control.
