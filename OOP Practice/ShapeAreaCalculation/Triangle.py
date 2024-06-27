from Shape import Shape

class Triangle(Shape):

    def __init__(self, type, color,base,height) -> None:
        super().__init__(type, color)
        self.base = base
        self.height = height

    def calculateArea(self) -> float:
        return 0.5*(self.base*self.height)
    
    def __str__(self) -> str:
        return (super().__str__()+f"Base:      {self.base}\n"
                f"Height:       {self.height}\n"
                f"Area of Triangle: {self.calculateArea():.2}\n")