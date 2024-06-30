from Cart import Cart
from Checkout import Checkout

myCart = Cart("Zaid")

print("\n====== E-Commerce Store System ======\n")
while True:
    print("\n1. Add Item to Cart")
    print("2. Remmove Item from Cart")
    print("3. View all the Items in the Cart")
    print("4. Set Payment Method")
    print("5. View Total Bill")
    print("6. Apply Discount")
    print("7. Checkout My Order")
    print("8. Press Other than 1-7 to Close.")

    choice = int(input("\nEnter your choice: "))
        
    if choice == 1:
        myCart.addItem()

    elif choice == 2:
        myCart.removeItem()

    elif choice == 3:
        myCart.viewItems()

    elif choice == 4:
        shippingAddress = input("Enter Shipping Address: ")
        global checkout
        checkout = Checkout(myCart,shippingAddress)
        checkout.setPaymentMethod()
    
    elif choice == 5:
        checkout.calculateBill()

    elif choice == 6:
        checkout.applyDiscount()

    elif choice == 7:
        checkout.processCheckout()

    else:
        print("Thanks for using")
        break