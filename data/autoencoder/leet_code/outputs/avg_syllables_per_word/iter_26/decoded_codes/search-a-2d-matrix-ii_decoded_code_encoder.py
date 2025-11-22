class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        row, col = 0, len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            val = matrix[row][col]
            if val == target:
                return True
            elif val > target:
                col -= 1
            else:
                row += 1

        return False