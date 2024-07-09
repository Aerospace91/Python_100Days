"""
Day 4 - Arithmetic Operations
1. Write a program that declares two integer variables and perform basic arithmetic operations (addition, subtraction, multiplication, division) on them. Print the results to the console.
2. Write a program that calculates the area of a rectangle. Prompt the user to input the length(integer) and width(integer) of the rectangle, calculate the area (length * width), and print the result.
3. Modify the above program to read decimal numbers as the length and width, and output the area to two decimal points
"""

a = int(input("A: "))
b = int(input("B: "))

print(f"The sum of inputs is {a+b}, the difference is {a-b}, the multiplication is {a*b}, the divison is {a/b}")

length = float(input("What is the length of the rectange? "))
width = float(input("What is the width of the rectangle? "))
print(f"The area of the rectangle is {length * width:.2f}")