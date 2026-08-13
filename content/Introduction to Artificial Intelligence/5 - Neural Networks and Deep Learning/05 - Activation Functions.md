## Introduction

A doctoral student in 2006 adds a fifth layer to a network that works perfectly well with four, retrains it, and gets a worse result. She checks the mathematics, which is right. She checks the new code against the four-layer version, which is identical apart from the extra layer. She adds a sixth, half expecting the trend to reverse, and it gets worse again.

She is not making a mistake, and she is not alone. Between 1990 and 2010 a great many capable researchers tried to train deep neural networks and mostly failed.

The theory said depth should help. The networks were built correctly, the mathematics was right, and the training procedure was the same one that worked perfectly well on networks two or three layers deep. Add more layers and performance did not improve; it got worse, and the early layers of a deep network would come out of training looking almost exactly as they had gone in, as though the process had never reached them.

Part of what eventually unlocked deep learning was not a new algorithm or more data. It was replacing a smooth S-shaped curve with a function so simple it looks like a mistake: output the input if it is positive, and zero otherwise.

Understanding why that helped means understanding what the activation function is actually for, and what a badly chosen one quietly does to a deep network.

**Definition:** An `activation function` is the rule applied to a neuron's weighted sum to produce its output. It is what prevents stacked layers from collapsing into a single layer, and its shape determines how well a correction can travel back through a deep network during training.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_section_introduction.png)

## The Three Common Choices

Three functions cover most of what you will meet.

- **Sigmoid** squashes any input into the range 0 to 1, following a smooth S.
- **Tanh** does the same into the range −1 to +1, so its output is centred on zero.
- **ReLU**, the rectified linear unit, returns the input unchanged if positive and zero otherwise.

Reading the code below: the three functions at the top are one line each and are the entire subject of the lesson. Everything after `FUNCTIONS` is plotting, a text chart that marks a star wherever the curve passes close to a given height. The table of numbers matters more than the drawing.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjsfa" 
 width="100%"
></iframe>

```
  input   sigmoid      tanh      ReLU
--------------------------------------
     -6    0.0025   -1.0000    0.0000
     -3    0.0474   -0.9951    0.0000
     -1    0.2689   -0.7616    0.0000
   -0.5    0.3775   -0.4621    0.0000
      0    0.5000    0.0000    0.0000
    0.5    0.6225    0.4621    0.5000
      1    0.7311    0.7616    1.0000
      3    0.9526    0.9951    3.0000
      6    0.9975    1.0000    6.0000

The same three, drawn across inputs from -6 to +6

sigmoid, output range 0.0 to 1.0
   1.0 |                  *******
   0.9 |               ***
   0.7 |              *
   0.6 |             *
   0.5 |            *
   0.4 |           *
   0.3 |          *
   0.1 |       ***
   0.0 |*******
       +-------------------------
        -6         0        +6

tanh, output range -1.0 to 1.0
   1.0 |               **********
   0.7 |              *
   0.5 |             *
   0.2 |
   0.0 |            *
  -0.2 |
  -0.5 |           *
  -0.7 |          *
  -1.0 |**********
       +-------------------------
        -6         0        +6

ReLU, output range 0.0 to 6.0
   6.0 |                        *
   5.2 |                      **
   4.5 |                     *
   3.8 |                   **
   3.0 |                  *
   2.2 |                **
   1.5 |               *
   0.8 |             **
   0.0 |*************
       +-------------------------
        -6         0        +6
```

| In the code | The function | Shape to notice |
| --- | --- | --- |
| `1 / (1 + math.exp(-z))` | Sigmoid | Flattens at both ends, never leaves 0 to 1 |
| `math.tanh(z)` | Tanh | Same S, but centred on zero |
| `max(0.0, z)` | ReLU | Exactly zero on the left, a straight ramp on the right |
| The star plot | Not part of any model | Draws each curve so the flattening is visible |

The shapes tell most of the story.

**Sigmoid and tanh flatten out at both ends.** Look at the sigmoid rows for inputs of 3 and 6: the outputs are 0.9526 and 0.9975, barely different despite the input having doubled. The same happens at the negative end. Beyond roughly plus or minus 4, the function has essentially stopped responding.

**ReLU does not flatten on the positive side.** It keeps rising forever, at a constant rate, and it is exactly zero for every negative input.

**Only tanh is centred on zero.** Sigmoid outputs are always positive, which means every neuron in the next layer receives only positive inputs, and that biases how its weights can move during training.

![Visual explanation of activation functions](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_activation_functions.png)

## What Steepness Has to Do With Learning

The shapes matter because of how training works. A network learns by asking, for each weight, whether nudging it up or down would reduce the error. That question is answered by how steep the activation function is at the neuron's current operating point.

Where the function is steep, a small change in the weighted sum produces a noticeable change in the output, so the weight has visible influence and can be adjusted usefully. Where the function is flat, changing the weight barely moves the output, so there is almost nothing to learn from.

Reading the code below: the three `_slope` functions give the steepness of each curve at a point, which is its derivative. You do not need the calculus to read the table; treat each one as a black box answering "how much does the output move if the input moves a little here". The rest is a printed table.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjsrz" 
 width="100%"
></iframe>

