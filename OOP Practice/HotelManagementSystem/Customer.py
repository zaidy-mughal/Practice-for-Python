import random

class Customer:

    """This class is used to define Customer of a Hotels"""

    def __init__(self,name,bookedRoom,phone) -> None:
        self.name = name 
        self.id = random.randint(1111,9999)
        self.bookedRoom = bookedRoom
        self.phone = phone



    def __str__(self) -> str:
        return (f"Name: {self.name}\n"
                f"ID:   {self.id}\n"
                f"Phone: {self.phone}\n"
                f"Booked Rooms: {self.bookedRoom}\n")


