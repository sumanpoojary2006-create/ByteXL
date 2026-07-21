## Introduction

Arjun manages pricing for a small electronics store, and the `products` `table` holds costs and margins as raw decimal numbers, exactly as calculated. The problem is that "exactly as calculated" is not how a price tag or an invoice should look:

- A price of 1499.996 needs to round to 1500.00 before it reaches a customer.
- A margin percentage needs rounding to a sensible number of decimal places for a report.
- A shipping-weight calculation occasionally produces a negative number that should really just be its positive distance from zero.

SQL's built-in **numeric `functions`** handle exactly this kind of cleanup, right inside the `query`.

![ROUND turning an over-precise selling price into a customer-ready price](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_round_price_display_precision.png)

**Definition:** Numeric `functions` turn raw, over-precise, or oddly signed numbers into values fit for a report or a receipt: `ROUND` for display precision, `CEIL` and `FLOOR` for deliberate rounding direction, `ABS` for magnitude regardless of sign, and `MOD` for remainders.

## Rounding to a Sensible Precision

The `products` `table` stores prices with more decimal precision than any customer needs to see.

Before applying any function, inspect the source data:

| product_id | product_name | cost_price | selling_price | stock_weight_kg | stock_units |
| ---------: | ----------------- | ---------: | ------------: | --------------: | ----------: |
| 1 | Wireless Mouse | 349.6789 | 599.9950 | 0.1450 | 24 |
| 2 | USB-C Cable | 89.3333 | 149.0000 | 0.0500 | 13 |
| 3 | Bluetooth Speaker | 1120.4567 | 1899.9900 | 0.6200 | 18 |
| 4 | Laptop Stand | 610.1111 | 999.5000 | 1.3000 | 7 |
| 5 | Webcam | 780.8888 | -1249.0000 | 0.2100 | 12 |

Arjun wants customer-ready whole-number prices. The query is `SELECT product_name, selling_price, ROUND(selling_price, 0) AS rounded_price FROM products;`. The second argument, `0`, tells PostgreSQL that no decimal places should remain.

## Hands-On Practice: Round Product Prices

The OneCompiler exercise uses two files. `init.sql` creates and populates the displayed `products` table. The active query file contains only the numeric-function query being practised. Where a query does not include `ORDER BY`, the database may return the correct rows in a different order from the example output.

First, `init.sql` prepares the dataset:

```postgresql file=init.sql
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    cost_price NUMERIC(10, 4),
    selling_price NUMERIC(10, 4),
    stock_weight_kg NUMERIC(10, 4),
    stock_units INTEGER
);

INSERT INTO products (product_id, product_name, cost_price, selling_price, stock_weight_kg, stock_units) VALUES
(1, 'Wireless Mouse', 349.6789, 599.9950, 0.1450, 24),
(2, 'USB-C Cable', 89.3333, 149.0000, 0.0500, 13),
(3, 'Bluetooth Speaker', 1120.4567, 1899.9900, 0.6200, 18),
(4, 'Laptop Stand', 610.1111, 999.5000, 1.3000, 7),
(5, 'Webcam', 780.8888, -1249.0000, 0.2100, 12);
```

Then the active query file rounds each selling price:

Before running the active query, read its `SELECT` list and clauses against the displayed source rows. Then compare the returned values with the expected output to see exactly what the function or operation changed.

```postgresql with=init.sql
SELECT product_name, selling_price, ROUND(selling_price, 0) AS rounded_price
FROM products;
```

Expected output:

| product_name | selling_price | rounded_price |
| ----------------- | ------------: | ------------: |
| Wireless Mouse | 599.9950 | 600 |
| USB-C Cable | 149.0000 | 149 |
| Bluetooth Speaker | 1899.9900 | 1900 |
| Laptop Stand | 999.5000 | 1000 |
| Webcam | -1249.0000 | -1249 |

- `ROUND(value, 0)` rounds `selling_price` to the nearest whole number, which is what a price tag needs.
- The second argument controls how many decimal places survive the rounding, so `ROUND(selling_price, 2)` would keep two decimal places instead of zero, useful when a currency still needs cents shown.

## Rounding Up and Rounding Down on Purpose

Sometimes a plain round is the wrong choice. If Arjun is calculating how many boxes are needed to ship a fractional number of kilograms, rounding down would leave stock behind, so he needs to always round up.

He compares both directions with `SELECT product_name, stock_weight_kg, CEIL(stock_weight_kg) AS boxes_needed_if_1kg_each, FLOOR(stock_weight_kg) AS full_kg_only FROM products;`. `CEIL` answers the capacity question, while `FLOOR` counts only complete kilograms.

```postgresql with=init.sql
SELECT product_name, stock_weight_kg,
       CEIL(stock_weight_kg) AS boxes_needed_if_1kg_each,
       FLOOR(stock_weight_kg) AS full_kg_only
FROM products;
```

Expected output:

