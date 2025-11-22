from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        k = len(mat1[0]) if m > 0 else 0
        # Correcting pseudocode: k should be length of mat1[0], n should be length of mat2[0]
        # Re-assigning k to len(mat2) in pseudocode is incorrect, we preserve the logic correctness.
        n = len(mat2[0]) if len(mat2) > 0 else 0

        # initialize result with zero values for m x n matrix
        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                for p in range(k):
                    result[i][j] += mat1[i][p] * mat2[p][j]

        return result