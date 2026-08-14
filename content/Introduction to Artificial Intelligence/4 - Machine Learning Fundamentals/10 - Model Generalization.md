## Introduction

Two students submit machine learning projects on the same dataset in the same week, and their reports read very differently.

Nikita's model gets 71 percent of the training examples right. She writes that she is disappointed and suspects she needs a more powerful method.

Arun's model gets 100 percent of the training examples right. He writes that his approach has completely solved the problem.

Their instructor tests both on a fresh sample nobody has seen. Nikita's model gets 68 percent. Arun's gets 34 percent, which is worse than guessing.

Arun's model has not solved anything. It has memorised the answer sheet, and memorising an answer sheet is precisely useless for the next examination. The gap between his 100 and his 34 is the single most important phenomenon in applied machine learning, and it has almost nothing to do with which method he chose.

**Definition:** `Generalization` is a model's performance on data it was not trained on. A model `overfits` when it captures noise particular to the training data and performs far worse on new data, and `underfits` when it is too rigid to capture the real pattern and performs poorly everywhere.

![Opening scene: Two students submit machine learning projects on the same dataset in the same week, and their reports read very differently.](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_section_introduction.png)

## Two Ways to Be Wrong

Failure comes in two opposite shapes, and confusing them leads to exactly the wrong repair.

- **Underfitting** means the model is too simple for the pattern. It performs badly on the training data and about equally badly on new data. Nikita's 71 and 68 look like this.
- **Overfitting** means the model is flexible enough to fit the noise as well as the signal. It performs superbly on training data and poorly on new data. Arun's 100 and 34 are the classic signature.

The diagnostic is not the score. It is **the gap between the two scores**.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Training score</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Test score</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Diagnosis</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What to do</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Poor</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Poor, and similar</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Underfitting</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">More flexibility, better features; more data will not help</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Excellent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Much worse</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Overfitting</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Less flexibility, or more data</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Good</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nearly as good</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">About right</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stop</td>
    </tr>
  </tbody>
</table>

Notice the first row's last cell, because it is the mistake people make most often. Collecting more data is the standard remedy for overfitting and does nothing at all for underfitting. If the model is too rigid to represent the pattern, ten times as many examples will let it be too rigid with more confidence.

![Visual explanation of underfit overfit](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_underfit_overfit.png)

## Watching It Happen

The cleanest demonstration uses a model whose flexibility can be turned up by a single number. A polynomial of degree 1 is a straight line, degree 2 a parabola, and higher degrees bend more freely.

Ten noisy points are sampled from a smooth curve, and polynomials of every degree from 0 to 9 are fitted to them.

Reading the code below: `solve` is Gaussian elimination, textbook linear algebra with nothing machine-learning about it, and it can be skipped entirely. `fit_polynomial` is least squares from the regression lesson generalised from a line to a curve. The lesson is the last loop, which fits ten models of increasing flexibility and prints two error columns side by side.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzk6fb" 
 width="100%"
></iframe>

```
Fitting curves of increasing flexibility to 10 noisy points

 degree  train RMSE  test RMSE
------------------------------
      0       0.613      0.702
      1       0.518      0.526
      2       0.517      0.528
      3       0.237      0.283
      4       0.207      0.294
      5       0.184      0.278
      6       0.181      0.281
      7       0.170      0.289
      8       0.169      0.300
      9       0.000      1.281

Lowest test error at degree 5
```

| In the code | What it is | Why it is there |
| --- | --- | --- |
| `true_curve` | One period of a sine wave | The real pattern, which no model is told about |
| `rng.gauss(0, 0.20)` | Noise added to each point | The thing an overfitted model will memorise |
| `degree` | The flexibility dial | 0 is a flat line, 9 can pass through all ten points |
| `rmse(w, TRAIN)` | Error on data it learned from | Falls forever, so it proves nothing |
| `rmse(w, TEST)` | Error on 30 unseen points | The column that actually matters |

Move the degree below and watch the fitted curve against the true one. The two error figures come from the table above; what the table cannot show is the shape the curve takes to earn them.

