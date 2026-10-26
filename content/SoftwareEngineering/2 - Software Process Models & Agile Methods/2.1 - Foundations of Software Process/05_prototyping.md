## Introduction

Customers often cannot describe exactly what they want until they see something. Engineers, in turn, cannot always know whether a technical idea will work until they try it. A prototype is an early, partial version of the system built to answer these questions cheaply, before committing to the full effort.

**Definition:** Prototyping is the practice of building an early, simplified version of a system to explore requirements, test ideas, and gather user feedback, so that uncertainty is reduced before the final product is built.

<!--
IMAGE PROMPT  ->  generate as images/05_intro_prototyping.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A rough paper sketch of a screen on the left, a clickable mock-up in the middle, and a polished working product on the right, with a user giving thumbs-up feedback to the middle one.

ON-IMAGE TEXT: show a short bold title "Prototyping" plus only these few labels, large and legible: Sketch, Test, Learn. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Why Build a Prototype?

- **To clarify requirements.** Seeing a screen or workflow prompts users to say what they really need.
- **To test feasibility.** A quick experiment shows whether a risky technical approach will work and perform acceptably.
- **To evaluate the interface.** Usability problems are far cheaper to find on a mock-up than in finished software.
- **To align stakeholders.** A concrete artifact ends debates that arise from different mental pictures.
- **To reduce risk.** Money is spent on learning before it is spent on building.

## Throwaway and Evolutionary Prototypes

The two main kinds differ in what happens to them afterwards.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Throwaway (exploratory) prototype</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Evolutionary prototype</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Purpose</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Learn, then discard</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Learn, then grow into the product</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality of construction</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quick and rough on purpose</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Built to production standards from the start</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Typical focus</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Poorly understood requirements, interface ideas</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Well-understood core that can be refined</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Main risk</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pressure to keep it and ship it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Starting with weak foundations and accumulating debt</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">After use</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Discarded; knowledge is kept</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Extended with new features</td>
    </tr>
  </tbody>
</table>

A common failure is a throwaway prototype that quietly becomes the product. Because it was built quickly and without proper structure, it carries hidden technical debt into production. A team that builds throwaways should agree beforehand that they will be discarded.

## Fidelity: How Real Should It Be?

Prototypes range from low to high fidelity, and the right level depends on the question being asked.

- **Low fidelity:** paper sketches, whiteboard drawings, simple wireframes. Fast, cheap, and invite criticism because they look unfinished.
- **Medium fidelity:** clickable mock-ups that show screens and flow without real functionality.
- **High fidelity:** a working slice with realistic behaviour, used to test performance, integration, or detailed usability.

Starting low is usually wise: it is cheaper to change and encourages honest feedback.

## Where Prototyping Fits in the Life Cycle

Prototyping is a technique, not a complete process. It is used inside other models: during requirements work to discover needs, during design to test an architecture or interface, and in iterative development to deliver evolving versions. Its value is greatest when uncertainty is high.

## Risks and Limits

- Users may mistake a convincing prototype for nearly finished software and expect it soon.
- A polished prototype can hide the large amount of unseen work needed, such as security, error handling, and performance.
- Feedback from a few users may not represent everyone.
- Without discipline, teams can keep prototyping and never commit to a design.

## Your Turn: Which Kind of Prototype?

1. A team wants to check whether a new search technique is fast enough for millions of records, and will discard the experiment afterwards.
2. A designer shows paper sketches of three layouts to potential users to see which is clearest.
3. A team builds the core of a booking system to production standards and extends it each cycle based on feedback.

Situation 1 is a throwaway prototype aimed at feasibility. Situation 2 is a low-fidelity prototype for interface evaluation. Situation 3 is an evolutionary prototype, grown into the product.

## Conclusion

Prototyping is the practice of building an early, simplified version of a system to explore requirements, test ideas, and gather user feedback, so that uncertainty is reduced before the final product is built. Used deliberately, it is one of the cheapest ways to avoid building the wrong thing.

Prototyping addresses uncertainty informally. The next topic introduces a model that makes risk the central organising principle of the whole project.
