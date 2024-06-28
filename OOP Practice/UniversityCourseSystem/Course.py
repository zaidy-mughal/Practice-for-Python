from Instructor import Instructor

class Course:
    
    def __init__(self,courseCode,courseName,courseInstructor: Instructor) -> None:
        self.courseCode = courseCode
        self.courseName = courseName
        self.courseInstructor = courseInstructor

    def __str__(self) -> str:
        return (f"Course Code: {self.courseCode}\n"
                f"Course Name: {self.courseName}\n"
                f"Course Instructor: \n{self.courseInstructor}\n")
    