"""
Day 55 - Iterable class.
Implement a custom iterable class.
"""

class SquareNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.limit:
            result = self.n ** 2
            self.n += 1
            return result
        else:
            raise StopIteration

squares = SquareNumbers(10)

for square in squares:
    print(square)