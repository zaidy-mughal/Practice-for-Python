from Product import Product
from Order import Order
from Customer import Customer
import random


order = None 
productList = []
customer = None
print("\n====== Online Store System ======\n")

while True:
    print("\n1. Register Customer")
    print("2. Place Order")
    print("3. Cancel Order")
    print("4. Add Product to Store")
    print("5. Remove Product from Store")
    print("6. Give Ratings to product")
    print("7. Update Stock of Product")
    print("8. View your Order")
    print("9. Press Other than 1-8 to Close.")

    choice = int(input("\nEnter your choice: "))
        
    if choice == 1:

        name = input("Enter your Name: ")
        phone = int(input("Enter your Phone: "))
        address = input("Enter your Address: ")
        gender = input("Enter your Gender: ")
        customerId = random.randint(1000,1999)
        customer = Customer(customerId,name,phone,address,gender)
        print("Customer Added Now you can place Order")



    elif choice == 2:

        if customer is not None and productList is not None:
            for product in productList:
                print(product)
            while True:
                name = input("\nEnter name of product to order \n(Enter 0 to stop adding products): ")
                if product.name == name:
                    productList.append(product)
                    print("Product added Successfully!")
                elif name == "0":
                    break
                else: 
                    print("Product Not Found!")
            order = Order(random.randint(100,999),customer.customerId,productList)
            customer.placeOrder(order)     
        else:
            print("Register Customer First AND Add Products to view some.")
        
        

    elif choice == 3:

        if customer is not None:
            retry = input("\nAre you sure to Cancel.Type yes")
            if retry == "yes":
                customer.cancelOrder()
            else:
                print("\nOrder Not Canceled!")
        else:
            print("\nRegister Customer First")


    elif choice == 4:

        name = input("Enter Product Name: ")
        price = float(input("Enter Product Price: "))
        stock = int(input("Enter Stock: "))
        rating = float(input("Enter Rating (1-5): "))
        id = random.randint(2000,2999)
        product = Product(id,name,price,stock,rating)
        productList.append(product)
        print("\nProduct Added Successfully!")

    elif choice == 5:

        name = input("Enter Product Name to remove: ")
        for product in productList:
            if product.name == name:
                productList.remove(product)
                print("\nProduct Removed Successfully!")
        print("\nProduct Not Found")

    elif choice == 6:
        name = input("Enter Product Name to Give Rating: ")
        rating = float(input("Enter Rating(1-5): "))

        for product in productList:
            if product.name == name:
                product.changeRating(rating)
        print("\nProduct Not Found")

    elif choice == 7:
        name = input("Enter Product Name to Give Rating: ")
        stock = int(input("Enter Quatity: "))

        for product in productList:
            if product.name == name:
                product.updateStock(stock)
        print("\nProduct Not Found")



    elif choice == 8:
        if customer is not None:
            if customer.order is not None:
                print(customer.order)
            else:
                print("Place Order First")
        else:
            print("Register Customer First!")

            
        
    else: 
        break

