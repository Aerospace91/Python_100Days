"""
Day 17 - Number of vowels in a string
Write a function to count the number of vowels in a string.
"""

vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

str = input("Enter string: ")

count = 0
for c in str:
    if c in vowels:
        count += 1

print(f"Number of vowels: {count}")