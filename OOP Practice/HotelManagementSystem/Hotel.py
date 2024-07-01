from Room import Room
from Customer import Customer

class Hotel:

    #DocString
    """This class id defined to manage rooms and customers of the Hotel"""

    def __init__(self,name,address,phone,allRooms: list[Room]) -> None:
        self.name = name 
        self.address = address
        self.phone = phone
        self.allRooms = allRooms
        self.customers = []



    def addRoom(self):
        roomNumber = input("Enter room Number: ")
        pricePerNight = input("Enter Room's Price per Night: ")
        roomType = input("Enter room Type: ")

        room = Room(roomNumber,pricePerNight,roomType)
        self.allRooms.append(room)
        print(f"Room is Registered With {self.name} Hotel.")




    def removeRoom(self):
        roomNumber = input("Enter room Number to Remove: ")
        for room in self.allRooms:
            if room.roomNumber == roomNumber:
                self.allRooms.remove(room)
                print("Room is Successfully Removed.")
                break
        else:
            print("Room not Found")




    def bookRoom(self):

        roomNumber = input("Enter room Number to Book: ")
        for room in self.allRooms:
            if room.roomNumber == roomNumber:
                print("To Book Room Enter your details.\n")
                name = input("Enter Your Name: ")
                phone = input("Enter Your Phone:   ")
                bookedRoom = room
                customer = Customer(name,bookedRoom,phone)
                room.bookRoom()
                self.customers.append(customer)
                break
        else:
            print("Room not Found")




    def checkAvailability(self):
        roomNumber = input("Enter room Number to check Availability: ")
        for room in self.allRooms:
            if room.roomNumber == roomNumber:
                print(f"Rooms is {room.status}")
                break
        else:
            print("Room not Found")



    def viewCustomerInfo(self):
        name = input("Enter Name to View Info:  ")
        for customer in self.customers:
            if customer.name == name:
                print(customer)
                break
        else:
            print("Customer Not Found!")


    def viewAllRooms(self):
        for room in self.allRooms:
            print(room)
        