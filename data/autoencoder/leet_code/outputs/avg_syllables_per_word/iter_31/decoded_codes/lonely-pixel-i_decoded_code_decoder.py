from typing import List

class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        if picture is None or len(picture) == 0 or len(picture[0]) == 0:
            return 0

        m, n = len(picture), len(picture[0])
        row_count = [0] * m
        col_count = [0] * n

        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    row_count[i] += 1
                    col_count[j] += 1

        lonely_pixel_count = 0
        for i in range(m):
            if row_count[i] == 1:  # Only check rows with exactly one B to optimize slightly
                for j in range(n):
                    if picture[i][j] == 'B' and col_count[j] == 1:
                        lonely_pixel_count += 1

        return lonely_pixel_count