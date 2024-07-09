"""
Day 45 - Polymorphism
Implement polymorphism with a shape area calculator.
"""

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, side, height):
        self.side = side
        self.height = height

square = Square(10)
rectangle = Rectangle(10, 20)
tri = Triangle(10, 5)

print(square.area())
print(rectangle.area())
