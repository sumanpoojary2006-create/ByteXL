## Introduction

A district health programme pilots a screening model for a condition affecting roughly two people in a hundred. The vendor's report leads with a single figure: 98 percent accuracy.

Dr Meera, who runs the programme, asks one question before signing. How many of the people who actually have the condition does it find?

The answer is none. The model has learned that saying "healthy" to everybody is correct 98 times out of 100, because 98 percent of the people screened are in fact healthy. It has achieved an excellent score by never doing the one thing it was built for.

Nobody cheated. The accuracy figure is arithmetically correct, and it is worse than useless because it hides the only failure that matters. What Dr Meera needs is not a better model in the first instance. It is a measurement that could have told her, from the report alone, that this model finds nobody.

Choosing measurements that expose failures rather than conceal them is **model evaluation**.

**Definition:** `Model evaluation` is the practice of measuring a model's performance with quantities chosen to reveal the specific ways it can fail, rather than with a single summary figure that can be high while the model is useless.

![Opening scene: A district health programme pilots a screening model for a condition affecting roughly two people in a hundred.](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_section_introduction.png)

## Accuracy and Its Blind Spot

`Accuracy` is the proportion of predictions that are correct. It is the natural first measure and it is unreliable whenever the classes are unbalanced.

The clearest way to see this is to compare a model that does nothing against a model that does something.

Reading the code below: no model is trained here. `ACTUAL` and the two prediction lists are written by hand so the counts are exactly as described in the text, and `confusion` does the only real work, four lines that count the four ways a prediction can turn out.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzka3x" 
 width="100%"
></iframe>

```
Model A: never flags anyone
   accuracy 0.980
                    predicted ill   predicted healthy
   actually ill             0                  20
   actually well            0                 980

Model B: a real classifier
   accuracy 0.936
                    predicted ill   predicted healthy
   actually ill            16                   4
   actually well           60                 920
```

| In the code | What it is | Note |
| --- | --- | --- |
| `ACTUAL = [1]*20 + [0]*980` | The truth | Twenty ill people in a thousand, the 2 percent rate |
| `model_a = [0] * 1000` | Says healthy to everybody | The degenerate model the vendor shipped |
| `model_b` | 16 found, 4 missed, 60 false alarms | Written to match the counts, not learned |
| `tp, fn, fp, tn` | The confusion matrix | The only four numbers that carry information |
| `(tp + tn) / len(ACTUAL)` | Accuracy | Correct predictions over all predictions |

**The useless model scores higher.** 0.980 against 0.936. Ranking these two by accuracy would lead the programme to deploy the one that finds nobody.

The four-cell table underneath is the `confusion matrix`, and it is the thing to insist on whenever someone quotes a single figure. Its four cells have standard names.

- **True positives:** ill and flagged. Model B has 16.
- **False negatives:** ill and missed. Model B has 4. These are the people the programme exists to find.
- **False positives:** healthy and flagged. Model B has 60. Each one means an unnecessary follow-up.
- **True negatives:** healthy and cleared. Model B has 920.

Model A's matrix makes its emptiness visible at a glance: the entire first column is zero. No summary number was needed, and no summary number would have shown it.

![Visual explanation of confusion matrix](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_confusion_matrix.png)

## Precision and Recall

Two measures pull the confusion matrix apart along the line that matters, and each answers a different practical question.

- **Recall** asks: of everyone who was ill, what fraction did we find? It is true positives divided by all actually ill. This is the question Dr Meera asked.
- **Precision** asks: of everyone we flagged, what fraction really was ill? It is true positives divided by all flagged. This is the question the follow-up clinic asks, because every false positive costs them an appointment.

Reading the code below: the data and `confusion` are unchanged from the previous block. The new function is `scores`, and its four lines are the four definitions written as arithmetic. Note which counts appear in each denominator, because that is the whole difference between the measures.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzkaep" 
 width="100%"
></iframe>

```
                       model  accuracy  precision  recall     F1
----------------------------------------------------------------
       A: never flags anyone     0.980      0.000   0.000  0.000
        B: a real classifier     0.936      0.211   0.800  0.333

Reading model B in plain words:
  Of 20 people who were ill, it found 16 and missed 4.
  Of 76 people it flagged, 16 were ill and 60 were not.
```

| In the code | Denominator | Reads as |
| --- | --- | --- |
| `tp / (tp + fp)` | Everyone flagged | Precision: how many of our alarms were real |
| `tp / (tp + fn)` | Everyone actually ill | Recall: how many real cases we caught |
| `(tp + tn) / len(actual)` | Everybody screened | Accuracy: why the rare class disappears |
| `2 * p * r / (p + r)` | Neither, it combines the two | F1: one number, and it hides which side is weak |
| `if (tp + fp) else 0.0` | Guard | Model A flags nobody, so the denominator is zero |

The ranking inverts, which is the point. Model A's recall is zero, and zero recall is the single number that would have stopped the contract.

Model B's figures deserve reading rather than glancing at. Recall of 0.800 means it finds four ill people in five. Precision of 0.211 means only one flagged person in five is actually ill. Both are true at once, and whether that is a good model depends entirely on what happens next: if the follow-up is a cheap confirmatory test, catching 80 percent while sending five people for every one case is an excellent trade, and if the follow-up is invasive and frightening, it is not.

The last two printed lines are worth adopting as a habit. **Convert every metric into a sentence with counts in it** before presenting it to anyone who will make a decision. "Precision 0.211" persuades nobody and hides everything; "of 76 people we flagged, 60 were not ill" starts the right conversation.

`F1` is the harmonic mean of precision and recall, useful as a single figure when you need one, and it is a compromise rather than a truth. Model B's F1 of 0.333 sits between its 0.211 and 0.800, and reporting only the F1 conceals which of the two is weak.

![Visual explanation of precision and recall](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_section_precision_and_recall_simple_v2.png)

## The Threshold Is a Choice

Most classifiers do not really output a category. They output a score, and a threshold converts the score into a decision. Moving that threshold moves precision and recall in opposite directions, and it is a policy decision rather than a technical one.

Reading the code below: the scores are simulated rather than learned, drawn so that ill patients tend to score around 0.70 and healthy ones around 0.30 with plenty of overlap. Nothing about the patients changes after that line. Only the number `threshold` moves, and `evaluate` recounts the same thousand scores against it.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzkarc" 
 width="100%"
></iframe>

```
One model, one set of scores, different thresholds for calling it positive

 threshold  found  missed  false alarms  precision  recall
------------------------------------------------------------
      0.30     20       0           514      0.037   1.000
      0.40     20       0           251      0.074   1.000
      0.50     17       3            86      0.165   0.850
      0.60     15       5            25      0.375   0.750
      0.70     10      10             3      0.769   0.500
      0.80      3      17             0      1.000   0.150
```

| In the code | What it is | Note |
| --- | --- | --- |
| `rng.gauss(0.70, 0.15)` | Scores for ill patients | Centred high, but spread wide enough to overlap |
| `rng.gauss(0.30, 0.15)` | Scores for healthy patients | The overlap is what makes the threshold matter |
| `min(1.0, max(0.0, ...))` | Clamping | Keeps every score inside 0 to 1 |
| `score >= threshold` | The decision rule | The entire classifier is this one comparison |
| `for threshold in (0.30, ..., 0.80)` | The sweep | Same scores, six different policies |

The table has six rows because six thresholds were chosen. Drag the threshold below and every value between them is available too, along with a picture of which people fall on each side of the line.

