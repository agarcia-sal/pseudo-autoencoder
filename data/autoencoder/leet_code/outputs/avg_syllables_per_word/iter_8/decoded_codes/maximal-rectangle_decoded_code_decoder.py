class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
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

    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        index = 0

        while index < len(heights):
            if not stack or heights[index] >= heights[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                top_of_stack = stack.pop()
                if stack:
                    width = index - stack[-1] - 1
                else:
                    width = index
                area = heights[top_of_stack] * width
                max_area = max(max_area, area)

        while stack:
            top_of_stack = stack.pop()
            if stack:
                width = index - stack[-1] - 1
            else:
                width = index
            area = heights[top_of_stack] * width
            max_area = max(max_area, area)

        return max_area