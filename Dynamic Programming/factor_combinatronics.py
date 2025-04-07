from typing import List


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []

        def backtrack(start: int, target: int, path: List[int]):
            # iterate possible factors from 'start' up to sqrt(target)
            i = start
            while i * i <= target:
                if target % i == 0:
                    # Found a valid factorization: add current factor and its complement.
                    res.append(path + [i, target // i])
                    # Recurse to further factorize the quotient.
                    backtrack(i, target // i, path + [i])
                i += 1

        backtrack(2, n, [])
        return res
