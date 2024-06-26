from Book import Book
from Member import Member

class Library:

    """This class is used to handle many Libary operations with the composition of Book and Member Class"""

    def __init__(self) -> None:
        self.booksList = []
        self.membersList = []


#BOOK RELATED FUNCTIONS
    def addBook(self,book):
        self.booksList.append(book)
        print('Book Successfully Added to Library')


    def removeBook(self,bookName):
        bookToRemove = self.searchBook(bookName)

        if bookToRemove is not None:
            self.booksList.remove(bookToRemove)
            print(bookName, " Successfully Removed")
        else:
            print(bookName," Not Found!")


    def borrowBook(self,bookName,memberName):
        book = self.searchBook(bookName)
        member = self.searchMember(memberName)

        if book is not None and member is not None:
            book.changeStatus('Borrowed')
            member.addBook(book)
        else:
            print('Book or Member Not Found!')


    def returnBook(self,bookName,memberName):
        book = self.searchBook(bookName)
        member = self.searchMember(memberName)

        if book is not None and member is not None:
            book.changeStatus('Available')
            member.removeBook(book)
        else:
            print('Book or Member Not Found!')
            

    def searchBook(self,bookName) -> Book:
        for book in self.booksList:
            if book.bookName == bookName:
                return book
        return None
    


#MEMBER RELATED FUNCTIONS
    def searchMember(self,memberName) -> Member:
        for member in self.membersList:
            if member.memberName == memberName:
                return member
        return None


    def enrollMember(self,member):
        self.membersList.append(member)
        print("Member Successfully Enrolled!")        


    def removeMember(self,memberName):
        for member in self.membersList:
            if member.memberName == memberName:
                self.membersList.remove(member)
                print(memberName," Successfully Removed!")
                return
        print(memberName," Member Not Found!")
        


#DEFAULT FUNCTIONS
    def showAllBooks(self):
        for book in self.booksList:
            print(book)

    def showAllMembers(self):
        for member in self.membersList:
            print(member)

