from collections import defaultdict
from math import inf
from fractions import Fraction

class Solution:
    def maxPoints(self, points):
        def slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            dx = x1 - x2
            if dx == 0:
                return inf
            return Fraction(y1 - y2, dx)

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

        return max_points + 1 if points else 0