<iframe
 frameBorder="0"
 height="520px" data-visualizer="threshold_explorer.html" src="data:text/html;base64,PCFkb2N0eXBlIGh0bWw+CjxodG1sIGxhbmc9ImVuIj4KPGhlYWQ+CjxtZXRhIGNoYXJzZXQ9InV0Zi04Ij4KPG1ldGEgbmFtZT0idmlld3BvcnQiIGNvbnRlbnQ9IndpZHRoPWRldmljZS13aWR0aCwgaW5pdGlhbC1zY2FsZT0xIj4KPHRpdGxlPlRocmVzaG9sZCBFeHBsb3JlcjwvdGl0bGU+CjxzdHlsZT4KICA6cm9vdCB7CiAgICAtLWJnOiAjMTIxNjFkOwogICAgLS1wYW5lbDogIzFhMjAyOTsKICAgIC0tbGluZTogIzJjMzU0MjsKICAgIC0tdGV4dDogI2U2ZWJmMjsKICAgIC0tbXV0ZWQ6ICM4Yjk3YTg7CiAgICAtLWlsbDogI2YyOTk0YTsKICAgIC0td2VsbDogIzViOGRlZjsKICAgIC0tZGltOiAjM2E0NDUzOwogICAgLS1nb29kOiAjNTZjMjg4OwogICAgLS1iYWQ6ICNlMjY2NmI7CiAgfQogICogeyBib3gtc2l6aW5nOiBib3JkZXItYm94OyB9CiAgaHRtbCwgYm9keSB7CiAgICBtYXJnaW46IDA7CiAgICBiYWNrZ3JvdW5kOiB2YXIoLS1iZyk7CiAgICBjb2xvcjogdmFyKC0tdGV4dCk7CiAgICBmb250LWZhbWlseTogSW50ZXIsIHVpLXNhbnMtc2VyaWYsIHN5c3RlbS11aSwgLWFwcGxlLXN5c3RlbSwgIlNlZ29lIFVJIiwgc2Fucy1zZXJpZjsKICB9CiAgLndyYXAgeyBwYWRkaW5nOiAxOHB4IDIwcHggMjBweDsgbWF4LXdpZHRoOiA5MDBweDsgbWFyZ2luOiAwIGF1dG87IH0KICAudGl0bGUgewogICAgZm9udC1zaXplOiAxMXB4OwogICAgbGV0dGVyLXNwYWNpbmc6IDAuMThlbTsKICAgIHRleHQtdHJhbnNmb3JtOiB1cHBlcmNhc2U7CiAgICBjb2xvcjogdmFyKC0tbXV0ZWQpOwogICAgdGV4dC1hbGlnbjogY2VudGVyOwogIH0KICAuZm9ybXVsYSB7CiAgICB0ZXh0LWFsaWduOiBjZW50ZXI7CiAgICBmb250LWZhbWlseTogdWktbW9ub3NwYWNlLCBTRk1vbm8tUmVndWxhciwgTWVubG8sIG1vbm9zcGFjZTsKICAgIGZvbnQtc2l6ZTogMTVweDsKICAgIG1hcmdpbjogNnB4IDAgMTRweDsKICAgIGNvbG9yOiB2YXIoLS10ZXh0KTsKICAgIGRpc3BsYXk6IGZsZXg7CiAgICBmbGV4LXdyYXA6IHdyYXA7CiAgICBqdXN0aWZ5LWNvbnRlbnQ6IGNlbnRlcjsKICAgIGdhcDogNHB4IDI0cHg7CiAgfQogIC5mb3JtdWxhIHNwYW4geyB3aGl0ZS1zcGFjZTogbm93cmFwOyB9CiAgQG1lZGlhIChtYXgtd2lkdGg6IDcwMHB4KSB7CiAgICAuZm9ybXVsYSB7IGZvbnQtc2l6ZTogMTNweDsgfQogICAgLndyYXAgeyBwYWRkaW5nOiAxNHB4IDE0cHggMTZweDsgfQogIH0KICAucmVhZG91dCB7CiAgICBiYWNrZ3JvdW5kOiAjMGQxMTE3OwogICAgYm9yZGVyOiAxcHggc29saWQgdmFyKC0tbGluZSk7CiAgICBib3JkZXItcmFkaXVzOiA2cHg7CiAgICBwYWRkaW5nOiA5cHggMTJweDsKICAgIGZvbnQtZmFtaWx5OiB1aS1tb25vc3BhY2UsIFNGTW9uby1SZWd1bGFyLCBNZW5sbywgbW9ub3NwYWNlOwogICAgZm9udC1zaXplOiAxM3B4OwogICAgdGV4dC1hbGlnbjogY2VudGVyOwogICAgY29sb3I6IHZhcigtLXRleHQpOwogIH0KICAudmVyZGljdCB7CiAgICB0ZXh0LWFsaWduOiBjZW50ZXI7CiAgICBmb250LXNpemU6IDEzcHg7CiAgICBsaW5lLWhlaWdodDogMS41OwogICAgbWFyZ2luOiAxMHB4IDAgMTRweDsKICAgIG1pbi1oZWlnaHQ6IDM4cHg7CiAgICBjb2xvcjogdmFyKC0taWxsKTsKICB9CiAgLmNvbnRyb2wgeyBkaXNwbGF5OiBmbGV4OyBhbGlnbi1pdGVtczogY2VudGVyOyBnYXA6IDEycHg7IG1hcmdpbi1ib3R0b206IDE2cHg7IH0KICAuY29udHJvbCBsYWJlbCB7CiAgICBmb250LWZhbWlseTogdWktbW9ub3NwYWNlLCBTRk1vbm8tUmVndWxhciwgTWVubG8sIG1vbm9zcGFjZTsKICAgIGZvbnQtc2l6ZTogMTNweDsKICAgIGNvbG9yOiB2YXIoLS1tdXRlZCk7CiAgICB3aGl0ZS1zcGFjZTogbm93cmFwOwogIH0KICAuY29udHJvbCBvdXRwdXQgewogICAgZm9udC1mYW1pbHk6IHVpLW1vbm9zcGFjZSwgU0ZNb25vLVJlZ3VsYXIsIE1lbmxvLCBtb25vc3BhY2U7CiAgICBmb250LXNpemU6IDEzcHg7CiAgICB3aWR0aDogMzhweDsKICAgIHRleHQtYWxpZ246IHJpZ2h0OwogICAgY29sb3I6IHZhcigtLWlsbCk7CiAgfQogIGlucHV0W3R5cGU9cmFuZ2VdIHsKICAgIGZsZXg6IDE7CiAgICAtd2Via2l0LWFwcGVhcmFuY2U6IG5vbmU7CiAgICBhcHBlYXJhbmNlOiBub25lOwogICAgaGVpZ2h0OiA0cHg7CiAgICBib3JkZXItcmFkaXVzOiAycHg7CiAgICBiYWNrZ3JvdW5kOiB2YXIoLS1kaW0pOwogICAgb3V0bGluZTogbm9uZTsKICB9CiAgaW5wdXRbdHlwZT1yYW5nZV06Oi13ZWJraXQtc2xpZGVyLXRodW1iIHsKICAgIC13ZWJraXQtYXBwZWFyYW5jZTogbm9uZTsKICAgIGFwcGVhcmFuY2U6IG5vbmU7CiAgICB3aWR0aDogMTVweDsgaGVpZ2h0OiAxNXB4OwogICAgYm9yZGVyLXJhZGl1czogNTAlOwogICAgYmFja2dyb3VuZDogdmFyKC0taWxsKTsKICAgIGN1cnNvcjogcG9pbnRlcjsKICB9CiAgaW5wdXRbdHlwZT1yYW5nZV06Oi1tb3otcmFuZ2UtdGh1bWIgewogICAgd2lkdGg6IDE1cHg7IGhlaWdodDogMTVweDsKICAgIGJvcmRlcjogMDsKICAgIGJvcmRlci1yYWRpdXM6IDUwJTsKICAgIGJhY2tncm91bmQ6IHZhcigtLWlsbCk7CiAgICBjdXJzb3I6IHBvaW50ZXI7CiAgfQogIC5ncmlkIHsgZGlzcGxheTogZ3JpZDsgZ3JpZC10ZW1wbGF0ZS1jb2x1bW5zOiAxZnIgMjUwcHg7IGdhcDogMThweDsgYWxpZ24taXRlbXM6IHN0YXJ0OyB9CiAgQG1lZGlhIChtYXgtd2lkdGg6IDcwMHB4KSB7IC5ncmlkIHsgZ3JpZC10ZW1wbGF0ZS1jb2x1bW5zOiAxZnI7IH0gfQogIHN2ZyB7IHdpZHRoOiAxMDAlOyBkaXNwbGF5OiBibG9jazsgfQogIHRhYmxlIHsgd2lkdGg6IDEwMCU7IGJvcmRlci1jb2xsYXBzZTogY29sbGFwc2U7IGZvbnQtc2l6ZTogMTJweDsgfQogIHRoLCB0ZCB7IHBhZGRpbmc6IDVweCA3cHg7IHRleHQtYWxpZ246IHJpZ2h0OyBib3JkZXItYm90dG9tOiAxcHggc29saWQgdmFyKC0tbGluZSk7IH0KICB0aCB7IGNvbG9yOiB2YXIoLS1tdXRlZCk7IGZvbnQtd2VpZ2h0OiA1MDA7IHRleHQtYWxpZ246IHJpZ2h0OyB9CiAgdGQ6Zmlyc3QtY2hpbGQsIHRoOmZpcnN0LWNoaWxkIHsgdGV4dC1hbGlnbjogbGVmdDsgfQogIC5udW0gewogICAgZm9udC1mYW1pbHk6IHVpLW1vbm9zcGFjZSwgU0ZNb25vLVJlZ3VsYXIsIE1lbmxvLCBtb25vc3BhY2U7CiAgICBmb250LXZhcmlhbnQtbnVtZXJpYzogdGFidWxhci1udW1zOwogIH0KICAuYmFyLXRyYWNrIHsgaGVpZ2h0OiA2cHg7IGJhY2tncm91bmQ6IHZhcigtLWRpbSk7IGJvcmRlci1yYWRpdXM6IDNweDsgb3ZlcmZsb3c6IGhpZGRlbjsgbWFyZ2luLXRvcDogM3B4OyB9CiAgLmJhci1maWxsIHsgaGVpZ2h0OiAxMDAlOyBib3JkZXItcmFkaXVzOiAzcHg7IH0KICAubWV0cmljIHsgbWFyZ2luLWJvdHRvbTogMTJweDsgfQogIC5tZXRyaWMtaGVhZCB7IGRpc3BsYXk6IGZsZXg7IGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2VlbjsgZm9udC1zaXplOiAxMnB4OyBjb2xvcjogdmFyKC0tbXV0ZWQpOyB9CiAgLm1ldHJpYy1oZWFkIGIgeyBjb2xvcjogdmFyKC0tdGV4dCk7IGZvbnQtZmFtaWx5OiB1aS1tb25vc3BhY2UsIE1lbmxvLCBtb25vc3BhY2U7IGZvbnQtd2VpZ2h0OiA1MDA7IH0KICAubm90ZSB7IGZvbnQtc2l6ZTogMTFweDsgY29sb3I6IHZhcigtLW11dGVkKTsgbGluZS1oZWlnaHQ6IDEuNTsgbWFyZ2luLXRvcDogMTBweDsgfQo8L3N0eWxlPgo8L2hlYWQ+Cjxib2R5Pgo8ZGl2IGNsYXNzPSJ3cmFwIj4KCiAgPGRpdiBjbGFzcz0idGl0bGUiPlRocmVzaG9sZCBFeHBsb3JlcjwvZGl2PgogIDxkaXYgY2xhc3M9ImZvcm11bGEiPgogICAgPHNwYW4+cHJlY2lzaW9uID0gVFAgLyAoVFAgKyBGUCk8L3NwYW4+CiAgICA8c3Bhbj5yZWNhbGwgPSBUUCAvIChUUCArIEZOKTwvc3Bhbj4KICA8L2Rpdj4KCiAgPGRpdiBjbGFzcz0icmVhZG91dCIgaWQ9InJlYWRvdXQiPjwvZGl2PgogIDxkaXYgY2xhc3M9InZlcmRpY3QiIGlkPSJ2ZXJkaWN0Ij48L2Rpdj4KCiAgPGRpdiBjbGFzcz0iY29udHJvbCI+CiAgICA8bGFiZWwgZm9yPSJ0aHIiPnRocmVzaG9sZDwvbGFiZWw+CiAgICA8aW5wdXQgdHlwZT0icmFuZ2UiIGlkPSJ0aHIiIG1pbj0iMCIgbWF4PSIxIiBzdGVwPSIwLjAxIiB2YWx1ZT0iMC41Ij4KICAgIDxvdXRwdXQgaWQ9InRock91dCI+MC41MDwvb3V0cHV0PgogIDwvZGl2PgoKICA8ZGl2IGNsYXNzPSJncmlkIj4KICAgIDxkaXY+CiAgICAgIDxzdmcgaWQ9ImNoYXJ0IiB2aWV3Qm94PSIwIDAgNTYwIDI1MCIgcm9sZT0iaW1nIiBhcmlhLWxhYmVsPSJTY29yZSBkaXN0cmlidXRpb25zIHdpdGggdGhyZXNob2xkIGxpbmUiPjwvc3ZnPgogICAgPC9kaXY+CgogICAgPGRpdj4KICAgICAgPGRpdiBjbGFzcz0ibWV0cmljIj4KICAgICAgICA8ZGl2IGNsYXNzPSJtZXRyaWMtaGVhZCI+PHNwYW4+cmVjYWxsPC9zcGFuPjxiIGlkPSJyZWNhbGxWYWwiPjwvYj48L2Rpdj4KICAgICAgICA8ZGl2IGNsYXNzPSJiYXItdHJhY2siPjxkaXYgY2xhc3M9ImJhci1maWxsIiBpZD0icmVjYWxsQmFyIiBzdHlsZT0iYmFja2dyb3VuZDp2YXIoLS1nb29kKSI+PC9kaXY+PC9kaXY+CiAgICAgIDwvZGl2PgogICAgICA8ZGl2IGNsYXNzPSJtZXRyaWMiPgogICAgICAgIDxkaXYgY2xhc3M9Im1ldHJpYy1oZWFkIj48c3Bhbj5wcmVjaXNpb248L3NwYW4+PGIgaWQ9InByZWNWYWwiPjwvYj48L2Rpdj4KICAgICAgICA8ZGl2IGNsYXNzPSJiYXItdHJhY2siPjxkaXYgY2xhc3M9ImJhci1maWxsIiBpZD0icHJlY0JhciIgc3R5bGU9ImJhY2tncm91bmQ6dmFyKC0tYmFkKSI+PC9kaXY+PC9kaXY+CiAgICAgIDwvZGl2PgoKICAgICAgPHRhYmxlPgogICAgICAgIDx0cj48dGg+PC90aD48dGg+ZmxhZ2dlZDwvdGg+PHRoPmNsZWFyZWQ8L3RoPjwvdHI+CiAgICAgICAgPHRyPjx0ZD5pbGw8L3RkPjx0ZCBjbGFzcz0ibnVtIiBpZD0idHAiPjwvdGQ+PHRkIGNsYXNzPSJudW0iIGlkPSJmbiI+PC90ZD48L3RyPgogICAgICAgIDx0cj48dGQ+d2VsbDwvdGQ+PHRkIGNsYXNzPSJudW0iIGlkPSJmcCI+PC90ZD48dGQgY2xhc3M9Im51bSIgaWQ9InRuIj48L3RkPjwvdHI+CiAgICAgIDwvdGFibGU+CgogICAgICA8ZGl2IGNsYXNzPSJub3RlIj4KICAgICAgICAxLDAwMCBwZW9wbGUgc2NyZWVuZWQsIDIwIG9mIHdob20gaGF2ZSB0aGUgY29uZGl0aW9uLgogICAgICAgIFRoZSB0d28gcm93cyBvZiB0aGUgY2hhcnQgdXNlIGRpZmZlcmVudCB2ZXJ0aWNhbCBzY2FsZXMsIGJlY2F1c2UKICAgICAgICA5ODAgaGVhbHRoeSBwZW9wbGUgd291bGQgb3RoZXJ3aXNlIGZsYXR0ZW4gdGhlIDIwIGlsbCBvbmVzIHRvIG5vdGhpbmcuCiAgICAgIDwvZGl2PgogICAgPC9kaXY+CiAgPC9kaXY+Cgo8L2Rpdj4KCjxzY3JpcHQ+Ci8vIFNjb3JlcyBhcyBnZW5lcmF0ZWQgaW4gdGhlIGxlc3NvbjogcmFuZG9tLlJhbmRvbSg3KSwgaWxsIH4gZ2F1c3MoMC43MCwgMC4xNSksCi8vIGhlYWx0aHkgfiBnYXVzcygwLjMwLCAwLjE1KSwgY2xhbXBlZCB0byAwLi4xLiBGaXhlZCBoZXJlIHNvIHRoZSB3aWRnZXQgYW5kCi8vIHRoZSBsZXNzb24ncyBwcmludGVkIHRhYmxlIGFncmVlIGV4YWN0bHkgYXQgZXZlcnkgdGhyZXNob2xkLgpjb25zdCBJTEwgPSBbMC40Mzg0MiwwLjQ0NjMsMC40NTAwOSwwLjU2MDUsMC41NjY1NiwwLjYyOTc3LDAuNjUyNzQsMC42NjE2MiwwLjY2NjA5LDAuNjY4LDAuNzI3OCwwLjczNzM0LDAuNzU5MjIsMC43NjM2MiwwLjc3NDgyLDAuNzc1OTYsMC43NzY3MSwwLjgyODI5LDAuODU1NTMsMC44NjY3OV07CmNvbnN0IFdFTEwgPSBbMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMC4wMDIyNywwLjAwMzQ3LDAuMDAzOTIsMC4wMDQyLDAuMDA1NTgsMC4wMDgzNywwLjAwODY4LDAuMDA5MzgsMC4wMTUwMSwwLjAxNTM5LDAuMDE1NTgsMC4wMTYxMSwwLjAxODYsMC4wMTk4MywwLjAxOTk0LDAuMDIxOTEsMC4wMjYxLDAuMDI2MTgsMC4wMjcwNywwLjAyODMyLDAuMDMzNjEsMC4wMzU2OSwwLjAzNjI4LDAuMDM3NSwwLjAzNzYzLDAuMDM5OTMsMC4wNDEyOSwwLjA0MTc2LDAuMDQ0NzksMC4wNDU2MSwwLjA1MzA3LDAuMDUzMzQsMC4wNTY4NCwwLjA2MDQxLDAuMDYxOTYsMC4wNjQ3NSwwLjA2NDc3LDAuMDY1MzUsMC4wNjU0MSwwLjA2NzYsMC4wNjc3OCwwLjA2ODI3LDAuMDcwMjMsMC4wNzA5LDAuMDczNTcsMC4wNzQyMiwwLjA3NDM5LDAuMDc1MTUsMC4wNzUyOCwwLjA3NjE4LDAuMDc2NTQsMC4wNzk0OCwwLjA4MDMsMC4wODA0MSwwLjA4MTM0LDAuMDgyODcsMC4wODQzLDAuMDg3NDgsMC4wODg2MywwLjA4OTU3LDAuMDg5NjQsMC4wOTEzNCwwLjA5MywwLjA5MzM3LDAuMDk0NTksMC4wOTYwNiwwLjA5NjIyLDAuMDk2ODQsMC4wOTgyNSwwLjEwMzIyLDAuMTAzMzIsMC4xMDM1MywwLjEwMzk3LDAuMTA1MTIsMC4xMDc0MiwwLjEwOTc1LDAuMTEwMjgsMC4xMTEwNSwwLjExMTI0LDAuMTE0MjYsMC4xMTQzNSwwLjExNDQ1LDAuMTE1MjEsMC4xMTY4MywwLjExNzcsMC4xMTg1NiwwLjEyMDg3LDAuMTIzMDYsMC4xMjMxNiwwLjEyNDUsMC4xMjQ3MiwwLjEyNDkzLDAuMTI2MTksMC4xMjcwNiwwLjEyNzk3LDAuMTI4MjgsMC4xMjg5NSwwLjEzMDUsMC4xMzE0MSwwLjEzMjAzLDAuMTMzMjIsMC4xMzY1NiwwLjEzNjc3LDAuMTM3MzksMC4xMzc1LDAuMTM3NTcsMC4xMzgyOCwwLjEzODUxLDAuMTQwMjQsMC4xNDA5OCwwLjE0MTczLDAuMTQxODcsMC4xNDE5MiwwLjE0MzMsMC4xNDQwNywwLjE0NTIyLDAuMTQ1OTIsMC4xNDU5NiwwLjE0NiwwLjE0NjMsMC4xNDY1OCwwLjE0Njk4LDAuMTQ3NDIsMC4xNDc1OSwwLjE0Nzc5LDAuMTQ3OCwwLjE0OTk3LDAuMTUyOCwwLjE1MzM4LDAuMTUzODcsMC4xNTM5LDAuMTU0ODYsMC4xNTUxNCwwLjE1NTUzLDAuMTU2NDEsMC4xNTY0NiwwLjE1Njk0LDAuMTU5MzQsMC4xNTk0MiwwLjE2MDQzLDAuMTYwODYsMC4xNjQxMywwLjE2NDQ0LDAuMTY0NjUsMC4xNjY0NywwLjE2NzI0LDAuMTY3NjUsMC4xNjc2OCwwLjE2NzkzLDAuMTY4MjksMC4xNjg1OSwwLjE2ODc0LDAuMTY5MTksMC4xNzIwNSwwLjE3MjMxLDAuMTczNzYsMC4xNzQzMiwwLjE3NjA5LDAuMTc3NDEsMC4xNzc2NCwwLjE3NzksMC4xNzg4MSwwLjE3ODg1LDAuMTgxNDgsMC4xODE4MSwwLjE4MTk0LDAuMTgyNDgsMC4xODQxMiwwLjE4NDM2LDAuMTg1NSwwLjE4NjA0LDAuMTg2MzYsMC4xODcyOCwwLjE4Nzc4LDAuMTg4NCwwLjE4ODk0LDAuMTg5MDMsMC4xODkwNywwLjE4OTU2LDAuMTkwMzgsMC4xOTA4NywwLjE5MTI5LDAuMTkxNjIsMC4xOTM0MywwLjE5NDI2LDAuMTk0MjcsMC4xOTQ2LDAuMTk0NjksMC4xOTQ3MywwLjE5NTUzLDAuMTk1OSwwLjE5NjM4LDAuMTk2NDksMC4xOTY3MSwwLjE5NzA1LDAuMTk3NTcsMC4xOTgzOCwwLjE5ODM5LDAuMTk4NjIsMC4xOTg4OSwwLjE5OTE5LDAuMTk5MjMsMC4xOTk3MywwLjIwMDA1LDAuMjAwMTgsMC4yMDAzLDAuMjAwNzcsMC4yMDA4MywwLjIwMTY4LDAuMjAyNSwwLjIwMjksMC4yMDI5LDAuMjAzNDIsMC4yMDM2NiwwLjIwMzc2LDAuMjA0MTYsMC4yMDQ5NSwwLjIwNTQ1LDAuMjA1NjIsMC4yMDU3LDAuMjA2MTEsMC4yMDY5NSwwLjIwODE1LDAuMjA4MjQsMC4yMDgzMiwwLjIwODg1LDAuMjA5MTUsMC4yMDk1OCwwLjIxMDMyLDAuMjEwNDgsMC4yMTEyNywwLjIxMzM0LDAuMjEzNTgsMC4yMTM3MywwLjIxMzc3LDAuMjE1MTcsMC4yMTYyLDAuMjE2NTcsMC4yMTY2OSwwLjIxNjgyLDAuMjE2ODcsMC4yMTc1NCwwLjIxNzY2LDAuMjE4NiwwLjIyMDMzLDAuMjIwNTksMC4yMjA4OSwwLjIyMTY5LDAuMjIxNzgsMC4yMjE5MSwwLjIyMjAyLDAuMjIyMDgsMC4yMjQxOSwwLjIyNTA2LDAuMjI1OTMsMC4yMjYzNCwwLjIyNjk3LDAuMjI3MywwLjIyODA1LDAuMjI5MzMsMC4yMjk1NywwLjIyOTYyLDAuMjMxMDcsMC4yMzEyMSwwLjIzMjA5LDAuMjMyOSwwLjIzMzI4LDAuMjMzNSwwLjIzNDUyLDAuMjM0NjIsMC4yMzQ4MywwLjIzNTMzLDAuMjM1NzIsMC4yMzU4NiwwLjIzNjE2LDAuMjM2NSwwLjIzNzAzLDAuMjM3NzksMC4yMzgwNSwwLjIzODUxLDAuMjM5ODMsMC4yNDAyMywwLjI0MDM4LDAuMjQwODcsMC4yNDEzOCwwLjI0MTkyLDAuMjQyNjIsMC4yNDI3MywwLjI0MzY5LDAuMjQ0MDMsMC4yNDQxMiwwLjI0NDE0LDAuMjQ0MzUsMC4yNDQ5NSwwLjI0NTQsMC4yNDYxNSwwLjI0Njk4LDAuMjQ2OTksMC4yNDcwNiwwLjI0ODM5LDAuMjQ4NTIsMC4yNDg4NiwwLjI0OTUyLDAuMjQ5NjgsMC4yNDk3LDAuMjUwMDIsMC4yNTA2MSwwLjI1MTEzLDAuMjUxNDEsMC4yNTE3NiwwLjI1MTc4LDAuMjUyOTMsMC4yNTMwMiwwLjI1MzA5LDAuMjUzMzEsMC4yNTQ2OSwwLjI1NTMsMC4yNTU0NywwLjI1NTUzLDAuMjU1OTMsMC4yNTY4MSwwLjI1NzAyLDAuMjU3OTQsMC4yNTgyMiwwLjI1ODIyLDAuMjU4MzcsMC4yNTg2NywwLjI1OTAyLDAuMjU5MTcsMC4yNTkzMywwLjI2MDE0LDAuMjYwNDgsMC4yNjA5NiwwLjI2MTQ3LDAuMjYxODIsMC4yNjI0MSwwLjI2MzUsMC4yNjQxOSwwLjI2NTE4LDAuMjY1MjQsMC4yNjYxNiwwLjI2NjQ1LDAuMjY2NDksMC4yNjc2OSwwLjI2ODE0LDAuMjY4MTksMC4yNjk2NiwwLjI3MDA4LDAuMjcwMzEsMC4yNzA3LDAuMjcxMTcsMC4yNzE2MSwwLjI3MjIxLDAuMjcyNCwwLjI3MjkxLDAuMjczMDUsMC4yNzMzMiwwLjI3MzU3LDAuMjczODcsMC4yNzQwMSwwLjI3NTU5LDAuMjc2MjcsMC4yNzY1OSwwLjI3NzIzLDAuMjc3NDMsMC4yNzc0OCwwLjI3NzU3LDAuMjc3NiwwLjI3NzY1LDAuMjc3NzMsMC4yNzgzNiwwLjI3ODczLDAuMjc5NzksMC4yNzk4NiwwLjI4MDMzLDAuMjgxMzcsMC4yODE4LDAuMjgxODMsMC4yODE5NywwLjI4MjQxLDAuMjgyNDksMC4yODI2MSwwLjI4MjcyLDAuMjgzNDUsMC4yODM1NiwwLjI4Mzc1LDAuMjg0MDQsMC4yODQwOCwwLjI4NDMxLDAuMjg1MDcsMC4yODUwOCwwLjI4NTU2LDAuMjg2MDcsMC4yODY2NCwwLjI4NjczLDAuMjg2ODQsMC4yODcxLDAuMjg3ODEsMC4yODg0LDAuMjg4ODksMC4yODkyOCwwLjI4OTg4LDAuMjg5OTksMC4yOTAxOSwwLjI5MDUyLDAuMjkwNTksMC4yOTA2NiwwLjI5MDgxLDAuMjkwOTIsMC4yOTExNiwwLjI5MTgyLDAuMjkyMTgsMC4yOTI1MSwwLjI5MjU3LDAuMjkzMTEsMC4yOTMzLDAuMjkzNzQsMC4yOTQxMywwLjI5NDUzLDAuMjk0NTUsMC4yOTQ4MiwwLjI5NDk5LDAuMjk1NDksMC4yOTU3MSwwLjI5NjA0LDAuMjk2MzEsMC4yOTYzOSwwLjI5NjQsMC4yOTY1MywwLjI5Njg1LDAuMjk2ODgsMC4yOTcyNCwwLjI5NzU4LDAuMjk4MDMsMC4yOTgwOSwwLjI5ODQ4LDAuMjk4NTIsMC4yOTg1NiwwLjI5OTExLDAuMjk5NjcsMC4yOTk5MywwLjI5OTk1LDAuMzAwMTMsMC4zMDAxNSwwLjMwMDUsMC4zMDA3NSwwLjMwMDgyLDAuMzAwOTMsMC4zMDA5OSwwLjMwMTE0LDAuMzAxODIsMC4zMDE5NCwwLjMwMTk2LDAuMzAyMzksMC4zMDI1NywwLjMwMjc0LDAuMzAyOTMsMC4zMDM2MiwwLjMwMzY1LDAuMzAzOTQsMC4zMDQwMiwwLjMwNDUyLDAuMzA0NzQsMC4zMDUzOCwwLjMwNTUzLDAuMzA1NiwwLjMwNTc0LDAuMzA1OTcsMC4zMDY2NCwwLjMwNzI0LDAuMzA3MjcsMC4zMDc0LDAuMzA3OTIsMC4zMDgyOCwwLjMwODk0LDAuMzA5NTQsMC4zMDk5NCwwLjMxMDgsMC4zMTE3MiwwLjMxMTg0LDAuMzExOTMsMC4zMTE5NiwwLjMxMjI1LDAuMzEzNTksMC4zMTUyNiwwLjMxNTQ0LDAuMzE1ODIsMC4zMTcyNCwwLjMxNzI4LDAuMzE3NjgsMC4zMTc4OSwwLjMxODA2LDAuMzE4MjUsMC4zMTg2MywwLjMxOTg1LDAuMzIxMjEsMC4zMjEzNSwwLjMyMTczLDAuMzIxOTgsMC4zMjIxMiwwLjMyMjIyLDAuMzIyODcsMC4zMjMxNiwwLjMyMzU1LDAuMzIzNTksMC4zMjM3MywwLjMyMzk0LDAuMzI0NDUsMC4zMjQ5LDAuMzI1MzYsMC4zMjU0NCwwLjMyNiwwLjMyNjM4LDAuMzI2MzgsMC4zMjY1MSwwLjMyNjg1LDAuMzI3NTIsMC4zMjgxMywwLjMyODY3LDAuMzI5MDUsMC4zMjk0NiwwLjMyOTY4LDAuMzI5OTMsMC4zMzAxNCwwLjMzMDQ5LDAuMzMwNzQsMC4zMzA5MSwwLjMzMTE1LDAuMzMxMzUsMC4zMzEzOCwwLjMzMzMzLDAuMzM1MDUsMC4zMzU3OSwwLjMzNTksMC4zMzY1OCwwLjMzNjcxLDAuMzM2ODMsMC4zMzY4NywwLjMzNzA2LDAuMzM3MTEsMC4zMzcyNiwwLjMzNzM4LDAuMzM3NDQsMC4zMzgwOCwwLjMzODcyLDAuMzM5MDksMC4zMzkxLDAuMzM5NTEsMC4zNDAwMywwLjM0MDE3LDAuMzQwMjksMC4zNDE2MiwwLjM0MjMyLDAuMzQzNjUsMC4zNDM2NSwwLjM0MzY5LDAuMzQzOCwwLjM0MzkyLDAuMzQ0MTUsMC4zNDQyMiwwLjM0NTI2LDAuMzQ1NTEsMC4zNDU4MiwwLjM0NTk3LDAuMzQ2MjcsMC4zNDYzMSwwLjM0NjMxLDAuMzQ2NTksMC4zNDc0NiwwLjM0NzU2LDAuMzQ4MzgsMC4zNDg3MywwLjM0ODczLDAuMzQ4NzQsMC4zNDg5OSwwLjM0OTE3LDAuMzQ5MjQsMC4zNTAwMiwwLjM1MDMzLDAuMzUxNzUsMC4zNTE3OCwwLjM1MjY0LDAuMzUyODcsMC4zNTMwNiwwLjM1MzE0LDAuMzUzMjcsMC4zNTM2MSwwLjM1MzkxLDAuMzU0MzQsMC4zNTQ2MiwwLjM1NDg3LDAuMzU0OTIsMC4zNTQ5NywwLjM1NTMyLDAuMzU1NzIsMC4zNTY1LDAuMzU3ODcsMC4zNTkxMiwwLjM1OTc1LDAuMzU5OTQsMC4zNjExOCwwLjM2MTQ5LDAuMzYyNTksMC4zNjMyLDAuMzYzOTEsMC4zNjM5NSwwLjM2Mzk4LDAuMzY0MTYsMC4zNjQ0MiwwLjM2NTE1LDAuMzY1MiwwLjM2NTc0LDAuMzY2MjMsMC4zNjY4NCwwLjM2Njk3LDAuMzY3MjYsMC4zNjc2MSwwLjM2NzY4LDAuMzY4MTQsMC4zNjg3OCwwLjM2ODk4LDAuMzY5MDEsMC4zNjk1OSwwLjM2OTc5LDAuMzcwMTQsMC4zNzAzMywwLjM3MTIyLDAuMzcxNjYsMC4zNzIxLDAuMzczNTUsMC4zNzM4MywwLjM3NDEsMC4zNzQ1LDAuMzc0NTMsMC4zNzQ1NSwwLjM3NDYxLDAuMzc0NjEsMC4zNzUwOCwwLjM3NjIxLDAuMzc2MzcsMC4zNzY1MSwwLjM3NzMzLDAuMzc3NCwwLjM3NzgsMC4zNzgxMywwLjM3ODE1LDAuMzc4MzcsMC4zNzgzOSwwLjM3ODQxLDAuMzc4NSwwLjM3ODYyLDAuMzc4OTIsMC4zNzkyNywwLjM3OTQ0LDAuMzc5NjUsMC4zNzk2OCwwLjM4MDg3LDAuMzgwOTgsMC4zODE1MiwwLjM4MjE2LDAuMzgyMjgsMC4zODI3OSwwLjM4MzQ5LDAuMzg0MTgsMC4zODQ4OCwwLjM4NDk2LDAuMzg1MjcsMC4zODUzMywwLjM4NTc5LDAuMzg1OTEsMC4zODYyOSwwLjM4Njc3LDAuMzg3MzIsMC4zODgyOCwwLjM4OTQ1LDAuMzg5NSwwLjM5MDM3LDAuMzkwOSwwLjM5MTc4LDAuMzkyMjQsMC4zOTIzMiwwLjM5Mjg1LDAuMzkzMjIsMC4zOTM0OSwwLjM5MzUzLDAuMzkzNTUsMC4zOTQxNiwwLjM5NDU1LDAuMzk0NzMsMC4zOTQ4MSwwLjM5NTEsMC4zOTUyNCwwLjM5NTQ1LDAuMzk1NjEsMC4zOTU3LDAuMzk1OCwwLjM5NTg5LDAuMzk2LDAuMzk3MTYsMC4zOTc0NywwLjM5ODI3LDAuMzk4OTYsMC4zOTg5OCwwLjM5OTcxLDAuMzk5OTQsMC40MDAzNSwwLjQwMDQsMC40MDExMSwwLjQwMTM1LDAuNDAxMzYsMC40MDI0NywwLjQwMjkyLDAuNDAzNDQsMC40MDUxOSwwLjQwNTMsMC40MDU3NSwwLjQwNTk4LDAuNDA2NTEsMC40MDc4LDAuNDA4NzEsMC40MDkxOSwwLjQwOTQ4LDAuNDEwMDIsMC40MTAxLDAuNDEwMSwwLjQxMDE3LDAuNDEwOTgsMC40MTEwNiwwLjQxMTY1LDAuNDExODcsMC40MTE5OCwwLjQxMjEzLDAuNDEyMzgsMC40MTI0OSwwLjQxMjUzLDAuNDEzOTgsMC40MTQ2LDAuNDE0OTEsMC40MTQ5NywwLjQxNDk4LDAuNDE1MTYsMC40MTU3LDAuNDE1OTMsMC40MTcsMC40MTcwNywwLjQxNzQzLDAuNDE3ODksMC40MTgzNywwLjQxODkxLDAuNDE5MzIsMC40MTkzNywwLjQxOTU3LDAuNDIwNzksMC40MjEwOCwwLjQyMTUyLDAuNDIxNywwLjQyMTcyLDAuNDIxODYsMC40MjI4MiwwLjQyMzgxLDAuNDI0MTgsMC40MjQ4OSwwLjQyNjM1LDAuNDI2OTIsMC40MjczMywwLjQyODA0LDAuNDI4MTIsMC40Mjg0MywwLjQyODgyLDAuNDI4ODUsMC40Mjg5MywwLjQzMTA0LDAuNDMxMTIsMC40MzE5OSwwLjQzMjIxLDAuNDMyOTEsMC40MzMyMSwwLjQzMzMzLDAuNDMzNzIsMC40MzM3NSwwLjQzNDQ4LDAuNDM0NjYsMC40MzQ5MSwwLjQzNTA2LDAuNDM1MzksMC40MzU4NSwwLjQzNjI0LDAuNDM3MTUsMC40MzcxOSwwLjQzODQxLDAuNDM4NTcsMC40Mzg1OSwwLjQzOTM5LDAuNDQwMjcsMC40NDA5MSwwLjQ0MTg4LDAuNDQxOTcsMC40NDIxMSwwLjQ0MzAzLDAuNDQzMjcsMC40NDQ4NiwwLjQ0NTcsMC40NDU3NCwwLjQ0NjYxLDAuNDQ3MDcsMC40NDgyLDAuNDQ4MzcsMC40NDg1MywwLjQ1MDA4LDAuNDUxMTEsMC40NTEyOSwwLjQ1Mjc5LDAuNDUyOTMsMC40NTM1NiwwLjQ1MzY1LDAuNDU0OTksMC40NTUwMiwwLjQ1NTYxLDAuNDU2MDUsMC40NTYyNSwwLjQ1NzI3LDAuNDU4MDMsMC40NTgwNSwwLjQ2MDMzLDAuNDYwMzUsMC40NjEwNCwwLjQ2MTgyLDAuNDYzMywwLjQ2Mzc3LDAuNDYzOTYsMC40NjQwMiwwLjQ2NTI2LDAuNDY1MjcsMC40Njc0MiwwLjQ2OTMsMC40Njk0NSwwLjQ2OTQ2LDAuNDY5NzQsMC40NzA0NCwwLjQ3MDk4LDAuNDcxODUsMC40NzIwOSwwLjQ3MjYzLDAuNDc0NDYsMC40NzQ2NSwwLjQ3NjM2LDAuNDc3MiwwLjQ3NzM5LDAuNDc3NzcsMC40NzkxOCwwLjQ3OTIsMC40NzkyNSwwLjQ3OTU1LDAuNDgzMTQsMC40ODQwNCwwLjQ4NTk1LDAuNDg2LDAuNDg2NDQsMC40ODkwOSwwLjQ4OTE0LDAuNDg5OTYsMC40OTE5OCwwLjQ5MjI2LDAuNDkzMzMsMC40OTU1OSwwLjQ5NTk0LDAuNDk2NDEsMC40OTgxLDAuNDk4ODQsMC40OTg5OCwwLjUwMDA1LDAuNTAwMDcsMC41MDA1MSwwLjUwMjgsMC41MDQ4NiwwLjUwNjExLDAuNTA4NjEsMC41MTA3MiwwLjUxMDk5LDAuNTEyMTIsMC41MTM2MywwLjUxNjA5LDAuNTE2MTIsMC41MTY1LDAuNTE3ODQsMC41MTgzLDAuNTE5ODIsMC41MjA5NiwwLjUyMjU4LDAuNTIzMSwwLjUyMzY2LDAuNTIzNzIsMC41MjM4OSwwLjUyNDcxLDAuNTI1NCwwLjUyNzEzLDAuNTI4NDMsMC41Mjk5OSwwLjUzMTAzLDAuNTM0MDUsMC41MzQ4OCwwLjUzNjcxLDAuNTM3MTksMC41Mzc1MiwwLjUzODQxLDAuNTM5MSwwLjU0MTQ4LDAuNTQxNDksMC41NDE1MiwwLjU0ODE5LDAuNTQ5NTIsMC41NDk1NSwwLjU1MDAyLDAuNTUxNzUsMC41NTI2MSwwLjU1Mzg5LDAuNTU1NDcsMC41NTU3NCwwLjU1NzYzLDAuNTU5NjUsMC41NjI4OCwwLjU2OCwwLjU2ODY5LDAuNTcxNCwwLjU3MzE1LDAuNTc0MTcsMC41NzU2LDAuNTc5MzksMC41ODI5NiwwLjU4NDksMC41OTEwNCwwLjYwMTU5LDAuNjE0OCwwLjYxODA3LDAuNjE4MTIsMC42MjI4MiwwLjYyMzEyLDAuNjMxMjUsMC42MzI4MywwLjYzNTA1LDAuNjQyNTQsMC42NDcxNCwwLjY0ODY0LDAuNjUwNDgsMC42NTQ5MywwLjY1ODQ4LDAuNjYzNTYsMC42NjQ1MSwwLjY3MzU0LDAuNjgxOTYsMC42ODI3OSwwLjY4OTI4LDAuNjk0NTgsMC43LDAuNzExOCwwLjcxOTE5XTsKCmNvbnN0IEJJTlMgPSA0MDsKY29uc3QgY2hhcnQgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgiY2hhcnQiKTsKY29uc3QgTlMgPSAiaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciOwoKZnVuY3Rpb24gZWwobmFtZSwgYXR0cnMsIHRleHQpIHsKICBjb25zdCBub2RlID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudE5TKE5TLCBuYW1lKTsKICBmb3IgKGNvbnN0IGtleSBpbiBhdHRycykgbm9kZS5zZXRBdHRyaWJ1dGUoa2V5LCBhdHRyc1trZXldKTsKICBpZiAodGV4dCAhPT0gdW5kZWZpbmVkKSBub2RlLnRleHRDb250ZW50ID0gdGV4dDsKICByZXR1cm4gbm9kZTsKfQoKZnVuY3Rpb24gaGlzdG9ncmFtKHZhbHVlcykgewogIGNvbnN0IGJpbnMgPSBuZXcgQXJyYXkoQklOUykuZmlsbCgwKTsKICBmb3IgKGNvbnN0IHYgb2YgdmFsdWVzKSBiaW5zW01hdGgubWluKEJJTlMgLSAxLCBNYXRoLmZsb29yKHYgKiBCSU5TKSldICs9IDE7CiAgcmV0dXJuIGJpbnM7Cn0KCmNvbnN0IGlsbEJpbnMgPSBoaXN0b2dyYW0oSUxMKTsKY29uc3Qgd2VsbEJpbnMgPSBoaXN0b2dyYW0oV0VMTCk7CgovLyBHZW9tZXRyeTogdHdvIHN0YWNrZWQgc3RyaXBzIHNoYXJpbmcgb25lIHggYXhpcy4KY29uc3QgTCA9IDQyLCBSID0gNTQ2LCBXID0gUiAtIEw7CmNvbnN0IFJPV1MgPSBbCiAgeyB5OiAyNCwgIGg6IDc0LCBiaW5zOiBpbGxCaW5zLCAgY29sb3VyOiAidmFyKC0taWxsKSIsICBsYWJlbDogIjIwIHBlb3BsZSB3aG8gYXJlIGlsbCIgfSwKICB7IHk6IDEzMiwgaDogNzQsIGJpbnM6IHdlbGxCaW5zLCBjb2xvdXI6ICJ2YXIoLS13ZWxsKSIsIGxhYmVsOiAiOTgwIHBlb3BsZSB3aG8gYXJlIHdlbGwiIH0KXTsKCmZ1bmN0aW9uIGRyYXcodGhyZXNob2xkKSB7CiAgY2hhcnQudGV4dENvbnRlbnQgPSAiIjsKICBjb25zdCB4T2YgPSB2ID0+IEwgKyB2ICogVzsKCiAgZm9yIChjb25zdCByb3cgb2YgUk9XUykgewogICAgY29uc3QgcGVhayA9IE1hdGgubWF4KC4uLnJvdy5iaW5zLCAxKTsKICAgIGNoYXJ0LmFwcGVuZENoaWxkKGVsKCJ0ZXh0IiwgewogICAgICB4OiBMLCB5OiByb3cueSAtIDcsIGZpbGw6ICJ2YXIoLS1tdXRlZCkiLCAiZm9udC1zaXplIjogIjExcHgiCiAgICB9LCByb3cubGFiZWwpKTsKICAgIGNoYXJ0LmFwcGVuZENoaWxkKGVsKCJsaW5lIiwgewogICAgICB4MTogTCwgeTE6IHJvdy55ICsgcm93LmgsIHgyOiBSLCB5Mjogcm93LnkgKyByb3cuaCwKICAgICAgc3Ryb2tlOiAidmFyKC0tbGluZSkiLCAic3Ryb2tlLXdpZHRoIjogMQogICAgfSkpOwoKICAgIGZvciAobGV0IGkgPSAwOyBpIDwgQklOUzsgaSArPSAxKSB7CiAgICAgIGlmICghcm93LmJpbnNbaV0pIGNvbnRpbnVlOwogICAgICBjb25zdCBoZWlnaHQgPSAocm93LmJpbnNbaV0gLyBwZWFrKSAqIHJvdy5oOwogICAgICAvLyBBIGJpbiBjb3VudHMgYXMgZmxhZ2dlZCB3aGVuIGl0cyBsZWZ0IGVkZ2UgaXMgYXQgb3IgcGFzdCB0aGUgdGhyZXNob2xkLgogICAgICBjb25zdCBmbGFnZ2VkID0gKGkgLyBCSU5TKSA+PSB0aHJlc2hvbGQgLSAxZS05OwogICAgICBjaGFydC5hcHBlbmRDaGlsZChlbCgicmVjdCIsIHsKICAgICAgICB4OiB4T2YoaSAvIEJJTlMpICsgMC41LAogICAgICAgIHk6IHJvdy55ICsgcm93LmggLSBoZWlnaHQsCiAgICAgICAgd2lkdGg6IFcgLyBCSU5TIC0gMSwKICAgICAgICBoZWlnaHQ6IGhlaWdodCwKICAgICAgICBmaWxsOiBmbGFnZ2VkID8gcm93LmNvbG91ciA6ICJ2YXIoLS1kaW0pIgogICAgICB9KSk7CiAgICB9CiAgfQoKICAvLyBUaGUgdGhyZXNob2xkIGxpbmUsIHNwYW5uaW5nIGJvdGggc3RyaXBzLgogIGNvbnN0IHggPSB4T2YodGhyZXNob2xkKTsKICBjaGFydC5hcHBlbmRDaGlsZChlbCgibGluZSIsIHsKICAgIHgxOiB4LCB5MTogMTQsIHgyOiB4LCB5MjogMjEyLAogICAgc3Ryb2tlOiAiI2ZmZmZmZiIsICJzdHJva2Utd2lkdGgiOiAxLjUsICJzdHJva2UtZGFzaGFycmF5IjogIjQgMyIKICB9KSk7CiAgY2hhcnQuYXBwZW5kQ2hpbGQoZWwoInRleHQiLCB7CiAgICB4OiBNYXRoLm1pbih4ICsgNiwgUiAtIDY2KSwgeTogMTIsIGZpbGw6ICIjZmZmZmZmIiwgImZvbnQtc2l6ZSI6ICIxMHB4IgogIH0sICJmbGFnIGZyb20gaGVyZSDihpIiKSk7CgogIGZvciAoY29uc3QgdGljayBvZiBbMCwgMC4yNSwgMC41LCAwLjc1LCAxXSkgewogICAgY2hhcnQuYXBwZW5kQ2hpbGQoZWwoInRleHQiLCB7CiAgICAgIHg6IHhPZih0aWNrKSwgeTogMjMyLCBmaWxsOiAidmFyKC0tbXV0ZWQpIiwgImZvbnQtc2l6ZSI6ICIxMHB4IiwgInRleHQtYW5jaG9yIjogIm1pZGRsZSIKICAgIH0sIHRpY2sudG9GaXhlZCgyKSkpOwogIH0KICBjaGFydC5hcHBlbmRDaGlsZChlbCgidGV4dCIsIHsKICAgIHg6IChMICsgUikgLyAyLCB5OiAyNDYsIGZpbGw6ICJ2YXIoLS1tdXRlZCkiLCAiZm9udC1zaXplIjogIjEwcHgiLCAidGV4dC1hbmNob3IiOiAibWlkZGxlIgogIH0sICJyaXNrIHNjb3JlIHRoZSBtb2RlbCBnYXZlIGVhY2ggcGVyc29uIikpOwp9CgpmdW5jdGlvbiB2ZXJkaWN0Rm9yKHRwLCBmbiwgZnAsIHByZWNpc2lvbiwgcmVjYWxsKSB7CiAgaWYgKGZuID09PSAwICYmIGZwID4gMjAwKSB7CiAgICByZXR1cm4gIkV2ZXJ5IGNhc2UgZm91bmQsIGFuZCAiICsgZnAgKyAiIGhlYWx0aHkgcGVvcGxlIGNhbGxlZCBpbiBmb3Igbm90aGluZy4iOwogIH0KICBpZiAoZnAgPT09IDAgJiYgZm4gPiAwKSB7CiAgICByZXR1cm4gIk5vYm9keSB0cm91YmxlZCB1bm5lY2Vzc2FyaWx5LCBhbmQgIiArIGZuICsgIiBvZiB0aGUgMjAgY2FzZXMgbWlzc2VkIGVudGlyZWx5LiI7CiAgfQogIGlmIChyZWNhbGwgPj0gMC43NSAmJiBwcmVjaXNpb24gPCAwLjQpIHsKICAgIHJldHVybiAiQ2F0Y2hpbmcgbW9zdCBjYXNlcywgYnV0ICIgKyBNYXRoLnJvdW5kKDEgLyBwcmVjaXNpb24pICsKICAgICAgICAgICAiIHBlb3BsZSBhcmUgY2FsbGVkIGluIGZvciBldmVyeSByZWFsIG9uZS4iOwogIH0KICBpZiAocHJlY2lzaW9uID49IDAuNiAmJiByZWNhbGwgPD0gMC42KSB7CiAgICByZXR1cm4gIkFsYXJtcyBhcmUgbW9zdGx5IHJlYWwsIGFuZCBoYWxmIHRoZSBjYXNlcyBuZXZlciBnZXQgZm91bmQuIjsKICB9CiAgcmV0dXJuICJNb3ZpbmcgdGhlIGxpbmUgdHJhZGVzIGNhc2VzIGZvdW5kIGFnYWluc3QgcGVvcGxlIHRyb3VibGVkLiBOZWl0aGVyIGVuZCBpcyB0aGUgYmV0dGVyIG1vZGVsLiI7Cn0KCmZ1bmN0aW9uIHVwZGF0ZSgpIHsKICBjb25zdCB0aHJlc2hvbGQgPSBwYXJzZUZsb2F0KGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJ0aHIiKS52YWx1ZSk7CiAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoInRock91dCIpLnRleHRDb250ZW50ID0gdGhyZXNob2xkLnRvRml4ZWQoMik7CgogIGNvbnN0IHRwID0gSUxMLmZpbHRlcihzID0+IHMgPj0gdGhyZXNob2xkKS5sZW5ndGg7CiAgY29uc3QgZm4gPSBJTEwubGVuZ3RoIC0gdHA7CiAgY29uc3QgZnAgPSBXRUxMLmZpbHRlcihzID0+IHMgPj0gdGhyZXNob2xkKS5sZW5ndGg7CiAgY29uc3QgdG4gPSBXRUxMLmxlbmd0aCAtIGZwOwogIGNvbnN0IHByZWNpc2lvbiA9ICh0cCArIGZwKSA/IHRwIC8gKHRwICsgZnApIDogMDsKICBjb25zdCByZWNhbGwgPSAodHAgKyBmbikgPyB0cCAvICh0cCArIGZuKSA6IDA7CgogIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJyZWFkb3V0IikudGV4dENvbnRlbnQgPQogICAgInRocmVzaG9sZCAiICsgdGhyZXNob2xkLnRvRml4ZWQoMikgKwogICAgIiAgIOKGkiAgIGZvdW5kICIgKyB0cCArICIsIG1pc3NlZCAiICsgZm4gKyAiLCBmYWxzZSBhbGFybXMgIiArIGZwOwogIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJ2ZXJkaWN0IikudGV4dENvbnRlbnQgPSB2ZXJkaWN0Rm9yKHRwLCBmbiwgZnAsIHByZWNpc2lvbiwgcmVjYWxsKTsKCiAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoInJlY2FsbFZhbCIpLnRleHRDb250ZW50ID0gcmVjYWxsLnRvRml4ZWQoMyk7CiAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoInByZWNWYWwiKS50ZXh0Q29udGVudCA9IHByZWNpc2lvbi50b0ZpeGVkKDMpOwogIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJyZWNhbGxCYXIiKS5zdHlsZS53aWR0aCA9IChyZWNhbGwgKiAxMDApICsgIiUiOwogIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJwcmVjQmFyIikuc3R5bGUud2lkdGggPSAocHJlY2lzaW9uICogMTAwKSArICIlIjsKCiAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoInRwIikudGV4dENvbnRlbnQgPSB0cDsKICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgiZm4iKS50ZXh0Q29udGVudCA9IGZuOwogIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJmcCIpLnRleHRDb250ZW50ID0gZnA7CiAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoInRuIikudGV4dENvbnRlbnQgPSB0bjsKCiAgZHJhdyh0aHJlc2hvbGQpOwp9Cgpkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgidGhyIikuYWRkRXZlbnRMaXN0ZW5lcigiaW5wdXQiLCB1cGRhdGUpOwp1cGRhdGUoKTsKPC9zY3JpcHQ+CjwvYm9keT4KPC9odG1sPgo="
 width="100%"></iframe>

