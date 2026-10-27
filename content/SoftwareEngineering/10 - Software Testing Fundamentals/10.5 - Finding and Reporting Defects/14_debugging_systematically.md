## Introduction

Testing reveals that something is wrong. Debugging is the work of discovering why, and fixing it. Beginners often debug by guesswork: changing things at random, adding a statement here, trying a fix there, until the symptom disappears, often without understanding what was wrong. This wastes time and frequently leaves the real defect in place or creates new ones. Experienced engineers debug as scientists do: they observe, form hypotheses, test them, and narrow down the cause. The method is learnable, and it makes the difference between hours and minutes.

**Definition:** Debugging is the systematic process of reproducing a failure, locating the defect that causes it, understanding why it occurs, correcting it at its root, and verifying that the fix works and does not break anything else.

<!--
IMAGE PROMPT  ->  generate as images/14_intro_debugging_systematically.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A detective-style loop of steps: Reproduce, Observe, Hypothesise, Test, Fix, Verify, with a magnifying glass over a trail of events and a binary search narrowing a range of suspects.

ON-IMAGE TEXT: show a short bold title "Debugging Systematically" plus only these few labels, large and legible: Reproduce, Narrow, Fix. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Testing and Debugging

Testing and debugging are different activities. **Testing** finds failures. **Debugging** diagnoses and removes their causes. A test that fails is the starting point. Good tests make debugging easier by showing exactly what failed and under what conditions.

## The Scientific Method of Debugging

1. **Observe the failure.** What exactly happens? What was expected? When did it start?
2. **Reproduce it reliably.** A failure you can trigger on demand can be studied. If it is intermittent, find the conditions that make it more likely.
3. **Simplify.** Reduce the case to the smallest input and set of steps that still shows the problem. A minimal reproduction removes distractions, and often reveals the cause on its own.
4. **Form a hypothesis.** Based on the evidence, propose a specific explanation: "the total is wrong because the discount is applied before the item is added."
5. **Predict and test.** If the hypothesis is true, something else must also be true. Check it with a log statement, a debugger, or an experiment. A hypothesis that makes no testable prediction is not useful.
6. **Refine or reject.** If the evidence disagrees, discard the hypothesis and form another. Each experiment narrows the possibilities.
7. **Find the root cause.** Keep asking why until you reach the real source, not just a symptom.
8. **Fix it properly,** at the root.
9. **Verify** that the original failure is gone, and that nothing else is broken.
10. **Prevent recurrence:** add a regression test, and consider why the defect got in and whether similar ones exist.

The most common mistake is to skip observation and hypothesis and to start changing the code. Changing things without understanding is "shotgun debugging."

## Techniques for Locating the Defect

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Technique</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">How it works</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Good for</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Read the error message and stack trace</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The message states what failed; the stack trace shows the chain of calls that led there. Start at the top of the relevant part, in your own code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Crashes and exceptions</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Divide and conquer (binary search)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Find a point where things are still right and a point where they are wrong, then check the middle, and repeat. Halving the suspect region each time finds the fault in few steps</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Long sequences of steps or large amounts of code</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Bisecting history</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use version control to search the commit history for the commit that introduced the bug, as Unit 9 described</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Regressions: it worked before</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Logging and tracing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Record values and decisions as the program runs, and read the record</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Production issues, concurrency, distributed systems</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Interactive debugger</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pause execution at a breakpoint, examine variables, and step through the code line by line, watching how state changes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Understanding exactly what code does</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Print (log) debugging</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Insert temporary output at key points</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quick checks where a debugger is awkward</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rubber duck debugging</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Explain the problem and the code aloud, line by line, to a colleague or even an inanimate duck; the act of explaining often exposes the faulty assumption</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stuck on a puzzling problem</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Check assumptions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">List what you believe to be true and verify each: the input, the configuration, the version, the environment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Bugs where "that cannot be wrong"</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Compare working and failing cases</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What differs between input that works and input that fails, or between a machine where it works and one where it does not?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Environment and data-dependent issues</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Examine recent changes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What changed since it last worked?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sudden failures</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Wolf fence algorithm</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Build a fence across the middle of the territory and see which side the wolf is on; repeat. Named by Edward Gauss in 1982</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Same as binary search</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Profilers and memory tools</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Measure where time and memory go</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Performance and resource problems</td>
    </tr>
  </tbody>
