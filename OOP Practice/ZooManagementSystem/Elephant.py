from Animal import Animal

class Elephant(Animal):

    """This class is used to handle Elephant's Behaviour and is inherited from Animal class"""

    def __init__(self, name, age, species, diet, healthStatus) -> None:
        super().__init__(name, age, species, diet, healthStatus)


    def makeSound(self):
        print("Paaaaarrrrrrummmppp-trumpppp-trumppppp-pa-paa!")

    def eat(self):
        print(f"Ahhaaa! Eating {self.diet} . Yummy yummiiies wanna taste it!")


    def checkHealth(self):
        return super().checkHealth()

    def __str__(self) -> str:
        return super().__str__()