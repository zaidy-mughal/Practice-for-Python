from ChatRoom import ChatRoom


myChatRoom = ChatRoom()
print("\n====== Chat Application System ======\n")
while True:
    print("\n1. Add User")
    print("2. Send Message to ChatRoom")
    print("3. View All Users")
    print("4. View All Messages of ChatRoom")
    print("5. Press Other than 1-4 to Close.")

    choice = int(input("\nEnter your choice: "))
        
    if choice == 1:
        myChatRoom.addUser()

    elif choice == 2:
        myChatRoom.sendMessage()

    elif choice == 3:
        myChatRoom.veiwUsers()

    elif choice == 4:
        myChatRoom.veiwAllmessages()

    else:
        print("Chat room Ended")
        break