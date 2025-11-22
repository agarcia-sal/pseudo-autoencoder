from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                current_value = triangle[row][col]
                left_child = triangle[row + 1][col]
                right_child = triangle[row + 1][col + 1]
                minimum_child = left_child if left_child < right_child else right_child
                triangle[row][col] = current_value + minimum_child
        return triangle[0][0]