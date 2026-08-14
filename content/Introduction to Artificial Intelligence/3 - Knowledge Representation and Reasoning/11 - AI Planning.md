## Introduction

A fulfilment warehouse outside Hosur runs a small fleet of picking robots, and Vikram, who maintains them, describes the first version of the software as a machine that knew everything and could do nothing.

It knew where every parcel sat. It knew where the robot was, whether the gripper was holding anything, and which aisles connected to which. Ask it any question about the warehouse and it answered correctly. Then an order arrived for two items, and the robot stood still, because knowing where the parcels are is not the same as knowing what to do about them.

Somebody had to work out that the robot must travel to aisle one, take the book, carry it to packing, put it down, go back for the cable, and bring that too. Nine separate actions, in an order where every one depends on the last, and where doing them in the wrong sequence achieves nothing: the gripper cannot take the cable while it holds the book, and it cannot put the book at packing without going there first.

Producing that sequence, from a description of the current situation and a description of the desired one, is a different job from anything in this unit so far. It is **AI planning**.

**Definition:** `AI planning` is the task of finding a sequence of actions that transforms a described initial state into a state satisfying a goal, where each action is specified by the conditions required before it can be taken and the changes it makes when taken.

![Opening scene: A fulfilment warehouse outside Hosur runs a small fleet of picking robots, and Vikram, who maintains them, describes the first version of the software as a machine that knew everything and could do…](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_section_introduction.png)

## Why Planning Is Not Just Search

Planning is a search problem, and treating it as an ordinary one throws away everything that makes it tractable. The difference is in what the algorithm is allowed to see.

In the search problems earlier in this course, a state was opaque. The algorithm knew states existed and that operators led from one to another, and nothing about what a state was made of.

In planning, the state is **factored**: it is a set of individual facts, and every action declares exactly which facts it requires and which it changes. That transparency buys three things.

1. **Actions are described once, generally.** A single "pick" description covers every parcel in every location, rather than a separate operator per combination.
2. **Relevance becomes visible.** Since an action states which facts it changes, a planner can work out which actions could possibly contribute to a goal and ignore the rest.
3. **Goals can be partial.** The goal is a set of facts that must hold, saying nothing about the others. "Both parcels at packing" does not care where the robot ends up, so any state satisfying those two facts will do.

![Visual explanation of why planning is not just search](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_section_why_planning_is_not_just_search_simple_v2.png)

## The STRIPS Representation

The standard way of describing an action has three parts, and it is named after an early planning system.

- **Preconditions.** The facts that must hold before the action can be taken.
- **Add list.** The facts that become true afterwards.
- **Delete list.** The facts that stop being true.

For the robot picking up a parcel:

| Part | Contents |
| --- | --- |
| Action | pick *parcel* at *place* |
| Preconditions | robot is at *place*, parcel is at *place*, gripper is empty |
| Delete | parcel is at *place*, gripper is empty |
| Add | holding *parcel* |

Read the delete list carefully, because it is doing something clever. Once the parcel is held, it is no longer *at* a place, and the gripper is no longer empty. Both facts must be withdrawn, or the robot would believe it could pick the same parcel twice.

This is also the practical answer to a problem raised earlier in the unit. Specifying everything an action leaves unchanged is impossible, and STRIPS avoids it by convention: **anything not in the add list or the delete list is unchanged.** Picking up a parcel does not affect where the other parcels are, and nobody has to say so. The representation makes the frame problem disappear by declaring what changes rather than what does not.

![Visual explanation of strips planning](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_strips_planning.png)

## Planning the Order

The warehouse is a line of four places, dock to aisle one to aisle two to packing, with a book in aisle one and a cable in aisle two. The robot starts at the dock with an empty gripper, and both parcels must reach packing.

Reading the code below: `build_actions` writes out every action the robot could ever take, as data. `plan` is a breadth-first search over states, and three expressions inside it are the entire STRIPS idea. Everything else is setup.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjfdh" 
 width="100%"
></iframe>

```
Goal: every parcel at packing
States explored: 52
Plan length: 9
  1. move dock -> aisle1
  2. pick book at aisle1
  3. move aisle1 -> aisle2
  4. move aisle2 -> packing
  5. drop book at packing
  6. move packing -> aisle2
  7. pick cable at aisle2
  8. move aisle2 -> packing
  9. drop cable at packing
```

That is the nine-step sequence Vikram's colleague had to work out by hand, produced from a description of the warehouse and a description of what was wanted.

