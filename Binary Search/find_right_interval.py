from typing import List
import bisect


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ints = sorted([[j, k, i] for i, [j, k] in enumerate(intervals)])
        begs = [i for i, _, _ in ints]
        res = [-1] * len(begs)
        for i, j, k in ints:
            t = bisect.bisect_left(begs, j)
            if t < len(begs):
                res[k] = ints[t][2]
        return res
