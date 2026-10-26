## Introduction

Deploying a new version to production is a moment of risk. However well tested, software behaves differently under real traffic, data, and use. The way a release is carried out determines how many users are exposed to a problem, how quickly it is noticed, and how fast it can be undone. Release strategies are techniques for putting new versions into production gradually and safely, with the ability to retreat. Together with the feature flags described here, they let teams release often without fear.

**Definition:** A release strategy is a planned method for moving a new version of software into production, such as rolling, blue-green, or canary deployment, chosen to limit the number of users exposed to a fault, to avoid downtime, and to allow quick reversal.

<!--
IMAGE PROMPT  ->  generate as images/20_intro_release_strategies.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Four small panels: Rolling (instances replaced one by one), Blue-green (two environments with a switch), Canary (a small slice of traffic going to the new version), Feature flag (a toggle switch on a feature).

ON-IMAGE TEXT: show a short bold title "Release Strategies" plus only these few labels, large and legible: Roll, Switch, Canary, Flag. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Deployment and Release Are Different

A key idea of modern practice is to **separate deploying from releasing.**

- **Deployment** is putting a new version of the code onto production infrastructure.
- **Release** is making a feature available to users.

With these separated, code can be deployed frequently and safely, with new behaviour hidden until the team decides to release it, to everyone or to some. This reduces the pressure and risk of each event.

## Strategies

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strategy</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">How it works</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Advantages</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Disadvantages</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Recreate (big bang)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stop the old version, then start the new one</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simplest; no two versions at once</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Downtime; all users exposed at once; slow to undo</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rolling update</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Replace instances of the old version with the new one gradually, a few at a time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No downtime; limited extra capacity needed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Old and new versions run together for a while, so they must be compatible; slower rollback</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Blue-green</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Run two identical environments: the live one (blue) and the idle one (green). Deploy to the idle one, test, then switch traffic to it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Instant switch and rollback by switching back; testing in a production-like place</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs double the infrastructure for a time; database changes must work with both versions</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Canary</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Release to a small percentage of users or servers first, watch the results, and increase gradually</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Limits the number of users exposed; real-world evidence before full release</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs good monitoring and traffic control; takes longer</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shadow (dark traffic)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Copy real traffic to the new version, without returning its results to users</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tests with real load and data without risk to users</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Complex; side effects must be avoided</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A/B testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Show different versions to different user groups to compare results</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Measures the effect on behaviour, not just correctness</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A purpose is experiment, not safety; needs statistics</td>
    </tr>
  </tbody>
</table>

The word **canary** comes from the practice of miners carrying canaries as an early warning of danger: a small group of users is the early warning for the whole.

## Feature Flags

A **feature flag** (or toggle) is a switch, controlled by configuration and not by code changes, that determines whether a feature is active. Pete Hodgson's widely read article distinguishes types.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Type</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Lifetime</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Release flag</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hide unfinished or newly deployed features until ready; supports merging to the main line early</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Short; remove after release</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Experiment flag</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Support A/B tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Short, for the length of the experiment</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operations flag (kill switch)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Turn off a feature quickly under load or fault</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">May be long-lived</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Permission flag</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Enable features for certain users or plans</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Long-lived</td>
    </tr>
  </tbody>
</table>

Flags allow **gradual rollout** (one percent of users, then ten, then all), **targeting** (staff first, then a region), and **instant disabling** of a feature without redeploying. They also bring costs: more paths to test, complexity in the code, and **flag debt** if old flags are never removed. Good practice names flags clearly, assigns an owner and an expiry, and removes them promptly.

## Rollback and Roll Forward

When a release goes wrong, there are two ways to recover.

- **Roll back:** return to the previous version. It is fast and well understood, but it is not always possible: if the new version changed data in ways the old version cannot read, going back may be unsafe.
- **Roll forward:** quickly release a fix on top. It suits small, frequent releases with fast pipelines.

The quicker and safer approach is often to **switch off the feature flag**, which avoids a redeployment entirely. Teams should **rehearse** recovery, not only deployment.

## Handling Databases

Changes to data structures are the hardest part of safe release, since a database is shared by the old and new versions during a rollout. The **expand and contract** (parallel change) pattern avoids breaking either:

1. **Expand:** add the new structure alongside the old one, compatible with both versions of the application.
2. **Migrate:** move the data and switch the application to the new structure, gradually if needed.
3. **Contract:** once nothing uses the old structure, remove it in a later release.

Each step is separately deployable and reversible, so no step breaks a running version.

## Automated Verification and Rollback

Strong release processes **verify automatically**:

- **Smoke tests** immediately after deployment check that the key functions work.
- **Health checks** determine whether an instance is ready to receive traffic.
- **Monitoring of key measures,** such as error rates and response times, compared with a baseline, during a canary or rolling release.
- **Automatic rollback or halt** if the measures cross thresholds.

This closes the loop with the monitoring topic that follows: a release strategy is only as safe as the team's ability to see what is happening.

## Progressive Delivery

**Progressive delivery** is the name given to combining these techniques: deploy continuously, release gradually using flags and canary analysis, watch the effect, and expand or retreat according to evidence. It treats release as a controlled experiment rather than a single leap.

## Choosing

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Situation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Suitable strategy</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simple internal tool, downtime acceptable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Recreate</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stateless service, steady changes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rolling update</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Need instant rollback and strong pre-release testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Blue-green</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High-traffic service where faults are costly</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Canary, with automated analysis</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unfinished feature on the main line; gradual exposure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Feature flag</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Need to test new logic safely with real traffic</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shadow traffic</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Need evidence of user impact</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A/B test</td>
    </tr>
  </tbody>
</table>

<!--
IMAGE PROMPT  ->  generate as images/02_canary_and_blue_green.png   (16:9 explanatory diagram, place here)

Left: blue-green, two environments with a router switch pointing at the blue one and a dotted arrow to the green one, labelled Switch and instant rollback. Right: canary, a traffic bar split 95 percent to old version and 5 percent to new, with a metrics panel and arrows increasing the share to 25, 50, 100 percent, and an abort arrow on error.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Choose the Strategy

1. A team wants to test a new checkout flow with one percent of real users before exposing everyone.
2. A team needs to be able to return instantly to the old version if the new one misbehaves.
3. A feature is not finished, but the code must be merged into the main line today.

Case 1 is a canary release or a flag-based gradual rollout. Case 2 suits blue-green deployment, where rollback is a switch back. Case 3 suits a feature flag: deploy the code, hide the feature.

## Conclusion

A release strategy is a planned method for moving a new version of software into production, such as rolling, blue-green, or canary deployment, chosen to limit the number of users exposed to a fault, to avoid downtime, and to allow quick reversal. Separating deployment from release, using flags, and verifying automatically make frequent releases safe.

Once software is running, the team must know how it is behaving. The next chapter turns to operating software in production, beginning with monitoring, logging, and observability.
