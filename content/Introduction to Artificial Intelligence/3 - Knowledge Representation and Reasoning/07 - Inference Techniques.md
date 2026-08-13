## Introduction

Two systems in the same hospital use the same kind of reasoning engine and behave nothing alike, and the difference tells you almost everything about this lesson.

The first watches the intensive care monitors. Nobody asks it anything. Readings arrive every few seconds, and as they do the system works out whatever those readings imply, continuously, raising an alert the moment something it derives crosses a threshold. It is pushed along by incoming data and has no particular question in mind.

The second is the IT helpdesk system, and it is the opposite. A doctor rings to say she cannot print a discharge summary. The system does not want every fact about the hospital network. It wants to establish one thing, whether printing is possible, and it works backwards from that: to print you need a reachable printer, to have a reachable printer you need a working network, so is the cable connected? It asks four or five questions and stops.

Same machinery, same shape of rules, opposite direction of travel. The first runs **forward chaining**, from what is known towards whatever follows. The second runs **backward chaining**, from a goal towards what would have to be true to support it. Choosing between them is one of the more consequential design decisions in a knowledge-based system.

**Definition:** `Forward chaining` starts from known facts and repeatedly fires every applicable rule to derive all their consequences, while `backward chaining` starts from a goal and recursively seeks facts or rules that would establish it, pursuing only what is relevant to that goal.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_section_introduction.png)

## One Rule Base, Two Directions

Both techniques operate on identical rules. To compare them fairly, the same knowledge base is used throughout this lesson: a small model of an office network, with three separate concerns tangled together, because real rule bases are never about one thing.

| Concludes | When these hold |
| --- | --- |
| network_ok | cable_connected, link_light_on |
| printer_reachable | network_ok, printer_powered |
| can_print | printer_reachable, driver_installed, paper_loaded |
| workstation_ok | os_updated, driver_installed |
| user_can_work | can_print, workstation_ok |
| backup_healthy | backup_ran_today, backup_verified |
| security_ok | antivirus_updated, firewall_on |
| compliance_ok | backup_healthy, security_ok |

Notice the structure. Rules one to five concern whether the doctor can print. Rules six to eight concern backups and security, and have nothing whatever to do with printing. That irrelevance is deliberate, and it is where the two techniques part company.

![Visual explanation of one rule base, two directions](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_section_one_rule_base_two_directions.png)

## Forward Chaining

Forward chaining is the recognise-act cycle from rule-based reasoning, run until it runs out. Take the known facts, fire every rule whose conditions are satisfied, add the conclusions, and repeat until nothing new can be derived.

Reading the code below: the rules are written as pairs of a conclusion and the set of conditions that produce it. `forward_chain` is nine lines, and the thing to notice is that the goal, `can_print`, appears nowhere inside it.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjk7w" 
 width="100%"
></iframe>

```
Goal wanted: can_print
Rules fired: 8
Facts derived, in order:
  - network_ok
  - printer_reachable
  - can_print  <- the goal
  - workstation_ok
  - user_can_work
  - backup_healthy
  - security_ok
  - compliance_ok

Goal reached: True
```

The goal was reached, and look what happened afterwards. Having established `can_print` on the third firing, the engine carried straight on and derived five more facts, three of which concern backups and antivirus software. The doctor asked whether she could print. She has also been told, at no charge, that the organisation is compliant.

This is the defining characteristic, and it is visible in what the function does not contain.

| In the code | What it does | Note |
| --- | --- | --- |
| `conditions <= known` | Are all this rule's conditions known? | The subset test again |
| `conclusion not in known` | Skip what is already derived | Stops the sweep repeating itself |
| `changed = True` | Something fired, so sweep again | New facts may unlock further rules |
| `while changed` | Stop when a full pass adds nothing | The only stopping condition there is |
| **the goal** | **absent** | `can_print` appears nowhere in the function |

