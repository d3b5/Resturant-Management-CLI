"""People who will use the software:
1. Customer
2. Employee
3. Admin 
"""
from abc import ABC

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = order()
    
    def show_menu(self, restaurant):
        restaurant.menu.show_menu()
    
    def add_to_cart(self, restaurant, item_name):
        item = restaurant.find_item(item_name)
        if item:
            pass #later, inside order class
        else:
            print("Item not found!")

    def show_cart(self):
        print(f"<-----{self.name}'s Cart----->")
        print(f"Name\tPrice\tQuantity")
        """ for item,quantity in self.cart.items.item():
            print(f"{item.name}\t{item.price}\t{item.quantity}") """
class Order:
    def __init__(self):
        self.items={}

class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary
    
    def __repr__(self):
        return f"""
        Name: {self.name}
        Phone: {self.phone}
        E-Mail: {self.email}
        Address: {self.address}
        Age: {self.age}
        Designation: {self.designation}
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
        
class Restaurent:
    def __init__(self,name):
        self.name = name
        self.employees = [] #employee database
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{name} is added as an employee!")
        
    def view_employees(self):
        print("Employee List:")
        for i,emp in enumerate(self.employees,1):
            print(f"{i}.{emp}")

class FoodItem:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Menu:
    def __init__(self):
        self.items = {} #menu database
    
    def add_item(self,item):
        self.items[item.name]=item
    
    def find_item(self,item_name):
        return self.items.get(item_name) #returns item or None

    def remove_item(self,item_name): 
        if self.find_item(item_name) is not None: 
            self.items.pop(item_name)
        else:
            print("Invalid Item")

    def show_menu(self):
        print(f"Name\tPrice\tQuantity")
        for i,item in enumerate(self.items.values(),1):            
            print(f"{item.name}\t{item.price}\t{item.quantity}")

mn = Menu()
burger = FoodItem("Burger",15,75)
coke = FoodItem("Coke",3,100)
fries = FoodItem("Fries",4,100)
mn.add_item(burger)
mn.add_item(coke)
mn.add_item(fries)
mn.show_menu()