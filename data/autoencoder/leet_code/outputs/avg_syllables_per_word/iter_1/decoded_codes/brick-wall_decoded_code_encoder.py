from collections import defaultdict

def least_bricks(wall):
    gap_counts = defaultdict(int)
    for row in wall:
        sum_ = 0
        for brick in row[:-1]:
            sum_ += brick
            gap_counts[sum_] += 1
    max_gaps = max(gap_counts.values()) if gap_counts else 0
    return len(wall) - max_gaps