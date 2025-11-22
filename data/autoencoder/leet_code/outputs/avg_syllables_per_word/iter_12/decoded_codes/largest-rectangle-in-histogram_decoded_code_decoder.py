from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]  # stack stores indices, starts with sentinel -1
        max_area = 0
        heights.append(0)  # Append zero height to flush out remaining bars in stack

        for i, h in enumerate(heights):
            # While current height is less than height at top index of stack
            while stack[-1] != -1 and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area