import math

class Solution:
    def numPoints(self, darts, r):
        def distance(p1, p2):
            diff_x = p1[0] - p2[0]
            diff_y = p1[1] - p2[1]
            return math.sqrt(diff_x ** 2 + diff_y ** 2)

        def circle_center(p1, p2, r):
            d = distance(p1, p2)
            if d > 2 * r:
                return None
            a = math.sqrt(r ** 2 - (d / 2) ** 2)
            h_x = (p1[0] + p2[0]) / 2
            h_y = (p1[1] + p2[1]) / 2
            dx = (p2[1] - p1[1]) * a / d
            dy = (p2[0] - p1[0]) * a / d
            return [(h_x - dx, h_y + dy), (h_x + dx, h_y - dy)]

        def is_inside(circle, point, r):
            return distance(circle, point) <= r

        n = len(darts)
        if n == 1:
            return 1

        max_count = 1

        for i in range(n):
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