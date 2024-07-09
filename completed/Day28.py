"""
Day 28 - Reverse words
Reverse words in a sentence.
"""

str = "This is a sentence reverse the words in this"

str = str.split()

new_str = []

for word in str:
    new_str.append(word[::-1])

new_str = " ".join(new_str)

print(new_str)