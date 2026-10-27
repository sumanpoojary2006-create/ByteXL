## Introduction

Few organisations now run all their software on computers they own. Instead they rent computing, storage, and higher-level services from cloud providers, paying for what they use and creating or removing resources in minutes. This changes how software is designed. Applications built to take advantage of the cloud, scaling out under load, recovering from failures automatically, and consisting of small parts released independently, are called cloud native. Engineers entering the profession will almost certainly work with cloud services, so understanding the main models, the idea of shared responsibility, the principles of cloud-native design, and the importance of cost awareness is part of preparing for real work.

This topic introduces cloud service and deployment models, serverless computing, scalability and resilience, managed services, design principles such as the twelve-factor approach, and the cost and risk considerations.

**Definition:** Cloud computing is the on-demand delivery of computing resources, such as servers, storage, databases, and software, over a network with pay-for-use pricing; cloud-native development is the approach of designing and operating applications to exploit those characteristics, using elastic, automated, loosely coupled, and observable building blocks.

<!--
IMAGE PROMPT  ->  generate as images/15_intro_cloud_native_development_basics.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A cloud shape containing stacked layers labelled Application, Platform, Infrastructure with a sliding boundary showing which layers belong to the customer and which to the provider; scale arrows expanding and contracting a row of server icons.

ON-IMAGE TEXT: show a short bold title "Cloud-Native Development Basics" plus only these few labels, large and legible: Elastic, Automated, Shared. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## What the Cloud Offers

The US National Institute of Standards and Technology (NIST) defined five essential characteristics of cloud computing in 2011.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Characteristic</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">On-demand self-service</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Resources are provisioned by the user, without human intervention by the provider</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Broad network access</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Services are available over the network from many kinds of device</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Resource pooling</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The provider shares resources among many customers (multi-tenancy)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rapid elasticity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Capacity grows and shrinks quickly with demand</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Measured service</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Usage is metered and billed, giving transparency and pay-per-use cost</td>
    </tr>
  </tbody>
</table>

The attraction is converting large up-front capital cost into variable operating cost, avoiding the wait for hardware, and gaining global reach and services that would be costly to build.

## Service Models

The models describe how much the provider manages and how much is left to the customer.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Model</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Provider manages</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Customer manages</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples (kinds of service)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Infrastructure as a Service (IaaS)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Physical data centres, networking, storage, virtualisation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operating system, runtime, application, data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Virtual machines, block storage, virtual networks</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Platform as a Service (PaaS)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Plus operating system and runtime platform</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Application and data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Managed application hosting, managed databases</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Function as a Service / serverless</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Plus all server management and scaling</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Functions of code and configuration</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Event-driven functions</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Software as a Service (SaaS)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Everything</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Configuration and use</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Email, office suites, customer-management systems</td>
    </tr>
  </tbody>
</table>

Moving up the table reduces operating work and flexibility, and increases dependence on the provider.

### Deployment Models

- **Public cloud:** shared services from a provider such as Amazon Web Services, Microsoft Azure, or Google Cloud.
- **Private cloud:** cloud technology dedicated to a single organisation, on its own premises or hosted.
- **Hybrid cloud:** a combination of private and public environments connected together.
- **Multi-cloud:** use of more than one public provider, to reduce dependence or to use particular strengths, at the price of complexity.
- **Edge:** computing placed near users or devices to reduce delay.

## Shared Responsibility

In the cloud, security and operation are divided between provider and customer, a division called the **shared responsibility model.** The provider secures the underlying facilities and services ("security of the cloud"); the customer secures what they put in it ("security in the cloud"): their data, configuration, identities, and access rules. The great majority of cloud breaches come from customer misconfiguration, such as publicly exposed storage and over-broad permissions (Unit 14 security topics), not from failures of the provider. Engineers must know exactly which duties remain theirs under each service model.

## Cloud-Native Design

