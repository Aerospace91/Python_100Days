"""
Day 7 - Temparature Conversion
1. Write a program to convert temperature from Celsius to Fahrenheit. 2. Write a program to convert temperature from Fahrenheit to Celsius
"""

def ctof(num):
    print(f"{(num * (9/5)) + 32:.2f}")

def ftoc(num):
    print(f"{(num - 32) * (5/9):.2f}")

temperature = input("Enter temperature in the form of 32c or 45f: ")
temptype = temperature[-1]
tempnumber = float(temperature[0:len(temperature) - 1])

if temptype == "f":
    ftoc(tempnumber)
elif temptype == "c":
    ctof(tempnumber)
else:
    print("Invalid, Input F for fahrenheit or C for Celsius")