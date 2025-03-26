from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # TopDown Approach
        @cache
        def dfs(index: int) -> int:
            if index >= len(questions):
                return 0

            # Option 1 choose current problem
            points = questions[index][0]
            next_start = index + questions[index][1] + 1

            # Or skip and choose next
            return max(points + dfs(next_start), dfs(index + 1))

        return dfs(0)

        # Bottom up approach
        n = len(questions)
        dp = [0] * (n + 1)  # dp[i] is max points from i to n-1, dp[n] is 0

        # Iterate backwards through the questions
        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            next_index = i + brainpower + 1  # Next index after solving question i
            # If next_index is out of bounds, dp[next_index] is effectively 0 (since dp[n] is 0)
            take = points + (dp[next_index] if next_index < n + 1 else 0)
            skip = dp[i + 1]
            dp[i] = max(take, skip)

        return dp[0]