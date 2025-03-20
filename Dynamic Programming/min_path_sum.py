from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # Initialize dp table with the same dimensions as grid.
        dp = [[0] * n for _ in range(m)]

        # Base case: the starting cell.
        dp[0][0] = grid[0][0]

        # Fill in the first row.
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # Fill in the first column.
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # Process the rest of the grid.
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

        return dp[m - 1][n - 1]
