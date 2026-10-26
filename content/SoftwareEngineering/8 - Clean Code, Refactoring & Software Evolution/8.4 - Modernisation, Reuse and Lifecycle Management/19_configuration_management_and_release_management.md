## Introduction

A software product is not one file but thousands: source code, configuration, libraries, build scripts, documents, test data. Many people change them at the same time, and many versions exist in many places: on developer machines, in test environments, in production, and in the hands of customers. Without discipline, nobody can say with confidence which version is running where, what changed between two releases, or how to reproduce a version from last year. Configuration management and release management supply that discipline.

**Definition:** Configuration management is the practice of identifying, controlling, recording, and auditing the items that make up a software system and their versions, so that any version can be reproduced and changes are deliberate, and release management is the planning, building, testing, and delivery of those versions to users in a controlled way.

<!--
IMAGE PROMPT  ->  generate as images/19_intro_configuration_management_and_release_management.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A pipeline of numbered release boxes version 1.0, 1.1, 1.2, each stamped with a baseline seal, travelling from a Development area through Test and Staging to Production, with a change control gate before release.

ON-IMAGE TEXT: show a short bold title "Configuration and Release Management" plus only these few labels, large and legible: Identify, Control, Release. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Software Configuration Management

The standard definition, drawn from IEEE standards, divides configuration management into four activities.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Activity</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Configuration identification</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Decide what items are controlled and give each a unique name and version</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Source files, build scripts, configuration files, libraries and their versions, documents, database schemas</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Configuration control</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Control how changes to those items are proposed, reviewed, approved, and made</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reviewed changes in version control; a change control board for significant ones</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Configuration status accounting</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Record and report the state of items and changes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Which version is deployed in each environment; the history of changes</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Configuration audit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Verify that the delivered system matches what was intended</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Checking that a release contains exactly the approved changes</td>
    </tr>
  </tbody>
</table>

## Key Concepts

- **Configuration item:** anything placed under control, with an identity and a version.
- **Baseline:** a version of a set of items that has been formally reviewed and agreed, serving as the basis for later work. Changes to a baseline go through change control.
- **Version control:** the tool that records every change, supports branching and merging, and allows any past state to be recovered, as Unit 9 describes.
- **Build reproducibility:** the ability to produce exactly the same software from the same inputs, which requires that all inputs, including dependencies and tools, are versioned.
- **Environment configuration:** settings that differ between development, test, and production are kept separate from code, stored and versioned, with secrets handled securely.
- **Change request:** a recorded proposal to change a controlled item, which is assessed, approved or rejected, and tracked.
- **Software bill of materials (SBOM):** a list of all components and dependencies in a release, supporting security and licence checks.

## Versioning

A clear scheme tells users what to expect. **Semantic versioning** uses three numbers, MAJOR.MINOR.PATCH.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Number</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Increase when</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning for users</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">MAJOR</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Changes are made that are not backward compatible</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Upgrading may require changes by users</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">MINOR</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Functionality is added in a backward-compatible way</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Safe to upgrade; new features available</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">PATCH</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Backward-compatible bug fixes are made</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Safe to upgrade; fixes only</td>
    </tr>
  </tbody>
</table>

Pre-release labels, such as beta or release candidate, mark versions not yet final.

## Release Management

Release management covers the whole path from approved changes to a running release.

1. **Plan:** decide what goes into each release, when, and with what criteria for readiness.
2. **Build:** produce the release from controlled sources in an automated, reproducible way.
3. **Test:** verify the release, including regression, performance, security, and upgrade tests.
4. **Approve:** confirm that the release meets its criteria.
5. **Deploy:** deliver to production, staged and monitored, using the release strategies described in Unit 9, such as canary releases and feature flags.
6. **Communicate:** inform users and support with release notes, upgrade instructions, and known issues.
7. **Monitor and support:** watch behaviour after release and be ready to roll back or issue a fix.
8. **Review:** learn from each release to improve the next.

## Types of Release

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Type</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical cadence</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Major release</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Significant new capabilities, possibly with incompatible changes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Infrequent, planned</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Minor release</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">New features in a compatible way</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Regular</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Patch release</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Bug fixes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">As needed</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hotfix (emergency fix)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Urgent repair of a serious problem in production</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Immediate, with a streamlined process</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Continuous release</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Small changes released many times a day</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Continuous, with strong automation</td>
    </tr>
  </tbody>
</table>

Release **cadence** is a trade-off. Frequent small releases reduce risk per release and give fast feedback, while infrequent large ones are heavier to test and riskier. Teams with strong automation tend to release often.

## Release Readiness

Typical criteria that a release must meet:

- all planned changes are complete and reviewed
- automated tests pass, and no unresolved serious defects remain
- performance and security checks are satisfactory
- documentation and release notes are ready
- deployment and rollback have been rehearsed
- support and operations are prepared
- approvals are recorded

## Support and Compatibility Policies

For software used by others, it is important to be clear about:

- **Supported versions:** which are receiving fixes and for how long, such as long-term support releases.
- **Compatibility promises:** what will not change within a major version.
- **Deprecation policy:** how features are announced as obsolete, how long they remain, and how users are guided to alternatives.
- **Upgrade paths:** how users move between versions, including data migration.

## Why It Matters

- **Reproducibility:** a past version can be rebuilt to investigate a problem reported by a customer.
- **Safety:** changes are reviewed, tested, and traceable.
- **Speed:** automation of builds and releases removes manual delays and errors.
- **Compliance:** regulated sectors require evidence of what was released and why.
- **Trust:** users know what to expect.

<!--
IMAGE PROMPT  ->  generate as images/02_baseline_and_release_path.png   (16:9 explanatory diagram, place here)

Top: a version line with release markers 1.0.0, 1.1.0, 1.1.1, 2.0.0 and notes MAJOR breaks compatibility, MINOR adds features, PATCH fixes bugs. Bottom: a release path with gates Plan, Build, Test, Approve, Deploy, Monitor and a rollback arrow from Monitor back to the previous release.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Version and Decide

1. A release fixes three bugs and changes no behaviour otherwise, from version 2.4.1. What is the new version?
2. A release adds a new report and keeps everything else compatible, from version 2.4.1.
3. A release removes an operation that clients use, from version 2.4.1.

The first becomes 2.4.2, a patch. The second becomes 2.5.0, a minor release. The third is not backward compatible and becomes 3.0.0, a major release, with a deprecation notice and upgrade guide.

## Conclusion

Configuration management is the practice of identifying, controlling, recording, and auditing the items that make up a software system and their versions, so that any version can be reproduced and changes are deliberate, and release management is the planning, building, testing, and delivery of those versions to users in a controlled way. Together they make a changing system dependable.

Every piece of software eventually reaches the end of its useful life. The final topic of this unit considers how that end should be managed, and what it means for software to be sustainable.
