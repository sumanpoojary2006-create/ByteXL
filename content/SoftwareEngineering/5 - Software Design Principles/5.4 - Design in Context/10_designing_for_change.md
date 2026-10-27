## Introduction

Successful software is changed constantly. Users ask for new features, regulations alter rules, platforms evolve, and mistakes are corrected. Studies of software costs have long shown that most of the total effort over a system's life goes on changes after the first release. A design is therefore judged not only by whether it works today but by how cheaply and safely it can be altered tomorrow.

**Definition:** Designing for change is the practice of structuring software so that the changes most likely to occur can be made quickly, locally, and safely, by identifying what is likely to vary and isolating it behind stable boundaries.

<!--
IMAGE PROMPT  ->  generate as images/10_intro_designing_for_change.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A building with some rooms drawn as modular removable blocks labelled Likely to change, and the foundation and frame drawn solid and labelled Stable, with a crane swapping one block without disturbing the rest.

ON-IMAGE TEXT: show a short bold title "Designing for Change" plus only these few labels, large and legible: Stable, Variable, Swap. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Why Change Is the Norm

- **Requirements evolve** as users learn what they need.
- **The world changes:** laws, markets, competitors, and partners.
- **Technology moves:** libraries, platforms, and security needs.
- **Understanding grows,** exposing mistakes in earlier decisions.
- **Success invites growth:** more users and data than first planned.

Meir Lehman's laws of software evolution observe that a system used in the real world must continually change or become progressively less useful, and that its structure tends to degrade as it is changed unless effort is spent to maintain it.

## Predict Where Change Will Come

It is impossible to predict all changes, and wasteful to prepare for all of them. The practical approach is to ask, for each part of the design, **how likely is it to change, and how costly would the change be?** Parts that are both likely to change and expensive to change deserve protection.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Likely source of change</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical protection</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Business rules, such as prices and discounts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep rules in one place, possibly as data or configuration</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">External services, such as payment providers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hide them behind an interface</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data formats and storage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Encapsulate storage behind a module</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">User interface</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Separate presentation from logic</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Algorithms</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Put them behind a common interface so alternatives can be swapped</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Platform and infrastructure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Isolate platform-specific code in one layer</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Feature variation between customers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use configuration, not copies of code</td>
    </tr>
  </tbody>
</table>

## Techniques

1. **Information hiding.** Place each likely-to-change decision in its own module.
2. **Stable interfaces.** Keep the contract between modules steady while implementations change.
3. **Abstraction and extension points.** Allow new behaviour to be added without editing existing code, as the open-closed principle suggests.
4. **Configuration over code.** Move values and choices that vary into settings that can be changed without rebuilding.
5. **Loose coupling and high cohesion,** so that effects of a change stay local.
6. **Automated tests.** A good test suite is what makes change safe, since it tells you quickly whether something broke.
7. **Small, frequent releases.** Small changes are easier to understand and reverse.
8. **Feature toggles,** which allow a change to be released switched off and enabled when ready.

## The Balance With Simplicity

Preparing for change has a price. Each layer, option, and extension point adds code and concepts that everyone must understand. Preparing for changes that never come is waste, and the extra flexibility may even make the actual changes harder. The guidance of YAGNI applies: build for the change you can reasonably foresee, keep the design clean, and refactor when the real change arrives.

A useful principle is to **make the design easy to change, not to change it in advance.** Clean code with good tests is more adaptable than elaborate machinery for imagined futures.

## Technical Debt

Ward Cunningham used the metaphor of **debt** for the consequences of expedient design: a shortcut buys speed now, but the extra effort of working with a messy design is like interest paid on every later change. Debt can be a sensible choice when deliberate, recorded, and repaid, for example to meet a deadline that truly matters. It becomes dangerous when it is accidental, or when interest accumulates until progress stalls. Designing for change includes managing debt: noticing it, tracking it, and paying down the debt that slows the most important work.

## Evolution of the Design

Even a well-prepared design will meet changes it did not foresee. Healthy teams treat design as **ongoing**: they improve structure continuously through small refactorings, review designs when requirements shift, and retire parts that no longer fit. Design quality is maintained, not achieved once.

<!--
IMAGE PROMPT  ->  generate as images/02_change_likelihood_vs_cost.png   (16:9 explanatory diagram, place here)

A two-by-two grid with Likelihood of change on one axis and Cost of change on the other. Quadrants: Protect first (likely and costly, highlighted green), Keep simple (unlikely and cheap), Watch (likely but cheap), Accept risk (unlikely but costly). Example items placed in each.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Where to Invest?

A food-ordering system relies on an external payment provider, a fixed company logo, and delivery fee rules that marketing changes monthly.

1. Which two areas are worth isolating for change?
2. Which is probably not?

The payment provider is likely to change or fail and is costly to replace, so it should be hidden behind an interface. The delivery fee rules change often and should be kept in one place, ideally as configuration. The fixed logo is unlikely to change and cheap to alter, so it needs no special design.

## Conclusion

Designing for change is the practice of structuring software so that the changes most likely to occur can be made quickly, locally, and safely, by identifying what is likely to vary and isolating it behind stable boundaries. It means preparing for the probable, keeping everything else simple, and maintaining the design as it evolves.

To judge whether a design achieves these aims, it must be evaluated. The next topic describes how.
