## Introduction

Infrastructure, meaning the servers, networks, storage, and services on which software runs, can be created by hand or by description. Manual setup leaves each environment slightly different and impossible to reproduce exactly. Infrastructure as code takes the second route: the desired infrastructure is described in files, kept in version control, and created and changed by tools that read the description, so that environments can be reviewed, repeated, and rebuilt like any other software.

**Definition:** Infrastructure as code is the practice of defining and managing servers, networks, storage, and platform services through machine-readable definition files, kept in version control and applied by automated tools, so that infrastructure can be created, changed, reviewed, and reproduced like software.

<!--
IMAGE PROMPT  ->  generate as images/19_intro_infrastructure_as_code.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A definition file card on the left feeding through an automation machine into a set of identical cloud resources, servers, network, database, on the right, with a version control history beside the card.

ON-IMAGE TEXT: show a short bold title "Infrastructure as Code" plus only these few labels, large and legible: Describe, Apply, Repeat. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Problems It Addresses

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Manual infrastructure</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Infrastructure as code</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Servers configured by hand, each slightly different</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every server created from the same definition</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Setup knowledge lives in people and documents that are out of date</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The definition is the documentation, always current</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rebuilding after a failure is slow and uncertain</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rebuild by running the definitions again</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Changes are untracked and unreviewed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Changes go through version control, review, and testing</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test and production environments differ</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Same definitions create each, with different parameters</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scaling means repeating manual work</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scale by changing a number in a definition</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hard to audit who changed what</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The history of the definition files records it</td>
    </tr>
  </tbody>
</table>

## Core Ideas

### Declarative and Imperative

- **Declarative** definitions state the **desired end state**: "there should be three servers of this size, a database of this type, and a network with these rules." The tool works out what to create, change, or remove to reach it. Terraform and cloud templates such as CloudFormation work this way.
- **Imperative** definitions list the **steps** to carry out, in order, such as a script. Some configuration tools use a mixture.

Declarative approaches are generally preferred for infrastructure, because they are easier to reason about and can be rerun safely.

### Idempotence

An operation is **idempotent** if applying it repeatedly has the same effect as applying it once. A good infrastructure definition can be applied again and again: if the infrastructure already matches, nothing changes. This makes it safe to run automatically and to recover from partial failures.

### Desired State and Drift

The tool compares the **desired state** in the definitions with the **actual state** of the environment. Differences, called **drift**, caused by manual changes, are detected, and can be corrected by reapplying the definition or reported for investigation.

### Immutable Infrastructure

In the **mutable** approach, servers are updated in place over time, accumulating changes. In the **immutable** approach, a server is never modified after creation: to change it, a new one is built from the updated definition and the old one is discarded. The shorthand is **pets versus cattle**: pets are named, hand-cared servers, and cattle are interchangeable, numbered instances that are replaced when they misbehave. Containers and virtual machine images support the immutable approach.

## Categories of Tools

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Kind</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Provisioning</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Create the infrastructure: servers, networks, storage, services</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Terraform, OpenTofu, CloudFormation, Pulumi</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Configuration management</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Install and configure software on servers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ansible, Chef, Puppet</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Image building</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Create machine or container images</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Packer, container build tools</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Orchestration platforms</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Manage containers and their configuration declaratively</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Kubernetes resource definitions</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Policy as code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Express and automatically check rules the infrastructure must follow</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Policy languages and scanners</td>
    </tr>
  </tbody>
</table>

Some tools use their own specification languages, while others use general-purpose programming languages. The principles are the same.

## GitOps

**GitOps** extends the idea: the **Git repository is the single source of truth** for the desired state of the system, and an automated agent continuously compares the running system with the repository and brings it into line. A change to infrastructure is a pull request: reviewed, approved, merged, and applied automatically. The repository's history is the complete audit trail, and rollback is a revert.

## The Workflow

1. **Write or change** the definition files in a branch.
2. **Validate and test:** check syntax, scan for security and policy violations, and preview the changes the tool would make (often called a plan).
3. **Review** the change and the preview.
4. **Merge** it and apply it through an automated pipeline, to each environment in turn.
5. **Monitor** the result, and detect any drift.

## Benefits

- **Repeatability and consistency** across environments.
- **Speed:** whole environments can be created in minutes, including temporary ones for testing.
- **Reduced human error.**
- **Documentation and auditability.**
- **Disaster recovery:** rebuild from the definitions and the backed-up data.
- **Safe change** through review and testing.
- **Cost control:** unused environments can be destroyed and recreated on demand.

## Risks and Challenges

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Challenge</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Explanation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Response</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Large blast radius</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One mistake can destroy or expose a great deal at once</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Review and preview changes; protect critical resources; separate environments and permissions</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">State management</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tools keep a record of what they have created; losing or corrupting it is serious</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Store state remotely, with locking and backup</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Secrets in definitions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Credentials accidentally written into files</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use secrets managers; scan for secrets</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Manual changes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Someone edits the environment directly, causing drift</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Restrict permissions; detect and correct drift</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Complexity and learning curve</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">New tools and concepts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Start small; build shared modules; train the team</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tool and provider lock-in</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Definitions tied to one cloud</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Accept the trade-off consciously; keep definitions modular</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Testing is harder than for application code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Real resources cost money and time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use temporary environments, static checks, and small tests</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Over-engineering</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Elaborate abstractions for simple needs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep definitions simple and readable</td>
    </tr>
  </tbody>
</table>

## Practices

- Keep **all** infrastructure definitions in version control, with the application where it makes sense.
- Use **modules** for reusable patterns, such as a standard network layout.
- **Parameterise** for environments, instead of copying definitions.
- Apply infrastructure changes **only through the pipeline.**
- Apply **least privilege** to the pipeline credentials.
- Apply **the same review standards** as for application code.
- Treat environments as **disposable and rebuildable**.

<!--
IMAGE PROMPT  ->  generate as images/02_desired_state_vs_actual_and_drift.png   (16:9 explanatory diagram, place here)

Left: a definition file card labelled Desired state with three servers and one database. Right: the actual environment with one server missing and one manually altered, marked as Drift. In the middle, a Plan step lists Create 1 server, Revert 1 change, then an Apply arrow bringing the actual state into line with a green tick.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Spot the Infrastructure Issue

1. An administrator logs into a production server and changes a setting directly to fix a problem. Nobody records it.
2. A team can create a complete copy of its test environment in fifteen minutes by running its definitions.
3. A teammate's infrastructure change would delete a database. How should the team find this before it happens?

Case 1 creates drift and an unreproducible server: the fix belongs in the definitions, applied by the pipeline. Case 2 shows a main benefit of infrastructure as code. In case 3, the change must go through review with a **preview of the changes**, which would show the deletion, along with protections on critical resources.

## Conclusion

Infrastructure as code is the practice of defining and managing servers, networks, storage, and platform services through machine-readable definition files, kept in version control and applied by automated tools, so that infrastructure can be created, changed, reviewed, and reproduced like software. It brings the discipline of software engineering to the platform beneath the software.

With environments, containers, and infrastructure defined, the remaining question is how new versions are put in front of users without harming them. The next topic describes release strategies.
