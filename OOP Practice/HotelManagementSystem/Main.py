from Hotel import Hotel
from Room import Room
import random


print("\n====== Hotel Management System ======\n")

name = input("Enter Hotel Name:    ")
phone = input("Enter contact Number of Hotel:   ")
address = input("Enter Address of Hotel: ")


#this function is used to generate random data for Room to save time
def generate_random_room():
    roomNumber = f'{random.randint(100, 999)}'  
    pricePerNight = round(random.uniform(50.0, 500.0), 2)  
    roomType = random.choice(['Single', 'Double', 'Suite', 'Deluxe'])
    return Room(roomNumber, pricePerNight, roomType)

#making 10 rooms for hotel
allrooms = []
for i in range(10):
    allrooms.append(generate_random_room())



myHotel = Hotel(name,address,phone,allrooms)
while True:
    print("\n1. View All Rooms")
    print("2. Add Room")
    print("3. Remove Room")
    print("4. Book Room")
    print("5. Check Availability")
    print("6. View Customer Info")
    print("7. Press Other than 1-6 to Close.")

    choice = int(input("\nEnter your choice: "))
        
    if choice == 1:
        myHotel.viewAllRooms()

    elif choice == 2:
        myHotel.addRoom()

    elif choice == 3:
        myHotel.removeRoom()

    elif choice == 4:
        myHotel.bookRoom()

    elif choice == 5:
        myHotel.checkAvailability()

    elif choice == 6:
        myHotel.viewCustomerInfo()

    else:
        print("Thanks For Using\n")
        break