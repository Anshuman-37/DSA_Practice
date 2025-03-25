from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)]
        m, n = len(grid), len(grid[0])
        num_of_islands = 0
        visited = set()

        def bfs_helper(row: int, col: int):
            queue = deque([(row, col)])
            while queue:
                row, col = queue.popleft()
                if (row, col) not in visited:
                    visited.add((row, col))
                for dx, dy in directions:
                    nrow, ncol = row + dx, col + dy
                    if (
                            (0 <= nrow < m)
                            and (0 <= ncol < n)
                            and (nrow, ncol) not in visited
                            and grid[nrow][ncol] == "1"
                    ):
                        visited.add((nrow, ncol))
                        queue.append((nrow, ncol))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs_helper(i, j)
                    num_of_islands += 1
        return num_of_islands
