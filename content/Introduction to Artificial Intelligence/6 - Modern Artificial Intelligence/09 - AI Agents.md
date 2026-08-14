## Introduction

A logistics firm's expense desk processes about six hundred claims a month, and each one takes a clerk four minutes of the same tedious sequence.

Read the claim. Look up the policy limit for that category. If the receipt is in a foreign currency, find the rate for the date of the expense. Convert. Compare against the limit. Write the decision. Notify the claimant. Update the ledger.

Every individual step is trivial and already automated somewhere in the building. The policy limits sit in a spreadsheet, the exchange rates come from an internal service, and the ledger has an interface. What no system does is the sequence: decide which steps this particular claim needs, in what order, feeding each result into the next.

That gap is what an **AI agent** fills. Not a better model, but a model placed in a loop where it can choose actions, call other software, observe what came back, and continue until the task is done.

**Definition:** An `AI agent` is a system in which a model is given a goal, a set of `tools` it may call, and a loop in which it repeatedly decides an action, executes it, observes the result, and continues until the goal is achieved or it gives up.

![Opening scene: A logistics firm's expense desk processes about six hundred claims a month, and each one takes a clerk four minutes of the same tedious sequence.](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_section_introduction.png)

## What Turns a Model Into an Agent

A language model on its own answers once and stops. Four additions turn it into something that completes tasks.

- **Tools.** Functions it may call: a search, a database query, a calculator, an interface that sends an email. Each has a name, a description of what it does, and a defined set of arguments.
- **A loop.** The output is examined for a tool call, the tool is run, and the result is fed back in, repeatedly.
- **Memory.** A record of what has been done and learned so far, since the model itself retains nothing between calls.
- **A stopping condition.** Something that decides the goal is met, or that enough attempts have been made.

The crucial point is that **the model does not execute anything**. It emits a request to call a tool, and ordinary software decides whether to honour it, runs it, and returns the result. Everything the agent can actually do is defined by what the surrounding program permits, which is where all the safety lives.

![Visual explanation of model to agent](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_model_to_agent_context_v4.png)

## The Loop

Here is the expense task as an agent run. The plan below is fixed so that the loop itself is what you can inspect; in a working system the model would produce each step from the goal and what it has learned so far.

Reading the code below: the four tools are one line each and deliberately dull. The agent is `run`, and inside it the line beginning `resolved = ` is the only piece of real machinery: it substitutes stored results wherever a plan argument begins with a dollar sign, which is how step 3 gets hold of what step 2 produced.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzj8hs" 
 width="100%"
></iframe>

```
TASK: Can a 240 USD hotel bill be reimbursed?
known at the start: {'amount': 240}

step 1: call lookup_policy('hotel',)
         -> 15000   (stored as 'limit')
step 2: call exchange_rate('USD',)
         -> 83.2   (stored as 'rate')
step 3: call multiply(240, 83.2)
         -> 19968.0   (stored as 'spent_inr')
step 4: call compare(19968.0, 15000)
         -> over limit   (stored as 'verdict')

ANSWER: 19968.0 rupees against a limit of 15000, over limit

No single tool could answer this. The agent's contribution is
choosing which to call, in what order, feeding each result into
the next.
```

| In the code | Which of the four parts | Note |
| --- | --- | --- |
| `TOOLS` | Tools | Ordinary functions with fixed contracts |
| `for step, (tool, args, store_as) in ...` | The loop | Run a tool, record the result, continue |
| `facts` | Memory | The only thing carried between steps |
| `"$rate"` and the `resolved` line | Wiring | How one step's output becomes the next one's input |
| End of `PLAN` | The stopping condition | Fixed here; a real agent must decide when to stop |
| `multiply` as a tool | Deliberate | Arithmetic is moved off the model, which gets it subtly wrong |

Four tool calls, each trivial, producing an answer none of them could give.

Two things about this structure are worth noticing.

**The `facts` dictionary is the memory.** Step 3 needs the rate that step 2 produced, and the model holds nothing between calls, so the loop must carry it. Everything the agent knows at any moment is what has been written there.

**The tools do the work that models do badly.** `multiply` is a function rather than something the model is asked to compute, because arithmetic is exactly the kind of thing a next-token predictor gets subtly wrong. Giving an agent a calculator is not a convenience; it is moving a task to something that cannot be approximately right.

![Visual explanation of agent loop recovery](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_agent_loop_recovery_context_v4.png)

## How a Real Agent Chooses the Next Step

The plan above was fixed, which made the loop inspectable and skipped the interesting part. A working agent does not receive a plan; it produces one step at a time.

The dominant pattern alternates between reasoning and acting. At each turn the model is given the goal, the tools available, and everything that has happened so far, and it produces two things: a short statement of what it intends to do next and why, and a request to call one tool. The tool runs, its result is appended to the record, and the model is called again with the longer record.

For the expense claim, the exchange looks like this.

| Turn | The model produces | The program does |
| --- | --- | --- |
| 1 | "I need the policy limit for hotels." Call `lookup_policy("hotel")` | Runs it, appends `15000` |
| 2 | "The bill is in dollars, so I need a rate." Call `exchange_rate("USD")` | Runs it, appends `83.2` |
| 3 | "Now convert." Call `multiply(240, 83.2)` | Runs it, appends `19968.0` |
| 4 | "Compare against the limit." Call `compare(19968.0, 15000)` | Runs it, appends `over limit` |
| 5 | "I have enough to answer." No tool call | Stops and returns the answer |

Three things about this arrangement are worth drawing out.

**The written reasoning is not decoration.** Requiring the model to state its intention before acting measurably improves the choices it makes, and it gives whoever audits the run something to read. It is also not a reliable account of why the model did what it did, for the same reasons post-hoc explanations are unreliable elsewhere, so it should be read as a useful log rather than as ground truth.

**Nothing enforces a sensible plan.** The model may call a tool that does not help, misread a result, or loop between two steps indefinitely. The surrounding program has to detect that, which is why step caps and repetition checks are not optional extras.

**Stopping is a decision the model makes badly.** Knowing that enough information has been gathered is harder than choosing the next action, and agents commonly either stop early with a confident partial answer or continue past the point of usefulness. Most practical systems constrain this rather than trusting it, by requiring a specific output format that signals completion.

![Visual explanation of how a real agent chooses the next step](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_section_how_a_real_agent_chooses_the_next_step.png)

## The Arithmetic That Limits Agents

Agents are frequently demonstrated on short tasks and then disappoint on long ones, and the reason is not subtle.

Reading the code below: there is no agent here. The entire program is `p ** steps`, printed as a table. It is the same compounding arithmetic seen twice already in this course, in the vanishing-gradient table and in the fading recurrent state, now applied to the chance that every step of a task goes right.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzj8up" 
 width="100%"
></iframe>

```
If every step succeeds independently with probability p,
a task of n steps succeeds with probability p to the power n.

 steps       99%       95%       90%       80%
----------------------------------------------
     1     99.0%     95.0%     90.0%     80.0%
     3     97.0%     85.7%     72.9%     51.2%
     5     95.1%     77.4%     59.0%     32.8%
    10     90.4%     59.9%     34.9%     10.7%
    20     81.8%     35.8%     12.2%      1.2%
    50     60.5%      7.7%      0.5%      0.0%

Read the 95 percent column. A step that works nineteen times in
twenty sounds reliable, and a twenty-step task built from such
steps finishes correctly 36% of the time.

This is why long autonomous chains disappoint. Nothing is broken;
the arithmetic of composition is simply unforgiving, and it is the
main argument for short chains with a person checking between them.
```

| In the code | What it stands for | Note |
| --- | --- | --- |
| `p` | Reliability of one step | 0.95 means it works nineteen times in twenty |
| `steps` | Length of the chain | Every step must succeed for the task to succeed |
| `p ** steps` | The whole program | Probabilities multiply, they do not average |
| `0.95 ** 20` | 35.8 percent | The gap between a demo and a deployment |
| `0.99 ** 50` | 60.5 percent | Even near-perfect steps fail over long chains |

Ninety-five percent per step sounds like a working system. Twenty such steps complete correctly barely a third of the time.

This single table explains most of the gap between agent demonstrations and agent deployments. A demonstration is five steps and succeeds; a real workflow is twenty and mostly does not. **The problem is not that any component is bad, it is that reliability multiplies**, and the only ways out are making each step more reliable, using fewer steps, or catching failures rather than hoping they do not occur.

![Visual explanation of the arithmetic that limits agents](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_section_the_arithmetic_that_limits_agents.png)

## Recovering From Failure

The third option is the practical one, and its effect is large.

Reading the code below: this is a simulation, not a real agent. `attempt` is a coin flip weighted by the reliability figure. The retry logic is the inner `for` loop with its `else`, which runs only when every attempt failed, and that is what abandons the task. Two thousand runs per row make the percentages steady.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzj9cn" 
 width="100%"
></iframe>

```
A task of 8 steps, each succeeding 90% of the time

 retries allowed   tasks completed      commonest failure
----------------------------------------------------------
               0             43.8%         read the claim
               1             92.7%          compute total
               2             98.9%    notify the claimant
               3             99.9%          compute total

Retrying a step that can be retried safely turns a 43 percent
success rate into near certainty. The catch is in the words 'safely':
retrying a lookup is harmless, and retrying 'notify the claimant'
sends a second message.
```

| In the code | What it is | Note |
| --- | --- | --- |
| `rng.random() < reliability` | A weighted coin flip | Standing in for a step that sometimes fails |
| `range(retries + 1)` | The attempts | Retries of 0 still means one try |
| `break` | This step worked | Move on to the next step |
| The inner `for ... else` | Every attempt failed | The task is abandoned here |
| `random.Random(7)` per row | Same seed each time | Only the retry count differs between rows |
| `"notify the claimant"` | A step in the list | Also the one that must never be retried blindly |

One retry takes the task from 43.8 percent to 92.7 percent. Three takes it to 99.9.

The closing caution is the real content. Retrying works only for steps that can be repeated without consequence. Looking up a policy limit twice is free. Notifying the claimant twice sends two emails; updating the ledger twice books the expense twice. **An agent's tools must be classified by whether repeating them is safe**, and the ones that are not need a different treatment: a check for whether the action already happened, or a human confirmation, or a design that makes repetition harmless.

This distinction is the single most practically important thing in building agents, and it is a software engineering concern rather than an AI one.

![Visual explanation of recovering from failure](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_section_recovering_from_failure.png)

## What Agents Need That Models Do Not

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Concern</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Why it appears</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Usual answer</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Permissions</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The agent now acts, not just answers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Give it the narrowest set of tools that suffices</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Cost control</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A loop can call the model many times per task</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A hard cap on steps and on spend per task</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Loop detection</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An agent can repeat the same failing action forever</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Detect repetition and stop</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Auditability</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Somebody must reconstruct what happened and why</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Log every step, argument, and result</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Untrusted input</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A tool may return text containing instructions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Treat everything a tool returns as data, never as commands</td>
    </tr>
  </tbody>
</table>

The last row is the one that turns a reliability problem into a security problem, and it is taken up properly two lessons from now.

![Visual explanation of what agents need that models do not](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_section_what_agents_need_that_models_do_not.png)

## Your Turn

Classify the expense agent's tools by whether repeating them is safe.

Take the eight steps from the retry program and sort them into three groups: safe to repeat any number of times, safe only if the system first checks whether it already happened, and never safe to repeat automatically. Then, for the middle group, describe the check. If your check involves recording that the action was taken before taking it, you have arrived at the standard pattern.

Then compute the cost of a cap. Set a limit of ten steps per claim and rerun the retry logic mentally for a claim that needs eight steps and hits two failures. Work out whether it completes. Then decide what the system should do when it hits the cap, and note that "give up silently" and "escalate to a clerk" are very different products.

Finally, reason about the boundary between agent and workflow. The expense sequence is the same every time: eight steps in a fixed order. Argue that this task does not need an agent at all and should be an ordinary program. Then describe the smallest change to the task that would make an agent genuinely worth it. If your answer involves claims that sometimes need extra steps nobody can enumerate in advance, you have found the actual dividing line.
