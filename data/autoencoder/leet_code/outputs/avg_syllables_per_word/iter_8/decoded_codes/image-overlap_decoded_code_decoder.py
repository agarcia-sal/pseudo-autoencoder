from collections import defaultdict

class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)
        points1 = []
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    points1.append((i, j))
        points2 = []
        for i in range(n):
            for j in range(n):
                if img2[i][j] == 1:
                    points2.append((i, j))
        overlap_count = defaultdict(int)
        for x1, y1 in points1:
            for x2, y2 in points2:
                dx = x2 - x1
                dy = y2 - y1
                overlap_count[(dx, dy)] += 1
        return max(overlap_count.values()) if overlap_count else 0