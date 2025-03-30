from typing import List


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # Initialize parent and rank arrays.
        parent = [-1] * (m * n)
        rank = [0] * (m * n)

        # Find function with path compression.
        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # Union function: returns 1 if two separate sets are merged, otherwise 0.
        def union(x: int, y: int) -> int:
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                # Union by rank.
                if rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                elif rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
                return 1
            return 0

        # Directions for adjacent cells.
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        result = []
        count = 0

        for r, c in positions:
            idx = r * n + c
            # If the cell is already land, append the current island count.
            if parent[idx] != -1:
                result.append(count)
                continue

            # Mark cell as land and consider it a new island.
            parent[idx] = idx
            count += 1

            # Check all 4 neighboring cells.
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                n_idx = nr * n + nc
                if 0 <= nr < m and 0 <= nc < n and parent[n_idx] != -1:
                    # If neighbor is land and not already connected, merge them.
                    if union(idx, n_idx):
                        count -= 1

            result.append(count)

        return result
