## Introduction

A system can do everything its requirements list and still fail its users: it responds slowly when many people use it, it can be broken into by an attacker, it crashes when a server fails, it cannot be read by someone using a screen reader. These are failures of **qualities**, not of features. Unit 3 explained that quality requirements must be stated in measurable terms. Non-functional testing is how they are verified. It is more specialised than functional testing and is often neglected until a crisis, yet it frequently determines whether a product succeeds.

**Definition:** Non-functional testing evaluates how well a system performs rather than what it does, by measuring qualities such as performance, security, reliability, compatibility, and accessibility against stated targets, usually under conditions that approximate or exceed real use.

<!--
IMAGE PROMPT  ->  generate as images/13_intro_non_functional_testing.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A system block surrounded by six gauges and shields: speed, load, security, reliability, compatibility, accessibility, with a measuring tape and a stress hammer testing it.

ON-IMAGE TEXT: show a short bold title "Non-Functional Testing" plus only these few labels, large and legible: Speed, Safety, Strength. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Main Kinds

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Kind</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Question</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example target</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Performance testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How fast does it respond, and how much can it handle?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">95 percent of requests within 300 ms at 2,000 users</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can it be attacked or misused?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No high-severity vulnerabilities; accounts locked after repeated failed logins</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reliability and resilience testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does it keep working, and recover from failure?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Service restored within 60 seconds of a server failure</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Compatibility testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does it work on the supported browsers, devices, and platforms?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Works on the latest two versions of major browsers and on common phones</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Usability and accessibility testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can everyone use it?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Meets the accessibility standard at the target level</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Compliance testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does it meet laws and standards?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Personal data handled as the regulations require</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Installability and upgrade testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can it be installed, configured, and upgraded safely?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Upgrade preserves existing data</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Localisation testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does it work in other languages and regions?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Correct formats for dates, currencies, and text direction</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maintainability and operability checks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can it be monitored and supported?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Health checks and alerts work</td>
    </tr>
  </tbody>
</table>

## Performance Testing

Performance testing has several forms, distinguished by the load applied and the question asked.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Type</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it does</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Question answered</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Load testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Applies the expected normal and peak load</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does the system meet its targets at expected use?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stress testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pushes beyond capacity until it breaks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Where are the limits, and how does it fail and recover?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Spike testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Applies a sudden large increase in load</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can it cope with sudden surges, such as a flash sale?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Soak (endurance) testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Applies steady load for hours or days</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Are there memory leaks or slow degradation?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scalability testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Increases load while adding resources</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does capacity grow in proportion?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Baseline and benchmark testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Measures a reference performance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Has a change made it faster or slower?</td>
    </tr>
  </tbody>
</table>

### What Is Measured

- **Response time**, reported as percentiles: median, 95th, and 99th, since averages hide the experience of the slowest users.
- **Throughput:** requests or transactions per second.
- **Error rate** under load.
- **Resource use:** processor, memory, disk, network, connections.
- **Concurrency:** the number of simultaneous users or requests.

### How to Do It Well

1. **Define goals** from the non-functional requirements: what response times at what load?
2. **Model a realistic workload:** the mix of actions real users perform, with realistic data and think time between actions.
3. **Use an environment like production,** in size and configuration as far as possible. A small test environment gives results that do not scale.
4. **Generate load** with specialist tools, such as JMeter, Gatling, k6, or Locust.
5. **Monitor the system** during the test with the metrics, logs, and traces of Unit 9, to see where time goes.
6. **Find the bottleneck,** fix it, and test again. Bottlenecks move: removing one reveals the next.
7. **Test regularly,** ideally in the pipeline, so that regressions in performance are caught as they appear.

Common mistakes include testing with unrealistic data or only trivial scenarios, testing too late, using an environment that is too different, and reporting averages only.

## Security Testing

Security testing seeks weaknesses before attackers find them. Approaches complement one another.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Approach</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Static application security testing (SAST)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Analyses source code for vulnerable patterns without running it</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dynamic application security testing (DAST)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Probes the running application from outside, as an attacker would</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Software composition analysis</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scans dependencies for known vulnerabilities and licence issues</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Penetration testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Skilled testers attempt to break in, using realistic attack methods, within an agreed scope</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fuzzing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Feeds large amounts of malformed or random input to find crashes and weaknesses</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security code review and threat modelling</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Humans examine the design and code for flaws</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Configuration and infrastructure scanning</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Checks for insecure settings, open ports, and exposed secrets</td>
    </tr>
  </tbody>
</table>

Guides such as the OWASP Top Ten list the commonest vulnerabilities and shape test plans. Security testing belongs throughout development, "shifted left," as Unit 9 described, and not only as a final check.

## Reliability and Resilience Testing

- **Failure injection and chaos engineering** deliberately cause faults, such as stopping a server, cutting a network link, or slowing a dependency, in a controlled way, to see whether the system degrades gracefully and recovers. Netflix popularised the practice.
- **Failover and recovery testing** checks that backups restore correctly and that replacement components take over.
- **Disaster recovery exercises** rehearse restoring service after a major loss.
- **Long-running tests** look for faults that appear only after extended operation.

## Compatibility and Accessibility

- **Cross-browser and cross-device testing** runs key journeys on the combinations of browsers, operating systems, and screen sizes that users actually have, often using cloud services that provide many devices. Analytics of real usage guides which combinations matter.
- **Accessibility testing** combines automated checkers, which find a portion of the problems, with manual checks: keyboard-only use, screen reader use, contrast, text sizing, and captions, against the Web Content Accessibility Guidelines.

## Planning Non-Functional Testing

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Step</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Action</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Identify the qualities that matter</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">From the requirements and the risks of this product</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Make targets measurable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Numbers, conditions, and methods, as in Unit 3</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Choose test types and tools</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Matching each target</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prepare environments and data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Realistic and controlled</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Run early and repeatedly</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not once at the end</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Analyse and act on the results</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fix, retest, report</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Monitor in production</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The real system is the final test, using the observability of Unit 9</td>
    </tr>
  </tbody>
</table>

## Common Challenges

- **Late discovery:** a performance problem that is architectural is costly to fix when found just before release.
- **Cost and complexity** of realistic environments and tools.
- **Specialist skills** are required, in performance engineering and security.
- **Vague targets:** without measurable requirements, there is nothing to test against.
- **Variability** of results from shared or cloud environments.

<!--
IMAGE PROMPT  ->  generate as images/02_load_stress_spike_soak_profiles.png   (16:9 explanatory diagram, place here)

Four small line charts of load against time: Load (steady plateau at expected level), Stress (rising ramp until failure marked in red), Spike (sudden sharp peak), Soak (long flat line over hours with a slowly rising memory line). A percentile bar shows median, 95th, and 99th response times.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Choose the Test

1. A shop is preparing for a flash sale expected to bring a sudden jump in visitors.
2. A team suspects that memory slowly leaks and the service degrades over several days.
3. A team wants to find out how the system behaves when its database server fails.

Case 1 calls for spike testing, together with load testing at the expected peak. Case 2 calls for a soak (endurance) test. Case 3 calls for a resilience test with failure injection, ideally rehearsed in a safe environment first.

## Conclusion

Non-functional testing evaluates how well a system performs rather than what it does, by measuring qualities such as performance, security, reliability, compatibility, and accessibility against stated targets, usually under conditions that approximate or exceed real use. Measurable targets, realistic conditions, and early, repeated testing make these qualities something a team can control.

Whatever the testing, defects will be found. The final chapter of this unit covers what to do with them: how to track one down, and how to report one so that it can be fixed.
