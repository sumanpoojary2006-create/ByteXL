## Introduction

Scrum describes how to organise work, but says little about how to write good software. Extreme Programming, or XP, fills that gap. It prescribes a set of engineering and teamwork practices that keep software of high quality while it changes quickly. The name reflects the idea of taking good practices to an extreme: if code review is good, review all the time through pair programming; if testing is good, test first and always.

**Definition:** Extreme Programming (XP) is an agile methodology, developed by Kent Beck, that combines technical practices such as pair programming, test-driven development, continuous integration, and refactoring with close customer involvement and short releases, to deliver high-quality software despite changing requirements.

<!--
IMAGE PROMPT  ->  generate as images/14_intro_extreme_programming_practices.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Two people sharing one workstation on the left, a circular test-then-build loop in the middle, and a series of small frequent releases on the right.

ON-IMAGE TEXT: show a short bold title "Extreme Programming Practices" plus only these few labels, large and legible: Pair, Test, Release. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Values

XP is founded on five values: **communication**, **simplicity**, **feedback**, **courage**, and **respect**. The practices exist to put these values into daily work. Feedback in particular is central: XP builds many fast feedback loops, from seconds (automated tests) to weeks (customer releases).

## The Main Practices

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Practice</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it means</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem it addresses</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pair programming</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two people work together at one workstation; one writes while the other reviews continuously and thinks ahead</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defects, knowledge silos, and delayed review</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test-driven development</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Write a failing automated test first, then the simplest code that makes it pass, then improve the design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unclear requirements and fear of change</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Continuous integration</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Integrate and test the work of everyone many times a day</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Late, painful integration of separate work</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Small releases</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Release working software frequently, in small steps</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Long gaps without feedback from users</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simple design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Build the simplest thing that meets current needs; avoid speculative features</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Over-engineering and wasted effort</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Refactoring</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Improve the internal structure of code without changing its behaviour, continuously</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Gradual decay of design quality</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Collective code ownership</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Anyone may improve any part of the code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Bottlenecks and dependence on single experts</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Coding standards</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The team follows an agreed style</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inconsistency that slows reading</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The planning game</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Customers choose features by value, developers estimate cost, plan is revised often</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Disputes about scope and priorities</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">On-site customer</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A representative of users is available to the team</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Misunderstood requirements</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sustainable pace</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Avoid long periods of overtime</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Burnout and rising defect rates</td>
    </tr>
  </tbody>
</table>

## How the Practices Support One Another

XP practices are designed as a system; each makes the others safer.

- **Refactoring and simple design** are only safe because **automated tests** catch mistakes.
- **Continuous integration** only works if the tests run quickly and automatically.
- **Collective ownership** is only safe because of tests, shared standards, and pair programming that spreads knowledge.
- **Small releases** keep the customer's feedback loop short, so the planning game can respond to what is learned.

Dropping one practice weakens the others. A team that skips tests but tries to refactor aggressively is courting disaster.

<!--
IMAGE PROMPT  ->  generate as images/02_xp_feedback_loops.png   (16:9 explanatory diagram, place here)

Concentric feedback loops from innermost to outermost: Pair programming (seconds), Unit tests (minutes), Continuous integration (hours), Customer review (weeks), each labelled with its time scale.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Strengths and Limitations

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strengths</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Limitations</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High technical quality and low defect rates</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Demands discipline and skill from every team member</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Very fast feedback</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">On-site customers are often unavailable in practice</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Spreads knowledge across the team</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pair programming may feel costly or uncomfortable at first</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Copes well with change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Less suited to large, distributed teams or heavy regulation without adaptation</td>
    </tr>
  </tbody>
</table>

## XP and Scrum Together

The two are complementary. Scrum provides the management framework of roles and events, and XP provides the engineering practices. Many successful teams run Scrum for organisation and adopt XP practices such as test-driven development and continuous integration to make each sprint's increment reliable.

## Your Turn: Which Practice?

1. A team notices that a bug was introduced three weeks ago and only discovered now because different developers' work was combined only at the end.
2. Only one developer understands the billing module, and the team is anxious when that person is away.
3. A team wants to restructure confusing code without risking new defects.

Problem 1 is addressed by continuous integration. Problem 2 is addressed by collective ownership supported by pair programming. Problem 3 is addressed by refactoring protected by automated tests.

## Conclusion

Extreme Programming (XP) is an agile methodology, developed by Kent Beck, that combines technical practices such as pair programming, test-driven development, continuous integration, and refactoring with close customer involvement and short releases, to deliver high-quality software despite changing requirements. Its practices reinforce one another.

The next topic introduces a different style of agile work, one that does not use fixed iterations and focuses instead on the flow of work through stages.
