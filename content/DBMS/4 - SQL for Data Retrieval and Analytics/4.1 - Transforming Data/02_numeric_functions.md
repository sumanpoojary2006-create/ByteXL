## Introduction

Arjun manages pricing for a small electronics store, and the `products` `table` holds costs and margins as raw decimal numbers, exactly as calculated. The problem is that "exactly as calculated" is not how a price tag or an invoice should look:

- A price of 1499.996 needs to round to 1500.00 before it reaches a customer.
- A margin percentage needs rounding to a sensible number of decimal places for a report.
- A shipping-weight calculation occasionally produces a negative number that should really just be its positive distance from zero.

SQL's built-in **numeric `functions`** handle exactly this kind of cleanup, right inside the `query`.

## Rounding to a Sensible Precision

The `products` `table` stores prices with more decimal precision than any customer needs to see.

```text
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    cost_price NUMERIC(10, 4),
    selling_price NUMERIC(10, 4),
    stock_weight_kg NUMERIC(10, 4)
);

INSERT INTO products (product_id, product_name, cost_price, selling_price, stock_weight_kg) VALUES
(1, 'Wireless Mouse', 349.6789, 599.9950, 0.1450),
(2, 'USB-C Cable', 89.3333, 149.0000, 0.0500),
(3, 'Bluetooth Speaker', 1120.4567, 1899.9900, 0.6200),
(4, 'Laptop Stand', 610.1111, 999.5000, 1.3000),
(5, 'Webcam', 780.8888, -1249.0000, 0.2100);
```

```postgresql
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    cost_price NUMERIC(10, 4),
    selling_price NUMERIC(10, 4),
    stock_weight_kg NUMERIC(10, 4)
);

INSERT INTO products (product_id, product_name, cost_price, selling_price, stock_weight_kg) VALUES
(1, 'Wireless Mouse', 349.6789, 599.9950, 0.1450),
(2, 'USB-C Cable', 89.3333, 149.0000, 0.0500),
(3, 'Bluetooth Speaker', 1120.4567, 1899.9900, 0.6200),
(4, 'Laptop Stand', 610.1111, 999.5000, 1.3000),
(5, 'Webcam', 780.8888, -1249.0000, 0.2100);

-- Query
SELECT product_name, selling_price, ROUND(selling_price, 0) AS rounded_price
FROM products;
```

- `ROUND(value, 0)` rounds `selling_price` to the nearest whole number, which is what a price tag needs.
- The second argument controls how many decimal places survive the rounding, so `ROUND(selling_price, 2)` would keep two decimal places instead of zero, useful when a currency still needs cents shown.

![ROUND turning an over-precise selling price into a customer-ready price](images/03_round_price_display_precision.png)

## Rounding Up and Rounding Down on Purpose

Sometimes a plain round is the wrong choice. If Arjun is calculating how many boxes are needed to ship a fractional number of kilograms, rounding down would leave stock behind, so he needs to always round up.

```postgresql
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    cost_price NUMERIC(10, 4),
    selling_price NUMERIC(10, 4),
    stock_weight_kg NUMERIC(10, 4)
);

INSERT INTO products (product_id, product_name, cost_price, selling_price, stock_weight_kg) VALUES
(1, 'Wireless Mouse', 349.6789, 599.9950, 0.1450),
(2, 'USB-C Cable', 89.3333, 149.0000, 0.0500),
(3, 'Bluetooth Speaker', 1120.4567, 1899.9900, 0.6200),
(4, 'Laptop Stand', 610.1111, 999.5000, 1.3000),
(5, 'Webcam', 780.8888, -1249.0000, 0.2100);

-- Query
SELECT product_name, stock_weight_kg,
       CEIL(stock_weight_kg) AS boxes_needed_if_1kg_each,
       FLOOR(stock_weight_kg) AS full_kg_only
FROM products;
```

