## Introduction

An API is used by programs written by other people, often in other organisations, which the provider cannot see and cannot easily change. Once consumers depend on an interface, every change to it has consequences for them. Yet the provider must keep improving the service. Managing this tension is the subject of API evolution: deciding which changes are safe, introducing versions when changes cannot be compatible, retiring old behaviour in an orderly way, and documenting everything so that consumers can understand and trust the interface.

This topic covers compatible and breaking changes, versioning strategies, deprecation, description languages, and documentation.

**Definition:** API evolution is the practice of changing a published interface over time while protecting the consumers that depend on it, using compatible changes, explicit versions, deprecation policies, machine-readable descriptions, and accurate documentation.

<!--
IMAGE PROMPT  ->  generate as images/03_intro_api_versioning_documentation_and_evolution.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A timeline of API versions v1, v2, v3 with consumers attached to each, an overlap period marked Deprecated, a sunset date flag, and a documentation book with a machine-readable specification card feeding it.

ON-IMAGE TEXT: show a short bold title "API Versioning, Documentation and Evolution" plus only these few labels, large and legible: Compatible, Version, Deprecate. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Why Interfaces Are Hard to Change

Consumers depend on the interface, and often on more than the documentation promises. An observation formulated by Hyrum Wright and popularised by Titus Winters is known as **Hyrum's Law**: with enough users of an interface, all observable behaviours of it will be depended on by somebody, whatever the contract says. Even the order of items in a response, the precise wording of an error, or the speed of a response may become relied upon. The practical lesson is to **think carefully before publishing, document what is guaranteed, and be cautious about changing anything observable.**

## Compatible and Breaking Changes

Unit 9 introduced the distinction in the context of semantic versioning. For web APIs it applies in detail.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Generally compatible (non-breaking)</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Generally breaking</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Adding a new operation or resource</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Removing or renaming an operation, resource, or field</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Adding an optional input with a sensible default</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Making an optional input required</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Adding new fields to a response, if consumers ignore unknown fields</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Removing a field from a response or changing its meaning</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Adding new values to an open-ended set, if consumers are tolerant</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Changing the type or format of a field, such as a number to text or a date format</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Relaxing a restriction on inputs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tightening a restriction on inputs, or changing validation rules</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fixing a defect so that behaviour matches the documentation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Changing the meaning of a status code or error</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Improving performance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Changing authentication requirements, or lowering rate limits sharply</td>
    </tr>
  </tbody>
</table>

The principle of the **tolerant reader**, related to Postel's law, asks consumers to ignore fields they do not recognise and to accept reasonable variation, which makes additions safe. Providers should tell consumers to do so, and design to **add, never change or remove**.

## Strategies for Evolving Without Versions

Many changes can be made compatibly if planned for.

- **Add alongside.** Introduce the new field or operation, keep the old working, and move consumers across.
- **Expand and contract** (parallel change), described in Unit 9 for databases: add the new form, migrate consumers, then remove the old.
- **Make extension points.** Use objects in place of bare values so that additions are possible later.
- **Use feature flags** to introduce behaviour gradually.
- **Test with consumers,** using consumer-driven contract tests as in Unit 10, so that a break is detected before release.

## Versioning

When a breaking change is unavoidable, the provider publishes a new **version** of the API and runs it beside the old one for a time.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Approach</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">How the version is indicated</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Advantages</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Disadvantages</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">In the address path</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A version marker as part of the address, such as v1 and v2</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Obvious, easy to route and to test in a browser; widely used</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Changes the address of every resource</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">In a request header</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A custom header names the version</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Addresses stay stable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Less visible; harder to try by hand</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">In the media type</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The consumer asks for a specific representation version through content negotiation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Aligned with REST theory; versions individual representations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">More complex; tooling support is uneven</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">In a query parameter</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A parameter states the version</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simple</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mixes version with resource selection</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Date-based versions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The version is a release date, and each consumer is pinned to the date of its first use</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fine-grained, with gradual upgrade</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs infrastructure to support many behaviours</td>
    </tr>
  </tbody>
</table>

Practical advice:

- Version the **whole API** by **major version** only, and use compatible changes within a major version, as semantic versioning suggests.
- **Avoid creating new versions casually,** since each version must be supported, tested, and documented.
- Keep the **number of supported versions** small.
- Make the version **visible** in logs and monitoring so that usage can be tracked.

## Deprecation and Retirement

Old versions and features cannot be supported forever. A responsible process runs through stages.

