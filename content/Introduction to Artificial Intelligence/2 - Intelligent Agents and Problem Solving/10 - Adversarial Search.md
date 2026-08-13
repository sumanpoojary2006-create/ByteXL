## Introduction

Manoj writes a tic-tac-toe program for a college assignment, and it plays reasonably well against his roommate for about a week. Then his roommate works out the pattern and starts winning every single game.

Manoj's program was built the way everything in this unit has been built so far. It searched for a sequence of moves leading to three in a row, found one, and started executing it. The flaw is obvious once you see it: the program planned a route to victory and then followed the route, while the opponent sat opposite deliberately removing squares from it.

This is a genuinely new situation, not a harder version of an old one. Every algorithm so far has assumed that when the agent takes an action, the resulting state is determined by the action and the world. Roads do not move. Tiles do not slide back on their own. But here, after Manoj's program places an X, somebody else chooses where the O goes, and that somebody is choosing specifically to make things worse.

The agent no longer controls the state that follows its move. It controls only every other move, and it must assume the intervening ones will be the worst possible for it. Searching under that assumption is **adversarial search**.

**Definition:** `Adversarial search` finds the best move in a competitive setting by searching a game tree in which the two players alternate, one trying to maximise the outcome and the other trying to minimise it, so every plan is evaluated against the opponent's best reply rather than a convenient one.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_section_introduction.png)

## Why an Opponent Changes Everything

Three assumptions break at once, and each has a direct consequence.

- **The agent no longer picks the whole sequence.** It picks alternate moves, so a "solution" cannot be a fixed plan. It must be a strategy: a reply prepared for whatever the opponent does.
- **Optimism becomes fatal.** Searching for the path where the opponent cooperates finds a route that will never happen. Manoj's program did exactly this.
- **The answer expires.** Because the opponent's choice is not known in advance, the search produces one move, and then the whole thing is done again from the new position.

The standard setting for this lesson is a two-player, zero-sum, perfect-information game. **Zero-sum** means one player's gain is exactly the other's loss, so a single number can score a position from both perspectives at once. **Perfect information** means both players see the entire position, with nothing hidden and nothing random. Tic-tac-toe, chess, and Go all qualify. Poker does not, because the cards are hidden, and that is a substantially harder problem.

![Visual explanation of why an opponent changes everything](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_section_why_an_opponent_changes_everything.png)

## Game Trees

A `game tree` has positions as nodes and moves as edges, with the levels alternating between the two players.

By convention the player the search is working for is called **MAX**, because it wants the score as high as possible, and the opponent is **MIN**. For Manoj, X is MAX. Terminal positions get a score: 1 if X wins, minus 1 if O wins, 0 for a draw. The whole tree is then just alternating layers, MAX choosing at one level and MIN choosing at the next.

The critical insight is about how values move back up. At a MAX node, the value is the largest of its children's values, because MAX will choose the best available. At a MIN node, the value is the smallest, because MIN will do likewise. **A position's value is not a property of the position alone; it is what the position becomes once both players play as well as they can.**

![Visual explanation of game trees](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_section_game_trees.png)

## Minimax

`Minimax` computes exactly that. It descends to terminal positions, scores them, and passes the values back up, taking the maximum at MAX levels and the minimum at MIN levels.

A small tree makes the arithmetic visible. Suppose MAX has three moves, each of which gives MIN three replies, and the nine resulting positions score as shown.

| MAX's move | MIN's replies score | MIN will choose | So the move is worth |
| --- | --- | --- | --- |
| A | 3, 12, 8 | 3 | 3 |
| B | 2, 4, 6 | 2 | 2 |
| C | 14, 5, 2 | 2 | 2 |

Move A looks unremarkable and move C looks tempting, since C contains the highest number anywhere on the tree. C is a trap. That 14 is only reachable if MIN volunteers it, and MIN will not. MIN will play the reply worth 2, so C is worth 2. Move A is worth 3, and MAX should play A.

