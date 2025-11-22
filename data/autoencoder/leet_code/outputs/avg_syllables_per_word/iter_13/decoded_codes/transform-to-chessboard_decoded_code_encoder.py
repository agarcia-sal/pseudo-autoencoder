class Solution:
    def movesToChessboard(self, board: list[list[int]]) -> int:
        N = len(board)
        rowSum = 0
        colSum = 0
        rowSwap = 0
        colSwap = 0

        for i in range(N):
            for j in range(N):
                # Check the pattern consistency using XOR logic:
                # If the four cells involved do not form a valid chessboard pattern, return -1.
                if (board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]) == 1:
                    return -1
            rowSum += board[i][0]
            colSum += board[0][i]
            # Check how many rows and columns are out of place relative to proper chessboard pattern
            if board[i][0] == i % 2:
                rowSwap += 1
            if board[0][i] == i % 2:
                colSwap += 1

        # The number of ones in first row and first column must be either N//2 or (N+1)//2
        if not (N // 2 <= rowSum <= (N + 1) // 2):
            return -1
        if not (N // 2 <= colSum <= (N + 1) // 2):
            return -1

        if N % 2 == 1:
            # For odd N, swaps must be even; adjust if not even.
            if rowSwap % 2 == 1:
                rowSwap = N - rowSwap
            if colSwap % 2 == 1:
                colSwap = N - colSwap
        else:
            # For even N, take minimal swaps needed
            rowSwap = min(rowSwap, N - rowSwap)
            colSwap = min(colSwap, N - colSwap)

        # Each swap fixes two rows/columns at once, so divide total by 2
        return (rowSwap + colSwap) // 2