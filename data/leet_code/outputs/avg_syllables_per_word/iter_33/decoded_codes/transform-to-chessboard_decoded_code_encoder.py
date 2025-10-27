class Solution:
    def movesToChessboard(self, board: list[list[int]]) -> int:
        N = len(board)
        rowSum = colSum = rowSwap = colSwap = 0

        for i in range(N):
            for j in range(N):
                if (board[0][0] ^ board[i][0] ^ board[i][j] ^ board[0][j]) != 0:
                    return -1
            rowSum += board[i][0]
            colSum += board[0][i]
            if board[i][0] == i % 2:
                rowSwap += 1
            if board[0][i] == i % 2:
                colSwap += 1

        if not (N // 2 <= rowSum <= (N + 1) // 2):
            return -1
        if not (N // 2 <= colSum <= (N + 1) // 2):
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