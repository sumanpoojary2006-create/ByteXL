## Introduction

At a two-wheeler service centre in Mysuru, the senior mechanic Iqbal has a habit his apprentices find maddening. A scooter comes in that will not start, and instead of opening anything he asks questions.

Does the starter turn, or is it silent? It turns. Is there petrol in the tank? Yes. He pulls the spark plug, looks at it for two seconds, and says the plug is fouled, clean it and it will start. It starts.

The apprentices assume this is instinct. It is not, and Iqbal can prove it, because when pressed he says the reasoning out loud. If it does not start but the starter turns, the electrics are fine, so the problem is fuel or spark. If there is petrol in the tank, it is not fuel, so it is spark. If it is a spark problem and the plug is black and wet, the plug is fouled.

Written like that, his expertise has an obvious shape. Each step is a rule of the form "if these things are true, then conclude this". Each conclusion becomes a fact the next rule can use. What looked like a single leap of judgment is a chain of small, checkable steps.

A system built out of exactly these pieces, a store of facts and a set of rules that fire when their conditions are met, is called a **production system**, and it is the most widely deployed form of reasoning machinery in commercial software.

**Definition:** `Rule-based reasoning` derives new facts by repeatedly matching `rules` of the form "if conditions then conclusion" against the `facts` currently known, adding each conclusion to the store of facts so that further rules become applicable.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_introduction.png)

## The Three Parts of a Production System

The architecture has three components, and the third is the one that does the work.

1. **Working memory.** The facts currently believed. For Iqbal's consultation it starts as the reported symptoms and grows as conclusions are drawn.

2. **The rule base.** The rules, each with a set of conditions and a single conclusion. These are general knowledge about scooters, unchanged from one customer to the next.

3. **The recognise-act cycle.** The engine. It repeatedly finds which rules can fire, chooses one, fires it, and adds the conclusion to working memory, stopping when nothing more can fire.

The cycle has three named phases worth learning, because they are the vocabulary used everywhere this architecture appears.

- **Match.** Find every rule whose conditions are all satisfied by working memory. This collection is the `conflict set`.
- **Resolve.** Choose one rule from the conflict set. This step is called `conflict resolution` and is discussed properly below.
- **Act.** Fire the chosen rule, adding its conclusion to working memory.

Then repeat. The name "production system" comes from these rules historically being called productions, because they produce new facts.

![Visual explanation of production system cycle](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_production_system_cycle_context_v4.png)

## Iqbal's Knowledge as a Rule Base

Here is his reasoning encoded, with a few extra rules for cases he sees often.

Reading the code below: `RULES` is Iqbal's knowledge as data, `working_memory` is what is known about this scooter, and `eligible` is the match step in a single line. The loop at the bottom is the recognise-act cycle. Notice that no part of this code knows anything about scooters.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzje75" 
 width="100%"
></iframe>

```
Reported symptoms:
  - engine does not start
  - plug is black and wet
  - starter turns
  - tank has petrol

cycle 1: eligible = [R1, R7], fired R1
         added: fuel or spark problem
cycle 2: eligible = [R3, R7], fired R3
         added: spark problem suspected
cycle 3: eligible = [R5, R7], fired R5
         added: DIAGNOSIS: fouled spark plug
cycle 4: eligible = [R7], fired R7
         added: engine is running rich

No rule can fire. Final conclusions:
  * DIAGNOSIS: fouled spark plug
```

The engine reproduced Iqbal's diagnosis in four cycles, and the trace is the explanation facility from the previous lesson, produced for free. Asked how it knows the plug is fouled, the system can point at R5, which needed R3's conclusion, which needed R1's.

Five pieces map onto the three phases named earlier.

| In the code | Phase | What it does |
| --- | --- | --- |
| `r["if"] <= facts` | Match | Subset test: are all of this rule's conditions currently believed? |
| `r["then"] not in facts` | Match | Skip rules concluding something already known, so the loop terminates |
| `eligible(...)` | Match | Returns the conflict set: every rule that could fire right now |
| `conflict_set[0]` | Resolve | Choose one. Here, simply the first listed |
| `working_memory.add(...)` | Act | Add the conclusion, which may make new rules eligible next cycle |

The `<=` in the first row is the piece worth pausing on. On Python sets it means "is a subset of", so one operator asks whether every condition of a rule is satisfied. That single character is the entire pattern-matching step of a production system.

