from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            max_area = max(max_area, self.largestRectangleArea(heights))
        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        index = 0
        n = len(heights)
        while index < n:
            if not stack or heights[index] >= heights[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                top_of_stack = stack.pop()
                width = index if not stack else index - stack[-1] - 1
                area = heights[top_of_stack] * width
                max_area = max(max_area, area)
        while stack:
            top_of_stack = stack.pop()
            width = index if not stack else index - stack[-1] - 1
            area = heights[top_of_stack] * width
            max_area = max(max_area, area)
        return max_area