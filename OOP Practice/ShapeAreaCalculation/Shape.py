#this module is used to create Abstact Classes and Abstract Methods
from abc import ABC,abstractmethod

class Shape(ABC):

    def __init__(self,type,color) -> None:
        self.type = type
        self.color = color

    @abstractmethod
    def calculateArea(self) -> float:
        pass

    def __str__(self) -> str:
        return (f"Type:     {self.type}\n"
                f"Color:    {self.color}\n")

