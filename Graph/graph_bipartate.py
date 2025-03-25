from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        seen = {}  # dictionary to track visited nodes and their colors

        def check(start: int) -> bool:
            q = deque([(start, 1)])  # Initialize deque with a tuple (node, color)
            while q:
                node, color = q.popleft()
                if node in seen:
                    if seen[node] != color:
                        return False
                    continue
                seen[node] = color
                for neighbor in graph[node]:
                    q.append((neighbor, -color))
            return True

        for i in range(len(graph)):
            if i not in seen:
                if not check(i):
                    return False
        return True