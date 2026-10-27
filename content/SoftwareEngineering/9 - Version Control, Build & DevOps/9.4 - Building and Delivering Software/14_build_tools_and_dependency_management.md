## Introduction

A modern application typically consists of a small amount of original code and a very large amount of other people's code: libraries, frameworks, and tools, each of which depends on others in turn. Keeping all of it consistent, up to date, secure, and reproducible is a serious engineering problem in its own right. Build tools automate the steps of building, and dependency managers handle the libraries, and together they determine whether a project can be built reliably by anyone, anywhere, at any time.

**Definition:** Build tools automate the steps that turn source code into artefacts according to a declared description, and dependency management is the practice of declaring, resolving, versioning, and securing the external libraries and tools a project relies on, so that builds are repeatable and risks from third-party code are controlled.

<!--
IMAGE PROMPT  ->  generate as images/14_intro_build_tools_and_dependency_management.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A tree of dependency boxes: the Application at the top depends on Library A and Library B, which both depend on a shared Library C at two different versions, flagged with a warning, and a lock file card fixing exact versions.

ON-IMAGE TEXT: show a short bold title "Build Tools and Dependency Management" plus only these few labels, large and legible: Declare, Resolve, Lock. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Build Tools

A build tool reads a **description of the project** and carries out the necessary steps in the right order, running only what is needed. The principal kinds are:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Kind</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Idea</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples (by ecosystem)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Task runners and scripts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Named tasks, such as build, test, lint, run</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Make, npm scripts, simple shell or task files</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Declarative build systems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The project describes what it is and its dependencies, and the tool knows the standard lifecycle</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maven and Gradle for Java, Cargo for Rust, the Go toolchain</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Package and project managers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Handle dependencies, virtual environments, packaging, and publishing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">pip with its tools, Poetry, npm, Yarn</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Bundlers and transpilers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Combine, convert, and optimise source for deployment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Webpack, Vite, esbuild</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Large-scale build systems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fast, reproducible, cached builds of big codebases with many languages</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Bazel and similar tools</td>
    </tr>
  </tbody>
</table>

Good build tools share useful properties:

- **Declarative:** describe the desired outcome, not every step.
- **Incremental:** recompute only what changed, using a **dependency graph** of tasks.
- **Repeatable:** the same inputs give the same results.
- **Standardised:** one command builds and tests the project, for developers and for the pipeline alike.
- **Extensible** through plug-ins and configuration.

A project should be buildable by a newcomer with a **short, documented, single set of steps**.

## Dependencies

A **dependency** is software your project needs in order to be built or run.

- **Direct dependencies** are those you choose and name.
- **Transitive dependencies** are those your dependencies need, and so on down the chain. They are typically many times more numerous than the direct ones, and you rarely chose them.
- **Development dependencies** are used only for building and testing, such as test frameworks, and are not shipped.
- **Runtime dependencies** are needed when the software runs.

All are declared in a **manifest file** that lists each dependency and the versions that are acceptable.

## Versions and Ranges

Dependencies are identified by version, and usually follow semantic versioning, as the previous chapter described. A manifest may require:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Style</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Risk</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Exact version</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Only that version</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stable but must be updated by hand; may conflict with other requirements</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Compatible range</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Any later version up to the next major one, relying on the promise of compatibility</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Convenient, but a mistaken promise can break the build</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Open-ended range</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Any later version</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dangerous: a future breaking release can arrive unexpectedly</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Latest</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Whatever is newest at build time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Builds not repeatable</td>
    </tr>
  </tbody>
</table>

## Lock Files

A manifest says what is **acceptable**, and a **lock file** records what was actually **chosen**: the exact versions of every direct and transitive dependency, and often their checksums. Committing the lock file to version control ensures that:

- every developer and the build server use **identical** versions
- builds are **reproducible** over time
- updates are **deliberate**: changing the lock file is a reviewed change
- tampered or substituted packages are detected through checksums

