## Introduction

A cooperative bank in Belagavi buys a loan-scoring model, deploys it, and withdraws it eleven weeks later. The model was accurate. That was never the problem.

The problem arrived the first time an applicant was rejected and asked why. The branch manager could not say. The vendor's documentation explained that the model compared each applicant against similar past applicants, which is true and is not an answer anyone can act on. The applicant wanted to know what to change. The bank's compliance officer wanted a rule she could check against lending policy. The regulator, when it eventually asked, wanted the criteria in writing.

What the bank needed was not a more accurate model. It was a model whose reasoning could be printed on a single sheet of paper, read by a branch manager with no technical training, and defended to a regulator. That requirement rules out most of machine learning and points directly at one model family.

A **decision tree** is a chain of yes-or-no questions ending in a verdict, learned from data rather than written by a policy committee.

**Definition:** A `decision tree` is a model that repeatedly splits the data on one feature at a time, choosing at each step the split that best separates the classes, producing a branching structure whose leaves give the prediction and whose path from the root is a readable explanation.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_section_introduction.png)

## The Shape of a Tree

A tree has three kinds of component.

- **The root** is the first question, asked of every applicant.
- **Internal nodes** are further questions, asked only of applicants who reached them.
- **Leaves** are the verdicts, where no further question is asked.

Following one applicant from root to leaf produces a sentence like "credit score above 615, and employed for more than six months, therefore approve". That sentence is simultaneously the prediction and the explanation, which is the property no other model in this unit has.

The learning problem is deciding which question to ask first, which to ask next, and when to stop.

![Visual explanation of the shape of a tree](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_section_the_shape_of_a_tree.png)

## Choosing a Split

At any node, the algorithm considers every feature and every threshold, and picks the one that best separates approved from rejected applicants. "Best" needs a number, and the usual one measures how mixed a group is.

`Gini impurity` is the probability that two applicants drawn at random from a group have different outcomes. A group where everybody was approved has impurity 0, because any two draws match. A group split evenly between approved and rejected has impurity 0.5, the worst possible for two classes.

A candidate split produces two groups, and its quality is the average of their impurities, weighted by size. Lower is better, because it means the split has sorted the applicants into purer piles.

Reading the code below: `gini` scores how mixed a group is, `weighted_gini` scores a whole split, and the loop at the bottom tries every threshold on every feature. That brute-force loop is exactly what a decision tree does at each node.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzk4xv" 
 width="100%"
></iframe>

```
Impurity of the whole training set: 0.430
(11 approved out of 16)

Best threshold for each feature, judged by impurity after the split:

         feature  threshold  impurity after  improvement
----------------------------------------------------------
        income_k       31.5           0.214        0.216
  years_employed        4.5           0.278        0.152
    credit_score      615.0           0.115        0.315
```

Credit score wins, and the numbers say why rather than merely asserting it. Splitting at 615 drops impurity from 0.430 to 0.115, an improvement of 0.315, against 0.216 for the best income split.

| In the code | What it computes | Reading it |
| --- | --- | --- |
| `1 - p**2 - (1-p)**2` | Gini impurity of one group | 0 when pure, 0.5 when evenly split |
| `weighted_gini(left, right)` | Impurity after a split | Each side counts in proportion to its size |
| `zip(values, values[1:])` | Adjacent pairs of observed values | Their midpoints are the candidate thresholds |
| `if score < best[1]` | Keep the purest split | Tries every feature and every threshold, then picks one |

Two things about this procedure deserve attention.

**Thresholds are found, not supplied.** Nobody told the algorithm that 615 was significant. It tried the midpoint between every pair of adjacent credit scores in the data and kept whichever separated best. This is why decision trees handle numeric features without any preparation.

**The choice is greedy.** The algorithm picks the best split available right now, with no consideration of what splits will be available afterwards. That is fast, and it does not guarantee the best tree overall, because a slightly worse first question might have enabled two excellent second ones. Finding the genuinely optimal tree is computationally infeasible, so every practical tree algorithm is greedy in this way.

![Visual explanation of decision tree splits](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_decision_tree_splits.png)

## Other Ways to Measure a Split

Gini impurity is one measure of how mixed a group is, and it is worth knowing that it is a choice rather than the definition.

The main alternative is `entropy`, borrowed from information theory, which measures how many bits are needed on average to record the outcome for a member of the group. A pure group needs none, because the answer is already known. An evenly split group needs one full bit. The reduction in entropy achieved by a split is called `information gain`, and choosing the split with the highest information gain is the criterion used by the classic tree algorithms.

In practice the two almost always pick the same split. Entropy involves logarithms and is slightly slower; Gini is a simple sum of squares. Neither is meaningfully more accurate, and the choice is usually left at whatever the library defaults to. What matters is understanding what both are for: **turning "this split separates the classes well" into a number that can be compared across every candidate feature and threshold.**

A third variant appears when the label is a number rather than a category. A `regression tree` predicts a continuous value, so impurity is measured as variance instead, and each leaf predicts the average of its members. The structure and the greedy search are unchanged, which is why trees handle both kinds of problem with one idea.

![Visual explanation of other ways to measure a split](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_section_other_ways_to_measure_a_split.png)

## Categorical Features Need No Encoding

One practical advantage deserves calling out, because it distinguishes trees from most other models.

A distance-based method cannot use a feature like the applicant's branch or occupation directly. Distance requires numbers, so categories have to be converted, and converting them badly invents an order that does not exist.

A tree has no such problem. It never computes a distance. It asks whether a value falls in one set of categories or another, which is meaningful for occupations and branches exactly as it is for numbers. A split becomes "is the occupation salaried or pensioned, or is it something else", and the same impurity calculation judges it against every numeric threshold on equal terms.

