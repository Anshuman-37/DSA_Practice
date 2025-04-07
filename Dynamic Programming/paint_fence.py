class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k

        # For post 2:
        same = k  # ways to paint two posts with same color
        diff = k * (k - 1)  # ways to paint two posts with different colors

        for i in range(3, n + 1):
            # New same becomes the previous diff (only if the last two were different)
            new_same = diff
            # New diff is total ways from previous post times (k - 1)
            new_diff = (same + diff) * (k - 1)
            same, diff = new_same, new_diff

        return same + diff
