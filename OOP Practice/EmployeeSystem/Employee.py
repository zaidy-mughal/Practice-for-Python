
class Employee:

    """This is the Base Class for Developer and Manager class"""

    def __init__(self,name,employeeId,age,salary) -> None:
        self.name = name
        self.employeeId = employeeId
        self.age = age
        self.salary = salary

    def updateSalary(self,increament):
        self.salary += increament

    def __str__(self) -> str:
        return (f"\nName: {self.name}\n"
                f"Employee ID: {self.employeeId}\n"
                f"Age: {self.age}\n"
                f"Salary: {self.salary}\n")