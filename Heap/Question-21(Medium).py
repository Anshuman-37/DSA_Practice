# Question 21: Convert a BST to a min-heap.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bst_to_min_heap(root):
    sorted_values = []
    def inorder(node):
        if node:
            inorder(node.left)
            sorted_values.append(node.val)
            inorder(node.right)
    inorder(root)

    index = 0
    queue = deque([root])
    while queue:
        node = queue.popleft()
        node.val = sorted_values[index]
        index += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return root

# Example (assuming you have a BST constructed)
# Create a sample BST
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

min_heap_root = bst_to_min_heap(root)

def level_order_values(root):
    values = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        values.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return values

print(f"Min-heap values (level order): {level_order_values(min_heap_root)}")