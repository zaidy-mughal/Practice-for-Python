
class Customer:

    def __init__(self,customerId,customerName,phone,address,gender) -> None:
        self.customerId = customerId
        self.customerName = customerName
        self.order = None
        self.phone = phone
        self.address = address
        self.gender = gender


    def placeOrder(self,order):
        self.order = order
        print("Order Placed Successfully!")

    def cancelOrder(self):
        self.order = None
        print("Order Canceled")

    def showAllOrders(self):
        for order in self.orders:
            print(order)


    def __str__(self) -> str:
        return (f"Name:     {self.customerName}\n"
                f"Phone:    {self.phone}\n"
                f"Gender:   {self.gender}\n"
                f"Address:  {self.address}")