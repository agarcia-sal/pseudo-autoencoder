from collections import defaultdict
from typing import List, Tuple

class Solution:
    def maxPoints(self, points: List[Tuple[int, int]]) -> int:
        def slope(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
            if p1[0] == p2[0]:
                return float('inf')
            return (p1[1] - p2[1]) / (p1[0] - p2[0])

        max_points = 0
        n = len(points)
        for i in range(n):
            slopes = defaultdict(int)
            for j in range(n):
                if i != j:
                    s = slope(points[i], points[j])
                    slopes[s] += 1
                    if slopes[s] > max_points:
                        max_points = slopes[s]
        if n > 0:
            return max_points + 1
        return 0