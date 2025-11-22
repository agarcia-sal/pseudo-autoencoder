class Solution:
    def longestLine(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        number_of_rows = len(matrix)
        number_of_columns = len(matrix[0])

        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

        maximum_length = 0

        def check(row_position, column_position, direction_x, direction_y):
            sequence_length = 0
            while 0 <= row_position < number_of_rows and 0 <= column_position < number_of_columns and matrix[row_position][column_position] == 1:
                sequence_length += 1
                row_position += direction_x
                column_position += direction_y
            return sequence_length

        for row_index in range(number_of_rows):
            for column_index in range(number_of_columns):
                if matrix[row_index][column_index] == 1:
                    for direction_x, direction_y in directions:
                        prev_row = row_index - direction_x
                        prev_col = column_index - direction_y
                        if prev_row < 0 or prev_col < 0 or prev_col >= number_of_columns or matrix[prev_row][prev_col] == 0:
                            maximum_length = max(maximum_length, check(row_index, column_index, direction_x, direction_y))

        return maximum_length