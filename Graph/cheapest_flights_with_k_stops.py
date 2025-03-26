from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman ford
        dp = [float('inf')] * n
        dp[src] = 0

        # Relax the edges up to k+1 times.
        for i in range(k + 1):
            temp = dp.copy()  # Create a copy of the current costs.
            for start, end, price in flights:
                if dp[start] != float("inf"):
                    temp[end] = min(dp[start] + price, temp[end])
            dp = temp

        return dp[dst] if dp[dst] != float('inf') else -1
