from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        max_side = 0

        # Initialize first row and first column
        for i in range(m):
            dp[i][0] = 1 if matrix[i][0] == "1" else 0
            max_side = max(max_side, dp[i][0])
        for j in range(n):
            dp[0][j] = 1 if matrix[0][j] == "1" else 0
            max_side = max(max_side, dp[0][j])

        # Fill the dp table
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    max_side = max(max_side, dp[i][j])
                else:
                    dp[i][j] = 0

        return max_side * max_side
