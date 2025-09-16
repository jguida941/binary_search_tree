# Binary Search Tree (BST) in Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Recursion](https://img.shields.io/badge/Recursion-Enabled-green)
![Data Structures](https://img.shields.io/badge/Data%20Structures-BST-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

A minimal example of a Binary Search Tree (BST) implemented with classes and recursion.

## Features
- Insert nodes
- Search for values
- Delete nodes (handles 0, 1, 2 children)
- Inorder traversal (prints sorted contents)

## Example
```python
from binary_search_tree import BinarySearchTree  # adjust filename if different

bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]

# Insert
for node in nodes:
    bst.insert(node)

# Search
print('Search for 80:', bst.search(80))  # -> 80

# Inorder before/after delete
print('Inorder before delete:', bst.inorder())  # [20, 30, 40, 50, 60, 70, 80]
bst.delete(80)
print('Inorder after delete :', bst.inorder())  # [20, 30, 40, 50, 60, 70]
```

## Extra Methods You Can Add

- **min() / max()**
```python
def min(self):
    node = self.root
    while node and node.left:
        node = node.left
    return node.key if node else None

def max(self):
    node = self.root
    while node and node.right:
        node = node.right
    return node.key if node else None
```

- **height()**
```python
def height(self, node=None):
    if node is None:
        node = self.root
    if not node:
        return -1  # empty tree has height -1
    return 1 + max(self.height(node.left), self.height(node.right))
```
