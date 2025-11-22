class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0
        for row_index in range(rows):
            for col_index in range(cols):
                if matrix[row_index][col_index] == 1:
                    heights[col_index] += 1
                else:
                    heights[col_index] = 0
            max_area = max(max_area, self.largestRectangleArea(heights))
        return max_area

    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        index = 0
        length = len(heights)
        while index < length:
            if not stack or heights[index] >= heights[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                top_of_stack = stack.pop()
                if not stack:
                    area = heights[top_of_stack] * index
                else:
                    area = heights[top_of_stack] * (index - stack[-1] - 1)
                max_area = max(max_area, area)
        while stack:
            top_of_stack = stack.pop()
            if not stack:
                area = heights[top_of_stack] * index
            else:
                area = heights[top_of_stack] * (index - stack[-1] - 1)
            max_area = max(max_area, area)
        return max_area