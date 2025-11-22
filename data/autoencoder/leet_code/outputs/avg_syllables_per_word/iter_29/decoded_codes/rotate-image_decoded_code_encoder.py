class Solution:
    def rotate(self, matrix):
        size = len(matrix)
        for i in range(size):
            for j in range(i, size):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(size):
            matrix[i].reverse()