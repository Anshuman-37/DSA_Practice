from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start with the last row, because we can accumulate from the bottom up.
        dp = triangle[-1][:]  # Make a copy of the last row

        # Iterate from the second-to-last row up to the top.
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                # For each element, choose the minimum path from the two adjacent numbers below.
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        # The top element of dp now contains the minimum path sum from top to bottom.
        return dp[0]
