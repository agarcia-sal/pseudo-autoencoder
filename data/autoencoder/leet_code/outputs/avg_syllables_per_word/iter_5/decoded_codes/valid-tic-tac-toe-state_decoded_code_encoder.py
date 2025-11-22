class Solution:
    def validTicTacToe(self, board):
        countX = sum(row.count('X') for row in board)
        countO = sum(row.count('O') for row in board)
        if countX < countO or countX > countO + 1:
            return False

        def check_win(player):
            for row in board:
                if row == player * 3:
                    return True
            for col in range(3):
                if all(board[row][col] == player for row in range(3)):
                    return True
            if all(board[i][i] == player for i in range(3)):
                return True
            if all(board[i][2 - i] == player for i in range(3)):
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