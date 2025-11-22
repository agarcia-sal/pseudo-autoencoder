from collections import defaultdict
from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gap_counts = defaultdict(int)

        for row in wall:
            total = 0
            for brick_length in row[:-1]:
                total += brick_length
                gap_counts[total] += 1

        max_gaps = max(gap_counts.values(), default=0)

        return len(wall) - max_gaps