One model, six completely different systems.

At 0.30 the programme finds every single case and calls in 514 healthy people to do it. At 0.80 it never troubles anyone unnecessarily and misses 17 of the 20 cases. **Neither end is a better model; they are the same model configured for different priorities.**

Two facts follow that are worth holding permanently.

**Precision and recall trade against each other**, and the trade is continuous. You cannot maximise both, and any claim to have done so usually means the classes were easy to separate rather than that the method was clever.

**The threshold belongs to whoever bears the cost of the errors.** Dr Meera, not the vendor, should be choosing between row three and row five, because she is the one who knows what a missed case costs against what an unnecessary follow-up costs. Shipping a model with the threshold buried inside it takes that decision away from her.

![Visual explanation of threshold tradeoff](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_threshold_tradeoff.png)

## The 920 People Nobody Counted

Precision and recall have a property that is easy to miss and occasionally important: **neither of them looks at the true negatives at all.**

Check the formulas against Model B's confusion matrix. Recall uses the 16 found and the 4 missed. Precision uses the 16 found and the 60 false alarms. The 920 healthy people correctly cleared appear in neither. You could add ten thousand more healthy people, all correctly cleared, and both figures would be unchanged.

That is usually the right behaviour, because on a rare-class problem the true negatives are the uninteresting majority and letting them into the arithmetic is exactly what made accuracy useless. Occasionally it is not, and a third measure covers the gap.