```
How steep each function is, which is how much a weight change matters

  input    sigmoid       tanh     ReLU
--------------------------------------
     -8    0.00034    0.00000      0.0
     -4    0.01766    0.00134      0.0
     -2    0.10499    0.07065      0.0
      0    0.25000    1.00000      0.0
      2    0.10499    0.07065      1.0
      4    0.01766    0.00134      1.0
      8    0.00034    0.00000      1.0

Steepest sigmoid slope anywhere: 0.25, at input 0
Sigmoid slope at input 8:        0.00034

A neuron whose total is 8 has essentially stopped responding to change.
It is said to be saturated.
```

| In the code | What it reports | Why it matters |
| --- | --- | --- |
| `sigmoid_slope(z)` | Steepness of sigmoid at z | Peaks at 0.25 and falls away fast |
| `tanh_slope(z)` | Steepness of tanh at z | Peaks at 1.0, but collapses even faster off centre |
| `relu_slope(z)` | Steepness of ReLU at z | Exactly 1 for any positive input, at any size |
| `sigmoid_slope(8)` | 0.00034 | A saturated neuron: still outputs, no longer learns |

Drag z below. The top strip is the output, the bottom strip is the slope, and the right-hand panel carries that slope forward through several layers, which is the subject of the next section.

<iframe
 frameBorder="0"
 height="620px" data-visualizer="activation_explorer.html" src="data:text/html;base64,PCFkb2N0eXBlIGh0bWw+CjxodG1sIGxhbmc9ImVuIj4KPGhlYWQ+CjxtZXRhIGNoYXJzZXQ9InV0Zi04Ij4KPG1ldGEgbmFtZT0idmlld3BvcnQiIGNvbnRlbnQ9IndpZHRoPWRldmljZS13aWR0aCwgaW5pdGlhbC1zY2FsZT0xIj4KPHRpdGxlPkFjdGl2YXRpb24gRXhwbG9yZXI8L3RpdGxlPgo8c3R5bGU+CiAgOnJvb3QgewogICAgLS1iZzogIzEyMTYxZDsgLS1saW5lOiAjMmMzNTQyOyAtLXRleHQ6ICNlNmViZjI7IC0tbXV0ZWQ6ICM4Yjk3YTg7CiAgICAtLWFjY2VudDogI2YyOTk0YTsgLS1kaW06ICMzYTQ0NTM7CiAgICAtLXNpZzogI2YyOTk0YTsgLS10YW5oOiAjNWI4ZGVmOyAtLXJlbHU6ICM1NmMyODg7CiAgfQogICogeyBib3gtc2l6aW5nOiBib3JkZXItYm94OyB9CiAgaHRtbCwgYm9keSB7IG1hcmdpbjogMDsgYmFja2dyb3VuZDogdmFyKC0tYmcpOyBjb2xvcjogdmFyKC0tdGV4dCk7CiAgICBmb250LWZhbWlseTogSW50ZXIsIHVpLXNhbnMtc2VyaWYsIHN5c3RlbS11aSwgLWFwcGxlLXN5c3RlbSwgIlNlZ29lIFVJIiwgc2Fucy1zZXJpZjsgfQogIC53cmFwIHsgcGFkZGluZzogMThweCAyMHB4IDIwcHg7IG1heC13aWR0aDogOTAwcHg7IG1hcmdpbjogMCBhdXRvOyB9CiAgLnRpdGxlIHsgZm9udC1zaXplOiAxMXB4OyBsZXR0ZXItc3BhY2luZzogLjE4ZW07IHRleHQtdHJhbnNmb3JtOiB1cHBlcmNhc2U7CiAgICBjb2xvcjogdmFyKC0tbXV0ZWQpOyB0ZXh0LWFsaWduOiBjZW50ZXI7IH0KICAuZm9ybXVsYSB7IHRleHQtYWxpZ246IGNlbnRlcjsgZm9udC1mYW1pbHk6IHVpLW1vbm9zcGFjZSwgU0ZNb25vLVJlZ3VsYXIsIE1lbmxvLCBtb25vc3BhY2U7CiAgICBmb250LXNpemU6IDE1cHg7IG1hcmdpbjogNnB4IDAgMTRweDsKICAgIGRpc3BsYXk6IGZsZXg7IGZsZXgtd3JhcDogd3JhcDsganVzdGlmeS1jb250ZW50OiBjZW50ZXI7IGdhcDogNHB4IDIwcHg7IH0KICAuZm9ybXVsYSBzcGFuIHsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgfQogIC5zd2F0Y2ggeyBkaXNwbGF5OiBpbmxpbmUtYmxvY2s7IHdpZHRoOiA5cHg7IGhlaWdodDogOXB4OyBib3JkZXItcmFkaXVzOiAycHg7IG1hcmdpbi1yaWdodDogNXB4OyB9CiAgLnJlYWRvdXQgeyBiYWNrZ3JvdW5kOiAjMGQxMTE3OyBib3JkZXI6IDFweCBzb2xpZCB2YXIoLS1saW5lKTsgYm9yZGVyLXJhZGl1czogNnB4OwogICAgcGFkZGluZzogOXB4IDEycHg7IGZvbnQtZmFtaWx5OiB1aS1tb25vc3BhY2UsIE1lbmxvLCBtb25vc3BhY2U7CiAgICBmb250LXNpemU6IDEzcHg7IHRleHQtYWxpZ246IGNlbnRlcjsgfQogIC52ZXJkaWN0IHsgdGV4dC1hbGlnbjogY2VudGVyOyBmb250LXNpemU6IDEzcHg7IGxpbmUtaGVpZ2h0OiAxLjU7CiAgICBtYXJnaW46IDEwcHggMCAxNHB4OyBtaW4taGVpZ2h0OiAzOHB4OyBjb2xvcjogdmFyKC0tYWNjZW50KTsgfQogIC5jb250cm9sIHsgZGlzcGxheTogZmxleDsgYWxpZ24taXRlbXM6IGNlbnRlcjsgZ2FwOiAxMnB4OyBtYXJnaW4tYm90dG9tOiAxNnB4OyB9CiAgLmNvbnRyb2wgbGFiZWwgeyBmb250LWZhbWlseTogdWktbW9ub3NwYWNlLCBNZW5sbywgbW9ub3NwYWNlOyBmb250LXNpemU6IDEzcHg7CiAgICBjb2xvcjogdmFyKC0tbXV0ZWQpOyB3aGl0ZS1zcGFjZTogbm93cmFwOyB9CiAgLmNvbnRyb2wgb3V0cHV0IHsgZm9udC1mYW1pbHk6IHVpLW1vbm9zcGFjZSwgTWVubG8sIG1vbm9zcGFjZTsgZm9udC1zaXplOiAxM3B4OwogICAgd2lkdGg6IDQ2cHg7IHRleHQtYWxpZ246IHJpZ2h0OyBjb2xvcjogdmFyKC0tYWNjZW50KTsgfQogIGlucHV0W3R5cGU9cmFuZ2VdIHsgZmxleDogMTsgLXdlYmtpdC1hcHBlYXJhbmNlOiBub25lOyBhcHBlYXJhbmNlOiBub25lOyBoZWlnaHQ6IDRweDsKICAgIGJvcmRlci1yYWRpdXM6IDJweDsgYmFja2dyb3VuZDogdmFyKC0tZGltKTsgb3V0bGluZTogbm9uZTsgfQogIGlucHV0W3R5cGU9cmFuZ2VdOjotd2Via2l0LXNsaWRlci10aHVtYiB7IC13ZWJraXQtYXBwZWFyYW5jZTogbm9uZTsgYXBwZWFyYW5jZTogbm9uZTsKICAgIHdpZHRoOiAxNXB4OyBoZWlnaHQ6IDE1cHg7IGJvcmRlci1yYWRpdXM6IDUwJTsgYmFja2dyb3VuZDogdmFyKC0tYWNjZW50KTsgY3Vyc29yOiBwb2ludGVyOyB9CiAgaW5wdXRbdHlwZT1yYW5nZV06Oi1tb3otcmFuZ2UtdGh1bWIgeyB3aWR0aDogMTVweDsgaGVpZ2h0OiAxNXB4OyBib3JkZXI6IDA7CiAgICBib3JkZXItcmFkaXVzOiA1MCU7IGJhY2tncm91bmQ6IHZhcigtLWFjY2VudCk7IGN1cnNvcjogcG9pbnRlcjsgfQogIC5ncmlkIHsgZGlzcGxheTogZ3JpZDsgZ3JpZC10ZW1wbGF0ZS1jb2x1bW5zOiAxZnIgMjUwcHg7IGdhcDogMjBweDsgYWxpZ24taXRlbXM6IHN0YXJ0OyB9CiAgQG1lZGlhIChtYXgtd2lkdGg6IDcwMHB4KSB7IC5ncmlkIHsgZ3JpZC10ZW1wbGF0ZS1jb2x1bW5zOiAxZnI7IH0KICAgIC5mb3JtdWxhIHsgZm9udC1zaXplOiAxM3B4OyB9IC53cmFwIHsgcGFkZGluZzogMTRweCAxNHB4IDE2cHg7IH0gfQogIHN2ZyB7IHdpZHRoOiAxMDAlOyBkaXNwbGF5OiBibG9jazsgfQogIHRhYmxlIHsgd2lkdGg6IDEwMCU7IGJvcmRlci1jb2xsYXBzZTogY29sbGFwc2U7IGZvbnQtc2l6ZTogMTJweDsgbWFyZ2luLWJvdHRvbTogMTRweDsgfQogIHRoLCB0ZCB7IHBhZGRpbmc6IDVweCA2cHg7IHRleHQtYWxpZ246IHJpZ2h0OyBib3JkZXItYm90dG9tOiAxcHggc29saWQgdmFyKC0tbGluZSk7IH0KICB0aCB7IGNvbG9yOiB2YXIoLS1tdXRlZCk7IGZvbnQtd2VpZ2h0OiA1MDA7IH0KICB0ZDpmaXJzdC1jaGlsZCwgdGg6Zmlyc3QtY2hpbGQgeyB0ZXh0LWFsaWduOiBsZWZ0OyB9CiAgLm51bSB7IGZvbnQtZmFtaWx5OiB1aS1tb25vc3BhY2UsIE1lbmxvLCBtb25vc3BhY2U7IGZvbnQtdmFyaWFudC1udW1lcmljOiB0YWJ1bGFyLW51bXM7IH0KICAuc3ViIHsgZm9udC1zaXplOiAxMXB4OyBsZXR0ZXItc3BhY2luZzogLjFlbTsgdGV4dC10cmFuc2Zvcm06IHVwcGVyY2FzZTsKICAgIGNvbG9yOiB2YXIoLS1tdXRlZCk7IG1hcmdpbi1ib3R0b206IDZweDsgfQogIC5ub3RlIHsgZm9udC1zaXplOiAxMXB4OyBjb2xvcjogdmFyKC0tbXV0ZWQpOyBsaW5lLWhlaWdodDogMS41OyBtYXJnaW4tdG9wOiAxMHB4OyB9Cjwvc3R5bGU+CjwvaGVhZD4KPGJvZHk+CjxkaXYgY2xhc3M9IndyYXAiPgoKICA8ZGl2IGNsYXNzPSJ0aXRsZSI+QWN0aXZhdGlvbiBFeHBsb3JlcjwvZGl2PgogIDxkaXYgY2xhc3M9ImZvcm11bGEiPgogICAgPHNwYW4+PGkgY2xhc3M9InN3YXRjaCIgc3R5bGU9ImJhY2tncm91bmQ6dmFyKC0tc2lnKSI+PC9pPnNpZ21vaWQ8L3NwYW4+CiAgICA8c3Bhbj48aSBjbGFzcz0ic3dhdGNoIiBzdHlsZT0iYmFja2dyb3VuZDp2YXIoLS10YW5oKSI+PC9pPnRhbmg8L3NwYW4+CiAgICA8c3Bhbj48aSBjbGFzcz0ic3dhdGNoIiBzdHlsZT0iYmFja2dyb3VuZDp2YXIoLS1yZWx1KSI+PC9pPlJlTFU8L3NwYW4+CiAgPC9kaXY+CgogIDxkaXYgY2xhc3M9InJlYWRvdXQiIGlkPSJyZWFkb3V0Ij48L2Rpdj4KICA8ZGl2IGNsYXNzPSJ2ZXJkaWN0IiBpZD0idmVyZGljdCI+PC9kaXY+CgogIDxkaXYgY2xhc3M9ImNvbnRyb2wiPgogICAgPGxhYmVsIGZvcj0ieiI+d2VpZ2h0ZWQgc3VtIHo8L2xhYmVsPgogICAgPGlucHV0IHR5cGU9InJhbmdlIiBpZD0ieiIgbWluPSItOCIgbWF4PSI4IiBzdGVwPSIwLjEiIHZhbHVlPSIwIj4KICAgIDxvdXRwdXQgaWQ9InpPdXQiPjAuMDwvb3V0cHV0PgogIDwvZGl2PgoKICA8ZGl2IGNsYXNzPSJncmlkIj4KICAgIDxkaXY+CiAgICAgIDxzdmcgaWQ9ImNoYXJ0IiB2aWV3Qm94PSIwIDAgNTYwIDI2MCIgcm9sZT0iaW1nIgogICAgICAgICAgIGFyaWEtbGFiZWw9IkFjdGl2YXRpb24gb3V0cHV0cyBhbmQgc2xvcGVzIGFnYWluc3QgdGhlIHdlaWdodGVkIHN1bSI+PC9zdmc+CiAgICA8L2Rpdj4KCiAgICA8ZGl2PgogICAgICA8ZGl2IGNsYXNzPSJzdWIiPkF0IHRoaXMgejwvZGl2PgogICAgICA8dGFibGU+CiAgICAgICAgPHRyPjx0aD48L3RoPjx0aD5vdXRwdXQ8L3RoPjx0aD5zbG9wZTwvdGg+PC90cj4KICAgICAgICA8dGJvZHkgaWQ9Im5vdyI+PC90Ym9keT4KICAgICAgPC90YWJsZT4KCiAgICAgIDxkaXYgY2xhc3M9InN1YiI+Q29ycmVjdGlvbiBsZWZ0IGFmdGVyIE4gbGF5ZXJzPC9kaXY+CiAgICAgIDx0YWJsZT4KICAgICAgICA8dHI+PHRoPmxheWVyczwvdGg+PHRoPnNpZ21vaWQ8L3RoPjx0aD5SZUxVPC90aD48L3RyPgogICAgICAgIDx0Ym9keSBpZD0iZGVjYXkiPjwvdGJvZHk+CiAgICAgIDwvdGFibGU+CgogICAgICA8ZGl2IGNsYXNzPSJub3RlIj4KICAgICAgICBBIGNvcnJlY3Rpb24gaXMgbXVsdGlwbGllZCBieSBlYWNoIGxheWVyJ3Mgc2xvcGUgb24gaXRzIHdheSBiYWNrLgogICAgICAgIFJlTFUncyBzbG9wZSBpcyBleGFjdGx5IDEgd2hlcmV2ZXIgdGhlIG5ldXJvbiBpcyBhY3RpdmUsIGF0IGFueSBzaXplCiAgICAgICAgb2YgaW5wdXQsIHdoaWNoIGlzIHdoeSBkZXB0aCBzdG9wcGVkIGJlaW5nIHNlbGYtZGVmZWF0aW5nLgogICAgICA8L2Rpdj4KICAgIDwvZGl2PgogIDwvZGl2PgoKPC9kaXY+Cgo8c2NyaXB0Pgpjb25zdCBzaWdtb2lkID0geiA9PiAxIC8gKDEgKyBNYXRoLmV4cCgteikpOwpjb25zdCBGVU5DUyA9IFsKICB7IG5hbWU6ICJzaWdtb2lkIiwgY29sb3VyOiAidmFyKC0tc2lnKSIsCiAgICBmOiBzaWdtb2lkLCAgICAgICAgICAgc2xvcGU6IHogPT4gc2lnbW9pZCh6KSAqICgxIC0gc2lnbW9pZCh6KSkgfSwKICB7IG5hbWU6ICJ0YW5oIiwgICAgY29sb3VyOiAidmFyKC0tdGFuaCkiLAogICAgZjogTWF0aC50YW5oLCAgICAgICAgIHNsb3BlOiB6ID0+IDEgLSBNYXRoLnRhbmgoeikgKiogMiB9LAogIHsgbmFtZTogIlJlTFUiLCAgICBjb2xvdXI6ICJ2YXIoLS1yZWx1KSIsCiAgICBmOiB6ID0+IE1hdGgubWF4KDAsIHopLCBzbG9wZTogeiA9PiAoeiA+IDAgPyAxIDogMCkgfQpdOwoKY29uc3QgTlMgPSAiaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciOwpjb25zdCBjaGFydCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJjaGFydCIpOwpmdW5jdGlvbiBlbChuYW1lLCBhdHRycywgdGV4dCkgewogIGNvbnN0IG5vZGUgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50TlMoTlMsIG5hbWUpOwogIGZvciAoY29uc3QgayBpbiBhdHRycykgbm9kZS5zZXRBdHRyaWJ1dGUoaywgYXR0cnNba10pOwogIGlmICh0ZXh0ICE9PSB1bmRlZmluZWQpIG5vZGUudGV4dENvbnRlbnQgPSB0ZXh0OwogIHJldHVybiBub2RlOwp9Cgpjb25zdCBMID0gNDAsIFIgPSA1NDgsIFcgPSBSIC0gTCwgWk1JTiA9IC04LCBaTUFYID0gODsKY29uc3QgeE9mID0geiA9PiBMICsgKCh6IC0gWk1JTikgLyAoWk1BWCAtIFpNSU4pKSAqIFc7Ci8vIFRvcCBzdHJpcDogb3V0cHV0cywgLTEuMSB0byAxLjEuIEJvdHRvbSBzdHJpcDogc2xvcGVzLCAwIHRvIDEuMDUuCmNvbnN0IE9VVCA9IHsgeTogMjIsIGg6IDk2LCBsbzogLTEuMSwgaGk6IDEuMSB9Owpjb25zdCBTTFAgPSB7IHk6IDE1MiwgaDogNzQsIGxvOiAwLCBoaTogMS4wNSB9Owpjb25zdCB5SW4gPSAoc3RyaXAsIHYpID0+IHN0cmlwLnkgKyBzdHJpcC5oIC0gKCh2IC0gc3RyaXAubG8pIC8gKHN0cmlwLmhpIC0gc3RyaXAubG8pKSAqIHN0cmlwLmg7CgpmdW5jdGlvbiBwYXRoKHN0cmlwLCBmbikgewogIGNvbnN0IHB0cyA9IFtdOwogIGZvciAobGV0IGkgPSAwOyBpIDw9IDI2MDsgaSArPSAxKSB7CiAgICBjb25zdCB6ID0gWk1JTiArIChpIC8gMjYwKSAqIChaTUFYIC0gWk1JTik7CiAgICBjb25zdCB2ID0gZm4oeik7CiAgICAvLyBDbGlwIHJhdGhlciB0aGFuIGxldCBSZUxVIHNob290IGZhciBvZmYgdGhlIHRvcCBvZiB0aGUgc3RyaXAuCiAgICBpZiAodiA+IHN0cmlwLmhpKSB7IHB0cy5wdXNoKG51bGwpOyBjb250aW51ZTsgfQogICAgcHRzLnB1c2goW3hPZih6KSwgeUluKHN0cmlwLCBNYXRoLm1heChzdHJpcC5sbywgdikpXSk7CiAgfQogIGxldCBkID0gIiIsIHBlbiA9IGZhbHNlOwogIGZvciAoY29uc3QgcCBvZiBwdHMpIHsKICAgIGlmICghcCkgeyBwZW4gPSBmYWxzZTsgY29udGludWU7IH0KICAgIGQgKz0gKHBlbiA/ICJMIiA6ICJNIikgKyBwWzBdLnRvRml4ZWQoMSkgKyAiICIgKyBwWzFdLnRvRml4ZWQoMSkgKyAiICI7CiAgICBwZW4gPSB0cnVlOwogIH0KICByZXR1cm4gZDsKfQoKZnVuY3Rpb24gZHJhdyh6KSB7CiAgY2hhcnQudGV4dENvbnRlbnQgPSAiIjsKCiAgZm9yIChjb25zdCBzdHJpcCBvZiBbT1VULCBTTFBdKSB7CiAgICBjb25zdCB6ZXJvWSA9IHlJbihzdHJpcCwgTWF0aC5taW4oTWF0aC5tYXgoMCwgc3RyaXAubG8pLCBzdHJpcC5oaSkpOwogICAgY2hhcnQuYXBwZW5kQ2hpbGQoZWwoImxpbmUiLCB7IHgxOiBMLCB5MTogemVyb1ksIHgyOiBSLCB5MjogemVyb1ksCiAgICAgIHN0cm9rZTogInZhcigtLWxpbmUpIiwgInN0cm9rZS13aWR0aCI6IDEgfSkpOwogIH0KICBjaGFydC5hcHBlbmRDaGlsZChlbCgidGV4dCIsIHsgeDogTCwgeTogT1VULnkgLSA3LCBmaWxsOiAidmFyKC0tbXV0ZWQpIiwKICAgICJmb250LXNpemUiOiAiMTFweCIgfSwgIm91dHB1dCwgd2l0aCBSZUxVIGNsaXBwZWQgYXQgdGhlIHRvcCBiZWNhdXNlIGl0IGtlZXBzIHJpc2luZyIpKTsKICBjaGFydC5hcHBlbmRDaGlsZChlbCgidGV4dCIsIHsgeDogTCwgeTogU0xQLnkgLSA3LCBmaWxsOiAidmFyKC0tbXV0ZWQpIiwKICAgICJmb250LXNpemUiOiAiMTFweCIgfSwgInNsb3BlLCB3aGljaCBpcyBob3cgbXVjaCBhIHdlaWdodCBjaGFuZ2UgbWF0dGVycyIpKTsKCiAgZm9yIChjb25zdCBmbiBvZiBGVU5DUykgewogICAgY2hhcnQuYXBwZW5kQ2hpbGQoZWwoInBhdGgiLCB7IGQ6IHBhdGgoT1VULCBmbi5mKSwgZmlsbDogIm5vbmUiLAogICAgICBzdHJva2U6IGZuLmNvbG91ciwgInN0cm9rZS13aWR0aCI6IDIgfSkpOwogICAgY2hhcnQuYXBwZW5kQ2hpbGQoZWwoInBhdGgiLCB7IGQ6IHBhdGgoU0xQLCBmbi5zbG9wZSksIGZpbGw6ICJub25lIiwKICAgICAgc3Ryb2tlOiBmbi5jb2xvdXIsICJzdHJva2Utd2lkdGgiOiAyIH0pKTsKICB9CiAgY29uc3QgeCA9IHhPZih6KTsKICBjaGFydC5hcHBlbmRDaGlsZChlbCgibGluZSIsIHsgeDE6IHgsIHkxOiBPVVQueSAtIDQsIHgyOiB4LCB5MjogU0xQLnkgKyBTTFAuaCwKICAgIHN0cm9rZTogIiNmZmZmZmYiLCAic3Ryb2tlLXdpZHRoIjogMS41LCAic3Ryb2tlLWRhc2hhcnJheSI6ICI0IDMiIH0pKTsKICBmb3IgKGNvbnN0IGZuIG9mIEZVTkNTKSB7CiAgICBjb25zdCBvdXQgPSBmbi5mKHopOwogICAgaWYgKG91dCA8PSBPVVQuaGkpIHsKICAgICAgY2hhcnQuYXBwZW5kQ2hpbGQoZWwoImNpcmNsZSIsIHsgY3g6IHgsIGN5OiB5SW4oT1VULCBvdXQpLCByOiAzLjUsIGZpbGw6IGZuLmNvbG91ciB9KSk7CiAgICB9CiAgICBjaGFydC5hcHBlbmRDaGlsZChlbCgiY2lyY2xlIiwgeyBjeDogeCwgY3k6IHlJbihTTFAsIGZuLnNsb3BlKHopKSwgcjogMy41LCBmaWxsOiBmbi5jb2xvdXIgfSkpOwogIH0KCiAgZm9yIChjb25zdCB0aWNrIG9mIFstOCwgLTQsIDAsIDQsIDhdKSB7CiAgICBjaGFydC5hcHBlbmRDaGlsZChlbCgidGV4dCIsIHsgeDogeE9mKHRpY2spLCB5OiAyNDQsIGZpbGw6ICJ2YXIoLS1tdXRlZCkiLAogICAgICAiZm9udC1zaXplIjogIjEwcHgiLCAidGV4dC1hbmNob3IiOiAibWlkZGxlIiB9LCB0aWNrKSk7CiAgfQogIGNoYXJ0LmFwcGVuZENoaWxkKGVsKCJ0ZXh0IiwgeyB4OiAoTCArIFIpIC8gMiwgeTogMjU3LCBmaWxsOiAidmFyKC0tbXV0ZWQpIiwKICAgICJmb250LXNpemUiOiAiMTBweCIsICJ0ZXh0LWFuY2hvciI6ICJtaWRkbGUiIH0sICJ6LCB0aGUgbmV1cm9uJ3Mgd2VpZ2h0ZWQgc3VtIikpOwp9CgpmdW5jdGlvbiB2ZXJkaWN0Rm9yKHopIHsKICBjb25zdCBzID0gRlVOQ1NbMF0uc2xvcGUoeik7CiAgaWYgKE1hdGguYWJzKHopID49IDYpIHsKICAgIHJldHVybiAiU2lnbW9pZCdzIHNsb3BlIGhlcmUgaXMgIiArIHMudG9GaXhlZCg1KSArCiAgICAgICAgICAgIi4gVGhpcyBuZXVyb24gaXMgc2F0dXJhdGVkOiBpdCBzdGlsbCBwcm9kdWNlcyBhbiBvdXRwdXQgYW5kIGhhcyBzdG9wcGVkIGxlYXJuaW5nLiI7CiAgfQogIGlmIChNYXRoLmFicyh6KSA8PSAwLjQpIHsKICAgIHJldHVybiAiU2lnbW9pZCBpcyBhdCBpdHMgc3RlZXBlc3QgYW55d2hlcmUsIGFuZCB0aGF0IHN0ZWVwZXN0IGlzIHN0aWxsIG9ubHkgMC4yNS4iOwogIH0KICByZXR1cm4gIlNpZ21vaWQgc2xvcGUgIiArIHMudG9GaXhlZCgzKSArICIsIFJlTFUgc2xvcGUgIiArCiAgICAgICAgIEZVTkNTWzJdLnNsb3BlKHopLnRvRml4ZWQoMSkgKyAiLiBEcmFnIHRvd2FyZHMgZWl0aGVyIGVkZ2UgYW5kIHdhdGNoIHRoZSBTLWN1cnZlcyBmbGF0dGVuLiI7Cn0KCmZ1bmN0aW9uIHVwZGF0ZSgpIHsKICBjb25zdCB6ID0gcGFyc2VGbG9hdChkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgieiIpLnZhbHVlKTsKICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgiek91dCIpLnRleHRDb250ZW50ID0gei50b0ZpeGVkKDEpOwoKICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgicmVhZG91dCIpLnRleHRDb250ZW50ID0KICAgICJ6ID0gIiArIHoudG9GaXhlZCgxKSArICIgICDihpIgICAiICsKICAgIEZVTkNTLm1hcChmbiA9PiBmbi5uYW1lICsgIiAiICsgZm4uZih6KS50b0ZpeGVkKDMpKS5qb2luKCIsICAiKTsKICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgidmVyZGljdCIpLnRleHRDb250ZW50ID0gdmVyZGljdEZvcih6KTsKCiAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoIm5vdyIpLmlubmVySFRNTCA9IEZVTkNTLm1hcChmbiA9PgogICAgJzx0cj48dGQ+PGkgY2xhc3M9InN3YXRjaCIgc3R5bGU9ImJhY2tncm91bmQ6JyArIGZuLmNvbG91ciArICciPjwvaT4nICsgZm4ubmFtZSArCiAgICAnPC90ZD48dGQgY2xhc3M9Im51bSI+JyArIGZuLmYoeikudG9GaXhlZCgzKSArCiAgICAnPC90ZD48dGQgY2xhc3M9Im51bSI+JyArIGZuLnNsb3BlKHopLnRvRml4ZWQoNSkgKyAnPC90ZD48L3RyPicpLmpvaW4oIiIpOwoKICBjb25zdCBzaWdTbG9wZSA9IEZVTkNTWzBdLnNsb3BlKHopOwogIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJkZWNheSIpLmlubmVySFRNTCA9IFsxLCA1LCAxMCwgMjBdLm1hcChuID0+IHsKICAgIGNvbnN0IGxlZnQgPSBNYXRoLnBvdyhzaWdTbG9wZSwgbik7CiAgICByZXR1cm4gJzx0cj48dGQgY2xhc3M9Im51bSI+JyArIG4gKyAnPC90ZD48dGQgY2xhc3M9Im51bSI+JyArCiAgICAgIChsZWZ0IDwgMC4wMDEgPyBsZWZ0LnRvRXhwb25lbnRpYWwoMSkgOiBsZWZ0LnRvRml4ZWQoMykpICsKICAgICAgJzwvdGQ+PHRkIGNsYXNzPSJudW0iPjEuMDwvdGQ+PC90cj4nOwogIH0pLmpvaW4oIiIpOwoKICBkcmF3KHopOwp9Cgpkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgieiIpLmFkZEV2ZW50TGlzdGVuZXIoImlucHV0IiwgdXBkYXRlKTsKdXBkYXRlKCk7Cjwvc2NyaXB0Pgo8L2JvZHk+CjwvaHRtbD4K"
 width="100%"></iframe>

