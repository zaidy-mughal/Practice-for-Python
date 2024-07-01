from Flight import Flight
from Passenger import Passenger
import random

class Reservation:
    """This class is designed to manage Flight and Passengers"""

    def __init__(self,passenger) -> None:
        self.reservationId = random.randint(11111,99999)
        self.passenger = passenger
        self.flights = []


    def bookFlight(self,flightNumber):
        for flight in self.flights:
            if flight.flightNumber == flightNumber:
                self.passenger.bookFlight(flight)
                break
        else:
            print("Flight Not Found!")


    def addFlight(self):
        airline = input("Enter Airline: ")
        classType = input("Enter ClassType: ")
        destination = input("Enter Destinatioin: ")
        price = input("Enter Price: ")

        flight = Flight(airline,destination,classType,price)
        self.flights.append(flight)
        print("Flight Added Successfully!\n")


    def removeFlight(self,flightNumber):
        for flight in self.flights:
            if flight.flightNumber == flightNumber:
                self.flights.remove(flight)
                print("Flight Removed Successfully!\n")
                break
        else:
            print("Flight Not Found!")

    
    def viewFlights(self):
        for flight in self.flights:
            print(flight)



    def addRandomFlights(self):
        airline = random.choice(["AirBlue","Emirates","PIA","Etihad"])
        classType = random.choice(["Bussiness","Economy"])
        destination = random.choice(["London","Dubai","New York","Mumbai","Barbados"])
        price = round(random.uniform(100000,999999),2)

        for i in range(10):
            self.flights.append(Flight(airline,destination,classType,price))

        
