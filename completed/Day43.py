"""
Day 43 - Encapsulation
Implement encapsulation in a class.
"""

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
    
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        self._age = age
    
    def __private_method(self):
        print("Private Method")
    
    def access_private_method(self):
        self.__private_method()
