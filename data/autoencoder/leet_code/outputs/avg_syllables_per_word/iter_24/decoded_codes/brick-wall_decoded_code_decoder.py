from collections import defaultdict
from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gap_counts = defaultdict(int)
        for row in wall:
            total = 0
            # skip the last brick to avoid counting the right edge
            for brick in row[:-1]:
                total += brick
                gap_counts[total] += 1
        max_gaps = max(gap_counts.values(), default=0)
        return len(wall) - max_gaps