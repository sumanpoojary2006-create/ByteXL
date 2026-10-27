## Introduction

Every program runs on hardware that consumes electricity, was manufactured from materials and energy, and will one day become waste. A single application uses a tiny amount, but software is run billions of times on billions of devices and in vast data centres, so decisions made by engineers add up to a measurable share of global energy use and emissions. Sustainable, or green, software engineering is the discipline of designing, building, and operating software so that its environmental impact, chiefly its carbon emissions, is as small as is reasonable for the value it delivers.

This topic explains where the energy goes, the core principles of green software, the measurement of software carbon intensity, practical techniques at the level of architecture, code, data, and operations, and the trade-offs and limits.

**Definition:** Sustainable software engineering is the practice of designing, developing, and operating software so as to minimise its negative environmental impact, particularly greenhouse-gas emissions from the energy used by the hardware it runs on and the hardware needed to run it, while meeting its functional and quality goals.

<!--
IMAGE PROMPT  ->  generate as images/14_intro_sustainable_and_green_software.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A data-centre rack on the left with a power meter, a leaf-shaped gauge in the centre labelled Carbon, and a world map on the right with a green wave indicating clean electricity moving across regions.

ON-IMAGE TEXT: show a short bold title "Sustainable and Green Software" plus only these few labels, large and legible: Less Energy, Cleaner Energy. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Why Software Matters to the Climate

- **Scale:** estimates vary, but information and communication technology is commonly put at between two and four per cent of global greenhouse-gas emissions, similar to the aviation industry, and data centres account for roughly one to two per cent of global electricity use. Demand is growing quickly, driven by cloud services, streaming, cryptocurrency mining, and training and operating large machine-learning models.
- **Invisible:** unlike a factory chimney, software's impact is hidden in electricity bills and hardware purchases.
- **Leverage:** a small efficiency gain in widely used software multiplies across millions of machines.
- **Responsibility:** the codes of ethics ask engineers to consider the environment and the public good (previous topics).
- **Business:** energy efficiency reduces cost; regulators and customers increasingly ask for emissions reporting.

## Where the Impact Comes From

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Source</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operational energy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Electricity used by servers, networks, and user devices while software runs. Emissions depend on both the amount of energy and how the electricity was generated</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Embodied carbon</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Emissions from manufacturing, shipping, and disposing of hardware: servers, phones, laptops. For many devices, manufacturing accounts for the majority of their lifetime emissions, so using devices longer and using fewer of them matters</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data transfer</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Energy used by networks to move data</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Idle and over-provisioned capacity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Machines that are on but doing little still consume a large part of their peak power</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Water</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cooling of data centres consumes water in some regions</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">E-waste</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Devices made obsolete by software that demands newer hardware</td>
    </tr>
  </tbody>
</table>

## Principles of Green Software

The Green Software Foundation, founded in 2021, describes core principles.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Principle</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Carbon efficiency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Emit the least carbon possible for the work done</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Choose regions and times with cleaner electricity</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Energy efficiency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use the least energy possible for the work done</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Efficient algorithms; avoid unnecessary computation</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Carbon awareness</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Do more when electricity is clean and less when it is dirty</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shift flexible work to times or places with more renewable power</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hardware efficiency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use the least embodied carbon; get the most out of each machine</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Higher utilisation; longer device lifetimes; avoid forcing upgrades</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Measurement</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What you cannot measure, you cannot improve</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Track energy and emissions per unit of work</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Climate commitments</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Understand the science and commit to real reductions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Targets and reporting</td>
    </tr>
  </tbody>
</table>

### Carbon Intensity

The **carbon intensity** of electricity is the grams of carbon dioxide equivalent emitted per kilowatt-hour. It varies enormously: grids powered by hydro, wind, solar, or nuclear emit a small fraction of those powered by coal. It also varies by hour as the supply of wind and sun changes, and public data services publish forecasts for many grids. The same computation can have very different emissions depending on where and when it runs.

### Software Carbon Intensity

The **Software Carbon Intensity (SCI)** specification, developed by the Green Software Foundation and published as an international standard in 2024, defines a rate: emissions per functional unit of the software, for example per user, per transaction, or per API call. It combines the energy consumed, the carbon intensity of that energy, and an allocated share of the embodied emissions of the hardware. Because it is a rate, not a total, it allows comparison between versions and encourages efficiency per unit of value rather than simply growth being penalised.

## Practices

### Architecture and Operations

- **Right-size resources and switch off what is idle.** Idle servers draw significant power. Turn off development and test environments out of hours; delete unused resources.
- **Raise utilisation:** consolidate workloads on fewer, busier machines through containers, orchestration, and autoscaling (the cloud-native topic).
- **Use elasticity** to scale up and down with demand rather than provisioning for the peak all day.
- **Choose cleaner regions** where latency, law, and cost allow; many cloud providers publish the carbon information of their regions.
- **Carbon-aware scheduling:** move flexible, non-urgent work (batch jobs, backups, model training, updates) to times and locations with lower carbon intensity (**time shifting** and **location shifting**), and reduce demand during dirty periods (**demand shaping**).
- **Use managed and shared services** run by operators who achieve high efficiency, while noting that efficiency claims should be checked.
- **Cache and use content delivery networks** to reduce repeated work and long-distance transfer (Unit 12).
- **Design for graceful degradation:** lower-fidelity modes when the grid is dirty or resources are scarce.
- **Retire** unused services and data.

