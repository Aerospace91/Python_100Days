"""
Day 26 - Anagram strings
Write a function check if two strings are anagrams.
"""

str = "listen"
str2 = "silent"

dict1 = {}
dict2 = {}
for c in str:
    if c not in dict1:
        dict1[c] = 1
    else:
        dict1[c] += 1

for c in str2:
    if c not in dict2:
        dict2[c] = 1
    else:
        dict2[c] += 1

print(dict1 == dict2)