<iframe
 frameBorder="0"
 height="520px" data-visualizer="overfitting_explorer.html" src="data:text/html;base64,PCFkb2N0eXBlIGh0bWw+CjxodG1sIGxhbmc9ImVuIj4KPGhlYWQ+CjxtZXRhIGNoYXJzZXQ9InV0Zi04Ij4KPG1ldGEgbmFtZT0idmlld3BvcnQiIGNvbnRlbnQ9IndpZHRoPWRldmljZS13aWR0aCwgaW5pdGlhbC1zY2FsZT0xIj4KPHRpdGxlPk92ZXJmaXR0aW5nIEV4cGxvcmVyPC90aXRsZT4KPHN0eWxlPgogIDpyb290IHsKICAgIC0tYmc6ICMxMjE2MWQ7IC0tbGluZTogIzJjMzU0MjsgLS10ZXh0OiAjZTZlYmYyOyAtLW11dGVkOiAjOGI5N2E4OwogICAgLS1hY2NlbnQ6ICNmMjk5NGE7IC0tZGltOiAjM2E0NDUzOyAtLXRyYWluOiAjNTZjMjg4OyAtLXRlc3Q6ICNlMjY2NmI7CiAgfQogICogeyBib3gtc2l6aW5nOiBib3JkZXItYm94OyB9CiAgaHRtbCwgYm9keSB7IG1hcmdpbjogMDsgYmFja2dyb3VuZDogdmFyKC0tYmcpOyBjb2xvcjogdmFyKC0tdGV4dCk7CiAgICBmb250LWZhbWlseTogSW50ZXIsIHVpLXNhbnMtc2VyaWYsIHN5c3RlbS11aSwgLWFwcGxlLXN5c3RlbSwgIlNlZ29lIFVJIiwgc2Fucy1zZXJpZjsgfQogIC53cmFwIHsgcGFkZGluZzogMThweCAyMHB4IDIwcHg7IG1heC13aWR0aDogOTAwcHg7IG1hcmdpbjogMCBhdXRvOyB9CiAgLnRpdGxlIHsgZm9udC1zaXplOiAxMXB4OyBsZXR0ZXItc3BhY2luZzogLjE4ZW07IHRleHQtdHJhbnNmb3JtOiB1cHBlcmNhc2U7CiAgICBjb2xvcjogdmFyKC0tbXV0ZWQpOyB0ZXh0LWFsaWduOiBjZW50ZXI7IH0KICAuZm9ybXVsYSB7IHRleHQtYWxpZ246IGNlbnRlcjsgZm9udC1mYW1pbHk6IHVpLW1vbm9zcGFjZSwgTWVubG8sIG1vbm9zcGFjZTsKICAgIGZvbnQtc2l6ZTogMTVweDsgbWFyZ2luOiA2cHggMCAxNHB4OwogICAgZGlzcGxheTogZmxleDsgZmxleC13cmFwOiB3cmFwOyBqdXN0aWZ5LWNvbnRlbnQ6IGNlbnRlcjsgZ2FwOiA0cHggMjBweDsgfQogIC5mb3JtdWxhIHNwYW4geyB3aGl0ZS1zcGFjZTogbm93cmFwOyB9CiAgLnN3YXRjaCB7IGRpc3BsYXk6IGlubGluZS1ibG9jazsgd2lkdGg6IDlweDsgaGVpZ2h0OiA5cHg7IGJvcmRlci1yYWRpdXM6IDJweDsgbWFyZ2luLXJpZ2h0OiA1cHg7IH0KICAucmVhZG91dCB7IGJhY2tncm91bmQ6ICMwZDExMTc7IGJvcmRlcjogMXB4IHNvbGlkIHZhcigtLWxpbmUpOyBib3JkZXItcmFkaXVzOiA2cHg7CiAgICBwYWRkaW5nOiA5cHggMTJweDsgZm9udC1mYW1pbHk6IHVpLW1vbm9zcGFjZSwgTWVubG8sIG1vbm9zcGFjZTsKICAgIGZvbnQtc2l6ZTogMTNweDsgdGV4dC1hbGlnbjogY2VudGVyOyB9CiAgLnZlcmRpY3QgeyB0ZXh0LWFsaWduOiBjZW50ZXI7IGZvbnQtc2l6ZTogMTNweDsgbGluZS1oZWlnaHQ6IDEuNTsKICAgIG1hcmdpbjogMTBweCAwIDE0cHg7IG1pbi1oZWlnaHQ6IDM4cHg7IGNvbG9yOiB2YXIoLS1hY2NlbnQpOyB9CiAgLmNvbnRyb2wgeyBkaXNwbGF5OiBmbGV4OyBhbGlnbi1pdGVtczogY2VudGVyOyBnYXA6IDEycHg7IG1hcmdpbi1ib3R0b206IDE2cHg7IH0KICAuY29udHJvbCBsYWJlbCB7IGZvbnQtZmFtaWx5OiB1aS1tb25vc3BhY2UsIE1lbmxvLCBtb25vc3BhY2U7IGZvbnQtc2l6ZTogMTNweDsKICAgIGNvbG9yOiB2YXIoLS1tdXRlZCk7IHdoaXRlLXNwYWNlOiBub3dyYXA7IH0KICAuY29udHJvbCBvdXRwdXQgeyBmb250LWZhbWlseTogdWktbW9ub3NwYWNlLCBNZW5sbywgbW9ub3NwYWNlOyBmb250LXNpemU6IDEzcHg7CiAgICB3aWR0aDogMjBweDsgdGV4dC1hbGlnbjogcmlnaHQ7IGNvbG9yOiB2YXIoLS1hY2NlbnQpOyB9CiAgaW5wdXRbdHlwZT1yYW5nZV0geyBmbGV4OiAxOyAtd2Via2l0LWFwcGVhcmFuY2U6IG5vbmU7IGFwcGVhcmFuY2U6IG5vbmU7IGhlaWdodDogNHB4OwogICAgYm9yZGVyLXJhZGl1czogMnB4OyBiYWNrZ3JvdW5kOiB2YXIoLS1kaW0pOyBvdXRsaW5lOiBub25lOyB9CiAgaW5wdXRbdHlwZT1yYW5nZV06Oi13ZWJraXQtc2xpZGVyLXRodW1iIHsgLXdlYmtpdC1hcHBlYXJhbmNlOiBub25lOyBhcHBlYXJhbmNlOiBub25lOwogICAgd2lkdGg6IDE1cHg7IGhlaWdodDogMTVweDsgYm9yZGVyLXJhZGl1czogNTAlOyBiYWNrZ3JvdW5kOiB2YXIoLS1hY2NlbnQpOyBjdXJzb3I6IHBvaW50ZXI7IH0KICBpbnB1dFt0eXBlPXJhbmdlXTo6LW1vei1yYW5nZS10aHVtYiB7IHdpZHRoOiAxNXB4OyBoZWlnaHQ6IDE1cHg7IGJvcmRlcjogMDsKICAgIGJvcmRlci1yYWRpdXM6IDUwJTsgYmFja2dyb3VuZDogdmFyKC0tYWNjZW50KTsgY3Vyc29yOiBwb2ludGVyOyB9CiAgLmdyaWQgeyBkaXNwbGF5OiBncmlkOyBncmlkLXRlbXBsYXRlLWNvbHVtbnM6IDFmciAyNTBweDsgZ2FwOiAyMHB4OyBhbGlnbi1pdGVtczogc3RhcnQ7IH0KICBAbWVkaWEgKG1heC13aWR0aDogNzAwcHgpIHsgLmdyaWQgeyBncmlkLXRlbXBsYXRlLWNvbHVtbnM6IDFmcjsgfQogICAgLmZvcm11bGEgeyBmb250LXNpemU6IDEzcHg7IH0gLndyYXAgeyBwYWRkaW5nOiAxNHB4IDE0cHggMTZweDsgfSB9CiAgc3ZnIHsgd2lkdGg6IDEwMCU7IGRpc3BsYXk6IGJsb2NrOyB9CiAgLnN1YiB7IGZvbnQtc2l6ZTogMTFweDsgbGV0dGVyLXNwYWNpbmc6IC4xZW07IHRleHQtdHJhbnNmb3JtOiB1cHBlcmNhc2U7CiAgICBjb2xvcjogdmFyKC0tbXV0ZWQpOyBtYXJnaW46IDAgMCA2cHg7IH0KICAubWV0cmljIHsgbWFyZ2luLWJvdHRvbTogMTBweDsgfQogIC5tZXRyaWMtaGVhZCB7IGRpc3BsYXk6IGZsZXg7IGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2VlbjsgZm9udC1zaXplOiAxMnB4OyBjb2xvcjogdmFyKC0tbXV0ZWQpOyB9CiAgLm1ldHJpYy1oZWFkIGIgeyBjb2xvcjogdmFyKC0tdGV4dCk7IGZvbnQtZmFtaWx5OiB1aS1tb25vc3BhY2UsIE1lbmxvLCBtb25vc3BhY2U7IGZvbnQtd2VpZ2h0OiA1MDA7IH0KICAubm90ZSB7IGZvbnQtc2l6ZTogMTFweDsgY29sb3I6IHZhcigtLW11dGVkKTsgbGluZS1oZWlnaHQ6IDEuNTsgbWFyZ2luLXRvcDogMTJweDsgfQo8L3N0eWxlPgo8L2hlYWQ+Cjxib2R5Pgo8ZGl2IGNsYXNzPSJ3cmFwIj4KCiAgPGRpdiBjbGFzcz0idGl0bGUiPk92ZXJmaXR0aW5nIEV4cGxvcmVyPC9kaXY+CiAgPGRpdiBjbGFzcz0iZm9ybXVsYSI+CiAgICA8c3Bhbj48aSBjbGFzcz0ic3dhdGNoIiBzdHlsZT0iYmFja2dyb3VuZDojOGI5N2E4Ij48L2k+dHJ1ZSBjdXJ2ZTwvc3Bhbj4KICAgIDxzcGFuPjxpIGNsYXNzPSJzd2F0Y2giIHN0eWxlPSJiYWNrZ3JvdW5kOnZhcigtLWFjY2VudCkiPjwvaT5maXR0ZWQgcG9seW5vbWlhbDwvc3Bhbj4KICAgIDxzcGFuPjxpIGNsYXNzPSJzd2F0Y2giIHN0eWxlPSJiYWNrZ3JvdW5kOnZhcigtLXRyYWluKSI+PC9pPjEwIHRyYWluaW5nIHBvaW50czwvc3Bhbj4KICA8L2Rpdj4KCiAgPGRpdiBjbGFzcz0icmVhZG91dCIgaWQ9InJlYWRvdXQiPjwvZGl2PgogIDxkaXYgY2xhc3M9InZlcmRpY3QiIGlkPSJ2ZXJkaWN0Ij48L2Rpdj4KCiAgPGRpdiBjbGFzcz0iY29udHJvbCI+CiAgICA8bGFiZWwgZm9yPSJkZWciPmRlZ3JlZTwvbGFiZWw+CiAgICA8aW5wdXQgdHlwZT0icmFuZ2UiIGlkPSJkZWciIG1pbj0iMCIgbWF4PSI5IiBzdGVwPSIxIiB2YWx1ZT0iMSI+CiAgICA8b3V0cHV0IGlkPSJkZWdPdXQiPjE8L291dHB1dD4KICA8L2Rpdj4KCiAgPGRpdiBjbGFzcz0iZ3JpZCI+CiAgICA8ZGl2PgogICAgICA8c3ZnIGlkPSJjaGFydCIgdmlld0JveD0iMCAwIDU2MCAyMzAiIHJvbGU9ImltZyIKICAgICAgICAgICBhcmlhLWxhYmVsPSJGaXR0ZWQgcG9seW5vbWlhbCBhZ2FpbnN0IHRoZSB0cnVlIGN1cnZlIj48L3N2Zz4KICAgIDwvZGl2PgoKICAgIDxkaXY+CiAgICAgIDxkaXYgY2xhc3M9Im1ldHJpYyI+CiAgICAgICAgPGRpdiBjbGFzcz0ibWV0cmljLWhlYWQiPjxzcGFuPnRyYWluIFJNU0U8L3NwYW4+PGIgaWQ9InRyYWluVmFsIj48L2I+PC9kaXY+CiAgICAgIDwvZGl2PgogICAgICA8ZGl2IGNsYXNzPSJtZXRyaWMiPgogICAgICAgIDxkaXYgY2xhc3M9Im1ldHJpYy1oZWFkIj48c3Bhbj50ZXN0IFJNU0U8L3NwYW4+PGIgaWQ9InRlc3RWYWwiPjwvYj48L2Rpdj4KICAgICAgPC9kaXY+CgogICAgICA8ZGl2IGNsYXNzPSJzdWIiPkVycm9yIGFnYWluc3QgZGVncmVlPC9kaXY+CiAgICAgIDxzdmcgaWQ9ImVycnMiIHZpZXdCb3g9IjAgMCAyNTAgMTMwIiByb2xlPSJpbWciCiAgICAgICAgICAgYXJpYS1sYWJlbD0iVHJhaW5pbmcgYW5kIHRlc3QgZXJyb3IgYWNyb3NzIGV2ZXJ5IGRlZ3JlZSI+PC9zdmc+CgogICAgICA8ZGl2IGNsYXNzPSJub3RlIj4KICAgICAgICBUZW4gbm9pc3kgcG9pbnRzIHNhbXBsZWQgZnJvbSBhIHNtb290aCBjdXJ2ZS4gVHJhaW5pbmcgZXJyb3Igb25seSBldmVyCiAgICAgICAgZmFsbHMsIHdoaWNoIGlzIHdoeSBpdCBpcyBubyBldmlkZW5jZSBhdCBhbGwuIFRlc3QgZXJyb3IgZmFsbHMsIGJvdHRvbXMKICAgICAgICBvdXQsIHRoZW4gY2xpbWJzLgogICAgICA8L2Rpdj4KICAgIDwvZGl2PgogIDwvZGl2PgoKPC9kaXY+Cgo8c2NyaXB0PgovLyBQb2ludHMgYW5kIGZpdHRlZCBjb2VmZmljaWVudHMgcHJlY29tcHV0ZWQgd2l0aCB0aGUgbGVzc29uJ3Mgb3duIGNvZGU6Ci8vIHRydWUgY3VydmUgc2luKDIqcGkqeCksIHJhbmRvbS5SYW5kb20oNSksIG5vaXNlIGdhdXNzKDAsIDAuMjApLCBsZWFzdAovLyBzcXVhcmVzIGJ5IEdhdXNzaWFuIGVsaW1pbmF0aW9uLiBFbWJlZGRlZCBzbyB0aGUgd2lkZ2V0J3MgUk1TRSBmaWd1cmVzCi8vIGFyZSB0aGUgbGVzc29uJ3MgZmlndXJlcyByYXRoZXIgdGhhbiBhIHJlLWRlcml2YXRpb24uCmNvbnN0IERBVEEgPSB7InRyYWluIjpbWzAuMCwtMC4yMzU3NjhdLFswLjExMTExMSwwLjQxMzE1NV0sWzAuMjIyMjIyLDEuMTE4NzAyXSxbMC4zMzMzMzMsMC40MDcyNDNdLFswLjQ0NDQ0NCwwLjMxMzM0M10sWzAuNTU1NTU2LC0wLjc5MzIzNl0sWzAuNjY2NjY3LC0wLjY0NTgzMV0sWzAuNzc3Nzc4LC0wLjk0NDIyOF0sWzAuODg4ODg5LC0wLjM3MTUyNF0sWzEuMCwtMC4xMDA4MzddXSwiZml0cyI6W3siZGVncmVlIjowLCJjb2VmIjpbLTAuMDgzODk4MDMxOV0sInRyYWluIjowLjYxMywidGVzdCI6MC43MDJ9LHsiZGVncmVlIjoxLCJjb2VmIjpbMC40MzA0MzM1MTUxLC0xLjAyODY2MzA5MzldLCJ0cmFpbiI6MC41MTgsInRlc3QiOjAuNTI2fSx7ImRlZ3JlZSI6MiwiY29lZiI6WzAuNDU0Mjc0MDM4NSwtMS4xODk1ODY2MjcsMC4xNjA5MjM1MzMxXSwidHJhaW4iOjAuNTE3LCJ0ZXN0IjowLjUyOH0seyJkZWdyZWUiOjMsImNvZWYiOlstMC4yMDU0ODU1MDczLDkuNjcyODgzMDM4MSwtMjguNDY3OTI4MTg3MiwxOS4wODU5MDExNDY5XSwidHJhaW4iOjAuMjM3LCJ0ZXN0IjowLjI4M30seyJkZWdyZWUiOjQsImNvZWYiOlstMC4zMjY5MjAzMTYzLDE0LjIyNjY4ODM3NDgsLTUxLjQ2NDY0NTEzNzUsNTUuOTcxNzI0Mzc0LC0xOC40NDI5MTE2MTM2XSwidHJhaW4iOjAuMjA3LCJ0ZXN0IjowLjI5NH0seyJkZWdyZWUiOjUsImNvZWYiOlstMC4yNjE2MDQwNjA2LDguMjc2Mzc3NDc3NCwtMS44NjUxMTM0Mzk1LC04NC4yMjk2MTg1NTkzLDE0Mi4yNTk1NzEwODg2LC02NC4yODA5OTMwODA5XSwidHJhaW4iOjAuMTg0LCJ0ZXN0IjowLjI3OH0seyJkZWdyZWUiOjYsImNvZWYiOlstMC4yNDk0MDEzODE2LDUuMDIwMDkyNTk0MywzOC4zMDg1NDYyNTk3LC0yNTcuMTQwODE2ODU0LDQ3Ni40MDYyOTE4ODM0LC0zNjEuNTEwMzM5MDQ4LDk5LjA3NjQ0ODY1MDldLCJ0cmFpbiI6MC4xODEsInRlc3QiOjAuMjgxfSx7ImRlZ3JlZSI6NywiY29lZiI6Wy0wLjIzOTE4MzM0MTYsLTYuMDI5OTEzNzYsMjIwLjY0MjI5ODc2NzQsLTEzMzguNDAwNzkzMzYwMywzNTMzLjczNDg0MzQzNTYsLTQ4MTkuOTg2NDMzNDUwMSwzMzM0LjYyMTExNzc0MTgsLTkyNC40NDEzMzE5NjYyXSwidHJhaW4iOjAuMTcsInRlc3QiOjAuMjg5fSx7ImRlZ3JlZSI6OCwiY29lZiI6Wy0wLjIzODE5NjA5MzgsLTEzLjA5NTI0NTMyNTYsMzYzLjEyNDc4OTY1NzgsLTI0MTMuMDg2MDM3NjE2Niw3NTg3LjkyNDYyNzI4MDYsLTEzMjYwLjQxODIzODUxNTIsMTMxODEuNzg5ODY2ODEzMywtNjk1My4zMTkyNjY2MjUxLDE1MDcuMjE5MjkxNzIwNl0sInRyYWluIjowLjE2OSwidGVzdCI6MC4zfSx7ImRlZ3JlZSI6OSwiY29lZiI6Wy0wLjIzNTc2MDc5MjMsLTI2Ny4wMTQ5NDI4NjY0LDYyMjguMTc5MjgxMzQwNiwtNTUyNDEuMzIxMTY2Njg2OSwyNTU3NjUuNzYzOTkwNTg5OCwtNjg5MzgzLjQ4NzQwMjM1MzMsMTEyMDI4NC4wNjI5NTMxMDI2LC0xMDgwNzY2LjUwOTA4NjQ4OSw1Njk2MjkuMDkzNzkxMjQ3MywtMTI2MjQ4LjYzMjQ5NjU1NzhdLCJ0cmFpbiI6MC4wLCJ0ZXN0IjoxLjI4MX1dfTsKCmNvbnN0IE5TID0gImh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIjsKZnVuY3Rpb24gZWwodGFnLCBhdHRycywgdGV4dCkgewogIGNvbnN0IG4gPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50TlMoTlMsIHRhZyk7CiAgZm9yIChjb25zdCBrIGluIGF0dHJzKSBuLnNldEF0dHJpYnV0ZShrLCBhdHRyc1trXSk7CiAgaWYgKHRleHQgIT09IHVuZGVmaW5lZCkgbi50ZXh0Q29udGVudCA9IHRleHQ7CiAgcmV0dXJuIG47Cn0KY29uc3QgYXBwbHlQb2x5ID0gKGNvZWYsIHgpID0+IGNvZWYucmVkdWNlKChzdW0sIGMsIGkpID0+IHN1bSArIGMgKiBNYXRoLnBvdyh4LCBpKSwgMCk7CgovLyAtLS0tIG1haW4gY2hhcnQgLS0tLQpjb25zdCBjaGFydCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJjaGFydCIpOwpjb25zdCBMID0gMzQsIFIgPSA1NDgsIFRPUCA9IDE2LCBCT1QgPSAxOTQ7CmNvbnN0IHhPZiA9IHggPT4gTCArIHggKiAoUiAtIEwpOwpjb25zdCBZTE8gPSAtMi4yLCBZSEkgPSAyLjI7CmNvbnN0IHlPZiA9IHkgPT4gVE9QICsgKChZSEkgLSBNYXRoLm1heChZTE8sIE1hdGgubWluKFlISSwgeSkpKSAvIChZSEkgLSBZTE8pKSAqIChCT1QgLSBUT1ApOwoKZnVuY3Rpb24gY3VydmUoZm4sIHNhbXBsZXMpIHsKICBsZXQgZCA9ICIiLCBwZW4gPSBmYWxzZTsKICBmb3IgKGxldCBpID0gMDsgaSA8PSBzYW1wbGVzOyBpICs9IDEpIHsKICAgIGNvbnN0IHggPSBpIC8gc2FtcGxlcywgeSA9IGZuKHgpOwogICAgLy8gQnJlYWsgdGhlIGxpbmUgd2hlcmUgdGhlIGZpdCBsZWF2ZXMgdGhlIHZpc2libGUgcmFuZ2UgZW50aXJlbHkuCiAgICBpZiAoeSA8IFlMTyB8fCB5ID4gWUhJKSB7IHBlbiA9IGZhbHNlOyBjb250aW51ZTsgfQogICAgZCArPSAocGVuID8gIkwiIDogIk0iKSArIHhPZih4KS50b0ZpeGVkKDEpICsgIiAiICsgeU9mKHkpLnRvRml4ZWQoMSkgKyAiICI7CiAgICBwZW4gPSB0cnVlOwogIH0KICByZXR1cm4gZDsKfQoKZnVuY3Rpb24gZHJhd01haW4oZml0KSB7CiAgY2hhcnQudGV4dENvbnRlbnQgPSAiIjsKICBjaGFydC5hcHBlbmRDaGlsZChlbCgibGluZSIsIHsgeDE6IEwsIHkxOiB5T2YoMCksIHgyOiBSLCB5MjogeU9mKDApLAogICAgc3Ryb2tlOiAidmFyKC0tbGluZSkiLCAic3Ryb2tlLXdpZHRoIjogMSB9KSk7CgogIGNoYXJ0LmFwcGVuZENoaWxkKGVsKCJwYXRoIiwgeyBkOiBjdXJ2ZSh4ID0+IE1hdGguc2luKDIgKiBNYXRoLlBJICogeCksIDIwMCksCiAgICBmaWxsOiAibm9uZSIsIHN0cm9rZTogIiM4Yjk3YTgiLCAic3Ryb2tlLXdpZHRoIjogMS41LCAic3Ryb2tlLWRhc2hhcnJheSI6ICI1IDQiIH0pKTsKICBjaGFydC5hcHBlbmRDaGlsZChlbCgicGF0aCIsIHsgZDogY3VydmUoeCA9PiBhcHBseVBvbHkoZml0LmNvZWYsIHgpLCA0MDApLAogICAgZmlsbDogIm5vbmUiLCBzdHJva2U6ICJ2YXIoLS1hY2NlbnQpIiwgInN0cm9rZS13aWR0aCI6IDIuMiB9KSk7CgogIGZvciAoY29uc3QgW3gsIHldIG9mIERBVEEudHJhaW4pIHsKICAgIGNoYXJ0LmFwcGVuZENoaWxkKGVsKCJjaXJjbGUiLCB7IGN4OiB4T2YoeCksIGN5OiB5T2YoeSksIHI6IDQsCiAgICAgIGZpbGw6ICJ2YXIoLS10cmFpbikiLCBzdHJva2U6ICIjMTIxNjFkIiwgInN0cm9rZS13aWR0aCI6IDEuNSB9KSk7CiAgfQogIGZvciAoY29uc3QgdCBvZiBbLTIsIC0xLCAwLCAxLCAyXSkgewogICAgY2hhcnQuYXBwZW5kQ2hpbGQoZWwoInRleHQiLCB7IHg6IEwgLSA2LCB5OiB5T2YodCkgKyAzLCBmaWxsOiAidmFyKC0tbXV0ZWQpIiwKICAgICAgImZvbnQtc2l6ZSI6ICIxMHB4IiwgInRleHQtYW5jaG9yIjogImVuZCIgfSwgdCkpOwogIH0KICBjaGFydC5hcHBlbmRDaGlsZChlbCgidGV4dCIsIHsgeDogKEwgKyBSKSAvIDIsIHk6IDIxNiwgZmlsbDogInZhcigtLW11dGVkKSIsCiAgICAiZm9udC1zaXplIjogIjEwcHgiLCAidGV4dC1hbmNob3IiOiAibWlkZGxlIiB9LCAieCIpKTsKfQoKLy8gLS0tLSBlcnJvci1hZ2FpbnN0LWRlZ3JlZSBjaGFydCAtLS0tCmNvbnN0IGVycnMgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgiZXJycyIpOwpjb25zdCBFTCA9IDMwLCBFUiA9IDI0MiwgRVQgPSAxMCwgRUIgPSAxMDA7CmNvbnN0IGVYID0gZCA9PiBFTCArIChkIC8gOSkgKiAoRVIgLSBFTCk7CmNvbnN0IEVNQVggPSAxLjQ7CmNvbnN0IGVZID0gdiA9PiBFQiAtIChNYXRoLm1pbih2LCBFTUFYKSAvIEVNQVgpICogKEVCIC0gRVQpOwoKZnVuY3Rpb24gZHJhd0Vycm9ycyhkZWdyZWUpIHsKICBlcnJzLnRleHRDb250ZW50ID0gIiI7CiAgZXJycy5hcHBlbmRDaGlsZChlbCgibGluZSIsIHsgeDE6IEVMLCB5MTogRUIsIHgyOiBFUiwgeTI6IEVCLAogICAgc3Ryb2tlOiAidmFyKC0tbGluZSkiLCAic3Ryb2tlLXdpZHRoIjogMSB9KSk7CgogIGZvciAoY29uc3Qga2V5IG9mIFsidHJhaW4iLCAidGVzdCJdKSB7CiAgICBjb25zdCBjb2xvdXIgPSBrZXkgPT09ICJ0cmFpbiIgPyAidmFyKC0tdHJhaW4pIiA6ICJ2YXIoLS10ZXN0KSI7CiAgICBsZXQgZCA9ICIiOwogICAgREFUQS5maXRzLmZvckVhY2goKGYsIGkpID0+IHsKICAgICAgZCArPSAoaSA/ICJMIiA6ICJNIikgKyBlWChmLmRlZ3JlZSkudG9GaXhlZCgxKSArICIgIiArIGVZKGZba2V5XSkudG9GaXhlZCgxKSArICIgIjsKICAgIH0pOwogICAgZXJycy5hcHBlbmRDaGlsZChlbCgicGF0aCIsIHsgZDogZCwgZmlsbDogIm5vbmUiLCBzdHJva2U6IGNvbG91ciwgInN0cm9rZS13aWR0aCI6IDIgfSkpOwogICAgY29uc3QgaGVyZSA9IERBVEEuZml0c1tkZWdyZWVdOwogICAgZXJycy5hcHBlbmRDaGlsZChlbCgiY2lyY2xlIiwgeyBjeDogZVgoZGVncmVlKSwgY3k6IGVZKGhlcmVba2V5XSksIHI6IDMuNSwgZmlsbDogY29sb3VyIH0pKTsKICB9CgogIGVycnMuYXBwZW5kQ2hpbGQoZWwoImxpbmUiLCB7IHgxOiBlWChkZWdyZWUpLCB5MTogRVQgLSA0LCB4MjogZVgoZGVncmVlKSwgeTI6IEVCLAogICAgc3Ryb2tlOiAiI2ZmZmZmZiIsICJzdHJva2Utd2lkdGgiOiAxLCAic3Ryb2tlLWRhc2hhcnJheSI6ICIzIDMiIH0pKTsKICBmb3IgKGNvbnN0IHQgb2YgWzAsIDMsIDYsIDldKSB7CiAgICBlcnJzLmFwcGVuZENoaWxkKGVsKCJ0ZXh0IiwgeyB4OiBlWCh0KSwgeTogRUIgKyAxNCwgZmlsbDogInZhcigtLW11dGVkKSIsCiAgICAgICJmb250LXNpemUiOiAiOXB4IiwgInRleHQtYW5jaG9yIjogIm1pZGRsZSIgfSwgdCkpOwogIH0KICBlcnJzLmFwcGVuZENoaWxkKGVsKCJ0ZXh0IiwgeyB4OiAoRUwgKyBFUikgLyAyLCB5OiBFQiArIDI2LCBmaWxsOiAidmFyKC0tbXV0ZWQpIiwKICAgICJmb250LXNpemUiOiAiOXB4IiwgInRleHQtYW5jaG9yIjogIm1pZGRsZSIgfSwgImRlZ3JlZSIpKTsKICBlcnJzLmFwcGVuZENoaWxkKGVsKCJ0ZXh0IiwgeyB4OiBFTCAtIDQsIHk6IGVZKDApICsgMywgZmlsbDogInZhcigtLW11dGVkKSIsCiAgICAiZm9udC1zaXplIjogIjlweCIsICJ0ZXh0LWFuY2hvciI6ICJlbmQiIH0sICIwIikpOwogIGVycnMuYXBwZW5kQ2hpbGQoZWwoInRleHQiLCB7IHg6IEVMIC0gNCwgeTogZVkoRU1BWCkgKyA4LCBmaWxsOiAidmFyKC0tbXV0ZWQpIiwKICAgICJmb250LXNpemUiOiAiOXB4IiwgInRleHQtYW5jaG9yIjogImVuZCIgfSwgRU1BWC50b0ZpeGVkKDEpKSk7Cn0KCmZ1bmN0aW9uIHZlcmRpY3RGb3IoZml0KSB7CiAgaWYgKGZpdC5kZWdyZWUgPD0gMikgewogICAgcmV0dXJuICJUb28gcmlnaWQgdG8gZm9sbG93IGEgY3VydmUgdGhhdCByaXNlcyBhbmQgZmFsbHMuIFdyb25nIG9uIHRoZSAiICsKICAgICAgICAgICAidHJhaW5pbmcgcG9pbnRzIGFuZCBlcXVhbGx5IHdyb25nIG9uIG5ldyBvbmVzOiB0aGlzIGlzIHVuZGVyZml0dGluZy4iOwogIH0KICBpZiAoZml0LmRlZ3JlZSA9PT0gOSkgewogICAgcmV0dXJuICJUcmFpbmluZyBlcnJvciBpcyBleGFjdGx5IDAuMDAwIGFuZCB0aGUgdGVzdCBlcnJvciBpcyB0aGUgd29yc3Qgb24gIiArCiAgICAgICAgICAgInRoZSBjaGFydC4gVGVuIHBvaW50cyBhbmQgdGVuIGNvZWZmaWNpZW50czogdGhlIGN1cnZlIHBhc3NlcyB0aHJvdWdoICIgKwogICAgICAgICAgICJldmVyeSBwb2ludCBhbmQgbWVhbnMgbm90aGluZyBiZXR3ZWVuIHRoZW0uIjsKICB9CiAgaWYgKGZpdC5kZWdyZWUgPT09IDUpIHsKICAgIHJldHVybiAiTG93ZXN0IHRlc3QgZXJyb3Igb2YgYW55IGRlZ3JlZS4gSXQgZml0cyB0aGUgdHJhaW5pbmcgcG9pbnRzIGxlc3MgIiArCiAgICAgICAgICAgImV4YWN0bHkgdGhhbiBkZWdyZWUgOSBhbmQgdHJhY2tzIHRoZSB0cnV0aCBmYXIgYmV0dGVyLiI7CiAgfQogIHJldHVybiAiVHJhaW5pbmcgZXJyb3Iga2VlcHMgZmFsbGluZyB3aGlsZSB0ZXN0IGVycm9yIGhhcyBzdG9wcGVkIGltcHJvdmluZy4gIiArCiAgICAgICAgICJUaGUgZXh0cmEgZmxleGliaWxpdHkgaXMgYmVpbmcgc3BlbnQgb24gdGhlIG5vaXNlLiI7Cn0KCmZ1bmN0aW9uIHVwZGF0ZSgpIHsKICBjb25zdCBkZWdyZWUgPSBwYXJzZUludChkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgiZGVnIikudmFsdWUsIDEwKTsKICBjb25zdCBmaXQgPSBEQVRBLmZpdHNbZGVncmVlXTsKICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgiZGVnT3V0IikudGV4dENvbnRlbnQgPSBkZWdyZWU7CiAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoInJlYWRvdXQiKS50ZXh0Q29udGVudCA9CiAgICAiZGVncmVlICIgKyBkZWdyZWUgKyAiICAg4oaSICAgdHJhaW4gUk1TRSAiICsgZml0LnRyYWluLnRvRml4ZWQoMykgKwogICAgIiwgIHRlc3QgUk1TRSAiICsgZml0LnRlc3QudG9GaXhlZCgzKTsKICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgidmVyZGljdCIpLnRleHRDb250ZW50ID0gdmVyZGljdEZvcihmaXQpOwogIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJ0cmFpblZhbCIpLnRleHRDb250ZW50ID0gZml0LnRyYWluLnRvRml4ZWQoMyk7CiAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoInRlc3RWYWwiKS50ZXh0Q29udGVudCA9IGZpdC50ZXN0LnRvRml4ZWQoMyk7CiAgZHJhd01haW4oZml0KTsKICBkcmF3RXJyb3JzKGRlZ3JlZSk7Cn0KCmRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJkZWciKS5hZGRFdmVudExpc3RlbmVyKCJpbnB1dCIsIHVwZGF0ZSk7CnVwZGF0ZSgpOwo8L3NjcmlwdD4KPC9ib2R5Pgo8L2h0bWw+Cg=="
 width="100%"></iframe>