`Specificity` is the fraction of genuinely healthy people who were correctly cleared, which is true negatives divided by all who were actually well. For Model B that is 920 out of 980, or 0.939. Where recall asks how good the model is at finding the positives, specificity asks how good it is at leaving the negatives alone.

The pairing matters when the cost of a false alarm falls on the population rather than on the programme. A screening programme with specificity of 0.939 sounds excellent, and on a population of one lakh it means around six thousand healthy people called back unnecessarily. Recall and precision would not have made that number visible; specificity, multiplied by the population, does.

The practical rule is short. **Report recall with precision when you care about the flagged list, and recall with specificity when you care about the whole population.** Both pairings are honest, and quoting one number from either pair is not.

![Visual explanation of the 920 people nobody counted](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_section_the_920_people_nobody_counted_simple_v2.png)

## More Than Two Categories

The mail folders from earlier in this unit had three categories rather than two, and the measures extend to that case with one decision to make.

Precision and recall are always defined for **one chosen class against everything else**. Recall for the promotions folder means: of the messages that genuinely belonged in promotions, what fraction was filed there. So a three-class problem has three recalls and three precisions, and a confusion matrix that is three by three rather than two by two, with correct predictions on the diagonal and every kind of mistake visible off it.

Reducing those to one figure requires choosing how to average, and the two common choices answer different questions.

