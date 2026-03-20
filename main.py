from users import Customer, Admin, Employee
from restaurant import Restaurant
from menu import Menu
from food_item import FoodItem
from order import Order
from helper import get_input, name_validator, int_validator, float_validator

star = Restaurant("Star Hotel")

def customer_menu():
    name = get_input(prompt="Enter your name: ", validator = name_validator, error_message="Valid Name is required.").lower()

    email = get_input(prompt="Enter your e-mail: ", validator = lambda x: '@' in x and '.' in x.split('@')[-1], error_message="Valid Email is required.").lower()

    phone = get_input(prompt="Enter your phone number: ", validator = lambda x: x.strip() != '', error_message="Valid Phone number is required.")

    address = get_input(prompt="Enter your address: ", validator = lambda x: x.strip() != '', error_message="Valid Address is required.").lower()

    customer = Customer(name = name, phone = phone, email = email, address = address)

    print(f"Welcome {customer.name.title()}!")
    while True:        
        print("\nSelect an option:")
        print("""
        1. View menu
        2. Add item to cart
        3. Remove item from cart
        4. View cart
        5. Show Bill
        6. Pay Bill
        7. Exit
        """)
        choice = get_input(prompt="Choice: ",cast_func=int, validator=int_validator,error_message="Invalid Choice!")
        if choice == 1:
            customer.show_menu(restaurant=star)
        elif choice == 2:
            item_name = input("Item Name: ").lower()
            quantity = get_input(prompt="Quantity: ",cast_func=int, validator=int_validator,error_message="Enter valid quantity.")
            customer.add_to_cart(restaurant = star, item_name = item_name, quantity = quantity)
        elif choice == 3:
            if customer.cart_empty:
                print("Sorry, your cart is empty!")
            else:
                item_name = input("Item Name: ").lower()
                quantity = get_input(prompt="Quantity: ",cast_func=int, validator=int_validator,error_message="Enter valid quantity.")
                customer.remove_from_cart(restaurant = star, item_name = item_name, quantity = quantity)
        elif choice == 4:
            customer.show_cart()
        elif choice == 5:
            print(f"Total Bill: {customer.show_bill} USD")
            choice = input("Would you like to pay now? (y/n): ").lower()
            if choice == 'y':
                cash = get_input(prompt="Enter Bill: ",cast_func=int, validator=int_validator,error_message="Enter valid amount.")
                customer.pay_bill(cash)
        elif choice == 6:
            print(f"Total Bill: {customer.show_bill}")
            cash = get_input(prompt="Enter Bill: ",cast_func=int, validator=int_validator,error_message="Enter valid amount.")
            customer.pay_bill(cash)
        elif choice == 7:
            print(f"Thank you for visiting {star.name}\n")
            break
        else:
            print("Invalid Choice!")

def admin_menu():
    name = get_input(prompt="Enter your name: ", validator = name_validator, error_message="Valid Name is required.").lower()

    email = get_input(prompt="Enter your e-mail: ", validator = lambda x: '@' in x and '.' in x.split('@')[-1], error_message="Valid Email is required.").lower()

    phone = get_input(prompt="Enter your phone number: ", validator = lambda x: x.strip() != '', error_message="Valid Phone number is required.")

    address = get_input(prompt="Enter your address: ", validator = lambda x: x.strip() != '', error_message="Valid Address is required.").lower()

    admin = Admin(name = name, phone = phone, email = email, address = address)

    print(f"Welcome Admin {admin.name.title()}!")
    while True:
        print("\nSelect an option:")
        print("""
        1. Add item
        2. Remove item
        3. Add employee
        4. View employees
        5. View menu
        6. Exit
        """)
        choice = get_input(prompt="Choice: ",cast_func=int, validator=int_validator,error_message="Invalid Choice!")
        if choice == 1:
            item_name = input("Item Name: ").lower()
            quantity = get_input(prompt="Quantity: ",cast_func=int, validator=int_validator,error_message="Enter valid quantity.")
            price = get_input(prompt="Price: ",cast_func=float, validator=float_validator,error_message="Enter valid price.")
            item = FoodItem(name = item_name, price = price, quantity = quantity)
            admin.add_item(star,item)
        elif choice == 2:
            item_name = input("Item Name: ").lower()
            admin.remove_item(star,item_name)
        elif choice == 3:
            print("Enter employee details:")

            name = get_input(prompt="Enter name: ", validator = name_validator, error_message="Valid Name is required.").lower()

            email = get_input(prompt="Enter e-mail: ", validator = lambda x: '@' in x and '.' in x.split('@')[-1], error_message="Valid Email is required.").lower()

            phone = get_input(prompt="Enter phone number: ", validator = lambda x: x.strip() != '', error_message="Valid Phone number is required.")

            address = get_input(prompt="Enter address: ", validator = lambda x: x.strip() != '', error_message="Valid Address is required.").lower()

            age = get_input(prompt="Enter age: ",cast_func=int, validator=int_validator, error_message="Enter valid age.")
            designation = get_input(prompt="Enter designation: ",cast_func=str, validator= lambda x: x.strip() != '', error_message="Enter valid designation")
            salary = get_input(prompt="Enter salary: ",cast_func=int, validator=int_validator, error_message="Enter valid salary.")
            employee = Employee(name=name, phone = phone, email = email, address = address, age = age, designation = designation, salary = salary)
            admin.add_employee(star,employee)
        elif choice == 4:
            admin.view_employees(star)
        elif choice == 5:
            admin.view_menu(star)
        elif choice == 6:
            print(f"Bye, Admin {admin.name}!\n")
            break
        else:
            print("Invalid Choice!")

while True:
    print(f"Welcome to {star.name}")
    print("""Select Option:
    1. Admin
    2. Customer
    3. Exit """)
    choice = get_input(prompt="Choice: ",cast_func=int, validator=int_validator,error_message="Invalid Choice!")
    if choice == 1:
        admin_menu()
    elif choice == 2:
        customer_menu()
    elif choice == 3:
        print("Bye!")
        break
    else:
        print("Invalid Choice!")
