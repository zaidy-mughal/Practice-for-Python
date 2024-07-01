from Flight import Flight
from Passenger import Passenger
from Reservation import Reservation

myReservation = None
print("\n====== Flight Reservation System ======\n")
while True:
    print("\n1. Add Passenger")
    print("2. Book Flight")
    print("3. Add Flight")
    print("4. Remove Flight")
    print("5. View Flights")
    print("6. View Passenger Details")
    print("7. Press Other than 1-6 to Close.")

    choice = int(input("\nEnter your choice: "))
        
    if choice == 1:
        name = input("Enter Passenger Name: ")
        phone = input("Enter Passenger Phone: ")
        passportNumber = input("Enter Passenger Passport Number: ")
        gender = input("Enter Passenger Gender: ")
        passenger = Passenger(name,phone,passportNumber,gender)
        myReservation = Reservation(passenger)
        myReservation.addRandomFlights()
        print("Passenger Added Successfully!\n")


    elif choice == 2:
        if myReservation is not None:
            flightNumber = int(input("Enter Flight Number to Book: "))
            myReservation.bookFlight(flightNumber)
        else:
            print("Add Passenger First\n")


    elif choice == 3:
        if myReservation is not None:
            myReservation.addFlight()
        else:
            print("Add Passenger First\n")

    elif choice == 4:
        if myReservation is not None:
            flightNumber = int(input("Enter Flight Number to Remove: "))
            myReservation.removeFlight()
        else:
            print("Add Passenger First\n")

    elif choice == 5:
        if myReservation is not None:
            myReservation.viewFlights()
        else:
            print("Add Passenger First\n")

    elif choice == 6:
        if myReservation is not None:
            print(myReservation.passenger)
        else:
            print("Add Passenger First\n")


    else:
        print("Thanks for using!")
        break