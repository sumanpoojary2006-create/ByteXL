## Introduction

"It works on my machine" has been a joke and a source of frustration for as long as software has been shared. Programs depend on a particular operating system, language runtime, libraries, and settings, and any difference can break them. Containers solve this by packaging an application with everything it needs to run, so that it behaves the same on a developer's laptop, on a test server, and in the cloud. Since the release of Docker in 2013, containers have become a standard way to build, ship, and run software.

**Definition:** A container is a lightweight, isolated, portable unit that packages an application together with its dependencies and runs on a shared operating system kernel, created from an image that describes its contents, so that the software runs consistently wherever it is deployed.

<!--
IMAGE PROMPT  ->  generate as images/18_intro_containers_for_developers.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A shipping container analogy: an application and its libraries sealed in a standard box, loaded on a laptop, a server, and a cloud ship, running identically, with a registry warehouse labelled Images.

ON-IMAGE TEXT: show a short bold title "Containers for Developers" plus only these few labels, large and legible: Package, Ship, Run. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Problem and the Idea

Without containers, each environment must be prepared with the right operating system packages, language versions, and libraries, and these drift apart. The container idea comes from the shipping industry: standard boxes that can be handled by any ship, train, or truck without caring what is inside. A software container is a **standard package** that any compatible host can run without caring what application is inside.

## Containers and Virtual Machines

Both provide isolation, in different ways.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Virtual machine</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Container</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What is virtualised</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Whole hardware: each VM has a full operating system</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The operating system: containers share the host kernel</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Size</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Gigabytes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Typically megabytes to a few hundred megabytes</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Start-up time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Minutes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Seconds or less</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Density</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Few per host</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Many per host</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Isolation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Strong, at the hardware level</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Strong but weaker: all share one kernel</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Different operating systems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Possible side by side</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Must be compatible with the host kernel</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Typical use</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Running whole systems, strong separation, legacy software</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Packaging and running applications and services</td>
    </tr>
  </tbody>
</table>

Containers rely on features of the operating system kernel, notably **namespaces**, which give each container its own view of processes, network, and files, and **control groups**, which limit the resources it can use, as Operating Systems courses explain.

## Key Concepts

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Term</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Image</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A read-only template that contains the application, its dependencies, and its settings, built in layers</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Container</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A running instance of an image, with a thin writable layer on top</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Layer</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A step in building an image; layers are shared and cached, which makes builds and downloads efficient</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dockerfile (build recipe)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A text file of instructions that defines how to build an image; it is versioned with the code</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Registry</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A store of images, which can be public or private, from which images are pulled</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tag</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A label naming a version of an image</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Volume</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Storage that exists outside the container and survives its removal</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Network</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A virtual connection between containers and to the outside world</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Compose (multi-container definition)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A file describing several containers that run together, such as an application, a database, and a cache</td>
    </tr>
  </tbody>
</table>

Docker is the best-known tool. The **Open Container Initiative** defines standards for images and runtimes, so other tools can build and run the same images.

## The Developer Workflow

1. **Define** the image in a build recipe kept in the repository.
2. **Build** the image, in the pipeline as well as locally.
3. **Run** it locally to test, with the same image that will run elsewhere.
4. **Push** the image to a registry.
5. **Deploy** the image to test, staging, and production.

The **image is the artefact** of the build topic: built once, immutable, and promoted through environments. Containers also give developers **local environments that match production**, and can start the database, queue, and other services the application needs with a single definition, without installing them on the machine. Onboarding a new developer becomes a matter of running the project, not following a long installation document.

## Principles of Good Containers

- **One main process per container,** and one concern per container.
- **Stateless and disposable:** a container can be stopped and replaced at any time, so persistent data goes into volumes or external services.
- **Immutable:** do not modify a running container. Build a new image and replace it.
- **Small images** with minimal base images, containing only what is needed. They build and start faster and have fewer vulnerabilities.
- **Configuration from outside,** through environment settings, not baked into the image.
- **Specific, meaningful tags,** with exact version tags for deployment. Avoid the moving tag "latest" in production, since it is ambiguous.
- **Logs to standard output,** so the platform can collect them.
- **Health checks** so that the platform knows whether the container is working.
- **Layer ordering:** put rarely changing steps first so that caching speeds rebuilds.

## Security

Containers share a kernel, so care is needed.

- **Run as a non-privileged user,** not as the administrator.
- **Use trusted, minimal base images** from reputable sources, and keep them updated.
- **Scan images** for known vulnerabilities in the pipeline.
- **Do not put secrets in images.** Supply them at run time.
- **Limit capabilities and resources.**
- **Keep the host and runtime patched.**
- **Sign images** and verify their origin.

## Orchestration

Running a handful of containers is simple. Running hundreds across many machines, keeping them healthy, scaling them with load, rolling out updates, and connecting them, requires an **orchestrator**. **Kubernetes**, created at Google and released in 2014, is the dominant one, now stewarded by the Cloud Native Computing Foundation. It provides:

- **Scheduling:** placing containers on machines.
- **Self-healing:** restarting failed containers.
- **Scaling:** adding or removing instances as load changes.
- **Service discovery and load balancing.**
- **Rolling updates and rollbacks.**
- **Configuration and secret management.**

Orchestrators bring power and complexity. Small projects may be better served by simpler platforms, including managed services that run containers without exposing the orchestrator.

## Limits and Cautions

- Containers are **not a security boundary as strong as virtual machines.**
- They add **a layer of tooling and concepts** to learn.
- **Stateful systems,** such as databases, need extra care, and are often better run as managed services.
- Poorly built images can be **huge and slow** or hide old, vulnerable software.
- A container does not fix a badly designed application.

<!--
IMAGE PROMPT  ->  generate as images/02_image_layers_and_vm_vs_container.png   (16:9 explanatory diagram, place here)

Left: a virtual machine stack (hardware, hypervisor, several guest operating systems, apps) beside a container stack (hardware, one host operating system, container runtime, several app containers). Right: an image drawn as stacked layers (base, dependencies, application) with a thin writable top layer when running.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Container Thinking

1. A developer changes a file inside a running container to fix a problem. What is wrong with this practice?
2. An image is 2 gigabytes because it contains many unused tools. What should be done?
3. A database running in a container loses all data when the container is replaced. Why, and what is the remedy?

Changing a running container makes it differ from its image and the change is lost on replacement; the fix should be made in the build and a new image deployed. An oversized image should be rebuilt from a minimal base with only what is needed. Data inside a container's writable layer disappears with the container, so persistent data must be kept in a volume or an external managed database.

## Conclusion

A container is a lightweight, isolated, portable unit that packages an application together with its dependencies and runs on a shared operating system kernel, created from an image that describes its contents, so that the software runs consistently wherever it is deployed. Immutable, small, stateless containers make environments consistent and deployment predictable.

Containers package software, and something must still create the servers, networks, and platforms they run on. The next topic describes infrastructure as code.
