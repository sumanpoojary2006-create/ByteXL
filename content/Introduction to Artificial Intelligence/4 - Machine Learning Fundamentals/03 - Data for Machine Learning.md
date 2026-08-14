## Introduction

Harsh joins a property portal in Pune as its first analyst and is told the company wants a price estimator. He is given access to the database and left to it.

He expects the difficulty to be the algorithm. It is not. Within two days he has a working formula and a result so good it worries him: his estimates match the actual sale prices almost exactly. He shows his manager, who asks one question. Which columns did you use?

Harsh lists them, and near the end of the list is `agreed_value`, a field the sales team fills in once a buyer and seller settle. Of course his estimates were nearly perfect. He had been predicting the price using the price.

He removes that column, rebuilds, and the estimates become mediocre, which is the honest starting point he should have had on day one. What Harsh learned in those two days is that a machine learning project is decided long before any algorithm runs, in the unglamorous work of deciding what the table looks like, which columns the model is allowed to see, and which rows it is allowed to learn from.

**Definition:** A `dataset` for machine learning is a table in which each row is an example, the `features` are the input columns the model may use, and the `label` is the output column it is trained to predict, with the rows deliberately divided into a `training set` used to fit the model and a `test set` reserved to measure it.

![Opening scene: Harsh joins a property portal in Pune as its first analyst and is told the company wants a price estimator.](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_introduction_simple_v2.png)

## The Shape of a Dataset

Almost all machine learning data arrives as a table, and the vocabulary maps directly onto it.

- A **row** is one example, sometimes called an instance or a sample. One flat.
- A **column** used as input is a **feature**, sometimes called an attribute or a variable.
- The **column being predicted** is the **label**, sometimes called the target.

Here is the dataset the next few lessons will use: twelve flats, four features, one label.

Reading the code below: mostly printing. The two lines that matter are near the bottom, where `row[:-1]` and `row[-1]` split each row into features and label. That split is the whole of this section.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzkb3a" 
 width="100%"
></iframe>

```
        area |     bedrooms |          age | km_to_centre |   price_lakh
--------------------------------------------------------------------
         550 |            1 |           12 |          8.0 |           32
         620 |            1 |            8 |          6.5 |           38
         700 |            2 |           15 |          9.0 |           41
         780 |            2 |            5 |          4.0 |           55
         850 |            2 |           10 |          7.0 |           52
         900 |            2 |            3 |          3.5 |           63
         980 |            3 |           12 |          6.0 |           60
        1050 |            3 |            7 |          5.0 |           71
        1150 |            3 |            4 |          3.0 |           82
        1250 |            3 |            9 |          4.5 |           80
        1400 |            4 |            6 |          2.5 |           96
        1550 |            4 |            2 |          2.0 |          110

Examples: 12
Feature columns: ['area', 'bedrooms', 'age', 'km_to_centre']
Label column:    price_lakh
First example features: (550, 1, 12, 8.0) -> label: 32
```

| In the code | What it is | Vocabulary |
| --- | --- | --- |
| One tuple in `FLATS` | One flat | A row, an example, an instance |
| `row[:-1]` | The four inputs | The features |
| `row[-1]` | The price | The label, or target |
| `len(FLATS)` | Twelve | The size of the dataset |

Twelve examples is far too few for a real model and exactly right for a lesson, because every number can be checked by hand. Real property datasets run to hundreds of thousands of rows, and nothing about the vocabulary changes.

Note what is absent from these four features. There is no locality name, no floor number, no indication of whether the building has a lift. Every one of those affects price in Pune, and their absence puts a ceiling on how good any model can be. **The features you choose set the limit; the algorithm only determines how close to that limit you get.**

![Visual explanation of dataset anatomy](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_dataset_anatomy.png)

## Kinds of Feature

Not all columns behave alike, and treating them alike is a common early mistake.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Kind</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it holds</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Care needed</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Numeric</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quantities where arithmetic is meaningful</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Area in square feet, age in years</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Wildly different ranges can distort some models</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Categorical</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Labels from a fixed set, with no order</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Locality name, facing direction</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Must not be numbered 1, 2, 3, which invents an order</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Ordinal</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Categories that do have an order</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Condition: poor, fair, good, excellent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Order is real, but the gaps are not equal</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Binary</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two values</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Has a lift, or does not</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Straightforward; encode as 0 and 1</td>
    </tr>
  </tbody>
</table>

