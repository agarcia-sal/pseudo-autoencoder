from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        k = len(mat1[0])
        # According to original pseudocode, the line "SET k TO the LENGTH OF mat2" seems meant to adjust k to len(mat2)
        # but since mat1's columns must match mat2's rows for multiplication, enforcing k = len(mat2)
        k = len(mat2)
        n = len(mat2[0])
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for p in range(k):
                    result[i][j] += mat1[i][p] * mat2[p][j]
        return result