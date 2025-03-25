from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Base case checks that there are only same amount of edges
        if len(edges) != n - 1: return False

        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)

        seen = set()

        def dfs(node, parent):
            if node in seen: return
            seen.add(node)
            for neib in adj_list[node]:
                if neib == parent:
                    continue
                if neib in seen:
                    return False
                result = dfs(neib, node)
                if not result: return False
            return True

        return dfs(0, -1) and len(seen) == n