Read the two columns against each other, because their shapes are completely different.

**Training error falls all the way down**, from 0.613 to exactly 0.000. More flexibility always fits the training points better, without exception. This is why training error is not evidence of anything.

**Test error falls and then rises.** It bottoms out around degree 5 at 0.278 and then climbs, reaching 1.281 at degree 9, which is worse than the flat line at degree 0.

The bottom row is the whole lesson in two numbers. **A training error of exactly zero, paired with the worst test error in the table.** With ten points and ten coefficients, the polynomial can pass through every single point precisely, and it purchases that perfection by contorting itself into shapes that have nothing to do with the underlying curve. This is Arun's 100 and 34.

The top rows are the opposite failure. Degrees 0, 1, and 2 cannot bend enough to follow a curve that goes up and comes back down, so they are wrong on the training data and equally wrong on new data. This is Nikita's 71 and 68.

![Visual explanation of watching it happen](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_section_watching_it_happen_simple_v2.png)

## What the Overfitted Curve Actually Does

Error numbers say a model is bad without saying how. Looking at the predictions between the training points shows the mechanism.

Reading the code below: everything above `simple = ...` is repeated from the previous block. The two fits are the same data at degree 5 and degree 9, and the loop deliberately asks both for values at the midpoints between training points, which is exactly where nothing constrained them.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzk6wb" 
 width="100%"