</table>

## Using a Debugger

A debugger lets you see the program in motion.

- **Breakpoints** pause execution at a chosen line, or when a condition is met.
- **Stepping** runs one line at a time: step over a call, step into it, or step out.
- **Inspection** shows the values of variables and the call stack at the pause.
- **Watch expressions** track values as they change.
- **Conditional breakpoints** stop only when a particular condition holds, useful in loops.
- **Exception breakpoints** stop at the moment an error occurs.

The debugger is powerful for understanding, but it is not always available (for example in production), and logs and traces complement it.

## Kinds of Defects and Their Habits

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Kind</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical sign</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Hint</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Off-by-one and boundary errors</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fails at the first or last item, or at limits</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Check loop bounds and comparisons</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Null or missing values</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Crash when something is absent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Trace where the value should have been set</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Wrong assumption about data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Works for typical input, fails for unusual</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Examine the actual data, not the expected</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">State and ordering errors</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Depends on what happened before</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reproduce the exact sequence</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Concurrency problems (race conditions)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Intermittent, vanishes when you add logging or step through</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Timing-sensitive; suspect shared state; stress the code to provoke it</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Configuration and environment differences</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Works on one machine only</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Compare versions, settings, and data</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Integration and interface mismatches</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fails when components meet</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inspect what is actually sent and received</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Resource problems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Slowdowns, crashes after long running</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Memory, connections, files not released</td>
    </tr>
  </tbody>
</table>

Some bugs are called **Bohrbugs**, because like the solid atom model of Niels Bohr they are stable and reproducible. Others are **Heisenbugs**, because like the uncertainty principle of Werner Heisenberg they change or disappear when you try to observe them, as with timing problems. Heisenbugs call for logging that does not disturb timing, and for reasoning about the code, and for stress testing.

## Good Habits

- **Stay calm and methodical.** Frustration leads to guesswork.
- **Change one thing at a time** and record what you tried and observed.
- **Do not trust assumptions,** including your own and other people's code. Verify.
- **Read the error message carefully,** completely, and literally.
- **Fix the cause, not the symptom.** Hiding an error or adding a special case that suppresses it leaves the defect in place.
- **Look for the same mistake elsewhere.** Bugs often have siblings.
- **Write a test first** that reproduces the bug, then fix it. This proves the fix and prevents recurrence.
- **Take a break** or ask for help when stuck. A fresh mind or another person often sees at once what you have missed. Explain what you have already tried.
- **Learn from each bug.** What made it possible? What would have found it sooner? Improve tests, design, or tooling.

## Debugging in Production

Production debugging is constrained: you cannot usually pause the system or experiment freely. Rely on **observability**: logs, metrics, and traces with correlation identifiers, as Unit 9 described. Reproduce the problem in a safe environment where possible. Prefer **feature flags, rollback, and fast mitigation** to restore service first, then investigate. Keep user data private when examining evidence.

<!--
IMAGE PROMPT  ->  generate as images/02_debugging_loop_and_binary_search.png   (16:9 explanatory diagram, place here)

Left: a loop of Observe, Reproduce, Simplify, Hypothesise, Predict and test, Fix at the root, Verify, Add regression test. Right: a row of twenty steps with a good marker at the start and a bad marker at the end and the middle being checked repeatedly, narrowing to one faulty step, labelled Divide and conquer.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Debug Methodically

1. A report is wrong, and the pipeline of eight processing steps that produces it has not been checked. What technique helps find the faulty step quickly?
2. A feature worked last week and is now broken, and fifty changes were made since. What technique helps?
3. A developer notices that adding a log statement makes an intermittent failure disappear. What kind of bug is likely?

For case 1, divide and conquer: check the output midway through the pipeline, and then keep halving. For case 2, bisect the version history to find the change that introduced it. In case 3, a Heisenbug, likely a timing or concurrency problem, which the extra logging disturbed.

## Conclusion

Debugging is the systematic process of reproducing a failure, locating the defect that causes it, understanding why it occurs, correcting it at its root, and verifying that the fix works and does not break anything else. Treating it as a disciplined investigation, with hypotheses and experiments, is faster and more reliable than guessing.

Defects are found by many people, and not always by those who can fix them. The last topic of this unit describes how to report a defect so that it can be understood and resolved.
