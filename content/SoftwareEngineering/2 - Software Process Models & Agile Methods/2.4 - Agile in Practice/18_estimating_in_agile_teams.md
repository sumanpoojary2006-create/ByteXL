## Introduction

Customers and managers want to know how long things will take, and developers are usually poor at predicting that in hours. Agile teams therefore estimate differently: they judge the size of work relative to other work, and use their measured speed to forecast. The goal is not a precise number but a good enough forecast to plan and make trade-offs.

**Definition:** Agile estimation is the practice of judging the relative size of backlog items, commonly in story points, and combining those sizes with the team's observed velocity to forecast how much can be delivered, with the understanding that estimates are approximations that improve with data.

<!--
IMAGE PROMPT  ->  generate as images/18_intro_estimating_in_agile_teams.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A row of cards labelled 1, 2, 3, 5, 8, 13 held by a team around a table, with a bar chart of past sprint velocity and a dotted forecast line extending to the right.

ON-IMAGE TEXT: show a short bold title "Estimating in Agile Teams" plus only these few labels, large and legible: Relative, Velocity, Forecast. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Why Estimating Is Hard

People are consistently optimistic about how long tasks take, a bias known as the **planning fallacy**. Work also contains unknowns, and the effort needed varies from person to person. An estimate is therefore a range of possibilities, and the earlier in the project, the wider the range (a pattern often called the cone of uncertainty).

## Relative Sizing and Story Points

Humans are far better at comparing than at measuring absolutely. It is easy to say that one task is about twice as large as another, and difficult to say that it will take 14 hours. **Story points** are a unit of relative size that combine the amount of work, its complexity, and its uncertainty. A story of 8 points is judged roughly twice as large as one of 4.

Teams often use a sequence that grows with the uncertainty of larger items, such as 1, 2, 3, 5, 8, 13, 20, adapted from the Fibonacci sequence. The gaps stop people arguing about false precision: nobody can reliably tell a 12 from a 13.

## Planning Poker

A common technique for team estimation is **planning poker**.

1. The Product Owner explains a story, and the team asks questions.
2. Each person privately chooses a card with their estimate.
3. All cards are revealed at the same time, which prevents anchoring on the first opinion spoken.
4. People with the highest and lowest estimates explain their reasoning.
5. The team discusses and re-estimates until the estimates converge.

The value lies in the **discussion**: differences reveal hidden assumptions and misunderstandings. A big gap often means the story is unclear or too large.

## Reference Stories

To keep points consistent, the team picks a few well-understood completed stories as a **reference** for each size, and compares new stories against them: is this more like our 3-point story or our 8-point one?

## Velocity and Forecasting

**Velocity** is the number of story points a team completes per sprint, counting only items that are fully done. After a few sprints, the average, or a range of recent values, gives a basis for forecasting.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Quantity</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Velocity of the last four sprints</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">21, 25, 19, 23 points</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Average velocity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">(21 + 25 + 19 + 23) divided by 4 = 22 points per sprint</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Remaining backlog for a release</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">110 points</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Forecast</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">110 divided by 22 = 5 sprints, with a likely range of about 5 to 6 sprints</td>
    </tr>
  </tbody>
</table>

The forecast is a planning aid, and is revised as velocity and the backlog change.

<!--
IMAGE PROMPT  ->  generate as images/02_velocity_forecast_chart.png   (16:9 explanatory diagram, place here)

A bar chart of four past sprint velocities (21, 25, 19, 23) with an average line at 22, and a burn-up chart beside it showing remaining backlog of 110 points and a projected completion in sprint five to six.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Misuses to Avoid

- **Treating estimates as commitments.** An estimate is a best guess, not a promise.
- **Comparing velocity between teams.** Points are relative to each team and are not a common unit.
- **Using velocity as a target.** If people are rewarded for velocity, points inflate and the number loses meaning.
- **Converting points into hours.** This brings back false precision and defeats the purpose of relative sizing.
- **Estimating too far ahead in detail.** Items far down the backlog should have rough sizes only.

Some teams go further and use **no estimates**, instead splitting work into similarly sized small items and counting them, using flow measures such as throughput.

## Your Turn: Forecast

1. A team's last three sprints delivered 18, 24, and 21 points. Estimate its average velocity.
2. The remaining backlog is 84 points. About how many sprints does that need?
3. A manager wants to compare two teams by their velocity. Is this valid?

The average velocity is (18 + 24 + 21) divided by 3, which is 21 points per sprint. The remaining work of 84 points needs about 84 divided by 21, which is 4 sprints. Comparing teams by velocity is not valid, because story points are relative sizes defined by each team and are not a standard measure of output.

## Conclusion

Agile estimation is the practice of judging the relative size of backlog items, commonly in story points, and combining those sizes with the team's observed velocity to forecast how much can be delivered, with the understanding that estimates are approximations that improve with data. Its purpose is useful planning, not false precision.

For any forecast to mean something, "completed" must mean the same thing every time. The next topic defines when work is truly done.
