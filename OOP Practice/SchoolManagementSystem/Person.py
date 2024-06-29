#this import is used to make the class Abstract and to make abstract method we should also import abstractmethod from abc Package

from abc import ABC

class Person(ABC):

    """This class is designed to store person data and to make subclasses"""
    
    def __init__(self,name,age,id) -> None:
        self.name = name
        self.age = age
        self.id = id

    def __str__(self) -> str:
        return (f"Name:     {self.name}\n"
                f"Age:      {self.age}\n"
                f"Id:       {self.id}\n")