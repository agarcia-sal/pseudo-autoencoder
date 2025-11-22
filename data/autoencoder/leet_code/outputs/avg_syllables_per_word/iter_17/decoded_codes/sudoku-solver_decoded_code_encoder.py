class Solution:
    def solveSudoku(self, board):
        def is_valid(board, row, col, num):
            # Check row
            for index in range(9):
                if board[row][index] == num:
                    return False
            # Check column
            for index in range(9):
                if board[index][col] == num:
                    return False
            # Check 3x3 sub-box
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
                        for num in range(1, 10):
                            string_num = str(num)
                            if is_valid(board, row, col, string_num):
                                board[row][col] = string_num
                                if solve(board):
                                    return True
                                board[row][col] = '.'
                        return False
            return True

        solve(board)