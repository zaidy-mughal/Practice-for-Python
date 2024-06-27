from Vehicle import Vehicle

class Truck(Vehicle):

    def __init__(self, name, model, year, color, rentalStatus, rentalPrice, fuelType, wheels) -> None:
        super().__init__(name, model, year, color, rentalStatus, rentalPrice)
        self.fuelType = fuelType
        self.wheels = wheels
        
    def updateRentalStatus(self, newStatus):
        return super().updateRentalStatus(newStatus)

    def __str__(self) -> str:
        return (super().__str__()+f"Truck Type: {self.type}\n"
                f"Wheels: {self.wheels}")