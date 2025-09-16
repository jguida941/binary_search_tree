# binary_search_tree

# Simple Binary Search Tree in Python

A minimal example of a Binary Search Tree (BST) implemented with classes and recursion.

## Features
- Insert nodes
- Search for values
- Delete nodes (handles 0, 1, 2 children)
- Inorder traversal (prints sorted contents)

## Example
```python
from bst import BinarySearchTree

bst = BinarySearchTree()
for v in [50, 30, 20, 40, 70, 60, 80]:
    bst.insert(v)

print("Inorder:", bst.inorder())   # [20, 30, 40, 50, 60, 70, 80]

from bst import BinarySearchTree

bst = BinarySearchTree()
for val in [50, 30, 20, 40, 70, 60, 80]:
    bst.insert(val)

print("Inorder before delete:", bst.inorder())
print("Search 80:", bst.search(80))
bst.delete(80)
print("Inorder after delete:", bst.inorder())