### Code and Algorithms

- **Efficient algorithms and data structures** cut work directly: a better algorithm may save more energy than any hardware choice.
- **Avoid wasteful operation:** needless polling, busy waiting, repeated recomputation, unneeded background activity, and chatty network calls. Prefer event-driven designs that act when something happens.
- **Choose languages and runtimes with awareness.** Studies show that execution time and energy differ widely between languages for the same task, with compiled languages typically using less than interpreted ones, but productivity, safety, and maintainability matter, and the architecture usually matters more than the language.
- **Measure before optimising** (Unit 8): profile to find the real hotspots, and do not sacrifice clarity for tiny gains.
- **Batch work** to amortise overheads, and use asynchronous designs so that processors can sleep.

### Data

- **Store less, and store it for less time:** retention limits reduce storage and are also good privacy practice (previous topic).
- **Compress** data in transit and at rest; use efficient formats (Unit 12).
- **Tier storage:** move rarely used data to cold, low-energy storage.
- **Transfer less:** send only the fields and records needed; paginate; avoid duplicate copies.
- **Remove duplicates and dark data** that nobody uses.

### Front End, Mobile, and Devices

- **Reduce page weight:** optimise and lazily load images, video, scripts, and fonts; remove unused code; avoid auto-playing video.
- **Be efficient on user devices:** limit background activity, animation, and wake-ups, which also extend battery life.
- **Support older devices** and operating systems for longer, so users need not replace hardware, and avoid forced obsolescence.
- **Offer lower-data modes** and respect user preferences for reduced data.
- **On displays that save power with dark colours,** dark themes can reduce energy use.

### Machine Learning and AI

Training large models consumes substantial energy, and serving them to millions of users consumes more over time. Ways to reduce impact include:

- choosing whether a model is needed at all, and using simpler models when they suffice;
- using smaller, distilled, or specialised models; quantisation and pruning;
- reusing pre-trained models rather than training from scratch;
- training in regions and at times with clean energy;
- avoiding wasteful repeated experiments and caching results;
- reporting energy and emissions (see the machine-learning topic).

### Process and Culture

- **Make it visible:** dashboards of energy and cost per service; include carbon in design reviews and architecture decisions (Unit 6), as a quality attribute.
- **Set targets** and review them like performance or reliability.
- **Use cost as a proxy:** in the cloud, spend correlates with resource use, so cost-optimisation (FinOps) frequently reduces emissions as well.
- **Include sustainability in requirements** and in the definition of done.
- **Educate teams** and share practices.

## Measuring Impact

- **Direct measurement** with power meters or on-chip counters is accurate but hard in the cloud.
- **Estimation tools:** cloud providers and open-source tools estimate emissions from usage records; energy-measurement tools for programs and browsers exist.
- **Proxies:** CPU hours, memory, bytes transferred, storage, instance-hours, and cost.
- **Granularity:** per service, per feature, per request, to find the largest contributors.
- **Honesty about uncertainty:** estimates rest on assumptions about grid mix and allocation of shared hardware; state them.
- **Beware of greenwashing:** claims such as "carbon neutral" based on offsets differ from reducing actual emissions. Prefer real reductions, then credible offsets for the remainder.

## Trade-offs and Rebound Effects

- **Performance, cost, and carbon** usually move together, but not always: running work in a distant clean region may add latency and transfer costs.
- **Reliability** may require redundancy that uses more resources; do not trade away safety or availability needs carelessly.
- **Rebound effect (Jevons paradox):** efficiency gains can lower cost and increase total use, cancelling the saving. Pair efficiency with attention to total demand.
- **Do not optimise the trivial.** Concentrate effort where usage is large.
- **Software can also enable savings** by optimising logistics, buildings, and energy grids; the net effect of a product should be considered.

<!--
IMAGE PROMPT  ->  generate as images/14_carbon_aware_computing_and_sources_of_impact.png   (16:9 explanatory diagram, place here)

Left: a pie of impact sources (operational energy, embodied carbon, data transfer). Right: a daily grid carbon intensity curve with low and high periods; flexible jobs shown as blocks sliding from the high peak into the green valley, and a second panel showing a job moving from a coal-grey region to a green region.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Reduce the Footprint

1. A nightly data-processing job that is not time-critical runs at the hour when the local electricity grid is dirtiest. What can be changed?
2. Test environments run all night and weekend with no users. What is the simplest saving?
3. Why can making a service more efficient fail to reduce total emissions?

For case 1, apply carbon-aware scheduling: shift the job to a cleaner period, or to a region with cleaner electricity, if allowed. For case 2, shut them down when not in use (or scale to zero) and recreate them on demand. For case 3, the rebound effect: cheaper operation can lead to more use, so total demand must also be considered.

## Conclusion

Sustainable software engineering is the practice of designing, developing, and operating software so as to minimise its negative environmental impact, particularly greenhouse-gas emissions from the energy used by the hardware it runs on and the hardware needed to run it, while meeting its functional and quality goals. Measuring emissions, raising efficiency, using cleaner energy at the right time and place, and keeping hardware in service longer are practical steps within an engineer's reach.

Much of this operational efficiency depends on how software is deployed on shared infrastructure. The next chapter covers modern engineering practice, beginning with cloud-native development.
