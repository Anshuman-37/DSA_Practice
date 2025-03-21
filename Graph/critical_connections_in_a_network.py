from typing import List
from collections import defaultdict


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # Build the graph as an adjacency list.
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        # Initialize discovery and low arrays.
        # discovery[u] is the time when node u is first visited.
        # low[u] is the smallest discovery time reachable from u.
        discovery = [-1] * n
        low = [-1] * n
        time = 0
        bridges = []

        def dfs(u: int, parent: int):
            nonlocal time
            discovery[u] = low[u] = time
            time += 1

            for v in graph[u]:
                if v == parent:
                    continue  # Skip the edge back to parent.
                if discovery[v] == -1:  # If v is not visited yet.
                    dfs(v, u)
                    # After dfs, update the low value for u.
                    low[u] = min(low[u], low[v])
                    # If the lowest vertex reachable from v is after u was discovered,
                    # then the edge u-v is a bridge.
                    if low[v] > discovery[u]:
                        bridges.append([u, v])
                else:
                    # v is already visited and is not parent,
                    # update low[u] because v might be part of an earlier cycle.
                    low[u] = min(low[u], discovery[v])

        # Run DFS from all nodes (the graph is connected per problem statement,
        # but this loop is useful if the graph wasn't fully connected).
        for i in range(n):
            if discovery[i] == -1:
                dfs(i, -1)

        return bridges
