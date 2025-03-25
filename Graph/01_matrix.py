from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Perfect solution to do a BFS traversal and then use DP on top to make it more efficient
        m, n = len(mat), len(mat[0])
        res = [[float('inf')] * n for _ in range(m)]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    queue.append((i, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            i, j = queue.popleft()
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                # Check bounds and update if a shorter distance is found
                if 0 <= ni < m and 0 <= nj < n and res[ni][nj] > res[i][j] + 1:
                    res[ni][nj] = res[i][j] + 1
                    queue.append((ni, nj))
        return res
