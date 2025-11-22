from collections import defaultdict
from typing import List
import math

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def slope(p1, p2):
            if p1[0] == p2[0]:
                return math.inf
            numerator = p1[1] - p2[1]
            denominator = p1[0] - p2[0]
            return numerator / denominator

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
        if points:
            return max_points + 1
        else:
            return 0