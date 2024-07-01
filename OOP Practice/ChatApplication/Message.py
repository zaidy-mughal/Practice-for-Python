import random
class Message:

    """This class is used to store Message Data"""

    def __init__(self,senderId,content) -> None:
        self.messageId = random.randint(10,99)
        self.senderId = senderId
        self.content = content 
        

    def editMessage(self):
        newMessage = input("Enter the edited Message: ")
        self.content = newMessage
        print("Message Edited!")


    def __str__(self) -> str:
        return (f"Message ID:   {self.message_id}\n"
                f"Sender ID:    {self.sender_id}\n"
                f"Content:      {self.content}\n")