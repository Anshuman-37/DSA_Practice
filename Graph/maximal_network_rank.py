from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(set)
        for u, v in roads:
            adj[u].add(v)
            adj[v].add(u)

        max_rank = 0
        # Iterate over all pairs of cities
        for city1 in range(n):
            for city2 in range(city1 + 1, n):
                # Sum the connections (network rank) of both cities.
                # Subtract one if there is a direct road between them.
                current_rank = len(adj[city1]) + len(adj[city2])
                if city2 in adj[city1]:
                    current_rank -= 1
                max_rank = max(max_rank, current_rank)

        return max_rank
