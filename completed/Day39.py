"""
Day 39 - Class Object
Create a class for a simple car with methods like start and stop.
"""

class Car:
    def __init__(self, length, width, make, model):
        self.length = length
        self.width = width
        self.make = make
        self.model = model
        self.accel = 0
        self.speed = 0

    def start(self):
        self.accel += 5
    
    def stop(self):
        self.speed = 0
    
    def accels(self):
        self.speed += self.accel


honda = Car(5, 10, 'Honda', 'Insight')
print(honda.speed)
honda.start()
honda.accels()
print(honda.speed)
honda.stop()
print(honda.speed)