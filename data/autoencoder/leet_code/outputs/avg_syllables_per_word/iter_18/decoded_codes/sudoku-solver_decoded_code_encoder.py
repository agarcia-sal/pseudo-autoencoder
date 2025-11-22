class Solution:
    def solveSudoku(self, board):
        def is_valid(board, row, col, num):
            for index in range(9):
                if board[row][index] == num:
                    return False
            for index in range(9):
                if board[index][col] == num:
                    return False
            start_row = 3 * (row // 3)
            start_col = 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
                        return False
            return True

        def solve(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for string_number in map(str, range(1, 10)):
                            if is_valid(board, row, col, string_number):
                                board[row][col] = string_number
                                if solve(board):
                                    return True
                                board[row][col] = '.'
                        return False
            return True

        solve(board)