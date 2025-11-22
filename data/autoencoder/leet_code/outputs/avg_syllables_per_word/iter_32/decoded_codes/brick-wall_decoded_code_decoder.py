from collections import defaultdict
from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gap_counts = defaultdict(int)
        for row in wall:
            total = 0
            # Exclude the last brick in each row to not count the edge of the wall
            for brick in row[:-1]:
                total += brick
                gap_counts[total] += 1
        max_gaps = max(gap_counts.values()) if gap_counts else 0
        number_of_rows = len(wall)
        result = number_of_rows - max_gaps
        return result