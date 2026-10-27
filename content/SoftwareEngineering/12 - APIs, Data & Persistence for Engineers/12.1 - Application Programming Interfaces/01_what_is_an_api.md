## Introduction

An application programming interface, or API, is the defined way in which one piece of software asks another to do something. It specifies what can be requested, what must be supplied with the request, what will come back, and what can go wrong. The software that offers the interface can change its inside freely, and the software that uses it needs to know only the interface. Almost every system built today is assembled from parts that talk through APIs.

This topic explains what an API is, the kinds of APIs that exist, the main styles of web APIs, and the properties that make an interface dependable. The following topics treat the design and evolution of web APIs in more detail.

**Definition:** An API is a contract that defines how software components communicate: the operations a provider offers, the inputs each requires, the outputs and errors each produces, and the conditions under which they can be used, so that consumers can use the provider without knowing how it works inside.

<!--
IMAGE PROMPT  ->  generate as images/01_intro_what_is_an_api.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A provider box on the right with a small labelled interface panel on its surface, a consumer box on the left sending a request arrow into the panel and receiving a response arrow back, with the inside of the provider shown faded.

ON-IMAGE TEXT: show a short bold title "What Is an API" plus only these few labels, large and legible: Request, Contract, Response. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Idea of an Interface

An interface is a boundary where two parties meet. It hides the inside of one party and describes what the other may rely on. This is the principle of information hiding from Unit 5, applied to the boundary between separately built programs. A well-designed API lets the provider improve its implementation without breaking anyone, and lets the consumer be written without understanding the provider.

The two roles have names.

- The **provider** (or server) implements the capability and publishes the API.
- The **consumer** (or client) calls it. A consumer can be another service, a mobile application, a web page, a script, or a program written by a different organisation.

## Kinds of APIs

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Kind</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Where the boundary lies</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Library (language-level) API</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Between a program and a code library linked into it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The operations a date-handling library offers to the program that uses it</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operating system API</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Between applications and the operating system</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operations to open files, create processes, or draw on the screen</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Framework API</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Between an application and a framework that calls it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The hooks through which a web framework calls application code</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hardware and device API</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Between software and devices</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Interfaces to a camera or a sensor</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Web (network) API</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Between programs on different machines, over a network</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A payment provider offering operations over the internet</td>
    </tr>
  </tbody>
</table>

This unit concentrates on **web APIs**, because modern systems are built from services that communicate across networks, as Unit 6 described. The same ideas apply to all the kinds.

## What an API Specifies

A complete API description covers more than a list of operations.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Element</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example for an ordering service</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The things that can be requested</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Place an order, cancel an order, view an order</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inputs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data required or allowed with each request, with formats and constraints</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dishes and quantities; a delivery time; a payment reference</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Outputs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The data returned and its format</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The order, its status, and its total</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Errors</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The ways a request can fail, and how each is reported</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dish unavailable; payment declined; request malformed</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Behavioural guarantees</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What the operation promises, including side effects</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Placing an order reserves stock</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Authentication and authorisation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Who may call and what each caller may do</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A signed-in customer may view only their own orders</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Limits</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rates, sizes, and quotas</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A maximum number of requests per minute</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality commitments</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Performance and availability targets</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A response time and an availability objective</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Versioning and support policy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How the API changes over time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Notice before removal of features</td>
    </tr>
  </tbody>
</table>

## Styles of Web API

Several styles are in common use, each with different strengths.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Style</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Idea</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strengths</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Limitations</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">REST (representational state transfer)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Resources are identified by addresses and manipulated with a small set of standard operations of the web protocol HTTP, as the next topic describes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simple, widely understood, uses the web infrastructure, cacheable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can require several requests to assemble one view; fixed response shapes</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">SOAP</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A formal, XML-based messaging protocol with a machine-readable contract</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Strong standards for security and transactions; common in older enterprise systems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Verbose and heavier</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">GraphQL</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The consumer sends a query describing exactly the data it wants, and receives exactly that. Developed at Facebook and released publicly in 2015</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Flexible, avoids over-fetching and multiple round trips</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">More complex to implement and secure; caching is harder</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">RPC (remote procedure call), including gRPC</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Calling a remote operation as if it were a local function, with compact binary messages. gRPC was released by Google in 2015</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Efficient and strongly typed; suits communication between internal services</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Less visible and less natural for public use</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Event and message APIs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Providers publish events or messages that consumers receive asynchronously, via queues, topics, or streams</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Decoupled in time; suits notifications and workflows</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Harder to follow and to debug, as Unit 6 explained</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Webhooks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The provider calls an address supplied by the consumer when something happens</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Avoids repeated checking for changes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The consumer must expose an address and handle retries</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">WebSockets and streaming</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A long-lived two-way connection</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Real-time updates</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">State to manage; harder to scale</td>
    </tr>
  </tbody>
