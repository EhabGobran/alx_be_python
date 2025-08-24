import math

class Shape:
    def area(self):
        return NotImplementedError()
    
class Rectangle(Shape):
    def __init__(self, length:int, width:int):
        self.length = length
        self.width = width
    
    def area(self)->int:
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius:int):
        self.radius = radius
        self.pi = math.pi

    def area(self)->float:
        return self.pi * self.radius ** 2 
    