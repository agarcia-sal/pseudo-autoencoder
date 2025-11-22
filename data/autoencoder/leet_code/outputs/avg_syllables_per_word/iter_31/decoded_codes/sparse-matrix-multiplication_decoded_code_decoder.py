from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        if m == 0:
            return []
        k = len(mat1[0])
        if k == 0 or len(mat2) != k:
            return []
        n = len(mat2[0]) if len(mat2[0]) > 0 else 0

        # Initialize result matrix with zeros
        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # use local variables to avoid repeated indexing overhead
                row = mat1[i]
                # column values from mat2 to speed up access are not necessary here, direct access is enough
                sum_val = 0
                for p in range(k):
                    sum_val += row[p] * mat2[p][j]
                result[i][j] = sum_val

        return result