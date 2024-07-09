"""
Day 36 - Handle Exceptions I
Handle exceptions for division by zero.
"""

try:
    print(4/0)
except ZeroDivisionError:
    print("Do not Divide by Zero")