## Introduction

Git allows teams to use branches in many ways, which is both its strength and a source of confusion. Without an agreed convention, every developer chooses differently, long-lived branches multiply, and nobody is sure which branch is current or safe to release. A branching strategy is a team agreement on which branches exist, what each is for, how work moves between them, and how releases are cut. The right one depends mainly on how often the software is released and how the team is organised.

**Definition:** A branching strategy is an agreed workflow that defines the branches a team uses, their purposes and lifetimes, and the rules for moving changes between them and into releases, chosen to balance stability, speed of integration, and the way the software is delivered.

<!--
IMAGE PROMPT  ->  generate as images/07_intro_branching_strategies.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Three small branch diagrams side by side labelled Git Flow, GitHub Flow, Trunk-based, with branch lifetimes shown by line length: long for Git Flow, medium for GitHub Flow, very short for Trunk-based.

ON-IMAGE TEXT: show a short bold title "Branching Strategies" plus only these few labels, large and legible: Flow, Lifetime, Release. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## What a Strategy Decides

- Which **long-lived branches** exist, such as the main line, and what each represents.
- How **short-lived work branches** are named, created, and merged.
- How **releases** are prepared and marked.
- How **urgent fixes** reach production.
- Which **checks and reviews** guard each step.

## Git Flow

Proposed by Vincent Driessen in 2010, **Git Flow** uses several branches with defined roles.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Branch</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Lifetime</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">main (or master)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Holds released, production-ready code; each commit corresponds to a release</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Permanent</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">develop</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Integration branch for the next release</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Permanent</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">feature branches</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Individual new features, created from develop and merged back into it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Days to weeks</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">release branches</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Preparation of a release: final fixes and version changes, then merged to main and develop</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Short, per release</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">hotfix branches</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Urgent fixes to production, from main, merged to both main and develop</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Very short</td>
    </tr>
  </tbody>
</table>

**Strengths:** clear structure, suits software with **scheduled, versioned releases** and several supported versions at once, such as installed products. **Weaknesses:** complexity, many merges, long-lived branches that diverge, and a delay between a change being written and its reaching production. Driessen himself later noted that it is not ideal for software that is delivered continuously, such as web applications.

## GitHub Flow

A much simpler approach, popularised by GitHub, with a single rule: **the main branch is always deployable.**

1. Create a branch from main for each piece of work, with a descriptive name.
2. Commit and push regularly.
3. Open a pull request to discuss and review.
4. Run the automated checks.
5. Merge into main after approval.
6. Deploy from main, often immediately.

**Strengths:** simple, fast, well matched to continuous delivery and web services. **Weaknesses:** gives no structure for maintaining several released versions at once, and relies on strong automated testing to keep main safe.

## GitLab Flow

A variation that adds **environment or release branches** to the simple model: for example, main flows into a staging branch and then a production branch, so that what is running in each environment is visible in the repository, and release branches are used when versions must be supported.

## Trunk-Based Development

In **trunk-based development**, all developers integrate their work into a single shared main line, the **trunk**, at least daily, either by committing directly or through very short-lived branches that last hours and not days. Unfinished work is hidden behind **feature flags** so that incomplete features can be merged without affecting users. Releases are made from the trunk, or from short-lived release branches cut from it.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Detail</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Strengths</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Minimal merge pain, because integration is constant; fast feedback; supports continuous integration in its true meaning; research on software delivery performance, from the DORA programme, associates it with high-performing teams</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Strong automated tests, fast builds, a culture of small changes, and feature flags</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Weaknesses</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs discipline and tooling; can feel risky to teams without good tests</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Suited to</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Teams practising continuous integration and delivery, particularly web services</td>
    </tr>
  </tbody>
</table>

## Comparing the Strategies

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Git Flow</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">GitHub Flow</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Trunk-based development</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Long-lived branches</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Several</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Work branch lifetime</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Days to weeks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Days</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hours to a day or two</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Release style</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scheduled, versioned</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Continuous</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Continuous</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Complexity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low, but needs strong practices</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Risk of large merges</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Moderate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs feature flags</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rarely</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sometimes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Often</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Supporting multiple released versions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Natural</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Awkward</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Possible with release branches</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Typical product</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Installed software, libraries, mobile apps with slow release</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Web applications and services</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Web applications and services at scale</td>
    </tr>
  </tbody>
</table>

## Long-Lived Branches and Their Cost

Whichever strategy is used, the longer a branch lives apart from the main line, the greater the **integration debt**: the larger the eventual merge, the more conflicts, the higher the chance of semantic breakage, and the later feedback arrives. This is sometimes called **merge hell**. A guideline across all approaches is to **keep branches as short-lived as possible**.

## Release Branches

When several versions must be maintained, as with a library used by many customers, a **release branch** is created from the main line at the point of release. Fixes for that version are made on it, and important fixes are also applied to the main line, often by selecting individual commits to copy across, a technique described in the next topics.

## Choosing a Strategy

Questions to ask:

1. **How often do you release,** and is it continuous or scheduled?
2. **How many versions must you support** at the same time?
3. **How strong is your test automation?** Light branching depends on it.
4. **How large and distributed is the team?**
5. **What are the regulatory or approval requirements?**
6. **What does the team already know?**

Start with the **simplest** approach that fits, write it down, enforce it with branch protection, and revisit it when needs change.

<!--
IMAGE PROMPT  ->  generate as images/02_three_branching_strategies.png   (16:9 explanatory diagram, place here)

Three commit graphs. Git Flow: main, develop, feature, release, hotfix lines with merges. GitHub Flow: main with short feature branches merged by pull requests. Trunk-based: a single trunk with tiny short branches and feature flag markers on commits. Each has a caption for release style.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Which Strategy?

1. A web application is deployed to production several times a day by a small team with strong automated tests.
2. A desktop product ships a new version every six months, and the previous two versions must still receive fixes.
3. A team finds that features are being merged only after three weeks of isolated work and merges are painful.

Team 1 fits GitHub Flow or trunk-based development. Team 2 fits Git Flow, or release branches cut from the main line. In case 3, the problem is long-lived branches: shorten them, integrate more often, and use feature flags to merge unfinished work safely.

## Conclusion

A branching strategy is an agreed workflow that defines the branches a team uses, their purposes and lifetimes, and the rules for moving changes between them and into releases, chosen to balance stability, speed of integration, and the way the software is delivered. The simplest strategy that fits the release style, with branches kept short, is usually the best.

Whatever the branching strategy, changes are normally examined by others before they join the shared line. The next topic describes the pull request and code review workflow.
