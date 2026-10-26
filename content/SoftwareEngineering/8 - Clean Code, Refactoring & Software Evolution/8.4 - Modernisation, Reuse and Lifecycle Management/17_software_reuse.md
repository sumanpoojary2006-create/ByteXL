## Introduction

Most software is built largely from things other people have already made: programming languages, operating systems, libraries, frameworks, databases, and cloud services. A modern application may contain a small amount of original code on top of an enormous body of reused components. Reuse is one of the main reasons software development has become faster, yet it brings its own costs and risks. Reuse is the practice of building new software from existing artefacts, and the engineering question is how to do it wisely.

**Definition:** Software reuse is the practice of creating new software from existing software artefacts, such as code, components, designs, tests, and knowledge, instead of building everything from scratch, in order to reduce cost and time and to improve quality, while managing the costs of finding, adapting, and depending on what is reused.

<!--
IMAGE PROMPT  ->  generate as images/17_intro_software_reuse.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A large construction made of standard labelled building blocks: Library, Framework, Service, Component, Pattern, with a small hand-made custom block at the top, and a magnifying glass inspecting one block label for licence and version.

ON-IMAGE TEXT: show a short bold title "Software Reuse" plus only these few labels, large and legible: Reuse, Adapt, Depend. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## What Can Be Reused

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Level</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Code and functions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Standard library routines, utility functions</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Libraries and packages</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Date handling, cryptography, charting, payment client libraries</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Components and modules</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Self-contained parts with defined interfaces</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Frameworks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A structure of partly built applications that you extend, such as web frameworks</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Services and platforms</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cloud services, external interfaces to payment, mapping, identity</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Applications and products</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Off-the-shelf systems configured for a purpose</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Designs and architectures</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Design patterns, reference architectures, templates</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requirements, tests, and documentation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Standard requirement sets, test suites, documentation templates</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Knowledge and experience</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Practices, checklists, lessons learned</td>
    </tr>
  </tbody>
</table>

## Benefits

- **Faster delivery:** less to build.
- **Higher quality:** a widely used component has been tested by many users and its defects found.
- **Lower cost:** development effort is shared across users.
- **Focus on what is unique:** teams spend effort on what distinguishes their product.
- **Standardisation and interoperability.**
- **Access to expertise:** specialised areas such as security or cryptography are better left to specialists.

## Costs and Risks

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Explanation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Mitigation</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Finding and judging components</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Time is needed to search, evaluate quality, fit, and maintenance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maintain a shortlist; evaluate against criteria</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Understanding and adapting</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reused parts must be learned and may not fit exactly</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prefer components with good documentation and clean interfaces</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maintenance burden of dependencies</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Updates, breaking changes, and abandoned projects</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Track dependencies; update regularly; choose actively maintained ones</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dependency conflicts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Different parts require incompatible versions of the same library, sometimes called dependency hell</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lock versions; limit the number of dependencies</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security and supply chain risk</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A flaw or malicious code in a dependency affects every user</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scan for vulnerabilities; inspect provenance; keep a bill of materials</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Licence obligations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Each component carries terms that may restrict how the result is used or distributed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Review licences; keep records</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Loss of control</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A supplier can change or remove a service or product</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prefer standards; isolate behind your own interfaces</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Over-reliance and bloat</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Many dependencies for trivial functions increase size and risk</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Weigh the value of each dependency</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not-invented-here syndrome</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rebuilding what already exists out of habit or mistrust</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Evaluate honestly</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reuse of poor-fit parts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Forcing a component to do what it was not designed for</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Choose the right tool or build what is needed</td>
    </tr>
  </tbody>
</table>

## Licences

Reusing software means accepting its licence.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Kind</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Idea</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Implication</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Permissive licences</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Allow almost any use, including in proprietary products, usually with a notice requirement</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Easy to reuse</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Copyleft licences</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Require that derived works, or in some cases combined works, be released under the same terms</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">May affect how the result can be distributed</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Commercial licences</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Paid terms with defined rights and limits</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost and contractual obligations</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unlicensed code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No permission granted</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Legally risky to reuse</td>
    </tr>
  </tbody>
</table>

Teams should know which licences they use and whether they are compatible. Organisations often maintain a list of approved licences.

## Designing for Reuse

Making something reusable costs more than making it for one use. Fred Brooks estimated that producing a generalised, tested, documented component that others can use takes about three times the effort of a program for the author's own use. Effort for reuse pays only if the component is **actually reused**. Guidelines:

- **Do not generalise early.** Wait until a second or third use appears, which the rule of three suggests.
- **Define a clear, stable interface,** with good documentation and examples.
- **Keep it cohesive and loosely coupled,** with few dependencies of its own.
- **Provide tests,** so that users can trust it and change it safely.
- **Version carefully,** using semantic versioning, so users know whether an update may break them.
- **Handle configuration, errors, and edge cases** thoughtfully.
- **Maintain it:** a reusable component needs an owner.

## Planned and Opportunistic Reuse

- **Opportunistic reuse** takes advantage of whatever is found when needed, and is common.
- **Planned (systematic) reuse** invests in building a library of components for deliberate reuse across projects. A **software product line** applies this at scale: a set of products built from a shared collection of core assets and a common architecture, with each product assembled and customised from them, as studied by the Software Engineering Institute.

## Choosing: Build, Buy, or Reuse

For each need, consider:

1. Does a suitable component, service, or product exist that is **well maintained and secure**?
2. How well does it **fit** the requirements and architecture?
3. What is the **total cost**: adaptation, integration, licence, and maintenance?
4. How easily could it be **replaced** if it fails or is abandoned?
5. Is the capability **core** to the business, which argues for building it?
6. What are the **risks**: security, licensing, supplier stability?

Isolating reused components behind your own interfaces, as in the adapter pattern, keeps the choice reversible.

<!--
IMAGE PROMPT  ->  generate as images/02_reuse_decision_and_risks.png   (16:9 explanatory diagram, place here)

Left: a decision flow for a need: Does a good component exist? Fit? Maintained and secure? Licence compatible? leading to Reuse, or Build when it is core to the business. Right: a dependency tree with one branch marked red for a vulnerable or abandoned dependency, labelled Supply chain risk.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Reuse Wisely?

1. A team needs password hashing and considers writing its own algorithm.
2. A team imports a large library to use a single trivial function.
3. A team discovers that a library it uses has not been updated for four years and has a known vulnerability.

Case 1 should reuse a well-established, reviewed implementation: security components are best left to specialists. Case 2 adds dependency, size, and risk for little gain; writing the small function may be wiser. Case 3 is a maintenance and security risk: the team should replace or isolate the dependency and plan the change.

## Conclusion

Software reuse is the practice of creating new software from existing software artefacts, such as code, components, designs, tests, and knowledge, instead of building everything from scratch, in order to reduce cost and time and to improve quality, while managing the costs of finding, adapting, and depending on what is reused. Reuse is powerful, but every dependency is a commitment.

Reused or not, software and the knowledge about it must be recorded. The next topic describes software documentation.
