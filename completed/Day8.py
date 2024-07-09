"""
Day 8 - Simple Calculator
Create a simple calculator program that can add, subtract, multiply, and divide two integers
"""

expression = input("Enter math expression(Format: 3 + 4, 4 * 5): ")

def calculate(expr):
    expr = expr.split()
    a = int(expr[0])
    b = int(expr[2])
    # print(a, b)
    match expr[1]:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b

print(f"{expression} = {calculate(expression)}")