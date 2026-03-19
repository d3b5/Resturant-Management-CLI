"""People who will use the software:
1. Customer
2. Employee
3. Admin 
"""
from abc import ABC
from restaurant import Restaurant
from menu import Menu
from order import Order
from food_item import FoodItem
class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()
    
    def show_menu(self, restaurant):
        restaurant.menu.show_menu()
    
    def add_to_cart(self, restaurant, item_name,quantity):
        item = restaurant.menu.find_item(item_name)
        if item:         

            if quantity<0:
                print("Invalid Quantity!")
            elif quantity>item.quantity:
                print(f"Insufficient stock. We have {item.quantity} {item.name}")
            else:
                self.cart.add_item(FoodItem(item.name, item.price, quantity))
                item.quantity -= quantity #updating resturant inventory
                print(f"{quantity} {item.name} is added to the cart.")
        else:
            print("Item not found!")
    
    def remove_from_cart(self, restaurant, item_name, quantity):
        cart_item = self.cart.find_item(item_name)
        inventory_item = restaurant.menu.find_item(item_name)
        if not cart_item and not inventory_item:
            print("Invalid Item")
        elif not cart_item:
            print(f"You dont have {item_name} in your cart!")
        elif quantity<0:
            print("Invalid quantity")
        elif cart_item.quantity < quantity:
            print(f"Insufficient quantity. You only have {cart.item.quantity} {item_name} in your cart")
        else:
            cart_item.quantity -= quantity
            inventory_item.quantity += quantity

            if cart_item.quantity==0:
                self.cart.remove_item(item_name)
                print(f"All {item_name} has been removed!")
            else:
                print(f"{quantity} {item_name} has been removed from cart. Remaining {item_name}: {cart_item.quantity}")
    @property
    def show_bill(self):
        return self.cart.total_price
    def pay_bill(self,cash):
        if cash<0:
            print("Invalid amount!")
        if cash < self.show_bill:
            print(f"Insufficient amount!")
        else:
            print(f"{self.show_bill} USD Paid!")
            self.cart.clear_cart()
                        
            if cash > self.show_bill:
                print(f"Change return: {cash - self.show_bill}")
            


    def show_cart(self):
        print(f"<-----{self.name}'s Cart----->")
        print(f"Name\tPrice\tQuantity")
        for item in self.cart.items.values():
            print(f"{item.name}\t{item.price}\t{item.quantity}")

class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary
    
    def __repr__(self):
        return f"""
        Name: {self.name.title()}
        Phone: {self.phone}
        E-Mail: {self.email}
        Address: {self.address.title()}
        Age: {self.age}
        Designation: {self.designation.title()}
        Salary: {self.salary}"""

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
    
    def add_employee(self,restaurant,employee):
        restaurant.add_employee(employee)

    def view_employees(self,restaurant):
        restaurant.view_employees()
    
    def add_item(self,restaurant,item):
        restaurant.menu.add_item(item)
    
    def remove_item(self,restaurant,item_name):
        restaurant.menu.remove_item(item_name)
    
    def view_menu(self,restaurant):
        restaurant.menu.show_menu()