></iframe>

```
What the two curves do BETWEEN the training points

     x     true   degree 5   degree 9
--------------------------------------
 0.056    0.342      0.179     -3.216
 0.167    0.866      0.778      1.692
 0.278    0.985      0.829      0.483
 0.389    0.643      0.403      0.517
 0.500    0.000     -0.236     -0.253
 0.611   -0.643     -0.761     -0.912
 0.722   -0.985     -0.914     -0.509
 0.833   -0.866     -0.632     -1.455
 0.944   -0.342     -0.183      2.867

Degree 9 is worst at x = 0.056, where it predicts -3.22 instead of 0.34
```

| In the code | What it is | Why it is there |
| --- | --- | --- |
| `x = (step - 0.5) / 9` | Halfway between two training points | The gaps are where an overfitted model runs loose |
| `true_curve(x)` | The right answer | Available only because the data was simulated |
| `apply(simple, x)` | Degree 5's guess | Fits the training points less exactly, tracks the truth better |
| `apply(complex_, x)` | Degree 9's guess | Perfect on the training points, unhinged between them |
| `max(..., key=lambda x: abs(...))` | Finds the worst gap | Picks out the single most damning point |

The degree 9 column is not slightly wrong, it is wild. Asked for a value the true curve puts at 0.34, it answers minus 3.22. At the other end it answers 2.87 where the truth is minus 0.34, a prediction of the wrong sign and eight times the magnitude.

