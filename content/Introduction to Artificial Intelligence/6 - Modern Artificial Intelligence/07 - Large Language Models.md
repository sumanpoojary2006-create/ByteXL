## Introduction

A logistics firm builds a support assistant on a hosted language model, and the pilot goes well enough that they roll it out. Three problems appear within a fortnight.

The first is money. The bill is four times the estimate, and nobody can say why, because the team estimated in words and the invoice is in tokens.

The second is memory. Customers report that the assistant contradicts itself in long conversations, agreeing to something on turn five and denying it on turn thirty.

The third is inconsistency. The same question asked twice gets different answers, sometimes materially different, and the team cannot work out whether that is a bug.

None of these is a defect. Each follows directly from how these systems work, and each is predictable by anyone who understands three things: what a token is, what a context window is, and what happens when the model picks its next word.

**Definition:** A `large language model` is a transformer trained on a very large quantity of text to predict the next `token` given the preceding ones, which after sufficient scale produces a system capable of a wide range of language tasks it was never separately trained for.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_section_introduction_simple_v2.png)

## Tokens

A model does not read words. It reads tokens, which are pieces of words drawn from a fixed vocabulary decided before training.

Reading the code below: `tokenise` is a greedy matcher. It repeatedly takes the longest vocabulary piece that starts the remaining text and chops it off. The `for ... else` is Python's rarely used construct: the `else` runs only when the `for` finished without hitting `break`, meaning no piece matched at all, and the character is marked with a question mark. A real tokeniser learns its vocabulary from data; this one is written by hand.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjamu" 
 width="100%"
></iframe>

```
          word  letters  tokens   pieces
----------------------------------------------------------
           the        3       1   ['the']
          food        4       1   ['food']
     delivered        9       2   ['deliver', 'ed']
  unbelievable       12       3   ['un', 'believ', 'able']
       biryani        7       3   ['bir', 'yan', 'i']
          dosa        4       2   ['do', 'sa']
       quickly        7       6   ['q?', 'u?', 'i', 'c?', 'k?', 'ly']
      zamindar        8       8   ['z?', 'a?', 'm?', 'i', 'n?', 'd?', 'a?', 'r?']

Common words cost 1 token each: ['the', 'food']
Rarer words cost more: {'unbelievable': 3, 'zamindar': 8}

A tokeniser is fitted to the text it was trained on. Words that
were frequent there are cheap; anything else is assembled from
fragments, which is why some languages cost far more tokens than
English for exactly the same meaning.
```

| In the code | What it is | Note |
| --- | --- | --- |
| `VOCAB` | The fixed vocabulary | Decided before training and never changed after |
| `sorted(..., key=len, reverse=True)` | Longest match first | Prevents "the" being split into smaller pieces |
| `rest.startswith(piece)` | The greedy match | One piece consumed per pass |
| The `for ... else` | No piece matched | Falls back to a single character |
| `len(pieces)` versus `len(word)` | Tokens versus letters | The billing unit is the first, not the second |
| `'zamindar'` costing 8 | The unequal-cost problem | Nothing in this vocabulary fits it |

Three consequences fall out of that table, and they explain the logistics firm's first problem.

**Cost is not proportional to words.** "The food" is two tokens; "zamindar" alone is eight in this toy vocabulary. A real tokeniser handles English words in one or two tokens and handles unusual names, technical terms, and other scripts far less efficiently. A firm estimating in words and billed in tokens will be wrong, and wrong in the direction of underestimating whenever the text is not ordinary English.

**Some languages cost several times more than others.** Text written in a script poorly represented in the tokeniser's training data fragments into many pieces, so the identical meaning consumes more of the context window and costs more to process. This is a real and often unnoticed source of unequal cost.

**The model does not see letters.** This is why language models are unreliable at counting characters, spelling words backwards, or noticing rhyme. Asked how many times a letter appears in a word, the model is looking at chunks, not letters, and the question is harder for it than it looks.

![Visual explanation of tokens context sampling](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_tokens_context_sampling_context_v4.png)

## The Context Window

The model sees a fixed number of tokens at once, and that is all it sees.

Reading the code below: no model is called and nothing is generated. This is a budget, written as arithmetic. The five constants at the top are planning figures for a support assistant, and the whole program is subtraction: fixed costs come off the context limit, and whatever remains is divided by the cost of one conversational turn.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjazk" 
 width="100%"
></iframe>

