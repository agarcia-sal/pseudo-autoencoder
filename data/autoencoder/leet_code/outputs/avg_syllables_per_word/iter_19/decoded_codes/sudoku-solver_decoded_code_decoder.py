from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(board: List[List[str]], row: int, col: int, num: str) -> bool:
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

        def solve(board: List[List[str]]) -> bool:
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for num in '123456789':
                            if is_valid(board, row, col, num):
                                board[row][col] = num
                                if solve(board):
                                    return True
                                board[row][col] = '.'
                        return False
            return True

        solve(board)