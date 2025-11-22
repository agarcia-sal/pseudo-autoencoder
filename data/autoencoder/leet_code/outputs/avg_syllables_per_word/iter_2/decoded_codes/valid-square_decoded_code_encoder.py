from typing import List

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def squared_distance(point1, point2):
            diff_x = point1[0] - point2[0]
            diff_y = point1[1] - point2[1]
            return diff_x * diff_x + diff_y * diff_y

        points = [p1, p2, p3, p4]
        distances = set()

        for i in range(4):
            for j in range(i + 1, 4):
                dist = squared_distance(points[i], points[j])
                if dist == 0:
                    return False
                distances.add(dist)

        return len(distances) == 2