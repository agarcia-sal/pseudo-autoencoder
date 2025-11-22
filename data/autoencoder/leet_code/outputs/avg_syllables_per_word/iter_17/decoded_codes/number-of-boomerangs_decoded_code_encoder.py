from collections import defaultdict
from typing import List

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        answer = 0
        for point_one in points:
            count_map = defaultdict(int)
            for point_two in points:
                delta_x = point_one[0] - point_two[0]
                delta_y = point_one[1] - point_two[1]
                distance_squared = delta_x * delta_x + delta_y * delta_y
                answer += count_map[distance_squared]
                count_map[distance_squared] += 1
        return answer * 2