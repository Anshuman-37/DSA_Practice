from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        num_of_islands = 0
        m, n = len(grid), len(grid[0])
        visited = set()

        def bfs_helper(row: int, col: int):
            nonlocal num_of_islands
            queue = deque([(row, col)])
            component = []
            isIsland = True  # Assuming its an island
            while queue:
                r, c = queue.popleft()
                component.append((r, c))
                # Check is the boundary is surrounded by water
                for dx, dy in direction:
                    nr, nc = r + dx, c + dy
                    if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                        isIsland = False
                    if (0 <= nr < m and 0 <= nc < n and
                            (nr, nc) not in visited and grid[nr][nc] == 0):
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            if isIsland:
                num_of_islands += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i, j) not in visited:
                    visited.add((i, j))
                    bfs_helper(i, j)

        return num_of_islands
