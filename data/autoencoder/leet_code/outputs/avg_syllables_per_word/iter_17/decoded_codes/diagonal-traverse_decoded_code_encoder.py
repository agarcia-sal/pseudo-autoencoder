class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        number_of_rows = len(matrix)
        number_of_columns = len(matrix[0])
        result_list = []
        row = 0
        column = 0
        direction = 1

        for _ in range(number_of_rows * number_of_columns):
            result_list.append(matrix[row][column])
            new_row = row - 1 if direction == 1 else row + 1
            new_column = column + 1 if direction == 1 else column - 1

            if (new_row < 0 or new_row == number_of_rows or
                    new_column < 0 or new_column == number_of_columns):
                if direction == 1:
                    if new_column == number_of_columns:
                        new_row = row + 1
                        new_column = column
                    else:
                        new_row = 0
                        new_column = column + 1
                else:
                    if new_row == number_of_rows:
                        new_row = row
                        new_column = column + 1
                    else:
                        new_row = row + 1
                        new_column = 0
                direction *= -1

            row = new_row
            column = new_column

        return result_list