from food_item import FoodItem
class Order:
    def __init__(self):
        self.items={}
    
    def empty(self):
        return not self.items

    def add_item(self,item):
        if item.name in self.items:
            self.items[item.name].quantity += item.quantity
        else:
            self.items[item.name] = item

    def find_item(self,item_name):
        return self.items.get(item_name) #returns item or None            
    @property
    def total_price(self):
        return sum(item.price * item.quantity for item in self.items.values())

    def clear_cart(self):
        self.items = {}
    
    def remove_item(self, item_name):
        self.items.pop(item_name)