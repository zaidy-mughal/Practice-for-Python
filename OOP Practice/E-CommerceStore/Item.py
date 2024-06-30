from datetime import date
import random

class Item:

    def __init__(self,name,price,quantity) -> None:
        self.name = name
        self.id = random.randint(111,999)
        self.price = price
        self.quantity = quantity
        self.expiryDate = date.today()



    def updateQuantity(self):
        newQuantity = int(input("Enter New Quantity(int): "))
        self.quantity = newQuantity
        print("Quantity Upadated Successfully!\n")
    

    
    def __str__(self) -> str:
        return (
            f"Name:     {self.name}\n"
            f"ID:       {self.id}\n"
            f"Price:    {self.price}\n"
            f"Quantity: {self.quantity}\n"
            f"Expiry Date: {self.expiryDate}"
        )