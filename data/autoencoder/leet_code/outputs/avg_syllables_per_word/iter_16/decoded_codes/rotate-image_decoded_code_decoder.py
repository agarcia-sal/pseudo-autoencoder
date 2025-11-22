class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                temp = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = temp
        for i in range(n):
            matrix[i].reverse()