from typing import List
from functools import cache


class Solution:
    def rob(self, nums: List[int]) -> int | None:
        ## Top Down Approach DP
        @cache
        def backtrack(index: int) -> int | None:
            # If there is only one house then he can rob it easily
            if index >= len(nums):
                return 0

            # option 1 he choses first house then can't choose immediate other one
            rob_current = nums[index] + backtrack(index+2)

            # option 2
            skip_current = backtrack(index+1)

            return max(rob_current, skip_current)

        ## Bottom up approach
        n = len(nums)
        # dp[i] represents the maximum money you can rob from house i to end.
        # We can initialize dp[n] = 0 (beyond last house), and dp[n-1] = nums[n-1].
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # Starting from the end:
        dp_next = 0         # This represents dp[i+2] initially.
        dp_curr = nums[-1]  # This represents dp[i+1] initially.

        # Process from the second-last house down to the first.
        for i in range(n-2, -1, -1):
            current = max(nums[i] + dp_next, dp_curr)
            dp_next, dp_curr = dp_curr, current

        return dp_curr
