class Solution:
    def movesToChessboard(self, board):
        N = len(board)

        rowSum = 0
        colSum = 0
        rowSwap = 0
        colSwap = 0

        for i in range(N):
            for j in range(N):
                # Check XOR condition for board validity:
                if (board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]) != 0:
                    return -1
            rowSum += board[i][0]
            colSum += board[0][i]
            if board[i][0] == i % 2:
                rowSwap += 1
            if board[0][i] == i % 2:
                colSwap += 1

        half = N // 2
        half_plus = (N + 1) // 2

        if not (half <= rowSum <= half_plus):
            return -1
        if not (half <= colSum <= half_plus):
            return -1

        if N % 2 == 1:
            if rowSwap % 2 == 1:
                rowSwap = N - rowSwap
            if colSwap % 2 == 1:
                colSwap = N - colSwap
        else:
            rowSwap = min(rowSwap, N - rowSwap)
            colSwap = min(colSwap, N - colSwap)

        return (rowSwap + colSwap) // 2