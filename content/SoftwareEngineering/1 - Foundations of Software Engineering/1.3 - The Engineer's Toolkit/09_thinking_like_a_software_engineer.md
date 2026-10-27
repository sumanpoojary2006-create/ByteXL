## Introduction

Experienced engineers apply a consistent set of habits of mind to almost every decision: asking whether something should be built at all, what could go wrong, and what it will cost later. These habits matter more than any single language or framework, because they apply to every system.

This topic describes those habits.

**Definition:** Thinking like a software engineer means applying a small set of habits, breaking problems down, abstracting away detail, weighing trade-offs, stating assumptions, and planning for failure, to make sound decisions under uncertainty.

<!--
IMAGE PROMPT  ->  generate as images/09_intro_thinking_like_a_software_engineer.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Five icons arranged in a ring around a head silhouette: puzzle pieces, a magnifying lens, a balance scale, a sticky note, and a cracked shield.

ON-IMAGE TEXT: show a short bold title "Thinking Like a Software Engineer" plus only these few labels, large and legible: Decompose, Trade off, Plan. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Five Habits of Mind

**1. Decomposition.** Break a large problem into smaller parts that can be understood, assigned, and checked separately. "Accept online payments" becomes: choose a provider, create an order, confirm the result, record it, handle failure, handle refunds.

**2. Abstraction.** Focus on what matters and hide what does not. To the ordering logic, a payment provider is simply something that takes an amount and answers "paid" or "failed". How it talks to banks is hidden behind that simple interface.

**3. Trade-off analysis.** Almost every design decision gives up one good thing for another. There is rarely a best answer, only a best answer **for this context**.

**4. Making assumptions explicit.** Every plan rests on beliefs about users, load, and the environment. Writing them down turns hidden risks into things the team can check.

**5. Planning for failure.** Ask "what if this breaks?" at every step. Networks drop, storage fills, users do unexpected things. Designing for the unhappy path separates professional software from demonstrations.

## A Worked Trade-off: Build or Buy?

Engineers often compare options with a simple decision table. List the criteria that matter, score each option, and discuss the result. The scores below use 1 (poor) to 5 (excellent) and are judgement calls, not facts.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Criterion</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Build our own payment system</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Use a payment provider</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Time to launch</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1 (months)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">5 (days)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Initial cost</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">4</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security and compliance burden on us</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">4</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Control over every detail</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">5</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Long-term fees</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">5 (none per transaction)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2 (fee per payment)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maintenance effort for a small team</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">4</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Total (equal weights)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">15</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">21</td>
    </tr>
  </tbody>
</table>

The totals are a conversation starter, not an answer. If the team cares far more about security and time than about fees, the provider wins by even more. If the product later processes millions of payments a month, fees may dominate and the decision may be revisited. Building the table also forces the team to say **which criteria it cares about**.

## Reasoning With Evidence

Opinions are cheap in engineering, so experienced engineers ask "what would we measure?" Where possible they replace opinions with a quick experiment, a prototype, or a number: how long does the provider take to respond, and how many payments do we expect each day? A thirty-minute experiment that disproves an assumption is far cheaper than a month spent building on it.

## Reversible and Irreversible Decisions

Not all choices deserve equal deliberation. Changing the colour of a button can be undone in minutes. Choosing a data storage technology or a public interface format is expensive to reverse. A useful rule: **decide reversible things quickly, and spend your thinking on the irreversible ones**.

## Thinking About Debt

Every shortcut taken to deliver sooner creates **technical debt**: extra future cost in return for present speed. Debt is not always wrong, just as a loan is not always unwise, but it must be a conscious decision, recorded and repaid, because unmanaged debt slows every later change. Engineers learn to ask not only "will this work today?" but "what will this cost us to live with?"

## Your Turn: Name the Habit

1. A design document opens with the line "we assume fewer than 500 simultaneous users."
2. A team divides a booking system into search, booking, payment, and notification parts.
3. An engineer asks, "What does the system do if the text-message service is down?"
4. A diagram shows a box labelled "Payment Service" without describing its internals.

Item 1 is making assumptions explicit. Item 2 is decomposition. Item 3 is planning for failure. Item 4 is abstraction.

## Conclusion

Thinking like a software engineer means applying a small set of habits, breaking problems down, abstracting away detail, weighing trade-offs, stating assumptions, and planning for failure, to make sound decisions under uncertainty. These habits matter more than any single technology.

Habits of mind need practical tools to act on. The next topic surveys the toolchain that professional teams use to build, check, and deliver software.