```
Fixed cost every single call: 3900 tokens
   instructions 400, policy text 3000, room to reply 500

Left for conversation history: 4100 tokens
That is 22 turns before the oldest ones must be dropped.

What happens as the conversation runs past that point:
   turn  5:  4800 tokens, fits
   turn 10:  5700 tokens, fits
   turn 20:  7500 tokens, fits
   turn 25:  8400 tokens, over by 400; oldest 3 turn(s) dropped
   turn 30:  9300 tokens, over by 1300; oldest 8 turn(s) dropped

The model has no memory beyond this window. Once a turn falls out,
it is gone, and the assistant will contradict something it 'said'
twenty minutes ago without any awareness of having done so.
```

| In the code | What it represents | Note |
| --- | --- | --- |
| `system_prompt` | Instructions and tone | Re-sent on every single call |
| `knowledge` | Pasted policy documents | The largest fixed cost, at 3,000 tokens |
| `reply_budget` | Space reserved for the answer | Must be held back, not spent on input |
| `fixed` | 3,900 tokens | Nearly half the window, before the customer speaks |
| `history_per_turn` | One question and one answer | The unit that gets dropped when space runs out |
| `dropped` | Turns pushed out of the window | Where the contradiction comes from |

That is the second problem, explained exactly. At turn 25 the earliest exchanges have been dropped to make room, and the model contradicts itself because the commitment it made on turn five is no longer in front of it.

Two things about this deserve emphasis.

**There is no memory.** The model is not a system that remembers a conversation; it is a function called afresh each time with a block of text. Everything it appears to recall was placed in that block by the surrounding software. The illusion of continuity is entirely the application's doing.

**Almost half the budget was spent before the customer said anything.** The instructions and pasted policy documents consume 3,400 tokens on every single call, and they are re-sent every time because there is nowhere to leave them. This is why prompt length is an engineering concern and not merely a style question.

The practical remedies follow from the arithmetic. Summarise old turns rather than dropping them. Retrieve only the policy sections relevant to the current question instead of pasting all of them. Store durable facts, such as the customer's order number, outside the model and reinsert them each call.

![Visual explanation of the context window](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_section_the_context_window.png)

## Sampling

The third problem is the model's answer varying between identical questions.

At each step the model produces a score for every token in its vocabulary. Those scores become probabilities, and one token is chosen. How it is chosen is a setting.

Reading the code below: `CANDIDATES` holds five raw scores and they never change. `distribution` is softmax with one addition, the `s / temperature` division on its first line, and that single division is the entire subject of this section. Dividing by a small number spreads the scores apart before they are normalised; dividing by a large one squeezes them together.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjbc6" 
 width="100%"
></iframe>

```
The same model scores, read at different temperatures

 temperature     good    tasty      bad     late   purple
---------------------------------------------------------
         0.2    0.952    0.047    0.001    0.000    0.000
         0.5    0.732    0.221    0.045    0.003    0.000
         1.0    0.537    0.295    0.132    0.033    0.004
         1.5    0.444    0.297    0.174    0.069    0.016
         3.0    0.330    0.270    0.207    0.130    0.062

At 0.2, 'good' takes 95.2% of the probability: nearly always the same word.
At 3.0, it takes 33.0%, and even 'purple' gets 6.2%.

Temperature does not change what the model knows. It changes how
much the sampling respects the model's own ranking.
```

| In the code | What it is | Effect |
| --- | --- | --- |
| `CANDIDATES` | The model's raw scores | Identical in every row of the table |
| `s / temperature` | The one new line | The only thing that varies |
| Temperature 0.2 | Dividing by a small number | Gaps widen, "good" takes 95.2 percent |
| Temperature 3.0 | Dividing by a large number | Gaps shrink, "purple" reaches 6.2 percent |
| The softmax below it | Unchanged | Turns whatever it is given into probabilities |

Move the temperature below. The five scores never change; only how much the sampling respects their ranking does.

