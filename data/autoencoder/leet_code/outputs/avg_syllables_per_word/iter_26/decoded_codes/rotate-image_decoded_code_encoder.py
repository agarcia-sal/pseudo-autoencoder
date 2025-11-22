from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        size_n = len(matrix)
        for index_i in range(size_n):
            for index_j in range(index_i, size_n):
                matrix[index_i][index_j], matrix[index_j][index_i] = matrix[index_j][index_i], matrix[index_i][index_j]
        for index_i in range(size_n):
            matrix[index_i].reverse()