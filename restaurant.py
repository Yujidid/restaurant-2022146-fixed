# Simple Restaurant Order System
import random
menu = {"Burger": 5, "Pizza": 8, "Soda": 2, "Fries": 3, "Ice Cream": 4}
order = []

def show_menu():
    print("MENU :")
    for item, price in menu.items():
        print(f"  {item}: ${price}")

def add_item():
    name = input("What do you want to order?\n").strip().title()
    if name in menu:
        order.append(name)
        print(f"{name} Added!")
    else:
        print("Sorry, that's not on the menu.")

def remove_item():
    name = input("What do you want to remove?\n").strip().title()
    if name in order:
        order.remove(name)
        print(f"{name} Removed!")
    else:
        print("That item is not in your order.")

def view_order():
    if not order:
        print("Your order is empty.")
        return
    print("YOUR ORDER :")
    total = 0
    for item in order:
        price = menu[item]
        print(f"  {item}: ${price}")
        total += price 
    print(f"Total: ${total}")

def checkout():
    if not order:
        print("Your order is empty!")
        return
    print("Thank you for your order!")
    print("Order placed! Enjoy your meal!")

print("Welcome to the Restaurant!")
while True:
    print("\n1. View Menu")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. View Order & Total")
    print("5. Checkout & Exit")
    choice = input("Pick an option: ")

    if choice == "1":
        show_menu()
    elif choice == "2":
        add_item()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        view_order()
    elif choice == "5":
        checkout()
    else:
        print("Invalid option, try again.")