class Solution:
    def multiply(self, mat1, mat2):
        m = len(mat1)
        k = len(mat1[0])
        k = len(mat2)
        n = len(mat2[0])
        result = self.initialize_result_matrix(m, n)
        for i in range(m):
            for j in range(n):
                for p in range(k):
                    result[i][j] += mat1[i][p] * mat2[p][j]
        return result

    def initialize_result_matrix(self, m, n):
        result = []
        for _ in range(m):
            row = []
            for _ in range(n):
                row.append(0)
            result.append(row)
        return result