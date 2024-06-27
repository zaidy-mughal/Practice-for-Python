from Vehicle import Vehicle
from Car import Car
from Bike import Bike
from Truck import Truck


allVehicles = []

print("\n====== Vehicle Rental System ======\n")

while True:
    print("\n1. Add Vehicle to Showroom")
    print("2. Remove Vehicle from Showroom")
    print("3. Rent a Vehicle")
    print("4. Return Vehicle")
    print("5. Show all Vehicles in Showroom")
    
    print("6. Press Other than 1-6 to Close.")

    choice = int(input("\nEnter your choice: "))
    
        
    if choice == 1:

        vehicleChoice = input("Which Vehicle you want to add\nCar \nBike \nTruck \nEnter Vehicle Name: ")
        
        if vehicleChoice == "Car":
            name = input("Ente Car Name: ")
            model = input("Enter Car Model: ")
            year = input("Enter Car Year: ")
            color = input("Enter Car Color: ")
            rentalPrice = input("Enter Car Rental Price: ")
            brakeType = input("Enter Car Brake Type: ")
            enginePower = input("Enter Car Engine Power: ")
            fuelType = input("Enter Car Fuel Type: ")

            toAddVehicle = Car(name,model,year,color,"Available",rentalPrice,brakeType,enginePower,fuelType)
            allVehicles.append(toAddVehicle)
            print("Car Added Successfully!")

        elif vehicleChoice == "Bike":
            name = input("Ente Bike Name: ")
            model = input("Enter Bike Model: ")
            year = input("Enter Bike Year: ")
            color = input("Enter Bike Color: ")
            rentalPrice = input("Enter Bike Rental Price: ")
            brakeType = input("Enter Bike Brake Type: ")
            enginePower = input("Enter Bike Engine Power: ")
            toAddVehicle = Bike(name,model,year,color,"Available",rentalPrice,brakeType,enginePower)

            allVehicles.append(toAddVehicle)
            print("Bike Added Successfully!")

        elif vehicleChoice == "Truck":
            name = input("Ente Truck Name: ")
            model = input("Enter Truck Model: ")
            year = input("Enter Truck Year: ")
            color = input("Enter Truck Color: ")
            rentalPrice = input("Enter Truck Rental Price: ")
            fuelType = input("Enter Truck Fuel Type: ")
            noOfWheels = input("Enter Truck Engine Power: ")

            toAddVehicle = Truck(name,model,year,color,"Available",rentalPrice,fuelType,noOfWheels)
            allVehicles.append(toAddVehicle)
            print("Truck Added Successfully!")

        else:
            print('Invalid Vehicle! Try Again')



    elif choice == 2:
        print("To Remove Vehicle from Showroom")
        vehicleName = input("Enter Vehicle Name: ")
        for vehicle in allVehicles:
            if vehicle.name == vehicleName:
                allVehicles.remove(vehicle)
                print("Vehicle Successfully Removed!")
                break
        else:
            print("Vehicle Not Found!")
        



    elif choice == 3:
        print("To Rent Vehicle")
        vehicleName = input("Enter Vehicle Name: ")
        for vehicle in allVehicles:
            if vehicle.name == vehicleName:
                vehicle.updateRentalStatus("Rented")
                print("Vehicle Successfully Rented!")
                break
        else:
            print("Vehicle Not Found!")





    elif choice == 4:
        print("To Return Vehicle to Showroom")
        vehicleName = input("Enter Vehicle Name: ")
        for vehicle in allVehicles:
            if vehicle.name == vehicleName:
                vehicle.updateRentalStatus("Rented")
                print("Vehicle Successfully Rented!")
                print("With Rent Price: ", vehicle.rentalPrice)
                break
        else:
            print("Vehicle Not Found!")



    elif choice == 5:
        print("===== All Vehicles =====")
        for vehicle in allVehicles:
            print(vehicle)


    else:
        break