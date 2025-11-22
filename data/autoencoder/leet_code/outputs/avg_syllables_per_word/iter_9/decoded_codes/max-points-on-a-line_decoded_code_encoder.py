from collections import defaultdict
from math import inf, gcd

class Solution:
    def maxPoints(self, points):
        def slope(p1, p2):
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            if dx == 0:
                return (inf, 0)
            if dy == 0:
                return (0, 0)
            sign = 1 if (dy > 0) == (dx > 0) else -1
            dy, dx = abs(dy), abs(dx)
            g = gcd(dy, dx)
            return (sign * dy // g, dx // g)

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