## Introduction

Meera is a business analyst brought in to help Sunrise Traders untangle the anomalies Priya kept running into with the combined Orders `table`, the address that forgot to update everywhere, the product that could not be added until someone bought it, the customer record that vanished when an order was cancelled.

Meera's manager asks her a deceptively simple question: "Before we redesign anything, can you tell me exactly which `column` depends on which?" Meera realizes she needs a precise, almost mathematical way to answer that, not a vague sense that "these seem related."

The tool she reaches for is called a **`functional dependency`**, and it says something very specific: if you know the value in one `column`, does that guarantee you can know the value in another `column`, every single time, without exception?

- If CustomerID C12 always means the shop is Ilyas Bakery Supplies, and it can never mean anything else, then CustomerID determines CustomerName.
- `Functional dependencies` are the precise, rule-based foundation that every later decision about splitting or keeping a `table` rests on, and Meera spends her first afternoon simply writing them down.

![Functional dependency shown as X determining Y with CustomerID and RollNumber examples](images/03_functional_dependency_x_determines_y.png)

## What "X Determines Y" Actually Means

A `functional dependency` is usually written as X determines Y, meaning that for any two `rows` that share the same value of X, they must also share the same value of Y. It is not enough for X and Y to usually match up, the rule has to hold with certainty, for every `row`, always.

Meera tests this against Sunrise Traders' data using CustomerID and CustomerName. Every `row` with CustomerID C12 says "Ilyas Bakery Supplies," with no exceptions anywhere in the `table`.

So CustomerID determines CustomerName.

She writes it the way `database` designers do:

CustomerID -> CustomerName

The `column` on the left, CustomerID, is called the determinant. The `column` on the right, CustomerName, is the dependent `column`. Once Meera fixes a CustomerID, the CustomerName is no longer free to vary, it is pinned down completely.

## A Familiar Shape: Roll Number and Student Name

Meera explains the idea to a colleague using a simpler, more familiar example first: in any properly run college, a Roll Number determines a Student Name. Given Roll Number 21CS045, there is exactly one correct answer to "whose roll number is this," and that answer never changes depending on which `row` of a `table` you happen to be looking at.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">RollNumber</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">StudentName</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">21CS045</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Naina Fernandes</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">21CS046</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Arjun Rao</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">21CS047</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Naina Fernandes</td>
    </tr>
  </tbody>
</table>

Even though "Naina Fernandes" appears twice in this small `table`, attached to two different roll numbers, that does not break the dependency. A `functional dependency` only requires that the same X always produces the same Y, it says nothing about whether the same Y can come from more than one X. RollNumber -> StudentName holds perfectly here, because every occurrence of a given roll number brings the same name with it.

## Reading Functional Dependencies Out of Sunrise Traders' Data

Back at Sunrise Traders, Meera lists out every `functional dependency` she can spot in the old combined Orders `table`.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Determinant</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Dependent column</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Why it holds</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">CustomerID</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">CustomerName, CustomerAddress, CustomerPhone</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every order placed by the same customer shows the same name, address, and phone</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">ProductID</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">ProductName, ProductPrice</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every order line for the same product shows the same name and price</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">OrderID</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">OrderDate, CustomerID</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Each order happened on exactly one date, placed by exactly one customer</td>
    </tr>
  </tbody>
</table>

- Each `row` in this `table` represents a rule Meera can rely on absolutely.
- Given a CustomerID, the customer's name, address, and phone are no longer in question.
- Given a ProductID, the product's name and price are settled.
- These are the threads that, once pulled apart, tell Meera exactly which facts belong together in the same `table`.

## Partial Dependency: When Only Part of the Key Is Needed

Some of Sunrise Traders' data is identified not by a single `column` but by a combination, an OrderID together with a ProductID uniquely identifies one line of an order, since the same order can include several different products. Meera notices something odd when she looks at ProductName under this combined key: ProductName does not actually need the OrderID at all, it is fully explained by ProductID alone.

A dependency where a `column` depends on only part of a `composite key`, rather than the whole key, is called a **partial dependency**. It is a warning sign that a fact is being stored in a `table` keyed by more information than that fact actually needs.

## Transitive Dependency: A Chain of Two Hops

Meera spots a second, subtler pattern while looking at a simplified Orders `table` that stores OrderID, CustomerID, and CustomerCity together. OrderID determines CustomerID, since each order belongs to one customer, and CustomerID determines CustomerCity, since each customer has one registered city. But notice what that means for OrderID and CustomerCity: OrderID does not describe CustomerCity directly, it only gets there by first passing through CustomerID.

This two-hop chain, where a `column` depends on the key only indirectly, through another non-key `column`, is called a **transitive dependency**. Meera flags it for later, sensing that a fact reached only by a detour through another fact is probably not sitting in the right `table`.

![Dependency checker comparing full dependency, partial dependency, and transitive dependency](images/04_dependency_checker_partial_transitive.png)

## Functional Dependencies at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Idea</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it means</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Sunrise Traders example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Functional dependency (X -&gt; Y)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Knowing X guarantees Y, with no exceptions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">CustomerID -&gt; CustomerAddress</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Determinant</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The column on the left, the one doing the determining</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">CustomerID</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Partial dependency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A column depends on only part of a composite key</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">ProductName depends on ProductID alone, not on OrderID + ProductID together</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Transitive dependency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A column depends on the key only through another non-key column</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">CustomerCity depends on CustomerID, which depends on OrderID</td>
    </tr>
  </tbody>
</table>

## Your Turn: Write the Dependencies

A college table stores RollNumber, StudentName, DepartmentCode, DepartmentName, and DepartmentHOD (head of department) together, keyed by RollNumber. Write out the functional dependencies you can find, and identify which one is transitive.

A working answer: RollNumber -> StudentName, DepartmentCode holds directly since a roll number pins down exactly one student and one department code. DepartmentCode -> DepartmentName and DepartmentCode -> DepartmentHOD hold too, since every department has exactly one name and one head. The transitive one is RollNumber -> DepartmentName (and DepartmentHOD), reached only by first passing through DepartmentCode, a non-key column, meaning department facts are riding along on every student row rather than living where they truly belong.

## Conclusion

A `functional dependency` turns "these `columns` seem related" into a precise, testable rule: given a value in one `column`, exactly one value in another `column` is guaranteed, every time. Meera's afternoon of writing down CustomerID -> CustomerName, ProductID -> ProductPrice, and OrderID -> CustomerID gave Sunrise Traders something Priya's instinct never could, an exact map of which facts belong to which real-world thing.

Along the way, Meera also noticed two shapes worth watching for:

The first is a dependency on only part of a `composite key`. The second is a dependency reached only by a detour through another `column`.

Both turn out to be exactly the patterns that a disciplined, step-by-step process checks for, one refinement at a time, when it decides how a `table` ought to be split.
