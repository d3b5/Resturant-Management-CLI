from food_item import FoodItem
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
        if not self.items:
            print("Menu is Emply!")
        else:            
            print("<-----MENU----->")
            for i,item in enumerate(self.items.values(),1):            
                print(f"{item.name}\t{item.price}\t{item.quantity}")
