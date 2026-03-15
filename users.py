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