Three expressions carry the whole planner, and all three are set operations.

| In the code | What it is | Why a set operation |
| --- | --- | --- |
| `action["pre"] <= state` | Is this action possible here? | Subset: are all preconditions present? |
| `(state - action["del"]) \| action["add"]` | **Apply the action** | Remove, then add. Everything unmentioned survives untouched |
| `goal <= nxt` | Are we finished? | Subset again, which is what lets the goal be partial |

The middle row is the entire STRIPS semantics in one expression, and it is also the answer to the frame problem. Nothing has to state that picking up a parcel leaves the other parcels alone; anything not named in the delete or add list simply passes through the subtraction and union unchanged.

The third row is worth its own note. Because the test is a subset rather than equality, the goal says nothing about where the robot ends up, and any state containing both parcels at packing satisfies it.

Notice the plan the search found. The robot carries the book past aisle two without picking up the cable, because it cannot hold both, and it comes back afterwards. Nobody encoded that constraint as a rule about strategy. It falls out of the gripper precondition, which is the point of describing actions rather than procedures.

![Visual explanation of planning the order](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_section_planning_the_order.png)

## Why Planning Gets Hard Quickly

The nine-step plan appeared instantly, which is misleading. Add parcels and watch.

Reading the code below: `build` now takes the parcel list as an argument, so the same warehouse can be created with one, two, or three parcels. The planner is unchanged from the previous program. The column to watch is `states explored`, not the plan length.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjfq4" 
 width="100%"
></iframe>

```
order      | actions | plan length | states explored
------------------------------------------------------
1 parcel   |      14 |           5 |               8
2 parcels  |      22 |           9 |              52
3 parcels  |      30 |          15 |             410
```

One parcel more each time, and the states explored go 8, then 52, then 410. The plan itself grows gently, from 5 steps to 9 to 15, while the work to find it multiplies by roughly eight each time.

The reason is that a plan of length 15 sits fifteen levels down a tree branching by the number of applicable actions, so the search space grows exponentially in plan length. A real order of twenty items in a warehouse of a hundred aisles is far beyond what this planner could touch.

This is why practical planners do not search blindly. They use heuristics derived automatically from the action descriptions themselves, the most common being to estimate the remaining cost by pretending that actions have no delete lists, which makes the relaxed problem easy to solve and yields an admissible estimate for the real one. That trick is only available because the actions are described declaratively, which is the payoff for the whole representation.

![Visual explanation of why planning gets hard quickly](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_section_why_planning_gets_hard_quickly.png)

## Why Subgoals Cannot Be Solved Separately

Looking at the nine-step plan, an obvious shortcut suggests itself. The goal has two parts, get the book to packing and get the cable to packing. Why not solve each separately and join the two plans together?

For this warehouse that happens to work, and in general it fails, for a reason worth understanding properly because it is the central difficulty of planning.

**Achieving one subgoal can undo another.** Solve subgoal A, then solve subgoal B, and the actions taken for B may destroy the conditions that A established. The two plans are individually correct and their concatenation is wrong.

A small change to the warehouse shows it. Suppose packing has a single dispatch slot that holds one parcel, so putting a parcel down there requires the slot to be free, and the delete list of the drop action removes `slot_free`. Now the plan for the book ends with the slot occupied, and the plan for the cable begins by requiring it free. Each plan is valid in isolation. Together they are not, and no amount of care in writing either one separately would reveal the conflict.

The classic illustration of this in the planning literature is a stack of three blocks in which any order of tackling the two subgoals forces you to undo work you have already done, so the shortest correct plan is strictly longer than either subgoal plan and cannot be produced by concatenating them. It is known as the Sussman anomaly, and it is famous precisely because it defeats the obvious approach so simply.

Two responses exist, and both are standard.

- **Plan for the conjunction.** Search over states satisfying the whole goal at once, which is what the planner above does, and why it found a nine-step plan rather than gluing two five-step plans into a longer and possibly broken one.
- **Detect and repair the interaction.** Build the subgoal plans separately, then check whether any action in one deletes a condition another depends on, and reorder or insert steps until no such conflict remains. This is the idea behind partial-order planning, which commits to an ordering between two actions only when their interaction forces it, and leaves everything else free.

The general lesson reaches beyond planning. **A goal made of parts is not the sum of its parts**, whenever achieving the parts involves shared resources, and shared resources are the normal case rather than the exception.

![Visual explanation of planning interactions](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_planning_interactions.png)

