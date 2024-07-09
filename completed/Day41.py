"""
Day 41 - Inheritance
Implement inheritance between classes.
"""

class Shape:
    def __init__(self):
        self.isshape = True

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__()

class Square(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = length * width
        super().__init__()

class Triangle(Shape):
    def __init__(self, side, height):
        self.side = side
        self.height = height
        super().__init__()


circle = Circle(20)
square = Square(30, 40)
triangle = Triangle(30, 5)
