import random
class Flight:

    """This class is used to Maintain Flights in the Flights Reservation System."""

    def __init__(self,airline,destination,classType,price) -> None:
        self.flightNumber = random.randint(111111,999999)
        self.airline = airline
        self.destination = destination
        self.classType = classType
        self.price = price


    def __str__(self) -> str:
        return (f"Flight Number:   {self.flightNumber}\n"
                f"Airline:         {self.airline}\n"
                f"Destination:     {self.destination}\n"
                f"Class Type:      {self.classType}\n"
                f"Price:           {self.price}\n")