Both curves pass through the ten training points reasonably. Between them, the flexible one swings violently, because nothing constrained it there. **Overfitting is not being wrong about the training data; it is being unconstrained everywhere else.** The degree 5 column, by contrast, tracks the truth reasonably at every intermediate point despite fitting the training points less exactly.

This also explains why overfitting worsens near the edges of the data, where there is least to constrain the model, and why extrapolating beyond the range of the training data is dangerous for any flexible model.

![Visual explanation of what the overfitted curve actually does](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_section_what_the_overfitted_curve_actually_does_simple_v2.png)

## More Data Fixes Overfitting

Two remedies exist. Reducing flexibility is the one the table above suggests. The other is to leave the model alone and give it more to learn from.

Reading the code below: the helper functions are identical yet again. Only the final loop is new, and it holds the degree fixed at 9 while varying `n`, the number of training points, from 10 to 200. The test set is built once outside the loop so all five rows are judged against the same thirty points.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzk77y" 
 width="100%"
></iframe>

```
The same over-flexible model (degree 9), given more data to learn from

 training points  train RMSE  test RMSE
----------------------------------------
              10       0.000      1.352
              15       0.150      0.267
              25       0.162      0.217
              50       0.203      0.218
             200       0.219      0.187
```

| In the code | Fixed or varying | Note |
| --- | --- | --- |
| `fit_polynomial(train, 9)` | Fixed | The model is identical in all five rows |
| `for n in (10, 15, 25, 50, 200)` | Varying | The only thing that changes is how much data |
| `TEST` built before the loop | Fixed | All five rows are scored on the same thirty points |
| `10` versus `9` | The critical pair | Ten points and ten coefficients is exactly enough to memorise |

