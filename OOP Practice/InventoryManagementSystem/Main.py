from Warehouse import Warehouse
from Product import Product
import random

myWarehouse = Warehouse("Logistics","Lahore",50000)

def addRandomProduct()->Product:
    name = random.choice(["Cold Drinks","Chips","Candies","Chocolates"])
    price = round(random.uniform(50.0,1000.0),2)
    quantity = random.randint(1000,5000)
    rating = round(random.uniform(1.0,5.0),1)
    return Product(name,price,quantity,rating)

for i in range(4):
    myWarehouse.inventory.append(addRandomProduct())



print("\n====== Inventory Management System ======\n")
while True:
    print("\n1. Add Products to Inventory")
    print("2. Remove Products from Inventory")
    print("3. Increase Capacity of Warehouse")
    print("4. View All Products of Inventory")
    print("5. Check Remaining Capacity of Warhouse")
    print("6. Warehouse Details")
    print("7. Press Other than 1-6 to Close.")

    choice = int(input("\nEnter your choice: "))
        
    if choice == 1:
        myWarehouse.addProducts()

    elif choice == 2:
        myWarehouse.removeProducts()

    elif choice == 3:
        myWarehouse.increaseCapacity()

    elif choice == 4:
        myWarehouse.viewAllProducts()

    elif choice == 5:
        print(f"Remaining Capacity: {myWarehouse.checkCapacity()}")

    elif choice == 6:
        print(myWarehouse)


    else:
        print("Thanks for using!")
        break