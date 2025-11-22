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
                # Check if board[i][j] ^ board[i][0] ^ board[0][j] ^ board[0][0] != 0
                if (board[i][j] ^ board[i][0] ^ board[0][j] ^ board[0][0]) != 0:
                    return -1
            rowSum += board[i][0]
            colSum += board[0][i]
            rowSwap += (board[i][0] == i % 2)
            colSwap += (board[0][i] == i % 2)

        # rowSum and colSum must be within the correct bounds
        if not (N//2 <= rowSum <= (N+1)//2):
            return -1
        if not (N//2 <= colSum <= (N+1)//2):
            return -1

        if N % 2 == 1:
            # For odd N, rowSwap and colSwap must be even or corrected
            if rowSwap % 2 == 1:
                rowSwap = N - rowSwap
            if colSwap % 2 == 1:
                colSwap = N - colSwap
        else:
            # For even N, take the minimum of swaps or their complements
            rowSwap = min(rowSwap, N - rowSwap)
            colSwap = min(colSwap, N - colSwap)

        # Each swap fixes two positions
        return (rowSwap + colSwap) // 2