- `CEIL` (short for ceiling) always rounds up to the next whole number, so 0.145 becomes 1 and 1.3 becomes 2, guaranteeing enough capacity.
- `FLOOR` does the opposite, always rounding down, which is useful when Arjun only wants to count complete, full kilograms and discard the leftover fraction.

## Working with Distance from Zero and Remainders

The webcam `row` has a `selling_price` of -1249.0000, a data-entry mistake from a refund adjustment that got applied to the wrong `column`. Before fixing the source data, Arjun wants to see how far off each price is from zero, and separately, he wants to know which products can be packed into cartons of 6 with none left over.

```postgresql
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    cost_price NUMERIC(10, 4),
    selling_price NUMERIC(10, 4),
    stock_weight_kg NUMERIC(10, 4)
);

INSERT INTO products (product_id, product_name, cost_price, selling_price, stock_weight_kg) VALUES
(1, 'Wireless Mouse', 349.6789, 599.9950, 0.1450),
(2, 'USB-C Cable', 89.3333, 149.0000, 0.0500),
(3, 'Bluetooth Speaker', 1120.4567, 1899.9900, 0.6200),
(4, 'Laptop Stand', 610.1111, 999.5000, 1.3000),
(5, 'Webcam', 780.8888, -1249.0000, 0.2100);

-- Query
SELECT product_name, selling_price, ABS(selling_price) AS positive_price
FROM products
WHERE selling_price < 0;
```

```postgresql
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    cost_price NUMERIC(10, 4),
    selling_price NUMERIC(10, 4),
    stock_weight_kg NUMERIC(10, 4)
);

INSERT INTO products (product_id, product_name, cost_price, selling_price, stock_weight_kg) VALUES
(1, 'Wireless Mouse', 349.6789, 599.9950, 0.1450),
(2, 'USB-C Cable', 89.3333, 149.0000, 0.0500),
(3, 'Bluetooth Speaker', 1120.4567, 1899.9900, 0.6200),
(4, 'Laptop Stand', 610.1111, 999.5000, 1.3000),
(5, 'Webcam', 780.8888, -1249.0000, 0.2100);

-- Query
SELECT product_id, product_name, product_id % 6 AS remainder_when_packed_in_sixes
FROM products;
```

- `ABS` strips the sign off a number, turning -1249.0000 into 1249.0000, which is what flagged the webcam `row` as suspicious in the first place: a price should never be negative.
- The `%` operator, also written as `MOD(a, b)` in some `databases`, returns the remainder of a division, and here it shows which product IDs would divide evenly into groups of 6 (a remainder of 0) versus which would not.

![CEIL, FLOOR, ABS, and remainder reshaping numeric values for reports](images/04_numeric_functions_rounding_abs_mod.png)

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

```postgresql
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    cost_price NUMERIC(10, 4),
    selling_price NUMERIC(10, 4),
    stock_weight_kg NUMERIC(10, 4)
);

INSERT INTO products (product_id, product_name, cost_price, selling_price, stock_weight_kg) VALUES
(1, 'Wireless Mouse', 349.6789, 599.9950, 0.1450),
(2, 'USB-C Cable', 89.3333, 149.0000, 0.0500),
(3, 'Bluetooth Speaker', 1120.4567, 1899.9900, 0.6200),
(4, 'Laptop Stand', 610.1111, 999.5000, 1.3000),
(5, 'Webcam', 780.8888, -1249.0000, 0.2100);

-- Query
-- Write your query below
```

If your `query` is `SELECT product_name, ROUND(selling_price - cost_price, 2) AS margin FROM products;`, the webcam `row` will show a large negative margin, one more confirmation that its price needs a manual fix.

## Conclusion

Numeric `functions` turn raw, over-precise, or oddly signed numbers into values fit for a report or a receipt: `ROUND` for display precision, `CEIL` and `FLOOR` for deliberate rounding direction, `ABS` for magnitude regardless of sign, and `MOD` for remainders. Arjun cleaned up prices and packing counts without changing a single stored value, only how the `query` presented them.

Dates and times bring their own quirks, and SQL has a matching toolkit for those too.
