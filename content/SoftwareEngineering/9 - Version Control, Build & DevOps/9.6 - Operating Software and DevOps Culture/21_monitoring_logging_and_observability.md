## Introduction

Releasing software is not the end of the engineering task. A running system can slow down, fail partially, or misbehave in ways that no test predicted, and users may suffer long before anyone on the team knows. Operating software responsibly means being able to see what it is doing, detect trouble quickly, and find its cause. Monitoring, logging, and observability are the practices that provide this sight, and they are as much a part of the system's design as any feature.

**Definition:** Monitoring is the continuous collection and checking of measurements about a running system to detect problems, logging is the recording of events that happen inside it, and observability is the degree to which the internal state of a system can be understood from the data it produces, so that unexpected problems can be investigated and explained.

<!--
IMAGE PROMPT  ->  generate as images/21_intro_monitoring_logging_and_observability.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A running application box emitting three streams labelled Logs, Metrics, Traces into a dashboard showing graphs, with an alarm bell and a person investigating a spike on a chart.

ON-IMAGE TEXT: show a short bold title "Monitoring, Logging and Observability" plus only these few labels, large and legible: Logs, Metrics, Traces. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Monitoring and Observability

- **Monitoring** watches for **known** problems: you decide in advance what to measure and what thresholds indicate trouble, such as response time or error rate. It answers: is the system healthy, and is something wrong?
- **Observability** concerns the ability to ask **new questions** about a system without changing it: why is this particular user's request slow? It answers: what is going on inside, and why? It matters especially in distributed systems where failures are rarely the ones anyone anticipated.

Monitoring tells you that something is wrong. Observability helps you understand why.

## The Three Pillars of Telemetry

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Pillar</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it is</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strengths</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Limits</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Logs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Time-stamped records of discrete events, such as an order created or a payment failed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Detail and context; the story of what happened</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Volume and cost; hard to see trends; need structure to search</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Metrics</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Numerical measurements over time, such as requests per second, error percentage, memory use</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cheap, compact, ideal for dashboards, trends, and alerts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lose detail about individual requests</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Traces</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The path of a single request through several services, with the time spent at each step</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Show where time goes and which service fails in a distributed system</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Need instrumentation across all services; sampling needed at scale</td>
    </tr>
  </tbody>
</table>

Used together, they let a team move from a metric alert ("errors rose at 14:02") to the traces that show which service failed, to the logs that explain the cause.

## Logging

Logs are the oldest and most universal form of telemetry. To be useful they must be designed.

- **Use levels** to indicate importance: debug (detail for developers), info (normal events), warning (unexpected but handled), error (an operation failed), and critical (the system is in serious trouble). Production normally records info and above.
- **Structure the entries.** Logs written as fields, such as time, level, service, message, and identifiers, in a consistent machine-readable form, can be searched and analysed. Free text is hard to query.
- **Add context:** a **correlation identifier** attached to every log line of a request, passed between services, lets all entries for one request be gathered.
- **Say what happened and with what,** such as the operation and the identifiers involved, without being verbose.
- **Never log secrets or unnecessary personal data.** Passwords, keys, card numbers, and sensitive personal information must be kept out of logs, which are widely accessible and long-lived.
- **Log errors where they are handled,** once, with enough context, avoiding duplicates.
- **Send logs to standard output or a central collector,** not local files on servers that vanish.
- **Control volume and retention,** since logs have cost and legal implications.

## Metrics

Metrics come in a few basic kinds:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Type</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Counter</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A value that only increases</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Total requests served</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Gauge</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A value that can go up and down</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Current memory use; queue length</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Histogram (distribution)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The distribution of values, giving percentiles</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Response times: median, 95th, and 99th percentile</td>
    </tr>
  </tbody>
</table>

**Percentiles matter more than averages.** An average response time of 200 milliseconds can hide the fact that one in a hundred users waits ten seconds. The 95th or 99th percentile reveals the experience of the unlucky.

### What to Measure

Several frameworks suggest a core set.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Framework</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Measures</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Suited to</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The four golden signals (from the Google Site Reliability Engineering book)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Latency, traffic, errors, saturation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Any user-facing service</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">RED method</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rate, errors, duration</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Request-driven services</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">USE method</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Utilisation, saturation, errors</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Resources such as processors, memory, disks, and networks</td>
    </tr>
  </tbody>
