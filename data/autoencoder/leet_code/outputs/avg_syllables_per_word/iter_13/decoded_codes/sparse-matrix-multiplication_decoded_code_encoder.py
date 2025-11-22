from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        k = len(mat1[0])
        # The pseudocode reassigns k to len(mat2), which seems to be the inner dimension of multiplication,
        # so we must confirm k = len(mat2) to match multiplication condition.
        k = len(mat2)
        n = len(mat2[0])
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for p in range(k):
                    result[i][j] += mat1[i][p] * mat2[p][j]
        return result