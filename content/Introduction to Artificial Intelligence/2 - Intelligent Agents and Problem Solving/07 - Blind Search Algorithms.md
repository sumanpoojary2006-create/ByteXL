## Introduction

Farhan has forty minutes before his exam and he is standing at the hostel gate of a campus he joined three weeks ago. He knows the exam hall exists. He does not know where it is.

Someone hands him a corridor map: a sheet showing which blocks connect to which other blocks. Hostel gate connects to the canteen and the library. The canteen connects onward to the sports complex. The library connects onward to the admin block. That is all the sheet says. There are no distances printed, no arrows pointing towards the exam hall, nothing at all telling him whether walking towards the canteen takes him closer to his exam or further away.

This is not a small handicap, and it is worth pausing on. Farhan cannot ask "which of these two corridors leads more directly to the exam hall", because nothing in his information answers that. He can only ask "which corridors exist, and in what order shall I try them". A search that operates under exactly this restriction, with no estimate of how close any place is to the goal, is called **blind search**, or equivalently uninformed search, and the surprising thing is how much can be achieved with so little.

**Definition:** `Blind search` explores a problem's state space using only the structure of the connections available, with no information about how near any state is to the goal, so its behaviour is determined entirely by the order in which it chooses to expand what it has discovered.

![Opening scene: Farhan has forty minutes before his exam and he is standing at the hostel gate of a campus he joined three weeks ago.](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_section_introduction.png)

## What "Blind" Actually Means

The word describes what the algorithm is denied, not how well it performs.

A blind search algorithm is allowed to know three things: where it currently is, which places connect to it, and whether the place it has arrived at is the goal. It is denied any measure of progress. It cannot look at the sports complex and the admin block and form the judgment that one of them feels closer to the destination.

Because of this, every blind search algorithm reduces to a single design decision: **of everything discovered but not yet explored, which do I look at next?** That collection of discovered-but-unexplored places is called the `frontier`, and the choice of what to pull from it is the entire difference between the three algorithms in this lesson. Change the frontier from a queue to a stack and you have turned breadth-first search into depth-first search, without altering another line.

![Visual explanation of what "blind" actually means](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_section_what_blind_actually_means.png)

## Farhan's Campus as a Graph

Before any algorithm can run, the corridor map has to become a structure a program can hold. Each block is a node, and each corridor is a connection between two nodes.

| Block | Connects directly to |
| --- | --- |
| Hostel Gate | Canteen, Library |
| Canteen | Hostel Gate, Sports Complex |
| Sports Complex | Canteen, Science Block |
| Science Block | Sports Complex, Exam Hall |
| Library | Hostel Gate, Admin Block |
| Admin Block | Library, Exam Hall |
| Exam Hall | Science Block, Admin Block |

Read it and you can see there are exactly two ways to reach the exam hall. One goes through the library and the admin block. The other goes through the canteen, the sports complex, and the science block. Farhan cannot see this, because he is standing inside the map rather than looking down at it, and neither can a blind search algorithm at the moment it starts.

