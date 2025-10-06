# Module8-PortfolioProject
# Online Shopping Cart – Portfolio Project

This project implements a console-based shopping cart using Python **classes**, **lists/dictionaries**, **loops**, **branching**, **user-defined functions**, **exceptions**, and **string manipulation**—aligning with Modules 1–8.

## Features
- `ItemToPurchase` class with name, price, quantity, and description.
- `ShoppingCart` class supporting:
  - `add_item`, `remove_item`, `modify_item`
  - `get_num_items_in_cart`, `get_cost_of_cart`
  - `print_total`, `print_descriptions`
- Interactive **menu**:
  - `a` Add item
  - `r` Remove item
  - `c` Change item quantity
  - `i` Output items' descriptions
  - `o` Output shopping cart
  - `q` Quit
- **Input validation** and **custom exceptions** (e.g., `ItemNotFoundError`).
- Output formatting matches the examples in the prompt.

## How to Run
1. Ensure you have Python 3.9+ installed.
2. Run the script:
   ```bash
   python shopping_cart.py
   ```
3. When prompted, enter the **customer name** and **today's date**. Then use the menu.

## Example (abbreviated)
```text
Enter customer's name:
John Doe
Enter today's date:
February 1, 2020
Customer name: John Doe
Today's date: February 1, 2020

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: a

ADD ITEM TO CART
Enter the item name:
Nike Romaleos
Enter the item description:
Volt color, Weightlifting shoes
Enter the item price:
189
Enter the item quantity:
2
```
