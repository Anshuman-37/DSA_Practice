class Solution:
    def numSquares(self, n: int) -> int:
        # Look up for the squares
        # squares = [i * i for i in range(1, int(math.sqrt(n)) + 1)]
        # # Top Down approach
        # @cache
        # def dfs(target: int) -> int:
        #     # Base Case
        #     if target == 0:
        #         return 0
        #     if target < 0:
        #         return float('inf')

        #     min_count = float('inf')

        #     for sq in squares:
        #         if sq <= target:
        #             result = dfs(target - sq)
        #             if result != float('inf'):
        #                 min_count = min(min_count, 1 + result)
        #         else:
        #             break
        #     return min_count

        # min_required = dfs(n)
        # return min_required if min_required != float('inf') else -1
        # Bottom Up approach
        dp = [4] * (n + 1)
        dp[0] = 0
        squares = [i * i for i in range(1, int(n ** 0.5) + 1)]

        for i in range(1, n + 1):
            for square in squares:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[n]
