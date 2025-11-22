from collections import defaultdict
from typing import List
import math

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def slope(p1: List[int], p2: List[int]) -> float:
            # Handle vertical line case
            if p1[0] == p2[0]:
                return math.inf
            # Calculate slope as (y2 - y1) / (x2 - x1)
            return (p2[1] - p1[1]) / (p2[0] - p1[0])

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
        else:
            return 0