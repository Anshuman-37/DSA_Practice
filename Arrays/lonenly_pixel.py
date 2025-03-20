from typing import List

class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        # Get dimensions of the picture
        m, n = len(picture), len(picture[0])

        # Count black pixels per row and per column
        row_count = [0] * m
        col_count = [0] * n

        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    row_count[i] += 1
                    col_count[j] += 1

        # Now count lonely pixels: a pixel is lonely if it is 'B'
        # and its row and column each have exactly one 'B'
        lonely = 0
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B' and row_count[i] == 1 and col_count[j] == 1:
                    lonely += 1

        # Return the final count of lonely pixels
        return lonely





