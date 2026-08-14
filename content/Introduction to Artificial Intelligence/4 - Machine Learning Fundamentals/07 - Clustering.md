## Introduction

The marketing head of a supermarket chain in Nagpur asks her analytics team a question that sounds simple and turns out to be a different kind of question altogether.

She wants to stop sending the same offer to everybody. Instead she wants to know what kinds of customer the chain actually has, so that each kind can be treated differently. Send the right offer to the right sort of shopper.

The team asks the obvious follow-up: which kinds are there? She does not know. That is what she is asking them.

This is not a supervised problem with missing labels. Nobody has ever written down what type any customer is, and no amount of waiting or data collection will produce that column, because customer type is not a fact recorded anywhere in the world. It is a structure that may or may not exist in the purchasing data, and the task is to find out whether it does and what it looks like.

Discovering groups in data that carries no answers is **clustering**.

**Definition:** `Clustering` is unsupervised learning that partitions examples into groups so that members of a group resemble one another more than they resemble members of other groups, using only the features, with no labels available and therefore no answer key against which the result can be declared correct.

![Opening scene: The marketing head of a supermarket chain in Nagpur asks her analytics team a question that sounds simple and turns out to be a different kind of question altogether.](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_section_introduction.png)

## Similarity Is the Whole Idea

Every clustering method rests on a definition of resemblance, and choosing it is the real modelling decision.

Each customer is described by two numbers: visits per month, and annual spend in rupees. Two customers are similar when those numbers are close, measured as straight-line distance.

That sounds neutral and is not, for a reason that will become the central point of this lesson. Visits range from 1 to 22. Annual spend ranges from 5,000 to 52,000. In a straight-line distance between two customers, a difference of 20,000 rupees swamps a difference of 20 visits entirely. **The feature measured in bigger numbers silently becomes the only feature that matters.**

![Visual explanation of similarity is the whole idea](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_section_similarity_is_the_whole_idea.png)

## k-Means

The most widely used clustering method is `k-means`, and it is a loop of two steps repeated until nothing changes.

1. **Choose k starting points** as the initial centres, called `centroids`.
2. **Assign** every customer to the nearest centroid.
3. **Move** each centroid to the average position of the customers assigned to it.
4. **Repeat** steps 2 and 3 until the assignments stop changing.

The number of groups, k, is supplied by you rather than discovered. That is the method's defining limitation and is discussed below.

Here is k-means with k set to 4, applied to the raw numbers exactly as recorded.

Reading the code below: `k_means` is the four-step loop described above, written literally. Assign, then move, then check whether anything changed. The `while` loop is the algorithm and the rest is reporting.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzk2p6" 
 width="100%"
></iframe>

```
k-means on the raw numbers, settled after 1 rounds

  group 1: 2 customers
     visits 1-1 per month, spend 38000-45000
  group 2: 6 customers
     visits 7-21 per month, spend 19000-26000
  group 3: 1 customers
     visits 2-2 per month, spend 52000-52000
  group 4: 3 customers
     visits 18-22 per month, spend 5000-8000
```

| In the code | Step | What it does |
| --- | --- | --- |
| `random.Random(seed).sample(points, k)` | 1 | Pick k starting centres, which is where the randomness enters |
| `min(range(k), key=lambda i: distance(...))` | 2 | Assign: find the nearest centre for one customer |
| `tuple(sum(vals)/len(vals) for vals in zip(*group))` | 3 | Move: average each feature across the group's members |
| `if moved == centroids` | 4 | Stop when a full pass changes nothing |

The result is a mess, and it is worth diagnosing rather than dismissing.

Group 2 holds six customers whose visits run from 7 to 21 a month. Those are not one kind of shopper. Somebody visiting seven times a month and somebody visiting twenty-one times behave completely differently, and lumping them together is exactly the failure the marketing head wanted to avoid. Meanwhile the algorithm has wasted two of its four groups splitting three big spenders into a pair and a single.

Nothing is wrong with the algorithm. It faithfully minimised distance, and in that distance the visits column was invisible, because a gap of 14 visits counts for nothing beside a gap of several thousand rupees. **The clustering is entirely driven by annual spend, and the visits feature might as well not have been collected.**

![Visual explanation of kmeans steps](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_kmeans_steps.png)

## Scaling Fixes It

The repair is to put both features on a comparable footing before measuring distance. The simplest way is min-max scaling: rescale each column so its smallest value becomes 0 and its largest becomes 1.

Reading the code below: `k_means` is the same algorithm, changed only so that groups hold positions in the list rather than the points themselves, which lets the report print original rupees after clustering on scaled values. The one genuinely new function is `scale`, four lines long, and it is the entire fix.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzk2yx" 
 width="100%"
></iframe>

```
k-means on scaled features, settled after 3 rounds

  group 1: 3 customers, visits 1-2, spend 38000-52000
  group 2: 3 customers, visits 18-21, spend 20000-26000
  group 3: 3 customers, visits 7-9, spend 19000-25000
  group 4: 3 customers, visits 18-22, spend 5000-8000
```

| In the code | What it is | Why it matters |
| --- | --- | --- |
| `lows`, `highs` | The range of each column on its own | Scaling is per column, never across columns |
| `(v - lo) / (hi - lo)` | The scaling formula | Turns every feature into a 0-to-1 number |
| `groups[nearest].append(index)` | Stores positions, not points | Lets the report print original rupees after clustering on scaled values |
| `k_means(scaled, ...)` | Clustering runs on the scaled copy | The raw data is untouched and still available for reporting |

Both runs are below. Switch between raw and scaled to see the same twelve customers regrouped, and step through the rounds to watch the centres move to the average of their members.

