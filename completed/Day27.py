"""
Day 27 - Longest word
Find the longest word in a sentence.
"""

str = "Time to find the longest word in a sentence this is fun"

str = str.split()

largest = ""
length = 0

for word in str:
    count = 0
    for c in word:
        count += 1
    if count > length:
        length = count
        largest = word

print(f"The largest word is {largest} at {length} letters")