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
        

    def add_employee(self,name, phone, email, address, age, designation, salary):
        employee = Employee(name, phone, email, address, age, designation, salary)
        self.employees.append(employee)
        print(f"{name} is added as an employee!")
    
    def view_employee(self):
        print("Employee List:")
        for i,emp in enumerate(self.employees,1):
            print(f"{i}.{emp}")

class Restaurent:
    def __init__(self,name):
        self.name = name