**Minimax evaluates a move by its worst outcome under best opposition, not by its best outcome under lucky opposition.** That single sentence is what Manoj's original program was missing.

Now the real thing. Take a position where X is to move.

Reading the code below: the board is a flat list of nine squares, `LINES` lists the eight ways to win, and `winner` checks them. The algorithm is `minimax`, and it is nine lines: three checks for a finished game, then one recursive loop. The final block asks it about each legal move in turn.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzkfec" 
 width="100%"
></iframe>

```
X to move:
  X | O | X
    |   |  
  O |   |  
  play square 3: X loses
  play square 4: draw
  play square 5: draw
  play square 7: draw
  play square 8: X wins
Best move: square 8
Positions examined: 257
```

Five legal moves, and they are not remotely equivalent. One of them wins outright, one of them loses outright, and three draw. A human glancing at this board would very likely take square 4, the centre, on general principle, and would throw away a won game. Square 8 wins because it gives X two separate threats at once, through the top-right diagonal and the bottom row, and O cannot block both.

The whole of minimax is one line, and the rest is bookkeeping.

| In the code | What it is | Why it is there |
| --- | --- | --- |
| The three `if` returns | Terminal scores: 1, −1, 0 | The only positions whose value is known outright |
| `attempt = board[:]` | A copy of the board | Recursion explores many futures; none may disturb the present |
| `minimax(attempt, not x_to_move, ...)` | Ask the same question of the opponent | `not x_to_move` is what alternates MAX and MIN |
| `max(results) if x_to_move else min(results)` | **The algorithm** | X takes the best available, O takes the worst for X |

Everything above the last line exists to produce `results`. That single expression is the entire idea, and it encodes the assumption that the opponent will play their best reply rather than a convenient one.

![Visual explanation of minimax game tree](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_minimax_game_tree.png)

## The Cost

Manoj's position needed 257 positions examined. The empty board needs 549,946, which is still trivial for a computer, and it is why tic-tac-toe is a solved game whose perfect result is a draw.

Now scale it. The size of a game tree is roughly the number of legal moves per turn raised to the power of the number of turns. Chess averages around 35 legal moves and games run past 40 moves each side, giving a tree of roughly 35 to the power of 80. Go on a 19 by 19 board offers around 250 moves per turn.

These are not large numbers in the sense of needing a bigger computer. They exceed the number of atoms in the observable universe. **Full minimax is impossible for any interesting game**, and the two responses to that fact are the rest of this lesson and the whole history of game-playing programs.

![Visual explanation of the cost](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_section_the_cost.png)

## Alpha-Beta Pruning

The first response is to notice that much of the tree does not need to be examined at all.

Return to the three-move table. MAX evaluates A and learns it is worth 3. It then starts on B and finds MIN's first reply is worth 2. At that instant, B is finished. Whatever the remaining replies contain, MIN already has an option worth 2, so B cannot be worth more than 2, so B cannot beat A. The other two replies could be anything and the conclusion would not change, so evaluating them is wasted work.

`Alpha-beta pruning` formalises exactly this reasoning with two numbers carried down the tree.

- **Alpha** is the best score MAX is already guaranteed somewhere above. It only rises.
- **Beta** is the best score MIN is already guaranteed somewhere above. It only falls.

Whenever `beta <= alpha`, the current branch cannot influence the final answer and is abandoned. That single condition is the whole technique.

Reading the code below: `plain_minimax` is unchanged from the previous program, included so the two can be run side by side. `alpha_beta` is the same algorithm with two extra arguments carried down the recursion and one `break`. Compare the two functions directly; everything else in the file is scaffolding.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzkg2z" 
 width="100%"
></iframe>

```
Minimax    picks square 8, examining 257 positions
Alpha-beta picks square 8, examining 201 positions
```

Same move, less work. Four additions to minimax, and nothing else changed.

| In the code | What it is | Why it works |
| --- | --- | --- |
| `alpha` | Best score MAX is already guaranteed above | Only ever rises as the search proceeds |
| `beta` | Best score MIN is already guaranteed above | Only ever falls |
| `alpha = max(alpha, best)` | Record a new guarantee | MAX has found something at least this good |
| `if beta <= alpha: break` | **The pruning** | The opponent would never let play reach here, so stop looking |

