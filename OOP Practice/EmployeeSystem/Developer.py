from Employee import Employee

class Developer(Employee):

    def __init__(self, name, employeeId, age, salary,programmingLanguages) -> None:
        super().__init__(name, employeeId, age, salary)
        self.programmingLanguages = programmingLanguages

    def __str__(self) -> str:
        return super().__str__() + f"Pragramming Languages: {self.programmingLanguages.__str__()}\n"
    
    def addLanguage(self,language):
        self.programmingLanguages.append(language)
        print(language,' is Added Successfully!')

    def removeLanguage(self):
        self.programmingLanguages.pop()
        print('Last Language Removed Successfully')
    
    def updateSalary(self, increament):
        print(increament,'Salary Increased')
        return super().updateSalary(increament)
    