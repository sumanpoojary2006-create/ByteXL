## Introduction

At half past nine on a Tuesday, the network support desk at a college in Coimbatore receives a call: the internet is down in the library.

Two technicians respond differently. Nikhil says the router has failed, because a failed router takes the internet down, and the internet is down. He picks up a replacement router and starts walking. Sneha says something more careful: the internet being down is consistent with a failed router, and also with a cut cable, an expired lease from the provider, or a tripped switch, so the observation alone does not establish which.

An hour later they find the fault is at the provider's end. Nikhil's router was fine, and he carried it across campus for nothing.

The interesting thing is that Nikhil's reasoning was not sloppy in any way he could see. He had a true rule and a true observation, and he combined them, and the combination happened to be one of the invalid ones. What he lacked was not information or care. It was a precise account of when a conclusion genuinely follows from what is known, and that account is **logical inference**.

**Definition:** `Logical inference` is the derivation of new statements from known ones. A knowledge base `entails` a statement when that statement is true in every situation in which everything in the knowledge base is true, and a valid inference procedure derives only entailed statements.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_section_introduction.png)

## Entailment: The Standard Everything Is Measured Against

The central definition is short and worth reading twice.

A knowledge base entails a statement when **there is no possible situation in which the knowledge base is true and the statement is false.**

Notice what the definition does not mention. It says nothing about proofs, rules, or procedures. It is purely about situations, called `models`: an assignment of truth values to every proposition, one possible way the world could be. Entailment is then a relationship between two sets of models. The knowledge base rules out some worlds and permits others, and a statement is entailed when it happens to be true in every world the knowledge base still permits.

This gives an immediate method. To decide whether something is entailed, enumerate every model, throw away those in which the knowledge base is false, and check whether the statement holds in all of the survivors. This is called `model checking`, and it is the most direct way to see what entailment means.

![Visual explanation of entailment soundness](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_entailment_soundness_context_v4.png)

## Checking Nikhil's Reasoning

Encode the situation with three propositions and the two rules everyone agreed on.

Reading the code below: `all_models` produces every possible world, `knowledge_base` says which of them are consistent with what is known, and `entails` is the definition of entailment written as four lines of Python. That last function is the whole lesson.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjhn5" 
 width="100%"
></iframe>

```
Models in which the knowledge base is true:
  power_cut=False, router_down=False, internet_down=True 
  power_cut=False, router_down=True , internet_down=True 
  power_cut=True , router_down=True , internet_down=True 

NOT ENTAILED : the router is down
               counterexample: power_cut=False, router_down=False, internet_down=True
ENTAILED     : the internet is down
NOT ENTAILED : there is no power cut
               counterexample: power_cut=True, router_down=True, internet_down=True
```

Eight models exist. Three survive the knowledge base, and those three are the full extent of what is currently known about the world.

Nikhil's conclusion fails, and the output does not merely say so, it produces the situation that defeats him: no power cut, router working, internet down. That is precisely the provider-side fault they eventually found. **A failed entailment check hands you a concrete counterexample**, which is far more useful than a verdict, because it describes exactly the case the reasoning overlooked.

The `entails` function is worth reading as a definition rather than as code.

| In the code | What it corresponds to |
| --- | --- |
| `all_models(symbols)` | Every situation that could conceivably hold |
| `kb(m)` | This situation is consistent with everything known |
| `not query(m)` | ...and yet the query is false in it |
| `return False, m` | A counterexample exists, so the query is **not** entailed |
| `return True, None` | No counterexample after checking all of them: entailed |

Read those five rows in order and they spell out the definition from the start of this lesson, word for word. There is no cleverness in the function; it is the definition, executed. And because it returns the offending model rather than merely `False`, a failed check hands you the exact situation your reasoning overlooked.

