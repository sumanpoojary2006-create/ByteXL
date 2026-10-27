## Introduction

Eventually a valuable system reaches a point where continuing to patch it is no longer sensible. The platform is obsolete, the skills to maintain it are scarce, the architecture blocks new features, or the running cost is too high. Yet it cannot simply be switched off, because the business depends on it. Modernisation is the set of strategies for renewing such systems, ranging from moving them to new infrastructure to replacing them entirely. The central skill is choosing the right option and carrying it out without breaking the business in the process.

**Definition:** Reengineering is the examination and alteration of an existing system to restore its value in a new form, and modernisation is the broader choice among strategies, such as rehosting, restructuring, rearchitecting, rebuilding, or replacing, for bringing a legacy system up to date with the least disruption and risk.

<!--
IMAGE PROMPT  ->  generate as images/16_intro_reengineering_and_modernization.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: An old building on the left and a new building on the right connected by a bridge of small incremental steps, with a legacy system slowly being wrapped and replaced by new modules, like vines growing around a tree.

ON-IMAGE TEXT: show a short bold title "Reengineering and Modernization" plus only these few labels, large and legible: Assess, Choose, Migrate. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Why Modernise

- **Obsolete technology:** unsupported languages, platforms, or hardware, with security risk.
- **Skills shortage:** few people can maintain it, and fewer wish to.
- **High cost:** licences, hosting, and the effort of each change.
- **Inflexibility:** the structure resists new features, integration, or scaling.
- **Poor reliability or performance.**
- **Security and compliance gaps.**
- **Strategic change:** a move to cloud services, new channels, or new business models.

## First Assess

Before choosing a strategy, evaluate the system along two dimensions: its **business value** (how important it is, how much it is used) and its **technical quality** (how maintainable, reliable, and modern it is).

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Business value</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Technical quality</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Likely direction</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep and evolve normally</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Modernise: the most important cases for reengineering</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maintain cheaply; consider merging or retiring later</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Retire or replace with a bought product</td>
    </tr>
  </tbody>
</table>

The assessment also looks at the size and structure of the code, its dependencies, the data, the interfaces to other systems, the available documentation and tests, the people who know it, and the cost of running it.

## The Range of Options

Cloud migration practice popularised a list of "R" strategies, which apply to modernisation generally. Different sources name them slightly differently.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strategy</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it means</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Effort and risk</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Gain</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Retain</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Leave the system as it is for now</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lowest</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Avoids disruption; defers the problem</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Retire</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Switch the system off because it is no longer needed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low to moderate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Removes cost and risk</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rehost (lift and shift)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Move the system to new infrastructure with no change to the code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cheaper or newer hosting, but structure unchanged</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Replatform</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Move to a new platform with small adjustments, such as a managed database</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low to moderate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Some operational gains</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Refactor and restructure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Improve internal structure within the same platform</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Moderate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maintainability</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rearchitect</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Change the architecture, such as splitting a monolith into services</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scalability, flexibility</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rebuild (rewrite)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rewrite from scratch on new technology, with the same purpose</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Very high</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A clean start, with large risk</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Replace (repurchase)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Adopt a commercial or open-source product in place of the custom system</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Moderate to high</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shifts maintenance to a supplier; may not fit all needs</td>
    </tr>
  </tbody>
</table>

## Incremental Replacement: The Strangler Fig

Complete replacement in one step, often called the **big bang**, has a bad record. The new system takes longer than planned, must reproduce years of hidden behaviour, and the business must wait. Martin Fowler, inspired by strangler fig vines that grow around a tree and eventually replace it, described the **strangler fig pattern** for gradual replacement.

1. **Place a facade or routing layer** in front of the legacy system so that requests pass through it.
2. **Build new functionality** in the new system, one capability at a time.
3. **Redirect** the corresponding requests from the old to the new.
4. **Repeat,** shrinking the legacy system until it can be switched off.

At every step, the system works, and value is delivered early. If something goes wrong, the routing can be changed back. The legacy system serves as the reference for behaviour during the transition.

## Protecting the New from the Old

When new components must talk to legacy ones, an **anti-corruption layer**, described in domain-driven design, translates between the old model and the new one, so that the legacy design does not leak into new code. It is an application of the adapter idea at larger scale.

## Challenges in Modernisation

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
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hidden behaviour</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The old system does things nobody documented, which users rely on</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Characterisation tests, parallel running, talking to users</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data migration</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data in old formats, with quality problems, must be moved and verified</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Plan early; migrate in stages; reconcile results</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Feature parity trap</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Trying to reproduce everything, including features nobody uses, delays the project</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Decide which features matter; retire the rest</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Second-system effect</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Over-ambitious redesign adds new features and complexity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fix scope; deliver incrementally</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Running two systems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Both must be supported during transition</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep the transition short; automate synchronisation</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Integration</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Many other systems depend on interfaces</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Preserve interfaces behind a facade; change them deliberately</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Loss of knowledge</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">People who understand the old system are leaving</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Capture knowledge early; involve them in the project</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Business disruption</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Users must not lose service</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Staged rollout, parallel run, rollback plans</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Underestimation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Legacy modernisation is routinely underestimated</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Spikes and pilots; add contingency</td>
    </tr>
  </tbody>
</table>

## Parallel Running and Cutover

For critical systems, a **parallel run** operates the old and new systems side by side on the same inputs and compares their results, until confidence is high. A **phased cutover** moves groups of users or functions gradually. A **rollback plan** allows return to the old system if serious problems appear. These measures reduce the risk of the final switch.

## Success Factors

- **A clear business case** and sponsorship, since modernisation costs money without immediately adding features.
- **Small, frequent deliveries** with visible benefits.
- **Strong testing** to confirm that behaviour is preserved.
- **Honest assessment** of the current system.
- **Involvement of users** and of people who know the old system.
- **A decision about the end state** and the retirement date of the old system, so that the transition does not become permanent.

<!--
IMAGE PROMPT  ->  generate as images/02_strangler_fig_migration.png   (16:9 explanatory diagram, place here)

A sequence of four panels showing time passing. A routing facade sits in front of a legacy system. In successive panels, more capabilities are rerouted to new services, the legacy block shrinks, and in the last panel the legacy block is switched off and removed. Requests arrows are shown in each panel.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Choose the Strategy

1. A stable, well-structured system must move from servers the company owns to a cloud provider, with no business change.
2. A large, critical, poorly structured system must be replaced while remaining in service.
3. A little-used system that costs a lot to run and whose functions are covered by another product.

Case 1 suits rehosting or replatforming. Case 2 suits incremental replacement, the strangler fig approach. Case 3 suits retirement.

## Conclusion

Reengineering is the examination and alteration of an existing system to restore its value in a new form, and modernisation is the broader choice among strategies, such as rehosting, restructuring, rearchitecting, rebuilding, or replacing, for bringing a legacy system up to date with the least disruption and risk. Incremental approaches that keep the system working at every step are generally safer than big-bang replacement.

Modernisation often relies on reusing what already exists. The next topic examines software reuse in general.
