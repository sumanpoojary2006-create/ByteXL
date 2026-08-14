## Introduction

A hospital in Kochi trials a model that flags which discharged patients are likely to need follow-up within thirty days. It performs well, and the pilot is stopped after seven weeks.

Not because of accuracy. Because of a conversation that happened repeatedly. A consultant would look at a flagged patient, disagree, and ask on what basis the flag was raised. The answer available to her was that the model had computed a score above a threshold. She could accept it or override it, and she had nothing to reason with in either direction.

Overriding a system you cannot interrogate is not clinical judgment; it is a coin toss with extra steps. So the consultants overrode nearly everything, the flags became noise, and the trial ended.

The model was not wrong. It was unusable, and the missing property has a name.

**Definition:** `Explainable AI` covers methods for producing an account of why a model reached a particular decision, in a form the person affected by it or responsible for it can check, challenge, and act on.

![Opening scene: A hospital in Kochi trials a model that flags which discharged patients are likely to need follow-up within thirty days.](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_section_introduction.png)

## Two Ways to Get an Explanation

There is a fork in the road, and it is worth being clear which branch you are on.

**Build a model that is transparent by construction.** A short decision tree, a small set of rules, a linear model with a handful of interpretable features. The explanation is the model, and there is nothing to reconstruct.

**Build whatever performs best, then explain it from outside.** Probe the trained model, observe how its output changes as inputs change, and construct an account after the fact. The explanation is a separate artefact and is an approximation of what the model does.

The first is preferable wherever it is affordable, and the reason is that a post-hoc explanation can be wrong. It describes a simplified picture of the model's behaviour, and the simplification may omit exactly the case in front of you.

Reading the code below: two models are defined and compared. `transparent` is a single threshold on one measurement. `opaque` is a weighted sum whose four coefficients are just numbers. Both are then scored on the same twelve patients and both are asked to justify the same decision, which is where they come apart.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzj9p8" 
 width="100%"
></iframe>

```
  transparent rule: 12/12 correct
      weighted sum: 12/12 correct

Same accuracy. Now ask each to justify one decision.

Patient: age 66, 7 days in, 3 prior visits, marker 74

   transparent rule says: 1
      because the marker is 74, which is above 55

   weighted sum says:     1
      because the weighted total is 2.179, which is above 0

The second sentence is true and useless. A clinician cannot check it,
and a patient cannot act on it.
```

| In the code | Which branch of the fork | What its explanation looks like |
| --- | --- | --- |
| `1 if p[3] > 55 else 0` | Transparent by construction | The rule is the explanation, in one sentence |
| The four-coefficient `total` | Opaque, explained later | A number above zero, which nobody can act on |
| `correct` for both | Identical, 12 of 12 | The accuracy trade did not exist here |
| `-0.0131`, `0.2044`, ... | The weights | Each is correct and none is interpretable |

Identical accuracy, and one of them can be discussed with a consultant.

This is the case worth remembering because it removes the usual excuse. **The trade between accuracy and explainability is real in general and frequently assumed where it does not exist.** Here it costs nothing at all, and a team that reached for the weighted sum by default gave away the property that decided whether the system got used.

The trade is genuine when the transparent model is materially worse. The point is to check rather than assume, and to know what the transparency was worth before trading it away.

![Visual explanation of intrinsic posthoc](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_intrinsic_posthoc_context_v4.png)

## Explaining From the Outside

Sometimes the accurate model really is opaque, and something must be reconstructed. The most broadly useful technique needs no access to the model's internals at all: scramble one input column and see how much the model's performance suffers.

Reading the code below: the model is treated as a sealed box, called and never inspected. The experiment is the middle of the loop, where one column is shuffled while every other column stays in place, breaking the link between that measurement and its patient. The 50 seeds are there because a single shuffle could be lucky.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzj9zc" 
 width="100%"
></iframe>

```
Accuracy with the data intact: 1.00

Now shuffle one column at a time and see how much accuracy falls.
A column the model relies on should hurt when scrambled.

       feature  accuracy after    drop
----------------------------------------
           age            1.00    0.00
       days_in            0.98    0.02
  prior_visits            1.00    0.00
        marker            0.51    0.49

Nothing here looked inside the model. Each column was scrambled and
the damage measured, which works on any model at all, however opaque.
```

| In the code | What it is | Note |
| --- | --- | --- |
| `baseline` | Accuracy with the data intact | The reference every row is measured against |
| `rng.shuffle(column)` | The scramble | Destroys one feature's information, keeps its distribution |
| `if k == i else r[k]` | Only column i changes | Isolates the feature being tested |
| `baseline - accuracy(scrambled)` | The drop | Large drop means the model depended on it |
| `for seed in range(50)` | Repetition | One shuffle could be accidentally harmless |
| `opaque` called, never read | Model-agnostic | Works on anything, including a vendor's sealed model |

Scrambling the marker halves accuracy; scrambling age changes nothing. The model is running almost entirely on one measurement, and this was established without inspecting a single coefficient.

`Permutation importance` is valuable precisely because it is indifferent to the model. It works on a decision tree, a neural network, or something a vendor will not let you look inside.

Two limitations must travel with it. It reports importance **across the whole dataset**, not for one patient, so it cannot answer "why was this person flagged". And when two features move together, scrambling one may barely hurt because the other still carries the information, so a genuinely important feature can appear irrelevant.

![Visual explanation of explaining from the outside](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_section_explaining_from_the_outside_simple_v2.png)

## Explaining One Decision

The consultant's question was about one patient, and there is a form of explanation built for exactly that: what would have had to be different.

