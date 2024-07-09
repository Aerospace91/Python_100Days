"""
Day 37 - Handle Exceptions II
Handle exceptions for file not found.
"""

try:
    with open('data.txt', 'r') as f:
        f = f.read()
except FileNotFoundError as e:
    print(e)