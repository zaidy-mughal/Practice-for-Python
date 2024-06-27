class Vehicle:

    def __init__(self,name,model,year,color,rentalStatus,rentalPrice) -> None:
        self.name = name
        self.model = model
        self.year = year
        self.color = color
        self.rentalStatus = rentalStatus
        self.rentalPrice = rentalPrice
        

    def updateRentalStatus(self,newStatus):
        self.rentalStatus = newStatus
        print('Status Updated Successfully!')

    def __str__(self) -> str:
        return (f"\nName: {self.name}\n"
                f"Model: {self.model}\n"
                f"Year: {self.year}\n"
                f"Color: {self.color}\n"
                f"Status: {self.rentalStatus}\n"
                f"Rent per day: {self.rentalPrice}\n")
