def maximalRectangle(matrix):
    if not matrix or not matrix[0]:
        return 0

    def largestRectangleArea(heights):
        stack = []
        max_area = 0
        for i in range(len(heights) + 1):
            h = heights[i] if i < len(heights) else 0
            while stack and h < heights[stack[-1]]:
                top = stack.pop()
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, heights[top] * w)
            stack.append(i)
        return max_area

    n = len(matrix[0])
    heights = [0] * n
    max_area = 0

    for row in matrix:
        for j in range(n):
            if row[j] == '1':
                heights[j] += 1
            else:
                heights[j] = 0
        max_area = max(max_area, largestRectangleArea(heights))

    return max_area