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

class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary
emp = Employee("Rahim",2441139,"rahim@outlook.com","Dhaka",28,"Chef",25000)
print(emp.age)