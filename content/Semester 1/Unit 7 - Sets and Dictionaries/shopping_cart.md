# Mini Project 5: Shopping Cart

## Background

Every time you add something to a cart on Flipkart or Amazon, a program is tracking what you picked, how many, and what it all costs. Building a shopping cart teaches you how dictionaries and sets work together — dictionaries to track items and quantities, sets to handle categories and uniqueness.

## What You Will Build

A CLI shopping cart where the user can add items, remove items, view the cart, and checkout with a final bill.

## Tasks

### Task 1: The Product Catalogue

1. Create a catalogue of at least 8 products as a dictionary. Each product should have a name, price, and category. You can structure it like this:
   ```python
   catalogue = {
       "P001": {"name": "Notebook", "price": 45, "category": "Stationery"},
       "P002": {"name": "Pen", "price": 10, "category": "Stationery"},
       ...
   }
   ```

2. Display the catalogue in a readable format showing the product ID, name, category, and price.

### Task 2: Add and Remove Items

1. Build a menu:
   ```
   1. View Catalogue
   2. Add Item to Cart
   3. Remove Item from Cart
   4. View Cart
   5. Checkout
   6. Exit
   ```

2. Add Item: ask for a product ID and quantity. If the product is already in the cart, increase the quantity. If the product ID does not exist in the catalogue, display an error.

3. Remove Item: ask for a product ID and remove it from the cart completely.

4. View Cart: display all items in the cart with quantity, unit price, and line total.

### Task 3: Checkout

1. Display a final bill with all items, quantities, and prices.
2. Compute and display the subtotal.
3. Apply a 10% discount if the subtotal exceeds ₹500.
4. Display the final amount after discount (if any).

   ```
   ======= YOUR BILL =======
   Notebook  x2   ₹  90.00
   Pen       x3   ₹  30.00
   -------------------------
   Subtotal       ₹ 120.00
   Discount       ₹   0.00
   -------------------------
   Total          ₹ 120.00
   =========================
   ```

5. After checkout, clear the cart.

**Answer these questions after completing all tasks:**
- Your cart stores product IDs and quantities. To display the cart, you look up the product name and price from the catalogue using the product ID. What happens if someone deletes a product from the catalogue while it is still in the cart?
- The discount applies only above ₹500. Test the boundary: add items worth exactly ₹500. Does the discount apply? Should it?
- Use a set to collect all unique categories of items currently in the cart. Display this as "Shopping across: Stationery, Electronics, ..." — how did you build this set from the cart contents?