Look also at the `eligible` column across the cycles. At every step there were **two** applicable rules, not one. R7 sat there from the beginning, ready to conclude that the engine is running rich, and something had to decide it should wait.

![Visual explanation of iqbal's knowledge as a rule base](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_iqbal_s_knowledge_as_a_rule_base_simple_v2.png)

## Rules Are Not If-Statements

Before going further it is worth being precise about what has actually been built, because the code above looks superficially like a long chain of conditionals and is a fundamentally different thing.

An if-statement is an instruction: when control reaches this line, test this condition. Its position in the program determines when it runs, and the programmer decides that position. A rule is a piece of data: a claim that whenever these conditions hold, this conclusion follows. Nothing in a rule says when it should be considered, because the engine considers all of them on every cycle.

Four consequences follow, and each is a reason to prefer rules where the domain is genuinely knowledge-heavy.

1. **Order in the list is not control flow.** Reorder the rules and the conclusions do not change, as the strategy comparison below demonstrates. Reorder if-statements and the program's behaviour usually changes, sometimes silently.

2. **Knowledge can be added without reading the rest.** To teach the system a new fault, Iqbal writes one rule. He does not need to know where in an existing procedure it belongs, or which branch it should sit inside, because there is no procedure.

3. **The rules are inspectable by their owner.** Iqbal can read `{"engine does not start", "starter turns"} -> "fuel or spark problem"` and tell you whether it is right. He cannot read control flow.

4. **The same engine works anywhere.** The `eligible` function contains no knowledge of scooters whatsoever, which is the separation of knowledge from reasoning made concrete in six lines.

The cost is speed. A production system re-examines every rule on every cycle, which an if-cascade never does. That cost is real and, in a domain where the knowledge changes more often than the code, it is a good trade.

![Visual explanation of rules are not if-statements](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_rules_are_not_if_statements.png)

## Conflict Resolution

Whenever more than one rule can fire, the engine must choose, and the choice is not arbitrary. Several standard strategies exist.

- **Rule order.** Fire the first applicable rule in the listed order. Simple, predictable, and it makes the ordering of the rule base silently significant.
- **Specificity.** Prefer the rule with the most conditions, on the reasoning that a rule matching a more detailed situation is better informed than a general one.
- **Recency.** Prefer the rule whose conditions were satisfied by the most recently added facts, which keeps the reasoning following one line of enquiry rather than jumping about.
- **Explicit priority.** Attach a number to each rule and fire the highest. Crude, effective, and the usual choice in commercial systems where a safety rule must always beat a convenience rule.

The interesting question is how much the choice actually matters.

Reading the code below: the rule base and symptoms are unchanged. Three tiny functions implement three different conflict-resolution strategies, and the loop runs the identical engine with each in turn, recording both the firing order and the final conclusion.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjemj" 
 width="100%"
></iframe>

```
first listed rule    fired R1 -> R3 -> R5 -> R7
                     concluded ['DIAGNOSIS: fouled spark plug']
most specific rule   fired R1 -> R3 -> R5 -> R7
                     concluded ['DIAGNOSIS: fouled spark plug']
fewest conditions    fired R7 -> R1 -> R3 -> R5
                     concluded ['DIAGNOSIS: fouled spark plug']
```

Three strategies, two different firing orders, one identical conclusion.

| In the code | Strategy | Result here |
| --- | --- | --- |
| `conflict_set[0]` | Whichever rule was listed first | R1, R3, R5, R7 |
| `max(..., key=len(r["if"]))` | Most conditions, so most specific | R1, R3, R5, R7 |
| `min(..., key=len(r["if"]))` | Fewest conditions, chosen to be awkward | R7, R1, R3, R5 |

One line changed between the three runs, the order changed, and the diagnosis did not. This is worth stating as a property rather than an accident.

**In a rule base that only ever adds facts, conflict resolution changes the path, not the destination.** Every rule that can eventually fire will fire, because nothing ever removes a fact that another rule was waiting on, so the order affects only how quickly the answer appears and how sensible the explanation reads.

The property fails the moment rules can also **retract** facts. A rule that removes something from working memory can disable another rule that was about to fire, and then the order determines the outcome. Real production systems allow retraction, which is why they take conflict resolution seriously rather than treating it as a tidiness question.

![Visual explanation of conflict resolution](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_conflict_resolution.png)

## The Same Rule Base, Different Cases

The reason to build a rule base rather than write a diagnostic procedure is that one rule base handles every case, including ones nobody traced through by hand.

Reading the code below: nothing here is new. The seven rules are unchanged and `consult` is the recognise-act cycle compressed into six lines. The only addition is a dictionary of four different symptom sets, all fed through the same engine.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjey7" 
 width="100%"
></iframe>

```
Fouled plug     R1 -> R3 -> R5 -> R7
                ['DIAGNOSIS: fouled spark plug']
Flat battery    R2 -> R6
                ['DIAGNOSIS: battery discharged']
Empty tank      R1 -> R4
                ['DIAGNOSIS: out of fuel']
Nothing known   no rule fired
                no diagnosis reached
```

Four cases, four different chains through the same seven rules, and nobody wrote a case-by-case procedure. Adding an eighth rule extends all four consultations at once, which is the reuse that makes this architecture worth its overhead.

The final row is the most instructive. Told only that the engine does not start, the system fires nothing and reports no diagnosis, which is exactly right. It has not failed; it has correctly determined that the available facts are insufficient. Compare that with a system that guesses. **A production system's silence is information**, and a good one distinguishes "I have concluded nothing" from "I have concluded there is no fault".

![Visual explanation of the same rule base, different cases](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_the_same_rule_base_different_cases.png)

## When the Conclusion Is Not Certain

Everything so far has treated a fired rule as establishing its conclusion outright, and Iqbal would object to that if he read the rule base carefully.

A black wet plug usually means fouling. Occasionally it means a much worse problem further inside the engine that is producing the same symptom. His real knowledge is not "if the plug is black and wet then it is fouled" but "if the plug is black and wet then it is very probably fouled". The rule base has no way to record the words "very probably", so it does not record them, and the system is more confident than the mechanic it was built from.

The classic response is a `certainty factor`: a number attached to each rule expressing how strongly its conditions support its conclusion, and a number attached to each fact expressing how strongly it is currently believed. When a rule fires, the confidence of its conclusion is derived from the confidence of its conditions combined with the strength of the rule, and when two rules independently support the same conclusion, their contributions reinforce each other.

Two things about this are worth knowing.

- **It changes what a diagnosis is.** Instead of one conclusion, the system produces a ranked list: fouled plug at high confidence, deeper engine fault at low confidence, which is far closer to what Iqbal would actually say if pressed.
- **It is not proper probability.** Certainty factors were invented because a full probabilistic treatment was thought impractical at the time, and the arithmetic for combining them is a reasonable-looking convention rather than something derived from the mathematics of probability. It works well enough in narrow domains and behaves oddly at the edges.

For now the important point is the gap itself. **A plain production system cannot distinguish a rule that is always right from one that is usually right**, and any domain where that distinction matters needs something added.

![Visual explanation of when the conclusion is not certain](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_when_the_conclusion_is_not_certain.png)

## Rule-Based Reasoning at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Element</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Role</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">In the code above</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Working memory</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Facts currently believed about this case</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The <code>facts</code> set</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Rule base</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">General domain knowledge, unchanged per case</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The <code>RULES</code> list</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Match</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Find every rule whose conditions hold</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>r["if"] &lt;= facts</code></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Conflict set</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">All rules eligible this cycle</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The list returned by <code>eligible</code></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Conflict resolution</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Choose which eligible rule to fire</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The <code>strategy</code> function</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Act</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Add the conclusion to working memory</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>facts.add(chosen["then"])</code></td>
    </tr>
  </tbody>
</table>

![Visual explanation of rule-based reasoning at a glance](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_rule_based_reasoning_at_a_glance.png)

## Your Turn

Extend Iqbal's rule base with a fault he sees every monsoon: a scooter that starts but cuts out after a minute, caused by water in the fuel.

Add the rules and the symptoms needed to reach a diagnosis of water in the fuel, then run the four cases again and check that none of the existing four diagnoses changed. That check is the point of the exercise. A rule base that silently alters an unrelated conclusion when you add knowledge is broken, and the only way to find out is to test the old cases after every addition.

Then break it deliberately. Add a rule concluding "DIAGNOSIS: out of fuel" from the single condition "engine does not start", run the empty tank case, and watch what happens to the trace. You will get the right answer for the wrong reason, and no error will be reported anywhere, because a production system cannot tell the difference between a rule that is correct and a rule that merely fires at a convenient moment. That silent failure mode is why rule bases become unmaintainable at scale, and it is worth seeing at seven rules rather than discovering at seven hundred.
