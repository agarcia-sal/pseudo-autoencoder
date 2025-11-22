class Solution:
    def validSquare(self, p1, p2, p3, p4):
        def squared_distance(point1, point2):
            difference_in_x = point1[0] - point2[0]
            difference_in_y = point1[1] - point2[1]
            squared_distance_value = difference_in_x * difference_in_x + difference_in_y * difference_in_y
            return squared_distance_value

        points = [p1, p2, p3, p4]
        distances = set()

        for i in range(4):
            for j in range(i + 1, 4):
                dist = squared_distance(points[i], points[j])
                if dist == 0:
                    return False
                distances.add(dist)

        return len(distances) == 2