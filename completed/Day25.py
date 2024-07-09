"""
Day 25 - Words frequency
Write a function to count the frequency of words in a sentence.
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