Two numbers in that output decide the rest of this lesson.

**The steepest sigmoid ever gets is 0.25.** Not at some unusual point, but at its very best, right in the middle. Everywhere else it is shallower.

**At an input of 8, the slope is 0.00034.** A neuron that has drifted into that region is `saturated`. It still produces an output, and it has stopped learning, because no adjustment to its weights makes an appreciable difference to what it produces. It is effectively frozen.

ReLU's column is different in kind. Its slope is exactly 1 for every positive input, no matter how large. A ReLU neuron with a weighted sum of 8 is just as responsive as one with a sum of 0.5.

![Visual explanation of what steepness has to do with learning](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_section_what_steepness_has_to_do_with_learning_simple_v2.png)

## Why Depth Broke

Now the two facts combine into the thing that stalled the field for twenty years.

When a network is trained, the correction is worked out at the output and passed backwards through the layers. At each layer it is multiplied by that layer's slope. So a correction reaching the first layer of a ten-layer network has been multiplied by ten slopes in succession.

Reading the code below: there is no network here and nothing is trained. The whole program is one multiplication repeated, `slope ** depth`, which is what "multiplied by each layer's slope on the way back" amounts to arithmetically. Sigmoid is given its most generous possible slope, 0.25, so the table understates the problem rather than exaggerating it.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjtca" 
 width="100%"
