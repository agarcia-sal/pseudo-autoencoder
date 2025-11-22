from collections import defaultdict
from math import inf, gcd
from typing import List, Tuple

class Solution:
    def maxPoints(self, points: List[Tuple[int, int]]) -> int:
        # Helper function to compute slope as a reduced fraction (dy, dx)
        # to avoid floating point precision issues.
        def slope(p1: Tuple[int, int], p2: Tuple[int, int]) -> Tuple[int, int]:
            x1, y1 = p1
            x2, y2 = p2
            dx = x1 - x2
            dy = y1 - y2
            if dx == 0:
                return (inf, 0)  # vertical line, use (inf, 0) as slope key
            # Normalize fraction sign and reduce it
            sign = 1 if (dy * dx) >= 0 else -1
            dy = abs(dy)
            dx = abs(dx)
            g = gcd(dy, dx)
            return (sign * (dy // g), dx // g)

        n = len(points)
        if n == 0:
            return 0

        max_points = 0

        for i in range(n):
            slopes = defaultdict(int)
            same_point = 1  # count of duplicates of points[i]
            for j in range(i + 1, n):
                if points[i] == points[j]:
                    same_point += 1
                else:
                    s = slope(points[i], points[j])
                    slopes[s] += 1

            current_max = max(slopes.values(), default=0)
            max_points = max(max_points, current_max + same_point)

        return max_points