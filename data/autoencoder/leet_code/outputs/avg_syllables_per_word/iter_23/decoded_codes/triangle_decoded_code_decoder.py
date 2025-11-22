from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start from second last row and move upwards
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                value_below_left = triangle[row + 1][col]
                value_below_right = triangle[row + 1][col + 1]
                minimum_adjacent_value = min(value_below_left, value_below_right)
                triangle[row][col] += minimum_adjacent_value
        return triangle[0][0]