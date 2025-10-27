from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, n = len(mat1), len(mat1[0])
        n2, p = len(mat2), len(mat2[0])
        result = [[0] * p for _ in range(m)]
        for i in range(m):
            for j in range(p):
                s = 0
                for k in range(n2):
                    s += mat1[i][k] * mat2[k][j]
                result[i][j] = s
        return result