from typing import List

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        countX = sum(row.count('X') for row in board)
        countO = sum(row.count('O') for row in board)

        # The number of X's must be equal to or exactly one more than O's
        if countX < countO or countX > countO + 1:
            return False

        def check_win(player: str) -> bool:
            # Check rows
            for row in board:
                if row == player * 3:
                    return True
            # Check columns
            for col in range(3):
                if board[0][col] == player and board[1][col] == player and board[2][col] == player:
                    return True
            # Check diagonals
            if board[0][0] == player and board[1][1] == player and board[2][2] == player:
                return True
            if board[0][2] == player and board[1][1] == player and board[2][0] == player:
                return True
            return False

        winX = check_win('X')
        winO = check_win('O')

        # Both players cannot win simultaneously
        if winX and winO:
            return False
        # If X wins, X must have one more move than O
        if winX and countX == countO:
            return False
        # If O wins, X and O must have the same number of moves
        if winO and countX != countO:
            return False

        return True