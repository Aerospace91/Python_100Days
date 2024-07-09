"""
Day 49 - Binary Search Tree
Implement a binary search tree.
"""

"""
A Binary Search Tree (BST) is a data structure where each node has at most two children referred to as left and right child.
Left Child - Less then Nodes value
Right Child - More then Nodes value
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)
    
    def _insert(self, current_node, key):
        if key < current_node.val:

            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert(current_node.left, key)
        elif key > current_node.val:

            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert(current_node.right, key)

    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, current_node, key):
        if current_node is None:
            return False
        if key == current_node.val:
            return True
        elif key < current_node.val:
            return self._search(current_node.left, key)
        else:
            return self._search(current_node.right, key)
    
    def inorder_traversal(self):
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, current_node):
        res = []
        if current_node:
            res = self._inorder_traversal(current_node.left)
            res.append(current_node.val)
            res = res + self._inorder_traversal(current_node.right)
        return res


bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("Inorder traversal of the BST:", bst.inorder_traversal())  # Inorder traversal of the BST: [20, 30, 40, 50, 60, 70, 80]

print("Search 40 in BST:", bst.search(40))  # Search 40 in BST: True
print("Search 25 in BST:", bst.search(25))  # Search 25 in BST: False