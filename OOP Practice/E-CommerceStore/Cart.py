from Item import Item

class Cart:

    def __init__(self,owner) -> None:
        self.owner = owner
        self.items = []



    def addItem(self):
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        
        new_item = Item(name, price, quantity)
        self.items.append(new_item)
        print(f"{quantity} {name}(s) added to the cart.")




    def removeItem(self):
        name = input("Enter item name to remove: ")
        for item in self.items:
            if name == item.name:
                self.items.remove(item)
                print("Item removed Successfully!")
                break
        else:
            print("Item not Found!")

    
    
    def viewItems(self):
        for item in self.items:
            print(item)

    

    

    
    