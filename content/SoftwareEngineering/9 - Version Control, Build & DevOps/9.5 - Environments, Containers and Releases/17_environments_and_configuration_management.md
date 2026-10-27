## Introduction

Software does not run in one place. It is written on developers' machines, checked on test systems, rehearsed in a staging area, and finally run in production, each with different data, settings, scale, and access. Much of the difficulty of delivery lies in the differences between these places: a feature that works in one fails in another, a test passes against fake data and fails against real data, a secret leaks because it was copied into the wrong file. Managing environments and their configuration deliberately removes much of this friction.

**Definition:** An environment is a distinct setting, with its own infrastructure, data, and settings, in which software runs at a particular stage of its life, and configuration management of environments is the practice of keeping those settings separate from the code, versioned, secure, and as similar as possible between stages.

<!--
IMAGE PROMPT  ->  generate as images/17_intro_environments_and_configuration_management.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Four boxes in a row labelled Development, Test, Staging, Production, the same application artefact placed in each, with a separate settings card with different values plugged into each box, and a vault icon holding secrets.

ON-IMAGE TEXT: show a short bold title "Environments and Configuration Management" plus only these few labels, large and legible: Same code, Own settings. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Usual Environments

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Environment</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical characteristics</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Local (developer)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Writing and trying code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Small, personal, fast, easily broken</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Development (shared)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Integration of work from several developers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Frequently changing; may be unstable</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test or QA</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Systematic testing, automated and manual</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Controlled data; stable enough for test runs</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Staging (pre-production)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Final rehearsal of the release</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">As close to production as practical in size, configuration, and software</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Production</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Serving real users</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Real data, high availability, strict access and monitoring</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Temporary or preview</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Short-lived environments for one change or branch</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Created automatically, discarded afterwards</td>
    </tr>
  </tbody>
</table>

The number and names vary. What matters is that each stage has a clear purpose, and that **the path between them is automated**.

## Environment Parity

Many production failures occur because an earlier environment differed in some way that mattered: a different version of the database, a smaller data set, a missing network rule, or a different operating system. The ideal, expressed in the **twelve-factor app** methodology published by developers at Heroku, is to **keep development, staging, and production as similar as possible**, reducing the gaps in time (deploy often), in personnel (the people who write the code take part in deploying it), and in tools (use the same kinds of services everywhere). Techniques include using containers and infrastructure defined as code so that every environment is created from the same definitions.

## Configuration

**Configuration** is everything that varies between deployments of the same code: addresses of databases and services, credentials, feature settings, resource limits, and external keys. The core rule is to **separate configuration from code.**

- **Do not embed** environment-specific values in the source code or the artefact.
- Supply them at **run time** through environment variables, configuration files provided to the environment, or a configuration service.
- Keep configuration **versioned** (excluding secrets), so changes are reviewed and traceable.
- Provide **sensible defaults** and **validate** configuration at start-up, failing early and clearly if something is missing or invalid.
- Keep the **number of settings small,** since each is a possible mistake.

The test of a good separation, stated by the twelve-factor approach, is whether the codebase could be made open source at any moment without exposing any credentials.

## Secrets

**Secrets** are configuration whose exposure causes harm: passwords, keys, tokens, and certificates.

- **Never commit secrets** to version control. History keeps them for ever. If one is committed, treat it as compromised and replace it.
- Store them in a **secrets manager** or vault that provides encryption, access control, auditing, and rotation.
- **Give each environment its own secrets,** so a leak from a test system does not endanger production.
- Apply **least privilege:** each service and person receives only the access needed.
- **Rotate** secrets regularly, and automatically where possible.
- **Keep them out of logs, error messages, and build output.**
- Use short-lived credentials where possible.

## Data in Environments

Using real production data in lower environments creates privacy and security risk, and is often illegal under data-protection rules. Options are **synthetic data** created for the purpose, **anonymised or masked** copies, and **small curated samples**. Test data should be **repeatable**: tests need known starting states, which are created and reset automatically.

## Feature Flags as Configuration

A **feature flag** is a setting that switches behaviour on or off without a new deployment. Flags let unfinished features be deployed but hidden, enable gradual rollout to selected users, and provide a quick switch to disable a problem feature. They are a form of runtime configuration that must be managed: flags need owners, documentation, and removal once they have served their purpose.

## Configuration Drift

**Drift** occurs when environments gradually diverge because of manual changes: someone adjusts a setting directly on a server and does not record it. Over time nobody knows the true state, and an environment cannot be rebuilt. Defences include:

- **Forbid manual changes** to shared environments; make changes through the pipeline.
- **Define environments as code,** as the infrastructure topic describes.
- **Detect drift** by comparing actual state to the declared state.
- **Rebuild instead of repair:** replace a drifting environment with a freshly created one.

## Promoting Changes

The same artefact is **promoted** through environments, with each receiving its own configuration. A promotion should be a **controlled, automated step**, recorded with what was deployed, when, by whom, and from which version, so that the state of each environment is always known.

## Common Problems

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Cause</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Remedy</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"Works in test, fails in production"</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Environments differ</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Increase parity; automate their creation; test deployments in staging</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A secret appears in the repository</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Convenience or accident</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Secrets manager; scanning tools that block commits containing secrets; rotate at once</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Different builds for each environment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Configuration baked into the artefact</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Build once; configure at run time</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nobody knows what is deployed where</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No records</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automated deployment records; dashboards</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test data contains personal information</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Copying production data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Masking or synthetic data</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Configuration files full of rarely used settings</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Accumulation over time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prune; document what each does; set defaults</td>
    </tr>
  </tbody>
</table>

<!--
IMAGE PROMPT  ->  generate as images/02_promotion_with_config_and_secrets.png   (16:9 explanatory diagram, place here)

A single artefact box moving left to right through Test, Staging, Production, each with a separate configuration card plugged in and a locked vault icon supplying secrets at run time. A red crossed-out arrow shows a secret being committed to the repository.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Where Does It Belong?

1. The address of the production database.
2. The password for the payment provider.
3. A setting that turns a new report feature on or off.

The database address is configuration, supplied at run time, different in each environment. The payment password is a secret, kept in a secrets manager and never committed. The feature setting is a feature flag, a form of runtime configuration that can change without a new deployment.

## Conclusion

An environment is a distinct setting, with its own infrastructure, data, and settings, in which software runs at a particular stage of its life, and configuration management of environments is the practice of keeping those settings separate from the code, versioned, secure, and as similar as possible between stages. Separating configuration from code, protecting secrets, and preventing drift make deployments predictable.

One of the most effective ways to make environments consistent is to package software together with its surroundings. The next topic describes containers.
