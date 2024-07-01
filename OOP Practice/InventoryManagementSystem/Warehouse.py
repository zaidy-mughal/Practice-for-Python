from Product import Product
import random

class Warehouse:
    def __init__(self, name, location, capacity:int):
        self.warehouse_id = random.randint(1111,9999)
        self.name = name
        self.location = location
        self.capacity = capacity
        self.inventory = []



    def increaseCapacity(self):
        capacity = input("Enter Warhouse Capacity to Increase: ")
        self.capacity += capacity
        print("Capacity is increased!")



    def addProducts(self):
        name = input("Enter Product Name: ")
        price = float(input("Enter Product Price: "))
        quantity = int(input("Enter Stock: "))
        rating = float(input("Enter Rating (1-5): "))
        product = Product(name,price,quantity,rating)
        if self.checkCapacity > quantity:
            self.inventory.append(product)
            print("Product Added Successfully!")
        else:
            print("WareHouse Capacity Reached")



    def removeProducts(self):
        name = input("Enter name of Product to remove: ")
        quantity = int(input("Enter Quantity to Remove: "))
        for product in self.inventory:
            if product.name == name:
                product.removeStock(quantity)
                print("Product removed")
                break
        else:
            print("Product Not Found!")


    def viewAllProducts(self):
        for product in self.inventory:
            print(product)

    

    def checkCapacity(self):
        totalProducts = 0
        for product in self.inventory:
            totalProducts += product.quantity
        return self.capacity-totalProducts
    

    def __str__(self) -> str:
        return (f"Name:     {self.name}\n"
                f"ID:       {self.warehouse_id}\n"
                f"Location:  {self.location}\n"
                f"Capacity:  {self.capacity}\n")