from typing import List


class Solution:
    def hasPath(self, grid: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(row: int, col: int) -> bool:
            if (row, col) in visited:
                return False
            if [row, col] == destination:
                return True

            visited.add((row, col))

            for dx, dy in directions:
                newRow, newCol = row, col
                # Roll the ball until it hits a wall
                while 0 <= newRow + dx < m and 0 <= newCol + dy < n and grid[newRow + dx][newCol + dy] == 0:
                    newRow += dx
                    newCol += dy
                # If this stopping position leads to a solution, return True.
                if dfs(newRow, newCol):
                    return True
            return False

        return dfs(start[0], start[1])
