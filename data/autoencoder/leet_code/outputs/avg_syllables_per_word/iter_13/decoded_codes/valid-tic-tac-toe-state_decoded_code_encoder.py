class Solution:
    def validTicTacToe(self, board):
        countX = 0
        for row in board:
            countX += row.count('X')

        countO = 0
        for row in board:
            countO += row.count('O')

        if countX < countO or countX > countO + 1:
            return False

        def check_win(player):
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

        if winX and winO:
            return False

        if winX and countX == countO:
            return False

        if winO and countX != countO:
            return False

        return True