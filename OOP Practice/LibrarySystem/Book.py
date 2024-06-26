from typing import Any


class Book:
    def __init__(self,bookName,bookAuthor,bookId,bookStatus) -> None:
        self.bookName = bookName
        self.bookAuthor = bookAuthor
        self.bookId = bookId
        self.bookStatus = bookStatus

    def changeStatus(self,status):
        self.bookStatus = status

    def __str__(self) -> str:
        return (f"\nBook Name: {self.bookName}\n"
                f"Book ID: {self.bookId}\n"
                f"Book Status: {self.bookStatus}\n")

    

    