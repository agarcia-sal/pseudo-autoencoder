class Solution:
    def movesToChessboard(self, board):
        N = len(board)
        rowSum = 0
        colSum = 0
        rowSwap = 0
        colSwap = 0

        # Validate board pattern and calculate sums and swaps
        for i in range(N):
            for j in range(N):
                if (board[i][j] ^ board[i][0] ^ board[0][j] ^ board[0][0]) != 0:
                    return -1
            rowSum += board[i][0]
            colSum += board[0][i]
            rowSwap += (board[i][0] == i % 2)
            colSwap += (board[0][i] == i % 2)

        halfN = N // 2
        halfN_plus = (N + 1) // 2

        # Check row and column sums constraints
        if not (halfN <= rowSum <= halfN_plus):
            return -1
        if not (halfN <= colSum <= halfN_plus):
            return -1

        # Adjust swaps based on board size parity
        if N % 2 == 1:
            if rowSwap % 2 == 1:
                rowSwap = N - rowSwap
            if colSwap % 2 == 1:
                colSwap = N - colSwap
        else:
            rowSwap = min(rowSwap, N - rowSwap)
            colSwap = min(colSwap, N - colSwap)

        # Each swap fixes two positions
        result = (rowSwap + colSwap) // 2
        return result