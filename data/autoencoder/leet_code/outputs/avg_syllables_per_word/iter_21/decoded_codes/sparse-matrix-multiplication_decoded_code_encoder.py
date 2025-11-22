from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        k = len(mat1[0]) if mat1 else 0
        # k was overwritten in pseudocode, correct is:
        # k = len(mat2) -- dimensions consistency: mat1 is m x k, mat2 is k x n
        # so mat2 should have k rows, so k = len(mat2)
        k = len(mat2)
        n = len(mat2[0]) if mat2 else 0

        result = self.initialize_result_matrix(m, n)

        for i in range(m):
            for j in range(n):
                s = 0
                for p in range(k):
                    s += mat1[i][p] * mat2[p][j]
                result[i][j] = s

        return result

    def initialize_result_matrix(self, m: int, n: int) -> List[List[int]]:
        matrix = []
        for _ in range(m):
            row = [0] * n
            matrix.append(row)
        return matrix