<iframe
 frameBorder="0"
 height="520px" data-visualizer="kmeans_explorer.html" src="data:text/html;base64,PCFkb2N0eXBlIGh0bWw+CjxodG1sIGxhbmc9ImVuIj4KPGhlYWQ+CjxtZXRhIGNoYXJzZXQ9InV0Zi04Ij4KPG1ldGEgbmFtZT0idmlld3BvcnQiIGNvbnRlbnQ9IndpZHRoPWRldmljZS13aWR0aCwgaW5pdGlhbC1zY2FsZT0xIj4KPHRpdGxlPmstbWVhbnMgRXhwbG9yZXI8L3RpdGxlPgo8c3R5bGU+CiAgOnJvb3QgewogICAgLS1iZzogIzEyMTYxZDsgLS1saW5lOiAjMmMzNTQyOyAtLXRleHQ6ICNlNmViZjI7IC0tbXV0ZWQ6ICM4Yjk3YTg7CiAgICAtLWFjY2VudDogI2YyOTk0YTsgLS1kaW06ICMzYTQ0NTM7CiAgfQogICogeyBib3gtc2l6aW5nOiBib3JkZXItYm94OyB9CiAgaHRtbCwgYm9keSB7IG1hcmdpbjogMDsgYmFja2dyb3VuZDogdmFyKC0tYmcpOyBjb2xvcjogdmFyKC0tdGV4dCk7CiAgICBmb250LWZhbWlseTogSW50ZXIsIHVpLXNhbnMtc2VyaWYsIHN5c3RlbS11aSwgLWFwcGxlLXN5c3RlbSwgIlNlZ29lIFVJIiwgc2Fucy1zZXJpZjsgfQogIC53cmFwIHsgcGFkZGluZzogMThweCAyMHB4IDIwcHg7IG1heC13aWR0aDogOTAwcHg7IG1hcmdpbjogMCBhdXRvOyB9CiAgLnRpdGxlIHsgZm9udC1zaXplOiAxMXB4OyBsZXR0ZXItc3BhY2luZzogLjE4ZW07IHRleHQtdHJhbnNmb3JtOiB1cHBlcmNhc2U7CiAgICBjb2xvcjogdmFyKC0tbXV0ZWQpOyB0ZXh0LWFsaWduOiBjZW50ZXI7IH0KICAuZm9ybXVsYSB7IHRleHQtYWxpZ246IGNlbnRlcjsgZm9udC1mYW1pbHk6IHVpLW1vbm9zcGFjZSwgTWVubG8sIG1vbm9zcGFjZTsKICAgIGZvbnQtc2l6ZTogMTRweDsgbWFyZ2luOiA2cHggMCAxNHB4OwogICAgZGlzcGxheTogZmxleDsgZmxleC13cmFwOiB3cmFwOyBqdXN0aWZ5LWNvbnRlbnQ6IGNlbnRlcjsgZ2FwOiA0cHggMThweDsgfQogIC5mb3JtdWxhIHNwYW4geyB3aGl0ZS1zcGFjZTogbm93cmFwOyB9CiAgLnJlYWRvdXQgeyBiYWNrZ3JvdW5kOiAjMGQxMTE3OyBib3JkZXI6IDFweCBzb2xpZCB2YXIoLS1saW5lKTsgYm9yZGVyLXJhZGl1czogNnB4OwogICAgcGFkZGluZzogOXB4IDEycHg7IGZvbnQtZmFtaWx5OiB1aS1tb25vc3BhY2UsIE1lbmxvLCBtb25vc3BhY2U7CiAgICBmb250LXNpemU6IDEzcHg7IHRleHQtYWxpZ246IGNlbnRlcjsgfQogIC52ZXJkaWN0IHsgdGV4dC1hbGlnbjogY2VudGVyOyBmb250LXNpemU6IDEzcHg7IGxpbmUtaGVpZ2h0OiAxLjU7CiAgICBtYXJnaW46IDEwcHggMCAxNHB4OyBtaW4taGVpZ2h0OiAzOHB4OyBjb2xvcjogdmFyKC0tYWNjZW50KTsgfQogIC5jb250cm9scyB7IGRpc3BsYXk6IGZsZXg7IGZsZXgtd3JhcDogd3JhcDsgYWxpZ24taXRlbXM6IGNlbnRlcjsKICAgIGdhcDogMTBweCAxNHB4OyBtYXJnaW4tYm90dG9tOiAxNnB4OyB9CiAgLmNvbnRyb2xzIGxhYmVsIHsgZm9udC1mYW1pbHk6IHVpLW1vbm9zcGFjZSwgTWVubG8sIG1vbm9zcGFjZTsgZm9udC1zaXplOiAxM3B4OwogICAgY29sb3I6IHZhcigtLW11dGVkKTsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgfQogIC5jb250cm9scyBvdXRwdXQgeyBmb250LWZhbWlseTogdWktbW9ub3NwYWNlLCBNZW5sbywgbW9ub3NwYWNlOyBmb250LXNpemU6IDEzcHg7CiAgICB3aWR0aDogMTZweDsgdGV4dC1hbGlnbjogcmlnaHQ7IGNvbG9yOiB2YXIoLS1hY2NlbnQpOyB9CiAgaW5wdXRbdHlwZT1yYW5nZV0geyBmbGV4OiAxOyBtaW4td2lkdGg6IDEzMHB4OyAtd2Via2l0LWFwcGVhcmFuY2U6IG5vbmU7IGFwcGVhcmFuY2U6IG5vbmU7CiAgICBoZWlnaHQ6IDRweDsgYm9yZGVyLXJhZGl1czogMnB4OyBiYWNrZ3JvdW5kOiB2YXIoLS1kaW0pOyBvdXRsaW5lOiBub25lOyB9CiAgaW5wdXRbdHlwZT1yYW5nZV06Oi13ZWJraXQtc2xpZGVyLXRodW1iIHsgLXdlYmtpdC1hcHBlYXJhbmNlOiBub25lOyBhcHBlYXJhbmNlOiBub25lOwogICAgd2lkdGg6IDE1cHg7IGhlaWdodDogMTVweDsgYm9yZGVyLXJhZGl1czogNTAlOyBiYWNrZ3JvdW5kOiB2YXIoLS1hY2NlbnQpOyBjdXJzb3I6IHBvaW50ZXI7IH0KICBpbnB1dFt0eXBlPXJhbmdlXTo6LW1vei1yYW5nZS10aHVtYiB7IHdpZHRoOiAxNXB4OyBoZWlnaHQ6IDE1cHg7IGJvcmRlcjogMDsKICAgIGJvcmRlci1yYWRpdXM6IDUwJTsgYmFja2dyb3VuZDogdmFyKC0tYWNjZW50KTsgY3Vyc29yOiBwb2ludGVyOyB9CiAgLnRvZ2dsZSB7IGRpc3BsYXk6IGZsZXg7IGJvcmRlcjogMXB4IHNvbGlkIHZhcigtLWxpbmUpOyBib3JkZXItcmFkaXVzOiA1cHg7IG92ZXJmbG93OiBoaWRkZW47IH0KICAudG9nZ2xlIGJ1dHRvbiB7IGJhY2tncm91bmQ6IHRyYW5zcGFyZW50OyBib3JkZXI6IDA7IGNvbG9yOiB2YXIoLS1tdXRlZCk7IGN1cnNvcjogcG9pbnRlcjsKICAgIGZvbnQtZmFtaWx5OiB1aS1tb25vc3BhY2UsIE1lbmxvLCBtb25vc3BhY2U7IGZvbnQtc2l6ZTogMTJweDsgcGFkZGluZzogNnB4IDExcHg7IH0KICAudG9nZ2xlIGJ1dHRvblthcmlhLXByZXNzZWQ9dHJ1ZV0geyBiYWNrZ3JvdW5kOiB2YXIoLS1hY2NlbnQpOyBjb2xvcjogIzEyMTYxZDsgfQogIC5ncmlkIHsgZGlzcGxheTogZ3JpZDsgZ3JpZC10ZW1wbGF0ZS1jb2x1bW5zOiAxZnIgMjUwcHg7IGdhcDogMjBweDsgYWxpZ24taXRlbXM6IHN0YXJ0OyB9CiAgQG1lZGlhIChtYXgtd2lkdGg6IDcwMHB4KSB7IC5ncmlkIHsgZ3JpZC10ZW1wbGF0ZS1jb2x1bW5zOiAxZnI7IH0KICAgIC5mb3JtdWxhIHsgZm9udC1zaXplOiAxMnB4OyB9IC53cmFwIHsgcGFkZGluZzogMTRweCAxNHB4IDE2cHg7IH0gfQogIHN2ZyB7IHdpZHRoOiAxMDAlOyBkaXNwbGF5OiBibG9jazsgfQogIHRhYmxlIHsgd2lkdGg6IDEwMCU7IGJvcmRlci1jb2xsYXBzZTogY29sbGFwc2U7IGZvbnQtc2l6ZTogMTJweDsgfQogIHRoLCB0ZCB7IHBhZGRpbmc6IDVweCA2cHg7IHRleHQtYWxpZ246IHJpZ2h0OyBib3JkZXItYm90dG9tOiAxcHggc29saWQgdmFyKC0tbGluZSk7IH0KICB0aCB7IGNvbG9yOiB2YXIoLS1tdXRlZCk7IGZvbnQtd2VpZ2h0OiA1MDA7IH0KICB0ZDpmaXJzdC1jaGlsZCwgdGg6Zmlyc3QtY2hpbGQgeyB0ZXh0LWFsaWduOiBsZWZ0OyB9CiAgLm51bSB7IGZvbnQtZmFtaWx5OiB1aS1tb25vc3BhY2UsIE1lbmxvLCBtb25vc3BhY2U7IGZvbnQtdmFyaWFudC1udW1lcmljOiB0YWJ1bGFyLW51bXM7IH0KICAuZG90IHsgZGlzcGxheTogaW5saW5lLWJsb2NrOyB3aWR0aDogOXB4OyBoZWlnaHQ6IDlweDsgYm9yZGVyLXJhZGl1czogNTAlOyBtYXJnaW4tcmlnaHQ6IDZweDsgfQogIC5ub3RlIHsgZm9udC1zaXplOiAxMXB4OyBjb2xvcjogdmFyKC0tbXV0ZWQpOyBsaW5lLWhlaWdodDogMS41OyBtYXJnaW4tdG9wOiAxMnB4OyB9Cjwvc3R5bGU+CjwvaGVhZD4KPGJvZHk+CjxkaXYgY2xhc3M9IndyYXAiPgoKICA8ZGl2IGNsYXNzPSJ0aXRsZSI+ay1tZWFucyBFeHBsb3JlcjwvZGl2PgogIDxkaXYgY2xhc3M9ImZvcm11bGEiPgogICAgPHNwYW4+YXNzaWduIHRvIG5lYXJlc3QgY2VudHJlPC9zcGFuPgogICAgPHNwYW4+bW92ZSBlYWNoIGNlbnRyZSB0byBpdHMgYXZlcmFnZTwvc3Bhbj4KICAgIDxzcGFuPnJlcGVhdDwvc3Bhbj4KICA8L2Rpdj4KCiAgPGRpdiBjbGFzcz0icmVhZG91dCIgaWQ9InJlYWRvdXQiPjwvZGl2PgogIDxkaXYgY2xhc3M9InZlcmRpY3QiIGlkPSJ2ZXJkaWN0Ij48L2Rpdj4KCiAgPGRpdiBjbGFzcz0iY29udHJvbHMiPgogICAgPGRpdiBjbGFzcz0idG9nZ2xlIj4KICAgICAgPGJ1dHRvbiBpZD0iYnRuUmF3IiBhcmlhLXByZXNzZWQ9ImZhbHNlIj5yYXcgbnVtYmVyczwvYnV0dG9uPgogICAgICA8YnV0dG9uIGlkPSJidG5TY2FsZWQiIGFyaWEtcHJlc3NlZD0idHJ1ZSI+c2NhbGVkIDAgdG8gMTwvYnV0dG9uPgogICAgPC9kaXY+CiAgICA8bGFiZWwgZm9yPSJzdGVwIj5yb3VuZDwvbGFiZWw+CiAgICA8aW5wdXQgdHlwZT0icmFuZ2UiIGlkPSJzdGVwIiBtaW49IjAiIG1heD0iMyIgc3RlcD0iMSIgdmFsdWU9IjMiPgogICAgPG91dHB1dCBpZD0ic3RlcE91dCI+Mzwvb3V0cHV0PgogIDwvZGl2PgoKICA8ZGl2IGNsYXNzPSJncmlkIj4KICAgIDxkaXY+CiAgICAgIDxzdmcgaWQ9ImNoYXJ0IiB2aWV3Qm94PSIwIDAgNTYwIDI1MCIgcm9sZT0iaW1nIgogICAgICAgICAgIGFyaWEtbGFiZWw9IkN1c3RvbWVycyBwbG90dGVkIGJ5IHZpc2l0cyBhbmQgYW5udWFsIHNwZW5kLCBjb2xvdXJlZCBieSBjbHVzdGVyIj48L3N2Zz4KICAgIDwvZGl2PgoKICAgIDxkaXY+CiAgICAgIDx0YWJsZT4KICAgICAgICA8dHI+PHRoPmdyb3VwPC90aD48dGg+dmlzaXRzPC90aD48dGg+c3BlbmQ8L3RoPjwvdHI+CiAgICAgICAgPHRib2R5IGlkPSJncm91cHMiPjwvdGJvZHk+CiAgICAgIDwvdGFibGU+CiAgICAgIDxkaXYgY2xhc3M9Im5vdGUiPgogICAgICAgIFR3ZWx2ZSBjdXN0b21lcnMsIGsgc2V0IHRvIDQsIHNhbWUgc3RhcnRpbmcgY2VudHJlcyBpbiBib3RoIG1vZGVzLgogICAgICAgIFRoZSBheGVzIGFsd2F5cyBzaG93IHRoZSBvcmlnaW5hbCB2aXNpdHMgYW5kIHJ1cGVlczsgb25seSB3aGF0IHRoZQogICAgICAgIGFsZ29yaXRobSBtZWFzdXJlcyBkaXN0YW5jZSBvbiBjaGFuZ2VzLgogICAgICA8L2Rpdj4KICAgIDwvZGl2PgogIDwvZGl2PgoKPC9kaXY+Cgo8c2NyaXB0PgovLyBFdmVyeSByb3VuZCBvZiBib3RoIHJ1bnMgd2FzIHJlY29yZGVkIGJ5IGV4ZWN1dGluZyB0aGUgbGVzc29uJ3Mgb3duCi8vIGtfbWVhbnMgKHJhbmRvbS5SYW5kb20oMSkuc2FtcGxlIGZvciB0aGUgc3RhcnRpbmcgY2VudHJlcykgYW5kIGNhcHR1cmluZwovLyB0aGUgYXNzaWdubWVudHMgYW5kIGNlbnRyb2lkcyBhdCBlYWNoIHBhc3MuIFJlcGxheWluZyByZWNvcmRlZCBmcmFtZXMKLy8gYXZvaWRzIHRyeWluZyB0byByZXByb2R1Y2UgUHl0aG9uJ3Mgc2FtcGxlciBpbiBKYXZhU2NyaXB0Lgpjb25zdCBEQVRBID0geyJjdXN0b21lcnMiOltbMSw0NTAwMF0sWzIsNTIwMDBdLFsxLDM4MDAwXSxbMTgsNjAwMF0sWzIyLDgwMDBdLFsyMCw1MDAwXSxbOCwyMjAwMF0sWzksMjUwMDBdLFs3LDE5MDAwXSxbMTksMjMwMDBdLFsyMSwyNjAwMF0sWzE4LDIwMDAwXV0sInJhdyI6W3sic3RlcCI6MCwiY2VudHJvaWRzIjpbWzEuMCwzODAwMC4wXSxbMTkuMCwyMzAwMC4wXSxbMi4wLDUyMDAwLjBdLFsyMi4wLDgwMDAuMF1dLCJncm91cHMiOltbMCwyXSxbNiw3LDgsOSwxMCwxMV0sWzFdLFszLDQsNV1dLCJtb3ZlZCI6dHJ1ZX0seyJzdGVwIjoxLCJjZW50cm9pZHMiOltbMS4wLDQxNTAwLjBdLFsxMy42NjY2NjcsMjI1MDAuMF0sWzIuMCw1MjAwMC4wXSxbMjAuMCw2MzMzLjMzMzMzM11dLCJncm91cHMiOltbMCwyXSxbNiw3LDgsOSwxMCwxMV0sWzFdLFszLDQsNV1dLCJtb3ZlZCI6ZmFsc2V9XSwic2NhbGVkRnJhbWVzIjpbeyJzdGVwIjowLCJjZW50cm9pZHMiOltbMC4wLDAuNzAyMTI4XSxbMC44NTcxNDMsMC4zODI5NzldLFswLjA0NzYxOSwxLjBdLFsxLjAsMC4wNjM4M11dLCJncm91cHMiOltbMCwyLDYsNyw4XSxbOSwxMCwxMV0sWzFdLFszLDQsNV1dLCJtb3ZlZCI6dHJ1ZX0seyJzdGVwIjoxLCJjZW50cm9pZHMiOltbMC4yLDAuNTI3NjZdLFswLjg3MzAxNiwwLjM4Mjk3OV0sWzAuMDQ3NjE5LDEuMF0sWzAuOTA0NzYyLDAuMDI4MzY5XV0sImdyb3VwcyI6W1syLDYsNyw4XSxbOSwxMCwxMV0sWzAsMV0sWzMsNCw1XV0sIm1vdmVkIjp0cnVlfSx7InN0ZXAiOjIsImNlbnRyb2lkcyI6W1swLjI1LDAuNDQ2ODA5XSxbMC44NzMwMTYsMC4zODI5NzldLFswLjAyMzgxLDAuOTI1NTMyXSxbMC45MDQ3NjIsMC4wMjgzNjldXSwiZ3JvdXBzIjpbWzYsNyw4XSxbOSwxMCwxMV0sWzAsMSwyXSxbMyw0LDVdXSwibW92ZWQiOnRydWV9LHsic3RlcCI6MywiY2VudHJvaWRzIjpbWzAuMzMzMzMzLDAuMzYxNzAyXSxbMC44NzMwMTYsMC4zODI5NzldLFswLjAxNTg3MywwLjg1MTA2NF0sWzAuOTA0NzYyLDAuMDI4MzY5XV0sImdyb3VwcyI6W1s2LDcsOF0sWzksMTAsMTFdLFswLDEsMl0sWzMsNCw1XV0sIm1vdmVkIjpmYWxzZX1dfTsKCmNvbnN0IENPTE9VUlMgPSBbIiNmMjk5NGEiLCAiIzViOGRlZiIsICIjNTZjMjg4IiwgIiNjNzdkZmYiXTsKY29uc3QgTlMgPSAiaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciOwpjb25zdCBjaGFydCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJjaGFydCIpOwpmdW5jdGlvbiBlbCh0YWcsIGF0dHJzLCB0ZXh0KSB7CiAgY29uc3QgbiA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnROUyhOUywgdGFnKTsKICBmb3IgKGNvbnN0IGsgaW4gYXR0cnMpIG4uc2V0QXR0cmlidXRlKGssIGF0dHJzW2tdKTsKICBpZiAodGV4dCAhPT0gdW5kZWZpbmVkKSBuLnRleHRDb250ZW50ID0gdGV4dDsKICByZXR1cm4gbjsKfQoKbGV0IHNjYWxlZCA9IHRydWU7CgovLyBBeGVzIGFsd2F5cyBzaG93IHRoZSBvcmlnaW5hbCB1bml0cywgd2hhdGV2ZXIgdGhlIGFsZ29yaXRobSBtZWFzdXJlZCBvbi4KY29uc3QgTCA9IDUyLCBSID0gNTQ2LCBUT1AgPSAxOCwgQk9UID0gMjA2Owpjb25zdCB4T2YgPSB2ID0+IEwgKyAodiAvIDI0KSAqIChSIC0gTCk7CmNvbnN0IHlPZiA9IHYgPT4gQk9UIC0gKHYgLyA1NTAwMCkgKiAoQk9UIC0gVE9QKTsKCmZ1bmN0aW9uIGZyYW1lcygpIHsgcmV0dXJuIHNjYWxlZCA/IERBVEEuc2NhbGVkRnJhbWVzIDogREFUQS5yYXc7IH0KCmZ1bmN0aW9uIGRyYXcoZnJhbWUpIHsKICBjaGFydC50ZXh0Q29udGVudCA9ICIiOwoKICBjaGFydC5hcHBlbmRDaGlsZChlbCgibGluZSIsIHsgeDE6IEwsIHkxOiBCT1QsIHgyOiBSLCB5MjogQk9ULAogICAgc3Ryb2tlOiAidmFyKC0tbGluZSkiLCAic3Ryb2tlLXdpZHRoIjogMSB9KSk7CiAgY2hhcnQuYXBwZW5kQ2hpbGQoZWwoImxpbmUiLCB7IHgxOiBMLCB5MTogVE9QLCB4MjogTCwgeTI6IEJPVCwKICAgIHN0cm9rZTogInZhcigtLWxpbmUpIiwgInN0cm9rZS13aWR0aCI6IDEgfSkpOwogIGZvciAoY29uc3QgdCBvZiBbMCwgMTAsIDIwXSkgewogICAgY2hhcnQuYXBwZW5kQ2hpbGQoZWwoInRleHQiLCB7IHg6IHhPZih0KSwgeTogQk9UICsgMTQsIGZpbGw6ICJ2YXIoLS1tdXRlZCkiLAogICAgICAiZm9udC1zaXplIjogIjEwcHgiLCAidGV4dC1hbmNob3IiOiAibWlkZGxlIiB9LCB0KSk7CiAgfQogIGZvciAoY29uc3QgdCBvZiBbMCwgMjAwMDAsIDQwMDAwXSkgewogICAgY2hhcnQuYXBwZW5kQ2hpbGQoZWwoInRleHQiLCB7IHg6IEwgLSA2LCB5OiB5T2YodCkgKyAzLCBmaWxsOiAidmFyKC0tbXV0ZWQpIiwKICAgICAgImZvbnQtc2l6ZSI6ICIxMHB4IiwgInRleHQtYW5jaG9yIjogImVuZCIgfSwgdCAvIDEwMDAgKyAiayIpKTsKICB9CiAgY2hhcnQuYXBwZW5kQ2hpbGQoZWwoInRleHQiLCB7IHg6IChMICsgUikgLyAyLCB5OiBCT1QgKyAyOCwgZmlsbDogInZhcigtLW11dGVkKSIsCiAgICAiZm9udC1zaXplIjogIjEwcHgiLCAidGV4dC1hbmNob3IiOiAibWlkZGxlIiB9LCAidmlzaXRzIHBlciBtb250aCIpKTsKICBjaGFydC5hcHBlbmRDaGlsZChlbCgidGV4dCIsIHsgeDogMTIsIHk6IChUT1AgKyBCT1QpIC8gMiwKICAgIGZpbGw6ICJ2YXIoLS1tdXRlZCkiLCAiZm9udC1zaXplIjogIjEwcHgiLCAidGV4dC1hbmNob3IiOiAibWlkZGxlIiwKICAgIHRyYW5zZm9ybTogInJvdGF0ZSgtOTAgMTIgIiArICgoVE9QICsgQk9UKSAvIDIpICsgIikiIH0sICJhbm51YWwgc3BlbmQiKSk7CgogIGZyYW1lLmdyb3Vwcy5mb3JFYWNoKChtZW1iZXJzLCBnKSA9PiB7CiAgICBmb3IgKGNvbnN0IGkgb2YgbWVtYmVycykgewogICAgICBjb25zdCBbdmlzaXRzLCBzcGVuZF0gPSBEQVRBLmN1c3RvbWVyc1tpXTsKICAgICAgY2hhcnQuYXBwZW5kQ2hpbGQoZWwoImNpcmNsZSIsIHsgY3g6IHhPZih2aXNpdHMpLCBjeTogeU9mKHNwZW5kKSwgcjogNiwKICAgICAgICBmaWxsOiBDT0xPVVJTW2ddLCBzdHJva2U6ICIjMTIxNjFkIiwgInN0cm9rZS13aWR0aCI6IDEuNSB9KSk7CiAgICB9CiAgfSk7CgogIC8vIENlbnRyb2lkcywgY29udmVydGVkIGJhY2sgaW50byB2aXNpdHMgYW5kIHJ1cGVlcyB3aGVuIHRoZSBydW4gd2FzIHNjYWxlZC4KICBmcmFtZS5jZW50cm9pZHMuZm9yRWFjaCgoYywgZykgPT4gewogICAgY29uc3QgdmlzaXRzID0gc2NhbGVkID8gY1swXSAqIDIxICsgMSA6IGNbMF07CiAgICBjb25zdCBzcGVuZCAgPSBzY2FsZWQgPyBjWzFdICogNDcwMDAgKyA1MDAwIDogY1sxXTsKICAgIGNvbnN0IHggPSB4T2YodmlzaXRzKSwgeSA9IHlPZihzcGVuZCk7CiAgICBjaGFydC5hcHBlbmRDaGlsZChlbCgicGF0aCIsIHsKICAgICAgZDogIk0iICsgKHggLSA2KSArICIgIiArIHkgKyAiIEgiICsgKHggKyA2KSArICIgTSIgKyB4ICsgIiAiICsgKHkgLSA2KSArCiAgICAgICAgICIgViIgKyAoeSArIDYpLAogICAgICBzdHJva2U6IENPTE9VUlNbZ10sICJzdHJva2Utd2lkdGgiOiAyLjUgfSkpOwogIH0pOwp9CgpmdW5jdGlvbiB2ZXJkaWN0Rm9yKGZyYW1lLCBzZXR0bGVkKSB7CiAgY29uc3Qgc2l6ZXMgPSBmcmFtZS5ncm91cHMubWFwKGcgPT4gZy5sZW5ndGgpLnNvcnQoKGEsIGIpID0+IGIgLSBhKTsKICBpZiAoIXNjYWxlZCAmJiBzZXR0bGVkKSB7CiAgICByZXR1cm4gIkdyb3VwcyBvZiAiICsgc2l6ZXMuam9pbigiLCAiKSArICIuIE9uZSBncm91cCBob2xkcyBzaXggY3VzdG9tZXJzICIgKwogICAgICAgICAgICJ3aG9zZSB2aXNpdHMgcnVuIGZyb20gNyB0byAyMSwgd2hpY2ggYXJlIG5vdCBvbmUga2luZCBvZiBzaG9wcGVyLiAiICsKICAgICAgICAgICAiU3BlbmQgaXMgbWVhc3VyZWQgaW4gdGhvdXNhbmRzIGFuZCB2aXNpdHMgaW4gdGVucywgc28gZGlzdGFuY2Ugc2F3ICIgKwogICAgICAgICAgICJzcGVuZCBhbmQgbm90aGluZyBlbHNlLiI7CiAgfQogIGlmIChzY2FsZWQgJiYgc2V0dGxlZCkgewogICAgcmV0dXJuICJGb3VyIGNsZWFuIGdyb3VwcyBvZiB0aHJlZSwgYW5kIGVhY2ggaXMgYSBjdXN0b21lciB0eXBlIHRoZSAiICsKICAgICAgICAgICAibWFya2V0aW5nIGhlYWQgY2FuIGFjdCBvbi4gT25seSB0aGUgc2NhbGluZyBjaGFuZ2VkLiI7CiAgfQogIHJldHVybiAiUm91bmQgIiArIGZyYW1lLnN0ZXAgKyAiOiBldmVyeSBjdXN0b21lciBoYXMgYmVlbiBhc3NpZ25lZCB0byBpdHMgIiArCiAgICAgICAgICJuZWFyZXN0IGNlbnRyZSwgYW5kIHRoZSBjZW50cmVzIGFyZSBhYm91dCB0byBtb3ZlIHRvIHRoZSBhdmVyYWdlIG9mICIgKwogICAgICAgICAidGhlaXIgbWVtYmVycy4iOwp9CgpmdW5jdGlvbiB1cGRhdGUoKSB7CiAgY29uc3QgbGlzdCA9IGZyYW1lcygpOwogIGNvbnN0IHNsaWRlciA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJzdGVwIik7CiAgc2xpZGVyLm1heCA9IGxpc3QubGVuZ3RoIC0gMTsKICBsZXQgc3RlcCA9IE1hdGgubWluKHBhcnNlSW50KHNsaWRlci52YWx1ZSwgMTApLCBsaXN0Lmxlbmd0aCAtIDEpOwogIHNsaWRlci52YWx1ZSA9IHN0ZXA7CiAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoInN0ZXBPdXQiKS50ZXh0Q29udGVudCA9IHN0ZXA7CgogIGNvbnN0IGZyYW1lID0gbGlzdFtzdGVwXTsKICBjb25zdCBzZXR0bGVkID0gc3RlcCA9PT0gbGlzdC5sZW5ndGggLSAxOwogIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJyZWFkb3V0IikudGV4dENvbnRlbnQgPQogICAgKHNjYWxlZCA/ICJzY2FsZWQiIDogInJhdyIpICsgIiBmZWF0dXJlcywgcm91bmQgIiArIGZyYW1lLnN0ZXAgKyAiICAg4oaSICAgIiArCiAgICAiZ3JvdXAgc2l6ZXMgIiArIGZyYW1lLmdyb3Vwcy5tYXAoZyA9PiBnLmxlbmd0aCkuam9pbigiLCAiKSArCiAgICAoc2V0dGxlZCA/ICIgICAoc2V0dGxlZCkiIDogIiIpOwogIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJ2ZXJkaWN0IikudGV4dENvbnRlbnQgPSB2ZXJkaWN0Rm9yKGZyYW1lLCBzZXR0bGVkKTsKCiAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoImdyb3VwcyIpLmlubmVySFRNTCA9IGZyYW1lLmdyb3Vwcy5tYXAoKG1lbWJlcnMsIGcpID0+IHsKICAgIGlmICghbWVtYmVycy5sZW5ndGgpIHJldHVybiAiIjsKICAgIGNvbnN0IHZpc2l0cyA9IG1lbWJlcnMubWFwKGkgPT4gREFUQS5jdXN0b21lcnNbaV1bMF0pOwogICAgY29uc3Qgc3BlbmQgPSBtZW1iZXJzLm1hcChpID0+IERBVEEuY3VzdG9tZXJzW2ldWzFdKTsKICAgIHJldHVybiAnPHRyPjx0ZD48aSBjbGFzcz0iZG90IiBzdHlsZT0iYmFja2dyb3VuZDonICsgQ09MT1VSU1tnXSArICciPjwvaT4nICsKICAgICAgbWVtYmVycy5sZW5ndGggKyAnPC90ZD48dGQgY2xhc3M9Im51bSI+JyArIE1hdGgubWluKC4uLnZpc2l0cykgKyAiLSIgKwogICAgICBNYXRoLm1heCguLi52aXNpdHMpICsgJzwvdGQ+PHRkIGNsYXNzPSJudW0iPicgKyBNYXRoLm1pbiguLi5zcGVuZCkgKyAiLSIgKwogICAgICBNYXRoLm1heCguLi5zcGVuZCkgKyAnPC90ZD48L3RyPic7CiAgfSkuam9pbigiIik7CgogIGRyYXcoZnJhbWUpOwp9CgpmdW5jdGlvbiBzZXRNb2RlKHVzZVNjYWxlZCkgewogIHNjYWxlZCA9IHVzZVNjYWxlZDsKICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgiYnRuUmF3Iikuc2V0QXR0cmlidXRlKCJhcmlhLXByZXNzZWQiLCBTdHJpbmcoIXVzZVNjYWxlZCkpOwogIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJidG5TY2FsZWQiKS5zZXRBdHRyaWJ1dGUoImFyaWEtcHJlc3NlZCIsIFN0cmluZyh1c2VTY2FsZWQpKTsKICAvLyBMYW5kIG9uIHRoZSBzZXR0bGVkIHJvdW5kIHNvIHRoZSB0d28gbW9kZXMgY29tcGFyZSBsaWtlIGZvciBsaWtlLgogIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJzdGVwIikudmFsdWUgPSBmcmFtZXMoKS5sZW5ndGggLSAxOwogIHVwZGF0ZSgpOwp9Cgpkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgiYnRuUmF3IikuYWRkRXZlbnRMaXN0ZW5lcigiY2xpY2siLCAoKSA9PiBzZXRNb2RlKGZhbHNlKSk7CmRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJidG5TY2FsZWQiKS5hZGRFdmVudExpc3RlbmVyKCJjbGljayIsICgpID0+IHNldE1vZGUodHJ1ZSkpOwpkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgic3RlcCIpLmFkZEV2ZW50TGlzdGVuZXIoImlucHV0IiwgdXBkYXRlKTsKdXBkYXRlKCk7Cjwvc2NyaXB0Pgo8L2JvZHk+CjwvaHRtbD4K"
 width="100%"></iframe>