Libraries meant for others to use often declare wide ranges, while **applications** pin exact versions through the lock file.

## Dependency Problems

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Response</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Version conflicts (the diamond problem)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two dependencies need incompatible versions of a third</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Choose compatible versions; update the dependencies; some ecosystems allow multiple versions side by side</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dependency hell</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A tangle of conflicting, outdated, or unavailable dependencies</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep the number small; update regularly; use lock files</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Abandoned libraries</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No longer maintained and no longer receiving fixes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Replace, fork, or isolate them behind your own interface</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Breaking updates</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A new version changes behaviour</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Read release notes; rely on tests; update in small steps</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Left-pad style removals</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A tiny package disappears from the registry; in 2016 the removal of a trivial package broke many builds worldwide</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use a private mirror or cache; avoid dependencies for trivial functions</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Bloat</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Many dependencies for small benefits</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Evaluate each: is it worth the risk and weight?</td>
    </tr>
  </tbody>
</table>

## Security of Dependencies

Third-party code runs with the same privileges as your own, so its flaws are your flaws.

- **Known vulnerabilities** are catalogued with identifiers, called CVEs. A flaw in a widely used library can expose huge numbers of systems: the 2021 vulnerability in a popular logging library known as Log4Shell affected a vast range of software.
- **Supply-chain attacks** deliberately compromise packages: a maintainer account is taken over, a malicious package is given a name similar to a popular one, or a trusted package is altered to steal data. Incidents such as the compromise of build software from a network management vendor in 2020 showed the scale of the risk.
- **Defences:**
  - **Automated scanning** of dependencies for known vulnerabilities, built into the pipeline.
  - **Automated update tools** that open pull requests for new versions, so updates arrive in small, tested steps.
  - **A software bill of materials (SBOM)** listing all components, so that when a new vulnerability is announced, you can tell whether you are affected.
  - **Checksums and signatures** to verify packages.
  - **Private registries or mirrors** with approval of what may be used.
  - **Least privilege** for build systems and credentials.
  - **Reviewing new dependencies** before adopting them: maintenance, popularity, licence, and size.

## Good Practice

1. **Declare everything** the project needs, and nothing it does not.
2. **Commit lock files** for applications.
3. **Update dependencies regularly,** in small steps, with automation and tests, instead of rarely and in large, risky jumps.
4. **Keep the dependency count modest.**
5. **Separate** development and runtime dependencies.
6. **Scan** for vulnerabilities and licence issues in every build.
7. **Isolate** third-party libraries behind your own interfaces where replacement may be needed.
8. **Document** how to set up and build the project.

<!--
IMAGE PROMPT  ->  generate as images/02_manifest_lock_and_transitive_tree.png   (16:9 explanatory diagram, place here)

Left: a manifest card listing three direct dependencies with version ranges. Middle: a tree expanding each direct dependency into many transitive ones. Right: a lock file card with exact versions and checksums, and a vulnerability scanner icon flagging one transitive dependency in red.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Manage the Dependency

1. A team builds on Monday with one set of library versions and on Friday with a newer set, and a test fails only on Friday.
2. A security scan reports a serious vulnerability in a library that your project does not use directly.
3. Two libraries your project uses depend on different, incompatible versions of a third library.

Case 1 is solved by a committed lock file, which fixes exact versions. Case 2 involves a transitive dependency: update or replace the direct dependency that brings it in, or override the version if the tool allows. In case 3, look for compatible versions of the two libraries, update them, or replace one.

## Conclusion

Build tools automate the steps that turn source code into artefacts according to a declared description, and dependency management is the practice of declaring, resolving, versioning, and securing the external libraries and tools a project relies on, so that builds are repeatable and risks from third-party code are controlled. Lock files, small regular updates, and automated scanning are the core disciplines.

Having made the build automatic and reliable, the next step is to run it, with the tests, on every change. The next topic describes continuous integration.
