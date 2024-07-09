"""
Day 13 - Largest of three numbers.
Write a program to find the largest of three numbers.
"""

def maxcheck(num1, num2, num3):
    return max([num1, num2, num3])

max1, max2, max3 = int(input("First number to check which is max: ")), int(input("Second number to check which is max: ")), int(input("Third number to check which is max: "))
print(f"The max of the numbers is: {maxcheck(max1, max2, max3)}")