The model was not changed. It is degree 9 throughout. Test error goes from 1.352 to 0.187, an improvement of more than seven times, purely from having more examples.

Watch the training column while that happens: it rises from 0.000 to 0.219. The model gets *worse* at reproducing its training data and dramatically better at everything else, because with 200 points it can no longer memorise them and is forced to represent the actual pattern instead.

That inverse movement is worth remembering as a sanity check. **When training error rises and test error falls, something has gone right.** The two columns converging towards each other is the visible signature of a model that has stopped memorising.

![Visual explanation of more data fixes overfitting](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_section_more_data_fixes_overfitting_simple_v2.png)

## A Third Remedy: Penalise Complexity

Reducing the degree and gathering more data are blunt instruments. The degree is a whole number, so moving from 5 to 4 is a large jump, and more data is frequently unavailable at any price.

The third remedy keeps the flexible model and discourages it from using its flexibility. Look at what the degree 9 fit had to do to pass through all ten points: its coefficients had to become enormous and alternate in sign, so that huge positive and negative terms nearly cancel near the data and diverge violently away from it. That is the signature of overfitting in the numbers themselves.

`Regularisation` exploits this. Instead of choosing coefficients that minimise the training error alone, it minimises the training error **plus a penalty proportional to the size of the coefficients**. Large coefficients now have to earn their place: a term is only used strongly if it reduces the error by more than the penalty it incurs.

