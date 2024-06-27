class Product:

    def __init__(self,productId,name,price,stock,rating) -> None:
        self.productId = productId
        self.name = name
        self.price = price
        self.stock = stock
        self.rating = rating


    def updateStock(self,newStock):
        self.stock += newStock
        print("Stock Updated Successfully!")


    def changeRating(self,newRating):
        if newRating > 0 and newRating <= 5:
            self.rating = newRating
            print("Rating Successfully Updated!")
        else:
            print("Invalid Rating (Only 1-5)")


    def __str__(self) -> str:
        return (f"Name:     {self.name}\n"
                f"Price:    {self.price}\n"
                f"Stock:    {self.stock}\n"
                f"Rating:   {self.rating}\n")