from typing import List

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def squared_distance(point1: List[int], point2: List[int]) -> int:
            horizontal_difference = point1[0] - point2[0]
            vertical_difference = point1[1] - point2[1]
            horizontal_squared = horizontal_difference * horizontal_difference
            vertical_squared = vertical_difference * vertical_difference
            return horizontal_squared + vertical_squared

        points = [p1, p2, p3, p4]
        distances = set()

        for i in range(4):
            for j in range(i + 1, 4):
                dist = squared_distance(points[i], points[j])
                if dist == 0:
                    return False  # Overlapping points means invalid square
                distances.add(dist)

        return len(distances) == 2