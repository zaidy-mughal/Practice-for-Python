from Instructor import Instructor
from Course import Course
from Student import Student
import random


instructors = []
students = []
courses = []
currentStudent = None

print("\n====== University Course Management System ======")
while True:
    print("\n1. Add Instructor")
    print("2. Add Course")
    print("3. Add Student")
    print("4. Enroll Student Course")
    print("5. View Student Details")
    print("6. Press Other than 1-5 to Close.")

    choice = int(input("\nEnter your choice: "))
        
    if choice == 1:
        name = input("Enter Instructor Name: ")
        position = input("Enter Instructors Position: ")
        experience = input("Enter Instructors Experience: ")
        id = random.randint(111,999)

        instructor = Instructor(name,id,position,experience)
        instructors.append(instructor)
        print("Instructor Added Successfully!")

    elif choice == 2:
        courseInstructor = None
        if instructors is not None:

            for instructor in instructors:
                print(instructor)

            name = input("Enter Instructor Name: ")

            for instructor in instructors:
                if name == instructor.instructorName:
                    courseInstructor = instructors

            courseCode = input("Enter Course Code: ")
            courseName = input("Enter Course Name: ")

            course = Course(courseCode,courseName,courseInstructor)
            courses.append(course)
            print("Course Added Successfully!")

        else:
            print("Add Instructor to Add Course")

        
    elif choice == 3:
        print("To Add Student")
        name = input("Enter Student Name: ")
        degree = input("Enter Students Degree: ")
        semester = input("Enter Student Semester: ")
        id = random.randint(1111,9999)

        currentStudent = Student(name,id,degree,semester)
        students.append(currentStudent)
        print("Student Added Successfully!")

        
    elif choice == 4:

        if currentStudent is not None:
            courseName = input("Enter Course name: ")

            for course in courses:
                print(course)

            for course in courses:
                if courseName == course.courseName:
                    currentStudent.enrollCourse(course)
                    print("Course Successfully Enrolled!")
                    break
            else:
                print("Course Not Found!")

        else:
            print("Course not Found!")

    elif choice == 5:
        if students is not None:
            for student in students:
                print(student)
        else:
            print("Add Students First.")

    else:
        print("Thanks for using! Bye Bye")
        break