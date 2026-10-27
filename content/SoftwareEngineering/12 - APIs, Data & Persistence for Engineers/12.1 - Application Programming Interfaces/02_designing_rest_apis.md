## Introduction

REST, short for representational state transfer, is an architectural style for networked systems that treats everything of interest as a resource, identifies each resource by an address, and acts on resources with a small, uniform set of operations. Roy Fielding described it in his doctoral dissertation in 2000, as an account of the principles that made the World Wide Web scale. A web API that follows these principles is called RESTful. The style has become the default for public web APIs because it is simple, uses the existing infrastructure of the web, and is easy to understand.

This topic explains the principles of REST, the vocabulary of resources and operations, and the practical conventions for designing a clear, consistent REST API.

**Definition:** A REST API exposes the things a system manages as resources, each identified by an address and represented in a transferable format, and lets consumers act on them using the standard operations of HTTP in a stateless, cacheable, uniform way.

<!--
IMAGE PROMPT  ->  generate as images/02_intro_designing_rest_apis.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A collection of resources shown as labelled boxes Orders, Dishes, Customers, each with an address tag, and four operation arrows labelled retrieve, create, replace, delete pointing at them, with status code badges beside the responses.

ON-IMAGE TEXT: show a short bold title "Designing REST APIs" plus only these few labels, large and legible: Resource, Operation, Status. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Fielding's Constraints

REST is defined by a set of constraints. Together they produce the properties of simplicity, scalability, and independent evolution.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Constraint</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Benefit</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Client-server</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Separation of the consumer interface from the data and logic of the provider</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Each can evolve independently</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stateless</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Each request carries all the information needed to understand it; the server keeps no conversation state between requests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Easy to scale by adding servers; requests can be handled by any server; simple failure recovery</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cacheable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Responses say whether they may be stored and reused</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fewer requests; faster responses</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Uniform interface</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">All resources are accessed through the same small set of operations, with self-describing messages</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simplicity and visibility; generic tools work with any API</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Layered system</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Intermediaries such as load balancers, caches, and gateways can sit between consumer and provider without either knowing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scalability and security</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Code on demand (optional)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The server can send executable code to extend the client</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Flexibility, rarely used in APIs</td>
    </tr>
  </tbody>
</table>

## Resources and Representations

A **resource** is any concept the API exposes: an order, a customer, a dish, a collection of orders. It is a thing, not an action. Each resource has an **identifier**, an address (a URI), and consumers deal with **representations** of it, usually in a data format such as JSON (Topic 4), not with the resource itself. The same resource could be represented in several formats, and the consumer states its preference.

### Naming Resources

Good addresses are predictable and describe things.

- Use **nouns, not verbs.** The operation is expressed by the HTTP method, so the address names the thing: a collection of orders and an individual order, not "create order."
- Use **plural nouns for collections** and an identifier for an individual member.
- Express **hierarchy** where one thing belongs to another, such as the items of an order, but avoid deep nesting.
- Be **consistent** in style: the same case convention, no file extensions, no unnecessary words.
- Do not expose **internal implementation details** such as table names.
- Keep identifiers **stable** and meaningful to consumers.

## Operations: The HTTP Methods

REST uses the methods of HTTP with agreed meanings.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Method</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Safe?</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Idempotent?</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical use</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">GET</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Retrieve a representation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes (no change to the resource)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Read a collection or one resource</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">POST</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Create a new resource in a collection, or trigger a processing action</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Place a new order</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">PUT</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Replace a resource entirely with the supplied representation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Replace an order details</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">PATCH</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Apply a partial update</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not necessarily</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Change only the delivery time</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">DELETE</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Remove a resource</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cancel and remove an order</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">HEAD, OPTIONS</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Retrieve metadata, or discover what is allowed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Check existence; discover capabilities</td>
    </tr>
  </tbody>
</table>

**Safe** operations do not change the state of the server, so they may be repeated, cached, and prefetched freely. **Idempotent** operations have the same effect when repeated as when done once, which makes it safe to retry them after a timeout, as Unit 6 explained. POST is not idempotent: repeating it may create a second order. To make creation safe to retry, APIs accept an **idempotency key** supplied by the consumer, so that a repeated request with the same key is recognised and not processed twice.

## Status Codes

The response status code tells the consumer what happened. Using the right code, consistently, lets generic tools and consumers react correctly.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Family</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Common codes</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2xx Success</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The request was received and accepted</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">200 OK; 201 Created (with the address of the new resource); 202 Accepted (for asynchronous processing); 204 No Content (success with nothing to return)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">3xx Redirection</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Further action is needed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">301 Moved Permanently; 304 Not Modified (the cached copy is still valid)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">4xx Client error</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The request is faulty; the consumer should change it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">400 Bad Request; 401 Unauthorized (not authenticated); 403 Forbidden (not allowed); 404 Not Found; 409 Conflict; 422 Unprocessable Content (valid format, invalid content); 429 Too Many Requests</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">5xx Server error</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The provider failed to handle a valid request</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">500 Internal Server Error; 502 Bad Gateway; 503 Service Unavailable; 504 Gateway Timeout</td>
    </tr>
  </tbody>