<iframe
 frameBorder="0"
 height="520px" data-visualizer="temperature_explorer.html" src="data:text/html;base64,PCFkb2N0eXBlIGh0bWw+CjxodG1sIGxhbmc9ImVuIj4KPGhlYWQ+CjxtZXRhIGNoYXJzZXQ9InV0Zi04Ij4KPG1ldGEgbmFtZT0idmlld3BvcnQiIGNvbnRlbnQ9IndpZHRoPWRldmljZS13aWR0aCwgaW5pdGlhbC1zY2FsZT0xIj4KPHRpdGxlPlRlbXBlcmF0dXJlIEV4cGxvcmVyPC90aXRsZT4KPHN0eWxlPgogIDpyb290IHsKICAgIC0tYmc6ICMxMjE2MWQ7IC0tbGluZTogIzJjMzU0MjsgLS10ZXh0OiAjZTZlYmYyOyAtLW11dGVkOiAjOGI5N2E4OwogICAgLS1hY2NlbnQ6ICNmMjk5NGE7IC0tZGltOiAjM2E0NDUzOyAtLWNvb2w6ICM1YjhkZWY7CiAgfQogICogeyBib3gtc2l6aW5nOiBib3JkZXItYm94OyB9CiAgaHRtbCwgYm9keSB7IG1hcmdpbjogMDsgYmFja2dyb3VuZDogdmFyKC0tYmcpOyBjb2xvcjogdmFyKC0tdGV4dCk7CiAgICBmb250LWZhbWlseTogSW50ZXIsIHVpLXNhbnMtc2VyaWYsIHN5c3RlbS11aSwgLWFwcGxlLXN5c3RlbSwgIlNlZ29lIFVJIiwgc2Fucy1zZXJpZjsgfQogIC53cmFwIHsgcGFkZGluZzogMThweCAyMHB4IDIwcHg7IG1heC13aWR0aDogOTAwcHg7IG1hcmdpbjogMCBhdXRvOyB9CiAgLnRpdGxlIHsgZm9udC1zaXplOiAxMXB4OyBsZXR0ZXItc3BhY2luZzogLjE4ZW07IHRleHQtdHJhbnNmb3JtOiB1cHBlcmNhc2U7CiAgICBjb2xvcjogdmFyKC0tbXV0ZWQpOyB0ZXh0LWFsaWduOiBjZW50ZXI7IH0KICAuZm9ybXVsYSB7IHRleHQtYWxpZ246IGNlbnRlcjsgZm9udC1mYW1pbHk6IHVpLW1vbm9zcGFjZSwgU0ZNb25vLVJlZ3VsYXIsIE1lbmxvLCBtb25vc3BhY2U7CiAgICBmb250LXNpemU6IDE1cHg7IG1hcmdpbjogNnB4IDAgMTRweDsgY29sb3I6IHZhcigtLXRleHQpOwogICAgZGlzcGxheTogZmxleDsgZmxleC13cmFwOiB3cmFwOyBqdXN0aWZ5LWNvbnRlbnQ6IGNlbnRlcjsgZ2FwOiA0cHggMjRweDsgfQogIC5mb3JtdWxhIHNwYW4geyB3aGl0ZS1zcGFjZTogbm93cmFwOyB9CiAgLnJlYWRvdXQgeyBiYWNrZ3JvdW5kOiAjMGQxMTE3OyBib3JkZXI6IDFweCBzb2xpZCB2YXIoLS1saW5lKTsgYm9yZGVyLXJhZGl1czogNnB4OwogICAgcGFkZGluZzogOXB4IDEycHg7IGZvbnQtZmFtaWx5OiB1aS1tb25vc3BhY2UsIFNGTW9uby1SZWd1bGFyLCBNZW5sbywgbW9ub3NwYWNlOwogICAgZm9udC1zaXplOiAxM3B4OyB0ZXh0LWFsaWduOiBjZW50ZXI7IH0KICAudmVyZGljdCB7IHRleHQtYWxpZ246IGNlbnRlcjsgZm9udC1zaXplOiAxM3B4OyBsaW5lLWhlaWdodDogMS41OwogICAgbWFyZ2luOiAxMHB4IDAgMTRweDsgbWluLWhlaWdodDogMzhweDsgY29sb3I6IHZhcigtLWFjY2VudCk7IH0KICAuY29udHJvbCB7IGRpc3BsYXk6IGZsZXg7IGFsaWduLWl0ZW1zOiBjZW50ZXI7IGdhcDogMTJweDsgbWFyZ2luLWJvdHRvbTogMThweDsgfQogIC5jb250cm9sIGxhYmVsIHsgZm9udC1mYW1pbHk6IHVpLW1vbm9zcGFjZSwgTWVubG8sIG1vbm9zcGFjZTsgZm9udC1zaXplOiAxM3B4OwogICAgY29sb3I6IHZhcigtLW11dGVkKTsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgfQogIC5jb250cm9sIG91dHB1dCB7IGZvbnQtZmFtaWx5OiB1aS1tb25vc3BhY2UsIE1lbmxvLCBtb25vc3BhY2U7IGZvbnQtc2l6ZTogMTNweDsKICAgIHdpZHRoOiAzOHB4OyB0ZXh0LWFsaWduOiByaWdodDsgY29sb3I6IHZhcigtLWFjY2VudCk7IH0KICBpbnB1dFt0eXBlPXJhbmdlXSB7IGZsZXg6IDE7IC13ZWJraXQtYXBwZWFyYW5jZTogbm9uZTsgYXBwZWFyYW5jZTogbm9uZTsgaGVpZ2h0OiA0cHg7CiAgICBib3JkZXItcmFkaXVzOiAycHg7IGJhY2tncm91bmQ6IHZhcigtLWRpbSk7IG91dGxpbmU6IG5vbmU7IH0KICBpbnB1dFt0eXBlPXJhbmdlXTo6LXdlYmtpdC1zbGlkZXItdGh1bWIgeyAtd2Via2l0LWFwcGVhcmFuY2U6IG5vbmU7IGFwcGVhcmFuY2U6IG5vbmU7CiAgICB3aWR0aDogMTVweDsgaGVpZ2h0OiAxNXB4OyBib3JkZXItcmFkaXVzOiA1MCU7IGJhY2tncm91bmQ6IHZhcigtLWFjY2VudCk7IGN1cnNvcjogcG9pbnRlcjsgfQogIGlucHV0W3R5cGU9cmFuZ2VdOjotbW96LXJhbmdlLXRodW1iIHsgd2lkdGg6IDE1cHg7IGhlaWdodDogMTVweDsgYm9yZGVyOiAwOwogICAgYm9yZGVyLXJhZGl1czogNTAlOyBiYWNrZ3JvdW5kOiB2YXIoLS1hY2NlbnQpOyBjdXJzb3I6IHBvaW50ZXI7IH0KICAuZ3JpZCB7IGRpc3BsYXk6IGdyaWQ7IGdyaWQtdGVtcGxhdGUtY29sdW1uczogMWZyIDIzMHB4OyBnYXA6IDIycHg7IGFsaWduLWl0ZW1zOiBzdGFydDsgfQogIEBtZWRpYSAobWF4LXdpZHRoOiA3MDBweCkgeyAuZ3JpZCB7IGdyaWQtdGVtcGxhdGUtY29sdW1uczogMWZyOyB9CiAgICAuZm9ybXVsYSB7IGZvbnQtc2l6ZTogMTNweDsgfSAud3JhcCB7IHBhZGRpbmc6IDE0cHggMTRweCAxNnB4OyB9IH0KICAucm93IHsgZGlzcGxheTogZ3JpZDsgZ3JpZC10ZW1wbGF0ZS1jb2x1bW5zOiA2MnB4IDFmciA1OHB4OyBhbGlnbi1pdGVtczogY2VudGVyOwogICAgZ2FwOiAxMHB4OyBtYXJnaW4tYm90dG9tOiA5cHg7IH0KICAudG9rIHsgZm9udC1mYW1pbHk6IHVpLW1vbm9zcGFjZSwgTWVubG8sIG1vbm9zcGFjZTsgZm9udC1zaXplOiAxM3B4OyB0ZXh0LWFsaWduOiByaWdodDsgfQogIC50cmFjayB7IGhlaWdodDogMTZweDsgYmFja2dyb3VuZDogIzBkMTExNzsgYm9yZGVyOiAxcHggc29saWQgdmFyKC0tbGluZSk7CiAgICBib3JkZXItcmFkaXVzOiAzcHg7IG92ZXJmbG93OiBoaWRkZW47IH0KICAuZmlsbCB7IGhlaWdodDogMTAwJTsgdHJhbnNpdGlvbjogd2lkdGggLjA4cyBsaW5lYXI7IH0KICAucGN0IHsgZm9udC1mYW1pbHk6IHVpLW1vbm9zcGFjZSwgTWVubG8sIG1vbm9zcGFjZTsgZm9udC1zaXplOiAxMnB4OwogICAgZm9udC12YXJpYW50LW51bWVyaWM6IHRhYnVsYXItbnVtczsgY29sb3I6IHZhcigtLW11dGVkKTsgfQogIHRhYmxlIHsgd2lkdGg6IDEwMCU7IGJvcmRlci1jb2xsYXBzZTogY29sbGFwc2U7IGZvbnQtc2l6ZTogMTJweDsgfQogIHRoLCB0ZCB7IHBhZGRpbmc6IDVweCA2cHg7IHRleHQtYWxpZ246IHJpZ2h0OyBib3JkZXItYm90dG9tOiAxcHggc29saWQgdmFyKC0tbGluZSk7IH0KICB0aCB7IGNvbG9yOiB2YXIoLS1tdXRlZCk7IGZvbnQtd2VpZ2h0OiA1MDA7IH0KICB0ZDpmaXJzdC1jaGlsZCwgdGg6Zmlyc3QtY2hpbGQgeyB0ZXh0LWFsaWduOiBsZWZ0OyB9CiAgLm51bSB7IGZvbnQtZmFtaWx5OiB1aS1tb25vc3BhY2UsIE1lbmxvLCBtb25vc3BhY2U7IGZvbnQtdmFyaWFudC1udW1lcmljOiB0YWJ1bGFyLW51bXM7IH0KICAubm90ZSB7IGZvbnQtc2l6ZTogMTFweDsgY29sb3I6IHZhcigtLW11dGVkKTsgbGluZS1oZWlnaHQ6IDEuNTsgbWFyZ2luLXRvcDogMTJweDsgfQo8L3N0eWxlPgo8L2hlYWQ+Cjxib2R5Pgo8ZGl2IGNsYXNzPSJ3cmFwIj4KCiAgPGRpdiBjbGFzcz0idGl0bGUiPlRlbXBlcmF0dXJlIEV4cGxvcmVyPC9kaXY+CiAgPGRpdiBjbGFzcz0iZm9ybXVsYSI+CiAgICA8c3Bhbj50aGUgZm9vZCB3YXMgdmVyeSBfX188L3NwYW4+CiAgICA8c3Bhbj5wID0gc29mdG1heChzY29yZSAvIHRlbXBlcmF0dXJlKTwvc3Bhbj4KICA8L2Rpdj4KCiAgPGRpdiBjbGFzcz0icmVhZG91dCIgaWQ9InJlYWRvdXQiPjwvZGl2PgogIDxkaXYgY2xhc3M9InZlcmRpY3QiIGlkPSJ2ZXJkaWN0Ij48L2Rpdj4KCiAgPGRpdiBjbGFzcz0iY29udHJvbCI+CiAgICA8bGFiZWwgZm9yPSJ0ZW1wIj50ZW1wZXJhdHVyZTwvbGFiZWw+CiAgICA8aW5wdXQgdHlwZT0icmFuZ2UiIGlkPSJ0ZW1wIiBtaW49IjAuMSIgbWF4PSIzIiBzdGVwPSIwLjA1IiB2YWx1ZT0iMSI+CiAgICA8b3V0cHV0IGlkPSJ0ZW1wT3V0Ij4xLjAwPC9vdXRwdXQ+CiAgPC9kaXY+CgogIDxkaXYgY2xhc3M9ImdyaWQiPgogICAgPGRpdiBpZD0iYmFycyI+PC9kaXY+CiAgICA8ZGl2PgogICAgICA8dGFibGU+CiAgICAgICAgPHRyPjx0aD50b2tlbjwvdGg+PHRoPnNjb3JlPC90aD48dGg+cDwvdGg+PC90cj4KICAgICAgICA8dGJvZHkgaWQ9InRibCI+PC90Ym9keT4KICAgICAgPC90YWJsZT4KICAgICAgPGRpdiBjbGFzcz0ibm90ZSI+CiAgICAgICAgVGhlIHNjb3JlcyBuZXZlciBjaGFuZ2UuIFRlbXBlcmF0dXJlIG9ubHkgYWx0ZXJzIGhvdyBtdWNoIHRoZQogICAgICAgIHNhbXBsaW5nIHJlc3BlY3RzIHRoZSBtb2RlbCdzIG93biByYW5raW5nLiBPbmUgdG9rZW4gaXMgdGhlbiBkcmF3bgogICAgICAgIGF0IHJhbmRvbSB1c2luZyB0aGVzZSBwcm9iYWJpbGl0aWVzLCBzbyBhIHRva2VuIG5lYXIgdGhlIGJvdHRvbSBpcwogICAgICAgIHJhcmUgcmF0aGVyIHRoYW4gaW1wb3NzaWJsZS4KICAgICAgPC9kaXY+CiAgICA8L2Rpdj4KICA8L2Rpdj4KCjwvZGl2PgoKPHNjcmlwdD4KLy8gVGhlIG1vZGVsJ3MgcmF3IHNjb3JlcyBmb3Igd2hhdCBjb3VsZCBmb2xsb3cgInRoZSBmb29kIHdhcyB2ZXJ5IF9fXyIuCi8vIEZpeGVkLCBleGFjdGx5IGFzIHByaW50ZWQgaW4gdGhlIGxlc3Nvbi4gT25seSB0ZW1wZXJhdHVyZSBtb3Zlcy4KY29uc3QgQ0FORElEQVRFUyA9IFsKICB7IHRva2VuOiAiZ29vZCIsICAgc2NvcmU6ICA0LjAgfSwKICB7IHRva2VuOiAidGFzdHkiLCAgc2NvcmU6ICAzLjQgfSwKICB7IHRva2VuOiAiYmFkIiwgICAgc2NvcmU6ICAyLjYgfSwKICB7IHRva2VuOiAibGF0ZSIsICAgc2NvcmU6ICAxLjIgfSwKICB7IHRva2VuOiAicHVycGxlIiwgc2NvcmU6IC0xLjAgfQpdOwoKZnVuY3Rpb24gZGlzdHJpYnV0aW9uKHRlbXBlcmF0dXJlKSB7CiAgY29uc3QgYWRqdXN0ZWQgPSBDQU5ESURBVEVTLm1hcChjID0+IGMuc2NvcmUgLyB0ZW1wZXJhdHVyZSk7CiAgY29uc3QgYmlnZ2VzdCA9IE1hdGgubWF4KC4uLmFkanVzdGVkKTsKICBjb25zdCBleHBzID0gYWRqdXN0ZWQubWFwKHYgPT4gTWF0aC5leHAodiAtIGJpZ2dlc3QpKTsKICBjb25zdCB0b3RhbCA9IGV4cHMucmVkdWNlKChhLCBiKSA9PiBhICsgYiwgMCk7CiAgcmV0dXJuIGV4cHMubWFwKGUgPT4gZSAvIHRvdGFsKTsKfQoKLy8gV2FybSBjb2xvdXIgZm9yIHRoZSB0b2tlbiB0aGUgbW9kZWwgcHJlZmVycywgY29vbGluZyBkb3duIHRoZSByYW5raW5nLgpjb25zdCBDT0xPVVJTID0gWyIjZjI5OTRhIiwgIiNlOGE3NjUiLCAiI2M5YTE3ZSIsICIjOGY5NWE4IiwgIiM1YjhkZWYiXTsKCmNvbnN0IGJhcnMgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgiYmFycyIpOwpDQU5ESURBVEVTLmZvckVhY2goKGMsIGkpID0+IHsKICBjb25zdCByb3cgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCJkaXYiKTsKICByb3cuY2xhc3NOYW1lID0gInJvdyI7CiAgcm93LmlubmVySFRNTCA9CiAgICAnPGRpdiBjbGFzcz0idG9rIj4nICsgYy50b2tlbiArICc8L2Rpdj4nICsKICAgICc8ZGl2IGNsYXNzPSJ0cmFjayI+PGRpdiBjbGFzcz0iZmlsbCIgaWQ9ImZpbGwnICsgaSArICciIHN0eWxlPSJiYWNrZ3JvdW5kOicgKwogICAgQ09MT1VSU1tpXSArICciPjwvZGl2PjwvZGl2PicgKwogICAgJzxkaXYgY2xhc3M9InBjdCIgaWQ9InBjdCcgKyBpICsgJyI+PC9kaXY+JzsKICBiYXJzLmFwcGVuZENoaWxkKHJvdyk7Cn0pOwoKZnVuY3Rpb24gdmVyZGljdEZvcih0ZW1wZXJhdHVyZSwgcHJvYnMpIHsKICBjb25zdCB0b3AgPSBwcm9ic1swXSwgd29yc3QgPSBwcm9ic1twcm9icy5sZW5ndGggLSAxXTsKICBpZiAodGVtcGVyYXR1cmUgPD0gMC4zNSkgewogICAgcmV0dXJuICJBbG1vc3QgYWxsIHRoZSBwcm9iYWJpbGl0eSBzaXRzIG9uIG9uZSB0b2tlbiwgc28gdGhlIHNhbWUgcHJvbXB0ICIgKwogICAgICAgICAgICJyZXR1cm5zIHRoZSBzYW1lIGFuc3dlciBuZWFybHkgZXZlcnkgdGltZS4iOwogIH0KICBpZiAodGVtcGVyYXR1cmUgPj0gMi4yKSB7CiAgICByZXR1cm4gIlRoZSByYW5raW5nIGlzIG5lYXJseSBmbGF0dGVuZWQuICdwdXJwbGUnIG5vdyBoYXMgYSAiICsKICAgICAgICAgICAod29yc3QgKiAxMDApLnRvRml4ZWQoMSkgKyAiJSBjaGFuY2UsIGFuZCBvbmNlIGEgcG9vciB0b2tlbiBpcyAiICsKICAgICAgICAgICAiY29tbWl0dGVkIHRvLCBldmVyeXRoaW5nIGFmdGVyIGl0IGNvbnRpbnVlcyB0aGF0IG1pc3Rha2UuIjsKICB9CiAgcmV0dXJuICInZ29vZCcgaG9sZHMgIiArICh0b3AgKiAxMDApLnRvRml4ZWQoMSkgKyAiJSBvZiB0aGUgcHJvYmFiaWxpdHkuICIgKwogICAgICAgICAiTG93ZXIgdGhlIHRlbXBlcmF0dXJlIHRvIG1ha2UgdGhlIG1vZGVsIHJlcGVhdCBpdHNlbGYsIHJhaXNlIGl0IHRvIGxldCBpdCB3YW5kZXIuIjsKfQoKZnVuY3Rpb24gdXBkYXRlKCkgewogIGNvbnN0IHRlbXBlcmF0dXJlID0gcGFyc2VGbG9hdChkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgidGVtcCIpLnZhbHVlKTsKICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgidGVtcE91dCIpLnRleHRDb250ZW50ID0gdGVtcGVyYXR1cmUudG9GaXhlZCgyKTsKCiAgY29uc3QgcHJvYnMgPSBkaXN0cmlidXRpb24odGVtcGVyYXR1cmUpOwogIHByb2JzLmZvckVhY2goKHAsIGkpID0+IHsKICAgIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJmaWxsIiArIGkpLnN0eWxlLndpZHRoID0gKHAgKiAxMDApICsgIiUiOwogICAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoInBjdCIgKyBpKS50ZXh0Q29udGVudCA9IHAudG9GaXhlZCgzKTsKICB9KTsKCiAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoInJlYWRvdXQiKS50ZXh0Q29udGVudCA9CiAgICAidGVtcGVyYXR1cmUgIiArIHRlbXBlcmF0dXJlLnRvRml4ZWQoMikgKyAiICAg4oaSICAgJyIgKyBDQU5ESURBVEVTWzBdLnRva2VuICsKICAgICInIHRha2VzICIgKyAocHJvYnNbMF0gKiAxMDApLnRvRml4ZWQoMSkgKyAiJSBvZiB0aGUgcHJvYmFiaWxpdHkiOwogIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJ2ZXJkaWN0IikudGV4dENvbnRlbnQgPSB2ZXJkaWN0Rm9yKHRlbXBlcmF0dXJlLCBwcm9icyk7CgogIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJ0YmwiKS5pbm5lckhUTUwgPSBDQU5ESURBVEVTLm1hcCgoYywgaSkgPT4KICAgICc8dHI+PHRkPicgKyBjLnRva2VuICsgJzwvdGQ+PHRkIGNsYXNzPSJudW0iPicgKyBjLnNjb3JlLnRvRml4ZWQoMSkgKwogICAgJzwvdGQ+PHRkIGNsYXNzPSJudW0iPicgKyBwcm9ic1tpXS50b0ZpeGVkKDMpICsgJzwvdGQ+PC90cj4nKS5qb2luKCIiKTsKfQoKZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoInRlbXAiKS5hZGRFdmVudExpc3RlbmVyKCJpbnB1dCIsIHVwZGF0ZSk7CnVwZGF0ZSgpOwo8L3NjcmlwdD4KPC9ib2R5Pgo8L2h0bWw+Cg=="
 width="100%"></iframe>

