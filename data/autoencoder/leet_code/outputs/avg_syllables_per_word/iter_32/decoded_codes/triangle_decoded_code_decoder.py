from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start from the second last row and move upwards
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Update current element by adding the minimum of the two adjacent elements in the row below
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
        return triangle[0][0]