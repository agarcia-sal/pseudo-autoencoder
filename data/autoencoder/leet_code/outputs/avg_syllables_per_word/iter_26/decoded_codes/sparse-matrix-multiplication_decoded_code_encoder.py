class Solution:
    def multiply(self, mat1, mat2):
        m = len(mat1)
        k = len(mat1[0])
        # Overwrite k with length of mat2 (number of rows in mat2)
        k = len(mat2)
        n = len(mat2[0])

        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                for p in range(k):
                    result[i][j] += mat1[i][p] * mat2[p][j]

        return result