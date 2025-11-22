from collections import defaultdict
from typing import List

class Solution:
    def largestOverlap(self, image_one: List[List[int]], image_two: List[List[int]]) -> int:
        dimension_n = len(image_one)
        list_points_one = []
        for i in range(dimension_n):
            for j in range(dimension_n):
                if image_one[i][j] == 1:
                    list_points_one.append((i, j))
        list_points_two = []
        for i in range(dimension_n):
            for j in range(dimension_n):
                if image_two[i][j] == 1:
                    list_points_two.append((i, j))

        overlap_counter = defaultdict(int)
        for x1, y1 in list_points_one:
            for x2, y2 in list_points_two:
                difference_x = x2 - x1
                difference_y = y2 - y1
                overlap_counter[(difference_x, difference_y)] += 1

        maximum_overlap = max(overlap_counter.values(), default=0)
        return maximum_overlap