## What the Plan Quietly Assumes

The nine-step plan is correct, and it is correct about a warehouse that does not exist. Four assumptions are buried in the representation, and every one of them fails on a real floor.

1. **The world is fully known.** The planner was told where every parcel was. A real robot knows where the inventory system *says* the parcels are, which is a different claim, and shelves get restocked wrongly.

2. **Actions always succeed.** The gripper closes and the parcel is held. In practice a grip fails perhaps once in a hundred attempts, and the plan has no branch for that.

3. **Nothing else changes anything.** No other robot moves a parcel, no human takes one, and no aisle is blocked by a spill. A plan computed at nine o'clock assumes the warehouse of nine o'clock persists until the last step.

4. **The plan is executed in full.** There is no provision for stopping halfway, and no notion that a step might be worth reconsidering.

None of this makes planning useless, and pretending otherwise is the mistake. It means the plan is a starting point rather than a script, and real systems wrap it in two mechanisms.

**Execution monitoring** checks after each action whether the world matches what the plan expected. Since every action declares its add and delete lists, the expected state is already computed, so the check is simply a comparison against what the sensors report.

**Replanning** is what happens when the comparison fails. Rather than abandoning everything, the system takes the current actual state as a new initial state and plans again towards the same goal. If the grip failed, the robot is still at aisle one with an empty gripper and the book still on the shelf, so replanning from there produces a plan that begins by trying the grip again.

This plan-monitor-replan loop is how planning survives contact with reality, and it is worth recognising that it is the same instinct as re-planning in a stochastic environment: compute a plan, act, observe, and be willing to discard the rest of the plan when the world disagrees with it.

![Visual explanation of what the plan quietly assumes](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_section_what_the_plan_quietly_assumes.png)

## Planning at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Element</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it is</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">In the warehouse</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>State</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A set of facts that currently hold</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Robot at dock, gripper empty, book in aisle one</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Goal</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A set of facts that must hold, others unspecified</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Both parcels at packing, robot anywhere</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Precondition</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What must hold for an action to be possible</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Gripper empty, before picking anything up</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Add list</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Facts that become true</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Holding the book, after picking it</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Delete list</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Facts that stop being true; everything else is unchanged</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Book no longer in aisle one, gripper no longer empty</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Plan</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An ordered sequence of actions reaching the goal</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The nine steps printed above</td>
    </tr>
  </tbody>
</table>

![Visual explanation of planning at a glance](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_section_planning_at_a_glance.png)

## Your Turn

The warehouse manager is considering cutting a doorway directly from the dock to packing, and wants to know whether it is worth it.

Reading the code below: `build` now takes the corridor layout as its argument, so the identical planner can be run against two different warehouses. The two entries in `layouts` differ by exactly one pair.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjg5g" 
 width="100%"
></iframe>

```
corridor only: plan of 15 actions, 410 states explored
    1. pick charger at dock
    2. move dock -> aisle1
    3. move aisle1 -> aisle2
    4. move aisle2 -> packing
    5. drop charger at packing
    6. move packing -> aisle2
    7. move aisle2 -> aisle1
    8. pick book at aisle1
    9. move aisle1 -> aisle2
   10. move aisle2 -> packing
   11. drop book at packing
   12. move packing -> aisle2
   13. pick cable at aisle2
   14. move aisle2 -> packing
   15. drop cable at packing

with a short cut: plan of 13 actions, 368 states explored
    1. move dock -> aisle1
    2. pick book at aisle1
    3. move aisle1 -> aisle2
    4. move aisle2 -> packing
    5. drop book at packing
    6. move packing -> aisle2
    7. pick cable at aisle2
    8. move aisle2 -> packing
    9. drop cable at packing
   10. move packing -> dock
   11. pick charger at dock
   12. move dock -> packing
   13. drop charger at packing
```

Two actions saved, and notice something more interesting than the count: the plans differ in *strategy*, not merely in route. Without the shortcut the robot delivers the charger first, because it starts at the dock holding nothing and the charger is right there. With the shortcut it leaves the charger until last, because fetching it later is now cheap. Nobody encoded either strategy.

Now extend the model yourself. Give the robot a trolley that can hold two parcels at once, by replacing the single `gripper_empty` fact with two slots, and rerun the three-parcel order. Predict first whether the plan will shorten by two actions or by more, then check. Then work out why the number of states explored may go *up* even though the plan gets shorter, which is one of the least intuitive facts about planning and worth being able to explain.
