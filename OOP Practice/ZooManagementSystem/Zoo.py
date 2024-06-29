from Animal import Animal
from Elephant import Elephant
from Lion import Lion
from Giraffe import Giraffe

class Zoo:
    """This Class used to handle zoo operations and manageing animals"""

    def __init__(self) -> None:
        self.animals = []

    def addAnimal(self):
        animal = input("which animal do you want to add.\nElephant   Giraffe   Lion\nType: ")
        name = input("Enter Animal Name: ")
        age = input("Enter Animal Age: ")
        specie = input("Enter its Specie:   ")
        diet = input("Enter its Diet: ")
        healthStatus = input("Enter its Health Status: ")
        if animal == "Elephant":
            animaltoadd = Elephant(name,age,specie,diet,healthStatus)
        elif animal == "Lion":
            animaltoadd = Lion(name,age,specie,diet,healthStatus)
        elif animal == "Giraffe":
            animaltoadd = Giraffe(name,age,specie,diet,healthStatus)
        else:
            print("\nInvalid Animal\n")
        
        self.animals.append(animaltoadd)
        print("\mAnimal Added Successfully\n")



    def removeAnimal(self):
        name = input("Enter Animal Name to remove: ")
        for animal in self.animals:
            if name == animal.name:
                self.animals.remove(animal)
                break
        else:
            print("Animal not Found!")

        
    def makeSound(self):
        name = input("Enter Animal Name to Make Sound: ")
        for animal in self.animals:
            if name == animal.name:
                self.animals.makeSound()
                break
        else:
            print("Animal not Found!")

        
    def feedAnimal(self):
        name = input("Enter Animal Name to Feed: ")
        for animal in self.animals:
            if name == animal.name:
                self.animals.eat()
                break
        else:
            print("Animal not Found!")

        
    def checkHealth(self):
        name = input("Enter Animal Name to Check Health: ")
        for animal in self.animals:
            if name == animal.name:
                self.animals.checkHealth()
                break
        else:
            print("Animal not Found!")


    def viewAllAnimals(self):
        print("\n====All the Animals in the Zoo right Now=====\n")
        for animal in self.animals:
            print(animal)
