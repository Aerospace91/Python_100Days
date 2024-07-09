"""
Day 48 - Queues
Implement a queue data structure.
"""

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            re = self.items[0]
            self.items = self.items[1:]
            return re
        else:
            raise IndexError("dequeue from an empty queue")
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Peek from an Empty Qeuue")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue after enqueuing 1, 2, 3:", queue)  # Queue after enqueuing 1, 2, 3: [1, 2, 3]

print("Dequeued item:", queue.dequeue())  # Dequeued item: 1
print("Queue after dequeuing:", queue)  # Queue after dequeuing: [2, 3]

print("Front item:", queue.peek())  # Front item: 2

print("Is queue empty?", queue.is_empty())  # Is queue empty? False

print("Queue size:", queue.size())  # Queue size: 2