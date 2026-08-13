# Unit 3: Knowledge Representation and Reasoning

**Introduction to Artificial Intelligence**

Goal of this unit: represent knowledge and apply logical and probabilistic reasoning to support intelligent decision-making.

Key question this unit answers: **How do intelligent systems represent knowledge and reason?**

The unit moves through three stages. It opens with the architecture that separates what a system knows from how it reasons, and with the question of what knowledge even looks like once written down. It then builds the formal machinery: rules, propositional logic, predicate logic, entailment, and the two directions in which inference can run. It closes by relaxing the assumption that everything is known for certain, moving to probability and Bayesian reasoning, and finally to producing sequences of actions that achieve a goal.

## Topics (teach in order)

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">#</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Topic</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">File</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Knowledge-Based Systems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="01%20-%20Knowledge-Based%20Systems.md">01 - Knowledge-Based Systems.md</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Knowledge Representation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="02%20-%20Knowledge%20Representation.md">02 - Knowledge Representation.md</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">3</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rule-Based Reasoning</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="03%20-%20Rule-Based%20Reasoning.md">03 - Rule-Based Reasoning.md</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">4</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Propositional Logic</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="04%20-%20Propositional%20Logic.md">04 - Propositional Logic.md</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">5</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">First-Order Predicate Logic</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="05%20-%20First-Order%20Predicate%20Logic.md">05 - First-Order Predicate Logic.md</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">6</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Logical Inference</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="06%20-%20Logical%20Inference.md">06 - Logical Inference.md</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">7</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inference Techniques</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="07%20-%20Inference%20Techniques.md">07 - Inference Techniques.md</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Semantic Knowledge Models</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="08%20-%20Semantic%20Knowledge%20Models.md">08 - Semantic Knowledge Models.md</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reasoning Under Uncertainty</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="09%20-%20Reasoning%20Under%20Uncertainty.md">09 - Reasoning Under Uncertainty.md</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">10</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Bayesian Networks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="10%20-%20Bayesian%20Networks.md">10 - Bayesian Networks.md</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">11</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">AI Planning</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="11%20-%20AI%20Planning.md">11 - AI Planning.md</a></td>
    </tr>
  </tbody>
</table>

**Style:** professional, beginner-friendly, no emojis, no em dashes; standardized "Introduction" heading, narrative flow. Topics 3, 4, 6, 7, 9, and 11 carry runnable Python, where every block is self-contained and prints its own output. The remaining topics are conceptual and teach through worked tables instead.
