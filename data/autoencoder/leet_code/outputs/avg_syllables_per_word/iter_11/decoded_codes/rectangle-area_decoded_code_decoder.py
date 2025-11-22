class Solution:
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)

        min_right = ax2 if ax2 < bx2 else bx2
        max_left = ax1 if ax1 > bx1 else bx1

        overlap_width_candidate = min_right - max_left
        overlap_width = overlap_width_candidate if overlap_width_candidate > 0 else 0

        min_top = ay2 if ay2 < by2 else by2
        max_bottom = ay1 if ay1 > by1 else by1

        overlap_height_candidate = min_top - max_bottom
        overlap_height = overlap_height_candidate if overlap_height_candidate > 0 else 0

        overlap_area = overlap_width * overlap_height

        total_area = area1 + area2 - overlap_area
        return total_area