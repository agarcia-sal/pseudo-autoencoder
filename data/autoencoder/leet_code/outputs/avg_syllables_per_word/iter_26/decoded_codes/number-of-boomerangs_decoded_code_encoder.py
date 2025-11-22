from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        answer = 0
        for point_one in points:
            count = defaultdict(int)
            for point_two in points:
                delta_x = point_one[0] - point_two[0]
                delta_y = point_one[1] - point_two[1]
                distance_squared = delta_x * delta_x + delta_y * delta_y
                answer += count[distance_squared]
                count[distance_squared] += 1
        return answer * 2