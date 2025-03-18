from typing import Optional, List, Union

# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def cloneTree(self, root: 'Node') -> Union['Node',None]:
        # Recursvie Approach Takes O(n) time and O(n) space
        # if not root:
        #     return root
        #
        # node_copy = Node(root.val)
        # for child in root.children:
        #     node_copy.children.append(self.cloneTree(child))
        #
        # return node_copy

        # Iterative Approach Takes O(n) time and space O(log n) as we are using Stack to optimize for it
        new_root = Node(root.val)
        # Starting point to kick off the DFS visits.
        stack = [(root, new_root)]

        while stack:
            old_node, new_node = stack.pop()
            for child_node in old_node.children:
                new_child_node = Node(child_node.val)

                # Make a copy for each child node.
                new_node.children.append(new_child_node)

                # Schedule a visit to copy the child nodes of each child node.
                stack.append((child_node, new_child_node))

        return new_root
