import random
from Message import Message
from User import User

class ChatRoom:
    """This class is used to manage chats between some users"""

    def __init__(self) -> None:
        self.chatRoomId = random.randint(1111,9999)
        self.messages = []
        self.users = []

    def sendMessage(self):
        userName = input("Enter User Name to send Message: ")

        for user in self.users:
            if user.name == userName:
                senderId = user.id
                content = input("Enter Content: ")
                message = Message(senderId,content)
                self.messages.append(message)
                user.receiveMessage(message)
                break
        else:
            print("User Not Found! Add User to Chat Room\n")


    def addUser(self):
        name = input("Enter the Name of User: ")
        age = input("Enter Age : ")
        user = User(name,age)
        self.users.append(user)
        print("User Added Successfully! Now you can send messages!\n")

