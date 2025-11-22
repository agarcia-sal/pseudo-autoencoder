from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0
        # Append zero to handle remaining bars
        heights.append(0)
        for i, h in enumerate(heights):
            while stack[-1] != -1 and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                area = height * width
                if max_area < area:
                    max_area = area
            stack.append(i)
        return max_area