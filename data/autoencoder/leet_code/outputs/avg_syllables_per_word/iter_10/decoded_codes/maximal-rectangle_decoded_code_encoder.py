class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            max_area = max(max_area, self.largestRectangleArea(heights))
        return max_area

    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        index = 0
        n = len(heights)
        while index < n:
            if not stack or heights[index] >= heights[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                top = stack.pop()
                area = heights[top] * (index - stack[-1] - 1 if stack else index)
                max_area = max(max_area, area)
        while stack:
            top = stack.pop()
            area = heights[top] * (n - stack[-1] - 1 if stack else n)
            max_area = max(max_area, area)
        return max_area