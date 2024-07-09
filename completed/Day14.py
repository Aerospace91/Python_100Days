"""
Day 14 - Leap Year
Write a program that checks if a given input year is a leap year or not
"""

def leapyearcheck(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


year = int(input("Enter year to check for leapyear: "))
print(leapyearcheck(year))