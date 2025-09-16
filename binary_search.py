"""
TreeNode = the building block (stores data + left/right children).
BinarySearchTree (BST) = manages the root and overall tree operations.

- _insert(node, key): recursive engine that walks the tree and finds the correct spot.
- insert(key): public wrapper, starts at root (so you don’t pass self.root manually).
- _search(node, key): recursive engine, checks left or right branch.
- search(key): public wrapper for _search.
- _delete(node, key): recursive engine that removes a node:
    * no children → return None
    * one child   → return that child
    * two children→ replace with inorder successor, then recurse
- delete(key): public wrapper for _delete.

In short:
    Insert → find the empty slot and attach.
    Search → keep halving the space until found/None.
    Delete → handle 3 cases (0, 1, 2 children).
"""


# Blueprint for nodes in tree
class TreeNode:

    # Constructor
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    # Convert memory instance into a string
    def __str__(self):
        return str(self.key)


# Blueprint for whole tree not just the node
class BinarySearchTree:
    # constructor , sets up new empty tree
    def __init__(self):
        # Initializes the root (topmost node) as empty.
        self.root = None

    # Define method to recursively insert into the tree.
    def _insert(self, node, key):
        if node is None:
            # Fills that empty spot with the new data.
            return TreeNode(key)

        if key < node.key:
            # Recursively insert into the left subtree
            node.left = self._insert(node.left, key)

        elif key > node.key:
            # Recursively insert into the right subtree.
            node.right = self._insert(node.right, key)
        return node

    # Call the helper method insert
    def insert(self, key):
        self.root = self._insert(self.root, key)

    # Define helper method for search
    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        if key > node.key:
            return self._search(node.right, key)

    # Public search method (calls the recursive _search helper)
    def search(self, key):
        return self._search(self.root, key)

    # Helper method for search
    def _delete(self, node, key):
        if node is None:
            # key not found so return node
            return node
        if key < node.key:
            # delete specified key
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # 2 children: replace with inorder successor (min in right subtree)
            succ = node.right
            while succ.left:
                succ = succ.left
            node.key = succ.key
            node.right = self._delete(node.right, succ.key)
        return node

    # Public search method
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def inorder(self):
        result = []

        def dfs(node):
            if not node: return
            dfs(node.left)
            result.append(node.key)
            dfs(node.right)

        dfs(self.root)
        return result

# Call the methods
bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]

# Loop through nodes and insert them into the bst
for node in nodes:
    bst.insert(node)
#Search for 80
print('Search for 80:', bst.search(80))

#Shows inorder before and after delete
print("Inorder before delete:", bst.inorder())  # [20, 30, 40, 50, 60, 70, 80]
bst.delete(80)
print("Inorder after delete :", bst.inorder())  # [20, 30, 40, 50, 60, 70]
