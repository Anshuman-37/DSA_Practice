from functools import cache
from typing import List


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        @cache
        def helper(n: int, total: int) -> list[str]:
            # Base cases:
            if n == 0:
                return [""]
            if n == 1:
                return ["0", "1", "8"]

            # Get strobogrammatic numbers for inner section.
            middles = helper(n - 2, total)
            result = []

            # Valid digit pairs for strobogrammatic numbers.
            pairs = [("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")]

            for middle in middles:
                for a, b in pairs:
                    # We should not add numbers with leading zeros.
                    if n == total and a == "0":
                        continue
                    result.append(a + middle + b)
            return result

        return helper(n, n)
