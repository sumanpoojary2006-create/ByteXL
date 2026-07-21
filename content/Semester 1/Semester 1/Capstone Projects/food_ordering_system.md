## Background

Every Indian college campus has a canteen, and most of them take orders manually — leading to long queues, wrong orders, and no record of what was sold. CampusEats is a command-line food ordering system for a college canteen. It lets students browse the menu, add items to a cart, place orders, track order history, and gives the canteen owner a daily sales report.

This project draws on everything from Units 1 through 13: input validation, loops, lists and dictionaries, functions, file handling, basic OOP, and exception handling. You will build it in six stages, from a simple menu display to a full order management system.

## Stages

### Stage 1: Display the Menu

1. Define a menu with at least 10 items across three categories: Meals, Snacks, and Beverages. Store as a list of dictionaries with keys: `item_id`, `name`, `category`, `price`, `available` (True/False).

2. Display the menu in a formatted, category-wise layout:
   ```
   ========== CampusEats Menu ==========

   MEALS
   [M01] Veg Thali          ₹ 60.00
   [M02] Chicken Biryani    ₹ 90.00
   [M03] Paneer Rice        ₹ 75.00

   SNACKS
   [S01] Samosa (2 pcs)     ₹ 15.00
   [S02] Vada Pav           ₹ 20.00
   ...

   BEVERAGES
   [B01] Chai               ₹ 10.00
   [B02] Cold Coffee        ₹ 40.00
   ...
   ======================================
   ```

3. Items marked as unavailable should display "(Unavailable)" instead of a price.

**Answer these questions after completing Stage 1:**
- You display unavailable items with a label instead of hiding them. What is the user experience tradeoff between hiding unavailable items versus showing them with a label?
- Your menu is hardcoded as a list in the source code. What is the first problem a real canteen owner would face with this design, and how would you address it in a later stage?

### Stage 2: Cart Management

1. Build a main menu:
   ```
   ========== CampusEats ==========
   1. View Menu
   2. Add to Cart
   3. View Cart
   4. Remove from Cart
   5. Place Order
   6. Exit
   ================================
   ```

2. Add to Cart: takes an item ID and quantity. Validate that the item exists and is available. If the item is already in the cart, increase the quantity instead of adding a duplicate entry.

3. View Cart: display all cart items with quantity, unit price, and line total. Display the cart subtotal at the bottom.

4. Remove from Cart: takes an item ID, removes it completely from the cart regardless of quantity.

**Answer these questions after completing Stage 2:**
- Adding the same item twice should increase quantity, not add a duplicate line. Test this — if you add "Chai" twice, does your cart show one line with quantity 2 or two lines with quantity 1 each?
- What happens if a student adds an item to the cart and then the canteen marks it as unavailable before the order is placed? Should your cart validation run at add-time, at order-time, or both?

### Stage 3: Order Placement and Billing

1. Place Order: takes the current cart, generates an order with a unique order ID, records the timestamp, and displays a bill:
   ```
   ============================================
   ORDER CONFIRMED — ORD-0042
   ============================================
   Time        : 12:45 PM, 20 July 2025
   --------------------------------------------
   Veg Thali       x2      ₹  120.00
   Samosa (2 pcs)  x3      ₹   45.00
   Chai            x1      ₹   10.00
   --------------------------------------------
   Subtotal                ₹  175.00
   GST (5%)                ₹    8.75
   --------------------------------------------
   TOTAL                   ₹  183.75
   ============================================
   Thank you! Your order will be ready shortly.
   ```

2. After placing, clear the cart.

3. Apply 5% GST on the subtotal. Round the final total to two decimal places.

4. Track an order status: Pending → Preparing → Ready → Delivered.

**Answer these questions after completing Stage 3:**
- GST is computed as 5% of subtotal. In reality, different food items attract different GST rates (packaged food vs restaurant food). How would you modify your data structure to store per-item GST rates?
- After placing an order, the cart is cleared. What if the student placed the order by mistake and wants to undo it? Does your system support this?

### Stage 4: Order Tracking and History

1. Add an **Order Status** option: takes an order ID and displays the current status.

2. Add an **Update Order Status** option (for canteen staff): takes an order ID and a new status. Validate that status transitions are logical — an order cannot go from Delivered back to Pending.

3. Add a **My Orders** option: takes a student name or phone number and shows all their past orders with totals and statuses.

4. Add a **Daily Sales Report** for the canteen owner:
   - Total orders placed today
   - Total revenue
   - Best-selling item (most units sold)
   - Revenue by category (Meals / Snacks / Beverages)