</table>

**Business metrics**, such as orders placed or payments completed, are as valuable as technical ones, since a system can look healthy technically while failing at its purpose.

## Traces

A **distributed trace** follows one request across services. Each unit of work, called a span, records its start, duration, and relationships, and the spans form a tree. Traces reveal the **slow step**, the **failing dependency**, and unexpected call patterns. Standards such as **OpenTelemetry** provide common ways to generate and collect traces, metrics, and logs from many languages and tools.

## Alerting

Alerts turn data into action by notifying people when attention is needed. Poor alerting is one of the biggest causes of operator exhaustion.

- **Alert on symptoms that matter to users,** such as high error rate or slow responses, rather than on every possible cause, such as a busy processor.
- **Every alert should be actionable:** a person must be able to do something about it, now. If not, it is a dashboard item or a report.
- **Avoid alert fatigue.** Too many alerts, many of them false, teach people to ignore them. Tune thresholds, remove noisy alerts, and review regularly.
- **Include context:** what is wrong, the likely impact, and a link to a runbook and relevant dashboards.
- **Route appropriately:** urgent alerts page the on-call person, less urgent ones create tickets.
- **Test alerts,** so that you know they work before you need them.

## Service Level Objectives

To decide what "healthy" means, mature teams define:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Term</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">SLI (service level indicator)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A measurement of some aspect of service quality</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The proportion of requests answered successfully within 300 ms</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">SLO (service level objective)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The target for an SLI over a period</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">99.9 percent of requests meet the indicator over 30 days</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">SLA (service level agreement)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A contractual promise to customers, often with consequences</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Credits if monthly availability falls below a stated figure</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Error budget</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The amount of unreliability the SLO allows</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">0.1 percent over 30 days, about 43 minutes of full outage</td>
    </tr>
  </tbody>
</table>

The **error budget** is a management tool: while budget remains, the team may release quickly and take risks. When it is exhausted, effort turns to reliability. This links release speed to stability in an explicit way.

## Dashboards and Other Tools

A good **dashboard** answers a particular question for a particular audience at a glance, with a few meaningful graphs and not a wall of numbers. Beyond them:

- **Synthetic monitoring** runs scripted checks against the system from outside, like a robot user, to detect outages even when no real users are active.
- **Real user monitoring** records the experience of actual users in browsers and apps.
- **Health endpoints** let platforms and monitors ask whether the service is working.
- **Profiling and error tracking tools** capture exceptions and performance hot spots, grouping repeated errors.
- Commonly used tools include Prometheus and Grafana for metrics and dashboards, systems that gather and search logs, and commercial observability platforms.

## Designing for Observability

Observability must be built in, not added after a crisis:

1. **Instrument** code to emit metrics, logs, and traces as a normal part of building each feature.
2. **Standardise** formats and names across services.
3. **Include identifiers** that connect telemetry, such as request and user identifiers (with care for privacy).
4. **Define SLOs** for each service.
5. **Make dashboards and alerts part of the Definition of Done.**
6. **Review telemetry in incidents** and fill the gaps it reveals.

<!--
IMAGE PROMPT  ->  generate as images/02_three_pillars_and_golden_signals.png   (16:9 explanatory diagram, place here)

Left: three pillars labelled Logs (events), Metrics (numbers over time), Traces (request path across services). Right: four golden signal gauges Latency, Traffic, Errors, Saturation, and a small chart showing average versus 99th percentile response time diverging.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Pick the Signal

1. You want to know whether error rates are rising across the whole service over the last hour.
2. You want to see why one specific request took eight seconds as it passed through five services.
3. You want to read exactly what happened when one payment failed.

Question 1 is best answered by a metric. Question 2 needs a distributed trace. Question 3 needs the logs for that request, found through its correlation identifier.

## Conclusion

Monitoring is the continuous collection and checking of measurements about a running system to detect problems, logging is the recording of events that happen inside it, and observability is the degree to which the internal state of a system can be understood from the data it produces, so that unexpected problems can be investigated and explained. Telemetry designed in from the start, with actionable alerts and clear objectives, turns a running system from a black box into something a team can understand.

Even with excellent monitoring, failures will happen. The next topic describes how teams respond to them and learn from them.
