from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        rows = len(board)
        if rows == 0:
            return 0
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "X":
                    if (i == 0 or board[i - 1][j] == ".") and (j == 0 or board[i][j - 1] == "."):
                        count += 1
        return count