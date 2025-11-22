from collections import defaultdict
from typing import List

class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        if not picture or not picture[0]:
            return 0

        m, n = len(picture), len(picture[0])
        row_count = [0] * m
        col_count = [0] * n
        row_patterns = defaultdict(int)

        for r in range(m):
            pattern = ''.join(picture[r])
            row_patterns[pattern] += 1
            for c in range(n):
                if picture[r][c] == 'B':
                    row_count[r] += 1
                    col_count[c] += 1

        lonely_pixels = 0

        for r in range(m):
            pattern = ''.join(picture[r])  # compute once per row
            for c in range(n):
                if picture[r][c] == 'B':
                    if (row_count[r] == target and
                        col_count[c] == target and
                        row_patterns[pattern] == target):
                        lonely_pixels += 1

        return lonely_pixels