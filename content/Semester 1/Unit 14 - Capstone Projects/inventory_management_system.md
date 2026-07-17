# Capstone Project: Inventory Management System

## Background

Small businesses in India — kirana stores, stationery shops, electronics retailers — often manage stock in notebooks or basic spreadsheets, leading to stockouts, over-ordering, and lost sales. StockSense is a command-line inventory management system that tracks products, processes orders, alerts on low stock, and generates restocking reports.

This project draws on everything from Units 1 through 13: input validation, loops, lists and dictionaries, functions, file handling, basic OOP, and exception handling. You will build it in six stages, from a single product entry to a multi-supplier, file-backed inventory system.

## Stages

### Stage 1: Add a Product to Inventory

1. Ask the user to enter details for one product:
   - Product name (text)
   - Product ID (text — unique identifier)
   - Category (text — e.g. Electronics, Stationery, Grocery, Clothing)
   - Unit price (float, in ₹)
   - Quantity in stock (integer)
   - Reorder level (integer — alert when stock falls below this)

2. Display a product card after adding:
   ```
   ----------------------------------------
   PRODUCT ADDED
   ----------------------------------------
   ID          : PROD001
   Name        : Notebook A4
   Category    : Stationery
   Price       : ₹ 45.00
   Stock       : 200 units
   Reorder At  : 50 units
   ----------------------------------------
   ```

3. Validate that unit price and quantity are positive numbers. Validate that reorder level is less than the initial quantity.

**Answer these questions after completing Stage 1:**
- Your reorder level validation requires it to be less than initial quantity. But what if a business wants a reorder level of 500 for a product they currently have 200 of — is your validation too strict?
- Product ID is entered by the user. What could go wrong if two products are given the same ID, and what will you do about it in Stage 2?

### Stage 2: Manage Multiple Products with a Menu

1. Build a main menu:
   ```
   ========== StockSense ==========
   1. Add Product
   2. View All Products
   3. Search Product
   4. Update Stock
   5. Remove Product
   6. Exit
   ================================
   ```

2. Store products in a dictionary keyed by product ID. This enforces uniqueness and allows O(1) lookup.

3. Search should work by product name (partial, case-insensitive) or by product ID (exact match).

4. Update Stock: takes a product ID and a quantity change (positive to add stock, negative to reduce). Reject updates that would make stock go below 0.

5. After every stock update, check if the product has fallen below its reorder level. If so, display an alert immediately.

**Answer these questions after completing Stage 2:**
- You store products in a dictionary keyed by product ID. What is the tradeoff versus using a list? When would a list be the better choice here?
- A stock update of -10 is applied to a product with 8 units. Your program rejects this. But what if this represents a confirmed sale that already happened — should you still reject it?

### Stage 3: Order Processing

1. Add a **Process Sale** option: the user selects a product ID and quantity sold. The system deducts the quantity, records the sale with a timestamp, and displays a sale receipt.

2. Add a **Restock Order** option: the user selects a product ID and quantity to add. Stock increases and the restock is recorded with a timestamp.

3. Maintain a transaction log: a list of records with `type` (Sale / Restock), `product_id`, `quantity`, `timestamp`, and `total_value` (quantity × price for sales).

4. Add a **Daily Sales Report** option: displays all sales for today, total revenue, and which product generated the most revenue.

**Answer these questions after completing Stage 3:**
- Your daily sales report filters transactions by today's date. What happens to transactions from yesterday — are they lost or just not displayed? How would a user access last week's sales?
- Total revenue is computed as quantity × price at the time of sale. What if a product's price changes after some sales are recorded — should historical sales reflect the old or new price?

### Stage 4: Low Stock Alerts and Supplier Management

1. Add a **Stock Alerts** option: displays all products currently below their reorder level, sorted by how far below the reorder level they are.

2. Add a **Supplier** registry: each supplier has a name, contact number, and a list of product IDs they supply.

3. When a product falls below reorder level, the alert should also display the supplier name and contact for that product.

4. Add an **Inventory Valuation** option: displays the total value of current stock (quantity × price for each product, summed).

**Answer these questions after completing Stage 4:**
- A product can have multiple suppliers. How did you store this relationship? What does your alert display when a product has two suppliers?
- Inventory valuation uses current price × current quantity. Is this the right formula for a business that bought stock at different prices at different times? What does this limitation mean for the accuracy of the report?

### Stage 5: Redesign with Classes

1. Create a `Product` class with attributes `product_id`, `name`, `category`, `price`, `quantity`, `reorder_level` and methods `update_stock(change)`, `is_below_reorder()`, `value()`, and `__str__`.

2. Create a `Transaction` class with attributes `type`, `product_id`, `quantity`, `timestamp`, `total_value` and a `__str__` method.

3. Create an `Inventory` class that holds a dictionary of products and a list of transactions. Move all business logic into `Inventory` methods: `add_product`, `search`, `process_sale`, `restock`, `get_alerts`, `daily_report`, `total_valuation`.

4. The main menu calls only `Inventory` methods.

**Answer these questions after completing Stage 5:**
- After the refactor, where does the reorder alert check live — inside `Product.update_stock()` or in `Inventory.process_sale()`? Which location is more appropriate and why?
- `Transaction` objects are created inside `Inventory.process_sale()`. Should `Transaction` know anything about `Product`, or should it only store primitive values? What are the consequences of each design?

### Stage 6: Make It Persistent and Robust

1. Save products and transactions to `products.json` and `transactions.json`. Load both on startup.

2. Handle `FileNotFoundError`, corrupted JSON, and permission errors. On a corrupted file, display the error, back up the corrupted file with a `.bak` extension, and start fresh.

3. Add a custom exception `InventoryError` with subclasses `ProductNotFoundError` and `InsufficientStockError`. Raise these in the appropriate methods and catch them in the menu.

4. Find and fix the following three bugs:

**Bug 1:**
```python
def update_stock(self, change):
    self.quantity += change
    if self.quantity < 0:
        self.quantity -= change  # attempt to undo
        raise InsufficientStockError("Not enough stock")
    # the quantity is modified before the check
    # if an exception is raised, the rollback is correct
    # but consider: what if quantity is modified and
    # something else fails before the check runs?
```

**Bug 2:**
```python
def search(self, query):
    results = []
    for pid, product in self.products.items():
        if query in product.name or query == pid:
            results.append(product)
    return results
    # case-sensitive name search — "notebook" misses "Notebook"
```

**Bug 3:**
```python
def daily_report(self):
    today = "20-07-2025"  # hardcoded date
    sales = [t for t in self.transactions if t.timestamp == today]
    return sales
    # timestamp is stored as a full datetime string
    # exact match never works
```

**Answer these questions after completing Stage 6:**
- Bug 1 is a "modify then validate" pattern. What is the safer alternative — validate first or modify first? Rewrite the method using the safer pattern.
- Bug 3 used a hardcoded date during development and was never replaced. What practice would have caught this before it was submitted?

## The Complete Picture

When all six stages are complete, StockSense:

- Tracks a product catalogue with category, price, and reorder levels
- Processes sales and restocks with timestamped transaction logs
- Alerts on low stock with supplier contact information
- Generates daily sales reports and inventory valuation
- Persists all data across sessions in JSON files
- Uses a clean three-class OOP design
- Handles bad input and file errors without crashing
- Has three realistic bugs identified and fixed
