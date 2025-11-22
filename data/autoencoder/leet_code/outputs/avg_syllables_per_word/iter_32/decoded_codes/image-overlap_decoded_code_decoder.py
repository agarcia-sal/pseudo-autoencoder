from collections import defaultdict
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        points1 = []
        points2 = []

        # Collect coordinates of 1s in img1
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    points1.append((i, j))

        # Collect coordinates of 1s in img2
        for i in range(n):
            for j in range(n):
                if img2[i][j] == 1:
                    points2.append((i, j))

        # Count overlaps for each translation vector
        overlap_count = defaultdict(int)
        for x1, y1 in points1:
            for x2, y2 in points2:
                dx = x2 - x1
                dy = y2 - y1
                overlap_count[(dx, dy)] += 1

        # Find the maximum overlap
        maximum_overlap = 0
        for count in overlap_count.values():
            if count > maximum_overlap:
                maximum_overlap = count

        return maximum_overlap