from typing import List


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        distances = [[float('inf')] * n for _ in range(m)]
        distances[start[0]][start[1]] = 0

        # Priority queue holds (distance, row, col)
        heap = [(0, start[0], start[1])]

        # Directions: down, up, right, left.
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            dist, row, col = heapq.heappop(heap)
            # If we have reached the destination, return the distance.
            if [row, col] == destination:
                return dist
            # If this distance is not the current best, skip.
            if dist > distances[row][col]:
                continue

            for dx, dy in directions:
                new_row, new_col = row, col
                count = 0
                # Roll the ball until hitting a wall.
                while 0 <= new_row + dx < m and 0 <= new_col + dy < n and maze[new_row + dx][new_col + dy] == 0:
                    new_row += dx
                    new_col += dy
                    count += 1

                # If the new path is shorter, update and push into the heap.
                if dist + count < distances[new_row][new_col]:
                    distances[new_row][new_col] = dist + count
                    heapq.heappush(heap, (distances[new_row][new_col], new_row, new_col))

        # If destination is unreachable, return -1.
        return -1
