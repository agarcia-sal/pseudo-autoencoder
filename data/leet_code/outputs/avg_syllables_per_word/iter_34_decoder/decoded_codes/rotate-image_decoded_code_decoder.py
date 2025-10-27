class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            self.reverse_row(matrix[i])

    def reverse_row(self, row):
        start, end = 0, len(row) - 1
        while start < end:
            row[start], row[end] = row[end], row[start]
            start += 1
            end -= 1