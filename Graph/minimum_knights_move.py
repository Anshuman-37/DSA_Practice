from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # Direction a knight can take
        direction = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        directions = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        def bfs(x: int, y: int) -> int:
            visited = set()
            queue = deque([(0, 0)])
            steps = 0

            while queue:
                curr_level_count = len(queue)
                for _ in range(curr_level_count):
                    curr_x, curr_y = queue.popleft()
                    if (curr_x, curr_y) == (x, y):
                        return steps

                    for dx, dy in directions:
                        next_x, next_y = curr_x + dx, curr_y + dy
                        if (next_x, next_y) not in visited:
                            visited.add((next_x, next_y))
                            queue.append((next_x, next_y))
                steps += 1

            # If (x, y) is unreachable, return -1 or an appropriate value
            return -1

        return bfs(x, y)
