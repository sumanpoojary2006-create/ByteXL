## Introduction

Source code is what developers write, and it is not what users run. Between the two lies a series of transformations: dependencies are fetched, code is compiled or bundled, tests are run, and the result is packaged into something that can be installed or started on a server. This process is called the build, and its output is the **artefact** that is actually delivered. Understanding it explains why "it works on my machine" happens, why builds are automated, and why the same artefact should be tested and then deployed unchanged.

**Definition:** Building software is the automated process of transforming source code and its dependencies into a runnable, deployable artefact, through steps such as compiling, bundling, testing, and packaging, so that what is delivered to users can be produced reliably from a specific version of the source.

<!--
IMAGE PROMPT  ->  generate as images/13_intro_from_source_code_to_deployable_software.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A left-to-right production line: Source code and Dependencies entering, stations labelled Compile, Test, Package, Sign, and a finished sealed box labelled Artefact leaving to a registry shelf.

ON-IMAGE TEXT: show a short bold title "From Source Code to Deployable Software" plus only these few labels, large and legible: Source, Build, Artefact. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## What Happens in a Build

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Step</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fetch dependencies</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Obtain the libraries and tools the project needs, at the right versions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Downloading packages from a registry</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Generate code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Produce code from specifications or templates</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Interface stubs from a definition file</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Compile or transform</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Translate source into a form that can run</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Compiling to machine code or bytecode; converting newer language features to older ones</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Bundle and optimise</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Combine many files into fewer and reduce their size</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Joining scripts and removing unnecessary characters</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Run automated checks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unit, integration, and static analysis checks</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Package</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Assemble everything into a standard deliverable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An installer, an archive, a library package, a container image</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sign and verify</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Attach proof of origin and integrity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cryptographic signatures and checksums</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Publish</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Store the artefact where it can be retrieved</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An artefact repository or registry</td>
    </tr>
  </tbody>
</table>

Not every language compiles: some are interpreted, and some, like those running on a virtual machine, compile to an intermediate form. Even interpreted projects have a build step to install dependencies, process assets, run checks, and package.

## Source, Build, and Run

It helps to separate three times.

- **Source time:** the code and configuration in the repository.
- **Build time:** when the source is turned into an artefact.
- **Run time:** when the artefact executes in an environment.

Mistakes happen when these are blurred. For example, anything that differs between environments, such as database addresses, should be provided at run time and not baked into the artefact at build time, so that the same artefact works everywhere.

## Artefacts

An **artefact** is a produced file or bundle that is stored and delivered. Examples are an executable, a library archive, a web application bundle, or a container image. Good practice treats artefacts as:

- **Versioned and traceable:** each is labelled with a version and linked to the exact commit and build that produced it.
- **Immutable:** once built and published, it is never changed. A new change makes a new artefact.
- **Stored centrally** in an artefact repository, which provides a reliable source for deployment, with retention and access control.
- **Built once and deployed many times:** the same artefact is promoted through test, staging, and production, instead of being rebuilt for each. What was tested is exactly what is released.

## Types of Build

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Kind</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Characteristics</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Debug (development) build</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Easy diagnosis while developing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Includes extra information, no heavy optimisation, may be slower</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Release (production) build</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What users receive</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Optimised, stripped of debugging aids, often signed</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Incremental build</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rebuild only what changed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fast feedback during development</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clean (full) build</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Build everything from scratch</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Slower; verifies that the build does not depend on leftover files</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nightly or scheduled build</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Regular full builds on a server</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Catches problems with long-running or rarely run steps</td>
    </tr>
  </tbody>
</table>

## Reproducible Builds

A build is **reproducible** if the same source and the same declared inputs always give the same output. This matters for debugging (can we rebuild exactly what was released?), for security (can anyone verify that the artefact really comes from the published source?), and for trust. To achieve it:

- Pin the **versions** of all dependencies and tools.
- Build in a **clean, controlled environment,** such as a build server or container, not on an individual laptop with unknown settings.
- Avoid embedding **timestamps** and machine-specific details.
- Record **how** each artefact was built.

## Where Builds Run

Developers build locally for quick feedback. The **official** builds are done on a shared build server, in a clean environment, triggered by changes in the repository, which removes the dependence on any one person's machine. The topic on continuous integration describes this.

## Making Builds Fast

Slow builds slow every developer and discourage frequent integration. Common remedies:

- **Incremental builds** and **caching** of results that have not changed.
- **Parallel execution** of independent steps.
- **Splitting** large projects into modules that build independently.
- **Faster test stages first,** with the slowest run later.
- **Powerful build machines** and distributed caches.

A rough aim often quoted for the main build and test cycle is **about ten minutes or less**.

## Build Failures

A build can fail because of a compile error, a failing test, a missing or incompatible dependency, an environment difference, a resource limit, or a flaky external service. Clear **error messages**, logs kept for each build, and a team habit of **fixing a broken build immediately** keep the shared main line healthy.

<!--
IMAGE PROMPT  ->  generate as images/02_build_once_deploy_many.png   (16:9 explanatory diagram, place here)

A pipeline: Source commit (version label) goes through Build and Test, producing one Artefact stored in a Registry. From the registry, the same artefact is promoted to Test, Staging, and Production environments, each with its own configuration injected at run time. A note reads Same artefact everywhere.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Spot the Problem

1. A team rebuilds the application separately for staging and for production.
2. A database address is written into the code, so a different build is needed for each environment.
3. Nobody can rebuild the version released last year because the build depended on a laptop with specific tools installed.

Case 1 breaks build once, deploy many: what was tested in staging is not guaranteed to be what runs in production. Case 2 mixes configuration with the artefact; configuration should be supplied at run time. Case 3 is a reproducibility failure: builds should run in a controlled environment with pinned inputs.

## Conclusion

Building software is the automated process of transforming source code and its dependencies into a runnable, deployable artefact, through steps such as compiling, bundling, testing, and packaging, so that what is delivered to users can be produced reliably from a specific version of the source. Immutable, traceable, reproducible artefacts built once and deployed many times are the foundation of reliable delivery.

Builds rely on tools and on libraries written by others. The next topic describes build tools and dependency management.
