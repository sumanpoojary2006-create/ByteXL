## Introduction

Almost every system people use today is split across at least two computers: the device in their hand and one or more machines elsewhere. This division, in which one party asks for something and another provides it, is the client-server style. It is the foundation of the web, mobile applications, email, and most business software. Understanding its basic forms, and the idea of tiers, explains how most real systems are deployed.

**Definition:** Client-server architecture is a style in which a system is divided into clients, which request services and present results to users, and servers, which provide those services and manage shared resources, communicating over a network, and a three-tier system further separates presentation, application logic, and data storage into distinct tiers.

<!--
IMAGE PROMPT  ->  generate as images/04_intro_client_server_and_three_tier_systems.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Left: phones and laptops labelled Clients sending arrows to a server box labelled Server. Right: three stacked boxes labelled Presentation tier, Application tier, Data tier on separate machines connected by arrows.

ON-IMAGE TEXT: show a short bold title "Client-Server and Three-Tier Systems" plus only these few labels, large and legible: Request, Respond, Tiers. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Clients and Servers

- A **client** initiates a request. It is usually located near the user: a browser, a mobile app, or another program.
- A **server** waits for requests, performs work, and sends a response. It runs on a machine that is shared by many clients and is managed by the service provider.
- They communicate over a **network** using an agreed protocol, such as HTTP.

The interaction is typically **request and response**: the client asks, the server answers, and the exchange ends. A single server normally serves many clients, which concentrates data, security, and processing in one controlled place.

## Why This Style Is Used

- **Centralised data and rules:** one authoritative copy of data, consistent business logic, and one place to enforce security.
- **Easier updates:** changing a server updates the behaviour for all clients without redistributing software (for web clients).
- **Resource sharing:** powerful, expensive machines serve many light devices.
- **Specialisation:** clients focus on presentation, servers on processing and storage.
- **Scalability:** servers can be replicated to serve more clients.

## Thin and Thick Clients

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Kind</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Advantages</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Disadvantages</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Thin client</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Little logic on the client; mostly displays what the server sends</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simple to deploy and update; consistent behaviour</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Depends on the network; server does most work</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Thick (rich) client</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Substantial logic and sometimes local data on the client</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Responsive, can work offline</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Harder to update and secure; logic duplicated across platforms</td>
    </tr>
  </tbody>
</table>

Modern web and mobile applications lie between these extremes: the client handles interaction and some logic, while the server remains the authority on data and rules.

## Two-Tier and Three-Tier Architectures

A **tier** is a physical or logical grouping that runs separately, often on its own machine, as opposed to a layer, which is a logical division within the code.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Style</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Structure</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical use</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Limitation</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two-tier</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Client talks directly to a data server</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Small, internal applications</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Business logic ends up in the client or the database; hard to scale and secure</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Three-tier</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Presentation tier, application (logic) tier, data tier</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Most business and web applications</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">More components to deploy and operate</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">N-tier</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Further tiers added, such as separate caching, search, or integration tiers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Large systems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Increased complexity and latency</td>
    </tr>
  </tbody>
</table>

In the three-tier style, the clients never access the database directly. The application tier validates requests, applies business rules, and talks to the data tier on their behalf. This protects the data, allows each tier to be scaled and changed independently, and provides a natural place for security and control.

## How the Web Fits

A typical web application is three-tier: a browser (presentation), a web or application server running the business logic (application), and a database server (data). Additional elements are common: a **load balancer** to share requests among several application servers, a **cache** to avoid repeated work, and a **content delivery network** to serve static files from locations near users.

## Scaling the Server Side

To handle more clients, a system can be scaled in two ways.

- **Vertical scaling (scale up):** use a more powerful machine. It is simple but has limits and creates a single point of failure.
- **Horizontal scaling (scale out):** add more machines and share the work. It scales further and improves availability, but requires that the work can be distributed.

Horizontal scaling is easiest when servers are **stateless**: each request carries all the information needed, or the state is held in a shared store, so that any server can handle any request. State kept in the memory of one server, such as a login session, makes it hard to share requests among servers.

## Concerns

- **Network dependence:** latency and failure of the network affect every interaction.
- **Server as bottleneck or single point of failure** without replication.
- **Security:** servers are exposed to many clients, including hostile ones, and must treat all input as untrusted.
- **State management:** deciding where session and application state lives.
- **Version compatibility** between many different clients and the server.

<!--
IMAGE PROMPT  ->  generate as images/02_three_tier_with_load_balancer.png   (16:9 explanatory diagram, place here)

A three-tier deployment: Users with phones and laptops on the left, a load balancer in front of three application servers in the middle tier, a cache beside them, and a database server with a replica in the data tier. A dotted trust boundary separates the public internet from the internal tiers.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Place It in a Tier

1. A user interface running in a browser.
2. The rule that checks a coupon is valid before applying it.
3. The database storing all orders.
4. A device that spreads incoming requests across several servers.

Item 1 belongs to the presentation tier. Item 2 belongs to the application tier, which holds business logic. Item 3 is the data tier. Item 4 is a load balancer, which sits in front of the application tier and is how horizontal scaling is achieved.

## Conclusion

Client-server architecture is a style in which a system is divided into clients, which request services and present results to users, and servers, which provide those services and manage shared resources, communicating over a network, and a three-tier system further separates presentation, application logic, and data storage into distinct tiers. It underlies most networked software.

Within the application tier, the interface and business logic still need a clear internal structure. The next chapter turns to application styles, beginning with one of the most influential: model, view, controller.
