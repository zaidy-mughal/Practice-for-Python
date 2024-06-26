class Member:

    """This class is created to Alter Member Behaviour and it is composed in Library Class"""

    def __init__(self,memberName,memberId) -> None:
        self.memberName = memberName
        self.memberId = memberId
        self.containedBooks = []

    def addBook(self,book):
        self.containedBooks.append(book)

    def removeBook(self,book):
        self.containedBooks.remove(book)
        
    def __str__(self) -> str:
        return (f"\nName: {self.memberName}\n"
                f"ID: {self.memberId}\n"
                f"ContainedBooks: {self.containedBooks.__str__}\n")

    