The model's opinion is identical in every row. Only the reading of it changes.

At low temperature the highest-scoring token takes almost all the probability, so the same input reliably produces the same output. At high temperature the distribution flattens until a token the model rated poorly, "purple", gets a 6.2 percent chance of being chosen, and once a poor token is committed to, everything after it is generated as a continuation of that mistake.

So the logistics firm's inconsistency is a configuration choice, not a bug. **For a support assistant quoting policy, temperature should be near zero.** For brainstorming, higher is the point. Shipping a factual assistant at a creative setting is a common and entirely avoidable error.

![Visual explanation of sampling](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_section_sampling_simple_v2.png)

## From Next-Token Predictor to Assistant

There is a gap in the story so far worth closing. A model trained purely to predict the next token is not an assistant, and it does not behave like one.

Give a raw pre-trained model the input "How do I file a claim?" and the most likely continuation, judged by the text of the internet, is not an answer. It might be more questions, because the model has seen many pages listing frequently asked questions. It might be a heading, or a navigation menu, or an advertisement. The model is completing a document, and a question in a document is very often followed by more questions.

Two further stages turn that into something that answers.

**Instruction tuning** continues training on examples of instructions paired with good responses. These are written by people, in far smaller quantity than the pre-training corpus, and they teach the model what shape of output an instruction calls for. After this stage, a question is followed by an answer rather than by more questions.

