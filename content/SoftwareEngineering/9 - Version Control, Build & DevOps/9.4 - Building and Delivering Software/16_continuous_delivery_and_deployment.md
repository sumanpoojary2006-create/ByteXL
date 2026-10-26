## Introduction

Continuous integration confirms that the code builds and passes its tests. Delivering it to users is a further set of steps: more testing in realistic environments, approvals, installation, configuration, and checks that it works in production. Where these steps are manual, releases are rare, stressful, and error-prone, and teams respond by releasing even less often, which makes each release larger and riskier. Continuous delivery breaks the cycle by automating the path to production so that releasing becomes routine.

**Definition:** Continuous delivery is the practice of keeping software in a releasable state at all times, by automatically moving every change through a deployment pipeline of builds, tests, and checks so that it can be deployed to production at any moment, and continuous deployment goes further by deploying every change that passes the pipeline automatically.

<!--
IMAGE PROMPT  ->  generate as images/16_intro_continuous_delivery_and_deployment.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A pipeline conveyor with stages Commit, Automated tests, Acceptance, Performance, Staging, then a gate labelled Release with a human hand on a button for Continuous delivery, and the gate automatically open for Continuous deployment.

ON-IMAGE TEXT: show a short bold title "Continuous Delivery and Deployment" plus only these few labels, large and legible: Pipeline, Ready, Release. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Distinction

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Practice</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What is automated</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Who decides to release</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Continuous integration</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Build and test of every change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not about release</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Continuous delivery</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Everything up to a production-ready artefact, with deployment possible at the push of a button</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A person or the business chooses when to release</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Continuous deployment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Everything including release to production for each change that passes all checks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The pipeline: no human step</td>
    </tr>
  </tbody>
</table>

The foundational book, *Continuous Delivery* by Jez Humble and David Farley (2010), defines the aim: make deployments **boring, routine events** that can happen on demand, at low risk, whenever the business wishes. Continuous deployment is appropriate for products and cultures that can accept it, such as many web services, while continuous delivery with a manual release decision suits organisations with approval needs, such as regulated industries or scheduled launches.

## The Deployment Pipeline

The **deployment pipeline** is the automated path from commit to production, in which confidence increases at each stage. Typical stages:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Stage</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical content</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Commit stage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fast feedback on the change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Build, unit tests, static analysis; builds the artefact once</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automated acceptance stage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Confirm the system meets business requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automated functional tests against a running system</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Non-functional stage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Check qualities</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Performance, load, security, and accessibility tests</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Exploratory and user acceptance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Human judgement where needed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Manual exploration, demonstrations, stakeholder checks</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Staging (pre-production)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rehearse the release in a production-like environment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deploy exactly as for production; smoke tests</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Production release</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deliver to users</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Controlled rollout and checks</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Post-release verification</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Confirm health</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automated smoke tests and monitoring</td>
    </tr>
  </tbody>
</table>

The same **artefact** passes through every stage, so that what was tested is what is released. A change that fails any stage is rejected, and the team is told at once.

## Principles

1. **Build the artefact once** and promote it through environments.
2. **Automate everything repeatable:** builds, tests, deployments, database changes, configuration.
3. **Keep the main line always releasable.** If it is broken, fixing it is the first priority.
4. **Make small changes.** Small releases are easier to test, understand, and reverse.
5. **Everyone is responsible** for the release, not a separate handover team.
6. **Deploy the same way everywhere,** so that deployment to production has been rehearsed many times.
7. **Fail fast and visibly,** with feedback to the person who caused the failure.
8. **Continuously improve** the pipeline, using measurements.

## Handling Data and Unfinished Work

Two practical problems complicate frequent release.

- **Database changes.** Schema changes must be applied automatically and safely, and must be compatible with both the old and new versions of the application during the rollout. The approach, often called **expand and contract**, adds new structures first, moves the application to use them, and removes the old ones only later, in separate steps.
- **Unfinished features.** Work that is not ready can be merged and deployed but kept **hidden behind a feature flag**, so that deploying code is separated from releasing the feature to users. The release strategies topic covers this.

## Measuring Delivery Performance

Research by the DevOps Research and Assessment (DORA) programme, summarised in the book *Accelerate* by Nicole Forsgren, Jez Humble, and Gene Kim (2018), identified measures that distinguish high-performing teams and showed that speed and stability go together, not in opposition.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Measure</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deployment frequency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How often the team releases to production</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lead time for changes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Time from a commit to its running in production</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Change failure rate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The proportion of releases that cause a failure needing a fix or rollback</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Time to restore service</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How quickly the team recovers from a failure in production</td>
    </tr>
  </tbody>
</table>

Later versions of the research add reliability as a further dimension. High performers deploy often, with short lead times, low failure rates, and fast recovery. The measures are meant for **improving the system**, not for ranking people.

## Benefits

- **Lower risk** because each release is small.
- **Faster feedback** from real users.
- **Faster time to value:** finished work reaches users without waiting.
- **Less stress:** releases are no longer special, late-night events.
- **Better quality,** since automation tests everything the same way every time.
- **Easier diagnosis,** since few changes are in each release.
- **Higher morale and productivity.**

## Prerequisites and Challenges

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Challenge</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Remedy</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Weak automated tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Invest in the test suite; it is the basis of confidence</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Manual environments and configuration</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automate them, as the next topics describe</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Slow, long pipelines</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Parallelise and prune; keep the commit stage fast</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tightly coupled architecture that must be released as a whole</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Move towards modularity and independent deployment</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Approval and compliance requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automate evidence collection; integrate approvals into the pipeline; use continuous delivery with a gate</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cultural resistance and fear</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Start small; demonstrate benefits; build safety nets such as quick rollback</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Large database or infrastructure changes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Expand-and-contract; staged rollouts</td>
    </tr>
  </tbody>
</table>

<!--
IMAGE PROMPT  ->  generate as images/02_delivery_vs_deployment_and_dora.png   (16:9 explanatory diagram, place here)

Top: two pipelines identical up to a release gate; the first with a manual button labelled Continuous delivery and the second with an automatic arrow labelled Continuous deployment. Bottom: four DORA measure gauges Deployment frequency, Lead time, Change failure rate, Time to restore.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Delivery or Deployment?

1. A change passes all automated checks, is automatically released to production within minutes, and nobody approves it.
2. A change passes all checks and waits in a releasable state until the business decides on the launch date.
3. A team measures the average time between a commit and its running in production.

Case 1 is continuous deployment. Case 2 is continuous delivery. Case 3 measures lead time for changes, one of the four key delivery measures.

## Conclusion

Continuous delivery is the practice of keeping software in a releasable state at all times, by automatically moving every change through a deployment pipeline of builds, tests, and checks so that it can be deployed to production at any moment, and continuous deployment goes further by deploying every change that passes the pipeline automatically. Small, frequent, automated releases are safer and faster than large, rare, manual ones.

A pipeline moves software through a series of environments. The next chapter describes environments and the infrastructure beneath them, beginning with how they are configured.
