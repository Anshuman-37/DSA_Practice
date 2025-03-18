from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        # Base Case you can't perform two sum if one of them or both of them are empty
        if not root1 and not root2:
            return False
        if not root1 or not root2:
            return False

        # Find using binary search for the remainder solution how you do it in Hashmap for Two Sum
        def binary_search(root2: TreeNode | None, target_val: int) -> bool:
            if not root2:
                return False
            if root2.val == target_val:
                return True
            elif root2.val > target_val:
                return binary_search(root2.left, target_val)
            else:
                return binary_search(root2.right, target_val)

        # We will try a depth first search to find what we need
        def dfs(root: TreeNode | None, target_val: int) -> bool:
            if not root:
                return False
            if binary_search(root2, target_val - root.val):
                return True
            return dfs(root.left, target_val) or dfs(root.right, target_val)

        return dfs(root1, target)








