import users
from menu import Menu  
class Restaurant:
    def __init__(self,name):
        self.name = name
        self.employees = [] #employee database
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name.title()} is added as an employee!")
        
    def view_employees(self):
        if not self.employees:
            print("There are no employees!")
        else:
            print("Employee List:")
            for i,emp in enumerate(self.employees,1):
                print(f"{i}.{emp}")
