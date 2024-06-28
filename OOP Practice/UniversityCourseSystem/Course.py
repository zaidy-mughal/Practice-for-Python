from Instructor import Instructor

class Course:

    """This class is used to handle course operations and Instructor is Composed in this class"""
    
    def __init__(self,courseCode,courseName,courseInstructor: Instructor) -> None:
        self.courseCode = courseCode
        self.courseName = courseName
        self.courseInstructor = courseInstructor

    def __str__(self) -> str:
        return (f"Course Code: {self.courseCode}\n"
                f"Course Name: {self.courseName}\n"
                f"Course Instructor: \n{self.courseInstructor}\n")
    