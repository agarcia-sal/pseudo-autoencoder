class Solution:
    def findMinArrowShots(self, points):
        points.sort(key=lambda x: x[1])
        arrows = 0
        last_arrow_position = float('-inf')
        for start, end in points:
            if start > last_arrow_position:
                arrows += 1
                last_arrow_position = end
        return arrows