- **Macro averaging** takes the plain average across classes, so every class counts equally regardless of size. A tiny class that the model handles badly will drag the figure down.
- **Micro averaging** pools all the counts first and then computes once, so every *example* counts equally, which means large classes dominate.

If the personal folder holds 90 percent of messages and the model is hopeless at promotions, micro averaging will look fine and macro averaging will not. Neither is wrong; they are answers to "how well does this work per message" and "how well does this work per category", and stating which you used is part of reporting the number.

![Visual explanation of more than two categories](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_section_more_than_two_categories.png)

## Choosing What to Measure

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Measure</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Question it answers</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Use it when</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">It misleads when</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Accuracy</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What fraction of all predictions were right?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Classes are roughly balanced and both errors cost the same</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One class is rare, as here</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Recall</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Of the real cases, how many did we catch?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Missing a case is the expensive error</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quoted alone; flagging everyone gives recall 1.0</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Precision</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Of what we flagged, how much was real?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A false alarm is the expensive error</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quoted alone; flagging one certain case gives precision 1.0</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>F1</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A single figure balancing the two</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">You must rank many models automatically</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The two errors have very different costs</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Confusion matrix</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Exactly what happened, in counts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Always; every other measure derives from it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rarely, though it is harder to put in a headline</td>
    </tr>
  </tbody>
