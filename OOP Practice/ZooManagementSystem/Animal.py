from abc import ABC,abstractmethod

class Animal(ABC):
    
    """This is the Base Class for All the Animals in the Zoo. It means all other animal classes will be inherited from it."""

    def __init__(self,name,age,species,diet,healthStatus) -> None:
        self.name = name
        self.age = age
        self.species = species
        self.diet = diet
        self.healthStatus = healthStatus


    @abstractmethod
    def makeSound(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def checkHealth(self):
        print(f"Don't Worry Cutie I'm fine. Health:  {self.healthStatus}")



    def __str__(self) -> str:
        return (f"Animal Details:\n"
                f"Name:     {self.name}\n"
                f"Age:      {self.age}\n"
                f"Species:  {self.species}\n"
                f"Diet:     {self.diet}\n"
                f"Health Status: {self.healthStatus}\n")