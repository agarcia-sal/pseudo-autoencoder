class Solution:
    def multiply(self, mat1, mat2):
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for p in range(k):
                val = mat1[i][p]
                for j in range(n):
                    result[i][j] += val * mat2[p][j]
        return result