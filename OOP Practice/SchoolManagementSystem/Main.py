from School import School
import random



alliedSchool = School()
print("\n====== School Management System ======\n")

while True:
    print("1. Add Teacher")
    print("2. Add Student")
    print("3. Remove Teacher")
    print("4. Remove Student")
    print("5. Search Student")
    print("6. Search Teacher")
    print("7. Check Total Number of Students of School")
    print("8. Check Total Number of Teachers of School")
    print("9. Update Student Grade")
    print("10. Increase Pay of Students")
    print("11. Press Other than 1-11 to Close.")

    choice = int(input("\nEnter your choice: "))
    
    if choice == 1:
        alliedSchool.addTeacher()
    
    elif choice == 2:
        alliedSchool.addStudent()

    elif choice == 3:
        alliedSchool.removeTeacher()

    elif choice == 4:
        alliedSchool.removeStudent()

    elif choice == 5:
        alliedSchool.searchStudent()

    elif choice == 6:
        alliedSchool.searchTeacher()

    elif choice == 7:
        alliedSchool.totalStudents()

    elif choice == 8:
        alliedSchool.totalTeachers()

    elif choice == 9:
        name = input("Enter Student name to update Grade: ")
        for student in alliedSchool.students:
            if name == student.name:
                student.updateGrade()
                break
        else:
            print("Student Not Found!")
            

    elif choice == 10:
        name = input("Enter Teacher name to increase Salary: ")
        for teacher in alliedSchool.teachers:
            if name == teacher.name:
                teacher.increasePay()
                break
        else:
            print("Teacher Not Found!")
    else:
        print("Thanks for using")
        break

