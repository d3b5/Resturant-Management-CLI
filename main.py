from users import Customer, Admin, Employee
from restaurant import Restaurant
from menu import Menu
from food_item import FoodItem
from order import Order

star = Restaurant("Star Hotel")

def customer_menu():
    name = input("Enter Your Name: ").lower()
    email = input("Enter Your E-Mail: ").lower()
    phone = input("Enter Your Phone Number: ")
    address = input("Enter Your Address: ").lower()
    customer = Customer(name = name, phone = phone, email = email, address = address)

    while True:
        print(f"Welcome {customer.name.title()}!")
        print("Select an option:")
        print("""
        1. View menu
        2. Add item to cart
        3. Remove item from cart
        4. View cart
        5. Pay Bill
        6. Exit
        """)
        choice = int(input("Choice: "))
        if choice == 1:
            customer.view_menu()
        elif choice == 2:
            item_name = input("Item Name: ").lower()
            quantity = int(input("Quantity: "))
            customer.add_to_cart(restaurant = star, item_name = item_name, quantity = quantity)
        elif choice == 3:
            item_name = input("Item Name: ").lower()
            quantity = int(input("Quantity: "))
            customer.remove_from_cart(restaurant = star, item_name = item_name, quantity = quantity)
        elif choice == 4:
            customer.show_cart()
        elif choice == 5:
            print(f"Total Bill: {customer.show_bill}")
            cash = int(input("Enter Bill: "))
            customer.pay_bill(cash)
        elif choice == 6:
            print(f"Thank you for visiting {star.name}")
            break
        else:
            print("Invalid Choice!")