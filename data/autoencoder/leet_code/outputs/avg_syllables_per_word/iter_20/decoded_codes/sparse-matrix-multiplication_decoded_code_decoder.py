from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        k = len(mat1[0]) if m > 0 else 0
        if k != len(mat2):
            raise ValueError("mat1's number of columns must be equal to mat2's number of rows")
        n = len(mat2[0]) if len(mat2) > 0 else 0

        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                total = 0
                for p in range(k):
                    total += mat1[i][p] * mat2[p][j]
                result[i][j] = total
        return result