from Person import Person
from Student import Student
from Teacher import Teacher

class School:

    """This is a School class used to perform School's Operations"""

    def __init__(self) -> None:
        self.students = []
        self.teachers = []


    def searchStudent(self,studentName):
        for student in self.students:
            if student.name == studentName:
                print("\n---Student Found---")
                print(student)
                break
        else:
            print("Student not Found!")


    def searchTeacher(self,teacherName):
        for teacher in self.teachers:
            if teacher.name == teacherName:
                print("\n---Teacher Found---")
                print(teacher)
                break
        else:
            print("Teacher not Found!")



    def totalStudents(self):
        print(f"Total Students in School:  {len(self.students)}\n")

    
    def totalTeachers(self):
        print(f"Total Teachers in School:  {len(self.teachers)}\n")


    