This is the property that makes alpha-beta so valuable: **it is not an approximation.** It returns exactly what minimax returns, every time. The positions it skips are provably incapable of changing the answer, so nothing is being traded away for the speed.

The saving here is modest because this position is nearly full and there is little left to prune. On a fuller tree it is dramatic, which the exercise below demonstrates.

One practical point that matters enormously in real engines. How much gets pruned depends on **move ordering**. Examining strong moves first raises alpha quickly, which lets later branches be cut off sooner. With ideal ordering, alpha-beta can search roughly twice as deep as plain minimax in the same time. With the worst possible ordering it prunes nothing at all. This is why serious chess programs invest heavily in guessing which moves are good *before* searching them, purely to make the search that follows more efficient.

![Visual explanation of alpha beta pruning](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_alpha_beta_pruning.png)

## What Real Game Engines Do

Alpha-beta shrinks the tree. It does not shrink it from 35 to the power of 80 down to anything reachable, so a second idea is required, and it is a concession rather than a trick.

**Stop early and guess.** A real engine searches to a fixed depth, perhaps fifteen or twenty moves ahead, and then, instead of reaching terminal positions with true scores, applies an `evaluation function` that estimates how good a non-final position looks. For chess this counts material, king safety, pawn structure, and mobility. The engine is no longer computing the true minimax value; it is computing the minimax value of estimates.

Everything else follows from that concession. Deep Blue's evaluation function was hand-crafted with grandmasters and paired with enormous search. AlphaGo's contribution was to learn the evaluation function from experience instead, which mattered because nobody has ever been able to write a good one for Go by hand.

Note what survived all of it. Both systems are still doing exactly what the three-row table above describes: assuming the opponent will pick their best reply, and choosing accordingly.

![Visual explanation of what real game engines do](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_section_what_real_game_engines_do.png)

## Adversarial Search at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Idea</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it does</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it costs</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Game tree</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Represents alternating turns, MAX then MIN</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Grows exponentially with depth</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Minimax</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Passes values up, taking max at MAX levels and min at MIN levels</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Must reach terminal positions, so impossible beyond toy games</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Alpha-beta pruning</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Skips branches that cannot change the result</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nothing in accuracy; effectiveness depends on move ordering</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Depth limit plus evaluation</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stops early and estimates the value of non-final positions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The answer is only as good as the estimate</td>
    </tr>
  </tbody>
</table>

![Visual explanation of adversarial search at a glance](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_section_adversarial_search_at_a_glance.png)

## Your Turn

Run both searches from a completely empty board and watch the pruning do its work at a scale where it matters.

Reading the code below: both functions are exactly as defined above, with nothing changed. The only new lines are the last six, which run each from an empty board and print the counter. This one takes a second or two to finish, because the first function really does examine every position.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzkgdd" 
 width="100%"
></iframe>

```
Minimax    from an empty board: value 0 after 549946 positions
Alpha-beta from an empty board: value 0 after 18297 positions
```

Thirty times less work for an identical answer, and that answer, a value of 0, is the proof that tic-tac-toe is a draw with perfect play from both sides. Manoj's roommate was not clever; the game simply cannot be won against someone who does not err.

Now test the move-ordering claim rather than believing it. Reverse the order in which squares are tried inside `alpha_beta`, by iterating over `reversed(list(enumerate(board)))`, and compare the node count. It will change, possibly a lot, while the returned value stays exactly 0. Sit with what that means: the answer is fixed by the game, and the effort needed to find it is a property of how you looked.

Then reason out one thing the code cannot show you. Alpha-beta assumes the opponent plays perfectly. What happens when the real opponent is a distracted roommate who blunders? Work out whether the algorithm's move is still a good move in that case, and whether always assuming the best possible opposition might cost you wins against a weak player. There is a real answer, and it is not entirely comfortable.
