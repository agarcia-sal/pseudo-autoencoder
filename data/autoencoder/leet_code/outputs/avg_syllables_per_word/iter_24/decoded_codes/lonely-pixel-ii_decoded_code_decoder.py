from collections import defaultdict
from typing import List, Optional

class Solution:
    def findBlackPixel(self, picture: Optional[List[List[str]]], target: int) -> int:
        if picture is None or len(picture) == 0 or picture[0] is None or len(picture[0]) == 0:
            return 0

        m = len(picture)
        n = len(picture[0])
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
            pattern = ''.join(picture[r])
            if row_count[r] != target or row_patterns[pattern] != target:
                continue
            for c in range(n):
                if picture[r][c] == 'B' and col_count[c] == target:
                    lonely_pixels += 1

        return lonely_pixels