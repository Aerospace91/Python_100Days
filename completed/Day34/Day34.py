"""
Day 34 - File operations: Append
Append data to an existing text file.
"""

str1 = "Line 4\n"
str2 = "Line 5\n"

with open('data.txt', 'a') as e:
    e.write(str1)
    e.write(str2)

