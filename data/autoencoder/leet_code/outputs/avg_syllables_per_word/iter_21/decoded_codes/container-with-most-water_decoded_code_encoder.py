from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            if height[left] < height[right]:
                smaller_height = height[left]
            else:
                smaller_height = height[right]

            current_area = smaller_height * (right - left)
            if current_area > max_area:
                max_area = current_area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area