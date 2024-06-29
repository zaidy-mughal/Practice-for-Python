from Person import Person

class Teacher(Person):

    """This class is used to manage Teacher related tasks and it is inherited from Person class"""

    def __init__(self, name, age, id, pay, experience) -> None:
        super().__init__(name, age, id)
        self.pay = pay
        self.experience = experience


    def increasePay(self):
        increasedPay = int(input("Enter the pay to increase(int): "))
        if increasedPay > 0:
            self.pay += increasedPay
            print("Pay has been Increased")
        else:
            print("Invalid Increament")


    def __str__(self) -> str:
        return (super().__str__()+f"Pay:    {self.pay}\n"
                f"Experience:       {self.experience}\n")