The Cloud Native Computing Foundation (CNCF) describes cloud-native technologies as those that enable scalable applications in modern, dynamic environments, typified by containers, service meshes, microservices, immutable infrastructure, and declarative interfaces, combined with automation that makes change frequent and predictable.

### Core Ideas

- **Elastic scale-out:** add instances to handle more load, remove them when it falls, preferably automatically (**horizontal scaling**), rather than depending on one ever-larger machine (**vertical scaling**).
- **Statelessness:** keep application servers free of local state, so any instance can serve any request and instances can be added or lost freely; keep state in managed databases, caches, and queues (Unit 12).
- **Design for failure:** in a large distributed system, parts fail constantly. Assume it. Use redundancy across **availability zones** (separate data centres within a region) and **regions,** health checks, retries with limits, timeouts, circuit breakers, and graceful degradation (Unit 6).
- **Loose coupling:** small, independent services or functions communicating through well-defined interfaces and asynchronous messages, so teams can change and scale each part separately (microservices and event-driven architecture, Unit 6), with the complexity costs described there.
- **Automation:** infrastructure as code, continuous integration and delivery, and automatic scaling and healing (Unit 9).
- **Immutable infrastructure:** replace servers and containers with new versions instead of modifying them in place.
- **Containers and orchestration:** package applications in containers (Unit 9) and let an orchestrator, most commonly **Kubernetes** (open-sourced by Google in 2014), place, scale, restart, and update them.
- **Observability:** logs, metrics, and traces to understand behaviour across many components (Unit 9).
- **Declarative configuration:** state the desired result and let the platform converge to it.
- **Security built in:** identity-based access, least privilege, encryption, and network segmentation, with secrets managed properly.

### The Twelve-Factor App

Developers at the platform company Heroku published in 2011 twelve guidelines for building applications that deploy well to cloud platforms. In summary:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Factor</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Guideline</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Codebase</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One codebase tracked in version control, many deploys</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dependencies</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Declare and isolate dependencies explicitly</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Config</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Store configuration in the environment, not in code</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Backing services</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Treat databases, queues, and other services as attached resources replaceable by configuration</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Build, release, run</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Strictly separate the stages</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Processes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Run as stateless processes; persist data in backing services</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Port binding</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Export services by listening on a port</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Concurrency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scale out through the process model</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Disposability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fast start-up and graceful shutdown for robust scaling and replacement</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dev/prod parity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep development, staging, and production as similar as possible</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Logs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Treat logs as event streams to be collected elsewhere</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Admin processes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Run one-off administrative tasks as processes in the same environment</td>
    </tr>
  </tbody>
</table>

They remain a handy checklist for portable, scalable applications.

## Serverless

In **serverless** computing, developers deploy small units of code or use fully managed services without provisioning or managing servers. Servers still exist, but the provider runs them.

- **Functions as a service:** code runs in response to events (a request, a message, a file upload, a timer), scales automatically from zero to many instances, and is billed by execution.
- **Serverless services** extend to managed databases, queues, storage, and authentication that scale and charge by use.
- **Advantages:** no server management, automatic scaling including to zero (no cost when idle), faster delivery of small pieces, and a good fit for spiky or unpredictable workloads, event processing, and glue code.
- **Limits:** start-up delay for rarely used functions (**cold starts**); limits on run time and resources; harder local testing and debugging; more dependence on provider-specific services (lock-in); costs that can exceed those of steady, fully utilised servers at high constant volume; and complexity in managing many small functions.

Serverless is best treated as one tool in a choice, alongside containers and virtual machines, chosen by workload.

## Managed Services

Providers offer managed versions of databases, queues, caches, search, identity, monitoring, machine-learning platforms, and more. Using them transfers undifferentiated work, such as patching, backups, replication, and scaling, to the provider. Guidelines:

- **Prefer managed services for commodity capabilities;** build your own only where it creates a distinct advantage.
- **Understand the service limits, guarantees (service levels, Unit 13), and failure modes;** managed does not mean infallible.
- **Weigh lock-in** against productivity: proprietary features speed delivery but make leaving harder. Keep data exportable, isolate provider-specific code behind interfaces, and decide consciously.
- **Remember shared responsibility:** configuration and access control remain with you.

