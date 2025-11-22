class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, 
                    bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)

        min_x = bx2 if ax2 >= bx2 else ax2
        max_x = ax1 if ax1 >= bx1 else bx1
        overlap_width_candidate = min_x - max_x
        overlap_width = overlap_width_candidate if overlap_width_candidate > 0 else 0

        min_y = by2 if ay2 >= by2 else ay2
        max_y = ay1 if ay1 >= by1 else by1
        overlap_height_candidate = min_y - max_y
        overlap_height = overlap_height_candidate if overlap_height_candidate > 0 else 0

        overlap_area = overlap_width * overlap_height
        total_area = area1 + area2 - overlap_area
        return total_area