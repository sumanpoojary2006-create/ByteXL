## Introduction

Software does not live forever. Products are replaced, platforms are withdrawn, businesses change, and the cost of keeping a system alive eventually exceeds its value. Teams that plan for the beginning of a system but not for its end leave users, data, and operators in difficulty. At the same time, there is a broader question of whether the way software is built and run is sustainable: whether it can be kept going without exhausting its people, harming the environment, or wasting resources. This topic closes the unit by considering both.

**Definition:** End of life is the stage at which software is no longer actively developed or supported and is withdrawn in a planned way, and software sustainability is the practice of designing, building, and operating software so that it can meet present needs over time without undue technical, social, economic, or environmental cost.

<!--
IMAGE PROMPT  ->  generate as images/20_intro_end_of_life_and_software_sustainability.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A sunset over a road leading from an old building labelled Sunset on the left to a new one labelled Successor on the right, with a green leaf and a small energy meter on the side labelled Sustainable.

ON-IMAGE TEXT: show a short bold title "End of Life and Software Sustainability" plus only these few labels, large and legible: Sunset, Migrate, Sustain. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Why Software Reaches End of Life

- **Replacement:** a better system or product takes over.
- **Obsolescence:** the platform, language, or dependencies are no longer supported.
- **Cost:** the cost of maintaining and running it exceeds its value.
- **Declining use:** few people use it.
- **Security risk:** unsupported software no longer receives security fixes and becomes a liability.
- **Business change:** the process or service it supported no longer exists.
- **Vendor decision:** a supplier withdraws a product or service.

An example familiar to many developers is the end of support for Python 2 on 1 January 2020, after years of notice, after which it received no further fixes.

## The Stages of Retirement

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Stage</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What happens</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deprecation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A feature or version is announced as obsolete and discouraged</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Warnings are given; alternatives and migration guides published; no new uses should begin</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">End of active development</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No new features are added</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Only fixes and security updates</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">End of support (sunset)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No more fixes or help</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Users are on their own; date announced long in advance</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Retirement (shutdown)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The software is switched off and removed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data is migrated or archived; access is closed</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Archive</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Source, data, and documents are preserved as required</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">For legal, historical, or reference needs</td>
    </tr>
  </tbody>
</table>

## Planning a Retirement

1. **Decide and announce early,** with a clear timetable. Users need time to adapt.
2. **Provide a migration path:** a successor, tools to move data and settings, and documentation. Support users through the move.
3. **Communicate repeatedly** through several channels, to everyone affected, including other systems that depend on the one being retired.
4. **Identify dependencies:** other systems, integrations, and reports that use it.
5. **Handle the data:** decide what to migrate, archive, or delete, observing legal retention requirements and privacy rules such as the right to erasure.
6. **Maintain security** during the wind-down, patching serious problems until the end date.
7. **Reduce in stages,** such as making the system read-only before switching it off.
8. **Decommission properly:** remove access, shut down servers and accounts, revoke credentials and keys, remove it from monitoring and inventories, and release licences.
9. **Preserve knowledge:** archive documentation and decisions, and record lessons.
10. **Verify** that nothing still depends on it.

## Long-Term Support and Deprecation Policies

Suppliers of software used by others publish how long each version will be supported, often offering **long-term support** versions with extended fixes, so that users can plan upgrades. Clear **deprecation policies** build trust. Users, for their part, should track the support dates of what they depend on, and plan upgrades before support ends, avoiding the risk and cost of emergency migration.

## Software Sustainability

Sustainability has several dimensions, set out in the 2014 Karlskrona Manifesto for sustainability design.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Dimension</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Concern</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Technical</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can the software be maintained and evolved over the long term?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clean structure, tests, up-to-date dependencies, documentation</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Social</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does it serve people fairly, and is the team sustained?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Accessibility, inclusive design, sustainable work pace, shared knowledge</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Economic</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Is it affordable to keep running?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Total cost of ownership, a funding model for maintenance</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Environmental</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What is its impact on energy and resources?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Energy use of servers and devices, carbon emissions, hardware lifetimes</td>
    </tr>
  </tbody>
</table>

## Green Software

Running software consumes electricity, in data centres, networks, and users' devices, and building hardware has its own environmental cost. Organisations such as the Green Software Foundation promote practices to reduce the carbon footprint of software.

- **Efficient design and code:** avoid wasted computation and data transfer.
- **Right-sizing and high utilisation:** do not run idle, oversized servers; switch off unused resources.
- **Carbon awareness:** run flexible workloads when and where electricity is cleaner.
- **Demand shaping:** reduce load, for example by limiting unnecessary background work or very large media.
- **Longer hardware life** and support for older devices, reducing waste.
- **Measure:** estimate and track energy use and emissions, since improvement requires data.
- **Remove unused features and data,** which consume resources for no benefit.

## Sustaining the Team and the Community

Software also depends on people. Sustainable teams share knowledge so that no one person is indispensable, a risk sometimes described as a low **bus factor**. They keep a manageable pace, avoiding burnout, and invest in onboarding. Open-source projects face particular risks when a few volunteer maintainers carry heavy loads of support and security work; organisations that depend on such projects have a responsibility to contribute, through funding, code, or time.

## Preserving Software and Data

Some software has lasting value, for example scientific software or cultural artefacts such as early games and documents. Preserving it requires keeping source code, build tools, documentation, and data formats, or using emulation to run it on future systems. Open formats, careful documentation, and archives such as those that store public source code help to keep information accessible long after the original platform has gone.

## Connecting the Unit

This unit has traced the life of code from clear writing, through improvement by refactoring and the management of debt, to evolution, modernisation, reuse, documentation, and release. End of life and sustainability complete the picture: the purpose of managing software well throughout its life is to deliver value over time at a cost that people, organisations, and the environment can bear.

<!--
IMAGE PROMPT  ->  generate as images/02_retirement_stages_and_sustainability_dimensions.png   (16:9 explanatory diagram, place here)

Top: a timeline of five stages Deprecation, End of active development, End of support, Retirement, Archive, with an announcement flag at the start and a migration bridge to a successor. Bottom: four sustainability dimension icons Technical, Social, Economic, Environmental arranged in a ring around a central heart labelled Sustainable software.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Plan the Shutdown

A company will retire a customer portal and replace it with a new product.

1. List three things that should be done before the shutdown date.
2. What should happen to the customer data?
3. Which dimension of sustainability is addressed by running unused servers only when needed?

Before shutdown: announce the date well in advance, provide a migration path and guidance to the new product, and identify the systems and reports that depend on the portal. Customer data should be migrated to the new system where needed, and the remainder archived or securely deleted, following legal retention and privacy requirements. Switching off idle servers addresses environmental sustainability, and also economic sustainability through lower cost.

## Conclusion

End of life is the stage at which software is no longer actively developed or supported and is withdrawn in a planned way, and software sustainability is the practice of designing, building, and operating software so that it can meet present needs over time without undue technical, social, economic, or environmental cost. Planning the end, and caring for the long term, is part of responsible engineering.

This completes Unit 8. You can now write code that others can read, handle errors robustly, recognise smells, refactor safely, and manage technical debt and legacy code. You understand why software changes and what it costs, how to analyse the impact of change, how to understand unfamiliar systems, how to modernise, reuse, document, and release software, and how to bring it to an orderly end. Unit 9 turns to the tools and practices that make the daily work of change safe and repeatable: version control, build, and DevOps.
