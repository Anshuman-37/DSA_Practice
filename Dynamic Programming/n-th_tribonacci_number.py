class Solution:
    def tribonacci(self, n: int) -> int:
        # ## Top Down Dynamic Programming
        # @cache
        # def backtrack(n: int) -> int:
        #     if n<= 0:
        #         return 0
        #     if n == 1:
        #         return 1
        #     return backtrack(n-1) + backtrack(n-2) + backtrack(n-3)
        # return backtrack(n)
        ## Bottom Up Dynammic Programming
        def dp(n: int) -> int:
            if n < 3:
                return 1 if n else 0
            dp = [0] * (n + 1)
            dp[1] = dp[2] = 1
            for i in range(3, n+1):
                dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
            return dp[n]
        return dp(n)