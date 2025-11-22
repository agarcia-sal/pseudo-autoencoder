class Solution:
    def largestRectangleArea(self, heights):
        stack = [-1]  # stack holds indices; start with sentinel
        max_area = 0
        heights.append(0)  # sentinel height to flush stack at end
        for index, height in enumerate(heights):
            while stack[-1] != -1 and height < heights[stack[-1]]:
                height_value = heights[stack.pop()]
                width_value = index - stack[-1] - 1
                max_area = max(max_area, height_value * width_value)
            stack.append(index)
        return max_area