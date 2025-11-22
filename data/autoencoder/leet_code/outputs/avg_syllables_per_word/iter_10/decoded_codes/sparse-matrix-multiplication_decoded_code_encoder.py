class Solution:
    def multiply(self, mat1, mat2):
        m, k1 = len(mat1), len(mat1[0])
        k2, n = len(mat2), len(mat2[0])
        assert k1 == k2, "mat1's column count must equal mat2's row count"
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                s = 0
                for p in range(k1):
                    s += mat1[i][p] * mat2[p][j]
                result[i][j] = s
        return result