"""
Day 9 - Random number generator
1. Write a program that generates a random number. 2. Write a program that generates random number between 2 integers
"""

import random

print(f"Random Number: {random.random()}")

a, b = list(map(int, input("Enter 2 numbers: ").split()))
print(f"Random Number between {a} and {b}: {random.randint(a, b)}")