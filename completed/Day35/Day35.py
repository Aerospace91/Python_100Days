"""
Day 35 - File operations
Calculate the average of numbers in a text file.
"""

with open('data.txt', 'r') as e:
    lines = e.read().splitlines()

sum = 0
count = 0
for line in lines:
    line = line.split()
    for num in line:
        sum += int(num)
        count += 1

print(sum / count)