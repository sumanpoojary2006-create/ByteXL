## Introduction

Software meets the unexpected constantly. A file is missing, a network call times out, a user enters a letter where a number was expected, a disk fills, a partner system returns nonsense. Code that works only when everything goes right is demonstration code, not production code. Error handling is the discipline of deciding what a program does when things go wrong, and doing it in a way that keeps the normal logic readable and the failures visible and recoverable.

**Definition:** Error handling is the practice of detecting abnormal conditions, signalling them clearly, and responding in a controlled way, and defensive programming is the broader habit of writing code that anticipates misuse and failure, so that faults are caught early, contained, and reported instead of silently corrupting results.

<!--
IMAGE PROMPT  ->  generate as images/06_intro_error_handling_and_defensive_programming.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A road with a smooth main path and side exits labelled Invalid input, Network failure, Missing file, each leading to a safe marked bay with a signal light, while a guard post at the entrance inspects incoming parcels.

ON-IMAGE TEXT: show a short bold title "Error Handling and Defensive Programming" plus only these few labels, large and legible: Detect, Signal, Recover. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Kinds of Errors

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Kind</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Cause</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical response</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Programming errors (bugs)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A mistake in the code, such as using a value that should never be empty</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fail fast, fix the code; do not try to recover silently</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Invalid input</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data from users or other systems that breaks the rules</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Validate at the boundary, report clearly, continue safely</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Expected environmental failures</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Network down, file missing, service busy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Handle gracefully: retry, use a fallback, or report</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Resource exhaustion</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Memory, disk, or connections run out</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Release resources, degrade, alert operators</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unexpected failures</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Conditions nobody predicted</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Log with context, stop safely, avoid corrupting data</td>
    </tr>
  </tbody>
</table>

Separating these kinds helps decide the response. A bug should not be hidden by a recovery attempt, while a temporary network failure should not crash the system.

## Principles of Good Error Handling

1. **Fail fast.** Detect a problem as close to its cause as possible and stop, instead of letting bad data travel and cause damage elsewhere. An error found at the point of entry is far easier to diagnose than one that appears three layers later.
2. **Never ignore errors.** Swallowing a failure, such as catching it and doing nothing, hides problems and creates mysteries. Every error should be handled, passed on, or logged, deliberately.
3. **Use exceptions or error results consistently.** Languages offer different mechanisms: exceptions that interrupt normal flow, or return values that carry an error. Choose according to the language convention and use one approach consistently. Exceptions keep the normal path uncluttered, and explicit results make failure paths visible.
4. **Use specific types of error.** A named error such as insufficient balance can be handled precisely, whereas a general failure forces guesswork.
5. **Provide context.** An error message should say what was being attempted, with what input, and why it failed, so that the cause can be found without a debugger.
6. **Separate normal logic from error handling.** Avoid cluttering the main path with checks; handle errors in well-defined places.
7. **Clean up reliably.** Release files, connections, and locks even when an error occurs, using the language constructs designed for it.
8. **Handle errors at the right level.** Deal with an error where there is enough knowledge to respond sensibly, and otherwise pass it upward, translating low-level errors into terms meaningful to the caller.
9. **Keep the system in a consistent state.** If an operation fails midway, undo partial changes or make the operation atomic, so that no half-finished state remains.

## The Problem of Null

Tony Hoare, who introduced the null reference in 1965, later called it his billion-dollar mistake, because the possibility that any reference may be missing has caused countless failures. Good practice includes:

- **Do not return a missing value when a meaningful alternative exists.** Return an empty collection instead of nothing, or a defined default object representing "no discount" (the **special case** pattern).
- **Do not pass missing values** to operations unless explicitly allowed.
- **Use types that make absence explicit,** such as optional values, where the language supports them, so that callers must handle the case.

## Validation

**Validate at the boundaries** of the system, where data enters from users, files, and other systems, since these cannot be trusted. Inside, between trusted components, rely on contracts and checks that find bugs, as Unit 5 described under design by contract. Validation should be thorough, checking type, range, format, and business rules, and should report all the problems found where possible, not only the first.

A principle sometimes quoted is Postel's law: be conservative in what you send and liberal in what you accept. It has value for tolerating minor differences between systems, but excessive leniency can hide errors and create security problems, so it should be applied with care.

## Defensive Programming

Defensive programming means writing code with the expectation that other code, and users, will make mistakes.

- Check inputs at boundaries and assumptions with **assertions** that stop the program during development when a condition thought to be impossible occurs.
- Prefer **safe defaults** and the **least privilege**.
- **Limit the damage** of failure with timeouts, limits on sizes and retries, and isolation of components.
- **Do not trust external data,** whatever its source.
- **Avoid over-defence.** Checking everything everywhere clutters code and can hide design problems. The contract approach states who is responsible for what, so that checks have a clear place.

## Reporting Errors

Different audiences need different messages.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Audience</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What they need</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">End user</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A clear, polite explanation and a way forward, without technical detail or blame</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Your card was declined. Please try another card.</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Developer or operator</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Full technical detail, the context, and a trace of how it happened, in a log</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Payment provider returned status 402 for order identifier, after 2 retries, at the given time</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Calling code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A specific error type or code it can handle</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Payment declined, with a reason code</td>
    </tr>
  </tbody>
</table>

Log errors with enough context, but never record secrets such as passwords or full card numbers.

## Recovery Strategies

- **Retry** transient failures, with limits and increasing delays, as the distributed systems topic described.
- **Fall back** to an alternative, such as cached data.
- **Degrade gracefully,** providing reduced function.
- **Compensate,** undoing earlier steps if a later one fails.
- **Abort safely,** leaving a clean state and a clear message.
- **Escalate** to a human, with an alert, when automatic recovery is not possible.

<!--
IMAGE PROMPT  ->  generate as images/02_fail_fast_vs_swallow.png   (16:9 explanatory diagram, place here)

Two timelines. Top, Swallowed error (red): a small fault at step 1 hidden, bad data travels through steps 2 to 4, failure appears far away at step 5. Bottom, Fail fast (green): the fault at step 1 stops the flow immediately with a clear message pointing at step 1.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: What Is Wrong?

1. A function catches every failure and does nothing, returning an empty result.
2. An error message reads: Something went wrong.
3. A function that looks up a customer returns nothing when the customer does not exist, and callers use the result without checking.

Case 1 swallows errors, hiding problems; it should handle specific errors, or let them rise, and log them. Case 2 gives no context or remedy; a useful message names the operation, the cause, and what the user can do. Case 3 is the null problem: the function should signal absence explicitly, for example with an optional result or a specific not-found error, so callers cannot overlook it.

## Conclusion

Error handling is the practice of detecting abnormal conditions, signalling them clearly, and responding in a controlled way, and defensive programming is the broader habit of writing code that anticipates misuse and failure, so that faults are caught early, contained, and reported instead of silently corrupting results. Robust software is distinguished by how it behaves when things go wrong.

Even careful code accumulates weaknesses of structure over time. The next topic gives names to the warning signs: code smells.
