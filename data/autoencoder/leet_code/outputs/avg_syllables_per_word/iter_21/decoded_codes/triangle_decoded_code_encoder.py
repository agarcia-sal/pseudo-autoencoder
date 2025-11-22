from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                minimum_of_adjacent = min(triangle[row + 1][col], triangle[row + 1][col + 1])
                triangle[row][col] += minimum_of_adjacent
        return triangle[0][0]