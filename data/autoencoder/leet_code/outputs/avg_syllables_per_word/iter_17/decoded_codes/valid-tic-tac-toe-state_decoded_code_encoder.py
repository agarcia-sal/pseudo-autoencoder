class Solution:
    def validTicTacToe(self, board: list[str]) -> bool:
        def count_occurrences(collection: str, symbol: str) -> int:
            return collection.count(symbol)

        countX = sum(count_occurrences(row, 'X') for row in board)
        countO = sum(count_occurrences(row, 'O') for row in board)

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
            # Check main diagonal
            if all(board[i][i] == player for i in range(3)):
                return True
            # Check anti-diagonal
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