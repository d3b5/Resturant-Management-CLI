from food_item import FoodItem
class Menu:
    def __init__(self):
        self.items = {} #menu database
    
    def add_item(self,item):
        self.items[item.name]=item
        print(f"{item.name.title()} added successfully!")
    
    def find_item(self,item_name):
        return self.items.get(item_name) #returns item or None

    def remove_item(self,item_name): 
        if self.find_item(item_name) is not None: 
            self.items.pop(item_name)
            print(f"{item_name.title()} removed successfully!")
        else:
            print("Invalid Item")

    def show_menu(self):
        
        if not self.items:
            print("Menu is Empty!")
        else:            
            print("<-------MENU------->")
            print(f"    {'Name':<12} {'Price':<8} {'Quantity':<8}")
            
            for i,item in enumerate(self.items.values(),1):            
                print(f"{i}. {item.name.title():<10} {item.price:<8} {item.quantity:<8}")
