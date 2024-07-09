"""
Day 12 - Odd-even
Write a program to check if a number is even or odd.
"""

def oddevencheck(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

resp = int(input("Enter number to check whether even or odd: "))
print(f"{resp} is {oddevencheck(resp)}")