![Visual explanation of farhan's campus as a graph](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_section_farhan_s_campus_as_a_graph.png)

## Breadth-First Search: Explore Level by Level

`Breadth-first search`, or BFS, examines every place one step away before it looks at anything two steps away, then everything two steps away before anything three steps away. It fans outward in rings.

To behave this way, it keeps the frontier as a **queue**, which hands back whatever has been waiting longest. Places discovered earlier, and therefore closer to the start, always get explored before places discovered later.

Reading the code below: `campus` is just the corridor table written as a dictionary, and the last three lines run it and print. The algorithm is the twelve lines of `breadth_first_search`, and within those, one word decides everything.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzkjd4" 
 width="100%"
></iframe>

```
BFS route: Hostel Gate -> Library -> Admin Block -> Exam Hall
Blocks walked through: 3
```

Four pieces of that function carry the whole idea.

| In the code | What it is | Why it is there |
| --- | --- | --- |
| `deque([[start]])` | A frontier holding whole routes | So the answer is a walkable route, not just "reachable" |
| `frontier.popleft()` | Take from the **front** | This one word is what makes the search breadth-first |
| `visited` | Blocks already discovered | Stops it walking back down a corridor and circling forever |
| `path + [neighbour]` | A **new** longer route | Building a copy rather than editing keeps each branch separate |

The second row is the one to remember. Change `popleft()` to `pop()` and nothing else, and this becomes depth-first search, which is exactly what the next program does.

Watching the frontier change is more instructive than reading the code. Each row below is one pass of the loop.

| Pass | Path taken off the frontier | Newly discovered | Frontier afterwards |
| --- | --- | --- | --- |
| 1 | Hostel Gate | Canteen, Library | Canteen, Library |
| 2 | Canteen | Sports Complex | Library, Sports Complex |
| 3 | Library | Admin Block | Sports Complex, Admin Block |
| 4 | Sports Complex | Science Block | Admin Block, Science Block |
| 5 | Admin Block | Exam Hall | Science Block, Exam Hall |
| 6 | Science Block | nothing new | Exam Hall |
| 7 | Exam Hall | goal reached | route returned |

Notice that the search finishes the entire second ring before touching the third. That discipline is exactly what guarantees the result: **BFS always returns a path with the fewest possible steps.** The first time it reaches the goal, no shorter route can exist, because a shorter one would have been found in an earlier ring.

The cost of that guarantee is memory. BFS holds the whole frontier at once, and the frontier grows with each ring. On a campus of seven blocks this is nothing. On a road network of a million junctions it becomes the reason BFS is unusable.

![Visual explanation of breadth-first search: explore level by level](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_section_breadth_first_search_explore_level_by_level.png)

## Depth-First Search: Follow One Path to the End

`Depth-first search`, or DFS, commits. It picks one corridor, walks it as far as it goes, and only when that path is exhausted does it back up and try an alternative.

The change is one line. The frontier becomes a **stack**, handing back whatever was added most recently, so the search always continues from where it just was rather than returning to older options.

Reading the code below: the map is unchanged and the printing is unchanged. Compare `depth_first_search` line by line against the previous function and you will find only two real differences, both marked in the comments.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzkjyz" 
 width="100%"
></iframe>

```
DFS route: Hostel Gate -> Canteen -> Sports Complex -> Science Block -> Exam Hall
Blocks walked through: 4
```

Two changed lines, and a different answer.

| In the code | BFS had | DFS has | Effect |
| --- | --- | --- | --- |
| Taking from the frontier | `popleft()`, the front | `pop()`, the end | Continues from where it just was, rather than returning to the oldest option |
| Neighbour order | `graph[block]` | `reversed(graph[block])` | A stack reverses order, so reversing first restores the map's reading order |
| Marking visited | When discovered | When expanded | A block can sit in the stack twice, so the check moves to where it is taken out |

The `reversed(...)` is worth understanding rather than copying. It changes nothing about how DFS works and everything about which of several correct answers you get, because it decides which corridor the search commits to first.

The result is a different answer to the same question. DFS walked Farhan through four blocks where BFS found a route through three, and it did so not because it made a mistake but because it never compared the two options. It went down the canteen corridor first and never looked back.

**DFS does not return the shortest path, and it offers no guarantee that it will.** What it offers instead is memory. DFS holds only the current path and the untried branches hanging off it, which on a large problem is dramatically less than BFS's expanding rings. It also has a genuine danger: on a graph with a very long or infinite branch, DFS can follow it forever and never discover a goal sitting two steps away down the corridor it did not take.

![Visual explanation of depth-first search: follow one path to the end](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_section_depth_first_search_follow_one_path_to_the_end.png)

## Why the Two Disagree

Both algorithms are correct. They optimise different things, and the disagreement is the point.

- **BFS is cautious and thorough.** It refuses to consider a longer route before exhausting the shorter ones, which is precisely why it can promise the fewest steps. It pays in memory.
- **DFS is committed and cheap.** It follows one line of enquiry to its conclusion, which uses very little memory and can find some answer quickly. It pays in optimality, and sometimes in never terminating.

Use BFS when the shortest path matters and the graph is small enough to hold. Use DFS when memory is the binding constraint, when any valid solution will do, or when the structure being searched is deep and narrow rather than broad.

![Visual explanation of blind search comparison](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_blind_search_comparison.png)

## Uniform Cost Search: When Steps Cost Different Amounts

Now the assumption that has been quietly wrong all along. BFS gives Farhan the route through the fewest blocks, and he has been treating that as the fastest route. It is not the same thing.

The library corridor is a long outdoor path. The canteen corridor is a short covered one. Once walking minutes are attached to each connection, "fewest blocks" and "least time" stop agreeing, and it is time that Farhan actually cares about with an exam in forty minutes.

`Uniform cost search`, or UCS, handles this by keeping the frontier as a **priority queue** ordered by the total cost accumulated so far, always expanding the cheapest known partial route rather than the shortest or the newest.

Reading the code below: the map now carries a number on every corridor, so each entry is a pair of destination and minutes. The frontier changes from a queue to a `heapq`, which is Python's priority queue, and one new idea appears that BFS did not need.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzkkh7" 
 width="100%"
></iframe>

```
UCS route: Hostel Gate -> Canteen -> Sports Complex -> Science Block -> Exam Hall
Total walking time: 16 minutes
Fewest-block route: Hostel Gate -> Library -> Admin Block -> Exam Hall takes 24 minutes
```

There is the lesson, printed side by side. The route through three blocks takes twenty-four minutes. The route through four blocks takes sixteen. BFS confidently returned the slower one, because BFS was never measuring time.

Three pieces do the work, and one of them is new.

| In the code | What it is | Why it is there |
| --- | --- | --- |
| `(cost, path)` tuples | Cost first, route second | `heapq` sorts on the first element, so this orders the frontier by cost |
| `heapq.heappop` | Take the cheapest | Replaces `popleft` and `pop`; the only structural change from BFS |
| `settled` | Cheapest cost reached so far per block | **New.** BFS could mark a block visited on sight; UCS cannot |

That last row is the idea BFS did not need. In BFS, the first time you reach a block is always by the shortest route, so claiming it immediately is safe. With costs, a block can be reached early by an expensive route and later by a cheap one, so it can only be finalised when it comes off the frontier as the cheapest thing there. The `settled` check throws away the stale copies left behind.

One property is worth stating carefully, because it is often stated wrongly. **UCS returns the cheapest path, and it does so only when no connection has a negative cost.** It also generalises the earlier algorithm exactly: make every connection cost the same amount, and UCS behaves identically to BFS, because cheapest and fewest-steps become the same question.

![Visual explanation of uniform cost search: when steps cost different amounts](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_section_uniform_cost_search_when_steps_cost_different_amounts.png)

## The Three Blind Searches at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Algorithm</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Frontier</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Expands next</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it guarantees</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Main weakness</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>BFS</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Queue</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The oldest discovery, so the shallowest</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fewest steps, and it will find a solution if one exists</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Memory grows with each ring</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>DFS</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stack</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The newest discovery, so the deepest</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Very little; it finds some path if the branch is finite</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not shortest, and can run down an endless branch</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>UCS</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Priority queue by cost</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The cheapest partial route so far</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lowest total cost, given no negative costs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Explores in all directions, including away from the goal</td>
    </tr>
  </tbody>
</table>

The final cell of that table is the one to remember, because it is the flaw that motivates everything after this lesson. UCS is thorough and correct and completely undirected. Searching for a route from Bengaluru to Chennai, it will happily examine roads leading towards Mumbai, simply because they are cheap so far. It has no way to know that Mumbai is the wrong way.

![Visual explanation of bfs dfs ucs](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_bfs_dfs_ucs.png)

## Your Turn

The college opens a covered walkway connecting the library directly to the exam hall, six minutes long.

Before running anything, predict two things and write them down. What route will BFS now return, and how many blocks will it pass through? And will UCS still send Farhan through the canteen, given that the new route costs nine minutes to the library plus six more?

The program below is the two earlier functions unchanged, run against two maps that both gained one corridor. Nothing new is introduced; the only edits are the three lines marked NEW.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzkktq" 
 width="100%"
></iframe>

```
BFS now picks: Hostel Gate -> Library -> Exam Hall with 2 blocks
UCS now picks: Hostel Gate -> Library -> Exam Hall taking 15 minutes
```

This time the two agree, at fifteen minutes against the canteen route's sixteen. Now push it further yourself. Change the walkway from six minutes to eight and run it again. BFS will not budge, because BFS cannot see minutes at all, while UCS will switch back to the canteen. Sitting with that difference until it feels obvious is worth more than memorising either algorithm, because it is the difference between counting steps and measuring cost.