**Answer these questions after completing Stage 4:**
- Status transitions must be logical. You allow Pending → Preparing → Ready → Delivered. What should happen if a staff member tries to set an already-Delivered order back to Ready? Test this and handle it.
- Best-selling item is measured by units sold. Should it be by units or by revenue? Which metric is more useful to a canteen owner, and do they point to the same item?

### Stage 5: Redesign with Classes

1. Create a `MenuItem` class with attributes `item_id`, `name`, `category`, `price`, `available` and methods `display()` and `__str__`.

2. Create an `Order` class with attributes `order_id`, `items` (list of dicts with item and quantity), `timestamp`, `status`, `subtotal`, `gst`, `total` and methods `compute_total()`, `update_status(new_status)`, `display_bill()`.

3. Create a `Cart` class with attributes `items` (dict mapping item_id → quantity) and methods `add(item, qty)`, `remove(item_id)`, `clear()`, `get_total()`, `display()`.

4. Create a `Canteen` class that holds the menu (list of `MenuItem`), a cart (`Cart`), and order history (dict of `Order`). Move all business logic into `Canteen` methods.

**Answer these questions after completing Stage 5:**
- The `Cart` holds item IDs and quantities, but to compute the total it needs prices. Should `Cart` store prices internally, or should it look them up from the menu each time? What are the consequences if a price changes after an item is added to the cart?
- `Order.compute_total()` applies GST. Should the GST rate be hardcoded inside the `Order` class, or passed in as a parameter? Which is easier to change if the rate changes?

### Stage 6: Persistent Menu and Robust Ordering

1. Load the menu from `menu.json` on startup so the canteen owner can update items without changing the source code. Save any menu changes back to the file.

2. Save all orders to `orders.json`. Load on startup and restore the last order ID counter.

3. Handle missing files, corrupted JSON, and the case where an item in a saved order no longer exists in the current menu.

4. Add a custom exception `OrderError` with subclasses `ItemUnavailableError` and `InvalidStatusTransitionError`. Raise these inside `add_to_cart()` and `update_status()` and catch them in the menu.

5. Find and fix the following three bugs:

**Bug 1:**
```text
def add_to_cart(self, item_id, qty):
    if item_id in self.cart.items:
        self.cart.items[item_id] += qty
    else:
        self.cart.items[item_id] = qty
    # does not check if the item is available before adding
```

**Bug 2:**
```text
def compute_total(self):
    self.subtotal = sum(item["price"] * item["qty"]
                        for item in self.items)
    self.gst = self.subtotal * 0.05
    self.total = self.subtotal + self.gst
    return round(self.total)
    # round() with no second argument rounds to the nearest integer
    # ₹183.75 becomes ₹184
```

**Bug 3:**
```text
def update_status(self, new_status):
    valid_transitions = {
        "Pending": "Preparing",
        "Preparing": "Ready",
        "Ready": "Delivered"
    }
    if valid_transitions.get(self.status) == new_status:
        self.status = new_status
    # silently does nothing if the transition is invalid
    # staff have no idea the update was rejected
```

**Answer these questions after completing Stage 6:**
- Bug 2 uses `round()` incorrectly. After fixing it to `round(self.total, 2)`, test with a total of ₹183.755. What does Python return for `round(183.755, 2)` — is it what you expect? Look up Python's banker's rounding if the answer surprises you.
- Bug 3 silently rejects invalid status transitions. Now that you have raised `InvalidStatusTransitionError` in Stage 6, does that fully replace the silent failure, or do you still want a message for staff? Which approach is most useful for the canteen staff using the CLI?

## The Complete Picture

When all six stages are complete, CampusEats:

- Displays a category-wise menu loaded from a JSON file
- Manages a shopping cart with quantity tracking and validation
- Places orders with GST calculation and generates formatted bills
- Tracks order status through a Pending → Preparing → Ready → Delivered lifecycle
- Generates daily sales reports with best-seller and category breakdowns
- Persists menu and order history across sessions
- Uses a clean four-class OOP design
- Has three realistic bugs identified and fixed

## Where to Build This Project

1. Go to [bytexl.app/nimbus](https://bytexl.app/nimbus).
2. Click **Create new workspace**.

![The Nimbus dashboard with the Create new workspace button highlighted](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/nimbus-python/01_create_new_workspace.png)

3. Select the **Python** template, then click **Next**.

![Select the Python template and click Next](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/nimbus-python/02_select_python_template.png)

4. Enter a workspace name and click **Launch Workspace**.

![Enter a workspace name and launch the Python workspace](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/nimbus-python/03_name_and_launch_workspace.png)