Four clean groups of three, and every one of them is a customer type the marketing head can act on.

- **Group 1** visits once or twice a month and spends a great deal. The monthly bulk shopper.
- **Group 2** visits almost daily and spends a moderate amount in total. The frequent regular.
- **Group 3** visits about weekly and spends a similar total. The steady weekly shopper.
- **Group 4** visits almost daily and spends very little. Small top-up purchases.

Groups 2 and 3 are precisely the pair the unscaled run could not separate. Their annual spends are nearly identical, at 20,000 to 26,000 against 19,000 to 25,000, and they differ by more than double in how often they come through the door. Distance on the raw numbers could not see that difference at all, because the only column it was really measuring was the one they agree on.

Groups 2 and 4 make the opposite point. They visit equally often, 18 to 21 against 18 to 22, and differ roughly fourfold in spend, so the unscaled run separated them without difficulty. One feature was doing all the work, which happened to be enough for one pair and useless for the other.

One scaling step changed a useless answer into a usable one, without touching the algorithm. This is the practical lesson of the whole lesson: **for any method that measures distance, scaling is not preprocessing hygiene, it is part of the model.**

![Visual explanation of clustering scaling k](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_clustering_scaling_k.png)

## Choosing k, and Living With Randomness

Two loose ends remain, and honest treatment of clustering requires both.