**Preference tuning** goes further. People are shown several candidate responses to the same prompt and asked which they prefer. Those comparisons train a second model that scores responses, and the language model is then adjusted to produce responses that score well. This is where the tone, the refusals, the hedging, and the general helpfulness come from.

Three consequences are worth carrying away.

- **The assistant's manner is a training decision, not a property of language models.** The same base model, tuned differently, produces a different personality, a different willingness to speculate, and different refusals.
- **Preferences come from particular people.** Whoever provided the comparisons has shaped what the model considers a good answer, and their assumptions are now embedded in every response.
- **Being preferred is not the same as being correct.** Human raters reward answers that sound confident and complete, so tuning on preferences can push a model towards assured-sounding output, which is one reason hedging and uncertainty are underrepresented in these systems.

This also explains something the logistics firm might otherwise find puzzling. The model's willingness to answer a policy question confidently, even when it has no basis for the answer, was trained into it by people who preferred confident answers.

![Visual explanation of llm to assistant](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_llm_to_assistant_context_v4.png)

## Prompting and Adaptation

Getting useful behaviour out of these systems involves a ladder of increasingly heavy interventions, and the cheapest sufficient one is the right choice.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Method</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it does</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Use when</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Clear instruction</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">States the task, format, and constraints precisely</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Always; most failures are underspecified requests</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Worked examples</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shows two or three input-output pairs in the prompt</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The format matters and is hard to describe</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Retrieval</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fetches relevant documents and includes them</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The answer depends on facts the model cannot know</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Fine-tuning</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Adjusts weights on your own examples</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A consistent style or format is needed at volume</td>
    </tr>
  </tbody>
