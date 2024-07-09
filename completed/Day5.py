"""
Day 5 - Conditional Statements
1. Write a program that reads an integer as user input and prints whether the number is Odd or Even to the console
2. Write a program that takes three numbers as input and prints the largest among them
3. Write a program that checks if a given input year is a leap year or not
4. Write a program that reads the percentage and then prints their corresponding letter grade (A, B, C, D, or F)
"""

def oddevencheck(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

def maxcheck(num1, num2, num3):
    print(max([num1, num2, num3]))

def leapyearcheck(year):
    print(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

def gradecheck(num):
    if num >= 90:
        print("A")
    elif num >= 80:
        print("B")
    elif num >= 70:
        print("C")
    elif num >= 60:
        print("D")
    else:
        print("F")

oddeven = int(input("Number to check if odd or even: "))
oddevencheck(oddeven)
max1, max2, max3 = int(input("First number to check which is max: ")), int(input("Second number to check which is max: ")), int(input("Third number to check which is max: "))
maxcheck(max1, max2, max3)
leapyear = int(input("Input year to check if leap year: "))
leapyearcheck(leapyear)
grade = int(input("Enter percentage to check grade: "))
gradecheck(grade)