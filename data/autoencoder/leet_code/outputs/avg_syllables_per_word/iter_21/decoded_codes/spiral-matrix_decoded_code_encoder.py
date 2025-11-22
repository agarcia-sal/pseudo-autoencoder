from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for index in range(left, right + 1):
                result.append(matrix[top][index])
            top += 1

            for index in range(top, bottom + 1):
                result.append(matrix[index][right])
            right -= 1

            if top <= bottom:
                for index in range(right, left - 1, -1):
                    result.append(matrix[bottom][index])
                bottom -= 1

            if left <= right:
                for index in range(bottom, top - 1, -1):
                    result.append(matrix[index][left])
                left += 1

        return result