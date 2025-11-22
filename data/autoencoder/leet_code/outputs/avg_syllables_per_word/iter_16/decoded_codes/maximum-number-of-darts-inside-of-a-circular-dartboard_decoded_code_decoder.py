import math

class Solution:
    def numPoints(self, darts, r):
        def distance(p1, p2):
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            return math.sqrt(dx * dx + dy * dy)

        def circle_center(p1, p2, r):
            d = distance(p1, p2)
            if d > 2 * r:
                return None
            a = math.sqrt(r * r - (d / 2) * (d / 2))
            h = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
            dx = (p2[1] - p1[1]) * a / d
            dy = (p2[0] - p1[0]) * a / d
            return [(h[0] - dx, h[1] + dy), (h[0] + dx, h[1] - dy)]

        def is_inside(center, point, r):
            return distance(center, point) <= r

        n = len(darts)
        if n == 1:
            return 1

        max_count = 1

        for i in range(n - 1):
            for j in range(i + 1, n):
                centers = circle_center(darts[i], darts[j], r)
                if centers is not None:
                    for center in centers:
                        count = 0
                        for dart in darts:
                            if is_inside(center, dart, r):
                                count += 1
                        if count > max_count:
                            max_count = count

        return max_count