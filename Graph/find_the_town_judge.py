from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = {i: [] for i in range(1, n + 1)}
        trusted_by = {i: 0 for i in range(1, n + 1)}

        for a, b in trust:
            trusts[a].append(b)
            trusted_by[b] += 1

        # The town judge trusts nobody and is trusted by n-1 people.
        for person in range(1, n + 1):
            if not trusts[person] and trusted_by[person] == n - 1:
                return person
        return -1
