## Introduction

Teams used to work separately for weeks and then try to combine everyone's work in a final "integration phase." It was usually painful: pieces that worked alone failed together, defects were hard to trace to their cause, and release dates slipped while people untangled the mess. Continuous integration reverses the approach by combining work constantly, so that problems are discovered within minutes, while the change that caused them is still fresh and small. It is the foundation on which continuous delivery and DevOps are built.

**Definition:** Continuous integration is the practice of frequently merging every developer's work into a shared main line and automatically building and testing each change, so that integration problems are detected immediately and the main line is kept in a working state.

<!--
IMAGE PROMPT  ->  generate as images/15_intro_continuous_integration.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Developers pushing small changes in a loop into a central trunk, with an automatic build and test machine producing a green or red light for each push, and an alert bell on red.

ON-IMAGE TEXT: show a short bold title "Continuous Integration" plus only these few labels, large and legible: Integrate, Verify, Fast. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Idea

The practice was developed within Extreme Programming and described by Martin Fowler and Matthew Foemmel around 2000, and in a widely read article revised in 2006. Its core:

1. Developers **integrate their work into the shared main line at least daily.**
2. Each integration is **verified by an automated build and test run** on a separate machine.
3. If the verification fails, **fixing it is the team's top priority.**

The result is that the main line is, at nearly all times, in a known good state.

## Practices of Continuous Integration

Fowler's description lists habits, which can be summarised:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Practice</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maintain a single shared repository</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Everything needed to build lives in version control</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automate the build</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One command or trigger builds the whole system</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Make the build self-testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automated tests run as part of every build</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Everyone commits to the main line frequently</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">At least daily, in small steps</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every commit builds on an integration machine</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A server verifies each change, not just the developer laptop</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fix broken builds immediately</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A red build is stopped-the-line work for the team</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep the build fast</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ideally minutes; slow feedback defeats the purpose</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test in an environment like production</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reduces surprises</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Make the latest build easy to get and see</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Anyone can find the current state</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Make results visible to everyone</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dashboards, notifications, status indicators on the change</td>
    </tr>
  </tbody>
</table>

## A Typical CI Pipeline

A pipeline is a series of **stages**, each running only if the previous one passed, ordered so that the quickest checks run first and give early feedback.

1. **Trigger:** a push or a pull request starts the pipeline.
2. **Check out** the code and **restore** cached dependencies.
3. **Static checks:** formatting, linting, and security scans.
4. **Build** the software.
5. **Unit tests:** fast, many, isolated.
6. **Integration tests:** parts working together, perhaps with real databases started for the purpose.
7. **Package** the artefact and **publish** it to the repository.
8. **Report** the results to the change, with logs and coverage.

Longer checks, such as end-to-end tests or performance tests, may run on a schedule or in a later pipeline stage, as the continuous delivery topic describes.

## Pre-Merge and Post-Merge Checks

- **Pre-merge (pull request) checks** run on the proposed change before it joins the main line, and block merging if they fail. They protect the main line.
- **Post-merge checks** run on the main line itself after merging, because the combination of several merged changes may fail even if each passed alone, and to produce the official artefact.

## Benefits

- **Early detection:** problems are found within minutes of introduction, so the cause is obvious.
- **Reduced integration risk:** no large, painful merges.
- **A releasable main line,** so that release becomes a business decision, not a technical crisis.
- **Confidence to change code,** supported by tests that run all the time.
- **Fast feedback** to developers.
- **Visibility** of the project health.
- **Less manual work:** repetitive checking is automated.

## What CI Requires

- **A good automated test suite.** CI without tests only checks that the code compiles. The value comes from the tests, which Unit 10 covers.
- **A fast, reliable build.**
- **A team culture** of small changes and of treating a broken build as urgent.
- **Reliable infrastructure** for the build server and its environments.

## Common Problems

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Effect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Remedy</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Slow builds</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Developers stop waiting for feedback and batch their changes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Parallelise; cache; split tests into fast and slow groups; use faster machines</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Flaky tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tests that sometimes fail for no reason destroy trust, and people ignore red builds</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Find and fix or quarantine them with a plan to repair; track flakiness</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Broken builds left unfixed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The main line cannot be trusted</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Agree a rule: fix or revert within minutes</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Infrequent integration</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Large changes and painful merges return</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Commit small; use feature flags for unfinished work</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Works on CI but not locally, or the reverse</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Environment differences</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use containers or declared environments so that both match</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Secrets in pipelines</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Leaks of credentials</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use the secure secret stores of the CI service; limit access</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pipelines no one maintains</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Configuration decays</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Treat pipeline definitions as code, versioned and reviewed</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Measuring only success rate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hides problems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Also track build time, time to fix, and flakiness</td>
    </tr>
  </tbody>
</table>

## Tools

Continuous integration is provided by services and servers such as Jenkins, GitHub Actions, GitLab CI, CircleCI, and similar products. Pipelines are described in **configuration files stored in the repository** (**pipeline as code**), so that they are versioned, reviewed, and reproducible, and changes to the process follow the same workflow as changes to the code.

## CI and Branching

Continuous integration truly means integrating **continuously**. A team that keeps branches for weeks and runs a CI server on them is running automated builds, but is not practising continuous integration, since the work is not combined. This is why trunk-based development and short-lived branches pair with it.

<!--
IMAGE PROMPT  ->  generate as images/02_ci_pipeline_stages_and_feedback.png   (16:9 explanatory diagram, place here)

A left-to-right pipeline: Commit, Static checks, Build, Unit tests, Integration tests, Package, Publish, with stage durations in seconds and minutes beneath, quickest first. A red failure at Unit tests sends a notification bell back to the developer within minutes, and a loop labelled Fix immediately.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Is This CI?

1. A team runs an automated build every night on a server, while developers keep their own branches for three weeks.
2. Every proposed change triggers a build and the test suite, which takes six minutes, and merging is blocked until it passes.
3. The build has been failing for two days and nobody has looked.

Case 1 runs automation but does not integrate continuously, so it is not true CI. Case 2 is a healthy CI practice. Case 3 breaks the central rule: a broken build must be fixed or reverted immediately.

## Conclusion

Continuous integration is the practice of frequently merging every developer's work into a shared main line and automatically building and testing each change, so that integration problems are detected immediately and the main line is kept in a working state. Its value depends on good tests, fast builds, and a team that treats a red build as urgent.

With a main line that is always working, the next step is to keep it always ready to release. The next topic describes continuous delivery and continuous deployment.
