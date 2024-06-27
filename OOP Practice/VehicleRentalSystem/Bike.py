from Vehicle import Vehicle

class Bike(Vehicle):

    wheels = 2

    def __init__(self, name, model, year, color, rentalStatus, rentalPrice,brakeType,enginePower) -> None:
        super().__init__(name, model, year, color, rentalStatus, rentalPrice)
        self.brakeType = brakeType
        self.enginePower = enginePower


    def updateRentalStatus(self, newStatus):
        return super().updateRentalStatus(newStatus)


    def __str__(self) -> str:
        return (super().__str__()+f"Brake Type: {self.brakeType}\n"
                f"Wheels: {self.wheels}\n"
                f"Engine Power: {self.enginePower}\n")