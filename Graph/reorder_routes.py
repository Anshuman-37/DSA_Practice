from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        count = 0
        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append((v, 1))
            adj[v].append((u, 0))

        def dfs(node: int, parent: int) -> None:
            nonlocal count
            for neighbor, sign in adj[node]:
                if neighbor == parent:
                    continue  # Avoid going back to the parent.
                count += sign
                dfs(neighbor, node)

        dfs(0, -1)
        return count

