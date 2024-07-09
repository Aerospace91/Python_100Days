"""
Day 47 - Stacks
Implement a stack data structure.
"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, items):
        self.items.append(items)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty Stack")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from an empty stack")
    
    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack after pushing 1, 2, 3:", stack)  # Stack after pushing 1, 2, 3: [1, 2, 3]

print("Popped item:", stack.pop())  # Popped item: 3
print("Stack after popping:", stack)  # Stack after popping: [1, 2]