</table>

No style is best for every purpose. Public APIs favour simplicity and familiarity, internal service-to-service calls often favour efficiency, and real-time features need streaming.

## HTTP in Brief

Most web APIs run over **HTTP**, the protocol of the web. A **request** states what is wanted and contains:

- a **method** (the kind of action, such as retrieve or create)
- an **address** identifying the target
- **headers** carrying information about the request, such as the format wanted and credentials
- an optional **body** carrying data

The **response** contains a **status code** saying how it went, headers, and usually a body. Communication is request and response, with the server unable to initiate. Messages normally travel over an encrypted connection (HTTPS), which protects them from eavesdropping and tampering.

## Synchronous and Asynchronous

- In a **synchronous** interaction, the consumer sends a request and waits for the response. It is simple but ties the consumer to the speed and availability of the provider.
- In an **asynchronous** interaction, the consumer sends a request and receives an acknowledgement, with the result delivered later, by a callback, an event, or a status that can be checked. It suits long-running work and loose coupling.

## Properties of a Good API

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Property</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clear purpose</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Each operation does one understandable thing, named in the language of the domain</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Consistency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Names, formats, errors, and behaviours follow the same conventions throughout</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simplicity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The common cases are easy; the interface is as small as it can be</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hard to misuse</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Required data is clear, mistakes are reported precisely, and dangerous operations need deliberate steps</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">It changes rarely and compatibly, so consumers are not repeatedly broken</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Documentation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Accurate and complete reference, with examples and guidance</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Authentication, authorisation, input validation, and limits are built in</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Observability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Calls can be traced and measured by both parties</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Idempotence where possible</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Repeating a request does no extra harm, which makes retries safe, as Unit 6 explained</td>
    </tr>
  </tbody>
</table>

## Security Basics

Every API that crosses a network boundary needs protection.

- **Authentication** establishes who is calling: with keys, tokens, or signed credentials. The common standard for delegated access is **OAuth 2.0**, in which a user grants an application limited access without sharing their password.
- **Authorisation** decides what the caller may do: roles, permissions, and ownership checks on every request.
- **Encryption in transit** protects the data.
- **Input validation** treats every request as untrusted.
- **Rate limiting** prevents abuse and protects the provider from overload.
- **Least privilege:** credentials carry only the permissions needed.
- **Secrets** are never placed in addresses, logs, or source code.

## APIs as Products

Public and partner APIs are products with users, documentation, support, and a lifecycle. The most important design question is therefore to ask what the **consumers** are trying to achieve. An **API-first** approach designs the interface, often with consumers and in a formal description, before building the implementation, so that teams can work in parallel against an agreed contract.

<!--
IMAGE PROMPT  ->  generate as images/02_api_styles_and_http_exchange.png   (16:9 explanatory diagram, place here)

Left: an HTTP exchange with a request card (method, address, headers, body) and a response card (status code, headers, body) between client and server. Right: six tiles labelled REST, SOAP, GraphQL, RPC, Events, Webhooks, each with a one-line characteristic.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Choose or Identify

1. A mobile app needs exactly the data for one screen, assembled from several resources, in a single request. Which style suits?
2. A provider wants to tell consumers when a payment has completed, without consumers repeatedly asking. Which mechanism?
3. Why must a consumer not depend on how the provider is implemented?

For case 1, GraphQL suits, as the consumer specifies precisely what it wants. For case 2, a webhook or an event message suits. For case 3, the provider is free to change its internals only if consumers rely solely on the published contract, which is the point of an interface.

## Conclusion

An API is a contract that defines how software components communicate: the operations a provider offers, the inputs each requires, the outputs and errors each produces, and the conditions under which they can be used, so that consumers can use the provider without knowing how it works inside. Clear, consistent, secure, and stable interfaces let independently built systems work together.

The most widely used style for web APIs is REST. The next topic explains its principles and how to design a REST API well.
