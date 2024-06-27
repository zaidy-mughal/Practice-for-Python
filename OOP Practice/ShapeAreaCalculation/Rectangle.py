from Shape import Shape

class Rectangle(Shape):

    def __init__(self, type, color,length,width) -> None:
        super().__init__(type, color)
        self.length = length
        self.width = width

    def calculateArea(self) -> float:
        return self.length*self.width
    
    def __str__(self) -> str:
        return (super().__str__()+f"Length:      {self.length}\n"
                f"Width:       {self.width}\n"
                f"Area of Rectangle: {self.calculateArea():.2f}\n")