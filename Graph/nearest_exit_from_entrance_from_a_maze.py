from typing import List
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        ex, ey = entrance
        maze[ex][ey] = "+"

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque([(ex, ey)])
        steps = 0

        while q:
            # Process all nodes in the current level.
            for _ in range(len(q)):
                x, y = q.popleft()

                # If we're not at the entrance and we're on the boundary, we've found an exit.§
                if (x != ex or y != ey) and (x == 0 or x == rows - 1 or y == 0 or y == cols - 1):
                    return steps

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    # Check if new coordinates are within bounds.
                    if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == ".":
                        q.append((nx, ny))
                        # Mark the cell as visited.
                        maze[nx][ny] = "+"
            steps += 1

        # No exit found.
        return -1






