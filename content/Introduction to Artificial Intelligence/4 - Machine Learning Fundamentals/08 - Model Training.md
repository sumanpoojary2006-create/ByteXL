## Introduction

Two analysts at the same property portal build price estimators in the same week, using the same twelve flats and, as it turns out, the same method.

Sameer reports that his model is accurate to within about half a lakh. Ritu reports that hers is off by nearly six lakh and apologises for it. They compare notes, expecting to find a difference in approach, and find none. Identical features, identical arithmetic, identical data.

The only difference is which three flats each of them happened to hold back for testing.

Neither number is a lie and neither is a measurement. Both analysts did what the workflow told them to do, split the data, train on one part, measure on the other, and both received a figure that says more about their shuffle than about their model. Sameer will present his half-lakh figure to management, and it will be wrong in a way nobody in the room can detect.

Fixing this is what **model training** covers: not the fitting itself, which is arithmetic, but the discipline around it that makes the resulting number mean something.

**Definition:** `Model training` is the process of fitting a model to data together with the procedures that make its measured performance trustworthy, including how the data is divided, how `hyperparameters` are chosen, and how the final estimate is kept honest.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_section_introduction.png)

## One Split Measures Luck

The place to start is by taking Sameer and Ritu's disagreement seriously and measuring how large the effect is.

Reading the code below: `fit_line` and `mae` are from the regression lesson and can be skimmed. The lesson is in `one_split`, six lines that do exactly what both analysts did, and in the single line that runs it two hundred times with two hundred different shuffles.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjzb6" 
 width="100%"
></iframe>

```
The same model and the same data, split 200 different ways

  best split   test MAE   0.52 lakh
  worst split  test MAE   5.74 lakh
  average      test MAE   3.42 lakh
  median       test MAE   3.44 lakh

Where the 200 results fall:
   0 to  2 lakh   21  #####################
   2 to  4 lakh  116  ####################################################################################################################
   4 to  6 lakh   63  ###############################################################
   6 to  8 lakh    0
```

| In the code | What it is | Why it is there |
| --- | --- | --- |
| `random.Random(seed).shuffle(rows)` | The only thing that varies | Every other input is identical across all 200 runs |
| `rows[:9], rows[9:]` | The train-test cut | Three test flats is what makes the spread so wide |
| `one_split(seed) for seed in range(200)` | 200 honest analysts | Turns one score into a distribution you can look at |
| `buckets[min(int(s // 2), 3)] += 1` | A text histogram | Each score falls into a two-lakh bin |

Sameer's 0.52 lakh is not a good result. It is **the single best of two hundred possible shuffles**, and Ritu's 5.74 is the worst. The truth is around 3.4, and neither analyst was in a position to know that from one run.

The histogram is the honest picture. A single split returns one sample from that distribution, and reporting it as though it were the model's accuracy is reporting a draw from a lottery. On twelve flats the spread is extreme because three test rows measure almost nothing, and the same effect operates, more mildly, on datasets of any size.

Two conclusions follow immediately. **A single test score is an estimate with error bars nobody printed.** And a model that looks better than another may simply have been luckier, which is why comparing two models on one split settles nothing.

![Visual explanation of one split measures luck](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_section_one_split_measures_luck.png)

## Cross-Validation

The fix is to stop relying on one division. `k-fold cross-validation` splits the data into k equal parts, then trains k times, each time holding out a different part.

Every example is used for training in most rounds and held out in exactly one. Instead of a single score there are k of them, and the average is a far steadier estimate.

Reading the code below: only `cross_validate` is new, and its whole trick is the two lines that carve `shuffled` into a held-out slice and everything else. The loop runs the same fit-and-measure four times, moving the held-out slice along by one each round.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjzry" 
 width="100%"
></iframe>

```
4-fold cross-validation: every flat is held out exactly once

  fold 1 used as test: MAE  2.68 lakh
  fold 2 used as test: MAE  5.08 lakh
  fold 3 used as test: MAE  3.74 lakh
  fold 4 used as test: MAE  0.52 lakh

  average across folds: 3.01 lakh
  spread between folds: 1.67 lakh
```

| In the code | What it is | Why it is there |
| --- | --- | --- |
| `size = len(shuffled) // folds` | Rows per fold | Three here, so each round holds out three flats |
| `shuffled[f*size:(f+1)*size]` | This round's test rows | The window slides along by one fold each pass |
| `shuffled[:f*size] + shuffled[(f+1)*size:]` | Everything else | The training rows, rebuilt from the two remaining slices |
| `average`, `spread` | Mean and standard deviation of the folds | The two numbers that get reported, not one |

Three lakh, give or take one and a half. That is a claim worth making, and notice it contains two numbers rather than one.

**The spread is as valuable as the average.** A spread of 1.67 on an average of 3.01 says the estimate is rough, which is the correct thing to say about twelve flats and something a single number can never convey. Reporting an average without it invites exactly the false confidence Sameer had.

Notice also that fold 4 scored 0.52, which is Sameer's number appearing as one fold out of four. Cross-validation does not eliminate the lucky split; it puts it in context.

Two practical points. Five or ten folds is the usual choice, trading computation for stability. And cross-validation costs k times as much training, which is trivial here and a genuine consideration on a model that takes a day to fit.

![Visual explanation of cross validation](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_cross_validation.png)

## A Random Split Is Not Always a Fair Split

Shuffling before cutting was introduced as the safe default, and there are two common situations where it is quietly wrong.

