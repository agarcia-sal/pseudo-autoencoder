class Solution:
    def maxPoints(self, points):
        from math import inf
        if not points:
            return 0
        max_points = 0
        n = len(points)

        for i in range(n):
            slopes = {}
            for j in range(n):
                if i == j:
                    continue
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2:
                    s = inf
                else:
                    s = (y1 - y2) / (x1 - x2)
                slopes[s] = slopes.get(s, 0) + 1
                if slopes[s] > max_points:
                    max_points = slopes[s]

        return max_points + 1