></iframe>

```
A correction travelling back through a deep network gets multiplied
by each layer's slope on the way. Best possible case for each:

 layers        sigmoid     ReLU
--------------------------------
      1       2.50e-01      1.0
      2       6.25e-02      1.0
      5       9.77e-04      1.0
     10       9.54e-07      1.0
     20       9.09e-13      1.0
     50       7.89e-31      1.0

With sigmoid, after 10 layers the signal reaching the first layer is
about 9.5e-07 of its original size, and that is the
most optimistic case. Those early layers barely learn at all.

With ReLU the slope is exactly 1 wherever the neuron is active, so
the signal passes through undiminished however many layers there are.
```

| In the code | What it stands for | Note |
| --- | --- | --- |
| `BEST_SIGMOID = sigmoid_slope(0)` | 0.25 | The best sigmoid ever manages, not a typical value |
| `RELU = 1.0` | ReLU's slope when active | Independent of how large the input is |
| `** depth` | Crossing that many layers | Each layer contributes one multiplication |
| `0.25 ** 10` | About 9.5e-07 | What reaches the first layer of a ten-layer network |
| `1.0 ** 50` | Still 1.0 | Why depth stopped being self-defeating |

This is the `vanishing gradient problem`, and the table states it more brutally than any description.

Multiplying by at most 0.25 ten times leaves under one millionth. Twenty layers leaves about 10 to the power of minus 13. Fifty layers leaves a number with thirty zeros after the decimal point. **The early layers of a deep sigmoid network receive a correction so small that, in ordinary floating-point arithmetic, they receive nothing at all.**

