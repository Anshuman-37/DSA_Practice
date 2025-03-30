import heapq
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        min_cost = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            cost = heapq.heappop(sticks) + heapq.heappop(sticks)
            heapq.heappush(sticks, cost)
            min_cost += cost
        return min_cost
