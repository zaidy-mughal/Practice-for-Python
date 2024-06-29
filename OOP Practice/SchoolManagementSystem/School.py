from Person import Person
from Student import Student
from Teacher import Teacher
import random

class School:

    """This is a School class used to perform School's Operations"""

    def __init__(self) -> None:
        self.students = []
        self.teachers = []


    def addTeacher(self):

        name = input("Enter Teacher Name: ")
        age = input("Enter Teacher Age: ")
        id = random.randint(100,999)
        pay = input("Enter Teacher Pay: ")
        experience = input("Enter Teacher Experience: ")
        teacher = Teacher(name,age,id,pay,experience)

        self.teachers.append(teacher)
        print("\nTeacher added Successfully\n")


    def removeTeacher(self):
        teacherName = input("Enter Teacher Name to Remove: ")

        for teacher in self.teachers:
            if teacher.name == teacherName:
                self.teachers.remove(teacher)
                print("\nTeacher removed Successfully!\n")
                break
        else:
            print("Teacher Not Found!")



    def addStudent(self):
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        id = random.randint(100,999)
        grade = input("Enter Student Grade: ")
        feePerMonth= input("Enter Student Fee Per Month: ")

        student = Student(name,age,id,grade,feePerMonth)
        self.students.append(student)
        print("\nStudent added Successfully\n")


    def removeStudent(self):
        studentName = input("Enter Student Name to Remove: ")

        for student in self.students:
            if student.name == studentName:
                self.students.remove(student)
                print("\nStudent removed Successfully!\n")
                break
        else:
            print("\nStudent Not Found!\n")



            


    def searchStudent(self):
        studentName = input("Enter Student Name to Search: ")
        for student in self.students:
            if student.name == studentName:
                print("\n---Student Found---\n")
                print(student)
                break
        else:
            print("\nStudent not Found!\n")


    def searchTeacher(self):
        teacherName = input("Enter Teacher Name to Search: ")
        for teacher in self.teachers:
            if teacher.name == teacherName:
                print("\n---Teacher Found---")
                print(teacher)
                break
        else:
            print("\nTeacher not Found!\n")



    def totalStudents(self):
        print(f"Total Students in School:  {len(self.students)}\n")

    
    def totalTeachers(self):
        print(f"Total Teachers in School:  {len(self.teachers)}\n")


    