This is why trees are often the first model tried on the kind of mixed table an organisation actually holds, where a few numeric columns sit beside a dozen categorical ones and preparing all of them for a distance-based method would be most of the work.

![Visual explanation of categorical features need no encoding](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_section_categorical_features_need_no_encoding.png)

## Growing the Whole Tree

Having chosen a split, the same procedure runs again on each side, and again, until a group is pure or a limit is reached.

Reading the code below: `best_split` is the search from the previous program packaged as a function. `build` is the new part, and it is recursive in the most literal way, calling itself on the left and right halves. `show` and `predict` merely walk the structure it produces.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzk5m7" 
 width="100%"
></iframe>

```
Learned decision tree:

is credit_score <= 615.0 ?   [16 applications]
    yes -> REJECT   (0 of 4 approved)
    no  -> is years_employed <= 0.5 ?   [12 applications]
        yes -> REJECT   (0 of 1 approved)
        no  -> APPROVE  (11 of 11 approved)

Training accuracy: 16/16
```

That printout is what the bank was asking for. It fits on a sheet of paper, a branch manager can read it, and a rejected applicant can be told exactly what happened: your credit score was below 615.

| In the code | What it is | Note |
| --- | --- | --- |
| `if approved == 0 or approved == len(rows)` | The group is pure | Nothing left to split on, so make a leaf |
| `depth == max_depth` | The depth limit | The only thing stopping the tree from growing forever |
| `build(left, depth+1, ...)` | Recursion | The same procedure, applied to a smaller group |
| `{"feature":..., "left":..., "right":...}` | The tree itself | A nested dictionary, which is why `predict` is a simple loop |

The model discovered two things nobody told it. Credit score matters most, and among applicants who clear the score threshold, having no employment history at all is disqualifying. Both are sensible lending policy, and neither was written by a policy committee.

Look closely at the middle leaf, though. It rejects on the basis of **one applicant**. A rule derived from a single example is not a rule, it is a memory, and if that applicant had been recorded differently the branch would not exist. This is the characteristic weakness of decision trees, and it has a name.

![Visual explanation of growing the whole tree](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_section_growing_the_whole_tree.png)

## Trees Memorise

Left alone, a decision tree will keep splitting until every leaf is pure, which on any dataset with a few unusual examples means growing branches that describe individuals rather than patterns.

Limiting the depth is the standard control, and its effect is visible directly.

Reading the code below: `build` and `predict` are unchanged. Two new helpers appear, `leaves` to count how big the tree got and `rules` to convert it into readable sentences, and the final loop builds the same tree three times at three depth limits.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzk62f" 
 width="100%"
></iframe>

```
max_depth=1: 2 leaves, training accuracy 0.94
    REJECT   when credit_score <= 615.0
    APPROVE  when credit_score > 615.0

max_depth=2: 3 leaves, training accuracy 1.00
    REJECT   when credit_score <= 615.0
    REJECT   when credit_score > 615.0 and years_employed <= 0.5
    APPROVE  when credit_score > 615.0 and years_employed > 0.5

max_depth=3: 3 leaves, training accuracy 1.00
    REJECT   when credit_score <= 615.0
    REJECT   when credit_score > 615.0 and years_employed <= 0.5
    APPROVE  when credit_score > 615.0 and years_employed > 0.5
```

A tree of depth 1, a single question, is already right about 15 of 16 applicants. Depth 2 reaches perfection by adding the employment rule. Depth 3 adds nothing, because the data ran out of impurity to remove.

The final output form is worth noticing in its own right: a tree converted into a numbered list of conditions. **A decision tree is a set of rules that was learned rather than written**, which puts it in the same readable form as a hand-built rule base while requiring no expert to sit down and enumerate the cases.

![Visual explanation of tree overfitting pruning](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_tree_overfitting_pruning.png)

## What Trees Are Good and Bad At

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strength</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Weakness</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Readable by non-specialists, and printable as rules</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Grows branches that describe single examples unless restrained</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs no feature scaling, since each feature is judged alone</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unstable: a few changed rows can produce a completely different tree</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Handles numeric and categorical features together</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Splits are axis-aligned, so diagonal boundaries need many steps</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Selects its own features; unhelpful ones are simply never split on</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Greedy, so the tree found is rarely the best tree possible</td>
    </tr>
  </tbody>
</table>

The instability in the second row is why single trees are often replaced in practice by ensembles, which grow many trees on varied samples of the data and let them vote. Accuracy improves substantially. Readability, the entire reason the Belagavi bank wanted a tree, is lost completely, and that trade is a decision rather than an upgrade.

![Visual explanation of what trees are good and bad at](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_section_what_trees_are_good_and_bad_at.png)

## Your Turn

Add one applicant to the training data and watch how much of the tree survives.

Append a row for someone with a credit score of 610 who was approved, say `(65, 12, 610, 1)`, representing a long-standing customer the manager vouched for. Rerun the tree and compare. The 615 threshold will move or the structure will change, from a single row out of seventeen, which is the instability the table above claims and is far more convincing when you cause it yourself.

Then use the depth limit as a policy instrument rather than a technical setting. Suppose the bank's regulator will only accept criteria that a customer can be told in one sentence. Which `max_depth` does that permit, and what accuracy does the bank give up to comply? The depth-1 tree above answers this: 0.94 instead of 1.00, in exchange for a rule that fits in a sentence. Decide whether you would take that trade, and note that this is a business decision informed by a number rather than a technical one.

Finally, examine the leaf built from a single applicant. Write down two different ways to prevent it: capping depth, or refusing to split a group smaller than some minimum. Implement the second by adding a check at the top of `build`, and confirm that the middle rule disappears. Then say which of the two you would prefer for a lending model and why.