![Visual explanation of checking nikhil's reasoning](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_section_checking_nikhil_s_reasoning_simple_v2.png)

## Deduction, Soundness, and Completeness

Model checking is a fine way to understand entailment and a poor way to compute it, because enumerating models becomes impossible quickly. The alternative is `deduction`: applying rules of inference that manipulate the statements themselves, without enumerating anything.

The most familiar rule is **modus ponens**: from "if P then Q" together with P, derive Q. Applying it requires no models, only pattern matching on the shape of what is written.

That raises the question this whole area turns on. If a procedure shuffles symbols according to rules, how do we know its conclusions are actually true? Two properties answer it, and they are the two most important words in this lesson.

- **Soundness.** Everything the procedure derives is genuinely entailed. A sound procedure never produces a falsehood from true premises. Without soundness the procedure is worthless, because its output cannot be trusted at all.
- **Completeness.** Everything genuinely entailed can be derived by the procedure. Without completeness the procedure is still trustworthy, but it may fail to find a conclusion that really does follow.

Soundness is the non-negotiable one. A sound but incomplete procedure sometimes says "I could not establish that", which is honest. An unsound procedure sometimes says "yes" when the answer is no, which is Nikhil walking across campus.

The four classic argument patterns can be checked for soundness mechanically, which is a satisfying way to settle arguments that have been going on since antiquity.

Reading the code below: `valid` is the same counterexample hunt as before, applied to an argument rather than a knowledge base. Each entry in `arguments` is a list of premises and a conclusion, all written as small functions of a model.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjj5r" 
 width="100%"
></iframe>

```
VALID   Modus ponens: (P implies Q), P, therefore Q
VALID   Modus tollens: (P implies Q), not Q, therefore not P
INVALID Affirming the consequent: (P implies Q), Q, therefore P
        broken when P=False, Q=True
INVALID Denying the antecedent: (P implies Q), not P, therefore not Q
        broken when P=False, Q=True
```

Both invalid patterns break in exactly the same situation, P false and Q true, and that single row is Nikhil's morning. The rule "router down implies internet down" is true, the internet is down, and the router is fine, all at once. Nothing about his premises was wrong. The step between them was.

Note also that the two valid patterns are valid **for any P and Q whatsoever**. Modus ponens works for routers, for blood tests, and for statements about nothing at all, which is why an inference engine can be written once and pointed at any domain.

![Visual explanation of deduction, soundness, and completeness](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_section_deduction_soundness_and_completeness.png)

## Using Entailment to Solve a Problem

Entailment is not only a way to audit reasoning. Framed correctly, it answers questions.

The duty roster at the same college has to be worked out from partial information. At least one of Asha, Bala, and Chandra is on duty tonight. If Asha is on duty then Chandra must be too, because Asha is still under training. Bala is on leave. And the two senior staff, Asha and Chandra, are never rostered together.

Reading the code below: each English constraint becomes one named line inside `knowledge_base`, which makes the translation checkable. Instead of asking about one query, this program keeps every surviving model and then reports a three-way verdict for each person.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjjvf" 
 width="100%"
></iframe>

```
Assignments consistent with everything known: 1 of 8
  on duty: Chandra

  Asha     is off duty in every surviving model -> ENTAILED to be off
  Bala     is off duty in every surviving model -> ENTAILED to be off
  Chandra  is on duty in every surviving model  -> ENTAILED
```

One model survives out of eight, so the roster is fully determined and Chandra is on duty. Nobody wrote a rule saying so; it follows from four constraints none of which mentions the answer.

The three-way verdict at the end is worth dwelling on, because it is how a knowledge-based system should report.

| In the code | Verdict | Means |
| --- | --- | --- |
| `all(m[name] for m in survivors)` | Entailed | On duty in every surviving model |
| `all(not m[name] for m in survivors)` | Entailed false | Off duty in every surviving model |
| neither | **Unknown** | It genuinely varies; the facts do not settle it |

A statement can be entailed, entailed to be false, or genuinely unknown, and a system that collapses the third into either of the first two is lying. Had two models survived with Chandra on duty in one and off in the other, the correct answer would have been "unknown", not a guess.

![Visual explanation of logical inference worked](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_logical_inference_worked_context_v4.png)

## Inference at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Term</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Why it matters</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Model</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One possible assignment of truth values to every proposition</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The unit in which entailment is defined</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Entailment</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">True in every model where the knowledge base is true</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The standard a procedure is judged against</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Model checking</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Enumerate models, keep those satisfying the KB, test the query</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Direct and clear; impractical beyond small problems</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Deduction</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Apply inference rules to the statements themselves</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scales, because no models are enumerated</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Soundness</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Everything derived is entailed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Non-negotiable; without it the output is untrustworthy</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Completeness</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Everything entailed can be derived</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Desirable; its absence means missed conclusions, not false ones</td>
    </tr>
  </tbody>
</table>

![Visual explanation of inference at a glance](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_section_inference_at_a_glance.png)

## Your Turn

Take the network knowledge base and add one statement: the provider has confirmed its service is running normally, which rules out the provider-side fault.

You will need a fourth proposition for the provider, plus a rule saying the internet can only be down if either the router is down or the provider has a fault. Add both, rerun the first program, and check whether "the router is down" is now entailed. Before you run it, predict the answer, and predict how many models will survive.

Then do the part that matters more. Delete the "at least one" line from the duty roster program and rerun it. You will get more than one surviving model, and the three-way verdict will start reporting UNKNOWN. Work out for each of the three people whether their status is genuinely undetermined or whether you have merely broken the program, and satisfy yourself that the difference is visible in the surviving models themselves.

Finally, construct a knowledge base with **zero** surviving models, which is easy to do by accident and important to recognise. Then answer this: what does the `entails` function return for *any* query at all when no model survives, and why? The answer follows directly from the definition, it is initially alarming, and every real system has to detect this case explicitly. An inconsistent knowledge base entails everything, including statements and their negations, which is why consistency checking is not an optional extra.
