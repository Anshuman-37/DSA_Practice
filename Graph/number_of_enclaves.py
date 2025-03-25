from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        visited = set()
        num_enclaves = 0

        def bfs_helper(row: int, col: int):
            nonlocal num_enclaves
            queue = deque([(row, col)])
            component = []
            isEnclave = True  # Assume it's an enclave unless proven otherwise

            while queue:
                r, c = queue.popleft()
                component.append((r, c))
                # Check if the cell touches the boundary
                if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                    isEnclave = False
                for dx, dy in direction:
                    nr, nc = r + dx, c + dy
                    if (0 <= nr < m and 0 <= nc < n and
                            (nr, nc) not in visited and grid[nr][nc] == 1):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            if isEnclave:
                num_enclaves += len(component)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    bfs_helper(i, j)

        return num_enclaves
