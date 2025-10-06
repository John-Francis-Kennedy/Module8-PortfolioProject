"""
Online Shopping Cart – Portfolio Project
Modules used: variables/expressions, data types/lists/dicts, loops, branching,
user-defined functions, exceptions, classes, string manipulation.
"""

from dataclasses import dataclass, field
from typing import List, Optional


class ItemNotFoundError(Exception):
    """Raised when an operation references an item that is not in the cart."""


def safe_int(prompt: str) -> int:
    """Prompt repeatedly until a valid non-negative integer is entered."""
    while True:
        try:
            raw = input(prompt).strip()
            value = int(raw)
            if value < 0:
                raise ValueError("Value must be non-negative.")
            return value
        except ValueError:
            print("Invalid input. Please enter a non-negative whole number.")


def safe_float(prompt: str) -> float:
    """Prompt repeatedly until a valid non-negative price is entered."""
    while True:
        try:
            raw = input(prompt).strip()
            # Allow things like "3", "3.0", "3.99"
            value = float(raw)
            if value < 0:
                raise ValueError("Value must be non-negative.")
            return value
        except ValueError:
            print("Invalid input. Please enter a non-negative number (e.g., 3 or 3.99).")

# Step 1: Build the ItemToPurchase class

@dataclass
class ItemToPurchase:
    item_name: str = "none"
    item_price: float = 0.0
    item_quantity: int = 0
    item_description: str = "none"

    def print_item_cost(self) -> None:
        """Print cost line like: Bottled Water 10 @ $1 = $10"""
        price_str = f"${int(self.item_price)}" if self.item_price.is_integer() else f"${self.item_price:.2f}"
        line_total = self.item_price * self.item_quantity
        total_str = f"${int(line_total)}" if line_total.is_integer() else f"${line_total:.2f}"
        print(f"{self.item_name} {self.item_quantity} @ {price_str} = {total_str}")

# Step 4: Build the ShoppingCart class

@dataclass
class ShoppingCart:
    customer_name: str = "none"
    current_date: str = "January 1, 2020"
    cart_items: List[ItemToPurchase] = field(default_factory=list)

    def add_item(self, item: ItemToPurchase) -> None:
        self.cart_items.append(item)

    def remove_item(self, name: str) -> None:
        for i, it in enumerate(self.cart_items):
            if it.item_name.lower() == name.lower():
                del self.cart_items[i]
                return
        # If not found, follow spec: print a message (and also raise a custom error for logic flow if needed)
        print("Item not found in cart. Nothing removed.")
        raise ItemNotFoundError(name)

    def modify_item(self, updated: ItemToPurchase) -> None:
        for it in self.cart_items:
            if it.item_name.lower() == updated.item_name.lower():
                # Only update fields that are not default
                if updated.item_description != "none":
                    it.item_description = updated.item_description
                if updated.item_price != 0.0:
                    it.item_price = updated.item_price
                if updated.item_quantity != 0:
                    it.item_quantity = updated.item_quantity
                return
        print("Item not found in cart. Nothing modified.")
        raise ItemNotFoundError(updated.item_name)

    def get_num_items_in_cart(self) -> int:
        return sum(it.item_quantity for it in self.cart_items)

    def get_cost_of_cart(self) -> float:
        return sum(it.item_price * it.item_quantity for it in self.cart_items)

    def print_total(self) -> None:
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        num_items = self.get_num_items_in_cart()
        print(f"Number of Items: {num_items}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            print("Total: $0")
            return
        for it in self.cart_items:
            it.print_item_cost()
        total = self.get_cost_of_cart()
        total_str = f"${int(total)}" if float(total).is_integer() else f"${total:.2f}"
        print(f"Total: {total_str}")

    def print_descriptions(self) -> None:
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for it in self.cart_items:
            print(f"{it.item_name}: {it.item_description}")

# Step 5-6 and 8-10: Menu loop

def print_menu(cart: ShoppingCart) -> None:
    """
    Display and run the interactive menu until the user quits.
    Options:
        a - Add item to cart
        r - Remove item from cart
        c - Change item quantity
        i - Output items' descriptions
        o - Output shopping cart
        q - Quit
    """
    
    menu = (
        "MENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit"
    )

    choice = ""
    while choice != "q":
        print()
        print(menu)
        choice = input("Choose an option: ").strip().lower()

        if choice == "q":
            break
        elif choice == "a":
            print("\nADD ITEM TO CART")
            name = input("Enter the item name: ").strip()
            desc = input("Enter the item description: ").strip() or "none"
            price = safe_float("Enter the item price: ")
            qty = safe_int("Enter the item quantity: ")
            cart.add_item(ItemToPurchase(name, price, qty, desc))
        elif choice == "r":
            print("\nREMOVE ITEM FROM CART")
            name = input("Enter name of item to remove: ").strip()
            try:
                cart.remove_item(name)
            except ItemNotFoundError:
                pass  # Spec already prints a message
        elif choice == "c":
            print("\nCHANGE ITEM QUANTITY")
            name = input("Enter the item name: ").strip()
            new_qty = safe_int("Enter the new quantity: ")
            try:
                # Create a temp object with name + quantity only (others default)
                temp = ItemToPurchase(item_name=name, item_quantity=new_qty)
                cart.modify_item(temp)
            except ItemNotFoundError:
                pass
        elif choice == "i":
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif choice == "o":
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()
        else:
            print("Invalid option. Please choose a valid menu option.")


def milestone1_demo():
    """
    Milestone 1 steps: prompt two items, then print total.
    Used here to generate example output for the portfolio doc.
    """

    print("\n\n*** Milestone 1 Demo ***\n")
    cart = []  # list to hold all items

    # Step 2 - Ask how many items user wants
    num_items = int(input("How many items would you like to add to your cart? "))

    for i in range(1, num_items + 1):
        print(f"\nItem {i}")
        name = input("Enter the item name:\n")
        price = float(input("Enter the item price:\n"))
        quantity = int(input("Enter the item quantity:\n"))
        
        # Create object and add to cart
        item = ItemToPurchase(name, price, quantity)
        cart.append(item)


    # Step 3 - Add the costs of the items together and output the total cost
    print("\nTOTAL COST")
    grand_total = 0
    for item in cart:
        item.print_item_cost()
        grand_total += item.item_price * item.item_quantity
    if grand_total.is_integer():
        print(f"\nTotal: ${int(grand_total)}")
    else:
        print(f"\nTotal: ${grand_total:.2f}")

def main():

    # Run milestone1_demo() to generate the output for Milestone 1
    milestone1_demo()

    print("\n\n*** Milestone 2 Demo ***\n\n")

    # Step 7: prompt for customer's name and today's date, then create ShoppingCart
    print("Enter customer's name:")
    customer_name = input().strip()
    print("Enter today's date:")
    current_date = input().strip()
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")

    cart = ShoppingCart(customer_name=customer_name, current_date=current_date)

    # Run print_menu() to generate the output for Milestone 2 
    print_menu(cart)


if __name__ == "__main__":
    main()