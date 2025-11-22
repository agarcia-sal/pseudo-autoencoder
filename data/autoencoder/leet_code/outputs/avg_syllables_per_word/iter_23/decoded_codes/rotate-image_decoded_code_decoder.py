from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse each row
        for i in range(n):
            left_index, right_index = 0, n - 1
            while left_index < right_index:
                matrix[i][left_index], matrix[i][right_index] = matrix[i][right_index], matrix[i][left_index]
                left_index += 1
                right_index -= 1