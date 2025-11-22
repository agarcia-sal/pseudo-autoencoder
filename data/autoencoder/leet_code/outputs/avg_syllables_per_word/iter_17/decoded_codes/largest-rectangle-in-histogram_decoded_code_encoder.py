from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0
        heights.append(0)
        for i, h in enumerate(heights):
            while stack[-1] != -1 and h < heights[stack[-1]]:
                height_value = heights[stack.pop()]
                width_value = i - stack[-1] - 1
                max_area = max(max_area, height_value * width_value)
            stack.append(i)
        return max_area