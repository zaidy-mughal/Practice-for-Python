from Vehicle import Vehicle

class Car(Vehicle):

    wheels = 4

    def __init__(self, name, model, year, color, rentalStatus, rentalPrice,brakeType,enginePower,fuelType) -> None:
        super().__init__(name, model, year, color, rentalStatus, rentalPrice)
        self.brakeType = brakeType
        self.enginePower = enginePower
        self.fuelType = fuelType


    def updateRentalStatus(self, newStatus):
        return super().updateRentalStatus(newStatus)


    def __str__(self) -> str:
        return (super().__str__()+f"Brake Type: {self.brakeType}\n"
                f"Engine Power: {self.enginePower}\n"
                f"Wheels: {self.wheels}\n"
                f"Fuel Type: {self.fuelType}")