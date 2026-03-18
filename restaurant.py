        
class Restaurant:
    def __init__(self,name):
        self.name = name
        self.employees = [] #employee database
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} is added as an employee!")
        
    def view_employees(self):
        print("Employee List:")
        for i,emp in enumerate(self.employees,1):
            print(f"{i}.{emp}")
