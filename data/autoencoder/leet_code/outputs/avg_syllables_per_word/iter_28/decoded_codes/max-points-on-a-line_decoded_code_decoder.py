from collections import defaultdict
from math import inf

class Solution:
    def maxPoints(self, points):
        def slope(p1, p2):
            if p1[0] == p2[0]:
                return inf
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

        return max_points + 1 if points else 0