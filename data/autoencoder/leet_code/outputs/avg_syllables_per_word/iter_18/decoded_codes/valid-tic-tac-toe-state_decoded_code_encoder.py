class Solution:
    def validTicTacToe(self, board: list[str]) -> bool:
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
            for c in range(3):
                if board[0][c] == player and board[1][c] == player and board[2][c] == player:
                    return True
            # Check diagonals
            if board[0][0] == player and board[1][1] == player and board[2][2] == player:
                return True
            if board[0][2] == player and board[1][1] == player and board[2][0] == player:
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