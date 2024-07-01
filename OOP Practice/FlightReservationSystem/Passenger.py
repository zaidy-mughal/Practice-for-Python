import random
from Flight import Flight

class Passenger:
    """This class is used to store Passenger Data and manage his/her Flight Reservation"""

    def __init__(self,name,phone,passportNumber,gender) -> None:
        self.passengerId = random.randint(100,999)
        self.name = name 
        self.phone = phone
        self.passportNumber = passportNumber
        self.gender = gender
        self.bookedFlight = None

    

    def bookFlight(self,flight:Flight):
        if flight is not None:
            self.bookedFlight = flight
            print("Flight is Booked\n")
        else:
            print("Not a Valid Flight!")



    def __str__(self) -> str:
        return (f"Passenger Name: {self.name}\n"
                f"Passenger ID: {self.passengerId}\n"
                f"Passenger Phone: {self.phone}\n"
                f"Passenger Gender: {self.gender}\n"
                f"Passport Number: {self.passportNumber}\n"
                f"Booked Flight No: {self.bookedFlight.flightNumber}\n")

