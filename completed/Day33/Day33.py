"""
Day 33 - File operations: Write
Write data to a text file.
"""

str = "Sample Text"

with open("data.txt", "w") as e:
    e.write(str)