The strength of the penalty is a single dial. Turn it to zero and you have ordinary least squares with all its wildness. Turn it very high and every coefficient is pushed towards zero, giving a flat and useless line, which is underfitting arrived at from the other direction. Somewhere in between the model has enough freedom to follow the real curve and not enough to chase the noise.

Two things make this the preferred approach in practice.

- **It is continuous.** The penalty strength is a real number, so it can be tuned finely by cross-validation, where the polynomial degree could only jump between whole numbers.
- **It scales to models with no notion of degree.** A neural network has no single flexibility knob, and penalising the size of its weights works exactly the same way.

The same instinct appears throughout machine learning under different names. Limiting a decision tree's depth is a crude regulariser. So is stopping training early, before the model has had time to memorise. So is deliberately discarding part of the model at random during training. All of them say the same thing: **give the model less room than it wants.**

![Visual explanation of a third remedy: penalise complexity](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_section_a_third_remedy_penalise_complexity.png)

## Bias and Variance

The two failure modes have formal names worth knowing, because they explain why the test error curve is U-shaped rather than merely descending.

`Bias` is error from the model being too rigid to represent the truth. A straight line fitted to a curve has high bias, and it will be wrong in the same way every time, regardless of which sample it is trained on.

`Variance` is error from the model being too sensitive to the particular training sample. The degree 9 polynomial has high variance: train it on a different ten points from the same source and it will produce a completely different set of wild swings.

