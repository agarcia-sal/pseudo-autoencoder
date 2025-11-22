class Solution:
    def validSquare(self, p1_list_of_integers, p2_list_of_integers, p3_list_of_integers, p4_list_of_integers):
        def squared_distance(point_one, point_two):
            dx = point_one[0] - point_two[0]
            dy = point_one[1] - point_two[1]
            return dx * dx + dy * dy

        points = [p1_list_of_integers, p2_list_of_integers, p3_list_of_integers, p4_list_of_integers]
        distances = set()

        for i in range(4):
            for j in range(i + 1, 4):
                dist = squared_distance(points[i], points[j])
                if dist == 0:
                    return False
                distances.add(dist)

        return len(distances) == 2