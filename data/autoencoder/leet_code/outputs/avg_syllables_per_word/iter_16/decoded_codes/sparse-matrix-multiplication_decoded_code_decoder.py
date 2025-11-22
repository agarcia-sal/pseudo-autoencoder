class Solution:
    def multiply(self, mat1, mat2):
        m = len(mat1)
        k = len(mat1[0]) if mat1 else 0
        # k should match rows in mat2 for valid multiplication
        k2 = len(mat2)
        n = len(mat2[0]) if mat2 else 0
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                s = 0
                for p in range(k):
                    s += mat1[i][p] * mat2[p][j]
                result[i][j] = s
        return result