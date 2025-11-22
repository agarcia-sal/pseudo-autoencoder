from collections import defaultdict
import math
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def slope(p1: List[int], p2: List[int]) -> float:
            if p1[0] == p2[0]:
                return math.inf
            return (p1[1] - p2[1]) / (p1[0] - p2[0])

        max_points = 0
        n = len(points)
        for i in range(n):
            slopes = defaultdict(int)
            for j in range(n):
                if i != j:
                    s = slope(points[i], points[j])
                    slopes[s] += 1
                    max_points = max(max_points, slopes[s])
        return max_points + 1 if n > 0 else 0