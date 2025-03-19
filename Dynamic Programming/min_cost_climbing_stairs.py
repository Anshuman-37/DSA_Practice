from typing import List
from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ## Top Down DP
        @cache
        def backtrack(steps: int):
            if steps <= 1:
                return 0
            down_one = cost[steps-1] + backtrack(steps-1)
            down_two = cost[steps-2] + backtrack(steps-2)
            return min(down_one, down_two)
        return backtrack(len(cost))