1. **Announce deprecation** in the documentation, in the changelog, and by direct message to known consumers.
2. **Signal in the API itself,** using headers that mark a response as deprecated and state the planned retirement date. Internet standards exist for these signals.
3. **Provide a migration guide** and, where possible, tools.
4. **Allow a generous period,** often six months to a year or more for widely used public APIs.
5. **Monitor usage** of the old version, contact those still using it, and decide when to retire.
6. **Retire** the old version, perhaps first with brownouts (scheduled short interruptions) to flush out forgotten consumers, and finally return a clear message that points to the replacement.

Unit 8 treated end of life more generally. For APIs, the courtesy and clarity of the process largely determine consumer trust.

## Describing APIs Formally

A **machine-readable description** of an API supports documentation, testing, and code generation.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Specification</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Describes</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">OpenAPI Specification (formerly Swagger)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The operations, inputs, outputs, errors, and security of REST APIs, in a standard document</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">AsyncAPI</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Event-driven and message-based APIs</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">GraphQL schema</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The types and queries of a GraphQL API, a built-in contract</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Protocol buffer definitions (used by gRPC)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Messages and services of remote procedure call APIs</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">JSON Schema</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The structure of data formats, used within the others</td>
    </tr>
  </tbody>
</table>

Benefits of a formal description:

- **Single source of truth** for providers and consumers.
- **Generated reference documentation** that stays in step with the interface.
- **Generated client libraries** and server stubs in many languages.
- **Mock servers** so consumers can build before the provider is ready.
- **Automatic validation** of requests and responses, and contract tests.
- **Linting** of the description to enforce design conventions.
- **Detection of breaking changes** by comparing two versions of the description automatically, as part of the pipeline.

### Design-First and Code-First

- In **design-first** (API-first) development, the team writes and agrees the description before implementing, and consumers and providers work to it.
- In **code-first** development, the description is generated from the implementation. It is quick to start, but the interface may evolve by accident.

Design-first suits public and cross-team APIs, where the interface is a contract.

## Documentation

Reference generated from a description is necessary but not sufficient. The documentation framework of Unit 8 applies: consumers need **tutorials** to get started, **how-to guides** for common tasks, **reference** for precise facts, and **explanation** of concepts and design.

Good API documentation includes:

- a **quick start** that gets a first successful call in minutes
- **authentication** instructions
- **examples** of requests and responses for each operation, including errors
- **a clear account of guarantees and limits**, such as rate limits and consistency
- **guidance on common tasks** and on pagination, retries, and idempotency
- **a changelog** and notes of deprecations
- **client libraries** and sample applications
- a **sandbox** environment in which to experiment safely
- a way to **ask questions and report problems**
- a **status page** and statement of support

A **developer portal** brings these together for larger offerings. As with all documentation, the discipline of keeping it current, by generating it and testing its examples, matters most.

## Governance and Lifecycle

Organisations with many APIs adopt **API governance**: design guidelines, review of new interfaces, a catalogue of what exists, and policies for security, versioning, and deprecation, so that the whole estate is consistent and manageable. The lifecycle of each API runs from **design** through **build**, **publish**, **operate and monitor**, **evolve**, to **deprecate and retire**, and usage analytics inform decisions at each stage.

<!--
IMAGE PROMPT  ->  generate as images/02_api_version_lifecycle_and_breaking_changes.png   (16:9 explanatory diagram, place here)

Top: a timeline with v1 active, v2 launched, v1 marked Deprecated with a Sunset date flag, v1 retired. Bottom: a specification file at the centre with arrows to Docs, Client libraries, Mock server, and Breaking-change check in the pipeline.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Compatible or Breaking?

For each change to a published API, say whether it is compatible or breaking.

1. A new optional field is added to the order response.
2. A field that was a number is changed to text.
3. A new operation for viewing order history is added.
4. A required input is added to an existing operation.

Change 1 is compatible if consumers ignore unknown fields. Change 2 is breaking. Change 3 is compatible. Change 4 is breaking, because existing requests would now be rejected; it should be made optional with a default, or introduced in a new version.

## Conclusion

API evolution is the practice of changing a published interface over time while protecting the consumers that depend on it, using compatible changes, explicit versions, deprecation policies, machine-readable descriptions, and accurate documentation. Treating the interface as a long-term commitment, and communicating every change early and clearly, keeps consumers' trust.

APIs carry data, and the next chapter turns to data itself, starting with the formats in which it is represented and exchanged.