The categorical row causes the most damage in practice. Encoding localities as Kothrud equals 1, Baner equals 2, Hadapsar equals 3 tells the model that Baner sits numerically between the other two and that Hadapsar is three times Kothrud, neither of which means anything. The standard repair is one-hot encoding: replace one column with several binary ones, each answering "is it this locality".

![Visual explanation of kinds of feature](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_kinds_of_feature.png)

## Why the Data Must Be Split

Now the discipline that Harsh's near-perfect model violated in spirit, and that every machine learning workflow enforces.

The purpose of a model is to perform on data it has never seen. Measuring it on the very examples it learned from answers a different and much easier question, since a sufficiently flexible model can memorise the training examples exactly and score perfectly while having learned nothing that transfers.

So the rows are divided before training begins.

- The **training set** is used to fit the model. The model sees these features and these labels.
- The **test set** is held back entirely. The model never sees it during training, and it is used once, at the end, to estimate performance on genuinely new data.

Reading the code below: `train_test_split` is four lines, and the order of those lines matters more than anything in them. Shuffle, then cut. The rest of the program prints what ended up where.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzkbez" 
 width="100%"
></iframe>

```
Total examples: 12
Training set:   9
Test set:       3

Held-out test flats the model will never see during training:
  area  550 sqft, 1 bedrooms  ->  32 lakh
  area  620 sqft, 1 bedrooms  ->  38 lakh
  area 1400 sqft, 4 bedrooms  ->  96 lakh

Average price in training set: 68.2 lakh
Average price in test set:     55.3 lakh
```

Two details of that four-line function matter more than they look.

| In the code | What it does | What breaks without it |
| --- | --- | --- |
| `rows[:]` | Copies before shuffling | The caller's data would be reordered as a side effect |
| `.shuffle(shuffled)` **then** `cut` | Shuffle first, cut second | Sorted data would put every expensive flat in one set |
| `random.Random(seed)` | A reproducible shuffle | Results drift between runs for no traceable reason |
| `shuffled[:cut], shuffled[cut:]` | The two halves | Nothing; this is just the split |

The second row is the one that causes real damage. Property data usually arrives sorted, often by date or by price, and slicing the last quarter off a sorted table would test the model on a world it never saw during training.

The last two lines show something worth noticing. The training and test sets have quite different average prices, 68.2 against 55.3 lakh, purely because twelve examples split three ways is a small sample and the shuffle happened to place two of the cheapest flats in the test set. On twelve rows this is unavoidable, and it is a real preview of why a single split is an unreliable measurement on small data.

![Visual explanation of train validation test leakage](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_train_validation_test_leakage.png)

## Data Leakage

Harsh's `agreed_value` column has a name: `data leakage`, information reaching the model that will not be available when it is actually used.

It is worth being precise about why it is fatal rather than merely untidy. A leaked feature makes the model look excellent during development and fail on the day it is deployed, because at prediction time the column either does not exist yet or is empty. The failure is discovered in production, by users, after the project has been declared a success.

Leakage takes several forms, and all of them are easy to miss.

1. **A feature containing the answer**, like Harsh's agreed value, or a `discount_given` column when predicting whether a customer will buy.
2. **A feature recorded after the outcome.** Predicting equipment failure using a `repair_cost` column, which only gets filled in once the machine has already failed.
3. **Test data influencing training.** Computing an average across all rows to fill in missing values, and doing it before the split, quietly carries information about the test rows into training.
4. **Time travel.** Training on data from after the period being predicted, which is easy to do accidentally whenever dates are involved.

The check that catches most of these is a single question, asked of every feature: **at the moment the model must make its prediction, will this value actually be known?** For a flat being listed today, the area is known and the agreed value is not, and asking that question about each column would have saved Harsh two days.

![Visual explanation of data leakage](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_data_leakage.png)

## Your Turn

Design the dataset for predicting whether a student will pass a semester, and be ruthless about the leakage question.

List eight features you would want. Then, for each one, state the exact moment the prediction must be made, and decide whether that feature is known by then. If the prediction is made in week two so that struggling students can be helped, then attendance to date is known and the mid-semester test score is not, and including the latter builds a model that cannot be used for the thing it was built for.

Then classify each surviving feature as numeric, categorical, ordinal, or binary, and for any categorical one, write out what its one-hot encoding would look like.

Finally, think about the split. If your data covers three years of students, describe what could go wrong with a purely random split, given that syllabuses and grading standards change between years. Then propose an alternative split that would give a more honest estimate of how the model will perform on next year's students. If your answer involves training on earlier years and testing on the most recent one, you have arrived at the standard practice for data that has a time dimension, and you will have understood why the random shuffle above is a simplification rather than a universal rule.