And 0.25 is the optimistic figure, requiring every neuron in every layer to sit exactly at its steepest point. Real neurons drift away from centre, so the true multipliers are smaller and the collapse is faster.

ReLU's column explains the fix. A slope of exactly 1 means the correction passes through unchanged, so the fiftieth layer back receives the same magnitude of signal as the first. Depth stops being self-defeating.

![Visual explanation of why depth broke](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_section_why_depth_broke_simple_v2.png)

## What ReLU Costs

ReLU is not free, and the honest account matters.

Its slope for negative inputs is exactly zero, which means a neuron whose weighted sum has become negative for every training example receives no correction at all and never recovers. It outputs zero forever and is called a `dead ReLU`. In a large network some proportion of neurons die during training, and while a network usually has enough spare capacity to tolerate it, wasting neurons is not ideal.

The usual remedy is a small variant: `leaky ReLU` gives negative inputs a small non-zero slope, perhaps 0.01, so a struggling neuron retains a faint path back to life.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Function</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Range</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strength</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Weakness</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Use for</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Sigmoid</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">0 to 1</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reads as a probability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Saturates; slope never exceeds 0.25</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The final layer of a yes-or-no classifier</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Tanh</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">-1 to 1</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Centred on zero; steeper than sigmoid</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Still saturates at both ends</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hidden layers in shallow networks; recurrent networks</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>ReLU</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">0 upwards</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Slope of 1 when active; very fast to compute</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Neurons can die permanently</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hidden layers, as the default choice</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Leaky ReLU</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unbounded</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keeps a small slope when negative</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One more setting to choose</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hidden layers where dead units are a problem</td>
    </tr>
  </tbody>
