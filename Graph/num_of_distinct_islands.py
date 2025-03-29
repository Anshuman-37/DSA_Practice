from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        distinct_islands = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(row: int, col: int):
            # use (row, col) as the reference point for relative positions
            start_row, start_col = row, col
            shape = []
            queue = deque([(row, col)])
            visited.add((row, col))

            while queue:
                r, c = queue.popleft()
                # record the relative position
                shape.append((r - start_row, c - start_col))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < m and 0 <= nc < n and
                            grid[nr][nc] == 1 and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            # Add a tuple version of the shape to the set
            distinct_islands.add(tuple(shape))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    bfs(i, j)

        return len(distinct_islands)
