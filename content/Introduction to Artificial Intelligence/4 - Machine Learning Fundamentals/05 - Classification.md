## Introduction

The IT desk at a college in Kochi gets the same complaint every week. Staff say the mail system is either letting junk through or hiding messages they needed, and both complaints arrive from the same people on the same day.

Rohini, who maintains the system, looks at what it currently does. It is a list of banned phrases. A message containing "winner" or "click here" goes to junk. The list has grown to two hundred entries, and it is failing in both directions at once: a genuine circular about a prize-giving ceremony was junked for containing "winner", while a fraud offering a refund passed through untouched because it happened to use none of the two hundred phrases.

Rohini has something better available. Every user has a junk folder, and every message a user has ever dragged out of it, or dragged into it, is a recorded judgment. She has thousands of messages already sorted into the right place by the people who received them.

The question she needs answered for each new message is not a quantity. Nobody wants a message scored 63.4. They want it put in a folder, which is a choice among a fixed set of options. Predicting which category something belongs to is **classification**.

**Definition:** `Classification` is supervised learning where the label is a category from a fixed set rather than a number, and the model learns to assign new examples to one of those categories using features whose relationship to the category is derived from labelled examples.

![Opening scene: The IT desk at a college in Kochi gets the same complaint every week.](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_section_introduction.png)

## Classification Against Regression

The distinction is not cosmetic, and it changes both the model and the measurement.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Regression</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Classification</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Label</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A continuous quantity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One of a fixed set of categories</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Being slightly wrong</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Meaningful; off by 2 lakh beats off by 20</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Meaningless; a message is in the right folder or it is not</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Typical error measure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Average size of the miss, in the label's units</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Proportion of examples put in the right category</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What the model produces</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A number on a scale</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A decision boundary carving the feature space into regions</td>
    </tr>
  </tbody>
</table>

That last row is the useful mental picture. Imagine every message plotted as a point according to its features. A classifier draws boundaries through that space, and everything falling in one region gets one label. Learning means positioning the boundaries.

Two kinds of classification problem are distinguished by how many categories there are.

- **Binary classification** has exactly two: junk or not junk, fraudulent or legitimate, defaulted or repaid.
- **Multi-class classification** has three or more: junk, promotions, or personal.

![Visual explanation of classification vs regression](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_classification_vs_regression.png)

## Classifying by Resemblance

The simplest classifier ignores boundaries entirely and works by resemblance. To label a new message, find the messages most similar to it among those already labelled, and go with whatever most of them are.

This is `k-nearest neighbours`, and its appeal is that there is essentially no training. The examples themselves are the model. The `k` is how many neighbours get a vote.

Rohini reduces each message to three numbers: how many links it contains, how many exclamation marks, and how many words in capitals.

Reading the code below: there is no training step, because this method has none. `distance` measures how alike two messages are, and `classify` sorts the training set by that distance and takes a vote among the closest few. Three lines do everything.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzk7u5" 
 width="100%"
></iframe>

```
obvious junk (links=10, '!'=6, CAPS=13)
   3 nearest training emails: ['spam', 'spam', 'spam']
   votes {'spam': 3}  ->  spam

note from a friend (links=1, '!'=0, CAPS=1)
   3 nearest training emails: ['personal', 'personal', 'personal']
   votes {'not spam': 3}  ->  not spam

a shop newsletter (links=5, '!'=2, CAPS=4)
   3 nearest training emails: ['promotions', 'promotions', 'promotions']
   votes {'not spam': 3}  ->  not spam

```

Three sensible verdicts from fourteen examples and no training at all.

| In the code | What it does | Note |
| --- | --- | --- |
| `distance(a, b)` | Straight-line distance in three dimensions | Small means alike, and this is the only notion of "similar" |
| `sorted(examples, key=...)` | Rank all fourteen by closeness | This is the whole "training", done fresh every prediction |
| `scored[:k]` | Keep the k nearest | Everything further away is discarded outright |
| `max(votes, key=votes.get)` | The majority label among them | Ties broken by whichever was counted first |

The `distance` function carries the entire content of the method: it trusts that messages with similar numbers deserve similar labels. That is an assumption rather than a fact, and it is the thing that fails when a feature is measured on a different scale.

Notice also that `sorted(...)` runs inside `classify`, so the work happens at prediction time rather than in advance. There is nothing to train, and equally nothing to store except the data itself.

Notice the third case. The shop newsletter's nearest neighbours are all promotions, and because promotions counts as "not spam", the newsletter stays in the inbox. The banned-phrase list would very likely have junked it.

![Visual explanation of knn classification](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_knn_classification_context_v4.png)

## More Than Two Categories

