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

burger = FoodItem("Burger",15,75)
coke = FoodItem("Coke",3,100)
fries = FoodItem("Fries",4,100)

customer1 = Customer("Nikki",1234,"fearless@bella.com","Arizona")
star = Restaurant("Star Hotel")
star.menu.add_item(burger)
star.menu.add_item(fries)
star.menu.add_item(coke)
customer1.show_menu(star)
customer1.add_to_cart(star,"Burger",1)
customer1.add_to_cart(star,"Coke",2)
customer1.add_to_cart(star,"Fries",2)
customer1.show_cart()
print("Bill: ",customer1.cart.total_price)
customer1.show_menu(star)
customer1.remove_from_cart(star,"Fries",1)
customer1.show_cart()