The first is that k was chosen as 4 with no justification. The usual approach is to try several values and look at how tightly the groups fit, measured by `inertia`: the total squared distance from each point to its own centroid. Inertia always falls as k rises, reaching zero when every point is its own group, so the number itself is not the answer. What is informative is where it stops falling steeply.

The second is that the starting centroids are random, so the same k can produce different answers on different runs.

Reading the code below: `scale`, `distance` and `k_means` are the same functions compressed onto fewer lines, with one addition. `k_means` now returns `inertia` instead of the groups themselves, so the two loops at the bottom can vary one thing at a time: the first sweeps k from 1 to 6 with the seed fixed, the second fixes k at 4 and varies the seed.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzk3cs" 
 width="100%"
></iframe>

```
How tightly the groups fit, as k increases

  k    inertia        group sizes
----------------------------------
  1      2.810               [12]
  2      0.798             [6, 6]
  3      0.288          [6, 3, 3]
  4      0.098       [3, 3, 3, 3]
  5      0.082    [3, 3, 3, 2, 1]
  6      0.066 [3, 3, 2, 2, 1, 1]

Same k, different starting points:
   seed 1: inertia 0.098, sizes [3, 3, 3, 3]
   seed 2: inertia 0.098, sizes [3, 3, 3, 3]
   seed 3: inertia 0.098, sizes [3, 3, 3, 3]
   seed 4: inertia 0.098, sizes [3, 3, 3, 3]
   seed 5: inertia 0.592, sizes [6, 3, 2, 1]
```

