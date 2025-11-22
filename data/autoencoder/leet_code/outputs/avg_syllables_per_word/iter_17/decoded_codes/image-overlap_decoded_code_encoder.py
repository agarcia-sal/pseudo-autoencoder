from collections import defaultdict
from typing import List, Tuple

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        points1 = self.generatePoints(img1, n)
        points2 = self.generatePoints(img2, n)

        overlap_count = defaultdict(int)
        for x1, y1 in points1:
            for x2, y2 in points2:
                dx = x2 - x1
                dy = y2 - y1
                overlap_count[(dx, dy)] += 1

        return max(overlap_count.values()) if overlap_count else 0

    def generatePoints(self, image: List[List[int]], size: int) -> List[Tuple[int, int]]:
        points_list = []
        for i in range(size):
            for j in range(size):
                if image[i][j] == 1:
                    points_list.append((i, j))
        return points_list