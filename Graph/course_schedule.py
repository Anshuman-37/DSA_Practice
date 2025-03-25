from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, ncourses: int, prereqs: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        indeg = {}
        for dest, src in prereqs:
            adj_list[src].append(dest)
            indeg[dest] = indeg.get(dest, 0) + 1

        zero_indeg_queue = deque([k for k in range(ncourses) if k not in indeg])

        topo_order = []
        while zero_indeg_queue:
            vertex = zero_indeg_queue.popleft()
            topo_order.append(vertex)
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indeg[neighbor] -= 1

                    # Add neighbor to Q if in-degree becomes 0
                    if indeg[neighbor] == 0:
                        zero_indeg_queue.append(neighbor)
        return topo_order if len(topo_order) == ncourses else []
