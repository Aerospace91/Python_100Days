"""
Day 23 - List intersection
Write a function to find the intersection of two lists.
"""
lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 3, 5, 6]
print(list(set(lst1) & set(lst2)))