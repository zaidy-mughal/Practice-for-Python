from Person import Person


class Student(Person):

    """This class is used to handle Students operations and it is inherited from Person class"""

    def __init__(self, name, age, id,grade,feePerMonth) -> None:
        super().__init__(name, age, id)
        self.grade = grade
        self.feePerMonth = feePerMonth 
           
    def __str__(self) -> str:
        return (super().__str__()+f"Grade:       {self.grade}\n"
                f"Fee Per Month:        {self.feePerMonth}\n")