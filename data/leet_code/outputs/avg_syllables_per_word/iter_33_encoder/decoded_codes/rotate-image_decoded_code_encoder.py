class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            self.reverse_row(matrix[i])

    def reverse_row(self, row):
        left_index, right_index = 0, len(row) - 1
        while left_index < right_index:
            row[left_index], row[right_index] = row[right_index], row[left_index]
            left_index += 1
            right_index -= 1