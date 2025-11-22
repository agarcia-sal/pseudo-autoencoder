from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Iterate from the second last row upwards
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Update current element by adding the minimum of the two adjacent elements in the next row
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
        return triangle[0][0]