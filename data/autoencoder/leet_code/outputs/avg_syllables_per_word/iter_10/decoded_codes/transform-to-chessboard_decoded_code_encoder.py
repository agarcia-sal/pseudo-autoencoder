class Solution:
    def movesToChessboard(self, board):
        N = len(board)
        rowSum = colSum = rowSwap = colSwap = 0

        for i in range(N):
            for j in range(N):
                if (board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]) != 0:
                    return -1
            rowSum += board[i][0]
            colSum += board[0][i]
            rowSwap += (board[i][0] == i % 2)
            colSwap += (board[0][i] == i % 2)

        half = N // 2
        if not (half <= rowSum <= (half + N % 2)):
            return -1
        if not (half <= colSum <= (half + N % 2)):
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