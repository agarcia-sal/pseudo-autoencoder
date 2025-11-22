class Solution:
    def movesToChessboard(self, board):
        N = len(board)
        rowSum = 0
        colSum = 0
        rowSwap = 0
        colSwap = 0

        for i in range(N):
            for j in range(N):
                # Check the XOR condition; if failed, return -1
                if (board[i][j] ^ board[i][0] ^ board[0][j] ^ board[0][0]) != 0:
                    return -1
            rowSum += board[i][0]
            colSum += board[0][i]
            # i % 2 is remainder of i divided by 2
            if board[i][0] == i % 2:
                rowSwap += 1
            if board[0][i] == i % 2:
                colSwap += 1

        halfN = N // 2
        halfN_ceil = (N + 1) // 2

        if rowSum < halfN or rowSum > halfN_ceil:
            return -1
        if colSum < halfN or colSum > halfN_ceil:
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