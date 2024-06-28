from Course import Course

class Student:

    def __init__(self,studentName,studentId: int,degree,semester) -> None:
        self.studentName = studentName
        self.studentId = studentId
        self.degree = degree
        self.semester = semester
        self.enrolledCourses = []
        

    def enrollCourse(self,course: Course):
        self.enrolledCourses.append(course)
        print("Course Enrolled Successfully!")


    def __str__(self) -> str:
        courses = " \n".join(self.enrolledCourses)
        return (f"Name:     {self.studentName}\n"
                f"ID:       {self.studentId}\n"
                f"Degree:   {self.degree}\n"
                f"Semester: {self.semester}\n"
                f"Enrolled Courses:     {courses}")