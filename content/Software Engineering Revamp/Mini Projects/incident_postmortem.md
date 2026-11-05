## Background

On results day, a university portal slows to a crawl at 9:05 and goes down at 9:20. By 11:00 it is back. The first message to the team asks who deployed last. The second asks who approved it. A postmortem that begins with a name ends with silence: next time, people hide what they know.

A blameless postmortem asks what in the system let a reasonable person make this mistake. This project gives you an incident timeline and asks you to write the report that turns it into lasting change.

## What You Will Build

A blameless postmortem for the results-day outage: timeline, impact, root causes, contributing factors, what went well, and an action list with owners and dates.

## Learning Objectives

By the end of this project, you will be able to:
- Build a timeline from raw events
- Separate the trigger from the root causes
- Write findings about systems rather than people
- Turn lessons into specific, owned actions

**Difficulty:** Intermediate · **Estimated time:** 2 hours

## Starting Material

| Time | Event |
|------|-------|
| 08:30 | A new result-search feature is released |
| 09:00 | Results published; traffic rises to 12 times normal |
| 09:05 | Pages become slow; no alert fires |
| 09:12 | A student tweets about the slowness; support begins receiving calls |
| 09:20 | The database reaches its connection limit; the site goes down |
| 09:25 | The on-call engineer is paged by support, not by a monitor |
| 09:40 | The team suspects the new feature; rollback is attempted |
| 10:05 | Rollback fails because a data change in the release cannot be reversed |
| 10:30 | A configuration change raises the connection limit |
| 11:00 | Service restored |

Other facts: the feature was tested with 50 simultaneous users, and the expected peak was never written down.

## Tasks

### Task 1: Impact and Timeline

1. State the duration of the full outage and of the degraded period.
2. Rewrite the timeline in your own words, marking the detection point, the response point and the recovery point.

Expected result: the outage is 100 minutes from 09:20 to 11:00, and detection by a person came before detection by a monitor.

### Task 2: Causes

1. Identify the trigger of the outage.
2. List at least four root or contributing causes, such as testing at the wrong scale, missing alerts and an irreversible change.
3. For each cause, ask "why" three times and record the chain.

### Task 3: Write It Blamelessly

1. Rewrite this sentence so it describes the system: "The developer didn't load test the feature."
2. Write the "what went well" section with at least two items.

### Task 4: Actions

1. Write at least five actions, each with an owner role, a due date and a measure of completion.
2. Mark which actions prevent a repeat, which shorten detection and which shorten recovery.
3. Choose the one action that, if you could do only one, would help most, and justify the choice.

**Answer these questions after completing all tasks:**
- Why was the time between 09:05 and 09:25 the most avoidable part of the outage?
- Which of your actions depends on a person remembering, and how can you make it depend on a system instead?
- How would you convince a manager to fund an action that prevents something that has not yet gone wrong again?

## Where to Build This Project

This project needs no software beyond a document editor. Write the report on your own device, or as a Markdown file in a ByteXL Nimbus workspace at [bytexl.app/nimbus](https://bytexl.app/nimbus).