Increasing flexibility lowers bias and raises variance. That is the trade, and the total error is the sum of the two, which is exactly why it falls at first and then rises. The best model is not the one that minimises either quantity; it is the one at the point where their sum is smallest, which was degree 5 on this data.

This framing also explains why more data helps overfitting specifically. Extra examples reduce variance, since the model can no longer swing freely between them, and they do nothing whatever about bias, since a straight line remains a straight line however many points it is shown.

![Visual explanation of bias variance remedies](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_bias_variance_remedies.png)

## Your Turn

Change the amount of noise and watch where the best degree moves.

Set the noise from 0.20 down to 0.02 in the first program and rerun. With almost no noise there is much less to memorise, so the best degree should rise. Then set it to 0.60 and rerun; with heavy noise, flexible models have more nonsense to chase, and the best degree should fall. Record the best degree at each noise level, and you will have derived a genuine principle for yourself: **the noisier the data, the simpler the model should be.**

Then diagnose rather than describe. For each of these three situations, say whether it is overfitting or underfitting and what you would do:

1. Training accuracy 0.99, test accuracy 0.62.
2. Training accuracy 0.66, test accuracy 0.64.
3. Training accuracy 0.99, test accuracy 0.97.

The second is the one people get wrong, because the instinct on seeing 0.66 is to gather more data, and more data is precisely what will not help.

Finally, reason about a case with no code. A colleague reports that his model achieves 100 percent on training and 99 percent on test. State two quite different explanations, one happy and one alarming, and describe the single check that would tell you which you are looking at. If your alarming explanation involves the same information appearing in both the features and the label, you have connected this lesson to the one on data.
