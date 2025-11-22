class Solution:
    def validSquare(self, p1, p2, p3, p4) -> bool:
        def squared_distance(p1, p2) -> int:
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            return dx * dx + dy * dy

        points = [p1, p2, p3, p4]
        distances = set()

        for i in range(4):
            for j in range(i + 1, 4):
                dist = squared_distance(points[i], points[j])
                if dist == 0:
                    return False
                distances.add(dist)

        return len(distances) == 2