Rohini actually wants three folders, not two, and the pleasant surprise is that nothing about the method changes. The votes are simply counted over three labels instead of two.

Reading the code below: compare `classify` against the previous version. The only edit is that `is_spam(row[3])` becomes `row[3]`, so the real folder name is counted instead of being collapsed to two options. Everything else is identical.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzk89a" 
 width="100%"
></iframe>

```
Three folders instead of two:

obvious junk           -> spam         votes {'spam': 3}
note from a friend     -> personal     votes {'personal': 3}
a shop newsletter      -> promotions   votes {'promotions': 3}
hard to call           -> promotions   votes {'promotions': 2, 'spam': 1}
```

The fourth message is the honest one. Three links, three exclamation marks, six capitalised words sits between the promotions cluster and the spam cluster, and the vote splits two to one.

**That split vote is information, and throwing it away is a design decision.** The classifier reports "promotions" and says nothing about having been unsure, and a system that treated a two-to-one vote identically to a three-to-nil vote would be discarding exactly the signal a human reviewer would want. Most real classifiers therefore output a confidence alongside the label, and a well-built mail system would file the confident cases automatically and surface the marginal ones.

Note also that some classifiers handle multiple categories naturally, as this one does, while others are built for two and must be extended by training several binary classifiers and combining them. Knowing which kind you have matters when the number of categories grows.

![Visual explanation of more than two categories](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_section_more_than_two_categories.png)

## Choosing k

The one setting in this method is how many neighbours vote, and it matters more than it looks.

To measure the effect honestly on fourteen examples, each message is classified using the other thirteen as training data, one at a time. This is a small version of a technique the training lesson develops properly.

Reading the code below: the new part is `leave_one_out_accuracy`. The slicing trick `EMAILS[:i] + EMAILS[i+1:]` builds a training set with example `i` removed, so each message is classified by the other thirteen and never by itself.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzk8su" 
 width="100%"
></iframe>

```
Every email classified using the other 13 as training data

  k   accuracy
---------------
  1       1.00
  3       1.00
  5       1.00
  7       0.64
  9       0.71
 13       0.00
```

The last row is worth staring at. **With k equal to 13, accuracy is zero, not low.** Every remaining message votes, so every prediction is simply whichever category is most common overall, and since each message is excluded from its own vote, the majority always tips away from its true category. The classifier has stopped looking at the features entirely.

That is the extreme, and the trend before it is the general rule.

- **Small k** follows the data closely and is sensitive to noise. With k equal to 1, a single mislabelled message creates a small wrong region around itself.
- **Large k** smooths over genuine detail and drifts towards always predicting the most common category.

There is no formula for the right value. It is chosen by measuring, which is what the training lesson is about.

![Visual explanation of choosing k](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_section_choosing_k.png)

## What This Method Costs

k-nearest neighbours is a good teaching classifier and a limited production one, and the reasons are worth knowing because they motivate everything that follows.

1. **It has no training and therefore no summary.** The whole dataset must be kept and searched for every prediction, so a million labelled messages mean a million distance calculations per email.
2. **It is at the mercy of feature scale.** Distance treats all three counts as equally important. Had one feature been measured in bytes and another in counts, the byte-sized one would dominate every distance and the others would be ignored.
3. **It cannot explain itself usefully.** The reason is "these three other messages were similar", which is not a policy anyone can audit or appeal.
4. **It degrades as features multiply.** With many features, all points become roughly equidistant from one another and "nearest" stops meaning much.

The third limitation is the one that hurts in regulated settings. Rohini can live with it for a mail folder. A bank rejecting a loan cannot tell the applicant that three other people who looked similar also defaulted.

![Visual explanation of what this method costs](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_section_what_this_method_costs_simple_v2.png)

## Your Turn

Change what the classifier sees and watch its behaviour change with it.

Add a fourth feature to every email: the number of times the word "free" appears, choosing values yourself that fit each category. Rerun the three-folder program and check whether the "hard to call" message moves. Then multiply just that new feature by 100 in every row, as though it had been recorded in a different unit, and run it again. The predictions will change even though nothing about the emails did, which demonstrates the scale problem concretely rather than as a warning.

Then confront the boundary. Construct an email whose features place it exactly between two categories, and find a value of k that classifies it one way and another value that classifies it the other. Once you can do that on demand, you understand that k is not a detail.

Finally, reason about a case the code cannot show you. Suppose 98 of every 100 messages arriving at the college are junk. A classifier that ignores every feature and labels everything junk would be right 98 percent of the time. Decide whether you would deploy it, and if not, say precisely what is wrong with 98 percent accuracy as a measure. Getting that answer clear in your head now will make the evaluation lesson considerably easier.
