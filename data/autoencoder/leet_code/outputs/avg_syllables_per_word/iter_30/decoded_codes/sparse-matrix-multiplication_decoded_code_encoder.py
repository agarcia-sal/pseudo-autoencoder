class Solution:
    def multiply(self, mat1, mat2):
        m = len(mat1)
        k = len(mat1[0])
        # Note: The next line in pseudocode overrides k to len(mat2),
        # presumably length of mat2 rows, which should equal k from mat1 cols.
        k = len(mat2)
        n = len(mat2[0])
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                total = 0
                row1 = mat1[i]
                for p in range(k):
                    # mat1[i][p] * mat2[p][j]
                    total += row1[p] * mat2[p][j]
                result[i][j] = total
        return result