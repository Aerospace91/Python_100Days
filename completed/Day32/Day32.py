"""
Day 32 - File operations: Read
Read and display the contents of a text file.
"""

with open('data.txt', 'r') as e:
    lines = e.readlines()

for line in lines:
    line = line.strip("\n")
    print(line)

