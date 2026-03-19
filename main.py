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

    print(f"Welcome {customer.name.title()}!")
    while True:        
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
            customer.show_menu(restaurant=star)
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

def admin_menu():
    name = input("Enter Your Name: ").lower()
    email = input("Enter Your E-Mail: ").lower()
    phone = input("Enter Your Phone Number: ")
    address = input("Enter Your Address: ").lower()
    admin = Admin(name = name, phone = phone, email = email, address = address)

    print(f"Welcome Admin {admin.name.title()}!")
    while True:
        print("Select an option:")
        print("""
        1. Add item
        2. Remove item
        3. Add employee1
        4. View employees
        5. View menu
        6. Exit
        """)
        choice = int(input("Choice: "))
        if choice == 1:
            item_name = input("Item Name: ").lower()
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))
            item = FoodItem(name = item_name, price = price, quantity = quantity)
            admin.add_item(star,item)
        elif choice == 2:
            item_name = input("Item Name: ").lower()
            admin.remove_item(item_name)
        elif choice == 3:
            print("Enter employee details:")
            name = input("Name: ").lower()
            email = input("E-Mail: ").lower()
            phone = input("Phone Number: ")
            address = input("Address: ").lower()
            age = int(input("Age: "))
            designation = input("Designation: ")
            salary = int(input("Salary: "))
            employee = Employee(name=name, phone = phone, email = email, address = address, age = age, designation = designation, salary = salary)
            admin.add_employee(star,employee)
        elif choice == 4:
            admin.view_employees(star)
        elif choice == 5:
            admin.view_menu(star)
        elif choice == 6:
            break
        else:
            print("Invalid Choice!")

while True:
    print(f"Welcome to {star.name}")
    print("""Select Option:
    1. Admin
    2. Customer
    3. Exit """)
    choice = int(input("Choice: "))
    if choice == 1:
        admin_menu()
    elif choice == 2:
        customer_menu()
    elif choice == 3:
        break
    else:
        print("Invalid Choice!")
