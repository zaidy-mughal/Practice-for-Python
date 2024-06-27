
class Order:

    def __init__(self,orderId,customerId,orderProducts) -> None:
        self.orderId = orderId
        self.customerId = customerId
        self.orderProducts = orderProducts
        self.orderStatus = 'Pending'
        self.orderPrice = 0


    def calculatePrice(self):
        for product in self.orderProducts:
            orderPrice += product.price


    def changeStatus(self,newStatus):
        self.orderStatus = newStatus
        print("Status Changed!")

    
    def addProduct(self,product):
        self.orderProducts.append(product)
        self.calculatePrice()
        print("Product Added Successfully!")


    def __str__(self) -> str:
        products = "\n".join(self.orderProducts)

        return (f"Order ID:         {self.orderId}\n"
                f"Customer ID:      {self.customerId}\n"
                f"Ordered Products: {products}\n"
                f"Ordered Status:   {self.orderStatus}\n"
                f"Order Price:      {self.orderPrice}")
    