| In the code | What it varies | What the table shows |
| --- | --- | --- |
| `for k in range(1, 7)` with `seed=1` | The number of groups | Where inertia stops falling steeply, the elbow |
| `for seed in (1, 2, 3, 4, 5)` with `k=4` | The starting centroids only | Whether the answer is stable across restarts |
| `inertia` | Total squared distance to own centroid | The single number being compared in both tables |

The first table shows a textbook `elbow`. Inertia collapses from 2.810 to 0.098 as k goes from 1 to 4, and then barely moves, dropping only to 0.082 and 0.066. Beyond four, extra groups are splitting hairs rather than finding structure, and the sizes give it away: k of 5 produces a group of one.

The second table is the caution. Four different starting points reach the same good answer with inertia 0.098, and the fifth lands somewhere quite different at 0.592, with groups of 6, 3, 2, and 1. **k-means finds a local optimum, not the best possible grouping**, and which one depends on where it started. The standard defence is to run it many times from different starts and keep the result with the lowest inertia, which is exactly what library implementations do by default.

![Visual explanation of choosing k, and living with randomness](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_section_choosing_k_and_living_with_randomness.png)

## The Honest Limits

Clustering deserves more scepticism than supervised learning, and three limits explain why.

1. **There is no correct answer to compare against.** Four groups and six groups are both defensible. Nothing in the data settles it, which is why the elbow is read as a hint rather than computed as an answer.
2. **The algorithm always returns something.** Run k-means with k of 4 on entirely random data and it will hand back four neat groups. The output is not evidence that structure exists.
3. **The groups have no meaning until a person supplies it.** The algorithm produced four sets of indices. The names "monthly bulk shopper" and "small top-up" were written above by a human reading the numbers, and a different human might read them differently.

The only real test is the one the marketing head applies: can she act differently towards each group, and does it work? Usefulness is the standard, because correctness is unavailable.

![Visual explanation of the honest limits](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_section_the_honest_limits.png)

## Your Turn

Add a third feature to every customer, the average basket size in rupees, choosing values that fit the four groups you have identified. Rerun the scaled clustering with k of 4 and check whether the same customers stay together. Then remove the scaling step and rerun, and confirm that the largest-numbered feature takes over again.

Then interrogate the elbow. Rerun the k sweep on a deliberately structureless dataset: twelve customers whose visits and spend you generate by pairing values at random. Look for the elbow. There will not be a sharp one, and seeing the difference between a real elbow and a smooth curve is the only way to learn to read the plot honestly.

Finally, take the marketing decision. Given the four groups, write one sentence describing the offer you would send to each. Then answer the harder question: what would you send to a customer who sits exactly between groups 2 and 4, and what does k-means tell you about that customer's membership? It assigns every point to exactly one group with no notion of being between two, and deciding whether that limitation matters for your use is a real modelling judgment rather than a technicality.