</table>

The third row is the one most projects need and most reach for last. `Retrieval` is how a model answers questions about your policies, your prices, or events after its training: the relevant text is found by ordinary search and placed in the context, and the model reads it there. It solves the knowledge cut-off, it lets answers cite a source, and updating means editing a document rather than retraining anything.

Fine-tuning is frequently misapplied. **It teaches form far more reliably than it teaches facts.** A team that fine-tunes on four thousand policy documents hoping the model will then know the policies is usually disappointed, and retrieval would have served them better.

![Visual explanation of prompting and adaptation](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_section_prompting_and_adaptation.png)

## Your Turn

Rebuild the logistics firm's budget with retrieval instead of pasted policy.

Suppose retrieval fetches only the two most relevant policy sections, costing 600 tokens instead of 3,000. Rerun the arithmetic from the second program: recompute the fixed cost, the tokens left for history, and how many turns fit. Then state what the firm gains beyond the extra turns, thinking about what happens when a policy changes.

Then work out the cost multiplier properly. If a customer writes in a language that fragments into roughly three tokens per word where English takes 1.3, compute how much more each of their conversations costs, and how many fewer turns fit in the same window. Then decide whether the firm should charge differently, serve those customers on a larger context model, or do something else. This is a real product decision that follows entirely from the tokeniser.

Finally, take a position on temperature. The support assistant runs at temperature 0 and gives identical answers to identical questions, which the team likes. Argue that this is correct, then argue that it hides a problem: a model that is confidently wrong at temperature 0 is wrong the same way every time, and nobody notices the variability that would have signalled uncertainty. Say what you would monitor instead.
