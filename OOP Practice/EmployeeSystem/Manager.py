from Employee import Employee
from Developer import Developer

class Manager(Employee):

    """This class is to Create and Alter the Behaviour of a Manager. And this class is inherited from Employee Class."""

    def __init__(self, name, employeeId, age, salary) -> None:
        super().__init__(name, employeeId, age, salary)
        self.projects = []
        self.developersTeam = []


    def __str__(self) -> str:
        return super().__str__()+f"Developers Team: {self.DevelopersTeam.__str__()}\n"
    
    
    def addProject(self,projectName):
        self.projects.append(projectName)
        print(projectName,'Added Successfully!')


    def completeProject(self,projectName):
        for project in self.projects:
            if project == projectName:
                self.projects.remove(projectName)
                print(projectName,'Completed Successfully!')
                return
        print('Project Not Found')
        
        

    def addDeveloper(self,developer):
        self.developersTeam.append(developer)
        print('Developer Added Successfully!')


    def removeDeveloper(self,developerName):
        for developer in self.developersTeam:
            if developer.name == developerName:
                self.developersTeam.remove(developer)
                print(developerName,'Removed Successfully!')
                return
        print(developerName,'Not Found')

    def updateSalary(self, increament):
        print('Salary Updated Successfully')
        return super().updateSalary(increament)

    def showDevelopersTeam(self):
        print('-----Developer Team-----')
        for developer in self.developersTeam:
            print(developer)