**Forward chaining is data-driven and computes everything derivable, whether or not anyone wanted it.** The loop has no notion of a goal at all; `can_print` appears in this program only in the final print statement, never in the reasoning.

That is a genuine strength in the right setting. The intensive care monitor does not know in advance which alert will matter, so deriving everything is exactly right, and each new reading simply extends what is known. It is a genuine waste in the wrong setting.

![Visual explanation of forward chaining](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_forward_chaining.png)

## Backward Chaining

Backward chaining inverts the question. Instead of asking what follows from the facts, it asks what would have to be true for the goal to hold.

To prove a goal: if it is already a known fact, done. Otherwise find a rule that concludes it, and try to prove each of that rule's conditions in turn, recursively. If they all succeed, the goal is proved.

Reading the code below: the rules and facts are identical to the previous program. `backward_chain` is recursive, and the `depth` argument exists only to indent the printout so the proof structure is visible. Ignore the printing and the function is six lines.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjkq9" 
 width="100%"
></iframe>

```
Goal wanted: can_print
can_print: try rule, need ['driver_installed', 'paper_loaded', 'printer_reachable']
  driver_installed: already known
  paper_loaded: already known
  printer_reachable: try rule, need ['network_ok', 'printer_powered']
    network_ok: try rule, need ['cable_connected', 'link_light_on']
      cable_connected: already known
      link_light_on: already known
    network_ok: PROVED
    printer_powered: already known
  printer_reachable: PROVED
can_print: PROVED

Goal reached: True
Rules examined: 3
```

Three rules examined instead of eight, and the indented trace is itself the proof: the goal at the top, decomposed into what it needed, decomposed again, down to facts that were already known.

Backups, security, and compliance never appear anywhere in that trace.

| In the code | What it does | Contrast with forward chaining |
| --- | --- | --- |
| `goal` as the first argument | The question drives everything | Forward chaining had no goal at all |
| `if goal in facts: return True` | Base case: already known | Where the recursion bottoms out |
| `if conclusion != goal: continue` | Ignore rules proving anything else | This is what skips backups and security |
| `all(backward_chain(c, ...))` | Prove every condition, recursively | Each sub-goal handled exactly like the original |
| `depth + 1` | Indentation for the printout | Not part of the algorithm |

The third row is where the efficiency comes from. The engine had no reason to think about compliance, because nothing in the chain from `can_print` downwards mentions it. **Backward chaining is goal-driven and touches only what is relevant to the question asked.**

Notice also what the trace gives you for free. The recursion structure is exactly the explanation a technician needs, and it reads as an argument: printing works because the printer is reachable, which is because the network is fine, which is because the cable is connected and the link light is on.

![Visual explanation of backward chaining](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_backward_chaining.png)

## The Difference That Decides Real Systems

Rules fired is a laboratory measurement. The decisive difference in practice is how much the system has to ask a human.

In the run above, all ten observations were handed to the engine in advance. That is a fantasy. In a real helpdesk consultation the system knows nothing at the start, and every fact costs a question put to a person who is already annoyed.

Reading the code below: the rules are unchanged, and `TECHNICIAN_SAYS` stands in for a person who would answer if asked. The new idea is `DERIVABLE`: anything a rule can conclude is worked out, and anything else must be asked about. The `asked` list records every question actually put.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjm23" 
 width="100%"
></iframe>

```
Backward chaining, goal can_print
  proved: True
  questions the technician was asked: 5
    - driver_installed
    - paper_loaded
    - cable_connected
    - link_light_on
    - printer_powered

Forward chaining would need every observation up front: 10
  unused for this goal: ['antivirus_updated', 'backup_ran_today', 'backup_verified', 'firewall_on', 'os_updated']
```

Five questions instead of ten, and the five it skipped are the ones about antivirus software and backup jobs that have nothing to do with a stuck print job.

This is why MYCIN was a backward-chaining system. Asking a physician for every possible laboratory value before starting would have been absurd. Asking only for the values some rule currently needs, in the order the reasoning requires, is a consultation.