</table>

The last row is the practical advice. Ask for the confusion matrix, and derive whichever measure your situation calls for. Everything else in the table is a summary of those four numbers, and summaries are where information goes to hide.

![Visual explanation of choosing what to measure](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_section_choosing_what_to_measure_simple_v2.png)

## Your Turn

Take the threshold table and turn it into a decision rather than an observation.

Suppose a missed case costs the health programme roughly fifty times what an unnecessary follow-up costs, because the condition is treatable when caught early and serious when missed. Compute, for each of the six thresholds, the total cost as fifty times the missed cases plus one times the false alarms. Find the threshold that minimises it. Then redo the calculation assuming the follow-up is an invasive procedure and the ratio is five to one instead. The best threshold moves, and being able to show that movement is what turns a metrics table into advice somebody can act on.

Then extend the code to a third model of your own construction: one that flags exactly the 20 ill people and nobody else. Compute all four measures for it. Notice that it scores perfectly on every one, and then ask yourself the awkward question of whether a perfect score on your test data is more likely to mean an excellent model or a mistake somewhere in how the data was assembled.

Finally, work out what a confusion matrix looks like when there are three categories rather than two, using the mail folders from earlier in this unit. Draw the grid. Then define recall for the promotions folder specifically, and satisfy yourself that precision and recall are always defined with respect to one chosen class rather than for the model as a whole.
