from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        if m == 0:
            return []
        k = len(mat1[0])
        if k == 0:
            return []
        if len(mat2) != k:
            return []
        n = len(mat2[0]) if mat2 else 0
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                s = 0
                for p in range(k):
                    s += mat1[i][p] * mat2[p][j]
                result[i][j] = s
        return result