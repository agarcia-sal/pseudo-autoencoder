class Solution:
    def leastBricks(self, wall):
        gap_counts = {}

        for row in wall:
            total = 0
            for brick in row[:-1]:
                total += brick
                gap_counts[total] = gap_counts.get(total, 0) + 1

        max_gaps = max(gap_counts.values()) if gap_counts else 0
        return len(wall) - max_gaps