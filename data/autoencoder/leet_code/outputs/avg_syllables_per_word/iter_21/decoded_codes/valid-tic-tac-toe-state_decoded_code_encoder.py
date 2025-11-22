from typing import List

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        countX = sum(row.count('X') for row in board)
        countO = sum(row.count('O') for row in board)

        if countX < countO or countX > countO + 1:
            return False

        def check_win(player: str) -> bool:
            # Check rows
            for row in board:
                if row == player * 3:
                    return True
            # Check columns
            for col in range(3):
                if all(board[row][col] == player for row in range(3)):
                    return True
            # Check diagonals
            if board[0][0] == board[1][1] == board[2][2] == player:
                return True
            if board[0][2] == board[1][1] == board[2][0] == player:
                return True
            return False

        winX = check_win('X')
        winO = check_win('O')

        if winX and winO:
            return False
        if winX and countX == countO:
            return False
        if winO and countX != countO:
            return False

        return True