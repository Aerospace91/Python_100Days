"""
Day 38 - Custom Exceptions
Create a custom exception class.
"""


class AerospaceError(Exception):
    def __init__(self, message):
        super().__init__(message)

def ErrorRaiser():
    raise AerospaceError("Aero Error Space Error")

try:
    ErrorRaiser()
except AerospaceError as e:
    print(e)