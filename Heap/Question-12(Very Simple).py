#  Question 12: Check if a binary tree is a valid heap.
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_complete_binary_tree(root):
    if not root:
        return True

    queue = deque([root])
    has_non_full_node = False

    while queue:
        node = queue.popleft()

        if not node:
            has_non_full_node = True
        else:
            if has_non_full_node:
                return False
            queue.append(node.left)
            queue.append(node.right)

    return True

def is_min_heap_property(node):
    if not node:
        return True

    if node.left and node.val > node.left.val:
        return False
    if node.right and node.val > node.right.val:
        return False

    return is_min_heap_property(node.left) and is_min_heap_property(node.right)

def is_max_heap_property(node):
    if not node:
        return True

    if node.left and node.val < node.left.val:
        return False
    if node.right and node.val < node.right.val:
        return False

    return is_max_heap_property(node.left) and is_max_heap_property(node.right)

def is_binary_min_heap(root):
    return is_complete_binary_tree(root) and is_min_heap_property(root)

def is_binary_max_heap(root):
    return is_complete_binary_tree(root) and is_max_heap_property(root)

root_min_heap = TreeNode(1)
root_min_heap.left = TreeNode(2)
root_min_heap.right = TreeNode(3)
root_min_heap.left.left = TreeNode(4)
root_min_heap.left.right = TreeNode(5)
root_min_heap.right.left = TreeNode(6)
root_min_heap.right.right = TreeNode(7)

print("Is the tree a valid min-heap?", is_binary_min_heap(root_min_heap))

root_max_heap = TreeNode(7)
root_max_heap.left = TreeNode(6)
root_max_heap.right = TreeNode(5)
root_max_heap.left.left = TreeNode(4)
root_max_heap.left.right = TreeNode(3)
root_max_heap.right.left = TreeNode(2)
root_max_heap.right.right = TreeNode(1)

print("Is the tree a valid max-heap?", is_binary_max_heap(root_max_heap))

invalid_heap = TreeNode(1)
invalid_heap.left = TreeNode(2)
invalid_heap.right = TreeNode(3)
invalid_heap.right.right = TreeNode(4)

print("Is the invalid tree a complete binary tree?", is_complete_binary_tree(invalid_heap))
print("Is the invalid tree a valid min-heap?", is_binary_min_heap(invalid_heap))

invalid_heap_property = TreeNode(1)
invalid_heap_property.left = TreeNode(0)
invalid_heap_property.right = TreeNode(3)

print("Is the tree with invalid property a valid min-heap?", is_binary_min_heap(invalid_heap_property))