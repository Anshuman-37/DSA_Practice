from functools import cache
class Solution:
    def fib(self, n: int) -> int:
        # Top Down way Dynammic Programming
        @cache
        def backtrack(n: int) -> int:
            if n <= 0:
                return 0
            if n == 1:
                return 1
            return backtrack(n-1) + backtrack(n-2)
        ## Bottom Up Dynammic Programming
        def dp(n:int) -> int:
            if n == 1:
                return 1
            current = 0
            prev1 = 1
            prev2 = 0

            # Since range is exclusive and we want to include N, we need to put N+1.
            for i in range(2, n + 1):
                current = prev1 + prev2
                prev2 = prev1
                prev1 = current
            return current
        return backtrack(n)







