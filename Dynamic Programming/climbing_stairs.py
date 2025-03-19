from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        ## Recursion with memomization DP top down approach
        # @cache
        # def rec(steps: int) -> int:
        #     # Base Case
        #     # the count has exceded the intendend target
        #     if steps > n:
        #         return 0
        #     #
        #     if steps == n:
        #         return 1
        #     # You can either take 1 step or you can take 2 steps
        #     return rec(steps+1) + rec(steps+2)
        # return rec(0)

        ## Dynamic Programming Bottom Up approach
        dp = [0 for _ in range(n + 1)]
        ## Try to formulate a formula for this DP problem
        ## As you can see for n = 0 ? the value should be 0
        ## For n = 1 the value can be 1 as you can take only 1 step
        ## For n = 2 the value can be 2 asn you can either take 1 step 2 time or 2 steps
        ## For n = 3 the value will be
        dp[1] , dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]