</table>

Note the last column carefully. Sigmoid did not disappear; it moved. It is a poor choice inside a deep network and remains the right choice for a final layer that must output something readable as a probability. The activation for hidden layers and the activation for the output layer are separate decisions.

![Visual explanation of what relu costs](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_section_what_relu_costs_simple_v2.png)

## The Output Layer Is a Separate Decision

Everything above concerns hidden layers, where the question is whether a correction can travel back through the network. The final layer answers a different question: what should the answer look like?

Three cases cover almost everything.

- **Predicting a quantity.** Use no activation at all. A price in lakh or a temperature in degrees should not be squashed into 0 to 1, and the layer's raw weighted sum is exactly what is wanted. This is the one place where a linear output is correct rather than a mistake.
- **A yes-or-no decision.** Use sigmoid. Its output between 0 and 1 reads directly as the probability of the positive class, and the threshold that turns it into a decision can then be chosen separately.
- **One of several categories.** Use `softmax`, which is the multi-class generalisation of sigmoid.

Softmax is worth a paragraph because it is the one genuinely new idea here. Given one raw total per class, it exponentiates each and divides by the sum of them all. Two properties follow, and both are what a multi-class output needs. Every result lands between 0 and 1, and they add up to exactly 1, so the layer produces a distribution across the classes rather than several unrelated scores.

