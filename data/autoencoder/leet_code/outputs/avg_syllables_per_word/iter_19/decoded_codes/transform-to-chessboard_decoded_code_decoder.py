class Solution:
    def movesToChessboard(self, board):
        N = len(board)
        rowSum = 0
        colSum = 0
        rowSwap = 0
        colSwap = 0

        for i in range(N):
            for j in range(N):
                # Check the condition for invalid board configuration
                if (board[i][j] ^ board[i][0] ^ board[0][j] ^ board[0][0]) != 0:
                    return -1
            rowSum += board[i][0]
            colSum += board[0][i]
            # Count rows and cols that are in correct swap position with pattern i % 2
            rowSwap += (board[i][0] == i % 2)
            colSwap += (board[0][i] == i % 2)

        # Check row and column sums for validity: they must be N//2 or (N+1)//2
        if not (N // 2 <= rowSum <= (N + 1) // 2):
            return -1
        if not (N // 2 <= colSum <= (N + 1) // 2):
            return -1

        if N % 2:
            # If N is odd, fix rowSwap and colSwap if they have wrong parity
            if rowSwap % 2:
                rowSwap = N - rowSwap
            if colSwap % 2:
                colSwap = N - colSwap
        else:
            # If N is even, take the minimal swap count for rows and cols
            rowSwap = min(rowSwap, N - rowSwap)
            colSwap = min(colSwap, N - colSwap)

        return (rowSwap + colSwap) // 2