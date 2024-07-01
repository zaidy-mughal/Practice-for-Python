import random

class User:

    """This class is designed to store User data and to make subclasses"""
    
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        self.id = random.randint(1111,9999)
        self.recievedMessages = []

    
    def receiveMessage(self,message):
        self.recievedMessages.append(message)



    def __str__(self) -> str:
        return (f"Name:     {self.name}\n"
                f"Age:      {self.age}\n"
                f"Id:       {self.id}\n")