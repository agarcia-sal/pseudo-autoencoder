class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0

        def largestRectangleArea(heights):
            stack = []
            max_area = 0
            index = 0
            while index < len(heights):
                if not stack or heights[index] >= heights[stack[-1]]:
                    stack.append(index)
                    index += 1
                else:
                    top = stack.pop()
                    width = index if not stack else index - stack[-1] - 1
                    max_area = max(max_area, heights[top] * width)
            while stack:
                top = stack.pop()
                width = index if not stack else index - stack[-1] - 1
                max_area = max(max_area, heights[top] * width)
            return max_area

        for i in range(rows):
            for j in range(cols):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            max_area = max(max_area, largestRectangleArea(heights))
        return max_area