**When one class is rare.** Suppose a fraud dataset contains 2 percent fraudulent invoices. A random split can easily produce a test set containing no fraud at all, in which case the test measures nothing about the only thing anyone cares about, or a training set containing very few, in which case the model barely learns the pattern. The repair is a `stratified split`: divide each class separately and take the same proportion from each, so both sets preserve the original balance. For any classification problem with an uneven class balance, stratifying should be the default rather than an optimisation.

**When the data has a time order.** The flats dataset carries no dates, so shuffling is harmless. Add a sale date and it stops being harmless, because a random split trains the model on flats sold in March and tests it on flats sold in January. In deployment the model will only ever face the future, so testing it on the past flatters it: prices drift, and a model that has seen next quarter's market has an advantage no real system gets. The repair is a **time-based split**: train on the earliest data, test on the most recent, exactly as the model will be used.

The principle behind both is one sentence worth remembering. **The split should imitate the situation the model will actually face.** A random shuffle imitates the situation where new examples are drawn from the same pool as old ones, which is true for many problems and false for anything with a time dimension or a rare class worth protecting.

![Visual explanation of a random split is not always a fair split](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_section_a_random_split_is_not_always_a_fair_split.png)

## Parameters and Hyperparameters

Several settings in this unit were chosen with no justification: the number of neighbours in the mail classifier, the maximum depth of the loan tree, the number of clusters for the supermarket. Each is a `hyperparameter`, and the distinction from ordinary parameters is worth stating precisely.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;"></th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Parameter</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Hyperparameter</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Set by</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The training procedure, from the data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">You, before training begins</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Examples</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The slope and intercept of the price line; a tree's thresholds</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The number of neighbours; a tree's maximum depth; the number of clusters</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How to get it right</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Run the training procedure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Try several values and measure</td>
    </tr>
  </tbody>
</table>

Since hyperparameters are chosen by measuring, and measuring requires held-out data, a trap opens up immediately.

![Visual explanation of parameters hyperparameters](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_parameters_hyperparameters.png)

## Three Sets, Not Two

If you try five values of a hyperparameter on the test set and keep whichever scored best, the test set has influenced the model. It is no longer untouched data, and the score it reports is optimistic. You have quietly fitted your choice to the test set.

The standard remedy is three sets rather than two.

- **Training set:** fits the model's parameters.
- **Validation set:** compares hyperparameter choices.
- **Test set:** used once, at the very end, to report performance.

The rule is short and often broken. **The test set is looked at once, after every decision has been made.** If you look at it, change something, and look again, it has become a validation set and you no longer have a test set.

Reading the code below: the model is nearest-neighbours rather than a line, so `knn_predict` averages the prices of the k most similar flats by area. The important line is the three-way split, and the important comparison is the two loops at the bottom, which are identical apart from which set they measure on.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzk243" 
 width="100%"
></iframe>

```
train 6  validation 3  test 3

Choosing k using the validation set only:
  k   validation MAE
---------------------
  1             4.67
  2             7.33
  3             4.44
  4             7.92
  5             9.80

Best k on validation: 3
Test MAE with k=3: 7.44 lakh

If we had cheated and picked k using the test set instead:
  we would have picked k=4 and reported 3.75 lakh
  which is a number no future flat will ever live up to
```

| In the code | Which set it uses | What it represents |
| --- | --- | --- |
| `mae(validation, train, k)` | Validation | The honest way to choose k |
| `min(results, key=results.get)` | Validation | The decision, made before test is opened |
| `mae(test, train, best_k)` | Test, once | The number you are allowed to report |
| `{k: mae(test, train, k) for k in ...}` | Test, five times | The cheat: choosing on the set you report |

The gap between 7.44 and 3.75 is the size of the self-deception, and it is worth reading carefully because it is counter-intuitive in two ways.

The honest procedure chose k of 3 and reported 7.44 lakh. The dishonest one chose k of 4, which the validation set had ranked second-worst, and reported 3.75. **Cheating produced a number roughly twice as flattering, and a worse choice of k**, because it selected whichever value happened to suit three particular flats rather than whichever generalises.

That is the essential point. Tuning on the test set does not merely inflate the reported score; it also picks the wrong hyperparameter, because it optimises for the accident of which rows landed in the test set.

In practice, cross-validation and hyperparameter search are combined: the training portion is cross-validated for each candidate value, the best is selected, and the test set is opened once at the end.

![Visual explanation of three sets, not two](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_section_three_sets_not_two_simple_v2.png)

## Your Turn

Change the shuffle seed in the three-way split from 3 to several other values and record both the chosen k and the final test MAE each time.

You will find the chosen k moves around. That is not a bug in the procedure; it is a demonstration that with six training flats and three validation flats there is not enough data to choose a hyperparameter reliably. Deciding that the honest conclusion is "this dataset cannot support tuning" is a legitimate and often correct finding.

Then implement the proper combination. Replace the single validation set with 4-fold cross-validation over the nine non-test rows, choosing k by average fold score, and open the test set once at the end. Compare the chosen k's stability against what you saw with a single validation set.

Finally, sit with a question the code cannot answer. Suppose you run the full honest procedure, see a disappointing test score, go back and try a different model family, and check the test set again. You have now looked at it twice. Describe precisely what you have lost, and what you would have to do to recover an honest estimate. If your answer involves setting aside data you have never touched, or accepting that your final number is optimistic and saying so, you have understood why this discipline is difficult to maintain in practice rather than difficult to understand.
