from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        k = len(mat1[0]) if m > 0 else 0
        # According to pseudocode, k is reassigned to the length of mat2
        k = len(mat2)
        n = len(mat2[0]) if k > 0 else 0

        result = [[0] * n for _ in range(m)]

        # The pseudocode uses 1-based indexing; Python uses 0-based indexing
        # Adjust indices accordingly:
        for i in range(m):
            for j in range(n):
                for p in range(k):
                    result[i][j] += mat1[i][p] * mat2[p][j]

        return result