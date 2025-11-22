from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            start_index, end_index = 0, n - 1
            while start_index < end_index:
                matrix[i][start_index], matrix[i][end_index] = matrix[i][end_index], matrix[i][start_index]
                start_index += 1
                end_index -= 1