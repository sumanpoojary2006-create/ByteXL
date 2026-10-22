## Introduction

CampusConnect needed to accept online payments for mess fees. Ananya's first instinct was enthusiastic: "I can build this. I know how card payments work. It will take me two weeks."

Vikram did not say she was wrong. He asked her a list of questions instead. What happens when the card network times out halfway through a payment? How do we handle refunds? Who is responsible if card numbers leak? What do the banks require before they will let a startup handle cards at all? Ananya stopped counting after the ninth question.

In the end the team connected to an established payment provider, and the integration took four days. Ananya had learned something no programming course had taught her: the skill that mattered was not whether she **could** build it, but whether she **should**, and she had reached the answer by thinking in a particular way.

**Definition:** Thinking like a software engineer means applying a small set of habits, breaking problems down, abstracting away detail, weighing trade-offs, stating assumptions, and planning for failure, to make sound decisions under uncertainty.

<!--
IMAGE PROMPT  ->  generate as images/09_intro_thinking_like_a_software_engineer.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Use the named person, setting, and engineering problem from the Introduction.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Ananya stands at a fork where one path is labelled Build It Ourselves with a tangled cable maze, and the other is labelled Use a Provider with a clean bridge, while Vikram holds a balance scale between them.

ON-IMAGE TEXT: show a short bold title "Thinking Like a Software Engineer" plus only these few labels, large and legible: Build, Buy, Trade-offs. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Five Habits of Mind

**1. Decomposition.** Break a large problem into smaller parts that can be understood, assigned, and tested separately. "Accept payments" becomes: choose a provider, create an order, redirect to payment, confirm the result, record it, handle failure, handle refunds.

**2. Abstraction.** Focus on what matters and hide what does not. To the order-handling code, the payment provider is simply something that takes an amount and says "paid" or "failed". How the provider talks to banks is hidden behind that simple interface.

**3. Trade-off analysis.** Almost every design decision gives up one good thing for another. There is rarely a best answer, only a best answer **for this context**.

**4. Making assumptions explicit.** Every plan rests on beliefs about users, load, and the environment. Writing them down turns hidden risks into things the team can check.

**5. Planning for failure.** Ask "what if this breaks?" at every step. Networks drop, disks fill, users type unexpected things. Designing for the unhappy path is what separates professional software from demonstrations.

<!--
IMAGE PROMPT  ->  generate as images/02_five_habits_of_mind.png   (16:9 explanatory diagram, place here)

A hexagon-like ring of five icons around a central head silhouette: puzzle pieces (Decomposition), a magnifying lens (Abstraction), a balance scale (Trade-offs), a sticky note (Assumptions), a shield with a crack (Failure).

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## A Worked Trade-off: Build or Buy?

Engineers often compare options with a simple decision table. List the criteria that matter, score each option, and discuss the result. The scores below use 1 (poor) to 5 (excellent) and are judgement calls, not facts.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Criterion</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Build our own payments</th>
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
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maintenance effort for our small team</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">4</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">**Total (equal weights)**</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">**15**</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">**21**</td>
    </tr>
  </tbody>
</table>

The totals are only a conversation starter. If the team decided that security burden and time were far more important than fees, the provider wins by even more. If CampusConnect later processed millions of payments a month, the fee column might become dominant and the decision might be revisited. Writing the table also forces the team to say **which criteria they care about**.

## Reasoning With Evidence

Vikram's first reply to many questions is: "What would we measure?" Engineering is full of estimates and opinions, and opinions are cheap. Where possible, replace them with a quick experiment, a prototype, or a number: how long does the provider take to respond? How many payments do we expect per day? A thirty-minute spike that disproves an assumption is far cheaper than a month spent building on it.

## Reversible and Irreversible Decisions

Not all choices deserve equal deliberation. Choosing the colour of a button can be reversed in a minute. Choosing a database technology or a public API format is expensive to undo. A useful rule: **decide reversible things quickly, and spend your thinking on the irreversible ones**.

## Your Turn: Name the Habit

1. A developer lists "we assume under 500 simultaneous users" at the top of a design document.
2. A team splits "build a booking system" into search, booking, payment, and notification parts.
3. An engineer asks, "What does the app do if the SMS service is down?"
4. A team draws a box labelled "Payment Service" without describing how it works inside.

Item 1 is making assumptions explicit. Item 2 is decomposition. Item 3 is planning for failure. Item 4 is abstraction.

## Conclusion

Thinking like a software engineer means applying a small set of habits, breaking problems down, abstracting away detail, weighing trade-offs, stating assumptions, and planning for failure, to make sound decisions under uncertainty. These habits matter more than any particular language or framework, because they apply to every system.

Habits of mind need practical tools to act on. Ananya's next task is to set up her working environment properly, so the next lesson walks through the toolchain that every professional developer uses.
