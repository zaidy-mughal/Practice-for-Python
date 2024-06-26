from Employee import Employee
from Developer import Developer
from Manager import Manager


print("\n====== Employee Management System ======\n")

employees = []


def searchDeveloper(developerName)->Developer:
    for employee in employees:
            if isinstance(employee,Developer):
                if employee.name == developerName:
                    return employee
    return None

def searchManager(managerName) -> Manager:
    for employee in employees:
            if isinstance(employee,Manager):
                if employee.name == managerName:
                    return employee
    return None




while True:
    print("\n----------DEVELOPER RELATED FUNCTIONS--------\n")
    print("1. Enroll Developer")
    print("2. Remove Developer")
    print("3. Add Language")
    print("4. Remove Language")
    print("5. Update Salary")
    print("\n----------MANAGER RELATED FUNCTIONS--------\n")
    print("6. Enroll Manager")
    print("7. Remove Manager")
    print("8. Add Project")
    print("9. Remove Project")
    print("10. Update Salary")
    print("11. Add Developer to team")
    print("12. Remove Developer From team")
    print("13. Show Manager's Team")
    print("14. Press Other than 1-11 to Close.")

    choice = int(input("\nEnter your choice: "))
    
    if choice == 1:
        name = input("Enter Developer name: ")
        employeeId = input("Enter Developer ID: ")
        age = input("Enter Age: ")
        salary = float(input("Enter salary: "))
        programmingLanguages = ["Java",'Python']

        developer = Developer(name,employeeId,age,salary,programmingLanguages)
        employees.append(developer)
        print('Developer Added Successfully!')


    elif choice == 2:
        developerName = input("Enter developer name to remove: ")
        developer = searchDeveloper(developerName)

        if developer is not None:
            employees.remove(developer)
        else:
            print(developerName,'Not Found!')

                
                
        
    elif choice == 3:
        language = input('Enter Language to add: ')
        developerName = input('Enter Developer name: ')

        developer = searchDeveloper(developerName)

        if developer is not None:
            developer.addLanguage(language)
        else:
            print(developerName,'Not Found!')

        
        
    elif choice == 4:
        developerName = input('Enter Developer name: ')

        developer = searchDeveloper(developerName)

        if developer is not None:
            developer.removeLanguage()
        else:
            print(developerName,'Not Found!')
        
        
    elif choice == 5:
        developerName = input('Enter Developer name to update Salary: ')
        increament = float(input('Enter increament to Salary: '))

        developer = searchDeveloper(developerName)

        if developer is not None:
            developer.updateSalary(increament)
        else:
            print(developerName,'Not Found!')
        


    elif choice == 6:
        name = input("Enter Manager name: ")
        employeeId = input("Enter Manager ID: ")
        age = input("Enter Age: ")
        salary = float(input("Enter salary: "))
        
        manager = Manager(name,employeeId,age,salary)
        employees.append(manager)
        print('Manager Added Successfully')
    

    elif choice == 7:
        managerName = input("Enter Manager name to remove: ")
        manager = searchManager(managerName)

        if manager is not None:
            employees.remove(manager)
        else:
            print(managerName,'Not Found!')


    elif choice == 8:
        projectName = input('Enter Project Name: ')
        managerName = input("Enter Manager name: ")
        manager = searchManager(managerName)

        if manager is not None:
            manager.addProject(projectName)
        else:
            print(managerName,'Not Found!')


    elif choice == 9:
        projectName = input('Enter Project Name: ')
        managerName = input("Enter Manager name: ")
        manager = searchManager(managerName)

        if manager is not None:
            manager.completeProject(projectName)
        else:
            print(managerName,'Not Found!')


    elif choice == 10:
        managerName = input('Enter Developer name to update Salary: ')
        increament = float(input('Enter increament to Salary: '))

        manager = searchManager(managerName)

        if manager is not None:
            manager.updateSalary(increament)
        else:
            print(manager,'Not Found!')


    elif choice == 11:
        developerName = input('Enter Developer name to Add to team: ')
        managerName = input('Enter Manger Name to add a member: ')

        developer = searchDeveloper(developerName)
        manager = searchManager(managerName)

        if developer is not None and manager is not None:
            manager.addDeveloper(developer)
        else:
            print('Some is not added !')

    elif choice == 12:
        developerName = input('Enter Developer name to remove to team: ')
        managerName = input('Enter Manger Name to remove a member: ')

        developer = searchDeveloper(developerName)
        manager = searchManager(managerName)

        if developer is not None and manager is not None:
            manager.removeDeveloper(developer)
        else:
            print('Some is not added !')

    elif choice == 13:
        managerName = input("Enter Manager name: ")
        manager = searchManager(managerName)

        if manager is not None:
            manager.showDevelopersTeam()
        else:
            print(managerName,'Not Found!')

    
    else:
        print('Thanks for using!')
        break

