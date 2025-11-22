from typing import List

class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        N = len(board)
        rowSum = 0
        colSum = 0
        rowSwap = 0
        colSwap = 0

        for i in range(N):
            for j in range(N):
                # Check the parity condition for the chessboard pattern:
                # XOR of four positions must be 0, otherwise pattern invalid
                if (board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]) != 0:
                    return -1

            rowSum += board[i][0]
            colSum += board[0][i]
            if board[i][0] == (i % 2):
                rowSwap += 1
            if board[0][i] == (i % 2):
                colSwap += 1

        # Check if the number of ones in first column and first row are valid
        if not (N // 2 <= rowSum <= (N + 1) // 2):
            return -1
        if not (N // 2 <= colSum <= (N + 1) // 2):
            return -1

        # Adjust swap counts depending on parity of N
        if N % 2 == 1:
            if rowSwap % 2 == 1:
                rowSwap = N - rowSwap
            if colSwap % 2 == 1:
                colSwap = N - colSwap
        else:
            rowSwap = min(rowSwap, N - rowSwap)
            colSwap = min(colSwap, N - colSwap)

        # Each swap fixes two rows or columns, so total moves is half the sum
        return (rowSwap + colSwap) // 2