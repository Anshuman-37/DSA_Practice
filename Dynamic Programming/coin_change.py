class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Top Down Aproach
        @cache
        def backtrack(remainder: int) -> int:
            if remainder < 0:
                return -1

            if remainder == 0:
                return 0

            min_cost = float('inf')
            for coin in coins:
                result = backtrack(remainder - coin)
                if result != -1:
                    min_cost = min(min_cost, result + 1)
            return min_cost if min_cost != float('inf') else -1
        return backtrack(amount)
        ## Bottom Approach
        # Initialize the DP table with a value larger than any possible answer
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed for amount 0

        # Build the table in a bottom-up manner
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # If dp[amount] is still infinity, then it is not possible to form that amount
        return dp[amount] if dp[amount] != float('inf') else -1

        # Bottom Up approach





