from Book import Book
from Member import Member
from Library import Library
import random


print("\n====== Library Management System ======\n")

comsatsLibrary = Library()

while True:
    print("\n----------MEMBER RELATED FUNCTIONS--------\n")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search Book")
    print("\n----------MEMBER RELATED FUNCTIONS--------\n")
    print("6. Enroll Member")
    print("7. Remove Member")
    print("8. Search Member")
    print("9. Show All Books")
    print("10. Show All Members")
    print("11. Press Other than 1-11 to Close.")

    choice = int(input("\nEnter your choice: "))
    
    if choice == 1:
        bookName = input('Enter Book Name: ')
        bookAuthor = input('Enter Book Author: ')
        bookId = random.randint(100,999)
        book = Book(bookName,bookAuthor,bookId,'Available')
        comsatsLibrary.addBook(book)

    elif choice == 2:
        bookName = input('Enter Book Name to Remove: ')
        comsatsLibrary.removeBook(bookName)

    elif choice == 3:
        print('To Borrow Book')
        bookName = input('Enter Book Name: ')
        memberName = input('Enter Member Name: ')
        comsatsLibrary.borrowBook(bookName,memberName)

    elif choice == 4:
        print('To Return Book')
        bookName = input('Enter Book Name: ')
        memberName = input('Enter Member Name: ')
        comsatsLibrary.returnBook(bookName,memberName)
        
    elif choice == 5:
        print('To Search Book')
        bookName = input('Enter Book Name: ')
        book = comsatsLibrary.searchBook(bookName)
        if book is not None:
            print(bookName, " is Available")
        else:
            print(bookName,' is not Found!')

    elif choice == 6:
        memberName = input('Enter member Name to Enroll: ')
        memberId = random.randint(1000,1999)
        member = Member(memberName,memberId)
        comsatsLibrary.enrollMember(member)
    
    elif choice == 7:
        memberName = input('Enter member Name to Remove: ')
        comsatsLibrary.removeMember(memberName)

    elif choice == 8:
        print('To Search Member')
        memberName = input('Enter Member Name: ')
        member = comsatsLibrary.searchMember(memberName)
        if member is not None:
            print(memberName, " is Available")
        else:
            print(memberName,' is not Found!')


    elif choice == 9:
        comsatsLibrary.showAllBooks()

    elif choice == 10:
        comsatsLibrary.showAllMembers()

    else:
        print('Thanks for using!')
        break

