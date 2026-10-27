## Introduction

Every team sometimes takes a shortcut: a quick fix to meet a deadline, a design chosen for speed, a missing test, a library not upgraded. Each shortcut saves time now and costs time later, because the code becomes harder to work with. In 1992 Ward Cunningham described this using a financial metaphor, and the term technical debt has since become the common way of discussing the long-term cost of short-term decisions.

**Definition:** Technical debt is the accumulated future cost of choosing, deliberately or by accident, a quicker or easier solution now in place of a better one, which must be paid as extra effort on every later change until the underlying problem is repaired.

<!--
IMAGE PROMPT  ->  generate as images/10_intro_technical_debt.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A balance with a stack of coins labelled Principal on one side, and a growing pile of small coins labelled Interest, paid on every new feature, on the other, beside a calendar showing repayment.

ON-IMAGE TEXT: show a short bold title "Technical Debt" plus only these few labels, large and legible: Principal, Interest, Repay. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Metaphor

Financial debt has a **principal**, the amount borrowed, and **interest**, the cost of carrying the debt over time.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Financial debt</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Technical debt</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Borrowing lets you buy something now</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A shortcut delivers something sooner</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Principal</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The effort needed to fix the shortcut properly</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Interest</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The extra effort paid on every later change because of the shortcut</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Repayment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Refactoring or redoing the work properly</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Default</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The code becomes so costly to change that progress stalls or a rewrite is forced</td>
    </tr>
  </tbody>
</table>

The key insight is that the **interest is paid continuously**, in slower changes, more defects, longer onboarding, and developer frustration, whether or not anyone notices. Debt in code that is never changed costs little, and debt in a hot area of frequent change costs a lot.

Cunningham's original point was not that bad code is acceptable. He was describing how an initial understanding is always incomplete, so the first design will not fit the problem as it is later understood, and unless the code is **refactored to match the new understanding**, the mismatch compounds as debt.

## Types of Technical Debt

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Type</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Code debt</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Poor readability, duplication, complexity, smells</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A very long function copied and modified in several places</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Design and architecture debt</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Structure that no longer fits needs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A monolith that cannot be scaled in parts; tangled dependencies</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test debt</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Missing or unreliable tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Features that nobody dares change because there is no safety net</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Documentation debt</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Missing or outdated documentation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No explanation of how to run or release the system</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Build and infrastructure debt</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Slow, manual, or fragile build and release</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Releases that need a long manual checklist</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dependency debt</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Outdated libraries and platforms</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A library several major versions behind, with known security flaws</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Knowledge debt</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Understanding held in one person head</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A critical part that only one developer understands</td>
    </tr>
  </tbody>
</table>

## The Technical Debt Quadrant

Martin Fowler classified debt along two dimensions: whether it was taken on **deliberately** or **inadvertently**, and whether the decision was **prudent** or **reckless**.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;"></th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Reckless</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Prudent</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deliberate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"We do not have time for design." A choice made without regard for consequences</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"We must ship now and deal with the consequences." A conscious, informed trade-off with a plan to repay</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inadvertent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"What is layering?" The team lacks the knowledge to know it is creating debt</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"Now we know how it should have been done." Learning after the fact, which is inevitable</td>
    </tr>
  </tbody>
</table>

Not all debt is bad. **Prudent deliberate debt** can be a sound business decision, as a loan can be, if it is recorded and repaid. **Reckless debt** is the problem, as is debt that is accidental and never noticed. The prudent inadvertent kind is unavoidable, and is why continuous refactoring is necessary.

## Causes

- **Schedule pressure** and unrealistic deadlines
- **Changing requirements,** leaving earlier designs misfit
- **Lack of knowledge or experience**
- **Lack of tests,** which makes improvement risky
- **Weak review and standards**
- **Short-term thinking** and incentives that reward features over quality
- **Aging dependencies** and platforms
- **Time,** as unmaintained code decays relative to its environment, sometimes called software rot or bit rot

## Making Debt Visible and Measuring It

Debt is hard to manage if it is invisible. Approaches:

- **A debt register:** record each known item with its location, cause, estimated cost to repair, and the interest it causes, in the ordinary issue tracker.
- **Static analysis tools** report measures such as duplication, complexity, and rule violations, and some estimate the time to repair, as in the SQALE method. These numbers are rough and should be used for trends and discussion.
- **Flow measures:** rising time to complete changes, rising defect rates, and long onboarding are symptoms of high interest.
- **Developer surveys and retrospectives** reveal where the team feels pain.
- **Change history** shows which areas change often, and so where interest is highest.

## Managing Debt

1. **Decide consciously.** When taking a shortcut, record it and say why, with a plan.
2. **Prioritise by interest, not by size.** Repair debt in the areas that change most and that most slow the team, not simply the worst-looking code.
3. **Pay down continuously.** Apply the scout rule and preparatory refactoring during normal work.
4. **Reserve capacity.** Many teams set aside a portion of each iteration for debt repair, so that it does not always lose to new features.
5. **Make it visible to stakeholders** in terms of consequences: slower delivery, higher risk, higher cost.
6. **Prevent new debt** with a strong Definition of Done, tests, reviews, and standards.
7. **Repair opportunistically** when you are already changing the area.
8. **Do not let it become a blame subject.** Debt is a shared cost, and honest reporting must be safe.
9. **Know when to stop:** some debt is not worth paying, such as in code about to be retired.

## Limits of the Metaphor

The metaphor helps communication but can mislead. Unlike financial debt, technical debt has no fixed interest rate, no lender who demands payment, and its size is uncertain. It is also sometimes used to describe any unpleasant code, or to excuse bad work. A useful discipline is to restrict the term to cases where a **specific cost can be named**.

<!--
IMAGE PROMPT  ->  generate as images/02_debt_quadrant_and_interest.png   (16:9 explanatory diagram, place here)

Left: a two-by-two grid with Deliberate/Inadvertent on one axis and Reckless/Prudent on the other, a short quotation in each cell, the Prudent-Deliberate cell highlighted green. Right: a line chart of time taken per change rising over months as debt grows, with a drop after a repayment period.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Classify the Debt

1. A team ships a feature without automated tests to meet a fixed launch date, records it, and schedules the tests for the next iteration.
2. A team writes a tangled design because nobody knew better, and does not notice.
3. A library has not been upgraded for three years, and its latest security fixes are not applied.

Case 1 is prudent, deliberate debt, acceptable if repaid as planned (test debt). Case 2 is inadvertent debt, reckless in the sense of lacking knowledge; it is reduced by learning, review, and refactoring (design debt). Case 3 is dependency debt, with security risk as its interest, and should be prioritised.

## Conclusion

Technical debt is the accumulated future cost of choosing, deliberately or by accident, a quicker or easier solution now in place of a better one, which must be paid as extra effort on every later change until the underlying problem is repaired. Managing it means making it visible, taking it on consciously, and repaying it where the interest is highest.

The most extreme form of debt is code that nobody dares change, often because it has no tests. The last topic of this chapter addresses working with such legacy code.
