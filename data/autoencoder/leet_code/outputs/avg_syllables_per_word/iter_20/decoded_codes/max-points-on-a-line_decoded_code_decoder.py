from collections import defaultdict
from math import inf
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def slope(p1: List[int], p2: List[int]) -> float:
            if p1[0] == p2[0]:
                return inf
            numerator = p1[1] - p2[1]
            denominator = p1[0] - p2[0]
            return numerator / denominator

        max_points = 0
        n = len(points)
        if n == 0:
            return 0

        for i in range(n):
            slopes = defaultdict(int)
            for j in range(n):
                if i != j:
                    s = slope(points[i], points[j])
                    slopes[s] += 1
                    if slopes[s] > max_points:
                        max_points = slopes[s]

        return max_points + 1