| product_name | stock_weight_kg | boxes_needed_if_1kg_each | full_kg_only |
| ----------------- | --------------: | ------------------------: | -----------: |
| Wireless Mouse | 0.1450 | 1 | 0 |
| USB-C Cable | 0.0500 | 1 | 0 |
| Bluetooth Speaker | 0.6200 | 1 | 0 |
| Laptop Stand | 1.3000 | 2 | 1 |
| Webcam | 0.2100 | 1 | 0 |

- `CEIL` (short for ceiling) always rounds up to the next whole number, so 0.145 becomes 1 and 1.3 becomes 2, guaranteeing enough capacity.
- `FLOOR` does the opposite, always rounding down, which is useful when Arjun only wants to count complete, full kilograms and discard the leftover fraction.

## Working with Distance from Zero and Remainders

The webcam `row` has a `selling_price` of -1249.0000, a data-entry mistake from a refund adjustment that got applied to the wrong `column`. Before fixing the source data, Arjun wants to measure its distance from zero. The query is `SELECT product_name, selling_price, ABS(selling_price) AS positive_price FROM products WHERE selling_price < 0;`.

```postgresql with=init.sql
SELECT product_name, selling_price, ABS(selling_price) AS positive_price
FROM products
WHERE selling_price < 0;
```

Expected output:

| product_name | selling_price | positive_price |
| ------------ | ------------: | -------------: |
| Webcam | -1249.0000 | 1249.0000 |

Arjun also packs stock into cartons of six units. The query `SELECT product_name, stock_units, stock_units % 6 AS units_left_over FROM products;` returns the remainder after forming as many complete cartons as possible.

```postgresql with=init.sql
SELECT product_name, stock_units, stock_units % 6 AS units_left_over
FROM products;
```

Expected output:

| product_name | stock_units | units_left_over |
| ----------------- | ----------: | --------------: |
| Wireless Mouse | 24 | 0 |
| USB-C Cable | 13 | 1 |
| Bluetooth Speaker | 18 | 0 |
| Laptop Stand | 7 | 1 |
| Webcam | 12 | 0 |

- `ABS` strips the sign off a number, turning -1249.0000 into 1249.0000, which is what flagged the webcam `row` as suspicious in the first place: a price should never be negative.
- The `%` operator, also written as `MOD(a, b)` in some `databases`, returns the remainder of a division. A remainder of 0 means every unit fits into complete cartons of six; a remainder of 1 means one unit is left over.

![CEIL, FLOOR, ABS, and remainder reshaping numeric values for reports](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_numeric_functions_rounding_abs_mod.png)

## A Few Values Worked Out by Hand

Seeing a handful of inputs and outputs side by side makes each `function`'s behavior easy to check:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Function call</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Result</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>ROUND(599.995, 2)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>600.00</code></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>CEIL(0.145)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>1</code></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>FLOOR(1.3)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>1</code></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>ABS(-1249.00)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>1249.00</code></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>7 % 6</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>1</code></td>
    </tr>
  </tbody>
</table>

## Numeric Functions at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Function</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>ROUND(value, places)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Round to a given number of decimals</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>ROUND(599.995, 2)</code></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>CEIL(value)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Always round up</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>CEIL(0.145)</code> -&gt; <code>1</code></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>FLOOR(value)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Always round down</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>FLOOR(1.3)</code> -&gt; <code>1</code></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>ABS(value)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Distance from zero</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>ABS(-1249)</code> -&gt; <code>1249</code></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>MOD(a, b)</code> / <code>a % b</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Remainder after division</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>10 % 3</code> -&gt; <code>1</code></td>
    </tr>
  </tbody>
</table>

## Your Turn

Arjun needs a margin report: for every product, show the product name and the profit margin (`selling_price - cost_price`) rounded to two decimal places, aliased as `margin`. Write that `query` against the `products` `table` above.

The calculation happens before rounding: `ROUND(selling_price - cost_price, 2)` subtracts the stored cost from the selling price and then keeps two decimal places.

```postgresql with=init.sql
-- Write your query below
```

If your `query` is `SELECT product_name, ROUND(selling_price - cost_price, 2) AS margin FROM products;`, the webcam `row` will show a large negative margin, one more confirmation that its price needs a manual fix.

Expected output:

| product_name | margin |
| ----------------- | -------: |
| Wireless Mouse | 250.32 |
| USB-C Cable | 59.67 |
| Bluetooth Speaker | 779.53 |
| Laptop Stand | 389.39 |
| Webcam | -2029.89 |

## Conclusion

Numeric `functions` turn raw, over-precise, or oddly signed numbers into values fit for a report or a receipt: `ROUND` for display precision, `CEIL` and `FLOOR` for deliberate rounding direction, `ABS` for magnitude regardless of sign, and `MOD` for remainders. Arjun cleaned up prices and packing counts without changing a single stored value, only how the `query` presented them.

Dates and times bring their own quirks, and SQL has a matching toolkit for those too.
