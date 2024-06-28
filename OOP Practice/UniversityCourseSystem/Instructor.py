
class Instructor:

    """This class is used to manage instructor related tasks"""

    def __init__(self,instructorName,instructorId,position,experience) -> None:
        self.instructorName = instructorName
        self.instructorId = instructorId
        self.position = position
        self.experience = experience

    def changePosition(self,newPosition):
        self.position = newPosition
        print("Position Changed Successfully!")

    def __str__(self) -> str:
        return (f"Name:         {self.instructorName}\n"
                f"ID:           {self.instructorId}\n"
                f"Position:     {self.position}\n"
                f"Experience:   {self.experience}\n")