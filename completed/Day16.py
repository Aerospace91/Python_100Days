"""
Day 16 - Palindrome String
Write a function to check if a given string is a palindrome.
"""

palin = input("Enter string to check for Palindrone: ")

if palin == palin[::-1]:
    print(True)
else:
    print(False)