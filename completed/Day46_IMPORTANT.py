"""
Day 46 - Class decorators
Use class decorators in Python.
"""

def add_str_method(cls):
    
    def __str__(self):
        return f"{self.__class__.__name__} with attributes: {self.__dict__}"

    # Attach the new __str__ method to the class
    cls.__str__ = __str__
    return cls


@add_str_method
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y


#Example
obj = MyClass(10, 20)
print(obj)