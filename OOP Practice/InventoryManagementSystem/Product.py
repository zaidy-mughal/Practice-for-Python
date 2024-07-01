import random
class Product:

    def __init__(self,name,price,quantity:int,rating) -> None:
        self.productId = random.randint(11,99)
        self.name = name
        self.price = price
        self.quantity = quantity
        self.rating = rating


    def increaseStock(self,newStock):
        self.quantity += newStock
        print("Stock Updated Successfully!")

    def removeStock(self,decreament):
        if decreament <= self.quantity:
            self.quantity -= decreament
        else:
            print("Product is not much!\n")

    

    def __str__(self) -> str:
        return (f"Name:     {self.name}\n"
                f"Price:    {self.price}\n"
                f"Stock:    {self.quantity}\n"
                f"Rating:   {self.rating}\n")