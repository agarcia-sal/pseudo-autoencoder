class Solution:
    def solveSudoku(self, board):
        def is_valid(board_parameter, row_parameter, col_parameter, num_parameter):
            for index_i in range(9):
                if board_parameter[row_parameter][index_i] == num_parameter:
                    return False

            for index_i in range(9):
                if board_parameter[index_i][col_parameter] == num_parameter:
                    return False

            start_row = 3 * (row_parameter // 3)
            start_col = 3 * (col_parameter // 3)

            for index_i in range(3):
                for index_j in range(3):
                    if board_parameter[start_row + index_i][start_col + index_j] == num_parameter:
                        return False

            return True

        def solve(board_parameter):
            for row in range(9):
                for col in range(9):
                    if board_parameter[row][col] == '.':
                        for num_ascii in map(str, range(1, 10)):
                            if is_valid(board_parameter, row, col, num_ascii):
                                board_parameter[row][col] = num_ascii
                                if solve(board_parameter):
                                    return True
                                board_parameter[row][col] = '.'
                        return False
            return True

        solve(board)