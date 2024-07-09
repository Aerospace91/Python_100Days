"""
Day 29 - Words frequency
Create a dictionary of words and their frequencies.
"""

str = "Hello hello testing word count count count"
str = str.lower().split()

dict = {}
for word in str:
    if word not in dict:
        dict[word] = 1
    else:
        dict[word] += 1

print(dict)