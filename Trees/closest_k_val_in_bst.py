from typing import Optional, List
from collections import deque
import heapq
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        heap = []

        # To use BFS we will push root node in the queue
        queue = deque([root])

        while queue:
            node = queue.popleft()

            # Calculate the absolute difference between node value and target
            diff = abs(node.val - target)

            # Push negative difference to simulate a max heap.
            heapq.heappush(heap, (-diff, node.val))

            # If heap size exceeds k, remove the element with the largest diff
            if len(heap) > k:
                heapq.heappop(heap)

            # Continue traversal
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Extract and return the k closest values
        return [val for _, val in heap]



