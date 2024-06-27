from Shape import Shape
import math

class Circle(Shape):

    def __init__(self, type, color,radius) -> None:
        super().__init__(type, color)
        self.radius = radius

    def calculateArea(self) -> float:
        return math.pi*self.radius*self.radius
    
    def __str__(self) -> str:
        return (super().__str__()+f"Radius:      {self.radius}\n"
                f"Area of Circle: {self.calculateArea():.2f}\n")