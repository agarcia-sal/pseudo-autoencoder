from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        k = len(mat1[0]) if mat1 else 0
        # Fix pseudocode issue: assign k from mat1's column count, not mat2's row count directly
        # but for multiplication, mat1's number of columns must equal mat2's number of rows
        assert k == len(mat2), "mat1 columns must equal mat2 rows for multiplication"
        n = len(mat2[0]) if mat2 else 0

        result = self.InitializeResultMatrix(m, n)

        for i in range(m):
            for j in range(n):
                s = 0
                for p in range(k):
                    s += mat1[i][p] * mat2[p][j]
                result[i][j] = s

        return result

    def InitializeResultMatrix(self, rows: int, columns: int) -> List[List[int]]:
        # Initialize result matrix with zeros
        return [[0] * columns for _ in range(rows)]