## Scalability and Resilience Concepts

- **Load balancing** distributes requests across instances.
- **Autoscaling** adjusts the number of instances according to metrics.
- **Queues and buffering** absorb bursts, decoupling producers from consumers.
- **Caching and content delivery networks** reduce load and latency (Unit 12).
- **Data scaling:** read replicas, partitioning (sharding), and choosing stores that scale as needed (Unit 12).
- **Multi-region designs** for disaster recovery and global users, with the consistency trade-offs of Unit 12 and the availability trade-offs of Unit 13.
- **Backups and recovery objectives:** define recovery time and recovery point objectives and rehearse restores.
- **Chaos engineering:** deliberately injecting failure in a controlled way, practised by organisations such as Netflix, to test resilience.

## Cost Awareness

Pay-per-use makes cost a design concern. A mistake can create large bills quickly.

- **Understand the pricing model:** charges for compute time, storage, requests, and, often surprisingly, **data transfer out** of the cloud or between regions.
- **Tag resources** by team and purpose so that costs can be attributed.
- **Set budgets and alerts** to detect runaway spending early.
- **Right-size and switch off:** match instance sizes to need, remove idle resources, and schedule non-production environments off-hours (this also saves energy, as the previous topic noted).
- **Use discount mechanisms** where appropriate: committed-use plans for steady load and spare-capacity instances for interruptible work.
- **Design for cost:** efficient queries, caching, and avoiding chatty cross-region traffic.
- **FinOps:** the practice of bringing engineering, finance, and business together to manage cloud spending, with shared visibility and accountability.
- **Cost is a quality attribute** to be considered in architecture decisions (Unit 6) and in estimates (Unit 13).

## Risks and Judgement

- **Vendor lock-in and concentration risk:** a major provider outage can affect many services at once; critical systems should know their dependencies and plan for them.
- **Complexity:** distributed systems are harder to understand, test, and debug than a single program. Do not adopt microservices, Kubernetes, or multi-cloud for their own sake; the monolith-first advice of Unit 6 still stands for many teams.
- **Skills:** the cloud needs knowledge of networking, security, and operations as well as programming.
- **Compliance and data location:** laws may restrict where data may be stored and processed (previous topics).
- **Cost surprises and sprawl:** unused resources accumulate.
- **Security through misconfiguration:** guardrails, policy-as-code, and scanning reduce risk.

<!--
IMAGE PROMPT  ->  generate as images/15_service_models_and_shared_responsibility.png   (16:9 explanatory diagram, place here)

Four columns IaaS, PaaS, Serverless, SaaS as stacks of layers (data centre, network, servers, OS, runtime, application, data); a coloured line in each column shows the boundary between provider-managed (upper blue) and customer-managed (lower green) responsibility moving upward from left to right.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Choose and Configure

1. A web application stores user sessions in the memory of a single server and fails when a second server is added. Which cloud-native principle is being violated?
2. Which service model leaves the customer responsible for the operating system?
3. A team's cloud bill rises sharply after a feature launch that transfers large files between regions. What is a likely cause, and what should they do?

For case 1, statelessness; move session data to a shared store or use tokens. For case 2, Infrastructure as a Service. For case 3, data transfer charges between regions; review architecture to keep traffic within a region, cache or use a content delivery network, set budget alerts, and track cost by feature.

## Conclusion

Cloud computing is the on-demand delivery of computing resources, such as servers, storage, databases, and software, over a network with pay-for-use pricing; cloud-native development is the approach of designing and operating applications to exploit those characteristics, using elastic, automated, loosely coupled, and observable building blocks. Understanding service models, shared responsibility, statelessness, managed services, and cost lets engineers use the cloud effectively and safely.

Another kind of system that has become common is one that learns from data. The next topic examines software engineering for machine-learning systems.
