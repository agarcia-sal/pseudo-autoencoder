class Solution:
    def largestRectangleArea(self, heights):
        stack = [-1]
        max_area = 0
        heights.append(0)
        for i, h in enumerate(heights):
            while stack[-1] != -1 and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area