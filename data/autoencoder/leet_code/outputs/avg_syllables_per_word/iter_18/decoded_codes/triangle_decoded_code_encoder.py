from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                value_below_left = triangle[row + 1][col]
                value_below_right = triangle[row + 1][col + 1]
                minimum_adjacent = value_below_left if value_below_left <= value_below_right else value_below_right
                triangle[row][col] += minimum_adjacent
        return triangle[0][0]