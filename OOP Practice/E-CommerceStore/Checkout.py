from Cart import Cart

class Checkout:

    def __init__(self,cart: Cart,shippingAddress) -> None:
        self.cart = cart
        self.discount = 1
        self.shippingAddress = shippingAddress
        self.paymentMethod = ''
        self.currentStatus = "Pending"


    def calculateBill(self):
        total = 0
        for item in self.cart.items:
            total += item.price * item.quantity
        total = total - (total * self.discount/100)
        print(f"\nTotal Bill After applying {self.discount} % discount is : {total}\n")


    def processCheckout(self):
        self.calculateBill()
        paid = input("Type Ok to pay the Bill and Complete the order.")
        if paid == "Ok":
            self.currentStatus = "Completed"
            print("Order Successful!")
        else:
            print("Order Canceled")


    def setPaymentMethod(self):
        newMethod = input("Enter the new Payment method: ")
        self.paymentMethod = newMethod
        print("Payment method is set!")


    def applyDiscount(self):
        discount = input("Enter the discount Code (Zaidy for 60%): ")
        if "Zaidy" == discount:
            self.discount = 60
            print("Discount Applied!")
        else:
            print("Wrong Coupon!")
    