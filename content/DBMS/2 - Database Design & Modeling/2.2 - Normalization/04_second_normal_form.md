## Introduction

Arjun inherits the OrderItems `table` from Tara once the phone number mess is sorted out, and his job is to model the fact that a single order at Sunrise Traders can include several different products. An order for Ilyas Bakery Supplies might include notebooks and pens in the same order, so no single OrderID is enough to identify one line of that order, Arjun needs both the OrderID and the ProductID together.

That pair becomes the `table`'s composite `primary key`.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">OrderID</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">ProductID</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">ProductName</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">ProductPrice</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">O501</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">P01</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A4 Notebook</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">45</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">100</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">O502</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">P03</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Gel Pen Box</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">120</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">20</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">O503</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">P01</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A4 Notebook</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">45</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">200</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">O504</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">P02</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">File Folder</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">30</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">50</td>
    </tr>
  </tbody>
</table>

Every `row` here is already in 1NF, each cell holds one atomic value, no comma-separated lists anywhere. But Arjun notices something uncomfortable when he thinks about what the key actually needs:

- Quantity genuinely depends on both OrderID and ProductID together, since the same product ordered in two different orders can have two completely different quantities.
- ProductName and ProductPrice, though, do not care about OrderID at all, they are fully settled by ProductID alone. This mismatch, where some `columns` lean on only part of a `composite key` rather than the whole thing, is exactly what **Second `Normal Form`**, or 2NF, exists to catch and correct.

![Second Normal Form showing ProductName and ProductPrice depending only on ProductID, not the full composite key](images/07_second_normal_form_partial_dependency.png)

## Second Normal Form Builds Directly on First Normal Form

2NF has a prerequisite: a `table` must already be in 1NF before 2NF is even a meaningful question to ask, since 2NF is entirely about how non-key `columns` relate to the key, and that relationship is only worth examining once every `column` is confirmed to hold a single atomic value. Arjun's OrderItems `table` clears that bar already.

The new requirement 2NF adds is this: every non-key `column` must depend on the whole `primary key`, not on just a piece of it. A `table` with a single-`column` `primary key` automatically satisfies this, since there is no "part" of a single `column` to partially depend on.

The question only becomes interesting, and only becomes a risk, once a `table`'s key is composite, built from two or more `columns` working together.

## Finding the Partial Dependency

Arjun writes out exactly what each non-key `column` in OrderItems depends on.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Column</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Depends on</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Full key or partial key?</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quantity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">OrderID and ProductID together</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Full key, the quantity is specific to this exact order line</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">ProductName</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">ProductID alone</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Partial key, OrderID is irrelevant to the product&#x27;s name</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">ProductPrice</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">ProductID alone</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Partial key, OrderID is irrelevant to the product&#x27;s price</td>
    </tr>
  </tbody>
</table>

ProductName and ProductPrice are sitting in a `table` keyed by OrderID plus ProductID, but neither of them actually needs the OrderID half of that key at all. This is a **partial dependency**, a non-key `column` that depends on only part of a `composite key` rather than the whole thing, and it drags the same redundancy problem back in that 1NF just cleaned up.

Look at `rows` O501 and O503, both order A4 Notebook, and both repeat "A4 Notebook" and "45" all over again. If Sunrise Traders ever changes the price of an A4 Notebook, every single order line that ever ordered one needs to be found and updated, exactly the update anomaly Priya ran into with customer addresses, now showing up again for products.

## Splitting Off the Partially Dependent Columns

The fix follows directly from the dependency `table` Arjun just wrote. Any `column` that depends on only part of the key gets moved into a `table` keyed by that part alone.

OrderItems, keeping only what genuinely needs the full `composite key`:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">OrderID</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">ProductID</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">O501</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">P01</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">100</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">O502</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">P03</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">20</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">O503</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">P01</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">200</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">O504</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">P02</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">50</td>
    </tr>
  </tbody>
</table>

Products, keyed by ProductID alone, holding everything that only ever needed ProductID:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">ProductID</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">ProductName</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">ProductPrice</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">P01</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A4 Notebook</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">45</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">P02</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">File Folder</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">30</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">P03</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Gel Pen Box</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">120</td>
    </tr>
  </tbody>
</table>

Now A4 Notebook's name and price exist exactly once, in one `row` of Products, no matter how many order lines across Sunrise Traders' entire history have ever included it. Changing its price is a single edit in a single `row`.

OrderItems still records exactly what each order actually needs, which product, in what quantity, tied to which order, without dragging along facts that were never really about the order line in the first place.

![Fixing 2NF by moving ProductName and ProductPrice into a Products table keyed by ProductID](images/08_second_normal_form_split_products.png)

## Why This Matters Only When the Key Is Composite

It is worth being precise about when 2NF actually bites. If OrderItems had used a single manufactured OrderItemID as its `primary key` instead of the composite OrderID-plus-ProductID pair, there would technically be no `composite key` for anything to be "partial" against, and the textbook definition of 2NF would already be satisfied.

But the underlying redundancy, ProductName and ProductPrice repeating across every line that mentions the same product, would still be sitting right there in the data, just less visible under the formal rule.

Arjun treats 2NF as a genuine warning sign to hunt for, not merely a checkbox to satisfy by renaming the key, because the goal was never to pass the rule, it was to stop retyping the same product details over and over.

## Second Normal Form at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Check</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Before (fails 2NF)</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">After (meets 2NF)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Key shape</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Composite key: OrderID + ProductID</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">OrderItems keeps the composite key; Products gets its own single-column key</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">ProductName&#x27;s true dependency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Only needs ProductID, but sits in a table keyed by both</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lives in Products, keyed by ProductID alone</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost of a price change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every order line for that product must be found and updated</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One row in Products is updated</td>
    </tr>
  </tbody>
</table>

## Your Turn: Find the Partial Dependency

A college table EnrollmentGrades is keyed by the composite pair (RollNumber, CourseCode) and holds StudentName, CourseTitle, and Grade. Decide which non-key columns depend on the whole key and which depend on only part of it, then describe the split.

A working answer: Grade genuinely depends on the full pair, since a student's grade is specific to that student in that particular course. StudentName depends on RollNumber alone, and CourseTitle depends on CourseCode alone, both partial dependencies, exactly the pattern Arjun found with ProductName and ProductPrice. The fix splits the table into Students (RollNumber, StudentName), Courses (CourseCode, CourseTitle), and a slimmer EnrollmentGrades left holding only RollNumber, CourseCode, and Grade.

## Conclusion

Second `Normal Form` asks a `table` with a `composite key` one pointed question: does every non-key `column` genuinely need the whole key, or is some `column` really only attached to part of it?

Arjun's OrderItems `table` showed the classic pattern, a Quantity that truly depends on the order-and-product pair together, sitting alongside a ProductName and ProductPrice that only ever depended on the product half, and splitting the `table` along that seam removed the redundancy cleanly.

Not every redundant `table` has a `composite key` to blame, though. Sunrise Traders' Orders `table`, keyed by nothing more than a single OrderID, still manages to repeat a customer's city on every order that customer places, and explaining why that happens requires looking one step further down the chain of dependencies than 2NF alone can reach.