The exponentiation matters more than it looks. Because it grows so steeply, a class whose total is modestly higher than the rest ends up with a substantially larger share, so the layer expresses confidence rather than merely ranking. Totals of 2, 1, and 0.1 do not become roughly a third each; they become approximately 0.66, 0.24, and 0.10.

The practical rule is short. **Hidden layers get ReLU because of gradients; the output layer gets whatever shape the answer needs.** Confusing the two produces networks that either cannot train or produce outputs nobody can interpret, and a sigmoid on the output of a regression model is one of the more common versions of the mistake.

![Visual explanation of output activation choice](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_output_activation_choice.png)

## Your Turn

Work out how flat is too flat, using the slope program.

Find the input at which the sigmoid slope drops below 0.01, then below 0.001. You will find these happen at surprisingly modest inputs, well inside the range a neuron's weighted sum reaches routinely once weights grow during training. That is why saturation is a practical problem rather than a theoretical one.

Then investigate the dead ReLU. Write a version of `relu_slope` for leaky ReLU with a slope of 0.01 on the negative side, and recompute the depth table with it. Check whether 0.01 to the power of 50 is any better than 0.25 to the power of 50. It is not, which tells you something important: leaky ReLU fixes dead neurons, and it does **not** fix vanishing gradients, because a network relying on the leak is back in the multiplying-small-numbers regime. The leak is insurance, not a substitute for neurons being active.

Finally, reason about the opposite failure. If multiplying by numbers below 1 makes the correction vanish, work out what happens when the multipliers are consistently above 1, say 1.5 per layer across 20 layers. Compute it. The resulting problem has its own name and its own remedies, and meeting it now will make it recognisable when you see a training run produce numbers that are not numbers at all.
