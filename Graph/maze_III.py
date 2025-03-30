from typing import List
import heapq


class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m, n = len(maze), len(maze[0])
        # Convert hole and ball to tuples for easier comparison.
        hole = (hole[0], hole[1])
        start = (ball[0], ball[1])

        # Directions sorted by letter so that when distances tie, lexicographical order is used. 'd' < 'l' < 'r' < 'u'
        directions = [
            (1, 0, 'd'),
            (0, -1, 'l'),
            (0, 1, 'r'),
            (-1, 0, 'u')
        ]

        # Priority queue: (distance so far, instruction string, x, y)
        pq = [(0, "", start[0], start[1])]
        # Dictionary to record the best (distance, path) achieved at a given cell.
        best = {start: (0, "")}

        while pq:
            dist, path, x, y = heapq.heappop(pq)
            # If we reached the hole, return the path.
            if (x, y) == hole:
                return path

            # If we have already found a better way to (x, y), skip this state.
            if best[(x, y)] < (dist, path):
                continue

            # Try each direction.
            for dx, dy, move in directions:
                nx, ny = x, y
                d = 0
                # Roll until hitting a wall or falling into the hole.
                while 0 <= nx + dx < m and 0 <= ny + dy < n and maze[nx + dx][ny + dy] == 0:
                    nx += dx
                    ny += dy
                    d += 1
                    if (nx, ny) == hole:
                        # Once the ball falls into the hole, it stops immediately.
                        break

                new_dist = dist + d
                new_path = path + move

                # Only update if this path is better (smaller distance or lexicographically smaller for same distance).
                if (nx, ny) not in best or (new_dist, new_path) < best[(nx, ny)]:
                    best[(nx, ny)] = (new_dist, new_path)
                    heapq.heappush(pq, (new_dist, new_path, nx, ny))

        return "impossible"
