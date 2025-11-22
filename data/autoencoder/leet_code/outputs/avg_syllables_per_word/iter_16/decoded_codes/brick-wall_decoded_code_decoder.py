from collections import defaultdict

class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        gap_counts = defaultdict(int)
        for row in wall:
            total = 0
            for brick in row[:-1]:
                total += brick
                gap_counts[total] += 1
        max_gaps = max(gap_counts.values(), default=0)
        return len(wall) - max_gaps