![Visual explanation of the difference that decides real systems](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_section_the_difference_that_decides_real_systems.png)

## Forward Chaining Is Cheaper Than It Looks

The comparison so far has been slightly unfair to forward chaining, and correcting that matters, because forward chaining is the more widely deployed of the two in production software.

The unfairness is that the program above recomputes everything from nothing. Look at the loop: it scans all eight rules repeatedly, re-testing conditions that have not changed since the last pass. On eight rules this is invisible; on a rule base of ten thousand rules against a working memory of a hundred thousand facts, it would be hopeless.

Real forward-chaining engines do not work that way. They match **incrementally**. When a new fact arrives, the engine does not re-examine every rule; it consults a structure recording which rules were partially satisfied and by what, and updates only the ones the new fact could possibly affect. Most facts affect almost nothing, so most arrivals cost almost nothing.

Two consequences follow, and they explain the intensive care monitor from the opening.

- **Cost scales with change, not with size.** Adding one reading to a knowledge base of a hundred thousand facts costs about as much as adding it to one of a hundred, provided few rules mention that kind of reading.
- **It suits a continuous stream.** A monitoring system receives facts forever and must react as they arrive. Backward chaining would have to be re-run from scratch on every tick, discarding everything it worked out a second earlier, whereas forward chaining simply extends what it already knows.

The trade-off in the table below therefore holds for a single one-off question. For a system that runs continuously against arriving data, forward chaining wins decisively, and the eight-versus-three comparison would be the wrong measurement to make.

![Visual explanation of forward chaining is cheaper than it looks](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_section_forward_chaining_is_cheaper_than_it_looks.png)

## Choosing Between Them

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Forward chaining</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Backward chaining</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Driven by</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Incoming data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A specific goal</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Computes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Everything derivable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Only what bears on the goal</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">On this rule base</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8 rules fired, 10 observations needed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">3 rules examined, 5 questions asked</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Suits</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Monitoring, alerting, streams of sensor data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Diagnosis, consultation, answering one question</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Wasteful when</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Few facts matter to the question asked</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Many goals must be tested against the same facts</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Natural explanation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"Here is what follows from what you told me"</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"Here is why I am asking, and why the answer holds"</td>
    </tr>
  </tbody>
</table>

The last row of "wasteful when" is the honest qualification, and it stops the comparison being one-sided. Backward chaining looks better in this lesson because there was one goal. Ask a hundred different questions of the same facts and backward chaining repeats its work a hundred times, while forward chaining derives everything once and answers all hundred by lookup.

One practical warning. The backward chaining code above will recurse forever on a rule base containing a cycle, such as a rule concluding A from B alongside a rule concluding B from A. Real implementations carry the set of goals currently being pursued and refuse to re-enter one, which is the same repeated-state problem that appeared in graph search wearing different clothes.

![Visual explanation of choosing between them](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_section_choosing_between_them.png)

## Your Turn

Change one thing and watch both techniques behave completely differently.

Remove `"paper_loaded"` from `OBSERVED` so the printer is out of paper, and run both programs again. Predict first: how many rules will forward chaining fire now, and what will backward chaining print at the point where the proof fails? Then check whether forward chaining still derives the backup and compliance facts, and consider whether it should.

Next, change the goal in the backward chaining program from `can_print` to `compliance_ok`, restoring the full observations. Count the rules examined. You should find that backward chaining is now the one ignoring everything about printers, which demonstrates that neither technique is inherently more efficient. Relevance is defined by the question, and the question is not a property of the rule base.

Finally, add a rule that concludes `network_ok` from `printer_reachable`, alongside the existing rule concluding `printer_reachable` from `network_ok`. Do not run the backward chaining program yet. Work out on paper what will happen when it tries to prove `can_print`, then decide what you would add to the function to make it safe. If your answer is a set of goals currently in progress, checked before recursing, you have independently reinvented what every real backward-chaining engine does.
