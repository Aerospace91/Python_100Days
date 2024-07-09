"""
Day 52 - Hash Table
Implement a hash table.
"""

class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def __len__(self):
        return self.size

    def _hash(self, key):
        hash_value = 0
        for char in key:
            hash_value = (hash_value + ord(char)) % self.size
        return hash_value

    def insert(self, key, value):
        index = self._hash(key)
        if self.data[index] is None:
            self.data[index] = []
        self.data[index].append((key,value))

    def get(self, key):
        index = self._hash(key)
        if self.data[index] is not None:
            for k, v in self.data[index]:
                if k == key:
                    return v
        return None

    def delete(self, key):
        index = self._hash(key)
        if self.data[index] is not None:
            for i, (k, v) in enumerate(self.data[index]):
                if k == key:
                    del self.data[index][i]
                    return

# Create a hash table with size 10
hash_table = HashTable(10)

# Insert key-value pairs
hash_table.insert("apple", 10)
hash_table.insert("orange", 20)

# Retrieve values
print(hash_table.get("apple"))   # Output: 10
print(hash_table.get("orange"))  # Output: 20

# Delete a key-value pair
hash_table.delete("apple")

# Check if deletion worked
print(hash_table.get("apple"))   # Output: None