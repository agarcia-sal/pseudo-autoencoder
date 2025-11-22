class Solution:
    def movesToChessboard(self, board):
        N = len(board)
        rowSum = colSum = rowSwap = colSwap = 0

        for i in range(N):
            for j in range(N):
                # XOR condition to check for invalid pattern
                if (board[i][j] ^ board[i][0] ^ board[0][j] ^ board[0][0]) == 1:
                    return -1
            rowSum += board[i][0]
            colSum += board[0][i]
            rowSwap += (board[i][0] == i % 2)
            colSwap += (board[0][i] == i % 2)

        if not (N // 2 <= rowSum <= (N + 1) // 2):
            return -1
        if not (N // 2 <= colSum <= (N + 1) // 2):
            return -1

        if N % 2:
            if rowSwap % 2:
                rowSwap = N - rowSwap
            if colSwap % 2:
                colSwap = N - colSwap
        else:
            rowSwap = min(rowSwap, N - rowSwap)
            colSwap = min(colSwap, N - colSwap)

        return (rowSwap + colSwap) // 2