Reading the code below: the search is deliberately brute force. For each feature it tries changes of increasing size, in both directions, and stops at the first one that flips the decision. Because `change` counts up from 1, the first flip found is the smallest. `CHANGEABLE` is not used by the search at all; it only annotates the output, and that separation is the point of the section.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjab8" 
 width="100%"
></iframe>

```
Patient: age 55, days_in 8, prior_visits 2, marker 70
Decision: follow-up needed

Smallest change to any single measurement that would flip it:

             age:  55 -> 207  (+152)   <- cannot be changed
         days_in: no reachable value flips the decision
    prior_visits: no reachable value flips the decision   <- cannot be changed
          marker:  70 -> 48   (-22)

Three of the four rows are useless as advice. Age cannot be altered,
prior visits are history, and days already spent cannot be reduced
far enough to matter. Only the marker offers a real answer, and it
is the one worth telling the patient about.
```

| In the code | What it is | Note |
| --- | --- | --- |
| `target = 1 - opaque(patient)` | The opposite decision | What the search is trying to reach |
| `for change in range(1, 300)` | Increasing sizes | Counting up guarantees the smallest flip is found first |
| `for direction in (-1, 1)` | Both ways | A feature might need to rise or fall |
| `found` staying `None` | No reachable value | Informative: this decision does not hinge on that feature |
| `CHANGEABLE` | Never used by the search | Pure annotation, and the whole point of the section |
| `age: 55 -> 207` | A valid counterfactual | True, and worthless as advice |

A `counterfactual explanation` states what would have produced a different outcome, and it is the form people find most natural because it is how humans explain decisions to each other.

The output shows why it is not merely a technical exercise. Three of the four answers are true and worthless. Telling someone the decision would differ if they were 152 years older is arithmetic, not an explanation. **A useful counterfactual must be restricted to things that can actually change**, which requires somebody to state which features are actionable, and that is a judgment the model cannot supply.

Note also the two rows saying no reachable value flips the decision. That is genuinely informative: it says the outcome does not hinge on those measurements at all for this patient, which is a stronger statement than a small importance score.

![Visual explanation of local explanation audiences](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_local_explanation_audiences_context_v4.png)

## Explaining Models Without Features

Everything so far assumed named input columns: age, marker, days in hospital. Scrambling a column or asking what would have to change makes sense because each column means something.

An image classifier has no such columns. Its inputs are two million brightness values, and "pixel 41,208 was important" is not an explanation anybody can use. A different family of methods is needed.

`Saliency maps` highlight the regions of an image that most affected the output, typically by measuring how much the prediction changes as each region is altered or obscured. The result is a heat map laid over the picture showing where the model was looking, and it is genuinely useful for one particular purpose: catching a model that is right for the wrong reason.

This is how the spurious-correlation failures described earlier in this unit are found. A model detecting disease from chest scans, examined this way, may turn out to be attending to a marker in the corner of the image identifying which hospital took it rather than to anything anatomical. The accuracy figure gave no hint; the heat map made it obvious in one glance.

For language models, the equivalent temptation is to read the attention weights, on the reasoning that attention shows what the model was looking at. This should be resisted, or at least heavily qualified. Attention weights show where information was gathered from, which is related to but not the same as what determined the output, and models have many attention heads doing many different things at once. A tidy attention picture can be produced for a model whose actual behaviour is nothing like the picture suggests.

The general caution applies to all of these. **A visual explanation is persuasive out of proportion to its reliability.** A heat map looks like evidence in a way a number does not, and it is still an approximation produced by a separate method, capable of being confidently wrong about a model that is itself confidently wrong.

![Visual explanation of explaining models without features](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_section_explaining_models_without_features.png)

## Who the Explanation Is For

The word covers several distinct needs, and a form that serves one may fail another.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Who is asking</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What they need</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Suitable form</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The person affected</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What to do differently</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A counterfactual over changeable features</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The professional using it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Whether to trust it this time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Which inputs drove this case, and how confident</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The team maintaining it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Whether it is right for the right reason</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Importance across the dataset; probing for spurious features</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A regulator</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Whether the basis is permissible</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Documented features, data sources, and tested behaviour</td>
    </tr>
  </tbody>
</table>

The Kochi hospital needed the second row and was given nothing, which is why the trial failed. A score above a threshold does not help a consultant decide whether to trust the system on this occasion.

One caution that deserves stating plainly. An explanation that sounds convincing is not thereby correct, and post-hoc methods can produce plausible accounts of behaviour the model is not actually exhibiting. A confident explanation can increase trust without increasing trustworthiness, which is worse than no explanation at all.

![Visual explanation of who the explanation is for](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_section_who_the_explanation_is_for.png)

## Your Turn

Rerun the pilot properly.

Given that the transparent rule matched the weighted sum exactly on this data, write the one-sentence explanation a consultant would receive under each model, and then decide what the hospital should deploy. Then state the condition under which you would change your mind: how much better would the opaque model have to be, in what measure, before giving up the explanation becomes worth it? Putting a number on that before you see the results is the honest way to make the decision.

Then break permutation importance deliberately. Add a fifth column to the patient data that is simply the marker plus a small constant, so the two are nearly identical. Rerun the importance calculation and watch what happens to the marker's score. Both features will now look unimportant, because scrambling either leaves the other carrying the information. Explain why this makes importance scores dangerous to read as "this feature does not matter".

Finally, write the patient-facing sentence. For the patient in the counterfactual program, draft what you would actually say to them, in plain language, using only the actionable row. Then draft what you would say if the only feature that could flip the decision had been age. The second is the harder writing task, and the fact that there is no good version of it is a real finding about the limits of explanation.
