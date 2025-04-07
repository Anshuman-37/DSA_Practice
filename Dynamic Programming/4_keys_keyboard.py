from functools import cache


class Solution:
    def maxA(self, n: int) -> int:
        @cache
        def dfs(n: int) -> int:
            # Base Case just keep printing A will give you max A
            if n <= 5:
                return n
            else:
                # For more than 5 keystrokes, consider two strategies:
                # 1. Press 'A' n times (which yields n 'A's).
                # 2. Use a combination of operations: perform a sequence of
                #    'Ctrl-A, Ctrl-C, and then multiple Ctrl-V's'. The expression
                #    "i * dfs(n - i - 1)" simulates the scenario where 'i' represents
                #    the number of times we press 'Ctrl-V' after performing one 'Ctrl-A'
                #    and one 'Ctrl-C', which takes 2 keystrokes. Hence, "n - i - 1" is the
                #    remaining keystrokes after those operations.
                # The recursive call dfs(n - i - 1) returns the maximum number of 'A's
                # that can be produced with the remaining keystrokes, and multiplying it by
                # i (the number of paste operations) gives the result for that sequence.
                # We take the maximum over all such valid paste counts (3, 4, 5, 6).
                return max(n, max(i * dfs(n - i - 1) for i in [3, 4, 5, 6]))

        return dfs(n)