</table>

The distinction between the 4xx family (the consumer's fault) and the 5xx family (the provider's fault) is vital for monitoring and for deciding whether to retry: a consumer should not retry a 400 unchanged, but may retry a 503 after waiting.

## Errors

Error responses should be as carefully designed as successes.

- Use the **right status code**, and a **consistent structure** for the body, with a machine-readable error code, a human-readable message, and, for validation errors, a list of the fields at fault.
- **Be specific and helpful** without revealing internal details, such as stack traces, that attackers could use.
- **Include a correlation identifier** so that a report from a consumer can be matched to the provider's logs, as Unit 9 described.
- A standard format for problem details has been published as an internet standard and is worth adopting.

## Collections: Filtering, Sorting, and Pagination

Collections can be large, so APIs must let consumers ask for part of them.

- **Filtering** selects members that meet conditions, such as orders with a given status.
- **Sorting** orders the results.
- **Pagination** returns a collection in pages. Two common approaches are **offset-based** (skip a number and take a number), which is simple but can skip or repeat items if the data changes, and **cursor-based** (continue after a marker returned by the previous page), which is stable and efficient for large or changing sets.
- **Field selection** lets consumers request only the fields they need.
- Provide **sensible default and maximum page sizes.**

## Statelessness in Practice

Because requests are stateless, the server does not remember the previous one. Anything needed, such as the identity of the caller, is sent with each request, usually as a token in a header. Application state that must persist, such as a basket, is held in a resource (the basket is itself a resource with an address) or in a shared store, not in the memory of one server. This is what allows any server to answer any request.

## Caching and Conditional Requests

REST responses can carry **caching directives** stating how long they may be stored. They can also carry a **version tag** (an entity tag). A consumer can then ask "give me this only if it has changed since this tag," and receive a short "not modified" response if it has not. The same tag supports **optimistic concurrency** for updates: a consumer says "update this only if it is still at the version I saw," preventing one consumer from overwriting another's change unnoticed, a topic taken up again later in this unit.

## Long-Running Operations

Some operations take too long to complete within a single request. The usual design is to respond immediately with an **accepted** status and the address of a **status resource** that the consumer can check, or to notify by a callback when finished. The consumer is not left waiting on an open connection.

## Hypermedia and the Maturity Model

Leonard Richardson described levels of adoption of REST, which Martin Fowler popularised.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Level</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Characteristic</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">0</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A single address and a single operation used to tunnel all requests, as in remote procedure calls over HTTP</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Separate resources, each with its own address</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Proper use of HTTP methods and status codes</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">3</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hypermedia controls: responses include links telling the consumer what it can do next</td>
    </tr>
  </tbody>
</table>

Most practical APIs aim for level 2. Level 3, sometimes called HATEOAS (hypermedia as the engine of application state), lets consumers discover actions from responses, not from out-of-band documentation, and allows the provider to change addresses without breaking consumers, but it is used less often because it adds complexity.

## Design Guidelines

1. **Design from the consumer's point of view,** around the tasks consumers need to perform, and not around the internal data model.
2. **Be consistent,** in naming, formats, errors, pagination, and dates.
3. **Make the common case simple.**
4. **Use standard conventions** and HTTP semantics, not inventing your own.
5. **Avoid chatty designs** that force many requests for one task, and avoid giant responses with everything in them.
6. **Do not expose the database;** keep the API model separate from the storage model.
7. **Validate inputs** thoroughly and reject early.
8. **Secure every operation:** authenticate, authorise, limit rates.
9. **Plan for change** with versioning and compatible evolution, the subject of the next topic.
10. **Document and test it** with real consumers.

<!--
IMAGE PROMPT  ->  generate as images/02_rest_methods_status_codes_and_pagination.png   (16:9 explanatory diagram, place here)

Left: a table-like poster of the five methods with safe and idempotent tick marks. Middle: status code families 2xx green, 3xx blue, 4xx orange labelled Your request, 5xx red labelled Our fault. Right: offset pagination versus cursor pagination drawn as page strips with a marker.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Design Choices

1. An API offers an address for creating orders that includes the verb "create." What is the better convention?
2. A consumer sends a malformed request. Which family of status code applies, and should the consumer retry unchanged?
3. A network failure makes a consumer unsure whether its order creation succeeded. How can the API make a retry safe?

For case 1, name the resource with a noun, such as a collection of orders, and use the create operation (POST) on it. For case 2, a 4xx code, such as 400; the consumer should fix the request and not retry unchanged. For case 3, accept an idempotency key with the request, so that a retry with the same key does not create a second order.

## Conclusion

A REST API exposes the things a system manages as resources, each identified by an address and represented in a transferable format, and lets consumers act on them using the standard operations of HTTP in a stateless, cacheable, uniform way. Consistent naming, correct methods and status codes, and thoughtful handling of errors, collections, and long-running work make an API predictable and pleasant to use.

An API is a long-term commitment, because consumers build on it. The next topic describes how to document it and how to let it evolve without breaking them.
