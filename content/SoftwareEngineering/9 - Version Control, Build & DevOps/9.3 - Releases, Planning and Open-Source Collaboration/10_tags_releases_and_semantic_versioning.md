## Introduction

A repository contains thousands of commits, and most of them are not something anyone ever shipped. At some points, the team declares that this exact state is a release: the one customers will receive, support will diagnose, and developers may need to rebuild years later. Tags mark those points, release notes explain them, and version numbers tell users what to expect. A clear scheme for all three saves enormous confusion, and a consistent version number scheme lets software that depends on yours make safe decisions automatically.

**Definition:** A tag is a permanent, human-readable name attached to a specific commit, typically marking a release, and semantic versioning is a convention for numbering releases as MAJOR.MINOR.PATCH so that the number communicates whether an update is a fix, a compatible addition, or a breaking change.

<!--
IMAGE PROMPT  ->  generate as images/10_intro_tags_releases_and_semantic_versioning.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A commit timeline with flag markers at certain commits labelled v1.0.0, v1.1.0, v1.1.1, v2.0.0, and a version number badge MAJOR.MINOR.PATCH with three explanatory arrows.

ON-IMAGE TEXT: show a short bold title "Tags, Releases and Semantic Versioning" plus only these few labels, large and legible: Mark, Number, Explain. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Tags

A **tag** is a fixed label on a commit. Unlike a branch, which moves as new commits are added, a tag **stays where it is placed**, so it always refers to exactly the same snapshot.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Kind</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Use</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lightweight tag</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Just a name pointing to a commit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quick personal markers</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Annotated tag</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A full object with a tagger, date, and message, and optionally a cryptographic signature</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Official releases</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Signed tag</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An annotated tag signed so that others can verify its origin</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High-trust releases</td>
    </tr>
  </tbody>
</table>

Tags are normally treated as **immutable**: moving or deleting a published release tag breaks anyone who depends on it. A mistake in a release is corrected with a **new** version, not by changing the old one.

## What a Release Contains

A release is more than a tag. It usually bundles:

- the **tag** identifying the exact source state
- the **built artefacts**, such as installable packages, libraries, or container images
- **release notes** describing what changed
- **checksums or signatures** allowing users to verify integrity
- the **documentation** for that version
- a **list of dependencies** (a software bill of materials), where required

Hosting platforms provide a release page that gathers these.

## Release Notes and Changelogs

Users need to know what changed. Two related documents serve that need.

- A **changelog** is a cumulative, curated record of notable changes between versions, written for humans. The Keep a Changelog convention groups entries under headings such as Added, Changed, Deprecated, Removed, Fixed, and Security, with the most recent version first.
- **Release notes** accompany a particular release, highlighting what matters to its audience: new features, fixes, breaking changes, upgrade instructions, and known issues.

A changelog is **not** a dump of the commit log. Good entries are written from the user point of view. Teams using structured commit messages can generate a draft automatically and then edit it.

## Semantic Versioning

Semantic Versioning, proposed by Tom Preston-Werner, is a widely adopted scheme. A version has three numbers separated by dots.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Part</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Increase it when</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Reset</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example effect</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">MAJOR</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">You make **incompatible** changes to the public interface</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">MINOR and PATCH to zero</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">From 2.7.3 to 3.0.0</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">MINOR</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">You add **backward-compatible** functionality</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">PATCH to zero</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">From 2.7.3 to 2.8.0</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">PATCH</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">You make backward-compatible **bug fixes**</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nothing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">From 2.7.3 to 2.7.4</td>
    </tr>
  </tbody>
</table>

Further rules:

- The scheme depends on declaring a **public interface**, which the version numbers describe. What is public must be documented.
- **Version 0.y.z** is for initial development: anything may change at any time.
- **Version 1.0.0** declares the public interface stable.
- A **pre-release** label, such as alpha, beta, or release candidate, marks a version before the final one and sorts below it.
- **Build metadata** may be appended for identification and is ignored in precedence.
- Once released, the contents of a version **must not change**.

## Why Semantic Versioning Matters

Software depends on other software. When a project uses a library, it declares which versions it accepts. With semantic versioning, the dependency tool can safely accept new minor and patch versions automatically, because they promise compatibility, while a new major version is treated as a deliberate decision. The numbers are a **contract** between the author and the users. Breaking that contract, for example by removing a feature in a patch release, damages trust.

## What Counts as Breaking

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Breaking (requires MAJOR)</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Compatible (MINOR or PATCH)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Removing or renaming a public operation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Adding a new operation</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Changing the meaning of existing behaviour</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fixing a defect so behaviour matches the documentation</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Making an optional input required</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Adding an optional input with a sensible default</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Changing the format of returned data in a way that breaks consumers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Adding extra fields that old consumers can ignore</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Raising the minimum supported platform version, in many conventions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Internal refactoring with no visible effect</td>
    </tr>
  </tbody>
</table>

When in doubt, treat the change as breaking, and announce it.

## Calendar Versioning and Other Schemes

Not every project suits semantic versioning. **Calendar versioning** uses the date, such as a year and month, which suits applications and operating systems where users care about recency and not compatibility promises. Some projects combine schemes. The important thing is that the scheme is **documented and consistent**.

## Automating Releases

Releasing by hand is slow and error-prone. Teams automate:

- **Version calculation** from structured commit messages, as described earlier.
- **Tagging, building, and publishing artefacts** by the pipeline when a release is approved.
- **Changelog generation** and release page creation.
- **Publishing** to package registries.

A release is then a **repeatable, auditable** event with a known set of steps, a theme the DevOps chapters return to.

## Good Practice

- **Tag every release,** and use a consistent naming pattern for tags, such as a letter v followed by the version.
- **Never reuse or move a published version.**
- **Write release notes for users,** not for the team.
- **Announce deprecations** in advance, with guidance.
- **Keep the version number in one place** so that it cannot disagree between files.
- **Link versions to the commits** and the build that produced them, so any release can be traced and reproduced.

<!--
IMAGE PROMPT  ->  generate as images/02_semver_decision_flow.png   (16:9 explanatory diagram, place here)

A decision flow starting at Change made: Breaking change to public interface? yes leads to MAJOR bump (2.7.3 to 3.0.0), no then New compatible feature? yes leads to MINOR bump (2.8.0), no then Bug fix only? yes leads to PATCH bump (2.7.4). A tag flag is planted on the resulting commit.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Pick the Version

The current version is 1.4.2.

1. A release fixes two bugs without changing documented behaviour.
2. A release adds a new optional feature.
3. A release removes a documented operation that clients use.

Release 1 becomes 1.4.3. Release 2 becomes 1.5.0. Release 3 is breaking and becomes 2.0.0, with notice and migration guidance.

## Conclusion

A tag is a permanent, human-readable name attached to a specific commit, typically marking a release, and semantic versioning is a convention for numbering releases as MAJOR.MINOR.PATCH so that the number communicates whether an update is a fix, a compatible addition, or a breaking change. Clear tags, honest release notes, and disciplined version numbers make releases trustworthy and reproducible.

Releases are the end of a stream of planned work. The next topic describes how that work is planned and tracked with issues and project boards.
