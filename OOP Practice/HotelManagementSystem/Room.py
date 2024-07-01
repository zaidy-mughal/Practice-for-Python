import random

class Room:

    """This class is used to create room in the Hotel Management System"""

    def __init__(self,roomNumber,pricePerNight,roomType) -> None:
        self.roomId = random.randint(111,999)
        self.roomNumber = roomNumber 
        self.pricePerNight = pricePerNight
        self.roomType = roomType
        self.status = 'Available'



    def bookRoom(self):
        self.status = 'Booked'
        print(f"Room {self.roomNumber} is Booked")
    


    def __str__(self) -> str:
        return (f"Room ID:      {self.roomId}\n"
                f"Room Number:  {self.roomNumber}\n"
                f"Price per Night: ${self.pricePerNight:.2f}\n"
                f"Room Type:    {self.roomType}\n"
                f"Status:       {self.status}\n")