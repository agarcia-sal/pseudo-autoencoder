class Solution:
    def validTicTacToe(self, board: list[str]) -> bool:
        countX = sum(row.count('X') for row in board)
        countO = sum(row.count('O') for row in board)
        if countX < countO or countX > countO + 1:
            return False

        def check_win(player: str) -> bool:
            for row in board:
                if row == player * 3:
                    return True
            for col in range(3):
                if board[0][col] == board[1][col] == board[2][col] == player:
                    return True
            if board[0][0] == board[1][1] == board[2][2] == player:
                return True
            if board[0][2] == board[1][1] == board[2][0] == player:
                return True
            return False

        winX, winO = check_win('X'), check_win('O')

        if winX and winO:
            return False
        if winX and countX == countO:
            return False
        if winO and countX != countO:
            return False
        return True