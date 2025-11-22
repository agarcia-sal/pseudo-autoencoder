from collections import defaultdict
from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gap_counts = defaultdict(int)

        for row in wall:
            total_length = 0
            # Exclude the last brick in each row to avoid counting the edge of the wall
            for brick in row[:-1]:
                total_length += brick
                gap_counts[total_length] += 1

        max_gaps = max(gap_counts.values(), default=0)
        number_of_rows = len(wall)
        minimum_crossed_bricks = number_of_rows - max_gaps
        return minimum_crossed_bricks