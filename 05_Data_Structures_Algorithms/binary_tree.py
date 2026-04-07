# binary_tree.py

"""
Definition: A Binary Tree is a hierarchical data structure in which each node has at most two children, 
referred to as the left child and the right child.
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

# Creating a simple binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal of binary tree:")
inorder_traversal(root)
print()
